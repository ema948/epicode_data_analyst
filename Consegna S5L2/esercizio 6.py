""" abbiamo due liste, una di studenti e una di corsi: 
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"] 
Aggiungere i dati mancanti alla lista corsi, sapendo che 
Emma segue Data Analyst 
Faith segue Backend 
Grace segue Frontend 
Henry segue Cybersecurity
Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in coda alle liste, 
poi verificheremo che sono della stessa lunghezza e se lo sono stamperemo la lista corsi. 
Se alcuni dati sono già presenti non vanno aggiunti di nuovo """
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

nuovi_studenti = ["Grace", "Henry"]
nuovi_corsi = ["Frontend", "Cybersecurity"]
lunghezza = len(nuovi_studenti)
indice = 0
while indice < lunghezza:
    studente = nuovi_studenti[indice]
    corso = nuovi_corsi[indice]
    if studente not in studenti:
        studenti.append(studente)
    if studenti.index(studente) >= len(corsi):
        corsi.append(corso)
    indice += 1
if len(corsi) == len(studenti):
    print(corsi)