#include <iostream>
#include <string>
using namespace std;

string int128_to_string(__int128 num) {
    string result;
    bool is_negative = false;
    if (num < 0) {
        is_negative = true;
        num = -num;
    }
    do {
        result = char('0' + num % 10) + result;
        num /= 10;
    } while (num > 0);
    if (is_negative) result = "-" + result;
    return result;
}

int main()
{
    __int128_t a = 1e19;
    std::cout << int128_to_string(a / 1044);
}

