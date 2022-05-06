from bs4 import BeautifulSoup
import os
import csv

os.chdir("D:\\GSIB\\MBA-Fintech\\glearn_old")
#print(os.getcwd())
#print(os.listdir())

##mytext = "D:\\GSIB\\MBA-Fintech\\hadoop.html"
with open('hadoopNew.html', 'r') as f:
    contents = f.read()
    
    soup = BeautifulSoup(contents, 'lxml')
    ps = soup.find_all('label')
    qns = []
    for i in ps:
        qns.append(i.get_text())

    for i in qns:
        print(i)
##        print(i.get_text())
##    for i in range(10):
##        print(str(qns[i]))
##    print(len(qns))
##    f = open('questions_new_options.csv', 'w')
##    for i in qns:
##        f.write(i)
##        f.write('\n')
        
