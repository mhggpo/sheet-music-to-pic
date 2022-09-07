#array to pic
import os
from PIL import ImageFont, Image, ImageDraw
from random import choices,sample
from typing import List
from sheetparser import SheetParser


class SheetConverter:
    def __init__(self) -> None:
        self.COL = 30
        self.UNIT_HEIGHT_SIZE = 143
        self.UNIT_WIDTH_SIZE = 27
        self.TITLE_HEIGHT_SIZE = 40
        self.SHEET_HEIGHT_SIZE = 40
        self.PATH = "./res/images/"
    def add_first_line(self,main='C',title='None',more=''):
        main='1='+main
        font = ImageFont.truetype('./res/fonts/SourceHanSansHWSC-VF.ttf',25)
        target = Image.new('RGB',(self.UNIT_WIDTH_SIZE * self.COL,self.TITLE_HEIGHT_SIZE))
        draw = ImageDraw.Draw(target)
        draw.text((60,0),'|',(255,255,255),font)
        draw.text((435,0),'|',(255,255,255),font)
        draw.text((30-font.getsize(main)[0]//2,0),main,(255,255,255),font)
        draw.text((60+(375-font.getsize(title)[0])//2,0),title,(255,255,255),font)
        draw.text((435+(375-font.getsize(more)[0])//2,0),more,(255,255,255),font)
        draw = ImageDraw.Draw(target)
        #target.save('target.png')
        return target

    def gen_single_image(self,note: tuple,idx: str):
        target = Image.new('RGB',(self.UNIT_WIDTH_SIZE,self.UNIT_HEIGHT_SIZE+self.SHEET_HEIGHT_SIZE),(255,255,255))
        sheet = Image.new('RGB',(self.UNIT_WIDTH_SIZE-2,self.SHEET_HEIGHT_SIZE-2),(255,255,255))
        background = Image.new('RGB',(self.UNIT_WIDTH_SIZE,self.SHEET_HEIGHT_SIZE),(0,0,0))
        background.paste(sheet,(1,1))
        sheet=background
        try:
            iml = Image.open(self.PATH+idx+'.gif')
        except:
            print('Invaild Image:'+idx)
            exit(0)
        font = ImageFont.truetype('./res/fonts/SourceHanSansHWSC-VF.ttf',24)
        draw = ImageDraw.Draw(sheet)
        source,dot=note
        #print(font.getsize(source))
        nx=(self.UNIT_WIDTH_SIZE-font.getsize(source)[0]+6)/2
        ny=(self.SHEET_HEIGHT_SIZE-font.getsize(source)[1]+6)/2
        #print(nx,ny)
        draw.text((nx,ny),source,(0,0,0))
        if dot:
            draw.text((nx,ny-dot),'.',(0,0,0))
        draw = ImageDraw.Draw(sheet)    
        #sheet.save('sheet.png')
        target.paste(sheet, (0, 0))
        target.paste(iml, (0, self.SHEET_HEIGHT_SIZE))
        #target.save('target.png')
        return target

    def gen_image_with_sheet(self,source:List[tuple],arr:List[str]):
        image_files = []
        try:
            if not arr:
                for i in range(self.COL):
                    image_files.append(self.gen_single_image(('',0),'0'))
            else:
                n=len(arr)
                for i in range(n):
                    image_files.append(self.gen_single_image(source[i],arr[i]))
                for j in range(n,self.COL):
                    image_files.append(self.gen_single_image(('',0),'0'))
        except:
            print('Invaild Arrays')
            exit(0)
        return image_files

    def concat_images(self,source:List[List[tuple]],arr:List[List[str]],main='C',title='None',more=''):
        image_files = []
        ROW=len(arr)
        for i in range(ROW):
            image_files+=self.gen_image_with_sheet(source[i],arr[i])
        first_line_image = self.add_first_line(main,title,more)
        target = Image.new('RGB',(self.UNIT_WIDTH_SIZE * self.COL, (self.UNIT_HEIGHT_SIZE+self.SHEET_HEIGHT_SIZE) * ROW+self.TITLE_HEIGHT_SIZE))
        sheet = Image.new('RGB',(self.UNIT_WIDTH_SIZE * self.COL, (self.UNIT_HEIGHT_SIZE+self.SHEET_HEIGHT_SIZE) * ROW))
        for row in range(ROW):
            for col in range(self.COL):
                sheet.paste(image_files[self.COL*row+col], (0 + self.UNIT_WIDTH_SIZE*col, 0 + (self.UNIT_HEIGHT_SIZE+self.SHEET_HEIGHT_SIZE)*row))
        target.paste(first_line_image,(0,0))
        target.paste(sheet,(0,self.TITLE_HEIGHT_SIZE))
        target.save('target.png')
        return target
    
#just for test
if __name__=='__main__':
    p=SheetParser()
    test_sheet='0 (5) 0 (5) 0 (6) 0 (5) 0 1 0 (7) 0 0 (5) 0 (5) 0 (6) 0 (5) 0 2 0 1 N 0 (5) 0 (5) 0 5 0 3 0 1 0 (7) 0 (6) 0 0 4 0 4 0 3 0 1 0 2 0 1 N'
    sources=p.sourceParser(test_sheet)
    print(sources)
    arr=p.sheetParser(test_sheet,5)
    print(arr)
    c=SheetConverter()
    c.concat_images(sources,arr,'F','None','None')
