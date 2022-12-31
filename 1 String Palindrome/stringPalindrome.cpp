#include <iostream>

using namespace std;

// Time Complexity O(n)
// Space Complexity O(1)
bool isPalindrome(string str){
	if(str.length() == 1)
		return true;
	
	int left = 0;
	int right = str.length() - 1;
	
	while(true){
		if(left >= right || right < left)
			break;
		if(str[left++] != str[right--])
			return false;
	}
	return true;
}

int main(){
	cout << isPalindrome("Ans") << endl;
	cout << isPalindrome("a") << endl;
	cout << isPalindrome("abba") << endl;
 	cout << isPalindrome("aba") << endl;	
	cout << isPalindrome("acba") << endl;
}
