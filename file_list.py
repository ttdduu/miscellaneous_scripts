#!/usr/bin/env python3

import subprocess
import file_tags

#
# Get input keywords
input_keywords = file_tags.get_input("Enter keywords (space-separated):")


def file_list(input_keywords):
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


if input_keywords:
    # Prepare the command to run file_tags with the input keywords in a terminal
    command = f"st -e python3 -c \"file_list('{input_keywords}')\""
    subprocess.run(["sh", "-c", command])
else:
    print("No keywords entered")
