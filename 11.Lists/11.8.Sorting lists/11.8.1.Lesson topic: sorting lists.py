Тема урока: сортировка списков

1.Задача сортировки;
2.Сортировка пузырьком;
3.Сортировка выбором;
4.Сортировка простыми вставками.
Аннотация.  Задачи и способы (алгоритмы) сортировки списков.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Задача сортировки

Задача сортировки списка заключается в перестановке его элементов так, чтобы они были упорядочены по возрастанию или убыванию. 
Это одна из основных задач программирования. Мы сталкиваемся с ней очень часто: при записи фамилий учеников в классном журнале, 
при подведении итогов соревнований и т.д.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Алгоритмы сортировки

Алгоритм сортировки — это алгоритм упорядочивания элементов в списке. Алгоритмы сортировки оцениваются по скорости выполнения и эффективности использования памяти:
-  время — основной параметр, характеризующий быстродействие алгоритма;
-  память — ряд алгоритмов требует выделения дополнительной памяти под временное хранение данных.
Алгоритмы сортировки, не потребляющие дополнительной памяти, относят к сортировкам на месте.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Основные алгоритмы сортировки

Медленные:
1.Пузырьковая сортировка (Bubble sort);
2.Сортировка выбором (Selection sort);
3.Сортировка простыми вставками (Insertion sort).

Быстрые:
1.Сортировка Шелла (Shell sort);
2.Быстрая сортировка (Quick sort);
3.Сортировка слиянием (Merge sort);
4.Пирамидальная сортировка (Heap sort);
5.Сортировка TimSort (используется в Java и Python).

Большинство алгоритмов сортировки, в частности, указанные выше, основаны на сравнении двух элементов списка. 
Существуют однако алгоритмы не основанные на сравнениях. Такие алгоритмы как правило используют наперед заданные условия относительно элементов списка. 
Например, элементами списка являются натуральные или целые числа в некотором диапазоне, элементами являются строки и т.д.

К алгоритмам не основанным на сравнениях можно отнести следующие:
1.Сортировка подсчетом (Counting sort);
2.Блочная сортировка (Bucket sort);
3.Поразрядная сортировка (Radix sort).

В рамках курса мы рассмотрим несложные алгоритмы пузырьковой сортировки, сортировки выбором и сортировки простыми вставками.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Примечания

Примечание 1. Подробнее об алгоритмах сортировки можно почитать тут.
Примечание 2. Мы называем некоторые алгоритмы сортировки медленными, поскольку они тратят много времени на сортировку больших списков. 
Например, если список содержит порядка миллиона элементов, то такие алгоритмы тратят часы, а то и дни на выполнение сортировки, 
в то время как быстрые алгоритмы справляются с задачей за секунды.
Примечание 3. Наглядную работу алгоритмов сортировки на разных входных данных можно посмотреть тут.
