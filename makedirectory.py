import os
import os.path

# Set the source directory to the current directory
sourceDir = "."

# Walk through the source directory
for dirpath, dirs, files in os.walk(sourceDir):
        # Only process files in the root of the source directory
        if dirpath == ".":
            # Iterate over each file
            for filenm in files:
                # Create a new folder name based on the file name (without extension)
                newFolder = os.path.splitext(filenm)[0]
                # Check if the folder already exists
                if (not os.path.exists(newFolder)):
                    # Print the new folder name and create it
                    print (newFolder)
                    os.mkdir(newFolder)
                # Create the new path for the file
                newName = os.path.join(newFolder, filenm)
                # Create the old path for the file
                oldName = os.path.join(".", filenm)
                # Check if the file already exists in the new folder
                if (not os.path.exists(newName)):
                    # Print the renaming action and move the file
                    print ("Renaming to" , newName)
                    os.rename(oldName, newName)