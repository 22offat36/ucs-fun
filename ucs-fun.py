from ucsmsdk.ucshandle import UcsHandle
# Create a connection handle
handle = UcsHandle("10.87.118.160", "admin", "Cisco123")
# Login to the server
handle.login()
print 'Logged in Capitan!'


from ucsmsdk.mometa.ls.LsServer import LsServer

# checking to see if the python created SP exists - delete it if so


sp = LsServer(parent_mo_or_dn="org-root", name="sp1_demo")
handle.add_mo(sp)
print sp


print 'Created sp1_demo service profile'

sp = handle.query_dn("org-root/ls-sp_demo")
print sp
spall = handle.query_dn("org-root")
print spall

sp2 = handle.query_dn("org-root/ls-lab-65-bfs2")
sp2.descr = "pythoned"
handle.set_mo(sp2)
handle.commit()
print 'changing description'
sp2 = handle.query_dn("org-root/ls-lab-65-bfs2")
print sp2
print 'Added pythoned to service profile description'
handle.logout()
print 'Im out scotty'
