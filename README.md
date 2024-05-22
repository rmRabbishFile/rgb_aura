# rgb_aura

## installation

install openRGB

```bash
sudo add-apt-repository ppa:thopiekar/openrgb
sudo apt update
sudo apt upgrade openrgb
```

start

```bash
sudo killall openrgb
sudo openrgb --server
```
make them as a service

```
sudo copy pathto/openrgb.service /etc/systemd/system/openrgb.service
sudo systemctl daemon-reload
sudo systemctl enable openrgb
sudo systemctl start openrgb
sudo systemctl daemon-reload
```

