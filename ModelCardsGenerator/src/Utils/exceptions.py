class NoModelException(Exception):
    """
    Exception being raised if no model or experiment is found in MLflow.
    """
    def __init__(self, info):
        super().__init__(info)

class ParserError(Exception):
    """
    Exception that is raised if there are syntactic errors in the parsed file.
    """
    def __init__(self, info):
        super().__init__(info)
        
class ImpossibleIntegration(Exception):
    """
    Exception being raised if is not possible to integrate a Model Card.
    """
    def __init__(self, info):
        super().__init__(info)