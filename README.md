# safaritoanki
Re-format Safaribooks CSV files to be ready for import in Anki

Export highlights from Safaribooks (safari-annotations-export.csv) and run

    python safaritoanki.py


This should output a file named 'anki-flashcards.csv' that you can import in Anki

When highlighting in Safaribooks you create the question as a note. 
You can also add a tag after the question i.e

    What are the different LSA Types? #OSPF
    
Multiple tags are also supported

    What are the different LSA Types? #OSPF IGP

This will add two tags, OSPF and IGP to the flashcard

Here is an example of a note https://www.safaribooksonline.com/a/routing-tcpip-volume/17436430/
