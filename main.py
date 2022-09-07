from sheetparser import SheetParser
from converter import SheetConverter

if __name__=='__main__':
    sheet=input('Please Input Sheet:')
    offset=int(input('Please Input Offset:'))
    main=input('Please Input Main Tone:')
    name=input('Please Input Music Name:')
    more=input('Please Input More Information:')
    c=SheetConverter()
    p=SheetParser()
    target=c.concat_images(p.sourceParser(sheet),p.sheetParser(sheet,offset),main,name,more)
    target.save('target.png')
    print('Result Saved in target.png')