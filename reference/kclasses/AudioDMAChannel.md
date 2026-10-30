# `AudioDMAChannel`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AudioDMAController-Gen5p0`](../kexts/com.apple.driver.AudioDMAController-Gen5p0.md)
- Object size: `0x380` (896 bytes)
- Metaclass: `0xfffffe000b9def50`; metaclass vtable `0xfffffe00082c3fd8`; class vtable `0xfffffe00082c3a20`
- Registration (init): `0xfffffe0009be0ae8`
- Superclasses: [`ADMAChannel`](ADMAChannel.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (25)

- `AudioDMAChannelStateMachine.cpp`
- `AudioDMAChannelSharedResource.cpp`
- `site.AudioDMAChannel`
- `tx->gatePower(AudioDMAChannel::kAudioDMAChannelPowerStateAvailable, softTransition) == kIOReturnSuccess`
- `AudioDMAChannelStateMachine::AudioDMAChannelStateMachine(const char *, uint32_t, IORecursiveLock *)`
- `uint32_t AudioDMAChannelSharedResourceManager::allocateChannelBufferAperture(const char *, bool, uint32_t, uint32_t &)`
- `AudioDMAChannelSharedResourceManager`
- `/Library/Caches/com.apple.xbs/EDB52463-4048-495D-AB86-88E13335F3E1/TemporaryDirectory.lXLcfx/Sources/AudioDMAController/v5p0/Kext/AudioDMAChannel/AudioDMAChannelStateMachine.cpp`
- `tx->getPowerState() == AudioDMAChannel::kAudioDMAChannelPowerStateSuspended`
- `processChannelOperation(AudioDMAChannelStateMachine::ADMACOPER_Finish) == kIOReturnSuccess`
- `processChannelOperation(AudioDMAChannelStateMachine::ADMACOPER_ProcessMoreTransfers) == kIOReturnSuccess`
- `i16@?0^{AudioDMAChannel=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}^{IOCommandGate}B^{IOCommandPool}{queue_entry=^{queue_entry}^{queue_entry}}{?=B^{TransferRequest}}^{IOCommandPool}II^{OSDictionary}{queue_ent`
- `site.AudioDMAChannelConfiguration`
- `rx->getPowerState() == AudioDMAChannel::kAudioDMAChannelPowerStateSuspended`
- `AudioDMAChannelStateMachine`
- `processChannelOperation(AudioDMAChannelStateMachine::ADMACOPER_ProcessDone) == kIOReturnSuccess`
- `rx->gatePower(AudioDMAChannel::kAudioDMAChannelPowerStateAvailable, softTransition) == kIOReturnSuccess`
- `_admacTxChannels[channelIndex]->gatePower( AudioDMAChannel::kAudioDMAChannelPowerStateAvailable, softTransition) == kIOReturnSuccess`
- `AudioDMAChannel`
- `AudioDMAChannel.cpp`
- `processChannelOperation( AudioDMAChannelStateMachine::ADMACOPER_ProcessMoreTransfers) == kIOReturnSuccess`
- `AudioDMAChannelSharedResourceManager::AudioDMAChannelSharedResourceManager(const char *, uint32_t, uint32_t, uint32_t, uint32_t)`
- `site.AudioDMAChannelSharedResourceManager`
- `processChannelOperation( AudioDMAChannelStateMachine::ADMACOPER_Finish) == kIOReturnSuccess`
- `_admacRxChannels[channelIndex]->gatePower( AudioDMAChannel::kAudioDMAChannelPowerStateAvailable, softTransition) == kIOReturnSuccess`
