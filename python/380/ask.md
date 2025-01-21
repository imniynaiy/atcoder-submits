```
Python 3.11.7 (main, Sep 15 2024, 15:14:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1e19 / 1043
9587727708533078.0
>>> 1e19 // 1043
9587727708533078.0
>>> 1e19 // 1044
9578544061302680.0
>>> 1e19 / 1044
9578544061302682.0
```


wolfram 算出来是
9.578544061302681 × 10^15 即 9578544061302681

int 和 float 是在什么时候转换的呢

=============补充下背景

在刷 atcoder
https://atcoder.jp/contests/abc380/editorial/11362?lang=en

用 a//b ac 了，但是 math.floor(a/b)去实现就无法 ac
然而如果 a//b 精度有问题，那是否说明 a//b 的 ac 也只是巧合……