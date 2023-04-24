void selectionSort(List<int> arr) {
  int size = arr.length;
  for (int i = 0; i < size; i++) {
    int min_index = i;
    for (int j = i; j < size - 1; j++) {
      if (arr[min_index] > arr[j]) {
        min_index = j;
      }
    }
    var temp = arr[min_index];
    arr[min_index] = arr[i];
    arr[i] = temp;
  }
}

void main() {
  List<int> arr = [8, 2, 3, 5];
  selectionSort(arr);
  print(arr);
}
