from algorithms.SelectionSort import SelectionSort
from algorithms.BubbleSort import BubbleSort
from algorithms.InsertionSort import InsertionSort
from algorithms.MergeSort import MergeSort
from algorithms.QuickSort import QuickSort
from algorithms.HeapSort import HeapSort
from algorithms.CountingSort import CountingSort

class Algorithms():
    SELECTION = SelectionSort
    BUBBLE = BubbleSort
    INSERTION = InsertionSort
    MERGE = MergeSort
    QUICK = QuickSort
    HEAP = HeapSort
    COUNTING = CountingSort

    @staticmethod
    def get_algorithms():
        return { k.lower() : v for k, v in vars(Algorithms).items() if k.isupper() }

