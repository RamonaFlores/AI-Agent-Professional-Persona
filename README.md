---
title: Carreer_conversational_AI_Agent_Angarita
app_file: app.py
sdk: gradio
sdk_version: 5.39.0
---

# 🤖 AI Agent Professional Persona

Hello! I'm Juan José Angarita Yela and today I present to you:

A conversational AI agent that acts as a specific professional, answering questions about experience, skills, and projects in an authentic and personalized manner.

## 📋 Table of Contents

- [🎯 What does this application do?](#-what-does-this-application-do)
- [🚀 Deploy on Hugging Face Spaces](#-deploy-on-hugging-face-spaces)
- [⚙️ Initial Configuration](#️-initial-configuration)
- [🔧 Customization for Your Profile](#-customization-for-your-profile)
- [📁 Project Structure](#-project-structure)
- [🛠️ Technical Features](#️-technical-features)
- [📊 Agent Tools](#-agent-tools)
- [🔐 Environment Variables](#-environment-variables)
- [📝 Usage and Examples](#-usage-and-examples)
- [🔄 Data Updates](#-data-updates)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributions](#-contributions)

## 🎯 What does this application do?

This application creates a **professional conversational agent** that:

- **Acts as your digital representative** on your personal website
- **Answers questions about your experience** authentically
- **Facilitates professional connections** with interested visitors
- **Records important interactions** for follow-up
- **Maintains a professional tone** consistent with your personality

### Ideal use cases:
- **Independent professionals** who want to automate initial inquiries
- **Consultants** who receive many repetitive questions
- **Developers** who want to showcase their experience interactively
- **Any professional** looking to generate qualified leads

## 🚀 Deploy on Hugging Face Spaces

### Automatic Deploy (Recommended)

1. **Fork this repository** to your GitHub account
2. **Upload your personal information** (see customization section)
3. **Configure environment variables** in Hugging Face
4. **Deploy happens automatically** when you push changes

### Manual Deploy

```bash
# Clone the repository
git clone <your-repository>

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys

# Run locally
python app.py

# For Hugging Face deploy
# Push code to your GitHub repository
# Connect with Hugging Face Spaces
```

## ⚙️ Initial Configuration

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI API Key (required)
OPENAI_API_KEY=sk-your-openai-api-key

# Pushover Keys (optional, for notifications)
PUSHOVER_USER_KEY=your-pushover-user-key
PUSHOVER_API_KEY=your-pushover-api-key
```

### 3. Personal Files Structure

```
me/
├── linkedin.pdf      # Your LinkedIn profile in PDF
└── summary.txt       # Your professional summary in text
```

## 🔧 Customization for Your Profile

### Step 1: Prepare Your Information

#### A. Export LinkedIn to PDF
1. Go to your LinkedIn profile
2. Print the page (Ctrl+P / Cmd+P)
3. Save as PDF
4. Place the file in `me/linkedin.pdf`

#### B. Create Your Professional Summary
Create a `me/summary.txt` file with:

```txt
Juan José Angarita Yela
Full Stack Developer with 5+ years of experience

EXPERIENCE:
- Senior Developer at TechCorp (2022-present)
- Full Stack Developer at StartupXYZ (2020-2022)
- Junior Developer at DevStudio (2018-2020)

SKILLS:
- Frontend: React, Vue.js, TypeScript
- Backend: Python, Node.js, Django
- Database: PostgreSQL, MongoDB
- DevOps: Docker, AWS, CI/CD

EDUCATION:
- Systems Engineering, XYZ University
- Certifications: AWS Solutions Architect, Google Cloud

HIGHLIGHTED PROJECTS:
- E-commerce platform with 10k+ users
- REST API for fintech startup
- Enterprise management system

INTERESTS:
- Artificial Intelligence
- Software Architecture
- Open Source
```

### Step 2: Customize the Code

#### A. Change the Name in `app.py`

```python
class Me:
    def __init__(self):
        self.name="YOUR FULL NAME"  # Change here
        # ... rest of the code
```

#### B. Adjust the System Prompt

In the `system_prompt()` method you can modify:

```python
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

    # You can add specific instructions here
    - Always mention your expertise in [YOUR AREA]
    - Highlight your experience with [SPECIFIC TECHNOLOGIES]
    - Emphasize your passion for [PARTICULAR INTERESTS]

    # ... rest of the prompt
    """
    return system_prompt
```

### Step 3: Customize Tools (Optional)

#### A. Modify Pushover Notifications

If you want to change the notification format:

```python
def record_user_details(email, name="Name not provided", notes="not provided"):
    """Tool to record user details """
    message = f"""
    🎯 NEW INTERESTED PERSON IN YOUR PROFILE
    
    👤 Name: {name}
    📧 Email: {email}
    📝 Notes: {notes}
    
    ⏰ Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    """
    pushover_notification(message)
    return {"recorded": "Ok"}
```

#### B. Add New Tools

To add additional functionalities:

```python
def record_project_inquiry(project_type, budget, timeline):
    """Records specific project inquiries"""
    message = f"Project: {project_type}, Budget: {budget}, Timeline: {timeline}"
    pushover_notification(message)
    return {"recorded": "Project inquiry logged"}

# Add to the tools list
project_inquiry_json = {
    "name": "record_project_inquiry",
    "description": "Use when someone asks about hiring you for a project",
    "parameters": {
        "type": "object",
        "properties": {
            "project_type": {"type": "string", "description": "Type of project"},
            "budget": {"type": "string", "description": "Budget range"},
            "timeline": {"type": "string", "description": "Project timeline"}
        },
        "required": ["project_type"]
    }
}
```

## 📁 Project Structure

```
AI-Agent-Professional-Persona/
├── app.py                    # Main application
├── requirements.txt          # Python dependencies
├── pyproject.toml           # Project configuration
├── uv.lock                  # Dependency lock file
├── .env                     # Environment variables (create)
├── README.md               # This file
├── persona.ipynb           # Development notebook
└── me/                     # Folder with personal information
    ├── linkedin.pdf        # LinkedIn profile
    └── summary.txt         # Professional summary
```

## 🛠️ Technical Features

### System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Gradio UI     │    │   OpenAI API    │    │   Pushover API  │
│   (Frontend)    │◄──►│   (LLM Core)    │◄──►│   (Notifications)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Reader    │    │   Tool Handler  │    │   File Storage  │
│   (LinkedIn)    │    │   (Functions)   │    │   (Logs)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Processing Flow

1. **User sends message** → Gradio UI
2. **System builds context** → PDF + Summary + History
3. **OpenAI processes** → LLM with available tools
4. **Tools execute** → Data recording/notifications
5. **Response generated** → Based on personal profile
6. **UI updates** → Continuous conversation

## 📊 Agent Tools

### 1. `record_user_details`
**Purpose:** Record interested visitors

**When used:**
- Someone provides their email
- Mentions interest in collaboration
- Requests more information

**Data recorded:**
- Visitor's email
- Name (if provided)
- Conversation notes

### 2. `record_unknown_question`
**Purpose:** Record unanswered questions

**When used:**
- Question outside professional context
- Information not available in profile
- Very specific technical queries

**Benefits:**
- Identify gaps in your information
- Improve professional profile
- Understand what visitors ask

## 🔐 Environment Variables

### Required

```env
OPENAI_API_KEY=sk-...
```
- **Get at:** https://platform.openai.com/api-keys
- **Use:** Natural language processing
- **Cost:** ~$0.01-0.10 per conversation

### Optional

```env
PUSHOVER_USER_KEY=u_...
PUSHOVER_API_KEY=token_...
```
- **Get at:** https://pushover.net/
- **Use:** Push notifications of interactions
- **Alternative:** Email, Slack, Discord webhooks

## 📝 Usage and Examples

### Conversation Examples

#### Question about experience:
```
User: "How many years of experience do you have in React?"
Agent: "I have 3 years of experience developing applications with React. I've worked on projects including e-commerce, administrative dashboards, and hybrid mobile applications. My experience includes React Hooks, Context API, Redux, and REST API integration."
```

#### Project inquiry:
```
User: "What type of projects have you developed?"
Agent: "I've developed a variety of projects, from enterprise web applications to e-commerce solutions. My most outstanding project was an inventory management platform that processed more than 10,000 daily transactions. I've also worked on data analysis systems and APIs for fintech."
```

#### Contact request:
```
User: "I'm interested in working with you, my email is juan@company.com"
Agent: "Excellent! I'd love to explore collaboration opportunities. I've recorded your information and will contact you soon to discuss the details of your project. Meanwhile, could you tell me a bit more about what you have in mind?"
```

### Useful Commands

```bash
# Run locally
python app.py

# Run with specific port
python app.py --port 8080

# Run with debug
python app.py --debug

# Clear Gradio cache
rm -rf ~/.cache/gradio
```

## 🔄 Data Updates

### Update Profile Information

1. **Replace `me/linkedin.pdf`** with your updated profile
2. **Edit `me/summary.txt`** with new information
3. **Restart the application** to load changes

### Update System Prompt

```python
# In app.py, system_prompt() method
def system_prompt(self):
    # Add new instructions
    additional_instructions = """
    - Always mention your experience in [NEW TECHNOLOGY]
    - Highlight your work on [NEW PROJECT]
    - Emphasize your interest in [NEW AREA]
    """
    
    system_prompt = f"""
    {existing_prompt}
    {additional_instructions}
    """
    return system_prompt
```

### Add New Tools

```python
# 1. Define new function
def record_meeting_request(date, topic):
    pushover_notification(f"Meeting requested: {topic} for {date}")
    return {"recorded": "Meeting request logged"}

# 2. Create tool JSON
meeting_request_json = {
    "name": "record_meeting_request",
    "description": "Use when someone requests a meeting",
    "parameters": {
        "type": "object",
        "properties": {
            "date": {"type": "string", "description": "Preferred date"},
            "topic": {"type": "string", "description": "Meeting topic"}
        },
        "required": ["topic"]
    }
}

# 3. Add to tools list
tools.append({"type": "function", "function": meeting_request_json})
```

## 🐛 Troubleshooting

### Common Problems

#### 1. API Key Error
```
Error: Invalid API key
```
**Solution:**
- Verify `OPENAI_API_KEY` is correct
- Verify account has balance
- Verify key has chat permissions

#### 2. PDF Error
```
Error: Could not read PDF
```
**Solution:**
- Verify `me/linkedin.pdf` exists
- Ensure PDF is not corrupted
- Verify read permissions

#### 3. Pushover Error
```
Error: Pushover notification failed
```
**Solution:**
- Verify `PUSHOVER_USER_KEY` and `PUSHOVER_API_KEY`
- Verify internet connection
- Notifications are optional, app works without them

#### 4. Gradio Cache Issues
```
Error: Old Space redirects
```
**Solution:**
```bash
# Clear cache
rm -rf ~/.cache/gradio

# Or use automatic script
python deploy_new_space.py new-space-name
```

### Debug Mode

To enable debug mode:

```python
# In app.py, final line
gr.ChatInterface(me.chat, type="messages").launch(
    share=True,
    debug=True  # Add this line
)
```

### Detailed Logs

```python
# Add detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# In handle_tool_calls function
def handle_tool_calls(self, tool_calls):
    logging.debug(f"Tool calls received: {tool_calls}")
    # ... rest of the code
```

## 🤝 Contributions

### How to Contribute

1. **Fork the repository**
2. **Create a branch** for your feature
3. **Make your changes**
4. **Add tests** if necessary
5. **Send a Pull Request**

### Suggested Improvements

- [ ] CRM integration (HubSpot, Salesforce)
- [ ] Conversation analytics
- [ ] Multiple languages
- [ ] Calendar integration
- [ ] Chatbot with conversation memory
- [ ] Lead export to CSV
- [ ] Metrics dashboard
- [ ] LinkedIn API integration

### Report Bugs

1. **Verify** the bug isn't already reported
2. **Create issue** with detailed description
3. **Include** logs and steps to reproduce
4. **Specify** version and environment

---

## 📞 Support

- **Issues:** Use GitHub Issues for bugs and features
- **Discussions:** For general questions
- **Email:** [your-email@domain.com]

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

**Did you like this project? Give it a ⭐ on GitHub!**
