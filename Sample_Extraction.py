import json
import os
from tqdm import tqdm

def sample_json(input_file, output_file, target_size_gb, filter_key='also_buy'):
    target_size_bytes = target_size_gb * 1024 ** 3
    current_size_bytes = 0

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in tqdm(infile):
            record = json.loads(line)
            if record.get(filter_key):
                outfile.write(json.dumps(record) + '\n')
                current_size_bytes += len(line.encode('utf-8'))

            if current_size_bytes >= target_size_bytes:
                break

input_file = 'All_Amazon_Meta.json'
output_file = 'Sample_Amazon_Meta.json'

sample_json(input_file, output_file, target_size_gb=15, filter_key='also_buy')
