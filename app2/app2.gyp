{
  'targets': [
    {
      'target_name': 'app2',
      'type': 'executable',
      'msvs_guid': 'B7884C42-0B96-4B53-B20A-AEBCF53943C9',
      'includes': [
        '../settings.gypi',
        '../configs.gypi',
      ],
      'dependencies': [
        '../lib2/lib2.gyp:lib2',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        '../lib2/lib2.h',
        'app2.cpp',
      ],
    },
  ],
}
