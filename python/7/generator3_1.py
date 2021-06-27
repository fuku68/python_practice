# リストから順にファイルパスを取り出して、読み込みは委譲
def read_files(*files):
    for file in files:
        yield from read_lines(file)

# ファイル読み込みを担うサブジェネレーター
def read_lines(path):
    with open(path, 'r', encoding='UTF-8') as file:
        # 行単位にテキストを取得
        for line in file:
            yield line.rstrip('¥n')

for line in read_files(
    'decorator1.py'
):
    print(line)
