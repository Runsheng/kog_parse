# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Aim: for a given gene list (with spaces) contains kog number, get the kog class such as "[J]"
#just a simple loop work for two small tsv files
#Note: kog is really really old, the dataset I used is founded in 2003
#Runsheng, 2014/12/29

kog_f=open("data/kog")
kog=kog_f.readlines()
kog_dict={} # make a dict to store the small kog dataset
for line in kog:
    if line[0]=="[":
        kog_dict[line.split(" ")[1]]=line.split(" ")[0]
kog_f.close()

# <codecell>

print kog_dict.keys()[2] #check the dic str

# <codecell>

with open("data/genelist.txt") as aim: #"with open" is sometimes much more convenient than "open"
    print aim.readlines()[3]#check the str in gene list

aim_w=open("foo.txt","w") # foo is a popular name?
with open("data/genelist.txt") as aim:
    for line in aim.readlines():
        kog_title=line.split("\t")[0].replace("[","").replace("]","")
        if kog_title in kog_dict.keys():
            cc=kog_dict[kog_title]
            line_w=line.split("\t")[0]+"\t"+cc+"\n"
            aim_w.write(line_w)
        else: #for the space lines
            aim_w.write("\n")
aim_w.close()

