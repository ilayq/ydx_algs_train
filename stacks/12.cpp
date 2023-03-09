#include <stack>
#include <iostream>

using namespace std;

int main(){
    string s;
    cin >> s;
    int b = 0;
    stack<char> st;
    for (char i : s){
        if (i == ']' || i == '}' || i == ')'){
            --b;
            if (b < 0){
                cout << "no" << endl;
                return 0;
            }
            if (i == ']'){
                if (st.top() == '['){
                    st.pop();
                }else{
                    st.push(i);
                }
            }
            if (i == '}'){
                if (st.top() == '{'){
                    st.pop();
                }else{
                    st.push(i);
                }
            }
            if (i == ')'){
                if (st.top() == '('){
                    st.pop();
                }else{
                    st.push(i);
                }
            }
        }else{
            b++;
            st.push(i);
        }
    }
    if (st.empty()){
        cout << "yes" << endl;
        return 0;
    }
    cout << "no" << endl;
    return 0;
}