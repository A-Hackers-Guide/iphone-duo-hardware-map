# `AppleOnboardSerialBSDClient`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleOnboardSerial`](../kexts/com.apple.driver.AppleOnboardSerial.md)
- Object size: `0x118` (280 bytes)
- Metaclass: `0xfffffe000b986bb8`; metaclass vtable `0xfffffe00081857b0`; class vtable `0xfffffe0008185258`
- Registration (init): `0xfffffe00092e5a08`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleOnboardSerialBSDClient` in [`com.apple.driver.AppleOnboardSerial`](../kexts/com.apple.driver.AppleOnboardSerial.md): `IOProviderClass` = `AppleOnboardSerialSync`, `IOResourceMatch` = `IOBSD`, `IOMatchCategory` = `AppleOnboardSerialBSDClient`, `IOProbeScore` = `1000`

## Strings in its kext that name it (9)

- `AppleOnboardSerialBSDClient: could not make kernel control socket for %s: %d\n`
- `site.AppleOnboardSerialBSDClient`
- `AppleOnboardSerialBSDClient`
- `AppleOnboardSerialBSDClient: could not make skywalk-enabled socket for %s\n`
- `AppleOnboardSerialBSDClient: could not make sk kernel control socket for %s: %d\n`
- `AppleOnboardSerialBSDClient: could not allocate device node for %s\n`
- `AppleOnboardSerialBSDClient.cpp`
- `AppleOnboardSerialBSDClient: could not make devfs node for %s\n`
- `%s: AppleOnboardSerialBSDClient recevied unexpected serial event %#llx/%#llx\n`
