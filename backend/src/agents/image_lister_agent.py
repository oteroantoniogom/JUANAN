from strands import Agent
from strands.tools import tool
import json
import logging
from src.config.config import strands_model_mini
from src.config.prompts import image_lister_system_prompt
from src.tools.file_system_tools import list_files_in_dir, write_file_to_local

# inicializar logger
logger = logging.getLogger(__name__)

@tool()
def image_lister_agent(patient_identifier: str) -> str:
    """
    Tool that acts as an agent to list patient images.
    Takes a patient identifier and returns a JSON string with found image paths.
    
    Args:
        patient_identifier (str): Patient ID in format "Name_LastName1_LastName2"
    
    Tools: 
        - list_files_in_dir(path="data/pictures/"): Lists files in the specified directory.
        - write_file_to_local(path="data/temp/lister.json", content=json_string): Writes the JSON string to a local file.
        
    Returns:
        str: JSON string containing patient_identifier and list of image paths or error
    """
    try:
        lister_agent = Agent(
            model=strands_model_mini,
            tools=[
                list_files_in_dir,
                write_file_to_local,
            ],
            system_prompt=image_lister_system_prompt
        )
        result = lister_agent(patient_identifier)

        # resumen humano al progreso.txt
        logger.info(f"🖼️ Resumen (ImageLister): imágenes listadas para {patient_identifier}. Resultado crudo: {result}")

        return result

    except Exception as e:
        logger.error(f"❌ Resumen (ImageLister): fallo listando imágenes para {patient_identifier} - {str(e)}")
        return json.dumps({
            "patient_identifier": patient_identifier,
            "pictures": [],
            "error": str(e)
        })
