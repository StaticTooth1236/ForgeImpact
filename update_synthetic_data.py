import os
import glob

# ====================== CONFIG ======================
DATA_FOLDER = "data"
OLD_NAME = "AetherForge"
NEW_NAME = "Eurus Systems"
# ===================================================

def update_files():
    md_files = glob.glob(os.path.join(DATA_FOLDER, "**/*.md"), recursive=True)
    
    if not md_files:
        print("No .md files found in the data/ folder.")
        return

    print(f"Found {len(md_files)} markdown files in '{DATA_FOLDER}' folder.\n")

    changes = []

    for filepath in md_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if OLD_NAME in content:
            new_content = content.replace(OLD_NAME, NEW_NAME)
            changes.append((filepath, content.count(OLD_NAME)))

    if not changes:
        print("✅ No occurrences of 'AetherForge' found. Nothing to update.")
        return

    print("The following files contain 'AetherForge' and will be updated:\n")
    for filepath, count in changes:
        print(f"  - {filepath} ({count} occurrences)")

    confirm = input("\nDo you want to proceed with the replacement? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Operation cancelled.")
        return

    # Perform the replacement
    for filepath, _ in changes:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content.replace(OLD_NAME, NEW_NAME)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        print(f"✅ Updated: {filepath}")

    print("\n🎉 All files updated successfully!")

if __name__ == "__main__":
    update_files()