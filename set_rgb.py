import argparse
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

def setRGB(device_id, mode, color):
    """
    设置指定设备的RGB灯

    参数:
    device_id (int): 设备ID
    mode (str): 设备模式 (如 'static', 'breathing', 'flashing' 等)
    color (tuple): RGB颜色值, 例如 (255, 0, 0) 表示红色
    """
    # 连接到 OpenRGB 服务器
    client = OpenRGBClient()

    # 获取所有设备
    devices = client.devices

    # 检查设备ID是否有效
    if device_id < 0 or device_id >= len(devices):
        print("Invalid device ID")
        return

    # 获取指定设备
    device = devices[device_id]

    # 打印设备支持的模式
    print("Supported modes:")
    mode_str = ""
    for m in device.modes:
        mode_str = mode_str + m.name + " "
        
    print(f"{device.name} mode: \n{mode_str}")

    # 设置设备模式
    if mode == "default":
        mode = device.modes[0].name
    try:
        device.set_mode(mode)
    except Exception as e:
        print(f"Error setting mode: {e}")
        return

    # 设置设备颜色
    rgb_color = RGBColor(*color)
    try:
        device.set_color(rgb_color)
        print(f"Set device {device_id} to color {color} in mode {mode}")
    except Exception as e:
        print(f"Error setting color: {e}")

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="Set RGB lights for a device using OpenRGB: defualt mode is 'rainbow' and default color is '0,0,0'")
    parser.add_argument("device_id", type=int, nargs="?", default=0, help="ID of the device to control (default: 0)")
    parser.add_argument("mode", type=str, nargs="?", default="default", help="Mode to set (default: 'rainbow')")
    parser.add_argument("color", type=str, nargs="?", default="0,0,0", help="Color to set in RGB format (default: '0,0,0')")

    # 解析命令行参数
    args = parser.parse_args()

    # 解析颜色参数
    color = tuple(map(int, args.color.split(',')))

    # 调用 setRGB 函数
    setRGB(args.device_id, args.mode, color)

if __name__ == "__main__":
    main()
