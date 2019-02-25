# lets_log_stuff.py
"""
This file is the file that will perform logging for my ELK server.
Parts of this file were taken from the discussion board to make things
easy and to alleviate my frustration.
"""

import logging
import logstash
import sys

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('3.90.3.206', 5959, version=1))

test_logger.error('python-logstash: test logstash error message')
test_logger.info('python-logstash: test logstash info message')
test_logger.warning('python-logstash: test logstash warning message')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 126,
    'test_list': [1, 2, 3],
}
test_logger.info('python-logstash: test extra fields', extra=extra)

for x in range(0, 100):
    if x % 3 == 0:
        test_logger.error('ricks-logstash: error message ' + str(x) + ' is multiple of 3')
    elif x % 7 == 0:
        test_logger.info('ricks-logstash: info message ' + str(x) + ' is a multiple of 7 ')
    elif x % 17 == 0:
        test_logger.warning('ricks-logstash: warning message ' + str(x) + ' is multiple of 17')

