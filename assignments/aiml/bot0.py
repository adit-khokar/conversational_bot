import aiml
import os
from autocorrect import Speller

spell = Speller()

# Create the kernel and learn AIML files
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
    print("Using old brain")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
    kernel.saveBrain("bot_brain.brn")
    print("Using new brain")


# Press CTRL-C to break this loop
while True:
    message = input("you > ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("bot_brain.brn")
    else:
        query = message
        query = [spell(w) for w in (query.split())]
        question = " ".join(query)
        response = kernel.respond(question)
        if response:
            print("bot > ", response)
        else:
            print("bot > :) ", )
        