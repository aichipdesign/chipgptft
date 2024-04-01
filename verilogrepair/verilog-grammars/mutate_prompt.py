import json


def generate_training_data(input_file, index_info, output_json, modifier_func_type):
    modifier = VerilogCodeModifier(input_file, index_info)

    data = []
    instruction = "This input is not a bug-free code. Please read the code and try to summarize the bug information."
    modified_code = modifier.modify_code()
    modifier_func_desc = [
        "The port list was modified.",
        "Modified the width of the port.",
    ]
    output = modifier_func_desc[modifier_func_type]
    prompt = {
        "instruction": instruction,
        "input": modified_code,
        "output": output
    }
    data.append(prompt)

    with open(output_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)


generate_training_data(argv[1], index_info, 'training_data.json', 0)