import json
import requests
import logging

from src.handle_data import init_timezone, init_language, init_zone, init_dep

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

REQUEST = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?"

# Initialisation des listes
LANG_LIST = init_language()
TIME_LIST = init_timezone()
REGI_LIST = init_zone()
DEP_LIST = init_dep()

def getData(
    url: str = REQUEST,
    lang: str = "fr",
    timezone: str = "Europe/Paris",
    limit: int = 20,
    offset: int = 0,
    region: str = "Île-de-France",
    departement: str = "Essonne"
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
        logger.debug(f"L'offset '{offset}' n'est pas valide. Il doit être positive.")
        offset = 0
    if region not in REGI_LIST:
        logger.debug(f"La région '{region}' n'est pas disponible. Régions valides : {REGI_LIST}")
        region = "Île-de-France"
    if departement not in DEP_LIST:
        logger.debug(f"Le departement '{departement}' n'est pas disponible. Département : {DEP_LIST}")
        departement = "Essonne"

    request_url = (
        f"{url}"
        f"&lang={lang}"
        f"&offset={offset}"
        f"&timezone={timezone}"
        f"&limit={limit}"
        f"&refine=region:%22{region}%22"
        f"&refine=departement:%22{departement}%22"
    )

    logger.debug(f"URL de la requête : {request_url}")

    response = requests.get(request_url)
    return response


