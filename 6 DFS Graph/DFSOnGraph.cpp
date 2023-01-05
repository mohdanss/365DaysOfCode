#include <iostream>
#include <vector>

using namespace std;

class Node
{
	public:
		string name;
		vector<Node *> children;
		
		Node(string str) { name = str; }
		
		vector<string> depthFirstSearch(vector<string> * array)
		{	
			// search for the element in the trversed array
			vector<string>::iterator it = find(array->begin(), array->end(), this->name);
			
			// if element not found, traverse it's children.
			if(it == array->end())
			{	
				array->push_back(this->name);
				for(int i = 0; i < this->children.size(); i++)
				{
					this->children[i]->depthFirstSearch(array);
				}
			}
			return *array;
		}
		
		Node* addChild(string name)
		{
			Node* newChildNode = new Node(name);
			this->children.push_back(newChildNode);
			return this;
		}

};
