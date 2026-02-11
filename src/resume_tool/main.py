import os
import time
import sys
# If you don't have rich installed yet, run: pip install rich
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text

# Import your modules
import master_resume_builder
import ats_auditor

# Initialize Console with a standard theme
console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    # CHANGED: "on blue" removed. Text is now "bold blue" which works on white backgrounds.
    title = Text("🚀 RESUME COMMAND CENTER v2.1", style="bold blue", justify="center")
    console.print(Panel(title, style="black"))

def main_menu():
    while True:
        print_header()
        
        # CHANGED: Text colors are now Black/Blue for visibility on white screens
        console.print("\n[bold blue]MAIN MENU[/bold blue]")
        console.print("[bold black]1.[/bold black] [black]Build a Targeted Resume[/black]")
        console.print("[bold black]2.[/bold black] [black]Audit a Resume (Check Score)[/black]")
        console.print("[bold red]3.[/bold red] [black]Exit[/black]")
        console.print("-" * 40, style="black")
        
        # Ask for input
        choice = Prompt.ask("[bold blue]Select Option[/bold blue]", choices=["1", "2", "3"], default="1")
        
        if choice == "1":
            console.print("\n[bold green]...Launching Builder...[/bold green]")
            time.sleep(1)
            try:
                master_resume_builder.main()
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {e}")
            
            # Using input() instead of console.input() for safer pausing
            input("\nPress Enter to return to menu...")
            
        elif choice == "2":
            console.print("\n[bold green]...Launching Auditor...[/bold green]")
            time.sleep(1)
            try:
                ats_auditor.main()
            except Exception as e:
                console.print(f"[bold red]Error:[/bold red] {e}")
            
            input("\nPress Enter to return to menu...")
            
        elif choice == "3":
            console.print("\n[bold blue]Good luck! 👋[/bold blue]")
            break

if __name__ == "__main__":
    main_menu()
