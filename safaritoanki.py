import csv
with open('safari-annotations-export.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    standard = []
    cloze = []
    for row in spamreader:
        if row[-1] == '' or "Book Title" in row:
            continue
        elif '{{c' in row[-1]:
            cloze.append(row)
        else:
            standard.append(row)

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

for row in range(len(standard)):
    standard[row] = [standard[row][i] for i in neworder]
    if ' #' in standard[row][0]:
        if 'url:' in standard[row][0]:
            url = standard[row][0].split(' url:')[1]
            standard[row][0] = standard[row][0].split('url:')[0]
            standard[row][1] = standard[row][1] + ' ' + '<div><img src="{}"><br></div>'.format(url)
        try:
            note,tag = standard[row][0].split(' #')
        except ValueError:
            print("Error on following notes:")
            print(standard[row][0])
        standard[row][0] = note
        standard[row].append(tag)
    else:
        missing.append(standard[row])

for row in range(len(cloze)):
    cloze[row] = [cloze[row][i] for i in neworder]
    if ' #' in cloze[row][0]:
        if 'url:' in cloze[row][0]:
            url = cloze[row][0].split(' url:')[1]
            cloze[row][0] = cloze[row][0].split('url:')[0]
            cloze[row][1] = cloze[row][1] + ' ' + '<div><img src="{}"><br></div>'.format(url)
        try:
            note,tag = cloze[row][0].split(' #')
        except ValueError:
            print("Error on following notes:")
            print(cloze[row][0])
        cloze[row][0] = note
        cloze[row].append(tag)
    else:
        missing.append(cloze[row])

if missing:
    print("Missing tags on these notes")
    for row in missing:
        print(row[-2])

with open('anki-flashcards.csv','w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(standard)

with open('anki-flashcards-cloze.csv','w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    wr.writerows(cloze)
