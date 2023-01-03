#include <iostream>
#include <vector>

using namespace std;
	
vector<int> smallestDifference(vector<int> arrayOne, vector<int> arrayTwo) 
{
	sort(arrayOne.begin(), arrayOne.end());
	sort(arrayTwo.begin(), arrayTwo.end());
	
	int num1 = 0, num2 = 0;
	int p1 = 0, p2 = 0;

	int prevDif = INT_MAX;
	
	while(true)
	{
		int AD = abs(arrayOne[p1] - arrayTwo[p2]);
		
		if(AD < prevDif)
		{
			prevDif = AD;
			num1 = arrayOne[p1];
			num2 = arrayTwo[p2];
		}
		
		if(AD == 0)
		{
			break;
		}

		if(arrayOne[p1] > arrayTwo[p2])
		{
			p2++;
		}
		else
		{
			p1++;
		}

		if(p1 == arrayOne.size() || p2 == arrayTwo.size())
		{
			break;
		}
	}
	return {num1, num2};
}
