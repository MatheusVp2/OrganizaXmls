from datetime import datetime
import dateutil.parser
import os, shutil


def rmvTag(formato):
	base = "{http://www.portalfiscal.inf.br/nfe}"
	return formato.replace(base, '')

def format_DATA(bd_data):
	return datetime.strftime(dateutil.parser.parse(bd_data).date(), '%d/%m/%Y')


def moveData(filename, dataPath):
    # Se a pasta nao existir ele cria
    if not os.path.exists( dataPath ):
        os.mkdir(dataPath)
    # Move para nova pasta
    shutil.move(filename, dataPath)


def moveNaoAutorizada(filename, dataPath):
    path = "NAO AUTORIZADAS"
    # Se a pasta nao existir ele cria
    if not os.path.exists( path ):
        os.mkdir(path)

    newPath = "{}/{}".format( path, dataPath )
    # Se a pasta nao existir ele cria
    if not os.path.exists( newPath ):
        os.mkdir(newPath)

    shutil.move(filename, newPath)
    

