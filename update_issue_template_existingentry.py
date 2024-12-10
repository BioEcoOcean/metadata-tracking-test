import os

def update_template_with_folders():
    folder_path = "jsonFiles"
    template_path = ".github/ISSUE_TEMPLATE/update_existing_entry.yml"

    # Get list of folder names
    folder_names = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    # Format folder names into markdown list
    folder_list_md = "\n".join(f"- {folder}" for folder in folder_names)

    # Read the existing template
    with open(template_path, "r") as file:
        template_content = file.read()

    # Replace placeholder in the template
    updated_content = template_content.replace("<!-- FOLDER_NAMES_PLACEHOLDER -->", folder_list_md)

    # Write the updated template
    with open(template_path, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_template_with_folders()
