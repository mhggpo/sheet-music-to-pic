#sheet music to array

from typing import *
import re
sheet_convert_table={
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
    '7': 12, 
}

name_convert_table={
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


upper_pattern=r'\[#?\d+\]'
downer_pattern=r'\(#?\d+\)'

def sheetParser(sheet:str,of:int=0) -> List[str]:
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
        elif m:=re.match(upper_pattern,s):
            offset+=12
            s=m.group()[1:-1]
        elif m:=re.match(downer_pattern,s):
            offset-=12
            s=m.group()[1:-1]
        k.append(str(sheet_convert_table.get(s,0)+offset))
    if k:
        res.append(k.copy())
    return res

def arrayParser(arr:List[List[str]]) -> str:
    if not arr:return ''
    res="\n"
    for k in arr:
        res+=' '.join(name_convert_table.get(i,'??') for i in k)+'\n'
    return res

if __name__=='__main__':
    test_sheet1='5 #6 [#2] [#2] [#2] [#2] [2] [1] #6 [1] N 2 2 1 (#6) 5 4 5 1 2 #2 #2 #2 #2'
    t=sheetParser(test_sheet1,2)
    print(t)
    print(arrayParser(t))