# 📡 PacketPulse – Network Traffic Analyzer

PacketPulse is a lightweight Python-based network packet sniffer designed for real-time packet capture, logging, and visualization. Using Scapy for packet sniffing and Matplotlib/Seaborn for visual analytics, this tool provides quick insights into the protocol distribution of captured traffic.

---

## 🔍 Features

- 🛜 Captures live IP packets from network traffic
- 🧾 Extracts source IP, destination IP, and protocol type
- 📁 Exports captured data to `network_traffic.csv` for offline analysis
- 📊 Visualizes protocol distribution with clear, interpretable graphs
- 🧪 Ideal for educational demos, traffic diagnostics, or network security labs

---

## 🧠 Technologies Used

- [Python 3.x](https://www.python.org/)
- [Scapy](https://scapy.net/) — for packet sniffing
- [Pandas](https://pandas.pydata.org/) — for data structuring
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) — for visualization

---

## 🚀 How It Works

1. Starts packet capture on your network interface.
2. Filters only IP-layer packets.
3. Logs source, destination, and protocol data.
4. Saves the data to a `.csv` file.
5. Generates a bar plot showing protocol frequency.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Dinesh-Reddy-CSE/PacketPulse.git
cd PacketPulse

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
