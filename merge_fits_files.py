from astropy.table import Table, vstack, hstack
# vertical merge
t0 = Table.read('file1')
t1 = Table.read('file2')
new = vstack([t0, t1])
new.write('path')
# horizontal merge
# t0 = Table.read('file1')
# t1 = Table.read('file2')
# new = hstack([t0, t1])
# new.write('path')
