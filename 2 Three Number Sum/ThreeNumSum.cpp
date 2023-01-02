#include <iostream>
#include <vector>

using namespace std;

// O(n^2)
vector<vector<int>> threeNumberSum(vector<int> array, int targetSum){
	// O(log(n))
	sort(array.begin(), array.end());
	int curr = 0;
	vector<vector<int>>triplets;
	
	// O(n)
	while(curr < array.size() - 2){
    		int left = curr + 1;
    		int right = array.size() - 1;
		// O(n)
		while(left != right){
			int sum = array[curr] + array[left] + array[right];
			if(sum > targetSum)
				right--;
			else if (sum < targetSum)
				left++;
			else
				triplets.push_back({array[curr], array[left++], array[right]});
		}
      		curr++;
	}
	return triplets;
}
