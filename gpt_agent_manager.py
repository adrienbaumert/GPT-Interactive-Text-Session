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
# File: gpt_agent_manager.py
# Version : 1.0.0
# =================================================

# This module contains functions for managing a GPT agent,
# including receiving user input, generating agent responses,
# and updating the agent's memory.

# Debugging:
# Token to enable memory debugging (0 = OFF, 1 = ON)
display_memory_debug = 0

# Defining functions
def get_user_input():
    # Prompt the user for input and return their message as a string
    print("\n", end="")
    input_message = input("Enter input: ")
    print("\n", end="")
    return input_message

def format_user_input(input_message):
    # Add a 'User: ' prefix to the input message to distinguish it in the GPT agent's memory
    input_message = f"User: {input_message}"
    return input_message

def create_memory_entry(input_message, response_message):
    # Combine user input and GPT agent response into a single memory entry for storage
    memory_entry = f"\n{input_message}\n{response_message}"

    # Returns the processed memory
    return memory_entry

def update_agent_memory(agent_instance, user_input, ai_output):
    # Update the GPT agent's memory with the provided user input and AI output
    processed_memory = create_memory_entry(user_input, ai_output)
    agent_instance.append_gpt_agent_memory(processed_memory)

def display_memory(agent_instance):
    # Print the current memory of the GPT agent for debugging purposes
    print(f"\nAI Memory:\n[{agent_instance.get_memory()}]")

def run_gpt_agent_manager(gpt_agent):
    # Manage the GPT agent by coordinating user input, AI responses, and memory updates

    # Retrieve user input and format it
    user_input = get_user_input()

    # Add "User: " to user input
    user_input = format_user_input(user_input)

    # Retrieve the GPT agent's memory
    memory = gpt_agent.get_memory()

    # Generate an AI response based on the user input and memory
    ai_output = gpt_agent.generate_response(user_input, memory)

    # Update the GPT agent's memory with the new conversation entry
    update_agent_memory(gpt_agent, user_input, ai_output)

    # Displaying the AI output
    print(ai_output)

    # Calling the display memory testing function
    if display_memory_debug == 1:
        display_memory(gpt_agent)