from pathlib import Path
FILENAME = "U5.txt"
text = Path(FILENAME).read_text()
lines = text[text.find('\n'):].replace('\n', '')
print('Body of the ' + FILENAME + ' file:')
print(lines[1:])