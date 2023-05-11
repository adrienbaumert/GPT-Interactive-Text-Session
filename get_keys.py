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
# File: key_keys.py
# Version : 1.0.0
# =================================================

# This module retrieves the OpenAI Organization ID and OpenAI GPT API Key
# from the .env file and returns them as a dictionary.

# Importing os
import os

# Loading load_dotenv from dotenv
from dotenv import load_dotenv

def retrieving_keys():
    # Load the environment variables from the .env file
    load_dotenv()

    # Create a dictionary to store the OpenAI Organization ID and API Key
    keys = {
        "org_id" : os.getenv("OPENAI_ORGANIZATION_ID"),
        "api_key" : os.getenv("OPENAI_API_KEY")
    }

    # Return the dictionary containing the API keys
    return keys