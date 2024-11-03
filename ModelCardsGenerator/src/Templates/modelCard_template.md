# {{ modelName }} - v{{ version }}
## General Information 
- Developed by: {{ author }}
- Model Type: {{ modelType }}
- {{ library }} version: {{ libraryVersion }}
- Python version: {{ pythonVersion }}
## Training Details
{% if datasetName %}
- Dataset: {{ datasetName }}
{% endif -%}
{% if parameters -%}
- Parameters: 
    {% for param, val in parameters.items() -%}
    - `{{ param }}` {{ val }}
    {% endfor %}
{% endif -%}
- Training started at: {{ startTime }}
- Training ended at: {{ endTime }}
{% if evaluations -%}
## Evaluation
{% for metric, val in evaluations.items() -%}
- `{{ metric }}` {{ val }}
{% endfor -%}
{% endif -%}