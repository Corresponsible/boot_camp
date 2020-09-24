import json

def read_author():
    while True:
        author = input("\nEnter author's name: ")
        if author == 'x':
            break
        
        for k, v in enumerate(data):
            if author == v["Author_name"]:
                print(f"\nHere's info about {v['Author_name']}:\n\nRating: {v['Rating']}\nNote: {v['Note']}")
                break
            else:
                if k == len(data) - 1:
                    print("\nSorry, author not found, try again.")

def rates():
    while True:
        rating_query = input("\nTo see ratings type: 'l' for the lowest, 'h' for the highest, type 'avg' to see the average rating: ")
        if rating_query == "x":
            break

        if rating_query == "l":
            min_rating = min(item["Rating"] for item in data)
            min_authros = []
            for i in data:
                if min_rating == i["Rating"]:
                    min_authros.append(i["Author_name"])
            print(f"\nHere is the list of the lowest rated authors, with rating {min_rating}: {', '.join(min_authros)}")

        if rating_query == "h":
            max_rating = max(item["Rating"] for item in data)
            max_authros = []
            for i in data:
                if max_rating == i["Rating"]:
                    max_authros.append(i["Author_name"])
            print(f"\nHere is the list of the highest rated authors, with rating {max_rating}: {', '.join(max_authros)}")

        if rating_query == "avg":
            avg_rating = sum(item["Rating"] for item in data) / len(data)
            print (f"\nThe average rating among all authors is: {avg_rating}")
         
def add_author():
    while True:
        new_author = input("Enter author's name: ")
        while new_author:
            try:
                new_rating = int(input("Enter author's rating: "))
            except ValueError:
                print("Specify a number, please.")
                continue
            if new_rating < 1 or new_rating > 10:
                print("Rating should be between 1 and 10.")
                continue
            else:
                break
        new_note = input("Enter a note?\n")

        with open("lib.json","w") as lib_file:
            new = {
                "Author_name": "",
                "Rating": 0,
                "Note": ""
            }

            new['Author_name'] = new_author
            new['Rating'] = new_rating
            new['Note'] = new_note
            data.append(new)
            json.dump(data, lib_file, indent=4)
        
        print("\nAuthor added successfully!")
        break

while True:
    with open("lib.json","r") as lib_file:
        data = json.load(lib_file)

        print("""\n
        ###############         Welcome to the library's main menu.         ###############\n
        ###############     To exit, or go back to this menu - type 'x'     ###############\n
        * If you want to get information about an author, type: 'author';\n
        * To see info about ratings, type 'rates';\n
        * To add a new author, type 'new'.\n
        """)

        choice = input("")
        if choice == 'author':
            read_author()
        if choice == 'rates':
            rates()
        if choice == 'new':
            add_author()
        if choice == 'x':
            break