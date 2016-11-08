#ifdef WIN32
#  define EXPORTAPI __declspec(dllexport)
#  define IMPORTAPI __declspec(dllimport)
#else
#  define EXPORTAPI __attribute__((visibility("default")))
#  define IMPORTAPI 
#endif


#ifdef LIB2API
#define LIB1EXPORT EXPORTAPI
#else
#define LIB1EXPORT IMPORTAPI
#endif

LIB1EXPORT int Print2(const char* str);


