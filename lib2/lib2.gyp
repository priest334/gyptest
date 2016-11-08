{
  'targets': [
    {
      'target_name': 'lib2',
      'type': 'shared_library',
      'msvs_guid': 'B99E5A6E-749A-4362-9571-7A3C934F824E',
      'msvs_requires_importlibrary': 'true',
      'includes': [
        '../settings.gypi',
        '../configs.gypi',
      ],
      'include_dirs': [
        '..',
      ],
      'defines': [
        'LIB2API',
      ],
      'sources': [
        'lib2.h',
        'lib2.cpp',
      ],
      'conditions': [
        ['OS!="win"', {
          'cflags': [
            '-fPIC',
          ],
        }],
      ],
    },
  ],
}
