with open(r'C:\Users\ivank\Desktop\игра_ловля\style.css', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'result' in line.lower():
        print(f"L{i+1}: {line.strip()}")
