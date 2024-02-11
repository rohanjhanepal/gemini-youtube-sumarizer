from gemini import generate_summary

while True:
    prompt = input(">> ")
    print(generate_summary(prompt))
    
    