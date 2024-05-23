# rgb_aura

## installation

install openRGB

```bash
sudo add-apt-repository ppa:thopiekar/openrgb
sudo apt update
sudo apt upgrade openrgb
pip install openrgb-python
```

start andtest

```bash
sudo killall openrgb
sudo openrgb --server

python set_rgb.py 0 static 255,0,0
```
make them as a service

```
sudo copy pathto/openrgb.service /etc/systemd/system/openrgb.service
sudo systemctl daemon-reload
sudo systemctl enable openrgb
sudo systemctl start openrgb
sudo systemctl daemon-reload
```

