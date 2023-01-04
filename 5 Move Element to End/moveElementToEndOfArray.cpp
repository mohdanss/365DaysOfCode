#include <iostream>
#include <vector>

using namespace std;

vector<int> moveElementToEnd(vector<int> array, int toMove) {
	int left = 0, right = array.size() - 1;
	while(left < right)
	{
		if(array[left] != toMove) left++;
		else if(array[right] == toMove) right--;
		else
		{
			int temp = array[left];
			array[left] = array[right];
			array[right] == temp;
			left++;
			right--;
		}
				
	}
	return array;
}

int main(){
	vector<int> newArray = moveElementToEnd({2, 1, 2, 2, 2, 3, 4, 2}, 2);
	for(auto element: newArray)
		cout << element << " ";
	cout << endl;

}
