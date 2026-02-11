import json
import os
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()

# --- 1. LOAD DATABASE FROM FILE ---
def load_database():
    # Look for the file created by profile_builder.py
    if os.path.exists("master_profile.json"):
        with open("master_profile.json", "r") as f:
            return json.load(f)
    else:
        # Fallback to empty structure if file doesn't exist
        return {"summary": {}, "experience": [], "skills": {}}

def select_summary(data):
    console.print(Panel("[bold blue]Step 1: Choose a Summary[/bold blue]", style="blue"))
    
    if not data.get("summary"):
        console.print("[yellow]No summaries found in master profile.[/yellow]")
        return None
        
    options = list(data["summary"].keys())
    for idx, key in enumerate(options, 1):
        console.print(f"{idx}. {key}")
        
    choice = Prompt.ask("Select Summary", choices=[str(i) for i in range(1, len(options)+1)])
    selected_key = options[int(choice)-1]
    return data["summary"][selected_key]

def select_experience(data):
    console.print(Panel("[bold blue]Step 2: Filter Experience[/bold blue]", style="blue"))
    
    # Get all unique domains from experience
    all_domains = set()
    for entry in data.get("experience", []):
        for domain in entry.get("domains", []):
            all_domains.add(domain)
            
    if not all_domains:
        console.print("[yellow]No experience entries found with domains.[/yellow]")
        return []

    console.print(f"Available Domains: {', '.join(sorted(all_domains))}")
    target_role = Prompt.ask("Enter Target Role (e.g. QA, PRODUCT, TECH)").upper()
    
    selected_bullets = []
    console.print(f"\n[bold]Selecting bullets for {target_role}...[/bold]")
    
    for entry in data.get("experience", []):
        if target_role in entry.get("domains", []):
            console.print(f"[green]✓ Adding:[/green] {entry['text']}")
            selected_bullets.append(entry)
            
    return selected_bullets

def select_skills(data):
    console.print(Panel("[bold blue]Step 3: Select Skills[/bold blue]", style="blue"))
    
    if not data.get("skills"):
        console.print("[yellow]No skills found.[/yellow]")
        return {}
        
    selected_skills = {}
    for category, skills in data["skills"].items():
        if Confirm.ask(f"Include {category} skills?"):
            selected_skills[category] = skills
            
    return selected_skills

def generate_resume(summary, experience, skills):
    console.clear()
    console.print(Panel("[bold green]✨ GENERATING TARGETED RESUME ✨[/bold green]", style="green"))
    
    console.print("\n[bold]PROFESSIONAL SUMMARY[/bold]")
    console.print(summary)
    
    console.print("\n[bold]EXPERIENCE[/bold]")
    for entry in experience:
        console.print(f"• {entry['text']}")
        
    console.print("\n[bold]SKILLS[/bold]")
    for cat, skill_list in skills.items():
        console.print(f"[bold]{cat}:[/bold] {', '.join(skill_list)}")
        
    console.print("\n[dim]Resume generated successfully![/dim]")

def main():
    data = load_database()
    
    if not data["summary"] and not data["experience"]:
        console.print("[red]Error: master_profile.json is empty or missing.[/red]")
        console.print("Run option 4 (Create Profile) first.")
        return

    summary = select_summary(data)
    experience = select_experience(data)
    skills = select_skills(data)
    
    generate_resume(summary, experience, skills)

if __name__ == "__main__":
    main()
