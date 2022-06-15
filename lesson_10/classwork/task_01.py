"""
Создать функцию при помощи регулярных выражений для проверки, что строка является валидным телефонным номером в формате
+375 (29) 299-29-29.
"""
import re
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def valid_phone_number(phone_number: str) -> bool:
    match = re.findall(r"\+\d{3} \(\d{2}\) \d{3}-\d{2}-\d{2}", phone_number)
    return True if match else False


if __name__ == '__main__':
    # output = valid_phone_number("+375 (29) 299-29-29")
    for item in ("+375 (29) 299-29-29 ", "+375 (29) 299-29-29 "):
        assert valid_phone_number("+375 (29) 299-29-29") is True
    logger.info("All tests are OK.")