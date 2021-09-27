#include <Python.h>
#include <stdio.h>

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
	double v;
	char v_str[100] = {0};
	int v_i = 0;

	setbuf(stdout, NULL);
	if (p == NULL || strcmp(p->ob_type->tp_name, "float"))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	v_i = sprintf(v_str, "%.15f", v) - 1;
	v_str[17] = '\0';
	while (v_str[v_i] == '0' && v_str[v_i - 1] != '.')
		--v_i;
	v_str[v_i + 1] = '\0';

	printf("[.] float object info\n");
	printf("  value: %s\n", v_str);
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

