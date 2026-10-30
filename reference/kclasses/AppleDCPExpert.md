# `AppleDCPExpert`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md)
- Object size: `0x2d08` (11,528 bytes)
- Metaclass: `0xfffffe000b940558`; metaclass vtable `0xfffffe000804c430`; class vtable `0xfffffe000804be88`
- Registration (init): `0xfffffe0008b66334`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleDCPExpert` in [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `dcp-expert-v1`

## Device-tree nodes it binds (3) [DT]

- [`/arm-io/dcp0-expert`](../devicetree/root__arm-io__dcp0-expert.md) on `dcp-expert-v1`
- [`/arm-io/dcpsec-expert`](../devicetree/root__arm-io__dcpsec-expert.md) on `dcp-expert-v1`
- [`/arm-io/dcpext0-expert`](../devicetree/root__arm-io__dcpext0-expert.md) on `dcp-expert-v1`

## Strings in its kext that name it (25)

- `[AppleDCPExpert:0x%llx] open fail 0x%llx\n`
- `void AppleDCPExpert::_enterTrace(UInt32, void * _Nullable, void * _Nullable, void * _Nullable)`
- `\"[AppleDCPExpert:0x%llx] GAPF error with empty assertion mask\\n\" @%s:%d`
- `\"[AppleDCPExpert:0x%llx] GAPF Error (0x%x): failed to find violated GAPF\\n\" @%s:%d`
- `AppleDCPExpert::%s unexpected response size of %u: %zu\n`
- `void AppleDCPExpert::_pollReg(IOLogicalAddress, UInt32, UInt32, UInt32, bool)`
- `AppleDCPExpert::%s unexpected response size of %u: %u\n`
- `virtual bool AppleDCPExpert::start(IOService *)`
- `void AppleDCPExpert::_setDispSysFePowerGateEnable(bool)`
- `[AppleDCPExpert:0x%llx]_changeDCPPowerStateInternal:%x\n`
- `%s failed to get AppleDCPExpert\n`
- `site.AppleDCPExpert`
- `AppleDCPExpert`
- `[AppleDCPExpert:0x%llx] _setDCPExpertPowerState(%d,%d):%x duration:%lld\n`
- `[AppleDCPExpert:0x%llx] mogul auth failed\n`
- `[AppleDCPExpert:0x%llx]: support-health-telemetry present but mogul path not in devicetree\n`
- `AppleDCPExpert.cpp`
- `[AppleDCPExpert:0x%llx] mogul provider not found\n`
- `IOReturn AppleDCPExpert::_changeDCPPowerStateInternal(DCPPowerState)`
- `\"[AppleDCPExpert:0x%llx] GAPF Error (0x%x): Master ID %u, Address 0x%llx, CMD %s\\n\" @%s:%d`
- `void AppleDCPExpert::_setDCPForceWakeup(bool)`
- `AppleDCPExpert::%s epic unavailable\n`
- `[AppleDCPExpert:0x%llx] failed to create mogul matching dict\n`
- `void AppleDCPExpert::_setPMGRScratchRegion(bool)`
- `void AppleDCPExpert::_setConditionalRetentionEnable(bool)`
