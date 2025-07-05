from ncclient import manager
import xml.dom.minidom

router_ip = "192.168.56.106" 


nuevo_hostname = "Gomez_Mendoza_Urrea"

hostname_config = f"""
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>{nuevo_hostname}</hostname>
  </native>
</config>
"""

loopback_config = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

with manager.connect(
    host=router_ip,
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
) as m:
    
    print(" Cambiando hostname...")
    response1 = m.edit_config(target="running", config=hostname_config)
    print(xml.dom.minidom.parseString(response1.xml).toprettyxml())

    
    print("Configurando Loopback 11...")
    response2 = m.edit_config(target="running", config=loopback_config)
    print(xml.dom.minidom.parseString(response2.xml).toprettyxml())
