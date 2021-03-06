# This script downloads weekly dengue statistics from data.gov.bn
import os
import sys
import logging


DIRECTORY = '../../Data/raw/disease_BN'
OUTFILE = "Trend of Notifiable Diseases (2008 - 2012).xlsx"
URL = "https://www.data.gov.bn/Lists/dataset/Attachments/460/Trend%20of%20Notifiable%20Diseases%20(2008%20-%202012).xlsx"

logger = logging.getLogger(__name__)


def download():

    if sys.version_info < (3, 0):
        try:
            os.makedirs(DIRECTORY)
        except OSError as e:
            pass
        import urllib as downloader
        from urllib2 import URLError, HTTPError
    else:
        os.makedirs(DIRECTORY, exist_ok=True)
        import urllib.request as downloader
        from urllib.error import URLError, HTTPError

    output_path = os.path.join(DIRECTORY, OUTFILE)

    try:
        downloader.urlretrieve(URL, output_path)
        logger.info('Downloaded successfully to %s', os.path.abspath(output_path))
    except (HTTPError, URLError) as e:
        logger.error('Failed to download: %s', e.reason)


if __name__ == "__main__":
    DIRECTORY = '../../../Data/raw/disease_BN'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    download()