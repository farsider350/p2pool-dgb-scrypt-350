from distutils.core import setup, Extension

digibyte_subsidy_module = Extension('digibyte_subsidy', sources = ['digibyte_subsidy.cpp'])

setup (name = 'digibyte_subsidy',
       version = '0.1',
       description = 'Subsidy function for Digibyte',
       ext_modules = [digibyte_subsidy_module])
