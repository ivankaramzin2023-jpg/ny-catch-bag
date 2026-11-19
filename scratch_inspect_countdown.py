with open(r'C:\Users\ivank\Desktop\игра_ловля\game.js', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'countdown' in line.lower() or 'cnt3' in line.lower():
        print(f"L{i+1}: {line.strip()}")
