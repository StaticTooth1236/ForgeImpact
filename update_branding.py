import os
import glob

# ====================== CONFIG ======================
OLD_COMPANY = "Eurus Systems"
NEW_COMPANY = "Eurus Systems"

OLD_TOOL = "ARIA"
NEW_TOOL = "ARIA"

OLD_FULL_NAME = "Agentic Reasoning for Impact Analysis"
NEW_FULL_NAME = "Agentic Reasoning for Impact Analysis"
# ===================================================

def update_branding():
    py_files = glob.glob("**/*.py", recursive=True)
    md_files = glob.glob("**/*.md", recursive=True)
    all_files = py_files + md_files

    print(f"Scanning {len(all_files)} files for branding updates...\n")

    changes = []

    for filepath in all_files:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            count = 0

            if OLD_COMPANY in new_content:
                new_content = new_content.replace(OLD_COMPANY, NEW_COMPANY)
                count += content.count(OLD_COMPANY)

            if OLD_TOOL in new_content:
                new_content = new_content.replace(OLD_TOOL, NEW_TOOL)
                count += content.count(OLD_TOOL)

            if OLD_FULL_NAME in new_content:
                new_content = new_content.replace(OLD_FULL_NAME, NEW_FULL_NAME)
                count += content.count(OLD_FULL_NAME)

            if count > 0:
                changes.append((filepath, count))

        except Exception as e:
            print(f"Could not read {filepath}: {e}")

    if not changes:
        print("✅ No branding changes needed.")
        return

    print("The following files will be updated:\n")
    for filepath, count in changes:
        print(f"  - {filepath} ({count} changes)")

    confirm = input("\nProceed with these changes? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("Operation cancelled.")
        return

    for filepath, _ in changes:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            new_content = new_content.replace(OLD_COMPANY, NEW_COMPANY)
            new_content = new_content.replace(OLD_TOOL, NEW_TOOL)
            new_content = new_content.replace(OLD_FULL_NAME, NEW_FULL_NAME)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"✅ Updated: {filepath}")

        except Exception as e:
            print(f"❌ Failed to update {filepath}: {e}")

    print("\n🎉 Branding update complete!")

if __name__ == "__main__":
    update_branding()