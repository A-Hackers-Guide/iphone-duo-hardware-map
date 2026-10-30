# `AppleIDAMInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleIDAMInterface`](../kexts/com.apple.driver.AppleIDAMInterface.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b950fb0`; metaclass vtable `0xfffffe0008112968`; class vtable `0xfffffe0008112410`
- Registration (init): `0xfffffe0008ffec40`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleIDAMInterface` in [`com.apple.driver.AppleIDAMInterface`](../kexts/com.apple.driver.AppleIDAMInterface.md): `IOProviderClass` = `IOUSBDeviceInterface`, `IOPropertyMatch` = `{'USBDeviceFunction': 'IDAMInterface'}`

## Strings in its kext that name it (20)

- `site.AppleIDAMInterface`
- `/Library/Caches/com.apple.xbs/33C2ED7E-847A-4758-89A8-8CD4351472CC/TemporaryDirectory.XCcxY0/Sources/AppleIDAMInterface/Aspen/IDAM/AppleIDAMInterface/AppleIDAMInterface.cpp`
- `AppleIDAMInterface`
- `-> AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor()\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - Couldn't create streaming buffer!\n`
- `<- AppleIDAMInterface::addCSMSInterfaceDescriptor()\n`
- `-> AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI()\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - printing class-specific interface descriptor.\n`
- `-> AppleIDAMInterface::addEPDescriptors(0x%0X, assocJackID = %d)\n`
- `<- AppleIDAMInterface::addEPDescriptors()\n`
- `   AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() - creating bulk pipes.\n`
- `<- AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() = 0x%x\n`
- `<- AppleIDAMInterface::start() returning %s\n`
- `   AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor() - adding class-specific descriptor to interface.\n`
- `<- AppleIDAMInterface::CreateMIDIStreamingInterfaceDescriptor()\n`
- `-> AppleIDAMInterface::addCSMSInterfaceDescriptor()\n`
- `   AppleIDAMInterface::addClassSpecificDescriptorsAsMIDI() - creating endpoint descriptors.\n`
- `-> AppleIDAMInterface::start()\n`
- `-> AppleIDAMInterface::addJackDescriptor(%s, %s, jackID = %d, sourceID = %d)\n`
- `<- AppleIDAMInterface::addJackDescriptor()\n`
