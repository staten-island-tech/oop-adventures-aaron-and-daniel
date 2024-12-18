import json
import os

class new_question:
    def __init__(self, question):
        self.question = question
    def newest(self):
        self.question = input("question: ")
        return {"question": self.question}

q = new_question("")
s = q.newest()

# Create a new JSON file with the updated data
new_file = "updated.json"
with open("./json/q.json", "r") as f:
    data = json.load(f)

data.append(s)

with open(new_file, "w") as f:
    json_string = json.dumps(data, indent=4)  
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("./json/q.json")
os.rename(new_file, "./json/q.json")
