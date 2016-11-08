{
  'targets': [
    {
      'target_name': 'lib1',
      'type': 'static_library',
      'msvs_guid': '74AC0D8B-49E1-48C3-9727-E499D0B6A838',
      'includes': [
        '../settings.gypi',
        '../configs.gypi',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'lib1.h',
        'lib1.cpp',
      ],
    },
  ],
}
