#include <stdlib.h>
#include <iostream>
#include "lib2/lib2.h"

int Print2(const char* str) {
  std::cout << str << std::endl;
#ifdef WIN32
  system("pause");
#endif
  return 0;
}


