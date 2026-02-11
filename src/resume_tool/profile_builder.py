# profile_builder.py
import json
import os
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()

# File where we store your raw data
DATA_FILE = "master_profile.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"summary": {}, "experience": [], "skills": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    console.print(f"\n[bold green]✅ Profile saved to {DATA_FILE}![/bold green]")

def add_experience(data):
    console.clear()
    console.print(Panel("[bold blue]Add Work Experience[/bold blue]", style="blue"))
    
    role = Prompt.ask("Job Title (e.g. QA Analyst)")
    company = Prompt.ask("Company Name")
    dates = Prompt.ask("Dates (e.g. 2021-Present)")
    
    console.print("\n[yellow]Now, let's add bullet points. Type 'DONE' when finished.[/yellow]")
    
    while True:
        bullet = Prompt.ask("\n[bold]Enter a Bullet Point[/bold]")
        if bullet.strip().upper() == "DONE":
            break
            
        # The Magic: Auto-Tagging
        console.print("[dim]Select domains for this bullet (separate by comma):[/dim]")
        console.print("[dim]Options: QA, PRODUCT, DELIVERY, TECH[/dim]")
        tags_input = Prompt.ask("Tags", default="QA")
        tags = [t.strip().upper() for t in tags_input.split(",")]
        
        # Add to data
        new_entry = {
            "text": bullet,
            "domains": tags,
            "metadata": f"{role} at {company} ({dates})"
        }
        data["experience"].append(new_entry)
        console.print("[green]✓ Bullet added![/green]")

def add_skills(data):
    console.clear()
    console.print(Panel("[bold blue]Add Skills[/bold blue]", style="blue"))
    
    category = Prompt.ask("Skill Category (e.g. QA, PRODUCT, TECH)").upper()
    current_skills = data["skills"].get(category, [])
    
    console.print(f"Current {category} Skills: {', '.join(current_skills)}")
    
    new_skills = Prompt.ask("Enter new skills (comma separated)")
    skill_list = [s.strip() for s in new_skills.split(",")]
    
    if category in data["skills"]:
        data["skills"][category].extend(skill_list)
    else:
        data["skills"][category] = skill_list
        
    # Remove duplicates
    data["skills"][category] = list(set(data["skills"][category]))

def add_summary(data):
    console.clear()
    console.print(Panel("[bold blue]Add Professional Summary[/bold blue]", style="blue"))
    
    category = Prompt.ask("Summary Type (e.g. QA, PRODUCT, DELIVERY)").upper()
    text = Prompt.ask("Paste Summary Text")
    
    data["summary"][category] = text

def main():
    data = load_data()
    
    while True:
        console.clear()
        console.print(Panel("[bold white]📝 RESUME PROFILE BUILDER[/bold white]", style="bold blue"))
        
        console.print(f"[dim]Current Database: {len(data['experience'])} bullets, {len(data['skills'])} skill categories[/dim]\n")
        
        console.print("1. 💼 Add Work Experience (Bullets)")
        console.print("2. 🛠️  Add Skills")
        console.print("3. 📄 Add/Edit Summaries")
        console.print("4. 💾 Save & Exit")
        
        choice = Prompt.ask("\nSelect Option", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            add_experience(data)
        elif choice == "2":
            add_skills(data)
        elif choice == "3":
            add_summary(data)
        elif choice == "4":
            save_data(data)
            break

if __name__ == "__main__":
    main()
