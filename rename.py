import os
path = "/Handwritten Texts/finals/New folder_labels"
path = "/Handwritten Texts/finals/New folder_images"
files = os.listdir(path)
i = 491
for index, file in enumerate(files):
    ind = file.find('.')

    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index + i), file[ind:]])))
