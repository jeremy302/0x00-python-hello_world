
#ifndef PY_LONG_LONG
#define PY_LONG_LONG int64_t
#if defined(LLONG_MAX)
#define PY_LLONG_MIN LLONG_MIN
#define PY_LLONG_MAX LLONG_MAX
#define PY_ULLONG_MAX ULLONG_MAX
#elif defined(__LONG_LONG_MAX__)
#define PY_LLONG_MAX __LONG_LONG_MAX__
#define PY_LLONG_MIN (-PY_LLONG_MAX - 1)
#define PY_ULLONG_MAX (PY_LLONG_MAX * Py_ULL(2) + 1)
#elif defined(SIZEOF_LONG_LONG)

#define PY_LLONG_MAX (												\
		(1 + 2 * ((Py_LL(1) << (CHAR_BIT * SIZEOF_LONG_LONG - 2)) - 1)))
#define PY_LLONG_MIN (-PY_LLONG_MAX - 1)
#define PY_ULLONG_MAX (PY_LLONG_MAX * Py_ULL(2) + 1)
#endif /* LLONG_MAX */

#endif /* HAVE_LONG_LONG */

#include <pyconfig.h>
#undef HAVE_LONG_LONG

#include <Python.h>
#include <stdio.h>
#include <wchar.h>
#include <inttypes.h>
#include <locale.h>

/**
 * print_python_string - prints some info about a python string object
 * @p: a python float object
 *
 * Return: void
 */
void print_python_string(PyObject * p)
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

	setlocale(LC_ALL, "C.UTF-8");
	for (i = 0; i < len; ++i)
	{
		char *format = "%lc";

		code_point = PyUnicode_READ(kind, data, i);
		printf(format, (wint_t)code_point);
	}
	printf("\n");
}
