{
  'conditions': [
    ['OS=="win"', {
      'defines': [
        'WIN32',
      ],
      'msvs_settings': {
        'VCCLCompilerTool': {
          'ExceptionHandling': '1',
        },
        'VCLinkerTool': {
          'GenerateDebugInformation': 'true',
          'LinkIncremental': '1',
          'LinkLibraryDependencies': 'true',
          'SubSystem': '1',
        },
      },
    }],# OS!="win"
    ['OS!="win"', {
      
    }],
  ],
}