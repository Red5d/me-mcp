# Me MCP

> **Personal Information MCP Server**

A self-hosted MCP (Model Context Protocol) server allowing AI assistants to access personal information that you supply, and receive contact requests.

## Overview

This MCP server provides AI assistants with structured access to your personal details like bio, skills, and contact methods, while also offering a secure way for others to send you messages through your configured webhook.

## Features

- 📋 **Personal Info API**: Expose your professional details to AI assistants
- 📬 **Contact Mechanism**: Let people reach you without directly sharing your email
- 🔐 **Privacy Control**: Configure exactly what information you want to share
- 🤖 **AI-Friendly Interface**: Pre-built prompts and resources for modern AI systems

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/me-mcp.git
   cd me-mcp
   ```

2. Create and configure your `config.json` file:
   ```bash
   cp config.json.example config.json
   nano config.json  # Edit with your information
   ```

## Configuration

Edit `config.json` with your personal information and webhook URL. The "name" field is required, all others are optional and can be added/removed as needed:

```json
{
    "webhook_url": "https://your-webhook-endpoint.com",
    "personal_info": {
        "name": "Your Name",
        "handle": "yourhandle",
        "contact_methods": {
            "github": "https://github.com/yourhandle",
            "matrix": "https://matrix.to/#/@yourhandle:example.com",
            "X": "https://x.com/yourhandle",
            "email": "you@example.com"
        },
        "occupation": "Your Job",
        "skills": ["Your", "Skills", "Here"],
        "interests": ["Your", "Interests", "Here"],
        "bio": "A short biography about yourself."
    }
}
```

## Usage

Run the MCP server:

```bash
uv run mcp run -t sse me_mcp.py
```

Your MCP server will be available via SSE at `http://0.0.0.0:8000` which you can then expose to remote LLMs using a reverse proxy or similar.

You can also use [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) which includes a few more configuration options to run the server.

## MCP Tools

- **about_me()**: Returns your configured personal information
- **contact()**: Allows sending you messages via webhook

## MCP Resources

- **about://me**: JSON resource containing your personal information

## MCP Prompts

- **about_me_prompt()**: Asks the AI to describe your information
- **send_message()**: Guides the AI to help someone contact you

## Security Considerations

- Set up a secure webhook endpoint that processes contact requests
- Only expose information you're comfortable sharing publicly
- Consider running behind a reverse proxy with rate limiting

## License

MIT