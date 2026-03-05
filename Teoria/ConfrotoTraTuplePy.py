
"""
Confronto tra Tuple
Le tuple sono strutture dati immutabili che possono contenere elementi di diversi tipi.
In Python, è possibile confrontare le tuple utilizzando gli operatori di confronto standard

In seguito una dimostrazione di confronto tra tuple, con tutte le situazioni
"""

print( (10, 12) < (8, 1234567) ) # confronta i primi elementi
print( (10, 12) < (18, 1234567) )
print( (10, 12) < (10, 1234567) ) # Nel caso i primi valori uguali confronta i secondi
print( (10, 12) < (10, 12, 0) ) # Nel caso una delle due tuple finisce prima viene confrontata la lunghezza
print( (10, "uno") < (10, "due") ) # Confronta "uno" < "due" e determina in base al valore ascii

