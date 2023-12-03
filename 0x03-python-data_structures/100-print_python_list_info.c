#include <Python.h>

/**
 * print_python_list_info - prints an info about python lis
 * @p: Pyobject its a python object to be examined
 *
*/
void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a list");
		return;
	}

	PyListObject *list = (PyListObject *)p;
	Py_ssize_t listSize = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", listSize);
	printf("[*] Allocated = %zd\n", list->allocated);

	for (Py_ssize_t i = 0; i < listSize; ++i)
	{
		PyObject *element = list->ob_item[i];

		printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
	}

}
