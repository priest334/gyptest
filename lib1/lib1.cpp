#include <stdlib.h>
#include <iostream>
#include "lib1/lib1.h"

int Print(const char* str) {
  std::cout << str << std::endl;
#ifdef WIN32
  system("pause");
#endif
  return 0;
}


