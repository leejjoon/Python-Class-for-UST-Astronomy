import import_test

print import_test.A_value_in_module_namespace

import_test.test_modulenamespace()

import_test.A_value_in_module_namespace = 100

import_test.test_modulenamespace()

import import_test

import_test.test_modulenamespace() # 100

