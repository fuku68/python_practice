import sys

# 例外の再スロー
def re_rais():
    try:
        1 / 0
    except:
        print('Error: ', sys.exc_info()[0])
        raise

try:
    re_rais()
except:
    print('例外')

# sys.exc_info
# (例外クラス, 例外クラスのインスタンス, トレースバック)
