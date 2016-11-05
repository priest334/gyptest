# Copyright (c) 2011 hgfyphl. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
	'configurations': {
		'Debug': {
			'defines': [
				'DEBUG',
			],
		},
		'Release': {
			'defines': [
				'RELEASE',
			],
		},
	},
	'conditions': [
		['OS=="win"', {
			'msvs_settings': {
				'VCCLCompilerTool': {
					'ExceptionHandling': '1',
				},
				'VCLinkerTool': {
					'SubSystem': '0',
					'LinkIncremental': '1',
				},
			},
		}],
	],
}