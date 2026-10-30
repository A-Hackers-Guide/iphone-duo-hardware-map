# `AppleARMDMAAudioDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.AppleARMIISAudio`](../kexts/com.apple.iokit.AppleARMIISAudio.md)
- Object size: `0x1c8` (456 bytes)
- Metaclass: `0xfffffe000b9335b0`; metaclass vtable `0xfffffe0007fafe60`; class vtable `0xfffffe0007faf700`
- Registration (init): `0xfffffe00086d3210`
- Superclasses: [`IOAudio2Device`](IOAudio2Device.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 6 in total)

- [`AppleARMIISAudioDevice`](AppleARMIISAudioDevice.md) — `com.apple.iokit.AppleARMIISAudio`

## Strings in its kext that name it (29)

- `%s: AppleARMDMAAudioDevice::startDMAInternal:%d restart=%d. startTransport returned ret=kIOReturnNotReady but return kIOReturnSuccess.\n\n`
- `%s AppleARMDMAAudioDevice::%s:%d start failed.\n`
- `%s: AppleARMDMAAudioDevice::startIOEngineInternal could not start DMA: %s\n`
- `\"AppleARMDMAAudioDevice::createStreamFormat dataFormat=%4s\" @%s:%d`
- `%s: AppleARMDMAAudioDevice::startDataTransfers failed. bufferIndex=%u buffer=%p direction=%d byteCount=%u theAnswer=%s(%#x).\n\n`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioSampleRate failed. sampleRate=%lld err=%s(%#x)\n`
- `%s: AppleARMDMAAudioDevice::startDMAInternal failed. restart=%d ret=%s(%#x)\n`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionOut byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n\n`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioStreamFormats failed.\n`
- `%s AppleARMDMAAudioDevice::%s:%d startInternal failed.\n`
- `AppleARMDMAAudioDevice`
- `site.AppleARMDMAAudioDevice`
- `%s: AppleARMDMAAudioDevice::restartTransport failed. ret=%s(%#x)\n\n`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionIn byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n\n`
- `%s: AppleARMDMAAudioDevice::transferData:%d failed. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n\n`
- `site.AppleARMDMAAudioDevice::OverrideConfigs`
- `AppleARMDMAAudioDevice.cpp`
- `%s AppleARMDMAAudioDevice::%s:%d startInternal failed.`
- `%s: AppleARMDMAAudioDevice::startDMAInternal failed. restart=%d ret=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionIn byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n`
- `%s: AppleARMDMAAudioDevice::startIOEngineInternal could not start DMA: %s`
- `%s: AppleARMDMAAudioDevice::startDMAInternal:%d restart=%d. startTransport returned ret=kIOReturnNotReady but return kIOReturnSuccess.\n`
- `%s AppleARMDMAAudioDevice::%s:%d start failed.`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioSampleRate failed. sampleRate=%lld err=%s(%#x)`
- `%s: AppleARMDMAAudioDevice::sendBuffer:%d failed. kIODirectionOut byteCount=%llu startBytes=%llu theAnswer=%s(%#x).\n`
- `%s: AppleARMDMAAudioDevice::startDataTransfers failed. bufferIndex=%u buffer=%p direction=%d byteCount=%u theAnswer=%s(%#x).\n`
- `%s: AppleARMDMAAudioDevice::transferData:%d failed. direction=%#x byteCount=%lld startByteCount=%lld theAnswer=%s(%#x).\n`
- `%s AppleARMDMAAudioDevice::%s:%d setAudioStreamFormats failed.`
- `%s: AppleARMDMAAudioDevice::restartTransport failed. ret=%s(%#x)\n`
