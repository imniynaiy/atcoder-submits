## 配置

首先，你需要在[这个 blog](https://atcoder.jp/posts/518) 里面下载 Atcoder Library 的压缩包。可以发现里面有三堆东西，一个 python 程序，两种语言的 document，还有一个库文件夹。

把库文件夹直接拖到你的编译器库文件相同目录下。Mingw 的路径应该都是 `\lib\gcc\x86_64-w64-mingw32\8.1.0\include\c++`，如果不是也容易自己寻找一下。

需要使用时直接引用库 `#include <atcoder/all>`。

**约定**：存在宏定义 `ll` 表示 `long long`，`ull` 表示 `unsigned long long`，`uint` 表示 `unsigned int`。

## 内容

只介绍一部分比较有用的。

## `static_modint <mod>` 类型

该类型的声明形如 `static_modint <mod> x;`，其中 mod 是一个 \[1,2×109+1000\] 的整数。还有 `modint998244353` 和 `modint1000000007` 两个自带类型（前者表示 `static_modint <998244353>`，后者同理）。

ACL 为其重载了四则运算（除法需要保证有逆元）和判断符号，包括 `--`，`++`，`+=` 等运算符。

需要注意任何与 `static_modint <mod>` 类型的运算都会将常数强转为此类型导致取模过多造成效率下降。你可以使用 `static_modint <mod>::raw(int x)` 直接返回 x 而不经取模，**需要保证 0≤x<mod，否则行为未定义**。

你可以使用 `int x.val()` 读取一个 `static_modint <mod>` 类型变量 x 的值用于其他 `int` 操作（例如输入输出）。

你可以使用 `static_modint <mod> x.pow(ll n)` 得到 xn。

你可以使用 `static_modint <mod> x.inv()` 得到 x 的逆元。

## `dynamic_modint` 类型

该类型的声明形如 `dynamic_modint <mod> x;`，其中 mod 是一个 \[1,2×109+1000\] 的整数。也可以简写为 `modint x;`，它表示 `dynamic_modint <-1> x;`，**注意此时必须重新设置模数，否则行为未定义**。

使用 `void dynamic_modint <mod>::set_mod(int m)` 将某种类型的 mod 修改为 m，其中 m 是一个 \[1,2×109+1000\] 的整数。你还可以使用 `int dynamic_modint <mod>::mod()` 来获取该类型此时的模数~但我不知道有什么用~。

其他使用方式同 `static_modint`。注意该类型不能用于 ACL 内置的 NTT 等。

## (+,×) 卷积

计算 ci\=∑j\=0iajbi−j。返回一个大小为 |a|+|b|−1 的 `vector` 表示 c，第 i 项表示 ci。

包含两个函数：

```cpp
vector <T> convolution<mod>(vector <T> a, vector <T> b) vector <ll> convolution_ll(vector <ll> a, vector <ll> b)
```

其中 `T` 是 `int, uint, ll, ull` 其中之一或者 ACL 的 `static_modint` 类型。

前者基于 NTT 实现，所以你需要保证 mod 是一个满足存在 c 使得 2c|mod−1 且 |a|+|b|−1≤2c 的质数。如果不填入 `<mod>`，则默认模数 998244353。时间复杂度同 NTT，是 O(nlog⁡n+log⁡p)。

后者需要保证卷出来的结果都在 `long long` 范围内，且 |a|+|b|−1≤224。时间复杂度 O(nlog⁡n)。

## dsu

本质是一个结构体。你可以使用 `dsu d(int n)` 声明并初始化 fai\=i 一个大小为 n 名为 `d` 的并查集。**注意点的编号是从 0 开始的**。

-   `int d.merge(int a, int b)`：将 (a,b) 连接在一起，并返回连通块的代表元。
-   `bool d.same(int a, int b)`：返回 (a,b) 是否在同一连通块内。
-   `int d.leader(int a)`：返回 a 所在连通块的代表元。
-   `int d.size(int a)`：返回 a 所在连通块的大小。
-   `vector<vector<int>> d.groups()`：返回所有连通块包含的点的集合的集合。

## Fenwick Tree（树状数组）

本质是一个结构体。你可以使用 `fenwick_tree<T> fw(int n)` 声明并初始化为全 0 一个大小为 n 类型为 `T` 名为 `fw` 的树状数组。其中 `T` 是 `int, uint, ll, ull` 其中之一或者 ACL 的 `static_modint` 类型。**注意下标的编号是从 0 开始的。**

-   `void fw.add(int p, T x)`：单点 p 加上 x。
-   `T fw.sum(int l, int r)`：查询 \[l,r\] 的区间和。注意如果 `T` 是 `int, uint, ll, ull` 其中之一，如果答案超出范围，则会自然溢出（对 2bit 取模）。

## （带懒标记的）线段树

我愿称之为最吊。

考虑线段树的数学意义，其实就是半群单点修改和区间求积。所以我们要重载半群信息和乘法。**你需要确保自己的半群乘法具有结合律。**事实上，对于合理的半群信息维护，你总能将形式写成矩阵乘法，所以总是具有结合律。

你有两种方式 O(n) 建立一棵包含懒标记的线段树，同样**注意下标的编号是从 0 开始的**：

```cpp
lazy_segtree<S, op, e, F, mapping, composition, id> seg(int n); lazy_segtree<S, op, e, F, mapping, composition, id> seg(vector<S> v);
```

前半部分是相同的：

-   `S` 是一个结构体，包含了所有你的标记和答案所需要维护的半群信息。
-   `op` 是一个函数 `S op(S x, S y)`，表示将信息 x **左乘**信息 y 合并在一起得到的信息（即 x⋅y）。
-   `e` 是一个函数 `S e()`，表示信息的**左乘**单位元，也就是满足 e⋅x\=x 的 e。
-   `F` 是一个结构体，包含了你的标记信息。
-   `mapping` 是一个函数 `S mapping(F x, S y)`，表示将标记 x **左乘**信息 y 合并在一起得到的信息。
-   `composition` 是一个函数 `F composition(F x, F y)`，表示将标记 x **左乘**标记 y，也就是将标记 x 合并到 y 得到的标记（即 x∘y）。
-   `id` 是一个函数 `F id()`，表示标记的**左乘**单位元，也就是合并到其他标记上不会影响其他标记的标记。也就是满足 id∘x\=x 的 id。

后半部分，对于前者表示生成一棵维护 \[0,n−1\] 的线段树，目前每个元素为信息的单位元 e；对于后者表示生成一棵维护 \[0,siz(v)−1\] 的线段树，目前每个元素为 `v` 中的对应元素。

然后你可以使用以下函数：

-   `void seg.set(int p, S x)`：单点修改 p 上的信息为 x。
-   `S seg.get(int p)`：单点查询 p 上的信息。
-   `S seg.prod(int l, int r)`：区间查询**左闭右开**区间 \[l,r) 的区间半群信息。对于 l\=r 返回单位元。对于 l\>r 行为未定义。
-   `S seg.all_prod()`：查询 \[0,n) 的整个半群信息，时间复杂度 O(1)。
-   `void seg.apply(int p, F f)`：单点修改，将标记 f 合并到 p 上的信息。
-   `void seg.apply(int l, int r, F f)`：区间修改，将标记 f 合并到 \[l,r) 的所有信息。

还有一些线段树上二分操作。

你需要定义一个确定性的函数 `bool g(S x)`，需要满足其你所需的二分单调性。特别地，你需要使得 `g(e())` 的返回值为 `true`。

-   `int seg.max_right<g>(int l)` 函数：返回右侧第一个 r 使得 \[l,r) 的区间信息的 g 值是 `true` 且 \[l,r\] 的区间信息的 g 值是 `false`。特别地，如果所有值均为 `true` 则返回 n；如果所有值均为 `false` 则返回 l。
-   `int seg.min_left<g>(int r)` 函数：返回左侧第一个 l 使得 \[l−1,r) 的区间信息的 g 值是 `false` 且 \[l,r) 的区间信息的 g 值是 `true`。特别地，如果所有值均为 `true` 则返回 0；如果所有值均为 `false` 则返回 r。

以上操作无特殊说明时间复杂度均为 O(log⁡n)。当然还要乘上标记或信息合并的复杂度 O(T)。

对于不带懒标记的线段树，主体部分只实现 `S, op(), e()` 就足够了。

## 数学库（类欧、逆元、快速幂、CRT）

-   `ll pow_mod(ll x, ll n, int m)`：返回 xnmodm。
-   `ll inv_mod(ll x, ll m)`：返回 x 在模 m 意义下的逆元。
-   `ll floor_sum(ll n, ll m, ll a, ll b)`：使用类欧，返回 ∑i\=0n−1⌊ai+bm⌋，复杂度 O(log⁡(n+m+a+b))。**你需要保证 a,b<m**。
-   `pair<ll, ll> crt(vector<ll> r, vector<ll> m)`：使用 ExCRT，返回方程组 x≡ri(modmi) 的解。若无解，返回 (0,0)，否则返回 (y,z) 表示解为 x≡y(modz)，其中 z\=lcm⁡(mi)。若方程数量为 0 则返回 (0,1)。**你需要保证 lcm⁡(mi) 在 `long long` 范围内**。

-   [配置](https://www.cnblogs.com/lemonniforever/p/18487052#%E9%85%8D%E7%BD%AE)
-   [内容](https://www.cnblogs.com/lemonniforever/p/18487052#%E5%86%85%E5%AE%B9)
-       [static\_modint 类型](https://www.cnblogs.com/lemonniforever/p/18487052#static_modint-mod-%E7%B1%BB%E5%9E%8B)
-       [dynamic\_modint 类型](https://www.cnblogs.com/lemonniforever/p/18487052#dynamic_modint-%E7%B1%BB%E5%9E%8B)
-       [(+,×) 卷积](https://www.cnblogs.com/lemonniforever/p/18487052#-%E5%8D%B7%E7%A7%AF)
-       [dsu](https://www.cnblogs.com/lemonniforever/p/18487052#dsu)
-       [Fenwick Tree（树状数组）](https://www.cnblogs.com/lemonniforever/p/18487052#fenwick-tree%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84)
-       [（带懒标记的）线段树](https://www.cnblogs.com/lemonniforever/p/18487052#%E5%B8%A6%E6%87%92%E6%A0%87%E8%AE%B0%E7%9A%84%E7%BA%BF%E6%AE%B5%E6%A0%91)
-       [数学库（类欧、逆元、快速幂、CRT）](https://www.cnblogs.com/lemonniforever/p/18487052#%E6%95%B0%E5%AD%A6%E5%BA%93%E7%B1%BB%E6%AC%A7%E9%80%86%E5%85%83%E5%BF%AB%E9%80%9F%E5%B9%82crt)

\_\_EOF\_\_

[![](https://cdn.luogu.com.cn/upload/usericon/399150.png)](https://cdn.luogu.com.cn/upload/usericon/399150.png)

-   **本文作者：** [Shunpower with Z](https://www.cnblogs.com/lemonniforever)
-   **本文链接：** [https://www.cnblogs.com/lemonniforever/p/18487052](https://www.cnblogs.com/lemonniforever/p/18487052)
-   **关于博主：** 评论和私信会在第一时间回复。或者[直接私信](https://msg.cnblogs.com/msg/send/lemonniforever)我。
-   **版权声明：** 本博客所有文章除特别声明外，均采用 [BY-NC-SA](https://creativecommons.org/licenses/by-nc-nd/4.0/ "BY-NC-SA") 许可协议。转载请注明出处！
-   **声援博主：** 如果您觉得文章对您有帮助，可以点击文章右下角**【推荐】**一下。