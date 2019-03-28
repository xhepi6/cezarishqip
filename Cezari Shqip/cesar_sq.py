#OVERCOMMENTED WHATEVER...
#Importimi i funksionit per te dalluar shkronjat e dyfishta ne gjuhen shqipe
from shkronje_edyfisht import shkronje_edyfisht
import os

#Alfabeti i gjuhes shqipe
alfabeti = ['A','B','C','Ç','D','DH','E','Ë','F','G','GJ','H','I','J','K','L','LL','M','N','NJ','O','P','Q','R','RR','S','SH','T','TH','U','V','X','XH','Y','Z','ZH']

#Funksioni qe merr tekstin dhe qelesin dhe kthen tekstin e enkriptuar
def cezari_shqip(teksti,qelsi):
    print('brenda cezari_shqip()')
    list_cezari = []

    tejkalo = False
    for shkronje in list(teksti.upper()):
        print('shkronja qe po enkriptohet:', shkronje)
        #Neqoftese kjo variabel eshte true 'iteratori' eshte momentalisht ne
        #  shkronje te dyfisht qe veqse eshte enkriptuar
        if tejkalo == True:
            tejkalo = False
            continue
        
        try:
            #Numri alfabetik i shkronjes ne fjali
            nr_alfabetik = alfabeti.index(shkronje.upper())
            #Numri alfabetik i shkronjes qe do te zevendesoje shkronjen ne fjale
            nralf_zevendsimit = nr_alfabetik + qelsi
            
            #Nese eshte shkronje e dyfisht numri alfabetik dallon per 1 
            if shkronje_edyfisht(shkronje.upper(), teksti):
                nralf_zevendsimit = nralf_zevendsimit + 1
                #Ky kusht sherben kur numri alfabetik tejkalon numrin e shkronjave te alfabetit
                #prandaj kur tejkalon kthehemi prap nga fillimi i alfabetit(per shkronja te dyfishta)
                if nralf_zevendsimit>35:
                    nralf_zevendsimit = nralf_zevendsimit - 35
                print('shkronja u enkriptua me: ', alfabeti[nralf_zevendsimit])
                list_cezari.append(alfabeti[nralf_zevendsimit])
                # nje variabel qe tregon se shkronja momentale eshte pjes e shkronjes se dyfisht
                #  dhe duhet tejkaluar
                tejkalo = True 
            else:
                #Ky kusht sherben kur numri alfabetik tejkalon numrin e shkronjave te alfabetit
                #prandaj kur tejkalon kthehemi prap nga fillimi i alfabetit
                if nralf_zevendsimit>35:
                    nralf_zevendsimit = nralf_zevendsimit - 35
                print('shkronja u enkriptua me: ',alfabeti[nralf_zevendsimit])
                list_cezari.append(alfabeti[nralf_zevendsimit])
        except ValueError:
            #Nese karakteri nje tekst nuk eshte pjes e alfabetit
            # nuk enkriptohet por thjesht shtohet ne tekstin e enkriptuar
            print('shkronja nuk u zevendesua ', shkronje)
            list_cezari.append(shkronje)
    print('enkriptimi i tekstit perfundoi')
    return list_cezari

def enkripto_dokumentin(path, filename, qelesi):
    print('brenda enkripto_dokumentin() ', path)
    txt_file = open(path,'r')
    print('txt_file u hap')
    text = txt_file.read()
    txt_file.close()
    print('txt_file u mbyll')
    #funksioni i enkriptimit kthen list
    teksti_list_enkriptuar = cezari_shqip(text, qelesi)
    print('teksti u enkriptua')
    #bashkojme listen
    teksti_enkriptuar = ''.join(teksti_list_enkriptuar)
    directory = os.path.split(path)[0]
    save_file = open( os.path.join(directory,filename),'w')
    print('u krijua file i ri')
    save_file.write(teksti_enkriptuar)
    save_file.close()
    #file i ri veqse eshte mbyll dhe ruajtur ne direktorin se ku 
    # ka qen file-i paraprak me emrin filename
    print('file i ri u mbyll')


"""
try:
    #Nese shtyp diqka tjeter perveq numer qelesi merr vleren 2
    qelesi = int(input('Shkruani qelesin: '))
except ValueError:
    qelesi = 2
"""

#teksti_enkriptuar = cezari_shqip(teksti, qelesi)

