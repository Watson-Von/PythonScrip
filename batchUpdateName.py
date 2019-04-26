import os

path = "D:\\pythonCode\\batchUpdateName"
files = os.listdir(path)
i = 0

for filename in files:
    # 将文件名和缀名分成俩部分
    portion = os.path.splitext(filename)

    if portion[1] == '.txt':
        i = i+1
        portion = os.path.splitext(filename)
        if (portion[1] == ".txt"):  # 如果后缀是.txt
            newname = '第' + str(i) + "集" + ".txt"  # 重新组合文件名和后缀名
            os.chdir(path)
            os.rename(filename, newname)
