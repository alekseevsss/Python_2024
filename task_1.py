import json

INPUT_FILE = "input.json"
def task() -> float:
    with open (INPUT_FILE, 'r') as input_file:
        json_data = json.load(input_file)
        list_values = [item["score"] * item["weight"] for item in json_data]
        return round(sum(list_values), 3)


print(task())
