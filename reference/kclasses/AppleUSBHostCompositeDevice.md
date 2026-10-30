# `AppleUSBHostCompositeDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](../kexts/com.apple.driver.usb.AppleUSBHostCompositeDevice.md)
- Object size: `0xc0` (192 bytes)
- Metaclass: `0xfffffe000ba1fda0`; metaclass vtable `0xfffffe0008466a68`; class vtable `0xfffffe0008466500`
- Registration (init): `0xfffffe000a7f158c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`AppleUSBAudioComposite`](AppleUSBAudioComposite.md) — `com.apple.driver.AppleUSBAudio`
- [`AppleUSBCDCCompositeDevice`](AppleUSBCDCCompositeDevice.md) — `com.apple.driver.usb.cdc`
- [`AppleUSBHostiOSDevice`](AppleUSBHostiOSDevice.md) — `com.apple.driver.usb.AppleUSBHostiOSDevice`

## IOKit personalities that instantiate it (14)

- `Apple AX88772a Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Asix AX88178 Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Asix AX88772 Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Asix AX88772a Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Belkin F5D5055 Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Buffalo LUA-U2-GT Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `IO-DATA ETG-US2 Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Linksys USB1000 Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Linksys USB200M Device` in [`com.apple.driver.usb.ethernet.asix`](../kexts/com.apple.driver.usb.ethernet.asix.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `11000`
- `Billboard Device` in [`com.apple.driver.usb.AppleUSBHostBillboardDevice`](../kexts/com.apple.driver.usb.AppleUSBHostBillboardDevice.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHostCompositeDevice` in [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](../kexts/com.apple.driver.usb.AppleUSBHostCompositeDevice.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBPrinterDevice0` in [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](../kexts/com.apple.driver.usb.AppleUSBHostCompositeDevice.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBPrinterDevice1` in [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](../kexts/com.apple.driver.usb.AppleUSBHostCompositeDevice.md): `IOProviderClass` = `IOUSBHostDevice`
- `InterfaceAssociationClass` in [`com.apple.driver.usb.AppleUSBHostCompositeDevice`](../kexts/com.apple.driver.usb.AppleUSBHostCompositeDevice.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (2)

- `AppleUSBHostCompositeDevice`
- `site.AppleUSBHostCompositeDevice`
