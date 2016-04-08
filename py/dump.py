#!/usr/bin/python
import shelve
kvs = shelve.open("shelve.db");
for k,v in kvs.items():
    print k, '=', v

kvs.close();
