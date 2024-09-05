import json

# Function to extract key-value pairs from Textract output
def extract_key_value_pairs(textract_output):
    key_map = {}
    value_map = {}
    
    # Extract key-value mappings from the JSON blocks
    for block in textract_output['Blocks']:
        if block['BlockType'] == 'KEY_VALUE_SET' and 'EntityTypes' in block and 'KEY' in block['EntityTypes']:
            key_text = block.get('Key', {}).get('Text')
            if key_text and 'Relationships' in block:
                for relation in block['Relationships']:
                    if relation['Type'] == 'VALUE':
                        key_map[key_text] = relation['Ids'][0]
        
        if block['BlockType'] == 'KEY_VALUE_SET' and 'EntityTypes' in block and 'VALUE' in block['EntityTypes']:
            value_id = block['Id']
            value_text = block.get('Value', {}).get('Text')
            if value_text:
                value_map[value_id] = value_text

    key_value_pairs = {}
    for key, value_id in key_map.items():
        if value_id in value_map:
            key_value_pairs[key] = value_map[value_id]
    
    return key_value_pairs

# Load the JSON file
with open("C:/Users/estra/orders.json", "r") as file:
    textract_output = json.load(file)

# Extract key-value pairs
key_value_pairs = extract_key_value_pairs(textract_output)
print(key_value_pairs)
