s = 'full_string'

if 'string' in s:
    print('Substring found')

index = s.find('string')
if index != -1:
    print(f'Substring found at index {index}')

    #assert "substring " in full_string,  "expected {}, got {}".format(full_string, substring)