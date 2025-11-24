def argmax(L):
        
        '''
         Paramentri L: Lista di numeri

         Ritorna la posizione del maggiore tra i numeri
        '''

        cur_max, pos = None, None
        
        for i, x in enumerate(L):
            if  cur_max == None or x > cur_max:
                cur_max, pos = x, i

        return pos