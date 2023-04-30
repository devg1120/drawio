#from N2G import drawio_diagram
from N2G import create_yed_diagram

data = {"huawei": ['''
<hua_sw1>dis current-configuration interface
#
interface Vlanif140
 ip binding vpn-instance VRF_MGMT
 ip address 10.1.1.2 255.255.255.0
 vrrp vrid 200 virtual-ip 10.1.1.1
#
interface Eth-Trunk5.123
 vlan-type dot1q 123
 description hua_sw2 BGP  peering
 ip binding vpn-instance VRF_MGMT
 ip address 10.0.0.1 255.255.255.252
 ipv6 address FD00:1::1/126
#
interface Eth-Trunk5.200
 vlan-type dot1q 200
 description hua_sw3 OSPF  peering
 ip address 192.168.2.2 255.255.255.252

<hua_sw1>dis arp all
10.1.1.2        a008-6fc1-1101        I         Vlanif140       VRF_MGMT
10.1.1.1        a008-6fc1-1102   0    D         Vlanif140       VRF_MGMT
10.1.1.3        a008-6fc1-1103   10   D/200     Vlanif140       VRF_MGMT
10.1.1.9        a008-6fc1-1104   10   D/200     Vlanif140       VRF_MGMT
10.0.0.2        a008-6fc1-1105   10   D/200     Eth-Trunk5.123  VRF_MGMT
    ''',
    '''
<hua_sw2>dis current-configuration interface
#
interface Vlanif140
 ip binding vpn-instance VRF_MGMT
 ip address 10.1.1.3 255.255.255.0
 vrrp vrid 200 virtual-ip 10.1.1.1
#
interface Eth-Trunk5.123
 vlan-type dot1q 123
 description hua_sw1 BGP  peering
 ip binding vpn-instance VRF_MGMT
 ip address 10.0.0.2 255.255.255.252
 ipv6 address FD00:1::2/126
    ''',
    '''
<hua_sw3>dis current-configuration interface
#
interface Vlanif200
 ip binding vpn-instance VRF_CUST1
 ip address 192.168.1.1 255.255.255.0
#
interface Eth-Trunk5.200
 vlan-type dot1q 200
 description hua_sw1 OSPF  peering
 ip address 192.168.2.1 255.255.255.252

<hua_sw3>dis arp
192.168.1.1         a008-6fc1-1111       I      Vlanif200
192.168.1.10        a008-6fc1-1110   30  D/300  Vlanif200
    '''],
"cisco_nxos": ['''
switch_1# show run | sec interface
interface Vlan133
  description OOB
  vrf member MGMT_OOB
  ip address 10.133.137.2/24
  hsrp 133
    preempt
    ip 10.133.137.1
!
interface Vlan134
  description OOB-2
  vrf member MGMT_OOB
  ip address 10.134.137.2/24
  vrrpv3 1334 address-family ipv4
    address 10.134.137.1 primary
!
interface Vlan222
  description PTP OSPF Routing pat to  siwtch2
  ip address 10.222.137.1/30
!
interface Vlan223
  description PTP OSPF Routing pat to siwtch3
  ip address 10.223.137.1/30

switch_1# show ip arp vrf all
10.133.137.2    -  d094.7890.1111  Vlan133
10.133.137.1    -  d094.7890.1111  Vlan133
10.133.137.30   -  d094.7890.1234  Vlan133
10.133.137.91   -  d094.7890.4321  Vlan133
10.134.137.1    -  d094.7890.1111  Vlan134
10.134.137.2    -  d094.7890.1111  Vlan134
10.134.137.3   90  d094.7890.2222  Vlan134
10.134.137.31  91  d094.7890.beef  Vlan134
10.134.137.81  81  d094.7890.feeb  Vlan134
10.222.137.2   21  d094.7890.2222  Vlan222
'''
]}

drawing = create_yed_diagram()

drawer = cli_ip_data(drawing, add_arp=True, add_fhrp=True)
drawer.work(data)
drawer.drawing.dump_file(filename="ip_graph_dc_1.graphml", folder="./Output/")
