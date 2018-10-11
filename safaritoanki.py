import csv

data = []
cloze = []
missing = []
header = None


with open('safari-annotations-export.csv') as csvfile:
    linereader = csv.reader(csvfile,delimiter=',', quotechar='"')
    for i,row in enumerate(linereader):
        if not header:
            header = row
            continue
        row_data = {}

        for i, field in enumerate(header):
            row_data[field] = row[i].strip()

        # Create cover key/value
        cover_url = 'https://www.safaribooksonline.com/library/cover/'
        row_data['Cover'] = cover_url + row_data['Book URL'].split('/')[-2]

        # Create tags and add image url if it exists
        if ' #' in row_data['Personal Note']:
            if ' url:' in row_data['Personal Note']:
                row_data['Personal Note'], row_data['Image'] = row_data['Personal Note'].split(' url:')
                row_data['Personal Note'], row_data['Tags'] = row_data['Personal Note'].split(' #')
            else:
                row_data['Personal Note'], row_data['Tags'] = row_data['Personal Note'].split(' #')
        else:
            missing.append(row_data['Highlight URL'])

        if '{{c' in row_data['Personal Note']:
            cloze.append(row_data)
        else:
            data.append(row_data)

keys = ['Personal Note','Highlight','Book Title', 'Authors', 'Chapter Title',
        'Book URL', 'Chapter URL', 'Highlight URL', 'Date of Highlight', 
        'Cover', 'Image', 'Tags']

with open('anki.csv','w') as f:
    w = csv.DictWriter(f,keys)
    w.writerows(data)

with open('anki-cloze.csv','w') as f:
    w = csv.DictWriter(f,keys)
    w.writerows(cloze)

if missing:
    print("Missing tags on following notes: ")
    for note in missing:
        print("  " + note)