import subprocess

def ask_agent(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.2"],
        input=prompt,
        capture_output=True,
        text=True
    )
    return result.stdout

while True:
    question = input("You: ")
    answer = ask_agent(question)
    print("Agent:", answer)
