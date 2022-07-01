from uuid import UUID

from .utils import UUIDDict

service = UUIDDict(
    {
        0x1800: "Generic Access",
        0x1811: "Alert Notification Service",
        0x1815: "Automation IO",
        0x180F: "Battery Service",
        0x1810: "Blood Pressure",
        0x181B: "Body Composition",
        0x181E: "Bond Management Service",
        0x181F: "Continuous Glucose Monitoring",
        0x1805: "Current Time Service",
        0x1818: "Cycling Power",
        0x1816: "Cycling Speed and Cadence",
        0x180A: "Device Information",
        0x181A: "Environmental Sensing",
        0x1826: "Fitness Machine",
        0x1801: "Generic Attribute",
        0x1808: "Glucose",
        0x1809: "Health Thermometer",
        0x180D: "Heart Rate",
        0x1823: "HTTP Proxy",
        0x1812: "Human Interface Device",
        0x1802: "Immediate Alert",
        0x1821: "Indoor Positioning",
        0x183A: "Insulin Delivery",
        0x1820: "Internet Protocol Support Service",
        0x1803: "Link Loss",
        0x1819: "Location and Navigation",
        0x1827: "Mesh Provisioning Service",
        0x1828: "Mesh Proxy Service",
        0x1807: "Next DST Change Service",
        0x1825: "Object Transfer Service",
        0x180E: "Phone Alert Status Service",
        0x1822: "Pulse Oximeter Service",
        0x1829: "Reconnection Configuration",
        0x1806: "Reference Time Update Service",
        0x1814: "Running Speed and Cadence",
        0x1813: "Scan Parameters",
        0x1824: "Transport Discovery",
        0x1804: "Tx Power",
        0x181C: "User Data",
        0x181D: "Weight Scale",
        0xFE0F: "Signify Netherlands B.V. (formerly Phillips Lighting) Service",
        0xFEAA: "Eddystone",
        0xFE2C: "Fast Pair Service",
        0xFE59: "Secure DFU Service",
        0xFD6F: "Exposure Notification Service",
        0xFEBB: "File Transfer Service by Adafruit",
        UUID(
            "932C32BD-0000-47A2-835A-A8D455B859DD"
        ): "Phillips Hue Light Control Service",
        UUID(
            "0000180A-0000-1000-8000-00805F9B34FB"
        ): "Phillips Hue Light Information Service",
        UUID(
            "B8843ADD-0000-4AA1-8794-C3F462030BDA"
        ): "Phillips Hue Light Update Service",
        UUID(
            "7905F431-B5CE-4E99-A40F-4B1E122D00D0"
        ): "Apple Notification Center Service",
        UUID("89D3502B-0F36-433A-8EF4-C502AD55F8DC"): "Apple Media Service",
        UUID("7DFC6000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC7000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC8000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("7DFC9000-7D1C-4951-86AA-8D9728F8D66C"): "Apple Reserved Service",
        UUID("E95D0753-251D-470A-A062-FA1922DFA9A8"): "micro:bit Accelerometer Service",
        UUID("E95DF2D8-251D-470A-A062-FA1922DFA9A8"): "micro:bit Magnetometer Service",
        UUID("E95D9882-251D-470A-A062-FA1922DFA9A8"): "micro:bit Button Service",
        UUID("E95D127B-251D-470A-A062-FA1922DFA9A8"): "micro:bit IO Pin Service",
        UUID("E95DD91D-251D-470A-A062-FA1922DFA9A8"): "micro:bit LED Service",
        UUID("E95D93AF-251D-470A-A062-FA1922DFA9A8"): "micro:bit Event Service",
        UUID("E95D93B0-251D-470A-A062-FA1922DFA9A8"): "micro:bit DFU Control Service",
        UUID("E95D6100-251D-470A-A062-FA1922DFA9A8"): "micro:bit Temperature Service",
        UUID("EF680100-9B35-4933-9B10-52FFA9740042"): "Thingy Configuration Service",
        UUID("EF680200-9B35-4933-9B10-52FFA9740042"): "Thingy Weather Station Service",
        UUID("EF680300-9B35-4933-9B10-52FFA9740042"): "Thingy UI Service",
        UUID("EF680400-9B35-4933-9B10-52FFA9740042"): "Thingy Motion Service",
        UUID("EF680500-9B35-4933-9B10-52FFA9740042"): "Thingy Sound Service",
        UUID("00001523-1212-EFDE-1523-785FEABCD123"): "Nordic LED and Button Service",
        UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"): "Nordic UART Service",
        UUID("A3C87500-8ED3-4BDF-8A39-A01BEBEDE295"): "Eddystone Configuration Service",
        UUID("00001530-1212-EFDE-1523-785FEABCD123"): "Legacy DFU Service",
        UUID(
            "8E400001-F315-4F60-9FB8-838830DAEA50"
        ): "Experimental Buttonless DFU Service",
        UUID(
            "E2A00001-EC31-4EC3-A97A-1C34D87E9878"
        ): "Edge Impulse Remote Management Service",
        UUID("8D53DC1D-1DB7-4CD3-868B-8A527460AA84"): "SMP Service",
        UUID(
            "00001623-1212-EFDE-1623-785FEABCD123"
        ): "LEGO® Wireless Protocol v3 Hub Service",
        UUID(
            "00001625-1212-EFDE-1623-785FEABCD123"
        ): "LEGO® Wireless Protocol v3 Bootloader Service",
        UUID("ADAF0100-C332-42A8-93BD-25E905756CB8"): "Adafruit Temperature Service",
        UUID("ADAF0200-C332-42A8-93BD-25E905756CB8"): "Adafruit Accelerometer Service",
        UUID("ADAF0300-C332-42A8-93BD-25E905756CB8"): "Adafruit Light Service",
        UUID("ADAF0400-C332-42A8-93BD-25E905756CB8"): "Adafruit Gyroscope Service",
        UUID("ADAF0500-C332-42A8-93BD-25E905756CB8"): "Adafruit Magnetometer Service",
        UUID("ADAF0600-C332-42A8-93BD-25E905756CB8"): "Adafruit Button Service",
        UUID("ADAF0700-C332-42A8-93BD-25E905756CB8"): "Adafruit Humidity Service",
        UUID("ADAF0800-C332-42A8-93BD-25E905756CB8"): "Adafruit Barometric Service",
        UUID("ADAF0900-C332-42A8-93BD-25E905756CB8"): "Adafruit Addressable Service",
        UUID("ADAF0A00-C332-42A8-93BD-25E905756CB8"): "Adafruit Color Service",
        UUID("ADAF0B00-C332-42A8-93BD-25E905756CB8"): "Adafruit Sound Service",
        UUID("ADAF0C00-C332-42A8-93BD-25E905756CB8"): "Adafruit Tone Service",
        UUID("ADAF0D00-C332-42A8-93BD-25E905756CB8"): "Adafruit Quaternion Service",
        UUID("ADAF0E00-C332-42A8-93BD-25E905756CB8"): "Adafruit Proximity Service",
        UUID(
            "F000FFC0-0451-4000-B000-000000000000"
        ): "Texas Instruments Over-the-Air Download (OAD) Service",
        UUID("0FDA92B2-44A2-4AF2-84F5-FA682BAA2B8D"): "Helium Hotspot Custom Service",
    }
)
