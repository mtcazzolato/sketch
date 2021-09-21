### 
# Copyright (C) 2021  Mirela Teixeira Cazzolato <mirelac@usp.br>
# Copyright (C) 2021  Lucas Santiago Rodrigues <lucas_rodrigues@usp.br>
# 
# This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
###

import psycopg2

class Connect:

    def __init__(self, name_db, username, pwd):
        self.name_db  = name_db
        self.username = username
        self.pwd      = pwd
        self.connect  = None
        self.cursor   = None

    def open_connection(self):
        try:
            self.connect = psycopg2.connect("dbname={} user={} password={}".format(self.name_db, self.username, self.pwd))
        except NameError:
            return 'Error connecting to database!'

    def get_connection(self):
        return self.connect

    def commit(self):
        return self.connect.commit()

    def cursor(self):
        return self.connect.cursor()

    def begin(self):
        return self.connect.begin()

    def rollback(self):
        return self.connect.rollback()

    def cancel(self):
        return self.connect.cancel()

    def close_connection(self):
        self.connect.close()
