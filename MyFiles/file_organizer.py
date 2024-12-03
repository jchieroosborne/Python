import os 

def create_directories():
    #The main directories and subfolders
    main = "MyFiles"
    sub = ["Docs", "Images", "Videos"]

    try:
        # Create the main directory
        os.mkdir(main)
        print(f"Directory '{main}' has been created.")

        # Create the subdirectories inside the main directory
        for subdir in sub:
            path = os.path.join(main, subdir)
            os.mkdir(path)
            print(f"The subfolders '{subdir}' has been created inside '{main}'.")
    except Exception:
        print(f"An error has occurred")

create_directories()