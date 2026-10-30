# `AppleUSBHostMergeProperties`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000ba1fff0`; metaclass vtable `0xfffffe0008467c60`; class vtable `0xfffffe00084676f8`
- Registration (init): `0xfffffe000a7f3380`
- Superclasses: [`IOProviderPropertyMerger`](IOProviderPropertyMerger.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (69)

- `AppleEmbeddedUSBCardReader` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleEmbeddedUSBCardReaderPrototype` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSB20Hub_32789_merge` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `IOUSBHostDevice`
- `ParrotUSBResetLockup` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `AppleT8101USB20XHCILightningPort`
- `iOSDFU-Merge` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `AppleEmbeddedUSBDevice`
- `iOSRecovery-Merge` in [`com.apple.driver.AppleEmbeddedUSBHost`](../kexts/com.apple.driver.AppleEmbeddedUSBHost.md): `IOProviderClass` = `AppleEmbeddedUSBDevice`
- `Adapter HID` in [`com.apple.driver.AppleUSBAudio`](../kexts/com.apple.driver.AppleUSBAudio.md): `IOProviderClass` = `IOHIDDevice`
- `Billboard Device Properties` in [`com.apple.driver.usb.AppleUSBHostBillboardDevice`](../kexts/com.apple.driver.usb.AppleUSBHostBillboardDevice.md): `IOProviderClass` = `IOUSBHostDevice`
- `Billboard Interface Properties` in [`com.apple.driver.usb.AppleUSBHostBillboardDevice`](../kexts/com.apple.driver.usb.AppleUSBHostBillboardDevice.md): `IOProviderClass` = `IOUSBHostInterface`
- `AnkerUsbPowerSinkCapability-3000` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple 0x9226-7 Device` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Apple 0x9226-7 Interface` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBInterface`
- `Apple Acrylic Keyboard` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBInterface`
- `Apple LED Display Audio Device` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Apple Studio Display` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple WS Device` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Apple WS Interface` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBInterface`
- `AppleUsbPowerSinkCapability-1000` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-1300` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-1500` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-2100` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-2400` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-3000` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-500` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-700` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUsbPowerSinkCapability-800` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `BelkinUsbPowerSinkCapability-1500` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `DisplayiSight - 0x219` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Lightning Digital AV Adapter` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Lightning VGA Adapter` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBDevice`
- `Linksys USB3GIGV1` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `LogitechUsbPowerSinkCapability-2400` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `Moshi USB 10/100/1000 LAN` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `SIXAXIS controller` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBInterface`
- `eLicenser Enable Data Toggle Reset` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostInterface`
- `iPhoneUsbPowerSinkCapability-1000` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `iPhoneUsbPowerSinkCapability-2400` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `iPod` in [`com.apple.driver.AppleUSBHostMergeProperties`](../kexts/com.apple.driver.AppleUSBHostMergeProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple Aluminium Keyboard Properties` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple DVI to display port hub` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple Display Properties` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple USB-C Digital AV Multiport Adapter Properties V1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple USB-C Digital AV Multiport Adapter Properties V2 4.3.2` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple USB-C Digital AV Multiport Adapter Properties V2 4.3.3` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Apple USB-C VGA Multiport Adapter Properties` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleHub5678v1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`, `IOProbeScore` = `1000`
- `AppleUSBCameraKitHub` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37143` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37144` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37149v1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37151v1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37152v307` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37158` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37159` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSBHub37174` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Bretford Cart 4-port` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Bretford Cart 7-port` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `GenesysUSB30Hub-GL3520` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `GenesysUSB30Hubs` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Kinesis Keyboard Hub` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `LG USBC External Hub` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Lenovo VL820` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Personality1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `ThunderboltDisplay2011-InternalHub` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `USBHub8193-61699` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `VIA Labs VL820` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `ViaVL210Hubs` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `Mac Internal Hub Properties` in [`com.apple.driver.usb.AppleUSBHostPlatformProperties`](../kexts/com.apple.driver.usb.AppleUSBHostPlatformProperties.md): `IOProviderClass` = `IOUSBHostDevice`
- `Mac Internal Hub Properties 2` in [`com.apple.driver.usb.AppleUSBHostPlatformProperties`](../kexts/com.apple.driver.usb.AppleUSBHostPlatformProperties.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (2)

- `AppleUSBHostMergeProperties`
- `site.AppleUSBHostMergeProperties`
