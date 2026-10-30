# `AppleSPUAppDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0x150` (336 bytes)
- Metaclass: `0xfffffe000b99d0f8`; metaclass vtable `0xfffffe000821bdc0`; class vtable `0xfffffe000821b868`
- Registration (init): `0xfffffe00096de408`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUAppDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['SPUApp']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aop/iop-aop-nub/SPUApp`](../devicetree/root__arm-io__aop__iop-aop-nub__SPUApp.md) on `SPUApp`

## Strings in its kext that name it (10)

- `site.AppleSPUAppDriverUserClient`
- `site.AppleSPUAppDriver`
- `AppleSPUAppDriver: Register for audio notifier\n`
- `AppleSPUAppDriver : pmu-pwm-on-msg = %x\n`
- `AppleSPUAppDriver : pmu-pwm-off-msg = %x\n`
- `AppleSPUAppDriver error: pmu-pwm-off-msg not present\n`
- `AppleSPUAppDriver`
- `AppleSPUAppDriver error: pmu-pwm-on-msg not present\n`
- `AppleSPUAppDriverUserClient`
- `AppleSPUAppDriver: pdm notification message: %x, power state: %ld\n`
