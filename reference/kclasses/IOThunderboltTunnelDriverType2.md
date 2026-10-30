# `IOThunderboltTunnelDriverType2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000ba1ced8`; metaclass vtable `0xfffffe00084155d8`; class vtable `0xfffffe0008414f08`
- Registration (init): `0xfffffe000a5474d8`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleThunderboltUSBType2DownAdapter`](AppleThunderboltUSBType2DownAdapter.md) — `com.apple.driver.AppleThunderboltUSBType2DownAdapter`
- [`AppleThunderboltUSBType2UpAdapter`](AppleThunderboltUSBType2UpAdapter.md) — `com.apple.driver.AppleThunderboltUSBType2UpAdapter`

## Strings in its kext that name it (14)

- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::addAvailableTBTPorts - interface = %p srcPort = %p dstPort = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelWillActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelWillDeactivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::countActiveClients - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidActivate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::setTunnelSourcePort - interface = %p tbtPort = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::waitForClientStop - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::getAvailablePort - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::getAvailablePort - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::isTunnelInitializedWithTransportPort - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::areAllClientsForTransportAsleep - interface = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidDeallocate - interface = %p\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::setTunnelDestinationPort - interface = %p tbtPort = %p transportPort = 0x%x\n`
- `%lldus IOThunderboltTunnelDriverType2(%x:%llx:%x)::tunnelDidActivate - interface = %p\n`
