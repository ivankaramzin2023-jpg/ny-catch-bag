with open(r'C:\Users\ivank\Desktop\игра_ловля\game.js', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'pepper' in line.lower() or 'endgame' in line.lower() or 'showresult' in line.lower() or 'reset' in line.lower():
        print(f"L{i+1}: {line.strip()}")
