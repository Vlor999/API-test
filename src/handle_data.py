import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TIMEZONE_FILE = "data/timezone.xml"


def init_timezone() -> set[str]:
    timezone = set()
    tree = ET.parse(TIMEZONE_FILE)
    root = tree.getroot()
    for child in root.iter('type'):
        if 'alias' in child.attrib:
            timezone.add(child.attrib['alias'])
    return timezone

def init_language() -> set[str]:
    output_set = set()
    output_set.update(["en", "fr", "nl", "pt", "it", "ar", "de", "es", "ca", "eu", "sv"])
    return output_set

def init_zone() -> set[str]:
    # TODO
    return set()

def init_dep() -> set[str]:
    # TODO
    return set()