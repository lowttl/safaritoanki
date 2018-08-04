import csv
with open('safari-annotations-export.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    mylist = []
    for row in spamreader:
        if row[-1] == '':
            continue
        mylist.append(row)

# Remove headline
mylist.pop(0)

"""
Original order
['Book Title',
 'Authors',
 'Chapter Title',
 'Date of Highlight',
 'Book URL',
 'Chapter URL',
 'Highlight URL',
 'Highlight',
 'Personal Note']
 """
neworder = [8,7,0,1,2,4,5,6,3]
missing = []

for row in range(len(mylist)):
    mylist[row] = [mylist[row][i] for i in neworder]
    if ' #' in mylist[row][0]:
        note,tag = mylist[row][0].split(' #')
        mylist[row][0] = note
        mylist[row].append(tag)
    else:
        print("Missing tags on these notes")
        missing.append(mylist[row])

for row in missing:
    print(row[-2])

with open('anki-flashcards.csv','w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(mylist)