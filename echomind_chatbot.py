def generate_response(user_input):
    # Dynamic responses based on keywords
    if "favorite" in user_input.lower():
        return "I don't have favorites, but I enjoy helping people like you!"
    elif "time" in user_input.lower():
        return "I'm not sure what time it is, but it's always a good time to chat!"
    else:
        return f"I'm still learning, but here's a response to '{user_input}'."

print("Welcome to EchoMind Chatbot!")
user_name = input("What's your name? ")
print(f"Nice to meet you, {user_name}!")
print("You can type 'help' to see available commands or 'exit' to quit.")

while True:
    user_input = input(f"{user_name}: ")

    # Handle empty input
    if not user_input.strip():
        print("EchoMind Chatbot: It seems you didn't say anything. Try again!")
        continue

    # Exit command
    if user_input.lower() in ["exit", "quit"]:
        print(f"EchoMind Chatbot: Goodbye, {user_name}!")
        break

    # Help command
    elif user_input.lower() == "help":
        print("EchoMind Chatbot: Here are some things I can do:")
        print("- hello: Greet the chatbot.")
        print("- how are you?: Ask how I'm doing.")
        print("- joke: Hear a programmer joke.")
        print("- fun fact: Learn an interesting fact.")
        print("- exit/quit: Leave the chatbot.")

    # Predefined responses
    elif user_input.lower() == "hello":
        print(f"EchoMind Chatbot: Hi there, {user_name}! How can I help you today?")
    elif user_input.lower() == "how are you?":
        print("EchoMind Chatbot: I'm just a bot, but I'm here to help!")
    elif user_input.lower() == "joke":
        print("EchoMind Chatbot: Why don't programmers like nature? It has too many bugs!")
    elif user_input.lower() == "fun fact":
        print("EchoMind Chatbot: Did you know that the first computer bug was an actual moth?")

    # Catch-all dynamic response
    else:
        response = generate_response(user_input)
        print(f"EchoMind Chatbot: {response}")
