from hashlib import new
import os
import shutil

os.mkdir('styles')
file = open("./index.html", "w")
file.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n\t<meta charset="'UTF-8'">\n\t<meta http-equiv='X-UA-Compatible' content='IE=edge'>\n\t<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n\t<script src='./js/ejercicio1.js'></script>\n\t<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n</body>\n</html>")
file = open("./index.js", "w")
file = open("./style.css", "w")
file.close()
shutil.move('./style.css', "./styles")

dir ="project"


if os.path.exists(dir):     
        dir+="x"
        newdir= "./"+dir+"_"
        os.mkdir(newdir)    
        shutil.move('./index.html', newdir)
        shutil.move('./index.js', newdir)
        shutil.move('./styles', newdir)
        dir=newdir
        
        

else:
    os.mkdir(dir)
    shutil.move('./styles', dir)
    shutil.move('./index.js', dir)
    shutil.move('./index.html', dir)

