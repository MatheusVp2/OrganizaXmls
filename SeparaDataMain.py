from lxml import etree
from Controler import *
import time

inicio = time.time()
print("Organizando Pasta Aguarde ...")

for filename in os.listdir():
    if filename.endswith('.xml'):
        # Trata o Erro de Arquivo Vazio
        try:
            root = etree.parse(filename).getroot()
        except Exception as erro:
            print( "[ERRO Arquivo Vazio] {}".format( erro ) )
            continue
        
        # Trata se não tiver a tag com as informações da Nota
        try:
            infNFe  = root[0][0]
            infProt = root[1][0]
        except Exception as erro:
            print( "[ERRO Nota Info] {}".format( erro ) )
            continue

        # Se a nota tiver a tag de Autorização  
        if rmvTag(infNFe.tag) == "infNFe":
            if rmvTag(infProt.tag) == "infProt":
                for i in infProt:
                    if rmvTag( i.tag ) == "dhRecbto":
                        date_list = format_DATA(i.text).split('/')
                        pathData  = "XML {}-{}".format( date_list[1], date_list[2] )
                        moveData( filename, pathData )
        
        # Se não tiver Autorização
        else:
            date_list = format_DATA( infNFe[6].text ).split('/')
            pathData  = "XML {}-{}".format( date_list[1], date_list[2] )
            moveNaoAutorizada(filename, pathData)

final = time.time()

print("Organização Terminada em : {} ".format( final - inicio ))
input("Pressione Alguma Tecla para Continuar ...")