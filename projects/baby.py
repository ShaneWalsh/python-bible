from random import choice

questions = ["Why is the sky blue?:", "Why is the ocean blue?:",
             "Where is the sun?:"]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("But why?: ").strip().lower()

print("Oh... Okay")
