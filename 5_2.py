# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


from itertools import groupby

def coding(text_in, text_out):
    with open(text_in) as data_1, \
            open(text_out, "a") as data_2:
        string = ''.join(data_1.readlines())
        [list(g) for k, g in groupby(string)]
        data_2.write(''.join(['{}{}'.format(sum(1 for _ in g), k) for k, g in groupby(string)]))


def decoding(text_out):
    with open(text_out, "r") as data:
        string = ''.join(data.readlines())
        decode = ''
        count = ''
        for char in string:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        print(decode)
       

text_in = "text_words.txt"
text_out = "text_code_words.txt"

coding(text_in, text_out)
decoding(text_out)