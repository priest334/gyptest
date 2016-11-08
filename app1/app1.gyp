{
  'targets': [
    {
      'target_name': 'app1',
      'type': 'executable',
      'msvs_guid': 'DA4E52CE-D7AF-4EEC-9A4D-6A3DBE626DEB',
      'includes': [
        '../settings.gypi',
        '../configs.gypi',
      ],
      'dependencies': [
        '../lib1/lib1.gyp:lib1',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        '../lib1/lib1.h',
        'app1.cpp',
      ],
    },
  ],
}
