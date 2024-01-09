#include "Python.h"

/**
 * print_python_string - Print information about a Python string object.
 *
 * This function prints details about a Python string object,
 * length, and value. If the provided PyObject is not a valid string object,
 * an error message is printed.
 *
 * Parameters:
 * - p (PyObject*): A pointer to the Python string object to be analyzed.
 *
 * Returns:
 * - None: This function does not have a return value.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
