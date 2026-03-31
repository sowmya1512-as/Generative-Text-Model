import random

sentences = [
    "Artificial intelligence is transforming the world",
    "Technology is growing rapidly",
    "Machine learning improves systems",
    "AI is used in many industries"
]

prompt = input("Enter a topic: ")

result = prompt

for i in range(3):
    result += ". " + random.choice(sentences)

print("\nGenerated Text:\n")
print(result)
