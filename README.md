# safaritoanki
Re-format Safaribooks CSV files to be ready for import in Anki

The different card types that you will need to have when importing are included in the file card_templates.apkg. 
Make sure you have them in your Anki profile before trying to import the CSV files.

Make also sure you are logged in to Safaribooks with your default web browser and run

    python safaritoanki.py

This should output a file named 'anki.csv' that you can import in Anki

When highlighting in Safaribooks you create the question as a note. 
You can also add a tag after the question i.e (important to have a space after the question and then the hash symbol.)

    What are the different LSA Types? #OSPF
    
Multiple tags are also supported.

    What are the different LSA Types? #OSPF IGP

This will add two tags, OSPF and IGP to the flashcard

If you want to include an image on the backside of the flashcard use the url: parameter

    What are the different LSA Types? #OSPF IGP url:https://www.safaribooksonline.com/library/view/ospf-a-network/9781484214107/images/9781484214114_Ch16Tab1.jpg

Cloze deletion is also supported, but they will be exported to a seperate csv file named "anki-cloze.csv" that you import in Anki as cloze.

    OSPF uses IP protocol number {{c1::89}} #OSPF IGP

