# `AppleDialogSPMIPMU`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPMIPMU`](../kexts/com.apple.driver.AppleSPMIPMU.md)
- Object size: `0x1e8` (488 bytes)
- Metaclass: `0xfffffe000b99bf70`; metaclass vtable `0xfffffe000820a750`; class vtable `0xfffffe000820a168`
- Registration (init): `0xfffffe00096bae30`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `PMU` in [`com.apple.driver.AppleSPMIPMU`](../kexts/com.apple.driver.AppleSPMIPMU.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `pmu,spmi`, `IOMatchCategory` = `AppleSPMIPMU`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) on `pmu,spmi`
- [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) on `pmu,spmi`

## Strings in its kext that name it (22)

- `site.AppleDialogSPMIPMUFunction`
- `AppleDialogSPMIPMURTC\"::setCurrentDateTime() should not be called\" @%s:%d`
- `AppleDialogSPMIPMUNub`
- `/Library/Caches/com.apple.xbs/D1D3EE44-E60F-4D19-92CF-26ECE31C940B/TemporaryDirectory.cHA6be/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp`
- `AppleDialogSPMIPMURTC`
- `AppleDialogSPMIPMURTC tick read!&&&&&&&\n`
- `AppleDialogSPMIPMURTC\"::getCurrentDateTime() should not be called\" @%s:%d`
- `AppleDialogSPMIPMURTC.cpp`
- `AppleDialogSPMIPMUFunction`
- `site.AppleDialogSPMIPMURTC`
- `AppleDialogSPMIPMURTC started!******\n`
- `site.AppleDialogSPMIPMU`
- `AppleDialogSPMIPMU: Unknown UPSI action 0x%llx - ignoring\n`
- `AppleDialogSPMIPMU: UPSI injecting action 0x%llx at boot stage 0x%x\n`
- `AppleDialogSPMIPMURTC\"::readRTCUpcountTicks() ret=0x%x\" @%s:%d`
- `%s::%sAppleDialogSPMIPMUFunction has bad format\n`
- `site.AppleDialogSPMIPMUNub`
- `AppleDialogSPMIPMURTC ending!%%%%%%\n`
- `AppleDialogSPMIPMU: UPSI injection configured - stage=0x%llx, action=0x%llx\n`
- `AppleDialogSPMIPMU.cpp`
- `AppleDialogSPMIPMU: pmu offwake\n`
- `AppleDialogSPMIPMU`
