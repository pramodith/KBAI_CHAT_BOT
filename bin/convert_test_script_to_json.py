# Quick and dirty script to convert .txt to .json test scripts
import os
import json

def escape(input):
    return json.dumps(input) #.replace('"', '\\"')


def convert_to_json(input_name, output):
    output.write('[\n')
    with open(input_name, "r", encoding="utf-8") as input:
        first = True
        for line in input:
            if first:
                first = False
            else:
                output.write(',\n')
            output.write('  {\n')
            question, answer = line.strip().split('?')
            output.write('    "questions": [')
            output.write(escape(question))
            output.write('],\n')
            output.write('    "response": ')
            if answer.endswith('.'):
                output.write(escape(answer))
            else:
                output.write(escape(answer + '.'))
            output.write('\n')
            output.write('  }')
        output.write('\n')
        output.write(']\n')

# Change this code for other scripts, it also tests the json to mkae sure it is well-formed
for each_name in ['Fall2017syllabusFAQ.txt', 'AlternateTestScript.txt', 'TestScript.txt', 'TestScript3.txt']:
    # I run this from a bin dir with the parent dir having the .txt test scripts
    full_name = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', each_name))
    output_name = os.path.splitext(full_name)[0]+'.json'

    #convert
    with open(output_name, "w", encoding="utf-8") as output:
        convert_to_json(full_name, output)

    #test
    with open(output_name, "r", encoding="utf-8") as json_data:
        autograder_test_script_as_list_of_dicts = json.load(json_data)
        for qa_dict in autograder_test_script_as_list_of_dicts:
            pass