ip link show enp6s0                                               // to check if the port state is DOWN or UP
sudo ip link set enp6s0 up                                        // to set the state UP

sudo ip addr add 192.168.1.10/24 dev enp6s0   
sudo ip addr add 10.0.58.121/24 dev enp6s0     
sudo ip route add default via 10.0.58.1 dev enp6s0
sudo systemctl disable --now systemd-resolved
sudo rm /etc/resolv.conf
echo -e "nameserver 8.8.8.8\nnameserver 1.1.1.1" | sudo tee /etc/resolv.conf

if internet is working, no need to do this:
sudo dhclient enp6s0

ping 192.168.1.11
ping 8.8.8.8
ping google.com

if DNS does not work, go to http://iitgn.ac.in and login into the WiFi