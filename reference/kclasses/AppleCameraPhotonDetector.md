# `AppleCameraPhotonDetector`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCameraPhotonDetector`](../kexts/com.apple.driver.AppleCameraPhotonDetector.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b93ac90`; metaclass vtable `0xfffffe00080240f0`; class vtable `0xfffffe0008023b98`
- Registration (init): `0xfffffe0008adb4ec`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `generic` in [`com.apple.driver.AppleCameraPhotonDetector`](../kexts/com.apple.driver.AppleCameraPhotonDetector.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `aop,h16,vd5b704`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) on `aop,h16,vd5b704`

## Strings in its kext that name it (28)

- `AppleCameraPhotonDetectorUserClient`
- `site.AppleCameraPhotonDetectorUserClient`
- `AppleCameraPhotonDetector`
- `site.AppleCameraPhotonDetector`
- `OSValueObject<AppleCameraPhotonDetectorClientContext>`
- `AppleCameraPhotonDetectorUserClient:%s - New UserClient for process: %s (pid %d)\n`
- `AppleCameraPhotonDetectorUserClient:%s - client died\n`
- `AppleCameraPhotonDetector:%s - Could not start IOService\n`
- `AppleCameraPhotonDetector:%s - Could not get the IO Nub\n`
- `AppleCameraPhotonDetector:%s - %d: failed to read deviceID\n`
- `AppleCameraPhotonDetectorUserClient:%s - Could not start IOService\n`
- `AppleCameraPhotonDetector:%s - starting\n`
- `AppleCameraPhotonDetector:%s - Could not read compatible property\n`
- `AppleCameraPhotonDetector:%s - Could not get the IIC Nub\n`
- `AppleCameraPhotonDetectorUserClient:%s - Invalid provider\n`
- `AppleCameraPhotonDetector:%s - Matched with AOP node\n`
- `AppleCameraPhotonDetector:%s - ARM Functions to control hardware not available! Check registry\n`
- `AppleCameraPhotonDetector:%s - Matched with I2C node\n`
- `AppleCameraPhotonDetector:%s - Could not find function to control power to PhotonDetector\n`
- `AppleCameraPhotonDetector:%s - Could not create photon detector workloop\n`
- `AppleCameraPhotonDetector:%s - Could not add command gate to workloop\n`
- `AppleCameraPhotonDetectorUserClient:%s - Process %s (pid %d) was denied access\n`
- `AppleCameraPhotonDetectorUserClient:%s - Freeing UserClient for process %s (pid %d)\n`
- `AppleCameraPhotonDetector:%s - Could not read compatible string\n`
- `AppleCameraPhotonDetector:%s - Could not create command gate\n`
- `AppleCameraPhotonDetector:%s - Could not power on the device, err = 0x%x. Exiting\n`
- `AppleCameraPhotonDetector:%s - Could not allocate an array to store the list of clients\n\n`
- `AppleCameraPhotonDetector:%s - deviceID = 0x%x\n`
