from zipfile import ZipFile
import os

def unzipfile(filename="zippedfile.zip"):
    with ZipFile(filename,'r') as zip:
        zip.printdir()
        print("Extracting all files")
        zip.extractall()
        print("Done!")

def get_path(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath= os.path.join(root,filename)
            file_paths.append(filepath)

    return file_paths

def main():
    directory = './100-Days-Python-Challenge'
    file_paths = get_path(directory)

    print('following files will be zipped')

    for file_name in file_paths:
        print(file_name)

    with ZipFile("my_file_zipped.zip","w") as zip:
        for file in file_paths:
            zip.write(file)
    
    print("file is zipped successfull !")

    unzipfile("zippedfile.zip")


if __name__ == "__main__":
    main()