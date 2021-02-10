import csv
import sys
import os

# line input modes
NONE = 0
KEYS = 1
DISPLAY = 2
COLORS = 3
KEYCOLORS = 4

def stest(rowelement, string):
    if rowelement.replace('"','') == string:
        return True
    else:
        return False
 
if len(sys.argv) < 2:
    print('Usage: profbuild [csv profile directory name (NEW)]')
    quit()
    
fname = sys.argv[1]
if '.csv' not in fname:
    print(fname+' is not a csv file name')
    quit()
    
mode = NONE
ln = 0
kl = 0
dl = 0
kcl = 0
keysd = {}
disd = {}
colsd = {}
kcsd  = {}
profName = '*Undefined*'

with open(fname, 'r',newline='') as cf:
    reader = csv.reader(cf)
    ln += 1
    for row in reader:
        if stest(row[1], 'KEYS'):
            mode = KEYS
            continue
        if stest(row[1], 'DISPLAY'):
            mode = DISPLAY
            continue
        if stest(row[1], 'COLORS'):
            mode = COLORS
            continue
        if stest(row[1], 'KEY COLORS'):
            mode = KEYCOLORS
            continue
        if  stest(row[0],'Name:'):
            profName = row[1].replace('"','')
            mode = NONE
            continue
        
        if mode==KEYS:
            if kl > 4:
                mode = NONE
                continue
            for i in range(3):
                index = (i + 3*kl +1)
                keysd[index] = row[i+1].replace('"','')
            kl += 1
            
        if mode==DISPLAY:
            if dl > 4:
                mode = NONE
                continue
            for i in range(3):
                index = (i + 3*dl +1)
                disd[index] = row[i+1].replace('"','')
            dl += 1
            
        if mode==COLORS:
            rstr = row[1].replace('"','')
            if(not (rstr.isspace() or rstr=='')):
                index = row[1].replace('"','')
                colsd[index] = row[2].replace('""','')
            
        if mode==KEYCOLORS:
            if kcl > 4:
                mode = NONE
                continue
            for i in range(3):
                index = (i + 3*kcl +1)
                kcsd[index] = row[i+1].replace('"','')
            kcl += 1
            
#print('I found keys:')
#print(keysd)
#print('I found Display words')
#print(disd)
#print('I found color defs:')
#print(colsd)
#print('I found Key Colors')
#print(kcsd)



##  prevent clobbering existing profiles when testing
#profName = profName+'-TEST'
#print('New Profile Filename: '+profName)

###  now generate a profile folder:
 

if os.path.isdir(profName):
    print('Desired Profile Name: '+profName+' exists already, Quitting')
    quit()
    
os.mkdir(profName)

# populate the keyXX.txt files
for k in keysd.keys():
    fname = 'key'+str(k)+'.txt'
    f = open(profName+'/'+fname,'w')
    content = keysd[k]
    content.replace('STRING','')
    print(content, file=f)
    f.close()
    
# config.txt
f = open(profName+'/'+'config.txt','w')
for k in disd.keys():
    tag = 'z'+str(k)
    content = disd[k]
    if content.strip() == '' and 'STRING' in keysd[k]:
        content = keysd[k].replace('STRING','').strip()
    else:
        content = disd[k]
    print(tag+' '+content,file=f)
for k in colsd.keys():
        content = colsd[k].replace('/','  ')
        tag = str(k)
        print(tag+' '+content,file=f)
for k in kcsd.keys():
    content = kcsd[k].replace('/','  ')
    if content.strip() != '':
        tag = 'SWCOLOR_'+str(k)
        print(tag+' '+content,file=f)
    
f.close() 




        
