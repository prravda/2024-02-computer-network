#!/bin/bash

# Define the output pcap file
PCAP_FILE="/tmp/output.pcap"

# Define the destination URL
URL="http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html"

# Start capturing network packets on interface eth0
# Adjust the interface as necessary (use 'tcpdump -D' to list interfaces)
echo "Starting tcpdump to capture HTTP packets..."
tcpdump -i eth0 -w $PCAP_FILE tcp port 80 &

# Get the PID of tcpdump to stop it later
TCPDUMP_PID=$!

# Sleep for a couple of seconds to allow tcpdump to initialize
sleep 2

# Use curl to visit the URL
echo "Accessing the URL via curl..."
curl $URL

# Sleep for a couple more seconds to ensure tcpdump captures the packets
sleep 2

# Stop the tcpdump process
echo "Stopping tcpdump..."
kill $TCPDUMP_PID

# Analyze the .pcap file and look for HTTP packets
echo "Analyzing the captured packets..."
# with verbose output and ASCII dump
tcpdump -r $PCAP_FILE -A -vvv -X 'tcp port 80'

# Display a message indicating that the process is complete
echo "Packet capture and analysis complete!"