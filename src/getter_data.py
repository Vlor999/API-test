import json
import requests
import logging

from src.handle_data import init_timezone, init_language, init_zone

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

REQUEST = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/records?"

# Initialisation des listes
LANG_LIST = init_language()
TIME_LIST = init_timezone()
ZONE_LIST = init_zone()

def getData(
    url: str = REQUEST,
    lang: str = "fr",
    timezone: str = "Europe/Paris",
    limit: int = 20,
    offset: int = 0,
    region: str = "Île-de-France"
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
    if region not in ZONE_LIST:
        logger.debug(f"La région '{region}' n'est pas disponible. Régions valides : {ZONE_LIST}")
        region = "Île-de-France"

    request_url = (
        f"{url}"
        f"&lang={lang}"
        f"&offset={offset}"
        f"&timezone={timezone}"
        f"&limit={limit}"
        f"&refine=region:%22{region}%22"
    )

    logger.debug(f"URL de la requête : {request_url}")

    response = requests.get(request_url)
    return response


