#TODO Open .txt file********************************************************************************************
with open("quotes.txt", mode='r' ) as data:
    #TODO: Read File*******************************
    #contents = file.read()# read the file

    #TODO: Read File: as a list where each line is an item in the list object*******************************
    data = data.readlines()

     #TODO: Read File:removing each string's trailing newline character (\n) *******************************
    quotes_list = [quote.strip() for quote in data.readlines()]
    print(quotes_list)