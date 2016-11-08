{
  'configurations': {
    'Debug': {
      'defines': [
        'DEBUG',
      ],
      'conditions': [
        ['OS!="win"', {
          'cflags': [
            '-g',
          ],
        }],
      ],
    },
    'Release': {
      'defines': [
        'RELEASE',
      ],
    },
  },
}
