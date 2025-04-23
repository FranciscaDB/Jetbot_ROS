# Jetbot_ROS

Differential wheeled robot based on Jetson Orin Nano Dev kit.

## How to set the jetpack

## Install ROS 2 foxy

https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

## How to set up Jupyter Lab 4 an d jupyteer_clickable_image_widget (neccesary for collect data script)
´´´
pip install jupyterlab==4.0.10 ipywidgets
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
sudo npm install -g yarn
git clone https://github.com/jaybdub/jupyter_clickable_image_widget
cd jupyter_clickable_image_widget
cd js
yarn install
yarn add @jupyter-widgets/controls (maybe before?)
yarn run build:prod
cd ..
pip install .
jupyter lab build
´´´

## Login into eduroam wifi network via terminal: 
```
nmcli device
```
deberia verse wifi disconnected, si sale como unavailable:
```
nmcli radio wifi on
nmcli device set wlan0 managed yes
sudo systemctl restart NetworkManager
```
volver a verificar estado, y si sale como disconnected proceder con lo siguiente:
```
sudo nmcli connection add type wifi con-name eduroam ifname wlan0 ssid eduroam
```
```
sudo nmcli connection modify eduroam wifi-sec.key-mgmt wpa-eap 802-1x.eap peap 802-1x.phase2-auth mschapv2 802-1x.identity "<bannerID>@ontariotechu.ca" 802-1x.password "<password>"
```
```
sudo nmcli connection up eduroam
```
