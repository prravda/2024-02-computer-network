# Use Ubuntu as base image
FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y tcpdump curl

# Copy the script into the container
COPY capture-script.sh /usr/local/bin/capture-script.sh

# Make the script executable
RUN chmod +x /usr/local/bin/capture-script.sh

# Run the script when the container starts
ENTRYPOINT ["/usr/local/bin/capture-script.sh"]