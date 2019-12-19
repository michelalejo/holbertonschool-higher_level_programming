#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	int count = 0;
	PyObject *new;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		new = PyList_GetItem(p, count);
		printf("Element %i: %s\n", count, Py_TYPE(new)->tp_name);
	}
}
