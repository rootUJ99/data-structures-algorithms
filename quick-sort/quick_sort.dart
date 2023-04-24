void swap(List<int> arr, int value1, int value2) {
  var temp = arr[value1];
  arr[value1] = arr[value2];
  arr[value2] = temp;
}

int partition(List<int> arr, int low, int high) {
  int right = high - 1;
  int left = low;
  int pviot = arr[high];

  while (left <= right) {
    if (arr[left] < pviot) {
      left += 1;
    }
    if (arr[right] > pviot) {
      right -= 1;
    }

    if (left < right) {
      swap(arr, left, right);
    }
  }

  swap(arr, left, high);
  return left;
}

void quickSort(List<int> arr, low, high) {
  if (low < high) {
    int p = partition(arr, low, high);
    quickSort(arr, p + 1, high);
    quickSort(arr, low, p - 1);
  }
}

void main() {
  List<int> arr = [4, 2, 7, 1, 9, 3];
  quickSort(arr, 0, arr.length - 1);
  print(arr);
}
