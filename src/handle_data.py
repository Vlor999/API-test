import xml.etree.ElementTree as ET
import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TIMEZONE_FILE = "data/timezone.xml"

def init_timezone() -> set[str]:
    logger.debug("Initializing timezone set from file: %s", TIMEZONE_FILE)
    timezone = set()
    try:
        tree = ET.parse(TIMEZONE_FILE)
        root = tree.getroot()
        for child in root.iter('type'):
            if 'alias' in child.attrib:
                timezone.add(child.attrib['alias'])
        logger.debug("Timezone set initialized with %d entries", len(timezone))
    except Exception as e:
        logger.error("Error initializing timezone set: %s", e)
    return timezone

def init_language() -> set[str]:
    logger.debug("Initializing language set")
    output_set = set()
    output_set.update(["en", "fr", "nl", "pt", "it", "ar", "de", "es", "ca", "eu", "sv"])
    logger.debug("Language set initialized with %d entries", len(output_set))
    return output_set

def verify_dep_region_files(departement: str = None, region: str = None) -> bool:
    logger.debug("Verifying department and region files with departement=%s, region=%s", departement, region)
    if departement is None or region is None:
        logger.warning("Departement or region is None")
        return False
    try:
        filename = "data/dep-region-data.json"
        logger.debug("Opening file: %s", filename)
        with open(filename) as f:
            data = json.load(f)
        for region_dep in data:
            if region_dep['nom'] == departement and region_dep['region']['nom'] == region:
                logger.debug("Match found for departement=%s and region=%s", departement, region)
                return True
        logger.debug("No match found for departement=%s and region=%s", departement, region)
    except Exception as e:
        logger.error("Error verifying department and region files: %s", e)
        return False
    return False
