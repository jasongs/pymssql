import sys
import _mssql
import unittest
import ConfigParser

_parser = ConfigParser.ConfigParser({
    'server': 'localhost',
    'username': 'sa',
    'password': '',
    'database': 'tempdb'
})
_parser.read('tests.cfg')

if sys.argv[1:] and _parser.has_section(sys.argv[1]):
    section = sys.argv[1]
else:
    section = 'DEFAULT'

server = _parser.get(section, 'server')
username = _parser.get(section, 'username')
password = _parser.get(section, 'password')
database = _parser.get(section, 'database')


class MSSQLTestCase(unittest.TestCase):
    def setUp(self):
        self.mssql = _mssql.connect(server, username, password)
        self.mssql.select_db(database)
    
    def tearDown(self):
        self.mssql.close()
