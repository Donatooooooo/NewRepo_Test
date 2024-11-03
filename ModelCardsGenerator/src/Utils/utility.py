from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import json, os

PATH = "ModelCardsGenerator/src/Templates"

def convertTime(unixTime):
    """
    Convert Unix time in Human Time.
    """
    return datetime.fromtimestamp(unixTime/1000.0).strftime('%H:%M:%S %Y-%m-%d')

def extractInfoTags(tags):
    """
    Extract relevant info fromm tags tracked in MLflow experiment.
    """
    data_tags = json.loads(tags.get('mlflow.log-model.history', ''))
    flavors = data_tags[0]['flavors']
    py_version = flavors['python_function']['python_version']
    lib = str([key for key in flavors.keys() if key != 'python_function'][0])
    lib_version = flavors[lib].get(f'{lib}_version')
    return py_version, lib, lib_version

def extratDatasetName(data):
    """
    Extract a Dataset tracked in a MLflow experiment.
    """

    dataString = str(data)
    start = dataString.find("name='") + len("name='")
    end = dataString.find("'", start)
    return dataString[start:end]

def getPath(data):
    """
    Build a path for saving Model Cards file.
    """
    
    part = data.get("modelName").replace(" ", "")
    fname = f"{part}_v{data.get('version')}.md"
    root = os.path.abspath(os.path.join(os.path.join(os.path.join(
        os.path.dirname(__file__), '..'), '..'), '..'))
    ModelCards_directory = os.path.join(root, 'ModelCards')
    path = os.path.join(ModelCards_directory, fname)
    return path, fname

def templateRender(template, data):
    """
    Render a template.
    """
    
    environment = Environment(loader = FileSystemLoader(PATH))
    template = environment.get_template(template)
    return template.render(data)

def title(string):
    """
    Extract a title from a path.
    """

    if string.endswith('.md'):
        string = string[:-3]
    string = string.capitalize()
    string = string.replace('_', ' ')
    return string

def clean(path):
    """
    Parse a Model Card in order to check if it has been integrated.
    If it is, discard changes.
    """

    allowed_sections = ["## General Information", "## Training Details", "## Evaluation"]
    filtered_content = []
    keep_content = True

    with open(path, 'r') as file:
        for line in file:
            if keep_content and line.startswith("# "):
                filtered_content.append(line)
                keep_content = False
                continue
            
            if line.strip() in allowed_sections:
                keep_content = True
            elif line.startswith("##"):
                keep_content = False
            
            if keep_content:
                filtered_content.append(line)
    
    output = ''.join(filtered_content)
    with open(path, 'w') as modelCard:
        modelCard.write(output)
