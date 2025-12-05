

"""
===============================================================================
                            INVITE FORMATTER
===============================================================================

Description:
    A Python script to format invitation lists with names and email addresses.
    Supports removing emails, removing names, alphabetical sorting, and reverse
    ordering with backup/revert functionality.

Author: Chelina Obiang
Date: October 2025
Version: 1.0

Usage:
    1. Place your .txt files in the "Add Text Here" folder
    2. Run this script
    3. Select a file from the numbered list
    4. Choose formatting option(s)
    5. Optionally revert changes using backup

Input Format:
    FirstName, LastName <email@domain.com>; FirstName2, LastName2 <email2@domain.com>

Formatting Options:
    1. Remove email addresses (keep names only)
    2. Remove names (keep email addresses only)
    3. Sort alphabetically (must combine with 1 or 2)
    4. Reverse order (must combine with 1 or 2)
    Combinations: "1 + 3", "1 + 4", "2 + 3", "2 + 4"

===============================================================================
"""

# Global variable to store previous file content for backup
prev = ""

def format_no_email(txtfile):
    with open(txtfile, 'r') as file:
        text = file.read()
    
    # Replace semicolons with newlines and remove email addresses
    lines = text.replace(';', '\n').split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Remove email addresses (text between < and >)
            import re
            line_no_email = re.sub(r'<[^>]*>', '', line).strip()
            if line_no_email:
                formatted_lines.append(line_no_email)
    
    # Write back to file
    with open(txtfile, 'w') as file:
        file.write('\n'.join(formatted_lines))
    
    return txtfile

def format_no_name(txtfile):
    with open(txtfile, 'r') as file:
        text = file.read()
    
    # Replace semicolons with newlines and extract only email addresses
    lines = text.replace(';', '\n').split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            # Extract email addresses (text between < and >)
            import re
            emails = re.findall(r'<([^>]*)>', line)
            for email in emails:
                if email.strip():
                    formatted_lines.append(email.strip())
    
    # Write back to file
    with open(txtfile, 'w') as file:
        file.write('\n'.join(formatted_lines))
    
    return txtfile

def alphabetical(txtfile):
    with open(txtfile, 'r') as file:
        lines = file.readlines()
    
    # Sort lines alphabetically (case-insensitive)
    sorted_lines = sorted([line.strip() for line in lines if line.strip()], key=str.lower)
    
    # Write back to file
    with open(txtfile, 'w') as file:
        file.write('\n'.join(sorted_lines))
    
    return txtfile

def inverse(txtfile):
    with open(txtfile, 'r') as file:
        lines = file.readlines()
    
    # Reverse the order of lines
    reversed_lines = [line.strip() for line in reversed(lines) if line.strip()]
    
    # Write back to file
    with open(txtfile, 'w') as file:
        file.write('\n'.join(reversed_lines))
    
    return txtfile

def main():
    global prev
    import os
    
    folder_path = "Add Text Here"
    
    # List available text files in the folder
    text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    if not text_files:
        print(f"No .txt files found in '{folder_path}' folder. Please add your text file there and run the program again.")
        return
    
    print("Available text files:")
    for i, file in enumerate(text_files, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input("Select a file number: ")) - 1
        if choice < 0 or choice >= len(text_files):
            print("Invalid selection.")
            return
        filename = os.path.join(folder_path, text_files[choice])
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Save original content for backup
    try:
        with open(filename, 'r') as file:
            prev = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    
    formatType = input("How would you like it formatted [select a number]? (1.remove emails 2.remove names [+] 3.alphabetical order 4.inverse order)")
    
    if formatType == "1 + 3":
        alphabetical(format_no_email(filename))
    elif formatType == "1 + 4":
        inverse(format_no_email(filename))
    elif formatType == "2 + 3":
        alphabetical(format_no_name(filename))
    elif formatType == "2 + 4":
        inverse(format_no_name(filename))
    elif formatType == "1":
        format_no_email(filename)
    elif formatType == "2":
        format_no_name(filename)
    else:
        print("Invalid format type selected.")
        return
    
    print("Your file has been formatted successfully!")
    revert = input("Would you like to revert your formatting?(y/n) ")
    if revert == "y":
        with open(filename, 'w') as file:
            file.write(prev)
        print("File has been reverted to original content.")
    elif revert == "n":
        print("Glad to have helped, enjoy!👋🏽")

main()