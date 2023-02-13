# sheet-music-to-pic

## usage

```shell
python3 ./main.py
```

You'll see prompt information, then input your sheet and more to command line, if no error, you'll get result in "./target/{name}.png".



## parameter explanation

### sheet

looks at like "JE" model of sheet, for example:

```shell
0 (5) 0 (5) 0 (6) 0 (5) 0 1 0 (7) 0 0 (5) 0 (5) 0 (6) 0 (5) 0 2 0 1 N 0 (5) 0 (5) 0 5 0 3 0 1 0 (7) 0 (6) 0 0 4 0 4 0 3 0 1 0 2 0 1 N
```

'()':Means Lower Tone, offset=-12

'[]':Means Higher Tone, offset=12

'#':Means Up Half Tone, offset depends on table in code

'0':Means Zero Tone, image will show space for it

'N':Means Next Line, in fact, the max length of a line is 30, IDK what will happen when you input sheet more than 30 in a line

when input, you'll see "More?", means you can input multi lines in one time, just press enter twice to skip this feature.

### tone

means your sheet's offset text of Main C Tone, for example, if "1=F", then tone="F"

default value="C"

### offset

means your sheet's offset of Main C Tone, for example, if "1=F", then offset=5

default value=0

### name

your music name

default value="None"

### more

something you want to show



## something more

Default images are about recorder, main tone is "C", you can change them and code for yourself.

Default font is **SourceHanSansHWSC-VF**