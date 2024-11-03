class Logger:
    """
    Collects messages, dividing them into logs, alerts and errors, 
    and displays them formattin in .md style at the end of execution.
    """

    def __init__(self, context = ""):
        self.context = context
        self.messages = []
        self.alerts = []
        self.errors = []
        self.output = ""


    def log(self, msg):
        self.messages.append(msg)


    def warning(self, msg):
        self.alerts.append(msg)


    def error(self, msg):
        self.errors.append(msg)


    def display(self):
        self.output = f"# {self.context}\n"
        
        if self.messages:
            self.output += f"## ✅ Model Cards ready\n More details:\n"
            self.output += "```\n"
            for msg in self.messages:
                self.output += f"{msg};\n"
            self.output += "```\n"

        if self.errors:
            self.out("❌ Errors", self.errors)

        if self.alerts:
            self.out("⚠️ Warnings", self.alerts)
            
        print(self.output)


    def out(self, type, messages):
        self.output += f"## {type}\n"
        for i, msg in enumerate(messages):
            self.output += f"{i + 1}. {msg};\n"


    def merge(self, logger):
        self.messages.extend(logger.messages)
        self.alerts.extend(logger.alerts)
        self.errors.extend(logger.errors)
