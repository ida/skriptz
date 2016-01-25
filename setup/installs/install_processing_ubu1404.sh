# Update pckg-manager-index:
#sudo apt-get update -y
# Update pckgs:
#sudo apt-get upgrade -y

# Uh, wasn't available, always neeeeeed:
# sudo apt-get install vim -y

# Install processing's requirements:
# - Java
sudo apt-get install default-jre -y
# - Java Developer Kit
sudo apt-get install default-jdk -y
# - XServer (X11)
#   - On server machine:
sudo apt-get install xorg openbox -y
#   - On client machine:
#sudo apt-get install xauth -y
#   - Set DISPLAY sys-var:
#DISPLAY=localhost:0.0
#export DISPLAY
# Download processing:
wget download.processing.org/processing-2.2.1-linux64.tgz
# Unpack processing:
tar -xvzf processing-2.2.1-linux64.tgz
# Move into folder:
cd processing-2.2.1
# Execute processing-script:
./processing
