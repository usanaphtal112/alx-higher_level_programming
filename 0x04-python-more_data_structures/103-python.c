#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * Print information about a Python bytes object.
 *
 * This function prints the size, trying string, and the first 10 bytes
 * of a Python bytes object. If the input object is not a valid bytes
 * object, an error message is printed.
 *
 * @param p: A pointer to a Python bytes object.
 *           Must be a valid PyObject pointer.
 * @return: None
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *trying_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &trying_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * Print information about a Python list object.
 *
 * This function prints the size, allocated memory, and type information
 * for each element in a Python list. If an element is of type "bytes",
 * it calls the print_python_bytes function to print additional information.
 *
 * @param p: A pointer to a Python list object.
 *           Must be a valid PyObject pointer.
 * @return: None
 */
void print_python_list(PyObject *p)
{
        long int size = PyList_Size(p);
        int i;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", size);
        printf("[*] Allocated = %li\n", list->allocated);
        for (i = 0; i < size; i++)
        {
                type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[i]);
        }
}

