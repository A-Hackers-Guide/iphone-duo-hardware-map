# `ApplePhotonDetector`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePhotonDetector`](../kexts/com.apple.driver.ApplePhotonDetector.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b989298`; metaclass vtable `0xfffffe00081a8f50`; class vtable `0xfffffe00081a89f8`
- Registration (init): `0xfffffe00093e31c8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `generic` in [`com.apple.driver.ApplePhotonDetector`](../kexts/com.apple.driver.ApplePhotonDetector.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `aop,vd5b704`
- `t8101` in [`com.apple.driver.ApplePhotonDetector`](../kexts/com.apple.driver.ApplePhotonDetector.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `i2c,vd5b704`

## Strings in its kext that name it (27)

- `site.ApplePhotonDetectorUserClient`
- `site.ApplePhotonDetector`
- `ApplePhotonDetectorUserClient`
- `ApplePhotonDetector`
- `OSValueObject<ApplePhotonDetectorClientContext>`
- `ApplePhotonDetectorUserClient - %s: New UserClient for process: %s (pid %d)\n`
- `ApplePhotonDetectorUserClient - %s: Invalid provider\n`
- `ApplePhotonDetectorUserClient - %s\n`
- `ApplePhotonDetector - %s: Could not read compatible property\n`
- `ApplePhotonDetector - %s: Matched with AOP node\n`
- `ApplePhotonDetector - %s: Could not get the IO Nub\n`
- `ApplePhotonDetector - %s: ARM Functions to control hardware not available! Check registry\n`
- `ApplePhotonDetector - %s: Matched with I2C node\n`
- `ApplePhotonDetectorUserClient - %s: Process %s (pid %d) was denied access\n`
- `ApplePhotonDetectorUserClient - %s: Could not start IOService\n`
- `ApplePhotonDetector - %s: Could not find function to control power to PhotonDetector\n`
- `ApplePhotonDetector - %s: Could not create command gate\n`
- `ApplePhotonDetector - %s: Could not add command gate to workloop\n`
- `ApplePhotonDetector - %s: Could not read compatible string\n`
- `ApplePhotonDetector - %s: Could not create photon detector workloop\n`
- `ApplePhotonDetector = %s: Could not power on the device, err = 0x%x. Exiting\n`
- `ApplePhotonDetectorUserClient - %s: Freeing UserClient for process %s (pid %d)\n`
- `ApplePhotonDetector - %s:\n`
- `ApplePhotonDetector - %s: Could not start IOService\n`
- `ApplePhotonDetector - %s: Could not get the IIC Nub\n`
- `ApplePhotonDetector - %s: %d: failed to read deviceID\n`
- `ApplePhotonDetector - %s: deviceID = 0x%x\n`
