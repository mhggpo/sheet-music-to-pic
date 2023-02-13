from sheetparser import SheetParser
from converter import SheetConverter
import os

if __name__ == '__main__':
    if not os.path.exists('./target'):
        os.makedirs('./target')
    print('Please Input Sheet:')
    sheet = ""
    t = []
    while True:
        k = input()
        if k:
            print('More?', '')
            t.append(k)
        else:
            break
    offset = input('Please Input Offset:')
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            print('Invalid Offset')
            exit(0)
    else:
        offset = 0
    main = input('Please Input Main Tone:')
    name = input('Please Input Music Name:')
    more = input('Please Input More Information:')
    sep = input('Do you want to separate every not zero tone?(Y/N)')
    if sep:
        if sep == 'Y' or sep == 'y':
            for i in range(len(t)):
                j = t[i].split(' ')
                if len(j) <= 15:
                    t[i] = '0 ' + ' 0 '.join(j)
    for i in t:
        sheet += i + ' '
    del t
    del k
    c = SheetConverter()
    p = SheetParser()
    target = c.concat_images(p.source_parser(sheet), p.sheet_parser(sheet, offset), main, name, more)
    target.save('./target/' + (name if name else 'None') + '.png')
    print('Result Saved in /target/' + (name if name else 'None') + '.png')
