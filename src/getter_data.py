import json
import requests
import logging

from src.handle_data import init_timezone, init_language, verify_dep_region_files
from src.writter_data import write_data

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

REQUEST = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?"

# Initialisation des listes
LANG_LIST = init_language()
TIME_LIST = init_timezone()

def verify_dep_region(departement: str = None, region: str = None) -> bool:
    if not departement or not region:
        logger.debug("Le département ou la région n'est pas spécifié.")
        return False
    
    if verify_dep_region_files(departement, region):
        return True

    lien = "https://geo.api.gouv.fr/departements"
    try:
        response = requests.get(lien, params={"fields": "code,nom,region", "format": "json"})
        if response.status_code == 200:
            departements = response.json()
            write_data("data/dep-region-data", departements)
            for dep in departements:
                if dep.get("nom") == departement and dep.get("region", {}).get("nom") == region:
                    return True
        else:
            logger.error(f"Erreur lors de la requête à l'API : {response.status_code}")
    except requests.RequestException as e:
        logger.error(f"Exception lors de la requête à l'API : {e}")
    return False

def getData(
    url: str = REQUEST,
    lang: str = "fr",
    timezone: str = "Europe/Paris",
    limit: int = 20,
    offset: int = 0,
    region: str = None,
    departement: str = None
) -> requests.models.Response:

    if lang not in LANG_LIST:
        logger.debug(f"La langue '{lang}' n'est pas disponible. Langues valides : {LANG_LIST}")
        lang = "fr"
    if timezone not in TIME_LIST:
        logger.debug(f"Le fuseau horaire '{timezone}' n'est pas disponible. Fuseaux valides : {TIME_LIST}")
        timezone = "Europe/Paris"
    if limit < 1:
        logger.debug(f"La limite '{limit}' n'est pas valide. Elle doit être supérieure à 0.")
        limit = 1
    if offset < 0:
        logger.debug(f"L'offset '{offset}' n'est pas valide. Il doit être positif.")
        offset = 0

    if region and departement and not verify_dep_region(departement=departement, region=region):
        logger.debug(f"Le département '{departement}' ne correspond pas à la région '{region}'.")
        region = None
        departement = None

    request_url = f"{url}&lang={lang}&offset={offset}&timezone={timezone}&limit={limit}"

    if region:
        request_url += f"&refine=region:%22{region}%22"
    if departement:
        request_url += f"&refine=departement:%22{departement}%22"

    logger.debug(f"URL de la requête : {request_url}")

    response = requests.get(request_url)
    return response


