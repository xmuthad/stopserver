#coding=utf-8
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystone_client
from novaclient import client

def stopyou(gods):
    auth = v3.Password(auth_url='http://key.oceanstack.slancer.com:5000/v3',
                       username='admin',
                       password='admin',
                       project_name='admin',
                       user_domain_id='default',
                       project_domain_id='default')
    sess =session.Session(auth=auth)
    nova = client.Client('2.1',session=sess)
    servers = nova.servers.list(search_opts={'all_tenants':True})
    for server in servers:
        if server.id in gods:
           continue
        else:
           try:
               nova.servers.stop(server.id)
           except Exception:
               continue

with open("godlist.txt") as godlist:
   gods=godlist.read()
   stopyou(gods)
