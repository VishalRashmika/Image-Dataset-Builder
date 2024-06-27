from pygoogle_image import image as pi


# pi.download("gtr r34",limit=5,directory='../images')

with open("test.csv") as file_in:
    lines = []
    for line in file_in:
        pi.download(line,limit=2)
        