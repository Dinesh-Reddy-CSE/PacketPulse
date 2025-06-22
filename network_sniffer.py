from scapy.all import sniff
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

packet_data = []
def process_packet(packet):
    if packet.haslayer("IP"):

        src = packet["IP"].src
        dst = packet["IP"].dst
        protocol = packet["IP"].proto
        packet_data.append({"Source": src, "Destination": dst, "Protocol": protocol})

print("Starting packet capture...")
sniff(prn=process_packet, count=50) 

df = pd.DataFrame(packet_data)

df.to_csv("network_traffic.csv", index=False)
print("Captured packet data saved to 'network_traffic.csv'.")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Protocol")
plt.title("Protocol Distribution in Captured Packets")
plt.xlabel("Protocol")
plt.ylabel("Count")
plt.show()

print(df.head())
