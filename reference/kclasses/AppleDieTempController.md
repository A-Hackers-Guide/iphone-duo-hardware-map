# `AppleDieTempController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b943f60`; metaclass vtable `0xfffffe0008090790`; class vtable `0xfffffe0008090238`
- Registration (init): `0xfffffe0008c86c94`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleDieTempController` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['dietempctl,s5l8960x', 'dietempctl,t7000', 'dietempctl,t7001', 'dietempctl,s800`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (48)

- `AppleDieTempController::%s: Loop%d Sensors: %c%c%c%c\n`
- `AppleDieTempController::%s: Got CLPC version %d\n`
- `site.AppleDieTempController`
- `AppleDieTempController::%s: Loop: %d kp: 0x%x kits: 0x%x ctlType: 0x%x numSensors: %d\n`
- `AppleDieTempController::%s: Override loop %d kits to 0x%x\n`
- `AppleDieTempController::%s: Printing all configured loop data\n`
- `AppleDieTempController::%s: Override loop %d kp to 0x%x\n`
- `AppleDieTempController::%s: In handleBootArgs routine\n`
- `AppleDieTempController::%s: Override kp to %d\n`
- `AppleDieTempController::%s: couldn't start provider\n`
- `AppleDieTempController::%s: No loops exist for registering this sensor\n`
- `AppleDieTempController.cpp`
- `AppleDieTempController::%s: boot_dvd_factor 0x%08x\n`
- `AppleDieTempController::%s: pmgr null dict\n`
- `AppleDieTempController::%s: props is NULL\n`
- `AppleDieTempController::%s: couldn't create command gate\n`
- `AppleDieTempController::%s: _cpuPerfController is NULL\n`
- `AppleDieTempController::%s: Override kits to %d\n`
- `AppleDieTempController::%s: NULL properties dictionary\n`
- `AppleDieTempController::%s:  Config Complete %x\n`
- `AppleDieTempController::%s: pmgr null propData\n`
- `AppleDieTempController::%s: could not connect to %s\n\n`
- `AppleDieTempController::%s: iterator is NULL\n`
- `AppleDieTempController::%s: sensor data length doesn't make sense: %d\n`
- `AppleDieTempController::%s: couldn't cast dictionary\n`
- `AppleDieTempController::%s: Override interval to %d\n`
- `AppleDieTempController::%s:  _tGraphModeEnable(%x) config complete\n`
- `AppleDieTempController::%s: Loop %d control type: %d\n`
- `AppleDieTempController::%s: couldn't create dieTempSensorsSnapshot\n`
- `AppleDieTempController::%s: pmgr null service\n`
- `AppleDieTempController::%s: Loop %d kp: 0x%x\n`
- `AppleDieTempController::%s: couldn't create loop %d sensor set\n`
- `site.AppleDieTempControllerUserClient`
- `AppleDieTempController::%s: No loop sensor data for loop %d\n`
- `AppleDieTempController::%s: Override release temp to %d\n`
- `AppleDieTempController::%s: couldn't create _dieTempSensors\n`
- `AppleDieTempController::%s: key is NULL\n`
- `AppleDieTempControllerUserClient`
- `AppleDieTempController`
- `AppleDieTempController::%s: couldn't create loopSensorsSnapshot\n`
- `AppleDieTempController::%s: Loop %d ki: 0x%x\n`
- `AppleDieTempController::%s: provider is not AppleARMIODevice\n`
- `AppleDieTempController::%s: Successfully configured %d loops\n`
- `AppleDieTempController::%s: couldn't create _dieTempControllerLock\n`
- `AppleDieTempController::%s: couldn't create _loopTimer\n`
- `AppleDieTempController::%s: \n`
- `AppleDieTempController::%s: couldn't add timer to workloop\n`
- `AppleDieTempController::%s: Setting up legacy style (single loop) fast die control\n`
