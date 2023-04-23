"""
@author : Aditya Raj
"""

import io
import xml.etree.ElementTree as ET
import zipfile
import requests


def download_xml():
    url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"

    response = requests.get(url)

    xml_content = response.content

    root = ET.fromstring(xml_content)

    # loop through each <doc> tag and extract the download link
    for doc in root.findall('./result/doc'):
        download_link = doc.find("./str[@name='download_link']").text
        if (download_link):
            break

    # Download the zip file
    response = requests.get(download_link)

    # Extract the contents of the zip file
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    xml_filename = zip_file.namelist()[0]  # Assume there's only one file in the zip
    xml_content = zip_file.read(xml_filename).decode("utf-8")
if __name__ =='__main__':
    download_xml()


