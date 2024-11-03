from Utils.logger import Logger
from Utils.parser import parser
from Utils.exceptions import ParserError, ImpossibleIntegration
from Utils.exceptions import NoModelException
from generator import ModelCardGenerator
from mlflow.exceptions import MlflowException


def generator():
    output = Logger("Model Cards Generation")
    try:
        generator = ModelCardGenerator()
        lineage = generator.modelLineage()

        parsedInfo = None
        try:
            parsedInfo = parser()
        except ParserError as e:
            output.error(f"Invalid file format in IntegrateSetup.md: {str(e)}. Could not integrate")

        for model in lineage:
            generator.ModelCard(model, parsedInfo)

        output.merge(generator.getOutput())
    except MlflowException as e:
        output.error(f"Check MLflow Server status: {str(e)}")
    except NoModelException as e:
        output.error(f"Check if models exist: {str(e)}")
    except FileNotFoundError as e:
        output.error(f"Check file path, {str(e).split('] ')[1]}")
    except Exception as e:
        output.error(f"Exception caused by: {str(e)}")
    finally:
        output.display()


def integrator():
    output = Logger("Model Cards Integration")
    try:
        generator = ModelCardGenerator()
        
        parsedInfo = parser()
        generator.forceIntegrate(parsedInfo)

        output.merge(generator.getOutput())
    except MlflowException as e:
        output.error(f"Check MLflow Server status: {str(e)}")
    except ParserError as e:
        output.error(f"Invalid file format in IntegrateSetup.md: {str(e)}. Unable to integrate")
    except ImpossibleIntegration as e:
        output.error(str(e))
    except FileNotFoundError as e:
        output.error(f"Check file path, {str(e).split('] ')[1]}")
    except Exception as e:
        output.error(f"Exception caused by: {str(e)}")
    finally:
        output.display()


#------------------------------------------------------------------------------------------
import sys

if __name__ == "__main__":
    try:
        if sys.argv[1] == "0":
            generator()
        elif sys.argv[1] == "1":
            integrator()
    except Exception:
        sys.exit(1)