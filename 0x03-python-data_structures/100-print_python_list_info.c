#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list object.
 *
 * @p: A pointer to a Python list object.
 *
 * Description:
 *   This function prints the size of the Python list, the allocated memory,
 *   and the type name of each element in the list.
 */

void print_python_list_info(PyObject *p)
{
	int elem;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elem = 0; elem < Py_SIZE(p); elem++)
		printf("Element %d: %s\n", elem, Py_TYPE(PyList_GetItem(p, elem))->tp_name);
}
