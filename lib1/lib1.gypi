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
			'msvs_guid': '425F7460-15D1-45E6-B59B-46717E025525',
			'includes': [
				'../msvs.gypi',
			],
		}],
	],
  },
  'targets': [
	{
      'target_name': 'lib1',
      'type': 'static_library',
	  'standalone_static_library': '1',
      'defines': [
	    'LIB1API',
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
