import traceback
import xml.etree.ElementTree as ET
import pandas as pd
import logging
import test_calc

def fileLogging():
    """Initialize basic configuration for logging."""
    logging.basicConfig(
        filename="test.txt",
        filemode='w',
        format='[%(asctime)s:%(levelname)s] : [%(filename)s:%(lineno)d] : %(message)s',
        level=logging.INFO
    )
#Parse XML file
def get_root_xml(xml):
    """This Function will betaking the XML file as an argument and returns its root element."""
    if xml is None:
        log = "XML file is None."
        logging.info(log)
        return None
    try:
        tree = ET.parse(xml)
        root = tree.getroot()
        logging.info(msg="Root initiated")
        return root
    except Exception as e:
        error = f"{str(e)} {traceback.format_exc()}"
        logging.error(error)
        return None

def xml_to_csv(rows,cols):
    df = pd.DataFrame(rows, columns=cols)
    logging.info(msg="Data frame created")
    logging.debug(df.to_csv('DLTINS_20210117_01of01.csv', index=False))
    return df

if __name__=='__main__':
    fileLogging()
    # Initializing Column names.
    cols = ["Id",
            "FullNm",
            "ClssfctnTp",
            "CmmdtyDerivInd",
            "NtnlCcy",
            "Issr"]
    rows = []
    # variable to store "Root" of the xml file.
    root = get_root_xml("DLTINS_20210117_01of01.xml")

    try:
        # Initializing variable m for iteration of FinInstrm tags
        m = 1
        # while loop to iterate through all fininstrm tags.
        while(m<len(root[1][0][0])):
            # Initializing variable i for iteration to find column datas
            i = 0
            # loop to loop into FinInstrmGnlAttrbts tags to get header files.
            while i<6:
                if i == 0:
                    Id = root[1][0][0][m][0][0][i].text
                elif i == 1:
                    FullNm = root[1][0][0][m][0][0][i].text
                elif i == 3:
                    ClssfctnTp = root[1][0][0][m][0][0][i].text
                elif i == 4:
                    NtnlCcy = root[1][0][0][m][0][0][i].text
                elif i == 5:
                    CmmdtyDerivInd = root[1][0][0][m][0][0][i].text
                i += 1         # Increment i
            # To get issr tag text
            Issr = root[1][0][0][m][0][1].text
            rows.append({"Id":Id,"FullNm":FullNm,
                         "ClssfctnTp":ClssfctnTp,
                         "NtnlCcy":NtnlCcy,
                         "CmmdtyDerivInd":CmmdtyDerivInd,
                         "Issr":Issr}
                       )
            m += 1           # Increment m
    except Exception as e:
        error = f"{str(e)} {traceback.format_exc()}"
        logging.error(msg=error)
    df = xml_to_csv(rows=rows,cols=cols)
