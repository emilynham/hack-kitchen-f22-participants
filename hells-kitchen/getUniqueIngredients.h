#include <iostream>
#include <set>
using namespace std;

int getUniqueIngredients(string ingredients[], int size) {
    std::set<string> processed;
    string temp;
    
    for(int i = 0; i < size; i++)
    {
        temp = "";
        for (int j = 0; j < ingredients[i].size(); j++)
        {
            if (isalpha(ingredients[i].at(j)))
                temp += tolower(ingredients[i].at(j));
        }
        processed.insert(temp);
    }

    
    return processed.size();
}
