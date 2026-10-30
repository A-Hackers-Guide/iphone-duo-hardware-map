# `IOPort`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0x1a8` (424 bytes)
- Metaclass: `0xfffffe000b9f23d0`; metaclass vtable `0xfffffe00083463e8`; class vtable `0xfffffe0008345db0`
- Registration (init): `0xfffffe000a009d60`
- Superclasses: [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 34 in total)

- [`IOAccessoryManager`](IOAccessoryManager.md) — `com.apple.iokit.IOAccessoryManager`
- [`IODPHDMIPortController`](IODPHDMIPortController.md) — `com.apple.iokit.IODisplayPortFamily`
- [`IOPortAIDController`](IOPortAIDController.md) — `com.apple.iokit.IOAccessoryManager`

## IOKit personalities that instantiate it (1)

- `IOPort Auto Match` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `['port']`

## Strings in its kext that name it (60)

- `com.apple.iokit.IOPort.TRM.user-access`
- `site.IOPortTransport`
- `site.IOPortTransportComponentCCUSBPD`
- `IOPortFeaturePowerIn`
- `IOPortTransport`
- `IOPortFeature`
- `com.apple.iokit.IOPortFeature.LDCM`
- `site.IOPortTransportState`
- `site.IOPortFeatureLDCM`
- `site.IOPortTransportAIDBus`
- `IOPortTransportStateUSB2`
- `IOPortFeaturePower`
- `IOPortTunnelingTransportState`
- `IOPortFeatureLDCMUserClient`
- `IOPortTransportProtocol`
- `site.IOPortNumberNode`
- `IOPortFeatureLDCM.dryToWet`
- `IOPortTransportComponentCCUSBPD`
- `IOPortFeatureLDCM`
- `site.IOPortFeaturePowerSourceOption`
- `site.IOPortFeaturePowerSource`
- `IOPortFeatureUserClient`
- `site.IOPortUserClient`
- `site.IOPortFeaturePower`
- `IOPortTransportUserClient`
- `com.apple.private.IOPortTransportAIDBusUserClient.access`
- `IOPortTransportState`
- `site.IOPortFeaturePowerSourceOptionFixed`
- `IOPortTransportStateSD`
- `IOPortTransportStatePCIe`
- `com.apple.iokit.IOPort.user-access`
- `site.IOPortTransportStateUSB`
- `site.IOPortTransportStateOrderedSet`
- `site.IOPortTransportStateUSB2`
- `com.apple.iokit.IOPortFamily`
- `site.IOPortFamily`
- `site.IOPortAIDController`
- `IOPortFeatureRFCoEx`
- `site.IOPortTransportStateCIO`
- `IOPortFeaturePowerSource`
- `site.IOPortTransportStateDisplayPort`
- `IOPortFeatureLDCMDataQueue`
- `site.IOPortTransportComponentCCUSBPDSOPp`
- `IOPortTransportStateOrderedSet`
- `IOPortTransportStateCIO`
- `site.IOPortTransportAIDBusUserClient`
- `site.IOPortTransportStateUSB3`
- `site.IOPortTransportStateSD`
- `site.IOPortTransportProtocolCCUSBPDSSAM`
- `IOPortFeatureLDCM.measurement`
- `IOPortUserClient`
- `site.IOPortTransportStatePCIe`
- `site.IOPortFeature`
- `site.IOPortTransportStateCC`
- `site.IOPortTransportComponent`
- `%s::%s(): [%s@%s: %s%s%s] m_parentPort->isFeatureEnabled(kIOPortFeatureTRM): %s, this->isTRMSupported(): %s, (transportType: %d, parentPortType: %d, parentPortNumber: %d)\n`
- `site.IOPortFeatureRFCoEx`
- `site.IOPortTransportUserClient`
- `site.IOPortTransportComponentCCUSBPDSOP`
- `site.IOPortTunnelingTransportState`
