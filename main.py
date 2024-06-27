number_of_images = 2

try:
    from pygoogle_image import image as pi

    with open("test.csv") as file_in:
        lines = []
        for line in file_in:
            pi.download(line,limit=number_of_images)
            print(f"-- {line} :: download completed ---")

    print("Process Successfully Completed")
except:
    print("Error occured")