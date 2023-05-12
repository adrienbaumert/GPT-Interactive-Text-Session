# GPT-Interactive-Text-Session

Copyright (C) 2023 Adrien Baumert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

## Version
1.0.0

## Description
This project, "GPT-Interactive-Text-Session", is an interactive Python application that interfaces with OpenAI's GPT-3.5-turbo model. The application is designed to carry on a conversation with a user by managing a GPT agent that receives user input, generates responses, and maintains memory of the conversation. It showcases the capabilities of OpenAI's chat models in a user-friendly manner.

## Features
- **Interactive Session**: The application allows users to interact with the AI model in a conversational manner.
- **Agent Memory Management**: The application effectively manages the memory of the AI agent, storing and using past interactions to influence future responses.
- **API Key Security**: The API key and organization ID are securely stored and accessed using a .env file, ensuring that sensitive information is not exposed.
- **GNU License**: The project is released under the GNU General Public License, granting users the freedom to use, study, share, and modify the software.

## Installation

1. Clone the repository:
```
git clone https://github.com/adrienbaumert/GPT-Interactive-Text-Session.git
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Rename the `.env.template` file to `.env` and input OpenAI organization ID and API key (make sure to keep the quotes around both the id and api key):
```
OPENAI_ORGANIZATION_ID = "sk-************************************************"
OPENAI_API_KEY = "org-************************"
```

## Instructions to Find OpenAI Organization ID/API Key
https://platform.openai.com/docs/guides/production-best-practices/setting-up-your-organization

## Usage
To start an interactive text session, run `main.py` and follow the prompts in the console. The application will manage the flow of conversation and memory updates.

```bash
python main.py
```

## Troubleshooting
If you encounter any issues, ensure that your `.env` file is set up correctly and your OpenAI organization ID and API key are valid. If you continue to encounter problems, please submit an issue on this repository.
