from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import requests
from pypdf import PdfReader
import gradio as gr

load_dotenv(override=True)
pushover_user_key = os.getenv("PUSHOVER_USER_KEY")

pushover_api_key = os.getenv("PUSHOVER_API_KEY")
def pushover_notification(message):
    requests.post(
        "https://api.pushover.net/1/messages.json",
    data={
        "user":pushover_user_key,

        "token":pushover_api_key,

        "message":message
        }
    )

def record_user_details(email, name="Name not provided",notes="not provided"):
    """Tool to record user details """
    pushover_notification(f"Recording user details for {name} with email {email} and notes {notes}")
    return {"recorded": "Ok"}

def record_unknown_question(question):
    """This will send a pushover notification to us , notifying us that the agent
    was asked an unknown question"""
    pushover_notification(f"Recording {question}, I could not answer it")
    return {"recorded": "Ok"}

#The following code is boiler plate code for the agent, it's not something you'll typically use
#since frameworks already have this built in

#The LLM will use this to decide wether it's appropiate or not to use this tool
record_user_details_json={
    "name": "record_user_details",
    "description": "Use this tool to record everytime a user is interested in being in touch and provided an email address",
    "parameters": {
        "type":"object",
        "properties": {
            "email": {

                "type": "string",

                "description": "the email address of the user"
            },
            "name": {

                "type": "string",

                "description": "the user's name, if they provided it"
            },
            "notes": {

                "type": "string",

                "description": "Any additional notes , information or such  about the conversation the user provided that's worth recording"

            }
        },
        "required": ["email"],
        "additionalProperties": False
        
        }
}
record_unknown_question_json = {
    "name": "record_unknown_question",
    "description": "Always use this tool to record any question that couldn't be answered as you didn't know the answer",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question that couldn't be answered"
            },
        },
        "required": ["question"],
        "additionalProperties": False
    }
}
#A list with the tools that the agent can use
tools=[{"type":"function","function":record_user_details_json},
{"type":"function","function":record_unknown_question_json}]

class Me:
    def __init__(self):
        self.name="Juan José Angarita Yela"
        self.openai=OpenAI()
        reader=PdfReader("me/linkedin.pdf")
        self.linkedin_text=[]
        for page in reader.pages:
            text=page.extract_text()
            if text:
                self.linkedin_text.append(text)
        with open("me/summary.txt","r",encoding="utf-8") as f:
            self.summary=f.read()
    
    #Again we'll never have to do this with a framework, but it's the vainilla way to turn a json object into a function call
    def handle_tool_calls(self,tool_calls):
        """This function is used to handle the tool calls from the agent"""
        results=[]
        for tool_call in tool_calls:
            tool_name=tool_call.function.name
            arguments=json.loads(tool_call.function.arguments)
            print(f"The following tool was called: {tool_name}", flush=True)
            #we use globals() to get the tool function from the global namespace, a clever way to avoid using if statements
            tool=globals()[tool_name]
            #we use the tool function if it exists, otherwise we return an error
            result=tool(**arguments) if tool else {"error": f"Unknown tool: {tool_name}"}
            results.append({"role": "tool", "content": json.dumps(result),"tool_call_id": tool_call.id})
        return results
    def system_prompt(self):
        system_prompt = f"""
        You are acting as {self.name}, engaging professionally with visitors on {self.name}'s personal website.

        Your primary responsibility is to accurately and authentically represent {self.name}'s professional persona, answering questions related specifically to:
        - Career achievements
        - Professional background
        - Skills and expertise
        - Work experience
        - Education and certifications
        - Current projects and interests

        Always maintain a tone that is professional, courteous, engaging, and reflective of {self.name}'s communication style, as if addressing potential clients, collaborators, or employers who have visited the website.

        You have been provided with the following detailed resources to assist in your responses:

        ## Professional Summary:
        {self.summary}

        ## LinkedIn Profile Information:
        {self.linkedin_text}

        Guidelines for interactions:
        - When asked a question within your provided context, answer accurately and concisely, highlighting relevant experiences and skills.
        - If you encounter a question you cannot confidently answer, immediately record it using your `record_unknown_question` tool, even if the question seems trivial or unrelated to professional details.
        - Encourage deeper engagement by suggesting visitors provide their email for further communication. When visitors share their email, record it promptly using your `record_user_details` tool.

        Remember, your goal is to facilitate meaningful connections and professional opportunities, guiding visitors to take the next step in reaching out directly to {self.name} via email or another provided channel.

        Stay consistently in character as {self.name} throughout every interaction.
        """
        return system_prompt


    def chat(self,message, history):
        messages = [{"role": "system", "content": self.system_prompt()}] + history + [{"role": "user", "content": message}]
        done = False
        #Loop until the conversation is done
        while not done:

            # This is the call to the LLM - see that we pass in the tools json

            #we pass the same old stuff as before, but now we pass the tools json !!
            #this lets the llm know that it can call the tools we defined above
            response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)

            finish_reason = response.choices[0].finish_reason
            
            # If the LLM wants to call a tool, we do that!
            
            if finish_reason=="tool_calls":
                message = response.choices[0].message
                #we plug the tool calls into the handle_tool_calls function
                tool_calls = message.tool_calls
                #and this is where the magic happens, we call the tool functions
                results = self.handle_tool_calls(tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        return response.choices[0].message.content
if __name__ == "__main__":
    me = Me()
    # Configuración para crear un nuevo Space en Hugging Face
    # Cambia "tu-nuevo-space-name" por el nombre que quieras para tu nuevo Space
    gr.ChatInterface(me.chat, type="messages").launch(
        share=True,  # Esto creará un link público
        # Descomenta la siguiente línea y cambia el nombre para crear un nuevo Space
        # space_name="tu-nuevo-space-name"
    )