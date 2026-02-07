# expert_tips.py

# 1. THE UNIVERSAL TRANSLATOR DICTIONARY
# This maps "Generic/Tech" terms to "Industry Specific" terms.
INDUSTRY_TRANSLATORS = {
    "Sports Marketing": {
        "user": "fan",
        "users": "fans",
        "consumer": "season ticket holder",
        "consumers": "audience",
        "product": "campaign",
        "products": "activations",
        "feature": "sponsorship asset",
        "test": "activation",
        "testing": "market research",
        "bug": "friction point",
        "deployed": "launched",
        "development": "fan engagement strategy",
        "client": "partner",
        "stakeholder": "team leadership",
        "sales": "ticket revenue",
        "community": "fanbase"
    },
    "Healthcare & Nursing": {
        "customer": "patient",
        "customers": "patients",
        "client": "patient",
        "user": "patient",
        "product": "care plan",
        "service": "clinical care",
        "manager": "charge nurse",
        "team": "interdisciplinary team",
        "issue": "complication",
        "solution": "intervention",
        "sales": "patient outcomes"
    },
    "Tech & SaaS": {
        "project": "product",
        "tool": "stack",
        "managed": "orchestrated",
        "changed": "refactored",
        "plan": "roadmap",
        "issue": "bug",
        "fix": "patch",
        "customer": "user",
        "revenue": "ARR",
        "marketing": "growth hacking"
    },
    "Finance & Banking": {
        "money": "capital",
        "budget": "allocation",
        "spending": "expenditure",
        "saving": "cost reduction",
        "check": "audit",
        "mistake": "discrepancy",
        "team": "deal team",
        "sales": "deal flow",
        "customer": "client"
    },
    "Retail & E-Commerce": {
        "user": "shopper",
        "customer": "guest",
        "stock": "inventory",
        "store": "visual merchandising",
        "sales": "conversions",
        "team": "associates",
        "manager": "store director"
    },
    "Executive / Leadership": {
        "helped": "spearheaded",
        "worked on": "executed",
        "responsible for": "accountable for",
        "managed": "directed",
        "team": "organization",
        "idea": "strategic vision",
        "problem": "business challenge",
        "fix": "turnaround strategy"
    }
}

# 2. GENERAL HEALTH CHECK LISTS
WEAK_WORDS = [
    "responsible for", "duties included", "worked on", "helped", "assisted", 
    "handled", "participated in", "various", "hired to", "trying to"
]

POWER_VERBS = [
    "spearheaded", "orchestrated", "executed", "optimized", "accelerated", 
    "generated", "revitalized", "championed", "pioneered", "engineered"
]

# 3. INDUSTRY EXPERT TIPS
EXPERT_INSIGHTS = {
    "Sports Marketing": {
        "source": "Front Office Sports",
        "tips": [
            "⚠️ **Fan Experience:** Focus on how you improved the fan journey.",
            "💡 **Sponsorship:** Mention 'fulfillment' or 'activations'.",
            "🎟️ **Revenue:** Highlight ticket sales or merchandise ROI."
        ],
        "metrics": ["ticket sales", "attendance", "roi", "engagement"]
    },
    "Healthcare": {
        "source": "Nursing Boards",
        "tips": [
            "⚠️ **Patient Volume:** State your caseload (e.g., 5:1 ratio).",
            "💡 **EMR Systems:** List Epic, Cerner, or Meditech explicitly.",
            "🏥 **Compliance:** Mention HIPAA or JCAHO."
        ],
        "metrics": ["patient load", "compliance", "satisfaction"]
    },
    "Software Engineer": {
        "source": "Google Hiring Committee",
        "tips": [
            "⚠️ **GitHub Link:** Essential in header.",
            "💡 **Scale:** Mention 'requests per second' or 'latency'.",
            "🛠️ **Stack Order:** Languages go at the top."
        ],
        "metrics": ["latency", "users", "uptime", "optimization"]
    }
}

def get_expert_advice(job_title_guess):
    """Returns advice based on the detected industry."""
    if not job_title_guess: return None
    job_title_guess = job_title_guess.lower()
    
    # Simple mapping logic
    if any(x in job_title_guess for x in ["sport", "marketing", "brand"]):
        return EXPERT_INSIGHTS.get("Sports Marketing")
    elif any(x in job_title_guess for x in ["nurse", "medical", "health", "clinical"]):
        return EXPERT_INSIGHTS.get("Healthcare")
    elif any(x in job_title_guess for x in ["developer", "engineer", "data", "tech"]):
        return EXPERT_INSIGHTS.get("Software Engineer")
    
    return None
