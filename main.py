import random
import json

# Load lists from JSON files
with open('races.json', encoding='utf-8') as f:
    races = json.load(f)

with open('classes.json', encoding='utf-8') as f:
    classes = json.load(f)

with open('backstories.json', encoding='utf-8') as f:
    backstories = json.load(f)

# Function to generate a random character
def generate_character():
    race = random.choice(races)
    character_class = random.choice(classes)
    backstory = random.choice(backstories)

    return {
        "Race": race,
        "Character Class": character_class,
        "Backstory": backstory
    }

# Generate a character
character = generate_character()

# Print out the character
print("Race: ", character["Race"])
print("Character Class: ", character["Character Class"])
print("Backstory: ", character["Backstory"])