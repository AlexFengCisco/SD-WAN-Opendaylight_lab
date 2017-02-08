##  Opendaylight SD-WAN testing 

#### Install opendaylight karaf and install features
#### Build Virl network topology
#### BGP link state with Opendaylight controller
#### BGP monitor with opendaylight
#### BGP route inject with opendaylight
#### PCEP MPLS RSVP traffic engineering 
#### PCEP segment routing traffic engineering

### Opendaylight SD-WAN testing topology
![Alt][1]
[1]:/topology.png "Pic"

iosv-1 send traffic to iosv-2 via two path options, iosxrv9000-2 setup BGP address family BGP link state , 
redistribute OSPF linkstate to BGP and send to Opendaylight controller .

iosxrv9000-1 configed as BMP client , opendaylight in flat-1 network as BMP server to collect BGP data.

iosxrv9000-1 configed as PCC conected to opendaylight as PCE , opendaylight create LSP and push to PCC.

### BGP flowSpec is coming soon ;-)) 