#include <iostream>
#include <vector>

using namespace std;

// Функция для генерации всех подмножеств с использованием битовых масок
void generateSubsets(vector<int>& nums) {
    int n = nums.size();
    int totalSubsets = 1 << n; // 2^n

    for (int mask = 0; mask < totalSubsets; mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            // Проверяем, включен ли i-ый элемент в текущее подмножество
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }

        // Выводим текущее подмножество
        cout << "{ ";
        for (int num : subset) {
            cout << num << " ";
        }
        cout << "}" << endl;
    }
}

int main() {
    vector<int> nums = {1, 2, 3};

    cout << "Все подмножества:" << endl;
    generateSubsets(nums);

    return 0;
}
