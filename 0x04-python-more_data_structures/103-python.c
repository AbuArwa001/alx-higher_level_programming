#include <Python.h>
/**
 * print_python_list - prins info about python lists
 * @p: python object
 *
 *
*/
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		PyErr_Print();
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	printf("[*] Elements:\n");

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
/**
 * print_python_bytes - prints bytes info about python lists
 * @p: python object
 *
 *
*/
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		PyErr_Print();
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("size: %ld\n", size);

	printf("first 10 bytes:");

	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf(" %02hhx", ((char *)PyBytes_AsString(p))[i]);
	}

	printf("\n");
}
