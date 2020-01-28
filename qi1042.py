from split import *

def import_split_1042(fire_file):

    with open(fire_file,'r') as f:
        fire = f.read()
    
    # split file per line, as every "record" is a single line 1:n
    fire = fire.split('\n')
 
    class Block:

        def __init__(self,fire):
            self.fire = fire

        def TRec(self):
            tAry = []
            tAry = [el for el in fire if el.startswith('T')]
            return(tAry)

        def WRec(self):
            wAry = []
            wAry = [el for el in fire if el.startswith('W')]
            return(wAry)

        def QRec(self):
            qAry = []
            qAry = [el for el in fire if el.startswith('Q')]
            #d = {}
            #d = { el: qsplit(el) for el in qAry }
            return(qAry)

        def CRec(self):
            cAry = []
            cAry = [el for el in fire if el.startswith('C')]
            return(cAry)

        def FRec(self):
            fAry = []
            fAry = [el for el in fire if el.startswith('F')]
            return(fAry)

    block1 = Block(fire)

    all_q_records = {}
    for i in range(0,len(block1.QRec())):
        all_q_records[i] = qsplit(block1.QRec()[i])

    keys = [key for key,val in all_q_records[0].items()]

    return(all_q_records,keys)