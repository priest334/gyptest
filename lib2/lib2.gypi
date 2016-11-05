# Copyright (c) 2011 The TQ Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'variables': {
  },
  'includes': [
    # Bring in the source file lists.
  ],
  'target_defaults': {
	'conditions': [
		['OS=="win"', {
			'defines': [
				'WIN32',
			],
			'msvs_guid': '415F7460-15D1-45E6-B59B-46717E025525',
			'includes': [
				'../msvs.gypi',
			],
		}],
		['OS=="linux"', {
			'cflags': [
				'-fPIC',
			],
		}],
	],
  },
  'targets': [
	{
      'target_name': 'lib2',
      'type': 'shared_library',
      'dependencies': [
      ],
      'defines': [
	    'LIB2API',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
	    'lib2.h',
		'lib2.cpp',
      ],
    },
  ],
}
