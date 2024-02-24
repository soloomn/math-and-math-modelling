In the first approach, we implement the concept of multi-core processing to speed up Python computations. In the second approach, the part of the program dealing with calculations is translated into C and integrated into the Python code.
To integrate C into Python, we used compilation of the C source code into a .dll library and plugging it into Python. To generate such a library from a C file yourself, run this command in your terminal:
~#: gcc -shared -o ht.dll ht.c
Attention: perform this only in the directory with the "ht.c" file downloaded from the Main branch
