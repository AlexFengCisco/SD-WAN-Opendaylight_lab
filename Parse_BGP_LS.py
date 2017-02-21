import json
import copy
import requests
import base64


url = "http://10.75.195.243:8181/restconf/operational/bgp-rib:bgp-rib/rib/bgp-example/loc-rib/tables/bgp-linkstate:linkstate-address-family/bgp-linkstate:linkstate-subsequent-address-family/linkstate-routes"
credentials = base64.b64encode(b'admin:admin')
payload = "<neighbor xmlns=\"urn:opendaylight:params:xml:ns:yang:bgp:openconfig-extensions\">\n    <neighbor-address>172.16.1.85</neighbor-address>\n    <afi-safis>\n        <afi-safi>\n            <afi-safi-name>LINKSTATE</afi-safi-name>\n        </afi-safi>\n    </afi-safis>\n</neighbor>"
headers = {
    'content-type': "application/xml",
    'authorization': "Basic "+credentials,
    'cache-control': "no-cache",
    'postman-token': "b9fc303a-eab9-3a73-66e0-14e86e06f580"
    }


response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
Result=response.text



topology={}
node={}
node_list=[]
node_list=[]
link={}
links=[]
Node_dict={}
node_count=0

Resault_json=json.loads(Result)
#print type(Resault_json)    #type dict
Result_Link_state_Routes=Resault_json["bgp-linkstate:linkstate-routes"]["linkstate-route"]

#print type(Result_Link_state_Routes)   #type list
#x=100
#y=100

for i in Result_Link_state_Routes:

    if "prefix-descriptors" in i:
        print "PREFIX information"
        print "OSPF ID"+str(i["advertising-node-descriptors"]["ospf-node"]["ospf-router-id"])
        print "Prefix "+i["prefix-descriptors"]["ip-reachability-information"]
        print "---------------------------------------------------------"
    
    if "node-descriptors" in i:
        print "NODE information"
        print "OSPF ID"+str(i["node-descriptors"]["ospf-node"]["ospf-router-id"])
        print "IP address"+i["attributes"]["node-attributes"]["ipv4-router-id"]
        node_count=node_count+1
        Node_dict[i["attributes"]["node-attributes"]["ipv4-router-id"]]=str(node_count)
        node["id"]=node_count
        node["name"]=i["attributes"]["node-attributes"]["ipv4-router-id"]
        print node["id"]
        print node["name"]
        print node
        #node_list.append(node)
        copy_node=copy.deepcopy(node)
        node_list.append(copy_node)
        #node_list.insert(node_count-1, node)

        print node_list
        print "-----------------------------------------------------------"

for i in Result_Link_state_Routes:
    if "link-descriptors" in i:
        print "LINK information"
        print "Link from node "+i["attributes"]["link-attributes"]["local-ipv4-router-id"]+\
              " local ip address "+i["link-descriptors"]["ipv4-interface-address"]+\
              "  to Remote node "+i["attributes"]["link-attributes"]["remote-ipv4-router-id"]+\
              " remote ip address  "+i["link-descriptors"]["ipv4-neighbor-address"]
        print "Local Node id "+Node_dict[i["attributes"]["link-attributes"]["local-ipv4-router-id"]]+"  to  Remote node id "+\
              Node_dict[i["attributes"]["link-attributes"]["remote-ipv4-router-id"]]
            
        link["source"]=Node_dict[i["attributes"]["link-attributes"]["local-ipv4-router-id"]]
        link["target"]=Node_dict[i["attributes"]["link-attributes"]["remote-ipv4-router-id"]]
        copy_link=copy.deepcopy(link)
        links.append(copy_link)
        print "---------------------------------------------------------"    
              

print node_list
print links

topology["nodes"]=node_list
topology["links"]=links
print topology
