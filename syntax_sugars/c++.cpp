// Syntax Sugars for C++

#include <bits/stdc++.h>
// imports everything in STD

using namespace std;

struct MyStruct1 {
    int number;
    string text;
};

struct MyStruct2 {
    MyStruct2(int a) {
        cout << "Got parameter " << a << endl;
    }
};

struct MyStruct3 {
    int num;
    bool operator<(MyStruct3 &other) {
        return num < other.num;
    }
    bool operator==(MyStruct3 &other) {
        return num == other.num;
    }
};

class MyClass {
    // public: and private:
   public:
    MyClass(int a) {
        privateVar1 = a;
    }
    int publicVar;
    int publicVar2;
    int publicFunc() {
        return 0;
    }

   private:
    int privateVar1;
    int privateVar2;
    int privateFunc() {
        return 0;
    }

    // friends can access private variables
    friend ostream &operator<<(ostream &, MyClass &);
};
ostream &operator<<(ostream &stream, MyClass &obj) {
    stream << "(MyClass object with privateVar1=" << obj.privateVar1 << ")" << endl;
    return stream;
}

int main() {
    // reading
    ifstream fin("numbers.txt");
    int N;
    fin >> N;
    vector<int> nums(N);
    for (int i = 0; i < N; i++) fin >> nums[i];

    for (auto &num : nums) cout << num << endl;
    cout << endl;

    // lambda function
    vector<int> my_vec2 = {1, 2, 3};
    auto lambda_func = [](int a, int b) { return a < b; };
    sort(my_vec2.begin(), my_vec2.end(), lambda_func);
    for (auto &s : my_vec2) cout << s << endl;
    cout << endl;

    // lambda function with access to parent scope
    auto lambda_func_2 = [&]() {
        cout << N << endl;
    };
    lambda_func_2();
    cout << endl;

    // advanced initialization of structs
    MyStruct1 obj1 = {.number = 10, .text = "my string"};
    // quick initialization
    MyStruct2 obj2(420);
    cout << endl;

    // operator overloading
    MyStruct3 obj3_a = {.num = 6};
    MyStruct3 obj3_b = {.num = 9};
    bool a_is_less_than_b = obj3_a < obj3_b;
    // ternary operator
    cout << "obj3_a is "
         << (a_is_less_than_b ? "less than" : "more than or equal to")
         << " obj3_b" << endl;
    cout << endl;

    // arrow operator
    MyStruct3 *ptr = &obj3_b;
    cout << (*ptr).num << endl;
    cout << ptr->num << endl;
    cout << endl;

    // overloading streams
    MyClass obj4(420);
    cout << obj4 << endl;
    cout << endl;

    // int functions automatically return 0
    // return 0;
}