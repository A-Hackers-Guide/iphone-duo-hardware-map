# `AppleAOPAudioService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAOPAudio`](../kexts/com.apple.driver.AppleAOPAudio.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b932ea0`; metaclass vtable `0xfffffe0007fa6408`; class vtable `0xfffffe0007fa5dc0`
- Registration (init): `0xfffffe000869ea04`
- Superclasses: [`AppleAOPAudioServiceBase`](AppleAOPAudioServiceBase.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (17)

- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameFastClockSpeed, &lowPowerConfig.fastClockSpeed )`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNamePdmcFrequency, &lowPowerConfig.pdmcFrequency )`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameSlowClockSpeed, &lowPowerConfig.slowClockSpeed )`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameChannelPolaritySelect, &lowPowerConfig.channelPolaritySelect, sizeof(lowPowerConfig.channelPolaritySelect) )`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameChannelCount, &channelCount)`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicTurnOnTimeMs, &micParams.micTurnOnTimeMs.value[0])`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNamePdmFrequency, &lowPowerConfig.pdmFrequency )`
- `AppleAOPAudioServiceBase`
- `site.AppleAOPAudioServiceBase`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameBytesPerSample, &lowPowerConfig.bytesPerSample )`
- `site.AppleAOPAudioService`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameMicSettleTimeMs, &lowPowerConfig.pdmMicTuningParams.micSettleTimeMs.value[0])`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameClockSource, &lowPowerConfig.clockSource )`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicSettleTimeMs, &micParams.micSettleTimeMs.value[0])`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameChannelPhaseSelect, &lowPowerConfig.channelPhaseSelect, sizeof(lowPowerConfig.channelPhaseSelect) )`
- `AppleAOPAudioService::getNamedProperty(inService, kPropertyNameMicSensitivitydB, &micSensitivitydB)`
- `AppleAOPAudioService::getNamedProperty(inProvider, kPropertyNameMicTurnOnTimeMs, &lowPowerConfig.pdmMicTuningParams.micTurnOnTimeMs.value[0])`
