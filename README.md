## The Algorithms.
![front-image](https://image.ibb.co/eUJKdS/Algorithms_In_Computer_Science.jpg)
### Some information about the repository.
All algorithms are implemented on Python. For the execution of algorithms, the standard Python library version 3.6 is required. These algorithms are need for practice Python, a better understanding of algorithms and education the programming.
### What is Algorithms?
- Algorithm.  
In mathematics and computer science, an algorithm is an unambiguous specification of how to solve a class of problems. Algorithms can perform calculation, data processing and automated reasoning tasks.

##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Algorithm)

- Computer algorithm.  
In computer systems, an algorithm is basically an instance of logic written in software by software developers to be effective for the intended "target" computer(s) to produce output from given (perhaps null) input. An optimal algorithm, even running in old hardware, would produce faster results than a non-optimal (higher time complexity) algorithm for the same purpose, running in more efficient hardware; that is why algorithms, like computer hardware, are considered technology.  

##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Algorithm#Computer_algorithms)

### Sorting Algorithms.  
In computer science, a sorting algorithm is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) which require input data to be in sorted lists; it is also often useful for canonicalizing data and for producing human-readable output.  
##### Source: [Wikipeadia](https://en.wikipedia.org/wiki/Sorting_algorithm)  

#### Bubble Sort.  
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.  
##### Visualization of bubble sort.  
![Visualization of bubble sort](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif "Visualization of bubble sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)  

#### Insertion Sort.  
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 
##### Visualization of insertion sort.  
![Visualization of insertion sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif "Visualization of insertion sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)  

#### Gnome Sort.  
It is a sorting algorithm which is similar to insertion sort, except that moving an element to its proper place is accomplished by a series of swaps, as in bubble sort. It is conceptually simple, requiring no nested loops.
##### Visualization of gnome sort.  
![Visualization of gnome sort](https://upload.wikimedia.org/wikipedia/commons/3/37/Sorting_gnomesort_anim.gif "Visualization of gnome sort")    
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Gnome_sort)  

#### Cocktail Sort.  
Cocktail shaker sort,[1] also known as bidirectional bubble sort, cocktail sort, shaker sort (which can also refer to a variant of selection sort), ripple sort, shuffle sort, or shuttle sort, is a variation of bubble sort that is both a stable sorting algorithm and a comparison sort. 
##### Visualization of cocktail sort.  
![Visualization of cocktail sort](https://upload.wikimedia.org/wikipedia/commons/e/ef/Sorting_shaker_sort_anim.gif "Visualization of cocktail sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Cocktail_sort) 

#### Merge Sort.  
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 
##### Visualization of merge sort.  
![Visualization of merge sort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif "Visualization of merge sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)  

#### Selection Sort.  
In computer science, selection sort is a sorting algorithm, specifically an in-place comparison sort. It has O(n2) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.
##### Visualization of selection sort.  
![Visualization of selection sort](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif "Visualization of selection sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)  

#### Shell Sort.  
Shellsort, also known as Shell sort or Shell's method, is an in-place comparison sort. It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort).
##### Visualization of shell sort.  
![Visualization of shell sort](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif "Visualization of shell sort")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Shell_sort) 

### Searching Algorithms.  
In computer science, a search algorithm is any algorithm which solves the search problem, namely, to retrieve information stored within some data structure, or calculated in the search space of a problem domain. Examples of such structures include but are not limited to a linked list, an array data structure, or a search tree. The appropriate search algorithm often depends on the data structure being searched, and may also include prior knowledge about the data. Searching also encompasses algorithms that query the data structure, such as the SQL SELECT command. 
##### Source: [Wikipeadia](https://en.wikipedia.org/wiki/Search_algorithm)  

#### Linear Search.  
In computer science, linear search or sequential search is a method for finding a target value within a list. It sequentially checks each element of the list for the target value until a match is found or until all the elements have been searched.  
##### Visualization of linear search. 
![Visualization of linear search](https://www.tutorialspoint.com/data_structures_algorithms/images/linear_search.gif "Visualization of linear search")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Linear_search)  

#### Binary Search.  
In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array.
##### Visualization of binary search. 
![Visualization of binary search](https://image.ibb.co/jHDFsx/68747470733a2f2f626c6f672e70656e6a65652e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031352f31322f6f7074696d616c2d62696e6172792d7365617263682d747265652d66726f6d2d736f727465642d61727261792e676966.gif "Visualization of binary search")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Binary_search)  

#### Interpolation Search.  
Interpolation search is an algorithm for searching for a given key in an indexed array that has been ordered by numerical values assigned to the keys (key values). It parallels how humans search through a telephone book for a particular name, the key value by which the book's entries are ordered. In each search step it calculates where in the remaining search space the sought item might be, based on the key values at the bounds of the search space and the value of the sought key, usually via a linear interpolation. The key value actually found at this estimated position is then compared to the key value being sought. If it is not equal, then depending on the comparison, the remaining search space is reduced to the part before or after the estimated position. This method will only work if calculations on the size of differences between key values are sensible.
##### Visualization of interpolation search. 
![Visualization of interpolation search](https://image.ibb.co/b6OFsx/Interpolation_Searchfig_1.png "Visualization of interpolation search")  
![Visualization of interpolation search](https://image.ibb.co/efwDec/Interpolation_Searchfig_2.png "Visualization of interpolation search")  
##### Source: [Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)  

> Sincerely, Ilyas Salimov.   
> Email: ilyas.salimov.07@gmail.com