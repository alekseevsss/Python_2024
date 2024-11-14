import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_file:
        reader = csv.DictReader(input_file)
        data_json = []
        for row in reader:
            data_json.append(row)
        json_output = json.dumps(data_json, indent=4, ensure_ascii=False)
        with open(OUTPUT_FILENAME, 'w') as output_file:
            output_file.write(json_output)
            return json_output

task()

if __name__ == '__main__':
    # Нужно для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")








