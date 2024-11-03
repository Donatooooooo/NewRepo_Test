from Utils.exceptions import ParserError
import re

def parser():
    """
    Parse IntegrateSetup.md file and reorganize text in a
    dictionary with model as key and a list of file as value.
    """

    pattern = re.compile(r"^integrate (.+)$")
    
    data = {}
    current = None
    parsing = False
    with open("ModelCardsGenerator/setup/IntegrateSetup.md", "r") as main:
        for line in main:
            line = line.strip()
            
            if line == "## Your Commands Below":
                parsing = True
                continue

            if parsing and not line:
                continue

            if parsing:
                match = pattern.match(line)
                if match:
                    current = match.group(1)
                    data[current] = []
                elif current and line.startswith("/"):
                    data[current].append(line[1:])
                    if "/" in line[1:] or line == "/":  
                        raise ParserError(f"Check line -> {line}")
                elif not current:
                    raise ParserError(f"Check command -> {line}") 
                elif not line.startswith("/"):
                    raise ParserError(f"Check line -> {line}")

        for model in data:
            if not data[model]:
                raise ParserError(f"No files specified for Model Card _{model}_")
            for file in data[model]:
                try:
                    open(f"ModelCardsGenerator/setup/{file}", 'r')
                except FileNotFoundError:
                    raise ParserError(f"{file} doesn't exist")
        
        if not data:
            raise ParserError("No commands provided")

    return data