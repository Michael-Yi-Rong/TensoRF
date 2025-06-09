import json
import os

path = "transforms_train.json"
with open(path, 'r') as f:
    data = json.load(f)

for frame in data['frames']:
    old = frame['file_path']
    filename = os.path.basename(old)  # 提取 001.jpg 或 001
    if not filename.endswith('.jpg'):
        filename += '.jpg'
    frame['file_path'] = f'images/{filename}'

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
