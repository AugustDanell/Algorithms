#include <stdio.h>

/* is_sorted
*  Uses pointer arithmetics to discern if an array is sorted. We are dereferencing
*  value after value, comparing it to the previous one until the whol array is 
*  exhausted.
*/

int is_sorted(int* arr, int n){
    int prev = *arr;                // Dereferencing the value.
    for(int i = 1; i < n; i++){
        int current = *(arr + i);   // Dereferencing value after value.
        if(prev > current){
            return 0;
        }
        
        prev = current;
        
    }
    
    return 1;
}

/* bubble_sort
*  A very simple sorting algorithm that pushes the biggest value it can find to
*  the rightmost element.
*/

void bubble_sort(int* arr, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n-i-1; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

/* Insertion_sort
*  Insertiong sort switches two elements all the time, so that we have a sorted
*  array on the left hand side. If a smaller element comes along in the unsorted
*  array the insertion sort switches each left side element iteratively, thus pushing
*  that smaller element into the sorted array, where it belongs.
*/

void insertion_sort(int* arr, int n){
    for(int i = 1; i < n; i++){
        int comparing_element = arr[i];
        int j = i - 1;
        while(j >= 0 && comparing_element < arr[j]){
            arr[j+1] = arr[j];
            j--;
        }
        
        arr[j+1] = comparing_element;
    }
    
}

/* Selection_short
*  A sorting algorithm that iterates through an array and finds the smallest value
*  putting it at the front, then iterates on with the rest of the array similarily.
*/

void selection_sort(int* arr, int n){
    for (int i = 0; i < n; i++){
        int min_index = i;
        for (int j = i+1; j < n; j++){
            if(arr[j] < arr[min_index]){
                min_index = j;
            }
        }
        
        int temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }
    
}


/* split_array
*  A helper function that takes in two empty arrays (sarr1, sarr2) and an array
*  arr. The function also takes in n, which is the size of n and split_point which
*  is where the user wants to split arr into two splitted arrays, (sarr1 and sarr2)
*/

void split_array(int*arr, int*sarr, int* sarr2, int n, int split_point){
    int s1 = 0;
    int s2 = 0;
    
    for(int i = 0; i < n; i++){
        if(i > split_point){
            sarr2[s2] = arr[i];
        }
        else{
            sarr[s1] = arr[i];
        }
    }
}

/* merge_sort
*  A normal merge sort using the split_array above as a helper. 
*  1. We start with just plitting up the array until we reach 'ground floor', 
*  that is where each split consists of just one element. 
*  2. We start assembling the splits again, merging them as it were. Each time
*  we merge we know that both sub-arrays are already sorted from previous merging
*  and so we can directly compare between the two arrays.
*  3. If one sub-array is exhausted we have to take the rest of the elements from
*  the other array which is very simple because it is sorted so we only need to
*  take its elements in order.
*/

void merge_sort(int* arr, int n){
    int split_point = 0;
    int is_odd = 1;
    if(n > 1){
        // 1. Split it up:
        double split = n/2;
        split_point = (int)(split);
        
        if(n%2 == 0){
            is_odd = 0;
        }
    
        int first_size = split_point + is_odd;
        int second_size = split_point;
    
        int sarr[first_size];
        int sarr2[second_size];
        int s1 = 0;
        int s2 = 0;
        
        for (int i = 0; i < first_size; i++){
            sarr[i] = arr[i];
        }
        
        for (int i = 0; i < second_size; i++){
            sarr2[i] = arr[i+first_size];
        }
        
        merge_sort(sarr, first_size);
        merge_sort(sarr2, second_size);
        
        int l = 0;
        int r = 0;
        int k = 0;
        
        // 2. Combining it back up, make use of the fact that they are already sorted:
        
        while(l < first_size && r < second_size){
            if(sarr[l] < sarr2[r]){
                arr[k] = sarr[l];
                l++;
            }
            else{
                arr[k] = sarr2[r];
                r++;
            }
            
            k++;
        }
        
        // 3. Left overs we add in, the sub-arrays are already sorted, so this works:
        while(l != first_size){
            arr[k] = sarr[l];
            k++;
            l++;
        }
        
        while(r != second_size){
            arr[k] = sarr2[r];
            k++;
            r++;
        }
        
        
    }
    
    
}

void quick_sort(int* arr, int size){
    
}

int main()
{   
    
    int size = 5;
    // User specified size:
    // printf("Hello, how big of an array do you want?\n");
    // int size = 0;
    // scanf("%d", &size);
    
    
    
    int arr[] = {5, 2, 1, 3, 4};
    bubble_sort(arr, size);
    if(is_sorted(arr, size)){
        printf("Bubble sort ok!\n");
    }
    
    int arr2[] = {5, 2, 1, 3, 4};
    selection_sort(arr2, size);
    if(is_sorted(arr2, size)){
        printf("Selection sort ok!\n");
    }
    
    int arr3[] = {5, 2, 1, 3, 4};
    insertion_sort(arr3, size);
    if(is_sorted(arr3, size)){
        printf("Insertion sort ok!\n");
    }
    
    size = 5;
    int arr4[] = {5, 2, 1, 3, 4};
    merge_sort(arr4, size);
    if(is_sorted(arr4, size)){
        printf("Merge sort ok!\n");
    }
    
    size = 5;
    int arr5[] = {5, 2, 1, 3, 4};
    quick_sort(arr5, size);
    if(is_sorted(arr5, size)){
        printf("quick sort ok!\n");
    }
    else{
        printf("Quick sort todo!\n");
    }
    
    int* p = arr;
    
    return 0;
}
