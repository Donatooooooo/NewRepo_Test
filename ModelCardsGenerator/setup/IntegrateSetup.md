# Use this file to integrate your Model Card
## How to use
1. Each Model Card to be integrated should be specified with the command `integrate _model name_`, where _model name_ is the name of the model you want to create documentation. This command can be repeated each time you want to integrate a new Model Card.

2. Under this command, list the files to be included in that specific Model Card. Each file should be indicated on a new line and should be preceded by `/`. Files must be located in the directory _/ModelCardGenerator/Data_. The files listed under each Model Card will be integrated into the final document in the order they appear. Ensure they are arranged in the desired sequence.

Here an example:
```
integrate KNN
    /introduction.md
    /details.md
    /intended_usage.md

integrate Random Forest
    /overview.md
    /how_tu_use.md
    /limitations.md
```

3. If errors occurred when creating the model card and it was not automatically integrated you can force the integration by specifying the version immediately after the model name.Here an example:
```
integrate KNN 3
    /introduction.md
    /details.md
    /intended_usage.md
```

## Your Commands Below

