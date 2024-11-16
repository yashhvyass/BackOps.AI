import logging

logger = logging.getLogger('app_logger')
logging.basicConfig(filename='myapp.log', level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")