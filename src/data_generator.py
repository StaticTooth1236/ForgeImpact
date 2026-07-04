import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import random
from faker import Faker
from src.llm_client import LLMClient

fake = Faker()
llm = LLMClient()

def generate_change_request():
    """Generate realistic change request for the MAAP-1 Swarm System"""
    
    prompt = """You are working on the AetherForge Modular Autonomous Aerial Platform (MAAP-1) Swarm System.
This is a heavy-lift unmanned helicopter capable of modular payloads (firefighting, logistics, ISR) and autonomous group (swarm) operations. It operates from modified 18-wheeler mobile bases.

Generate ONE realistic Engineering Change Request.
Return ONLY valid JSON with these exact keys:
- change_id
- description (2-3 sentences)
- affected_parts (list of 2-4 part numbers/codes)
- reason
- proposed_solution

Make it sound professional for both wildfire response and military logistics/ISR missions."""
    
    try:
        response = llm.chat(prompt, system_prompt="You are a senior aerospace systems engineer specializing in autonomous platforms.", temperature=0.75)
        data = json.loads(response)
        return data
    except:
        # Fallback
        return {
            "change_id": f"MAAP-{fake.random_number(digits=5)}",
            "description": "Proposed engineering change to improve modular payload interface or swarm coordination capability.",
            "affected_parts": [fake.bothify("MAAP-####") for _ in range(random.randint(2,4))],
            "reason": random.choice(["Improved swarm coordination", "Enhanced payload modularity", "Better environmental resilience", "Regulatory compliance", "Cost/performance optimization"]),
            "proposed_solution": "Update design, software, and manufacturing processes with appropriate validation."
        }

if __name__ == "__main__":
    print("Generating synthetic changes for AetherForge MAAP-1 Swarm System...\n")
    
    changes = [generate_change_request() for _ in range(10)]
    
    with open("data/sample_changes.json", "w") as f:
        json.dump({
            "company": "AetherForge Systems",
            "program": "Modular Autonomous Aerial Platform (MAAP-1) Swarm System",
            "description": "Heavy-lift unmanned helicopter with modular payloads and swarm autonomy for firefighting and military logistics/ISR missions.",
            "changes": changes
        }, f, indent=2)
    
    print(f"✅ Generated {len(changes)} changes")
    print("Saved to data/sample_changes.json")