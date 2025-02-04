#include <iostream>
#include <vector>

using namespace std;

// Функция для генерации подмножеств
void generateSubsets(vector<int>& nums, vector<int>& currentSubset, int index) {
    // Добавляем текущее подмножество в результат
    cout << "{ ";
    for (int num : currentSubset) {
        cout << num << " ";
    }
    cout << "}" << endl;

    // Генерируем подмножества, начиная с текущего индекса
    for (int i = index; i < nums.size(); i++) {
        // Добавляем текущий элемент в текущее подмножество
        currentSubset.push_back(nums[i]);
        // Рекурсивно генерируем подмножества, начиная с следующего элемента
        generateSubsets(nums, currentSubset, i + 1);
        // Убираем последний добавленный элемент для возврата к предыдущему состоянию
        currentSubset.pop_back();
    }
}

int main() {
    vector<int> nums = {1, 2, 3};
    vector<int> currentSubset;

    cout << "Все подмножества:" << endl;
    generateSubsets(nums, currentSubset, 0);

    return 0;
}
