from ai import agent

print("--DEBUG-- Starting physics SLM")

while True:
    agent()
    
# This must have a system which identifies when the SLM must be stop being used which has to be made by ourselves, OpenRouter has no native way to make dynamic solutions for MoE or RAG systems which has dynamic running input dependent.