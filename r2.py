# function跟function的中間標準是: 空兩行
# encoding='utf-8-sig': 這是當你看到error是在第一行出現奇怪亂碼"\ufeff"時加上的

# 這是一個處理line對話紀錄的範例
# 這是一個用空格分開的對話紀錄
# 筆記重點: 清單的分隔, 開始值"有包含", 結束值"不包含"

def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:                               #注意! 容易忘記把else補上~ 
                for m in s[2:]:                 
                    allen_word_count += len(m) 
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:   
                    viki_word_count += len(m) 
    print('Allen打了', allen_word_count, '個字',',發了', allen_sticker_count, '個貼圖', ',傳了', allen_image_count, '張圖片')
    print('Viki打了', viki_word_count, '個字',',發了', viki_sticker_count, '個貼圖', ',傳了', viki_image_count, '張圖片')


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)


main()