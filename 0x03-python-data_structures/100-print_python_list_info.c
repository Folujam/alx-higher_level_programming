#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 *print_python_list_info -  prints some basic info about Python lists
 *@p: pointer to the objest in the list
 *Return: void
*/
void print_python_list_info(PyObject *p)
{
    PyObject *it;
    Py_ssize_t len, i;
    const char *item_type;
    PyListObject *castedp;

    if (PyList_Check(p))
    {
        castedp = (PyListObject *)p;
        len = PyList_Size(p);
        printf("[*] Size of the Python List = %d\n", (int) len);
        printf("[*] Allocated = %d\n", (int)castedp->allocated);
        if (len != 0)
        {
            for (i = 0; i < len; i++)
            {
                it = PyList_GetItem(p, i);
                item_type = Py_TYPE(it)->tp_name;
                printf("Element %d: %s\n", (int) i, item_type);
            }
        }
    }
}