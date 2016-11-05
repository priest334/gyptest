# Copyright (c) 2011 The TQ Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'targets': [
    {
	  'target_name': 'all',
	  'type': 'none',
	  'dependencies': [
		'app1/app1.gypi:*',
		'app2/app2.gypi:*',
	  ],
	  'includes': [
	  	'msvs.gypi',
	  ],
	},
	
  ],
}
