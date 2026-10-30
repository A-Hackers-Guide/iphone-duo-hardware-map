# `AppleC26Packet`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleC26Charger`](../kexts/com.apple.driver.AppleC26Charger.md)
- Object size: `0x68` (104 bytes)
- Metaclass: `0xfffffe000b938548`; metaclass vtable `0xfffffe0008005260`; class vtable `0xfffffe0008005180`
- Registration (init): `0xfffffe0008a28438`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (3; 3 in total)

- [`AppleC26FFBPacket`](AppleC26FFBPacket.md) — `com.apple.driver.AppleC26Charger`
- [`AppleCallistoPacket`](AppleCallistoPacket.md) — `com.apple.driver.AppleC26Charger`
- [`AppleWirelessPowerPacket`](AppleWirelessPowerPacket.md) — `com.apple.driver.AppleC26Charger`

## Strings in its kext that name it (4)

- `AppleC26Packet`
- `%s: receivePacketFromController() called with NULL packet or wrong AppleC26Packet subclass (%p %p)\n`
- `site.AppleC26Packet`
- `%s: completeSendTelegramGated() called with ACK packet of the wrong AppleC26Packet subclass (%p %p)\n`
