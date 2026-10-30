# `ApplePPMCPMSv2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md)
- Object size: `0x9838` (38,968 bytes)
- Metaclass: `0xfffffe000b9dbe50`; metaclass vtable `0xfffffe00082bc7e0`; class vtable `0xfffffe00082bc028`
- Registration (init): `0xfffffe0009b8e1cc`
- Superclasses: [`ApplePPMCPMS`](ApplePPMCPMS.md) → [`ApplePPM`](ApplePPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleiPhoneACSKPPM` in [`com.apple.driver.AppleiPhoneACSKPPM`](../kexts/com.apple.driver.AppleiPhoneACSKPPM.md): `IOProviderClass` = `ApplePMGRNub`, `IONameMatch` = `ppm,iphoneacsk`, `IOMatchCategory` = `ApplePPMCPMSv2`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) on `ppm,iphoneacsk`

## Strings in its kext that name it (9)

- `virtual bool ApplePPMCPMSv2::setSystemCapability(const int *, int32_t, uint8_t)`
- `virtual uint32_t ApplePPMCPMSv2::powerValueToBudgetScalar(uint32_t, UniqueClientID_t)`
- `ApplePPMCPMSv2`
- `virtual int32_t *ApplePPMCPMSv2::systemCapabilityToUse()`
- `site.ApplePPMCPMSv2`
- `virtual int32_t *ApplePPMCPMSv2::batteryPowerConsumptionPMUToUse()`
- `virtual void ApplePPMCPMSv2::setBrownoutRiskSysCap(int32_t, int32_t, uint8_t)`
- `ApplePPMCPMSv2.cpp`
- `virtual void ApplePPMCPMSv2::powerReport(int32_t *, uint32_t)`
