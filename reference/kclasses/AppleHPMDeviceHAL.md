# `AppleHPMDeviceHAL`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b94eed8`; metaclass vtable `0xfffffe00080fb3f0`; class vtable `0xfffffe00080face8`
- Registration (init): `0xfffffe0008f86e68`
- Superclasses: [`AppleHPMDevice`](AppleHPMDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 4 in total)

- [`AppleHPMDeviceHALType2`](AppleHPMDeviceHALType2.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMDeviceHALType3`](AppleHPMDeviceHALType3.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMDeviceHALType4`](AppleHPMDeviceHALType4.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (20)

- `AppleHPMDeviceHAL::setStatus - WARNING: Abnormal Status Length = 0x%x\n`
- `site.AppleHPMDeviceHAL`
- `site.AppleHPMDeviceHALType4`
- `AppleHPMDeviceHALType5::writeUSBConfigBuffer %02x %02x %02x %02x\n`
- `AppleHPMDeviceHAL::setDataStatus - WARNING: Abnormal DataStatus Length = 0x%x\n`
- `AppleHPMDeviceHALType2`
- `AppleHPMDeviceHALType3`
- `AppleHPMDeviceHALType5`
- `AppleHPMDeviceHALType4`
- `site.AppleHPMDeviceHALType3`
- `AppleHPMDeviceHAL::setPDStatus - no data, buffer or struct is null\n`
- `site.AppleHPMDeviceHALType2`
- `AppleHPMDeviceHALType5::getUSBConfigBuffer %02x %02x %02x %02x\n`
- `site.AppleHPMDeviceHALType5`
- `AppleHPMDeviceHAL::readReg - read FAILED! to ADDR = 0x%x\n`
- `AppleHPMDeviceHAL::setRxMIDBSOPStar - no data, buffer or struct is null\n`
- `AppleHPMDeviceHALType4::parseInterrupts - LDCM VBus event detected\n`
- `AppleHPMDeviceHAL::setBRDataControl - WARNING: Abnormal Data Control Length = 0x%x\n`
- `AppleHPMDeviceHAL`
- `AppleHPMDeviceHALType5::writeDataControl2 returned 0x%x\n`
