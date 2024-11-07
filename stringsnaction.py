
def main():
    #Book Titles Database
    book_titles = []
    
    #Counter to main sure it gets to 10 books
    count = 0
    
    #Collect 10 book titles
    while count < 10:
        #Ask for a book title
        title = input("Enter the title of a book: ")
        
        #Capitalize the title and add to the list
        book_titles.append(title.title())
        
        #Once there is a book entered it adds 1 to the count 
        count += 1
    
    #Created a sorted from the list previously entered by the user
    sorted_titles = sorted(book_titles)
    
    #Prints the sorted list
    print("\nSorted list of book titles:")
    for title in sorted_titles:
        print(title)

main()