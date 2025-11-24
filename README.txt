Project Title: Friendly Python Chatbot

Overview
This project is a small, beginner-friendly Python chatbot that you can talk to in your terminal. It understands a few common phrases like greetings, “how are you”, “thanks”, and “bye”, and answers with simple, friendly messages.

What the Chatbot Can Do

Chat with you in plain text in the terminal.

Respond to basic phrases such as:

hello / hi

how are you

name (asks who the bot is)

thanks

bye (ends the chat)

Pause briefly before replying so it feels a bit more natural.

How It Works (In Simple Terms)

At the top of the program, there is a dictionary that acts like the bot’s “phrasebook”. Each known phrase has a matching reply.

When you type something, the program converts it to lowercase and checks whether any of the known phrases appear in your message.

If it finds a match, it prints the corresponding reply. If not, it sends a default message saying it does not understand.

The chat continues in a loop until you type bye, which tells the program to say goodbye and stop running.

What You Need

Python 3 installed on your computer.

No extra packages are required; the only import is the built-in time module.

How to Run the Chatbot

Save the Python code in a file, for example: chatbot.py.



Open a terminal or command prompt in that folder.

Run the script with:

python chatbot.py or python3 chatbot.py

Type your messages after the You: prompt.

Type bye when you want to end the conversation.

How to Customize It

Open the script and find the responses dictionary.

Add new keys (phrases) and values (replies) to teach the bot new things to say.

Edit the existing replies if you want a different tone (more formal, more funny, etc.).

Keep the keys lowercase so they match the lowercased user input.

What This Bot Cannot Do (Yet)

It does not understand full natural language or context; it just looks for known phrases.

It does not learn from past conversations.

It does not use the internet or any AI models.

You can use this project as a simple starting point for learning how chatbots work and then gradually add more intelligence and features as you learn more Python.

