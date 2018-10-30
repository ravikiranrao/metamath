import networkx as nx
import re
import matplotlib.pyplot as plt
import PyPDF2 
G=nx.DiGraph()
pdfFileObj = open('WebPage.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pages=pdfReader.numPages
count=0
text=""
a=[]
b=[]
while count < pages-1:
    pageObj = pdfReader.getPage(count)
    text += pageObj.extractText()
    if count==47:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="1."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==67:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="2."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==107:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="3."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==127:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="4."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==153:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="5."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==191:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="6."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==225:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="7."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==251:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="8."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==279:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="9."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==421:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="10."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==469:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="11."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==503:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="12."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    elif count==537:
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}\])",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m="13."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            i+=1
        text=""
    count +=1
G.add_nodes_from(a)
G.add_edges_from(b)
#k=list(set(a) - set(list(G.nodes)))
nx.draw(G,with_labels = True, node_color = 'b')
plt.show()
pdfFileObj.close() 