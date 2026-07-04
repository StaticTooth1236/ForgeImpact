import json
from src.llm_client import LLMClient

def load_data():
    try:
        with open("data/sample_changes.json", "r") as f:
            return json.load(f)
    except:
        return {"changes": []}

def main():
    llm = LLMClient()
    data = load_data()
    
    print("=== AetherForge MAAP-1 Swarm System Chat ===\n")
    print("Ask questions about engineering changes, system impacts, or the program.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        # Add context from synthetic data
        context = f"""Company: AetherForge Systems
Program: Modular Autonomous Aerial Platform (MAAP-1) Swarm System
Description: Heavy-lift unmanned helicopter with modular payloads (firefighting, logistics, ISR) and swarm autonomy. Operates from mobile trailer bases.

Available sample changes: {len(data.get('changes', []))}"""
        
        full_prompt = f"{context}\n\nUser question: {user_input}"
        
        response = llm.chat(full_prompt, 
                          system_prompt="You are a knowledgeable systems engineer for AetherForge Systems. Provide professional, technical answers about the MAAP-1 platform and engineering changes.")
        print("AI:", response, "\n")

if __name__ == "__main__":
    main()