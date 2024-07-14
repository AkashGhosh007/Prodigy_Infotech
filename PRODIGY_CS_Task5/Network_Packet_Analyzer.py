from scapy.all import *
import logging

def packet_sniffer(packet):
    try:
        if packet.haslayer(ARP):
            # Handle ARP packets
            logging.info("ARP Packet: %s" % packet.summary())
        elif packet.haslayer(ICMP):
            # Handle ICMP packets
            logging.info("ICMP Packet: %s" % packet.summary())
        elif packet.haslayer(BOOTP):
            # Handle BOOTP packets
            logging.info("BOOTP Packet: %s" % packet.summary())
        else:
            # Unknown packet
            logging.info("Unknown Packet: %s" % packet.summary())
    except Exception as e:
        logging.exception("Error occurred while processing packet: %s" % str(e))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='packet_sniffer.log')

    # Adding a console handler to print logs to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logging.getLogger().addHandler(console_handler)

    logging.info("Packet Sniffer Started")

    # Sniff ARP packets
    sniff(filter="arp", prn=packet_sniffer, count=10)

    # Sniff ICMP packets
    sniff(filter="icmp", prn=packet_sniffer, count=10)

    # Sniff UDP packets on port 67 or 68 (BOOTP)
    sniff(filter="udp and (port 67 or port 68)", prn=packet_sniffer, count=10)
