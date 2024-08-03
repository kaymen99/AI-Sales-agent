# A sample products list (created with chatGPT)
# stripe_price_id is the same test stripe product
# should integrated with real products DB in production
products = [
    {
        "category": "Laptops",
        "model": "Dell XPS 13",
        "processor": "Intel Core i5",
        "memory": "8GB DDR4",
        "storage": "256GB SSD",
        "display": "13-inch Full HD",
        "graphics": "Integrated Intel UHD",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 700
    },
    {
        "category": "Laptops",
        "model": "MacBook Pro 15",
        "processor": "Intel Core i7",
        "memory": "16GB DDR4",
        "storage": "512GB SSD",
        "display": "15-inch Full HD",
        "graphics": "NVIDIA GeForce GTX 1650",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 1200
    },
    {
        "category": "Laptops",
        "model": "HP Envy 17",
        "processor": "AMD Ryzen 7",
        "memory": "16GB DDR4",
        "storage": "1TB SSD",
        "display": "17-inch 4K",
        "graphics": "AMD Radeon RX 580",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 2000
    },
    {
        "category": "Desktops",
        "model": "Alienware Aurora R11",
        "processor": "Intel Core i7",
        "memory": "16GB DDR4",
        "storage": "1TB HDD",
        "graphics": "NVIDIA GeForce RTX 2060",
        "cooling": "Air cooling",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 1000
    },
    {
        "category": "Desktops",
        "model": "Corsair One i200",
        "processor": "Intel Core i9",
        "memory": "32GB DDR4",
        "storage": "2TB SSD",
        "graphics": "NVIDIA GeForce RTX 3080",
        "cooling": "Liquid cooling",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 2500
    },
    {
        "category": "Desktops",
        "model": "CyberPowerPC Gamer Supreme",
        "processor": "AMD Ryzen 9",
        "memory": "64GB DDR4",
        "storage": "1TB SSD + 2TB HDD",
        "graphics": "AMD Radeon RX 6900 XT",
        "cooling": "Liquid cooling",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 3000
    },
    {
        "category": "Monitors",
        "model": "Dell UltraSharp U2419H",
        "display_type": "IPS",
        "resolution": "1920x1080",
        "refresh_rate": "60Hz",
        "size": "24-inch",
        "connectivity": "HDMI, DisplayPort",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 200
    },
    {
        "category": "Monitors",
        "model": "Samsung Odyssey G7",
        "display_type": "VA",
        "resolution": "2560x1440",
        "refresh_rate": "144Hz",
        "size": "27-inch",
        "connectivity": "HDMI, DisplayPort, USB-C",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 400
    },
    {
        "category": "Monitors",
        "model": "LG UltraFine 32UL950-W",
        "display_type": "OLED",
        "resolution": "3840x2160",
        "refresh_rate": "120Hz",
        "size": "32-inch",
        "connectivity": "HDMI, DisplayPort, USB-C",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 1000
    },
    {
        "category": "Keyboards",
        "model": "Corsair K95 RGB Platinum",
        "type": "Mechanical",
        "switch_type": "Cherry MX Red",
        "lighting": "RGB",
        "connectivity": "Wired USB",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 100
    },
    {
        "category": "Keyboards",
        "model": "Logitech K120",
        "type": "Membrane",
        "switch_type": "Quiet keys",
        "lighting": "Single color",
        "connectivity": "Wired USB",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 50
    },
    {
        "category": "Keyboards",
        "model": "Razer BlackWidow V3 Pro",
        "type": "Mechanical",
        "switch_type": "Cherry MX Blue",
        "lighting": "RGB",
        "connectivity": "Wireless",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 150
    },
    {
        "category": "Mice",
        "model": "Logitech G502 Hero",
        "sensor_type": "Optical",
        "dpi": "8000 DPI",
        "buttons": "6 programmable",
        "connectivity": "Wired USB",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 50
    },
    {
        "category": "Mice",
        "model": "Razer DeathAdder V2",
        "sensor_type": "Laser",
        "dpi": "16000 DPI",
        "buttons": "8 programmable",
        "connectivity": "Wireless",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 100
    },
    {
        "category": "Mice",
        "model": "SteelSeries Rival 650",
        "sensor_type": "Optical",
        "dpi": "12000 DPI",
        "buttons": "7 programmable",
        "connectivity": "Bluetooth",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 75
    },
    {
        "category": "Graphics Cards",
        "model": "ASUS ROG Strix RTX 3060",
        "chipset": "NVIDIA GeForce RTX 3060",
        "memory": "12GB GDDR6",
        "cooling": "Dual-fan",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 400
    },
    {
        "category": "Graphics Cards",
        "model": "EVGA GeForce RTX 3080 FTW3",
        "chipset": "NVIDIA GeForce RTX 3080",
        "memory": "10GB GDDR6X",
        "cooling": "Triple-fan",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 800
    },
    {
        "category": "Graphics Cards",
        "model": "Sapphire Nitro+ RX 6800 XT",
        "chipset": "AMD Radeon RX 6800 XT",
        "memory": "16GB GDDR6",
        "cooling": "Liquid cooling",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 900
    },
    {
        "category": "Storage Devices",
        "model": "Samsung 860 EVO",
        "type": "SATA SSD",
        "capacity": "512GB",
        "read_speed": "550MB/s",
        "write_speed": "520MB/s",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 100
    },
    {
        "category": "Storage Devices",
        "model": "WD Black SN750",
        "type": "NVMe SSD",
        "capacity": "1TB",
        "read_speed": "3500MB/s",
        "write_speed": "3300MB/s",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 200
    },
    {
        "category": "Storage Devices",
        "model": "Seagate Barracuda",
        "type": "HDD",
        "capacity": "2TB",
        "read_speed": "160MB/s",
        "write_speed": "150MB/s",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 80
    },
    {
        "category": "Networking Equipment",
        "model": "TP-Link Archer A7",
        "type": "Dual-band Router",
        "speed": "AC1200",
        "features": "MU-MIMO, QoS",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 50
    },
    {
        "category": "Networking Equipment",
        "model": "Netgear Nighthawk AX12",
        "type": "Tri-band Router",
        "speed": "AX6000",
        "features": "MU-MIMO, QoS, VPN support",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 250
    },
    {
        "category": "Networking Equipment",
        "model": "Cisco SG350-10",
        "type": "Managed Switch",
        "ports": 16,
        "speed": "Gigabit",
        "features": "VLAN, QoS",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 100
    },
    {
        "category": "Accessories",
        "model": "Noctua NH-D15",
        "type": "CPU Cooler",
        "cooling_type": "Air cooling",
        "compatibility": "Intel and AMD",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 50
    },
    {
        "category": "Accessories",
        "model": "Corsair LL120",
        "type": "Case Fan",
        "size": "120mm",
        "features": "RGB lighting",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 20
    },
    {
        "category": "Accessories",
        "model": "AmazonBasics HDMI Cable",
        "type": "HDMI Cable",
        "length": "6 feet",
        "features": "4K support",
        "stripe_price_id" : "price_1PhAgsDhcxHZPqUXh81bslrj",
        "price": 10
    }
]