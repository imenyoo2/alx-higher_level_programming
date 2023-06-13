#include <python3.4/Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints infos about python list
 * @p: python lisl
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	/*PyTypeObject *ob = Py_TYPE(p);*/
	/*struct PyMemberDef *membs = ob->tp_members;*/
	int i;

	printf("[*] Size of the Python List = %ld\n", PyObject_Length(p));
	printf("[*] Allocated = %ld\n", PyObject_Size(p));
	for (i = 0; i < PyObject_Length(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
