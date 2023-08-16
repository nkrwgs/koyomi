import sys
sys.path.append(".")

import wareki 
import wareki.data

wareki.cli.execute()
print('1786-12-19', wareki.data.find_close_date('1786-12-19'))
print('1786-12-23', wareki.data.find_close_date('1786-12-23'))
