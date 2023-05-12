# Copyright (C) 2023 Adrien Baumert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# Project: GPT-Interactive-Text-Session
# File: main.py
# Version : 1.0.0
# =================================================

# Program architecture:
# 1. Import required classes and modules
# 2. Create an instance of the GPTAgent
# 3. Run the GPT agent manager system in a loop, passing the GPT agent instance

# importing os
import os

# Printing copyright notice
with open("COPYRIGHT_NOTICE.txt", "r") as notice:
    print(f"{notice.read()}\n")

# Printing version information
with open("VERSION.txt", "r") as version:
    print(f"{version.read()}\n")

# Importing GPTAgent and the system that manages it (gpt_agent_manager)
try:
    from gpt_agent import GPTAgent
    from gpt_agent_manager import run_gpt_agent_manager

except Exception as runtime_error:
    # Check if the .env file is missing and inform the user if so
    if os.path.isfile(".env") == False:
        print("Error: No .env File Found (Rename .env.template -> .env)")

    # Catching an error from OpenAI that means there was an issue with the API key
    if str(runtime_error) == "<empty message>":
        print("Error: Invalid OpenAI organization ID/API key")

    # Printing any other errors
    else:
        print(f"Error: {runtime_error}")

    quit()

# Printing the welcome message
print("\rThe following is a conversation between a user and an AI-Language model:\n")

# Create an instance of GPTAgent
gpt_agent = GPTAgent()

# Run the GPT agent manager system in a loop, continuously handling user input and generating AI responses
while True:
    # Pass the GPT agent instance to the manager system and manage the conversation
    try:
        run_gpt_agent_manager(gpt_agent)

    except Exception as error:
        # Print any other errors that occur during the execution
        print(f"Error: {error}")

        quit()
