import pymongo
import os
import time

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["music_app"]
collection = db["songs"]

def showData():
    foundData = collection.find({}, {"_id": 0, "Name": 1, "Author": 1, "Collection": 1, "Year": 1})
    for document in foundData:
        print(document)

def insertData():
    newName = input("Enter the name of a song: ")
    newAuthor = input("Enter the author of this song: ")
    newCollection = input("Enter the album this song is in: ")
    newYear = int(input("Enter the year when this song was released: "))
    newData = {"Name": newName, "Author": newAuthor, "Collection": newCollection, "Year": newYear}
    collection.insert_one(newData)

def updateData():
    name = input("Enter the name of a song you want to update: ")
    prop = input("Enter the property you want to change: ")
    if name == "Year":
        value = int(input("Enter a new value: "))
    else: value = input("Enter a new value: ")

    try:
        collection.find_one_and_update({"Name": name}, {"$set": {prop: value}})
    except:
        print("Name or property or value was wrong, try again!")

def deleteData():
    name = input("Enter the name of a song you want to deletedelete: ")

    try:
        collection.find_one_and_delete({"Name": name})
    except:
        print("Name was wrong, try again!")

def main():
    while 1:
        print("\nEnter the number of operation you have to do: ")
        print("1) Show Database\n2) Insert Data\n3) Update Data\n4) Delete Data\n5) Exit")
        ch = int(input("Choice: "))
        match ch:
            case 1:
                os.system("cls")
                showData()
            case 2:
                os.system("cls")
                insertData()
                os.system("cls")
            case 3: 
                os.system("cls")
                updateData()
                os.system("cls")
            case 4: 
                os.system("cls")
                deleteData()
                os.system("cls")
            case 5:
                os.system("cls")
                print("See you later")
                print(":)")
                time.sleep(1)
                os.system("cls")
                break
            case _:
                os.system("cls")
                print("Enter your choice more wisely")
    
    client.close()

main()