#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <stdlib.h>


/**
 * print_python_list_info - prints some info about a python list
 * @p: a python list
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *item = NULL;
	long i = 0, len = PyList_Size(p),
		alloc_len = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc_len);
	for (i = 0; i < len; ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
