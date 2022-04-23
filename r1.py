
def read_file(filename):
    lines = []
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None #先把person預設成沒有值, 在python來說就是None, 其他程式是叫null    
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果Person有值, 我們才執行下面這行
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()