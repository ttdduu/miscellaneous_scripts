#!/usr/bin/env python3

import json
import subprocess
import os
from datetime import datetime

# Path to the JSON file
json_file = "/home/ttdduu/code/miscellaneous_scripts/file_tags/demo_dir/files.json"
base_path = "/home/ttdduu/code/miscellaneous_scripts/file_tags/demo_dir"

# Define your custom message
custom_message = "TAGS: demo, jeje, tagx"


# Function to prompt user input using dmenu
def get_input(prompt):
    return (
        subprocess.run(
            ["dmenu", "-p", prompt],
            input="".encode(),
            stdout=subprocess.PIPE,
        )
        .stdout.decode()
        .strip()
    )


# Function to filter and sort filenames by keywords
def filter_files_by_keywords(data, keywords):
    matching_files = []

    for filename, tags in data.items():
        # Check if all keywords appear as whole words in the tags (case insensitive)
        if all(
            any(keyword.lower() == tag.lower() for tag in tags) for keyword in keywords
        ):
            file_path = os.path.join(base_path, filename)
            mod_time = os.path.getmtime(file_path)  # Get file modification time
            formatted_time = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M")
            matching_files.append(
                {
                    "filename": filename,
                    "display": f"{filename} - TAGS: {' | '.join(tags[1:])} - MODIFIED: {formatted_time}",
                    "mod_time": mod_time,
                }
            )

    # Sort the matching files by modification date (newest first)
    matching_files.sort(key=lambda x: x["mod_time"], reverse=True)

    return matching_files


# Load JSON file
with open(json_file, "r") as f:
    data = json.load(f)

# Get input keywords
input_keywords = get_input("Enter keywords (space-separated):")


if input_keywords:
    # Convert input to list of keywords
    keywords = input_keywords.split()

    # Filter the files by the entered keywords
    matching_files = filter_files_by_keywords(data, keywords)

    if matching_files:
        # Prepare the list for fzf input
        fzf_input = "\n".join([file["display"] for file in matching_files])

        # Run fzf to let the user select a file
        fzf = subprocess.Popen(
            [
                "fzf",
                "-e",
                "-i",
                "--sort",
                "0",
                "--header",
                custom_message,  # Add your custom message as a header
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        selected_file, _ = fzf.communicate(input=fzf_input.encode())

        selected_file = selected_file.decode().strip()

        if selected_file:
            # Find the selected filename by matching the display string
            for file in matching_files:
                if file["display"] == selected_file:
                    selected_filename = file["filename"]
                    break

            # Build the command to open the selected file with vifm
            cmd = f'st -e vifm --select "{base_path}/{selected_filename}"'
            subprocess.run(["sh", "-c", cmd])
        else:
            print("No file selected")
    else:
        print("No matching files found")
else:
    cmd = f'st -e vifm --select "{base_path}"'
    subprocess.run(["sh", "-c", cmd])
