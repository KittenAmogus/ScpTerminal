import csv
from functools import lru_cache
from random import randint
import time

"""
'code',
'title',
'text'
'image captions',
'rating',
'state',
'tags',
'link'
"""

csv.field_size_limit(131_072 * 10)


loaded = {}


def tprint(*args, end="\n\r"):
    for i, arg in enumerate(args):
        arg = str(arg)
        for l in arg:
            print(l, end="", flush=True)
            time.sleep(0.0025)

        if i + 1 < len(args):
            print(" ", end="")
    print(end=end)


def tinput(prompt):
	tprint(prompt, end="")
	return input()


def getElement(num):
    
	if not (0 < num <= 6999):
		return None

	if loaded.get(num) is not None:
		return loaded.get(num)

	with open("scp6999.csv", "r", newline="") as file:
		reader = csv.DictReader(file)
		for index, row in enumerate(reader):
			loaded[index] = row
			if index == num:
				return row


def formatElement(element: dict):
	if not element:
		return {}
	
	formated = {}

	formated["code"] = element.get("code")
	formated["title"] = element.get("title").strip(' "').replace('"', '')
	text = element.get("text")
    


	if text is not None:
		text = text.split("\n")
		for t in text:
			if "Object Class:" in t:
				formated["class"] = t.split(": ")[-1]
			elif "Special Containment Procedures:" in t:
				formated["containment"] = "\n".join(t.split(": ")[1:])
			elif "Description:" in t:
				formated["description"] = "\n".join(t.split(": ")[1:])

	return formated


ar = {
		# "code": "Code",
		# "title": "Title",
		"description": "Description",
		"containment": "Special Containment Procedures"
		# "class": "Object Class"
		}


def getColoredClass(class_):
	if not class_:
		return "None"

	b = class_.split(" ")

	a = class_
	for i in b[::-1]:
		if i in ("Safe", "Euclid", "Keter", "Thaumiel"):
			a = i
			break

	if "Safe" in a:
		return "\x1b[1;92m" + a + "\x1b[92m"

	if "Euclid" in a:
		return "\x1b[93m" + a + "\x1b[92m"

	if "Keter" in a:
		return "\x1b[91m" + a + "\x1b[92m"

	if "Thaumiel" in a:
		return "\x1b[95m" + a + "\x1b[92m"

	return "\x1b[96m" + class_ + "\x1b[92m"


def printElement(element: dict):
    
	for i in ar.keys():
		element[i] = element.get(i)

	if not element.get('code') or not element.get('title'):
		return None

    
	tprint("-" * 10)
	tprint(f"{element['code']}: ", end="")
	tprint(f"{element['title']}")

	if element.get('class', None):
		tprint("\x1b[94mClass:", getColoredClass(element['class']))
	print("\x1b[0;92m")

	for i, v in ar.items():
		if element[i]:
			tprint(f"\x1b[94m{v}:\x1b[0m\n")
			print("\x1b[92m")
			
			for line in element[i]:
				tprint(line, end="")
			
			print()
			print()
	
	print("\x1b[0m")


def hash_(string):
	return len(string) ** 5 * 152123 % (10 ** 20)


def main():
	import sys
	import os
	size = os.get_terminal_size()
	del os

	try:
		tprint("""\x1b[H\x1b[2J\x1b[3J\x1b[92m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠈⠀⠁⠈⠀⠉⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⠶⠛⠀⠀⠀⠀⠀⠀⠀⠘⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⠛⠁⠀⠀⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⠈⠛⣦⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡞⠋⠀⠀⢀⣤⣶⠿⠟⣿⡟⠻⠷⣦⣄⠀⠀⠀⠙⢷⡀⠀⠀⠀
⠀⠀⢀⡟⠀⠀⠀⣰⡿⠋⠀⠀⠀⣿⡇⠀⠀⠈⠙⣷⣄⠀⠀⠈⢿⡀⠀⠀
⠀⠀⣾⠀⠀⠀⣼⡏⠀⠀⠀⠀⠘⣿⡿⠃⠀⠀⠀⠈⢿⣇⠀⠀⠈⣧⠀⠀
⠀⢰⣿⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⣿⠀⠀
⠀⢸⡷⠀⠀⠀⣿⡆⠀⢀⣶⣷⡖⠀⠀⢶⣶⣆⡀⠀⢸⣿⠀⠀⠀⣿⡀⠀
⣴⠋⠀⠀⠀⢀⣻⣷⡾⠟⠉⠛⠀⠀⠀⠈⠏⠙⠻⢷⣾⣇⠀⠀⠀⠈⢻⣦
⠘⢧⡀⠀⠀⠀⠛⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠋⠋⠀⠀⠀⢀⡼⠁
⠀⠘⣧⠀⠀⠀⠀⠀⠀⠛⠿⣧⣤⣤⣤⣤⣿⠿⠛⠀⠀⠀⠀⠀⠀⡿⠃⠀
⠀⠀⠘⢷⣀⣠⣤⣀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⣠⣤⣄⣠⡾⠁⠀⠀
⠀⠀⠀⠈⠉⠀⠀⠙⠳⠶⣤⣀⣀⣀⣀⣀⣠⡤⠶⠞⠃⠀⠀⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Secure. Contain. Protect.

⠀""")

		name = tinput("Name: ").capitalize()
		surname = tinput("Surname: ").capitalize()
		tprint(f"""
+----+
| () | {surname}, {name}
|/  \\| ID: {hash_(surname + name)}
+----+
""")
		print()
		while True:
			try:
				inp = tinput(f"\x1b[92m{name.lower()}@scp-142 $ ").lower()
				if inp == "":
					continue
				if inp == "exit":
					raise EOFError
				elif inp == "clear":
					tprint("\x1b[H\x1b[2J\x1b[3J", end="")
				elif inp == "cacheclear":
					loaded.clear()
				elif inp == "cachesize":
					tprint(f"Cache size: {sys.getsizeof(loaded) // 1024}kb")
				elif inp == "help":
					tprint("""
Help menu:
	HELP	- Print this menu
	EXIT	- Disconnect
	CLEAR	- Clear screen
	CACHECLEAR	- Clear cache
	CACHESIZE	- Print cache size
	GET <SCP ID>	- get scp data
""")

				elif inp.startswith("get"):
					try:
						inp = inp.removeprefix("get")
						inp = int(inp.lstrip(" scp-0"))

						print("\n")
						printElement(formatElement(getElement(inp - 1)))

					except ValueError:
						tprint("Invalid id")

				else:
					tprint(f"Invalid command, type 'help'")

			except EOFError:
				tprint("\nexit")
				break
			except KeyboardInterrupt:
				tprint("\nexit")
				break
	
	except KeyboardInterrupt:
		tprint("Interrupted!\x1b[0m")
		return


if __name__ == "__main__":
	main()

