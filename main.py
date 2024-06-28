# from pygoogle_image import image as pi


# def main():
#     number_of_images = int(input("number of images per entry: "))
#     try:

#         with open("test.csv") as file_in:
#             lines = []
#             for line in file_in:
#                 pi.download(line,limit=number_of_images)
#                 print(f"-- {line} :: download completed ---")

#         print("Process Successfully Completed")
#     except:
#         print("An Error occured")

# main()

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"gtr r34","limit":2,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)