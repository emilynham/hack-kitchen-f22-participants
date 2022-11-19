#include "getUniqueIngredients.h"
#include <iostream>
using namespace std;

int main() {
    // add your own test cases here!
    string ingredients1[] = {"egg", "tomato", "cheese", "bread", "jam"};
    if(getUniqueIngredients(ingredients1, 5) == 5){
        cout << "Passed test case!" << endl;
    } else {
        cout << "Failed test case :(" << endl;
    }

    {string ingredients2[] = {"ch.ick.en wi.n.g.s", "onion@rings000", "chickenwings", "oNioNriNgs"};
    if (getUniqueIngredients(ingredients2, 4) == 2) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }}

        {string ingredients2[] = {"cheese", "cheEse", "CHEESE", "cheese0", "_cheese_", "c-h-e-e-s-e", "c0h0e0e0s0e", "c heese0"};
    if (getUniqueIngredients(ingredients2, 8) == 1) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }}

        {string ingredients3[] = {};
    if (getUniqueIngredients(ingredients3, 0) == 0) {
        cout << "Passed" << endl;
    } else {
        cout << "Failed" << endl;
    }}
}