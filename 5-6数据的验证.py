#所有字符都是数字（阿拉伯）
print('123'.isdigit())
print('12.3'.isdigit())
print('-'*50)
#所有字符都是数字
print('123'.isnumeric())
print('一六二'.isnumeric())
print('ⅠⅡⅢ'.isnumeric())
print('壹佰贰拾叁'.isnumeric())
print('1142314.4234'.isnumeric())
print('0b1001'.isnumeric())
#所有字符都是字母(含中文字符)
print('-'*50)
print('hello你好'.isalpha())
print('hello壹佰贰一二三'.isalpha())
print('hello123'.isalpha())

#所有字符都是字母和数字(含中文字符)
print('-'*50)
print('hello你好'.isalnum())
print('hello壹佰贰一二三'.isalnum())
print('hello123'.isalnum())
print('hello123'.isalnum())

#判断字符大小写(空格、中文不影响结果)
print()
print('i am fine'.islower())
print('I am fine'.islower())
print('hello你好'.islower())
print('I AM FINE再见'.isupper())

#所有字符都只是首字母大写（中文类似于空格效果）
print()
print(' Hello哇'.istitle())
print('HEllo'.istitle())
print('你好Hello你好 How Are You'.istitle())

#判断是否是空白字符
print('-'*50)
print('\t'.isspace())
print('\n'.isspace())
print(' '.isspace())
print('你'.isspace())