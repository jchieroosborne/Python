def main ():
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')
    
    #I found that everytime I ran the function while line 5 was in the For Item section it would repeat I moved the line above the looping section to only print it once
    print("The Tuple has",len(programming_classes), "Items.")

    for item in programming_classes:
        print(item)
        
main()