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
        if 'url:' in mylist[row][0]:
            url = mylist[row][0].split(' url:')[1]
            mylist[row][0] = mylist[row][0].split('url:')[0]
            mylist[row][1] = mylist[row][1] + ' ' + '<div><img src="{}"><br></div>'.format(url)
        try:
            note,tag = mylist[row][0].split(' #')
        except ValueError:
            print("Error on following notes:")
            print(mylist[row][0])
        mylist[row][0] = note
        mylist[row].append(tag)
    else:
        missing.append(mylist[row])

if missing:
    print("Missing tags on these notes")
    for row in missing:
        print(row[-2])

with open('anki-flashcards.csv','w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(mylist)
