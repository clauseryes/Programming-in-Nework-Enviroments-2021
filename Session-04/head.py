from pathlib import Path
FILENAME = "RNU6_269P.txt"
text = Path(FILENAME).read_text()
lines = text.split('\n')
print('First line of the ' + FILENAME + ' file:')
print(lines[0])