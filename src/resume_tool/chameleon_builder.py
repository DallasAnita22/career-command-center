# chameleon_builder.py
import json
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

# --- 1. LOAD DATABASE ---
def load_database():
    """Loads the master profile JSON created by the builder."""
    if os.path.exists("master_profile.json"):
        with open("master_profile.json", "r") as f:
            return json.load(f)
    else:
        print("⚠️  Warning: 'master_profile.json' not found. Using empty data.")
        return {"summary": {}, "experience": [], "skills": {}}

RESUME_DATABASE = load_database()

# --- 2. FILTER LOGIC ---
def get_targeted_content(target_role):
    """
    Filters the database based on the selected role (QA, PRODUCT, DELIVERY).
    """
    # A. Get Summary (Default to QA if specific one missing)
    summary = RESUME_DATABASE["summary"].get(target_role, "")
    if not summary:
        # Fallback: grab the first available summary
        if RESUME_DATABASE["summary"]:
            summary = list(RESUME_DATABASE["summary"].values())[0]
        else:
            summary = "Professional Summary..."
    
    # B. Filter Bullets
    filtered_bullets = []
    for item in RESUME_DATABASE["experience"]:
        # Check if the target role is in the item's domain tags
        item_text = item["text"] if isinstance(item, dict) else str(item)
        item_domains = item.get("domains", []) if isinstance(item, dict) else []
        
        if target_role in item_domains:
            filtered_bullets.append(item_text)
            
    # C. Assemble Skills (Target Role + TECH)
    target_skills = RESUME_DATABASE["skills"].get(target_role, [])
    tech_skills = RESUME_DATABASE["skills"].get("TECH", [])
    
    # Combine and remove duplicates
    combined_skills = list(set(target_skills + tech_skills))
    
    return summary, filtered_bullets, combined_skills

# --- 3. WORD DOC GENERATOR ---
def save_to_docx(filename, role_name, summary, bullets, skills):
    doc = Document()
    
    # Styling
    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(11)

    # Header
    doc.add_heading('J. Bateman', level=0).alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('Baltimore, MD | (301) 213-0948 | j.batemansheppard@gmail.com | LinkedIn/JBateman').alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph('='*80)

    # Summary
    doc.add_heading('PROFESSIONAL SUMMARY', level=2)
    doc.add_paragraph(summary)

    # Experience
    doc.add_heading('PROFESSIONAL EXPERIENCE', level=2)
    p = doc.add_paragraph()
    runner = p.add_run('APKUDO LLC | Technical Delivery Analyst (Product Focus) | 2021 – Present')
    runner.bold = True
    
    # --- BULLET POINT FIX ---
    for b in bullets:
        # Strip weird characters (bullets, dashes, question marks) from the start
        clean_text = b.lstrip("•-–*? ")
        doc.add_paragraph(clean_text, style='List Bullet')

    # Project Section (Hardcoded for now as it's a key asset)
    doc.add_heading('Projects', level=2)
    p_proj = doc.add_paragraph()
    runner_proj = p_proj.add_run('FOCUSFINANCE | Product Owner & Developer')
    runner_proj.bold = True
    doc.add_paragraph('Designed and launched an Android budgeting application, defining the product roadmap based on user needs.')

    # Skills
    doc.add_heading('SKILLS & TOOLS', level=2)
    
    # Join list of skills into string
    if isinstance(skills, list):
        skill_text = ' | '.join(skills)
    else:
        skill_text = str(skills)
        
    doc.add_paragraph(skill_text)

    # Save
    try:
        doc.save(filename)
        print(f"\n✅ SUCCESS: Resume saved to {filename}")
    except Exception as e:
        print(f"\n❌ ERROR: Could not save file: {e}")

# --- 4. MAIN EXECUTION ---
def main():
    print("--- Chameleon Resume Generator ---")
    
    print("Select Target Role:")
    print("1. QA (Quality Assurance)")
    print("2. PRODUCT (Product Owner/Analyst)")
    print("3. DELIVERY (Delivery Analyst)")
    
    choice = input("Enter choice (1-3): ").strip()
    
    role_map = {"1": "QA", "2": "PRODUCT", "3": "DELIVERY"}
    target_role = role_map.get(choice, "QA") # Default to QA
    
    print(f"\nSelected Mode: {target_role}")
    
    company_name = input("Enter Target Company Name (e.g. Strava): ").strip()
    
    if company_name:
        try:
            # Get Content
            summary, bullets, skills = get_targeted_content(target_role)
            
            if not bullets:
                print("\n⚠️  WARNING: No bullet points found for this role! Run the Profile Builder first.")
                return

            # Find Desktop
            user_home = os.path.expanduser("~")
            desktop_path = os.path.join(user_home, "Desktop")
            onedrive_desktop = os.path.join(user_home, "OneDrive", "Desktop")

            if os.path.exists(desktop_path):
                save_folder = desktop_path
            elif os.path.exists(onedrive_desktop):
                save_folder = onedrive_desktop
            else:
                save_folder = os.getcwd()

            # Save File
            filename = os.path.join(save_folder, f"JBateman_{company_name}_{target_role}.docx")
            save_to_docx(filename, target_role, summary, bullets, skills)
            
        except Exception as e:
            print(f"\n❌ ERROR: {e}")

if __name__ == "__main__":
    main()
