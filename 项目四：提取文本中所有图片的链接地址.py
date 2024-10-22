import re

s='1. ![风景图1](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0)2. ![风景图2](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0)3. ![风景图3](https://images.unsplash.com/photo-1471192028937-1a0a5938c92f)4. ![风景图4](https://images.unsplash.com/photo-1474434531770-8f75be3e0f34)5. ![风景图5](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0)6. ![风景图6](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0)7. ![风景图7](https://images.unsplash.com/photo-1522199710521-4a80324a23d0)8. ![风景图8](https://images.unsplash.com/photo-1446775810304-47c4c0f86f05)9. ![风景图9](https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0)10. ![风景图10](https://images.unsplash.com/photo-1496283162101-c8e4da193ec5'
pattern=r'https://images.unsplash.com/photo-\d*-\w*' #模式字符串

lst=re.findall(pattern,s)
for item in lst:
    print(item)