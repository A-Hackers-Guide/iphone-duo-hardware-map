# `IOUSBDeviceConfigurator`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000ba1e3d8`; metaclass vtable `0xfffffe000843ac88`; class vtable `0xfffffe000843a730`
- Registration (init): `0xfffffe000a63df60`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (5)

- `Configuration-iBridgeBringup` in [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md): `IOProviderClass` = `IOUSBDeviceController`, `IOPropertyMatch` = `{'ConfigurationType': 'iBridgeBringup'}`
- `Configuration-ncmAuxBringup` in [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md): `IOProviderClass` = `IOUSBDeviceController`, `IOPropertyMatch` = `{'ConfigurationType': 'ncmAuxBringup'}`
- `Configuration-ncmAuxOnlyBringup` in [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md): `IOProviderClass` = `IOUSBDeviceController`, `IOPropertyMatch` = `{'ConfigurationType': 'ncmAuxOnlyBringup'}`
- `Configuration-ncmBringup` in [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md): `IOProviderClass` = `IOUSBDeviceController`, `IOPropertyMatch` = `{'ConfigurationType': 'ncmBringup'}`
- `Configuration-standardBringup` in [`com.apple.iokit.IOUSBDeviceFamily`](../kexts/com.apple.iokit.IOUSBDeviceFamily.md): `IOProviderClass` = `IOUSBDeviceController`, `IOPropertyMatch` = `{'ConfigurationType': 'standardBringup'}`

## Strings in its kext that name it (3)

- `site.IOUSBDeviceConfigurator`
- `IOUSBDeviceConfigurator: controller->createUSBDevice()=0x%08x\n`
- `IOUSBDeviceConfigurator`
