import csv
import glob
import requests
import os.path
import time
import webbrowser

# Download highlights
for fl in glob.glob('/Users/rickard/Downloads/safari-annotations-export*'):
    os.remove(fl)
webbrowser.open('https://www.safaribooksonline.com/a/export/csv/')
time.sleep(3)

os.rename('/Users/rickard/Downloads/safari-annotations-export.csv','./safari-annotations-export.csv')


data = []
cloze = []
missing = []
header = None
paths = ('/Users/rickard/Library/Application Support/'
        'Anki2/Rickard/collection.media/','/Users/rickard/git/safaritoanki/media/')


with open('safari-annotations-export.csv') as csvfile:
    linereader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(linereader):
        if not header:
            header = row
            continue
        row_data = {}

        for i, field in enumerate(header):
            row_data[field] = row[i].strip()

        # Create cover key/value
        cover_url = 'https://www.safaribooksonline.com/library/cover/'
        full_url = cover_url + row_data['Book URL'].split('/')[-2]
        row_data['Cover'] = row_data['Book URL'].split('/')[-2] + '.jpg'
        for path in paths:
            filename = path + row_data['Cover']
            if not os.path.isfile(filename):
                r = requests.get(full_url, allow_redirects=True)
                with open(filename, 'wb') as f:
                    f.write(r.content)

        # Create tags and add image url if it exists
        if ' #' in row_data['Personal Note']:
            if ' url:' in row_data['Personal Note']:
                (row_data['Personal Note'], row_data['Image']) = \
                    row_data['Personal Note'].split(' url:')
                (row_data['Personal Note'], row_data['Tags']) = \
                    row_data['Personal Note'].split(' #')
            else:
                try:
                    (row_data['Personal Note'], row_data['Tags']) = row_data['Personal Note'].split(' #')
                except:
                   print(row_data['Personal Note'])
                   raise ValueError
        else:
            missing.append(row_data['Highlight URL'])


        if 'Image' in row_data.keys():
            # Download images
            full_url = row_data['Image']
            row_data['Image'] = row_data['Image'].split('/')[-1]
            for path in paths:
                filename = path + row_data['Book URL'].split('/')[-2] + row_data['Image']
                if not os.path.isfile(filename):
                    r = requests.get(full_url, allow_redirects=True)
                    with open(filename, 'wb') as f:
                        f.write(r.content)
            row_data['Image'] = row_data['Book URL'].split('/')[-2] + row_data['Image']


        if '{{c' in row_data['Personal Note']:
            cloze.append(row_data)
        else:
            data.append(row_data)

keys = ['Personal Note', 'Highlight', 'Book Title', 'Authors', 'Chapter Title',
        'Book URL', 'Chapter URL', 'Highlight URL', 'Date of Highlight',
        'Cover', 'Image', 'Tags']

with open('anki.csv', 'w') as f:
    w = csv.DictWriter(f, keys)
    w.writerows(data)

with open('anki-cloze.csv', 'w') as f:
    w = csv.DictWriter(f, keys)
    w.writerows(cloze)

if missing:
    print("Missing tags on following notes: ")
    for note in missing:
        print("  " + note)
