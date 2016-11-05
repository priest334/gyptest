# Copyright (c) 2011 The TQ Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'variables': {
	'project_name': 'app1',
  },
  'includes': [
    # Bring in the source file lists.
  ],
  'target_defaults': {
	'conditions': [
		['OS=="win"', {
			'msvs_guid': '445F7460-15D1-45E6-B59B-46717E025525',
			'includes': [
				'../msvs.gypi',
			],
			'library_dirs': [
				'<(PRODUCT_DIR)',
			],
			'link_settings': {
				'libraries': [
					'-llib1',
				],
			},
		}],
	],
  },
  'targets': [
	{
      'target_name': '<(project_name)',
      'type': 'executable',
      'dependencies': [
	    '../lib1/lib1.gypi:lib1'
      ],
      'defines': [
      ],
      'include_dirs': [
		'..',
      ],
      'sources': [
		'../lib1/lib1.h',
		'app1.cpp',
      ],
	  'library_dirs': [
	  ],
	  'link_settings': {
		'libraries': [
		],
	  },
    },
  ],
}
