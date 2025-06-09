import json

input_path = "transforms_train.json"          # 你的原文件
output_path = "transforms_test.json"   # 输出的新文件

with open(input_path, 'r') as f:
    data = json.load(f)

frames = data['frames']
# 每隔10个抽一个，包含第0个：即 0,10,20,...
sampled_frames = frames[::10]

# 更新frames
data['frames'] = sampled_frames

with open(output_path, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Saved sampled transforms to {output_path}, total frames: {len(sampled_frames)}")
