print('abc123'.isalnum())           # 結果：True
print('abc++'.isalnum())            # 結果：False
print('abcde'.isalpha())            # 結果：True
print('abc123'.isalpha())           # 結果：False
print('abc'.isascii())              # 結果：True
print('あいう'.isascii())           # 結果：False
print('100'.isdecimal())            # 結果：True
print('0x64'.isdecimal())           # 結果：False
print('1234'.isdigit())             # 結果：True
print('1234.56'.isdigit())          # 結果：False
print('百万'.isnumeric())           # 結果：True
print('million'.isnumeric())        # 結果：False
print('abc_123'.isidentifier())     # 結果：True
print('abc-123'.isidentifier())     # 結果：False
print('wings'.islower())            # 結果：True
print('Wings'.islower())            # 結果：False
print('WINGS'.isupper())            # 結果：True
print('Wings'.isupper())            # 結果：False
print('Wings Project'.istitle())    # 結果：True
print('WINGS Project'.istitle())    # 結果：False
print('Hello World'.isprintable())  # 結果：True
print('Hello¥nWorld'.isprintable()) # 結果：False
print(' '.isspace())                # 結果：True
print('***'.isspace())              # 結果：False
