/*
 * File: 103-python.c
 * Auth: Naphtal USABYUWERA
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about a Python list object.
 * @p: A pointer to the PyObject representing the Python list object.
 *
 * This function prints information about a Python list object, including its
 * size, allocation, and the types of elements within the list. It checks
 * whether the provided object is a valid list object before proceeding with
 * the printing. Additionally, for elements of type 'bytes' and 'float', it
 * calls specific functions to print additional information.
 *
 * Parameters:
 *   - p: A pointer to the PyObject representing the Python list object.
 *
 * Return: None
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: A pointer to the PyObject representing the Python bytes object.
 *
 * This function prints information about a Python bytes object, including its
 * size, contents (up to the first 10 bytes), and a representation of the
 * object as a string. It checks whether the provided object is a valid bytes
 * object before proceeding with the printing.
 *
 * Parameters:
 *   - p: A pointer to the PyObject representing the Python bytes object.
 *
 * Return: None
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: A pointer to the PyObject representing the Python float object.
 *
 * This function prints information about a Python float object, including its
 * value. It checks whether the provided object is a valid float object before
 * proceeding with the printing.
 *
 * Parameters:
 *   - p: A pointer to the PyObject representing the Python float object.
 *
 * Return: None
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
