# `AppleSMCPMU`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b99b4d0`; metaclass vtable `0xfffffe00082003e0`; class vtable `0xfffffe00081ffe00`
- Registration (init): `0xfffffe000967e9cc`
- Superclasses: [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCPMU` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `['smc-pmu']`, `IOProbeScore` = `1000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) on `smc-pmu`
- [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) on `smc-pmu`

## Strings in its kext that name it (17)

- `site.AppleSMCPMU`
- `AppleSMCPMU::%s(): %s vectorNumber=%d key=%08x cmd=%08x (%s)\n`
- `AppleSMCPMU`
- `AppleSMCPMU::%s(): PMU.GPIO%d -> vectorNumber=%d\n`
- `AppleSMCPMU.cpp`
- `AppleSMCPMU::start: has_smc_extended_keys = %u\n`
- `AppleSMCPMU::%s(vn=%d): %s pcIO(gpio%d) cmd=%016llx, value=%x [%s]\n`
- `AppleSMCPMU::%s(vn=%d): %s %x cmd=%08x, value=%x [%s]\n`
- `AppleSMCPMU::%s(): HID buttonIndex=%d buttonState=%d notification\n`
- `AppleSMCPMU::%s(): vectorNumber=%d disabled_soft=%d disable_hard=%d\n`
- `AppleSMCPMU::%s(): %s vectorNumber=%d pcIO(gpio%d) cmd=%016llx (%s)\n`
- `AppleSMCPMU::%s(vN=%d):`
- `AppleSMCPMU::%s(): no handler for vectorNumber=%d\n`
- `AppleSMCPMU::start\n`
- `AppleSMCPMU::%s(vn=%d): value=%x vt=%s [%s]\n`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCEmbeddedPMU/AppleSMCPMU.cpp`
- `AppleSMCPMU::%s(): Unexpected HID buttonIndex=%d\n`
