#include <iostream>
#include <vector>

using namespace std;

// Функция для слияния двух подмассивов
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1; // Размер первого подмассива
    int n2 = right - mid;    // Размер второго подмассива

    vector<int> L(n1); // Первый подмассив
    vector<int> R(n2); // Второй подмассив

    // Копируем данные во временные массивы L[] и R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Слияние временных массивов обратно в arr[left..right]
    int i = 0; // Индекс первого подмассива
    int j = 0; // Индекс второго подмассива
    int k = left; // Индекс слияния

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Копируем оставшиеся элементы L[], если есть
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Копируем оставшиеся элементы R[], если есть
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Основная функция сортировки слиянием
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        // Находим середину
        int mid = left + (right - left) / 2;

        // Рекурсивно сортируем первую и вторую половины
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Сливаем отсортированные половины
        merge(arr, left, mid, right);
    }
}

// Функция для вывода массива
void printArray(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    cout << "Исходный массив: ";
    printArray(arr);

    mergeSort(arr, 0, arr.size() - 1);

    cout << "Отсортированный массив: ";
    printArray(arr);

    return 0;
}
