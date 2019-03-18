from shkronje_edyfisht import shkronje_edyfisht

alfabeti = ['A','B','C','Ç','D','DH','E','Ë','F','G','GJ','H','I','J','K','L','LL','M','N','NJ','O','P','Q','R','RR','S','SH','T','TH','U','V','X','XH','Y','Z','ZH']

def cezari_shqip(fjalia,qelsi):
    list_cezari = []

    tejkalo = False
    for shkronje in list(fjalia.upper()):

        if tejkalo == True:
            tejkalo = False
            continue
        
        try:
            #numri alfabetik i shkronjes ne fjali
            nr_alfabetik = alfabeti.index(shkronje.upper())
            #numri alfabetik i shkronjes qe do te zevendesoje shkronjen ne fjale
            nralf_zevendsimit = nr_alfabetik + qelsi
            
            if shkronje_edyfisht(shkronje.upper(), fjalia):
                nralf_zevendsimit = nralf_zevendsimit + 1
                if nralf_zevendsimit>36:
                    nralf_zevendsimit = nralf_zevendsimit - 36
                list_cezari.append(alfabeti[nralf_zevendsimit])
                tejkalo = True
            else:
                if nralf_zevendsimit>36:
                    nralf_zevendsimit = nralf_zevendsimit - 36
                list_cezari.append(alfabeti[nralf_zevendsimit])
        except ValueError:
            list_cezari.append(shkronje)
    return list_cezari

qelsi = 2
fjalia = 'shoku xhep'
print(cezari_shqip(fjalia,qelsi))