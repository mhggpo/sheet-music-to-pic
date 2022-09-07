from sheetparser import SheetParser
from converter import SheetConverter

if __name__=='__main__':
    print('Please Input Sheet:')
    sheet=""
    t=[]
    while True:
        k=input()
        if k:
            print('More?','')
            t.append(k)
        else:
            sheet=' '.join(t)
            del t
            del k
            break
    offset=input('Please Input Offset:')
    if offset:
        try:
            offset=int(offset)
        except:
            print('Invaild Offset')
            exit(0)
    else:
        offset=0
    main=input('Please Input Main Tone:')
    name=input('Please Input Music Name:')
    more=input('Please Input More Information:')
    sep=input('Do you want to sepreate every not zero tone?(Y/N)')
    if sep:
        if sep=='Y' or sep=='y':sheet=' 0 '.join(sheet.split(' '))
    c=SheetConverter()
    p=SheetParser()
    target=c.concat_images(p.sourceParser(sheet),p.sheetParser(sheet,offset),main,name,more)
    target.save('target.png')
    print('Result Saved in target.png')