# `IOAVAudioDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAVFamily`](../kexts/com.apple.iokit.IOAVFamily.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b9f0128`; metaclass vtable `0xfffffe00083121b0`; class vtable `0xfffffe0008311ad0`
- Registration (init): `0xfffffe0009f1a4bc`
- Superclasses: [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`DCPAVAudioDriver`](DCPAVAudioDriver.md) — `com.apple.driver.DCPAVFamilyProxy`

## IOKit personalities that instantiate it (1)

- `IOAVAudioDriver` in [`com.apple.iokit.IOAVFamily`](../kexts/com.apple.iokit.IOAVFamily.md): `IOProviderClass` = `IOAVAudioInterface`

## Strings in its kext that name it (3)

- `IOAVAudioDriver`
- `IOAVAudioDriverUserInterfaceSupported`
- `site.IOAVAudioDriver`
