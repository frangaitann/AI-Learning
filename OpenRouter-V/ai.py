from openai import OpenAI
from misc import token_loader
import datetime, zoneinfo

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=token_loader,
)

tz = zoneinfo.ZoneInfo("America/Buenos_Aires")
physics_data= "--Some-Url/Data-Scraping--"

system_input = f"You're a SLM inside a MoE AI Agent, you're a especialist on physics, every question made in the physics area must be solved by you, who is equivalent to a physics major degree real human. You have your information from here: {physics_data}"


def agent():
    user_input = input("\n\nMe >> ")
    
    response= client.chat.completions.create(
        model="openai/gpt-4o-mini",     # This could be changed to any supported OpenRouter web model and it would change the entire model without any other changes to the code.
        messages=[
            {"role": "system", "content": system_input},
            {"role": "user", "content": user_input},
        ],
        temperature=0.5     # Temperature changes if model "thinking" must be rigid or flexible | 0 means totally rigid, precise, and fact-based answer, 1 means more flexible, creative, relative, non obvious answers
    )
        
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}] User Input: {user_input}\n")
        f.write(f"[{datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}] PhysicsBot: {response.choices[0].message.content}\n\n")
        f.close()
            
    print("\n\nPhysicsBot >> " +  response.choices[0].message.content)