#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

/**
 * print_python_bytes - prints some info about a python bytes object
 * @p: a python bytes object
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *bytes = NULL;
	Py_ssize_t len = 0;
	int i = 0, repr_len = 0;

	setbuf(stdout, NULL);
	if (p == NULL || strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = ((PyVarObject *)p)->ob_size;
	bytes = ((PyBytesObject *)p)->ob_sval;
	repr_len = len >= 10 ? 10 : len;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", (long)len);
	printf("  trying string: ");
	for (i = 0; i < len && bytes[i]; ++i)
		printf("%c", bytes[i]);
	printf("\n");
	printf("  first %d bytes:", repr_len + (repr_len < 10));
	for (i = 0; i < repr_len; ++i)
		printf(" %02hhx", bytes[i]);
	if (repr_len < 10)
		printf(" 00");
	printf("\n");
}

/**
 * print_python_float - prints some info about a python float object
 * @p: a python float object
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	PyObject *repr, *repr_str;
	char *repr_chrs;

	setbuf(stdout, NULL);
	if (p == NULL || strcmp(p->ob_type->tp_name, "float"))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	repr = ((PyObject *)p->ob_type->tp_repr(p));
	repr_str = PyUnicode_AsEncodedString(repr, "utf-8", "~E~");
	repr_chrs = ((PyBytesObject *)repr_str)->ob_sval;

	printf("[.] float object info\n");
	printf("  value: %s\n", repr_chrs);
	Py_XDECREF(repr);
	Py_XDECREF(repr_str);
}

/**
 * print_python_list - prints some info about a python list
 * @p: a python list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long i = 0, len, alloc_len;


	setbuf(stdout, NULL);
	if (p == NULL || strcmp(p->ob_type->tp_name, "list"))
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	len = ((PyVarObject *)p)->ob_size;
	alloc_len = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc_len);
	for (i = 0; i < len; ++i)
	{
		PyObject *item = ((PyListObject *)p)->ob_item[i];
		const char *tp = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, tp);
		if (!strcmp(tp, "bytes"))
			print_python_bytes(item);
		else if (!strcmp(tp, "float"))
			print_python_float(item);
	}
}

