# Copyright (c) 2011 The TQ Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'variables': {
	'project_name': 'app2',
  },
  'includes': [
    # Bring in the source file lists.
  ],
  'target_defaults': {
	'conditions': [
		['OS=="win"', {
			'msvs_guid': '435F7460-15D1-45E6-B59B-46717E025525',
			'includes': [
				'../msvs.gypi',
			],
			'library_dirs': [
				'<(PRODUCT_DIR)',
			],
			'link_settings': {
				'libraries': [
					'-llib2',
				],
			},
			'msvs_settings': {
				'VCLinkerTool': {
					'AdditionalLibraryDirectories': [
						#'<(PRODUCT_DIR)/obj/lib2',
					],
					'AdditionalDependencies': [
						#'lib2.lib',
					],
				},
			},
		}],
	],
  },
  'targets': [
	{
      'target_name': '<(project_name)',
      'type': 'executable',
      'dependencies': [
	    '../lib2/lib2.gypi:lib2'
      ],
      'defines': [
      ],
      'include_dirs': [
		'..',
      ],
      'sources': [
		'../lib2/lib2.h',
		'app2.cpp',
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
