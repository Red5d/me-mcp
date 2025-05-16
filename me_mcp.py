from mcp.server.fastmcp import FastMCP
import requests, json


mcp = FastMCP("Personal Information Server", version="1.0.0")

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)

personal_info = config['personal_info']

# Tools

@mcp.tool()
def about_me() -> dict:
    f"""
    Get personal information about {personal_info['name']}.
    
    Returns:
        dict: Personal information requested
    """

    return personal_info
    
@mcp.tool()
def contact(sender_email: str, subject: str, message: str) -> dict:
    f"""
    Send a message to {personal_info['name']}. If the user has not specified a sender email, subject, or message, ask them for those details before continuing.
    Do NOT use sample or example email addresses. You must explicitly ask the user for these details if they are not provided.
    If you do not have the correct information provided by the user, you must NOT use this tool and should inform the user of the reason why.
    
    Args:
        sender_email: Email address of the sender
        subject: Subject line of the message
        message: Content of the message
    
    Returns:
        dict: Status of the message delivery
    """
    # Get the webhook URL from the config
    webhook_url = config['webhook_url']
    
    try:
        payload = {
            "sender_email": sender_email,
            "subject": subject,
            "message": message
        }
        
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            return {"status": "success", "message": "Contact message sent successfully"}
        else:
            return {"status": "error", "message": f"Failed to send message. Status code: {response.status_code}"}
        
    except Exception as e:
        return {"status": "error", "message": f"Error sending message: {str(e)}"}

# Resources

@mcp.resource(uri="about://me", mime_type="application/json")
def about_me_resource() -> dict:
    """
    Returns complete personal information as a resource.
    
    Returns:
        dict: All personal information
    """
    return personal_info

# Prompts

@mcp.prompt()
def about_me_prompt() -> str:
    f"""Get information about {personal_info['name']}"""
    return f"Tell me about {personal_info['name']}, including his skills, interests and how to contact."

@mcp.prompt()
def send_message(sender: str, topic: str) -> str:
    """Send a message to me"""
    return f"I want to send a message to {personal_info['name']}. My email is {sender} and I want to discuss {topic}."

