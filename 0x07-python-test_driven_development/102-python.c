#include <Python.h>
#include <stdio.h>
#include <wchar.h>

/**
 * print_python_string - prints some info about a python string object
 * @p: a python float object
 *
 * Return: void
 */
void print_python_string(PyObject *p)
{
	long int i = 0, len = 0, code_point = 0;
	unsigned int kind = 0, is_ascii = 0, is_compact = 0;
	void *data = NULL;
	char *type_repr = NULL;
	PyASCIIObject *obj = NULL;

	setbuf(stdout, NULL);
	if (p == NULL || !PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	obj = (PyASCIIObject *)p;
	len = PyUnicode_GET_LENGTH(p);
	kind = obj->state.kind;
	is_ascii = obj->state.ascii;
	is_compact = obj->state.compact;
	data = PyUnicode_DATA(p);
	type_repr = is_ascii ? (is_compact ? "compact ascii" : "ascii")
		: (is_compact ? "compact unicode object" : "unicode object");

	printf("[.] string object info\n");
	printf("type: %s\n", type_repr);

	printf("  length: %ld\n", len);
	printf("  value: ");
	for (i = 0; i < len; ++i)
	{
		code_point = PyUnicode_READ(kind, data, i);
		printf("%lc", (wint_t)code_point);
	}
	printf("\n");
}
