from pathlib import Path

path = Path()
print()
for file in path.glob('*'):
    print(file)