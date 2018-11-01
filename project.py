import networkx as nx
import re
import matplotlib.pyplot as plt
import PyPDF2 
from networkx.algorithms import community
from collections import Counter
G=nx.DiGraph()
pdfFileObj = open('WebPage.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pages=pdfReader.numPages
a=[]
b=[]
c=[]
d=[]
def chapter(pa):
    text=""
    if pa==1:
        count=0
        pag=47
    elif pa==2:
        count=48
        pag=67
    elif pa==3:
        count=68
        pag=107
    elif pa==4:
        count=108
        pag=127
    elif pa==5:
        count=128
        pag=153
    elif pa==6:
        count=154
        pag=191
    elif pa==7:
        count=192
        pag=225
    elif pa==8:
        count=226
        pag=251
    elif pa==9:
        count=252
        pag=279
    elif pa==10:
        count=280
        pag=421
    elif pa==11:
        count=422
        pag=469
    elif pa==12:
        count=470
        pag=503
    elif pa==13:
        count=504
        pag=539
    elif pa==100:
        count=0
        pag=539
    while count<pag:
        pageObj = pdfReader.getPage(count)
        text += pageObj.extractText()
        somo=re.findall("(?:Proposition\d{1,3}|\[Prop\.\d{1,2}\.\d{1,3}|\[Post\.\d)",text)
        i=0
        while i<len(somo):
            if "Proposition" in somo[i]:
                e=somo[i].replace('Proposition','')
                m=str(pa)+"."+e
                a.append(m)
            elif "[Prop." in somo[i]:
                t=somo[i].replace('[Prop.','')
                p=t.replace(']','')
                b.append((p,m))
            elif "[Post." in somo[i]:
                y=somo[i].replace('[Post.','p')
                x=y.replace(']','')
                c.append((x,m))
            i+=1
        count+=1
    G.add_nodes_from(a)
    G.add_edges_from(b)
    G.add_edges_from(c)
    #k=list(set(a) - set(list(G.nodes)))
    nx.draw(G,with_labels = True, node_color = 'b')
    plt.show()
num=input("Enter chapter number:")
chapter(int(num))
in_degrees=list(G.in_degree(list(G.nodes)))
out_degrees=list(G.out_degree(list(G.nodes)))
print("in degrees of all the nodes:",in_degrees)
print('--------------------------------------------------------------------')
print("out degrees of all the nodes:",out_degrees)
print('--------------------------------------------------------------------')
print("communities:")
communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
next_level_communities = next(communities_generator)
coms=sorted(map(sorted, next_level_communities))
for i in coms:
    print(i)
print('--------------------------------------------------------------------')
def lin_eq(z):
    if G.in_degree(z)==0:
        d.append(z)
    else:
        for i in list(G.predecessors(z)):
            lin_eq(i)
#example for linear combination
lin_eq('1.33')
print("linear combinations for 1.33 is:",Counter(d))
pdfFileObj.close() 