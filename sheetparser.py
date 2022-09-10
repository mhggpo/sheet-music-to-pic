#sheet music to array

from typing import *
import re

class SheetParser:
    def __init__(self) -> None:
        self.sheet_convert_table={
            '0': 0, 
            '1': 1, 
            '#1': 2, 
            '2': 3, 
            '#2': 4, 
            '3': 5, 
            '4': 6, 
            '#4': 7, 
            '5': 8, 
            '#5': 9, 
            '6': 10, 
            '#6': 11, 
            '7': 12
        }

        self.name_convert_table={
            '0':'0',
            '1':'1',
            '2':'#1',
            '3':'2',
            '4':'#2',
            '5':'3',
            '6':'4',
            '7':'#4',
            '8':'5',
            '9':'#5',
            '10':'6',
            '11':'#6',
            '12':'7',
            '13':'[1]',
            '14':'[#1]',
            '15':'[2]',
            '16':'[#2]',
            '17':'[3]',
            '18':'[4]',
            '19':'[#4]',
            '20':'[5]',
            '21':'[#5]',
            '22':'[6]',
            '23':'[#6]',
            '24':'[7]',
            '25':'[[1]]',
        }
        self.upper_pattern=r'\[#?\d+\]'
        self.max_pattern=r'\[\[#?\d+\]\]'
        self.downer_pattern=r'\(#?\d+\)'
    def sourceParser(self,sheet:str) -> List[List[str]]:
        res=[]
        try:
            t=sheet.strip().split(' ')
        except:
            print("Wrong Input:"+sheet)
            exit(0)
        k=[]    
        for s in t:
            dot=0
            if s=='N':
                res.append(k.copy())
                k.clear()   
                continue         
            elif m:=re.match(self.upper_pattern,s):
                dot+=10
                s=m.group()[1:-1]
            elif m:=re.match(self.max_pattern,s):
                dot+=15
                s=m.group()[1:-1]
            elif m:=re.match(self.downer_pattern,s):
                dot-=10
                s=m.group()[1:-1]
            k.append((s if s!='0' else '',dot))
        if k:
            res.append(k.copy())
        return res

    def sheetParser(self,sheet:str,of:int=0) -> List[List[str]]:
        res=[]
        try:
            t=sheet.strip().split(' ')
        except:
            print("Wrong Input:"+sheet)
            exit(0)
        k=[]
        for s in t:
            offset=of
            if s=='N':
                res.append(k.copy())
                k.clear()   
                continue         
            elif m:=re.match(self.upper_pattern,s):
                offset+=12
                s=m.group()[1:-1]
            elif m:=re.match(self.max_pattern,s):
                offset+=24
                s=m.group()[2:-2]
            elif m:=re.match(self.downer_pattern,s):
                offset-=12
                s=m.group()[1:-1]
            num=self.sheet_convert_table.get(s,0)
            k.append(str(num+(offset if num else 0)))
        if k:
            res.append(k.copy())
        return res

    def arrayParser(self,arr:List[List[str]]) -> str:
        if not arr:return ''
        res="\n"
        for k in arr:
            res+=' '.join(self.name_convert_table.get(i,'??') for i in k)+'\n'
        return res

#just for test
if __name__=='__main__':
    test_sheet1='5 #6 [#2] [#2] [#2] [#2] [2] [1] #6 [1] N 2 2 1 (#6) 5 4 5 1 2 #2 #2 #2 #2'
    p=SheetParser()
    t=p.sheetParser(test_sheet1,2)
    print(t)
    print(p.sourceParser(test_sheet1))
    print(p.arrayParser(t))