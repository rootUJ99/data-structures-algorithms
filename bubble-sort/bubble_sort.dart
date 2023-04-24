void bubbleSort(List<int> arr) {
  int size = arr.length;
  for (int i = 0; i < size; i++) {
    bool swapped = false;
    for (int j = 0; j < size - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
}

void main() {
  List<int> arr = [5, 6, 7, 8];
  bubbleSort(arr);
  print(arr);
}
