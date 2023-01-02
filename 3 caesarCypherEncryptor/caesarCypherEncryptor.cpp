#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

char encryptedLetter(char letter, int key){
	int newLetterASCII = letter + key;
	return newLetterASCII > 122 ? 96 + newLetterASCII % 122 : newLetterASCII;
}


string caesarCypherEncryptor(string str, int key)
{
	key = key % 26;
	vector<char> encryptedStr;
	
	for(int i = 0; i < str.length(); i++)
	{
		encryptedStr.push_back(encryptedLetter(str[i], key));
	}
	return string(encryptedStr.begin(), encryptedStr.end());
}
