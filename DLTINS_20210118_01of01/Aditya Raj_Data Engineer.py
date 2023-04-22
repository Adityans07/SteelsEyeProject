import xml.etree.ElementTree as ET
import pandas as pd
import logging
import test
logging.basicConfig(filename="test.log",level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Initializing Column names.
cols = ["Id",
        "FullNm",
        "ClssfctnTp",
        "CmmdtyDerivInd",
        "NtnlCcy",
        "Issr"]
rows = []

#Parse XML file
tree = ET.parse('DLTINS_20210118_01of01.xml')
root = tree.getroot()
logging.info(msg="Root initiated")
# Initializing variable m for iteration of FinInstrm tags
m = 1
while(m<len(root[1][0][0])):
    # Initializing variable i for iteration to find column datas
    i = 0
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
    Issr = root[1][0][0][m][0][1].text
    rows.append({"Id":Id,"FullNm":FullNm,
                 "ClssfctnTp":ClssfctnTp,
                 "NtnlCcy":NtnlCcy,
                 "CmmdtyDerivInd":CmmdtyDerivInd,
                 "Issr":Issr}
               )
    m += 1           # Increment m
logging.info(msg="Rows created")
df = pd.DataFrame(rows, columns = cols)
logging.info(msg="Data frame created")
logging.debug(df.to_csv('DLTINS_20210118_01of01.csv',index = False))