{
  'targets': [
    {
      'target_name': 'all',
      'type': 'none',
      'msvs_guid': 'D229C4A2-652B-4430-A4DD-F944702B5C7F',
      'includes': [
        'settings.gypi',
        'configs.gypi',
      ],
      'dependencies': [
        'app1/app1.gyp:app1',
        'app2/app2.gyp:app2',
      ],
    },
  ],
}

