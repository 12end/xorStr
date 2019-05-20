## xorStr
**xorStr**是一款简陋而方便的工具，通过**xorStr**，我们可以在'^'不被禁用的前提下，轻松获取一个字符串的随机异或表示，以此来简单规避一些敏感字符的检测
例如获取 `_GET`：
```
xorStr.py _GET
"q" to quit,other to random:

}x.6
"?kb

```
在php中，'}x.6'^'"?kb'的结果如下：
```php
php > print('}x.6'^'"?kb');
_GET
```

todo:
- 加入指定表示数据类型的选项