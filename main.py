from pygoogle_image import image as pi

with open("test.csv") as file_in:
    lines = []
    for line in file_in:
        pi.download(line,limit=3)
        print(f"-- {line} :: download completed ---")

print("Process Successfully Completed")
