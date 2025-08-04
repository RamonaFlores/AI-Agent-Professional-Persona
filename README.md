---
title: Carreer_conversational_AI_Agent_Angarita
app_file: app.py
sdk: gradio
sdk_version: 5.39.0
---

# 🤖 AI Agent Professional Persona

Un agente conversacional de IA que actúa como un profesional específico, respondiendo preguntas sobre experiencia, habilidades y proyectos de manera auténtica y personalizada.

## 📋 Tabla de Contenidos

- [🎯 ¿Qué hace esta aplicación?](#-qué-hace-esta-aplicación)
- [🚀 Deploy en Hugging Face Spaces](#-deploy-en-hugging-face-spaces)
- [⚙️ Configuración Inicial](#️-configuración-inicial)
- [🔧 Personalización para tu Perfil](#-personalización-para-tu-perfil)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🛠️ Funcionalidades Técnicas](#️-funcionalidades-técnicas)
- [📊 Herramientas del Agente](#-herramientas-del-agente)
- [🔐 Variables de Entorno](#-variables-de-entorno)
- [📝 Uso y Ejemplos](#-uso-y-ejemplos)
- [🔄 Actualización de Datos](#-actualización-de-datos)
- [🐛 Solución de Problemas](#-solución-de-problemas)
- [🤝 Contribuciones](#-contribuciones)

## 🎯 ¿Qué hace esta aplicación?

Esta aplicación crea un **agente conversacional profesional** que:

- **Actúa como tu representante digital** en tu sitio web personal
- **Responde preguntas sobre tu experiencia** de manera auténtica
- **Facilita conexiones profesionales** con visitantes interesados
- **Registra interacciones importantes** para seguimiento
- **Mantiene un tono profesional** consistente con tu personalidad

### Casos de uso ideales:
- **Profesionales independientes** que quieren automatizar consultas iniciales
- **Consultores** que reciben muchas preguntas repetitivas
- **Desarrolladores** que quieren mostrar su experiencia de forma interactiva
- **Cualquier profesional** que busca generar leads cualificados

## 🚀 Deploy en Hugging Face Spaces

### Deploy Automático (Recomendado)

1. **Fork este repositorio** en tu cuenta de GitHub
2. **Sube tu información personal** (ver sección de personalización)
3. **Configura las variables de entorno** en Hugging Face
4. **El deploy se hace automáticamente** cuando subas cambios

### Deploy Manual

```bash
# Clona el repositorio
git clone <tu-repositorio>

# Instala dependencias
pip install -r requirements.txt

# Configura variables de entorno
cp .env.example .env
# Edita .env con tus API keys

# Ejecuta localmente
python app.py

# Para deploy en Hugging Face
# Sube el código a tu repositorio de GitHub
# Conecta con Hugging Face Spaces
```

## ⚙️ Configuración Inicial

### 1. Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### 2. Configuración de Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# OpenAI API Key (requerido)
OPENAI_API_KEY=sk-tu-api-key-de-openai

# Pushover Keys (opcional, para notificaciones)
PUSHOVER_USER_KEY=tu-pushover-user-key
PUSHOVER_API_KEY=tu-pushover-api-key
```

### 3. Estructura de Archivos Personales

```
me/
├── linkedin.pdf      # Tu perfil de LinkedIn en PDF
└── summary.txt       # Tu resumen profesional en texto
```

## 🔧 Personalización para tu Perfil

### Paso 1: Preparar tu Información

#### A. Exportar LinkedIn a PDF
1. Ve a tu perfil de LinkedIn
2. Imprime la página (Ctrl+P / Cmd+P)
3. Guarda como PDF
4. Coloca el archivo en `me/linkedin.pdf`

#### B. Crear tu Resumen Profesional
Crea un archivo `me/summary.txt` con:

```txt
Juan José Angarita Yela
Desarrollador Full Stack con 5+ años de experiencia

EXPERIENCIA:
- Senior Developer en TechCorp (2022-presente)
- Full Stack Developer en StartupXYZ (2020-2022)
- Junior Developer en DevStudio (2018-2020)

HABILIDADES:
- Frontend: React, Vue.js, TypeScript
- Backend: Python, Node.js, Django
- Base de datos: PostgreSQL, MongoDB
- DevOps: Docker, AWS, CI/CD

EDUCACIÓN:
- Ingeniería en Sistemas, Universidad XYZ
- Certificaciones: AWS Solutions Architect, Google Cloud

PROYECTOS DESTACADOS:
- E-commerce platform con 10k+ usuarios
- API REST para fintech startup
- Sistema de gestión empresarial

INTERESES:
- Inteligencia Artificial
- Arquitectura de software
- Open Source
```

### Paso 2: Personalizar el Código

#### A. Cambiar el Nombre en `app.py`

```python
class Me:
    def __init__(self):
        self.name="TU NOMBRE COMPLETO"  # Cambia aquí
        # ... resto del código
```

#### B. Ajustar el Prompt del Sistema

En el método `system_prompt()` puedes modificar:

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

    # Puedes agregar instrucciones específicas aquí
    - Always mention your expertise in [TU ÁREA]
    - Highlight your experience with [TECNOLOGÍAS ESPECÍFICAS]
    - Emphasize your passion for [INTERESES PARTICULARES]

    # ... resto del prompt
    """
    return system_prompt
```

### Paso 3: Personalizar Herramientas (Opcional)

#### A. Modificar Notificaciones Pushover

Si quieres cambiar el formato de las notificaciones:

```python
def record_user_details(email, name="Name not provided", notes="not provided"):
    """Tool to record user details """
    message = f"""
    🎯 NUEVO INTERESADO EN TU PERFIL
    
    👤 Nombre: {name}
    📧 Email: {email}
    📝 Notas: {notes}
    
    ⏰ Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    """
    pushover_notification(message)
    return {"recorded": "Ok"}
```

#### B. Agregar Nuevas Herramientas

Para agregar funcionalidades adicionales:

```python
def record_project_inquiry(project_type, budget, timeline):
    """Registra consultas sobre proyectos específicos"""
    message = f"Proyecto: {project_type}, Presupuesto: {budget}, Timeline: {timeline}"
    pushover_notification(message)
    return {"recorded": "Project inquiry logged"}

# Agregar a la lista de herramientas
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

## 📁 Estructura del Proyecto

```
AI-Agent-Professional-Persona/
├── app.py                    # Aplicación principal
├── requirements.txt          # Dependencias Python
├── pyproject.toml           # Configuración del proyecto
├── uv.lock                  # Lock file de dependencias
├── .env                     # Variables de entorno (crear)
├── README.md               # Este archivo
├── persona.ipynb           # Notebook de desarrollo
└── me/                     # Carpeta con información personal
    ├── linkedin.pdf        # Perfil de LinkedIn
    └── summary.txt         # Resumen profesional
```

## 🛠️ Funcionalidades Técnicas

### Arquitectura del Sistema

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Gradio UI     │    │   OpenAI API    │    │   Pushover API  │
│   (Frontend)    │◄──►│   (LLM Core)    │◄──►│   (Notificaciones)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Reader    │    │   Tool Handler  │    │   File Storage  │
│   (LinkedIn)    │    │   (Functions)   │    │   (Logs)        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Flujo de Procesamiento

1. **Usuario envía mensaje** → Gradio UI
2. **Sistema construye contexto** → PDF + Summary + Historial
3. **OpenAI procesa** → LLM con herramientas disponibles
4. **Herramientas se ejecutan** → Registro de datos/notificaciones
5. **Respuesta generada** → Basada en perfil personal
6. **UI actualiza** → Conversación continua

## 📊 Herramientas del Agente

### 1. `record_user_details`
**Propósito:** Registrar visitantes interesados

**Cuándo se usa:**
- Alguien proporciona su email
- Menciona interés en colaborar
- Solicita más información

**Datos registrados:**
- Email del visitante
- Nombre (si proporcionado)
- Notas de la conversación

### 2. `record_unknown_question`
**Propósito:** Registrar preguntas no respondidas

**Cuándo se usa:**
- Pregunta fuera del contexto profesional
- Información no disponible en el perfil
- Consultas técnicas muy específicas

**Beneficios:**
- Identificar gaps en tu información
- Mejorar el perfil profesional
- Entender qué preguntan los visitantes

## 🔐 Variables de Entorno

### Requeridas

```env
OPENAI_API_KEY=sk-...
```
- **Obtener en:** https://platform.openai.com/api-keys
- **Uso:** Procesamiento de lenguaje natural
- **Costo:** ~$0.01-0.10 por conversación

### Opcionales

```env
PUSHOVER_USER_KEY=u_...
PUSHOVER_API_KEY=token_...
```
- **Obtener en:** https://pushover.net/
- **Uso:** Notificaciones push de interacciones
- **Alternativa:** Email, Slack, Discord webhooks

## 📝 Uso y Ejemplos

### Ejemplos de Conversaciones

#### Pregunta sobre experiencia:
```
Usuario: "¿Cuántos años de experiencia tienes en React?"
Agente: "Tengo 3 años de experiencia desarrollando aplicaciones con React. He trabajado en proyectos que incluyen e-commerce, dashboards administrativos y aplicaciones móviles híbridas. Mi experiencia incluye React Hooks, Context API, Redux y integración con APIs REST."
```

#### Consulta sobre proyectos:
```
Usuario: "¿Qué tipo de proyectos has desarrollado?"
Agente: "He desarrollado una variedad de proyectos, desde aplicaciones web empresariales hasta soluciones de e-commerce. Mi proyecto más destacado fue una plataforma de gestión de inventarios que procesaba más de 10,000 transacciones diarias. También he trabajado en sistemas de análisis de datos y APIs para fintech."
```

#### Solicitud de contacto:
```
Usuario: "Me interesa trabajar contigo, mi email es juan@empresa.com"
Agente: "¡Excelente! Me encantaría explorar oportunidades de colaboración. He registrado tu información y me pondré en contacto contigo pronto para discutir los detalles de tu proyecto. Mientras tanto, ¿podrías contarme un poco más sobre lo que tienes en mente?"
```

### Comandos Útiles

```bash
# Ejecutar localmente
python app.py

# Ejecutar con puerto específico
python app.py --port 8080

# Ejecutar con debug
python app.py --debug

# Limpiar caché de Gradio
rm -rf ~/.cache/gradio
```

## 🔄 Actualización de Datos

### Actualizar Información del Perfil

1. **Reemplazar `me/linkedin.pdf`** con tu perfil actualizado
2. **Editar `me/summary.txt`** con información nueva
3. **Reiniciar la aplicación** para cargar cambios

### Actualizar Prompt del Sistema

```python
# En app.py, método system_prompt()
def system_prompt(self):
    # Agregar nuevas instrucciones
    additional_instructions = """
    - Siempre menciona tu experiencia en [NUEVA TECNOLOGÍA]
    - Destaca tu trabajo en [NUEVO PROYECTO]
    - Enfatiza tu interés en [NUEVA ÁREA]
    """
    
    system_prompt = f"""
    {existing_prompt}
    {additional_instructions}
    """
    return system_prompt
```

### Agregar Nuevas Herramientas

```python
# 1. Definir nueva función
def record_meeting_request(date, topic):
    pushover_notification(f"Reunión solicitada: {topic} para {date}")
    return {"recorded": "Meeting request logged"}

# 2. Crear JSON de herramienta
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

# 3. Agregar a lista de herramientas
tools.append({"type": "function", "function": meeting_request_json})
```

## 🐛 Solución de Problemas

### Problemas Comunes

#### 1. Error de API Key
```
Error: Invalid API key
```
**Solución:**
- Verificar que `OPENAI_API_KEY` esté correcta
- Verificar que tenga saldo en la cuenta
- Verificar que la key tenga permisos de chat

#### 2. Error de PDF
```
Error: Could not read PDF
```
**Solución:**
- Verificar que `me/linkedin.pdf` existe
- Asegurar que el PDF no esté corrupto
- Verificar permisos de lectura

#### 3. Error de Pushover
```
Error: Pushover notification failed
```
**Solución:**
- Verificar `PUSHOVER_USER_KEY` y `PUSHOVER_API_KEY`
- Verificar conexión a internet
- Las notificaciones son opcionales, la app funciona sin ellas

#### 4. Gradio Cache Issues
```
Error: Old Space redirects
```
**Solución:**
```bash
# Limpiar caché
rm -rf ~/.cache/gradio

# O usar script automático
python deploy_new_space.py nuevo-nombre-space
```

### Debug Mode

Para activar modo debug:

```python
# En app.py, línea final
gr.ChatInterface(me.chat, type="messages").launch(
    share=True,
    debug=True  # Agregar esta línea
)
```

### Logs Detallados

```python
# Agregar logging detallado
import logging
logging.basicConfig(level=logging.DEBUG)

# En la función handle_tool_calls
def handle_tool_calls(self, tool_calls):
    logging.debug(f"Tool calls received: {tool_calls}")
    # ... resto del código
```

## 🤝 Contribuciones

### Cómo Contribuir

1. **Fork el repositorio**
2. **Crea una rama** para tu feature
3. **Haz tus cambios**
4. **Añade tests** si es necesario
5. **Envía un Pull Request**

### Mejoras Sugeridas

- [ ] Integración con CRM (HubSpot, Salesforce)
- [ ] Analytics de conversaciones
- [ ] Múltiples idiomas
- [ ] Integración con calendario
- [ ] Chatbot con memoria de conversación
- [ ] Exportación de leads a CSV
- [ ] Dashboard de métricas
- [ ] Integración con LinkedIn API

### Reportar Bugs

1. **Verificar** que el bug no esté ya reportado
2. **Crear issue** con descripción detallada
3. **Incluir** logs y pasos para reproducir
4. **Especificar** versión y entorno

---

## 📞 Soporte

- **Issues:** Usa GitHub Issues para bugs y features
- **Discussions:** Para preguntas generales
- **Email:** [tu-email@dominio.com]

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles.

---

**¿Te gustó este proyecto? ¡Dale una ⭐ en GitHub!**
