# `AppleAuth`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b93a7e8`; metaclass vtable `0xfffffe000801e8e0`; class vtable `0xfffffe000801e368`
- Registration (init): `0xfffffe0008ab2af4`
- Superclasses: [`AppleAuthCPRelayInterface`](AppleAuthCPRelayInterface.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (24)

- `AppleAuth::authInit - ERROR: Couldn't add command gate to work loop\n`
- `AppleAuth::authSendData - ERROR: Unknown command 0x%02x\n`
- `AppleAuth::authInit - ERROR: Could not create AppleAuth work-loop\n`
- `AppleAuth::authThread - ERROR: Invalid command gate\n`
- `AppleAuth::authInit - ERROR: Failed to allocate thread call\n`
- `AppleAuth::authSendData - ERROR: Not initialized (no owner)\n`
- `AppleAuth::authSendData - ERROR: SetTrustStatus data length mismatch (expected %u, got %u)\n`
- `AppleAuth`
- `AppleAuth::authThreadGated - GetInfo: ERROR: RearCameraAuthICUID not found in registry\n`
- `AppleAuth::authSendData - ERROR: SetTrustStatus requires data\n`
- `AppleCamera::startAuth - ERROR: Unable to add AppleAuth to client list\n`
- `AppleAuth::authSendData - ERROR: Failed to allocate command structure\n`
- `AppleAuth::withAuthChip - ERROR: Invalid auth chip type\n`
- `AppleAuth::init - ERROR: Could not allocate submit lock\n`
- `AppleAuth::start - ERROR: Provider is not AppleCamera\n`
- `AppleAuth::authThread - GetSignature: ISP not idle (0x%x), skipping\n`
- `AppleAuth::authSendData - ERROR: GetSignature challenge too short (need %u, got %u)\n`
- `AppleAuth::authInit - ERROR: Invalid owner or callback\n`
- `AppleAuth::authInit - ERROR: Couldn't create command gate\n`
- `AppleAuth::authThreadGated - GetSignature: No valid response from ISP\n`
- `site.AppleAuth`
- `AppleAuth::authThreadGated - ERROR: NULL fCameraProvider\n`
- `AppleAuth::authThreadGated - ERROR: NULL cmd parameter\n`
- `AppleAuth::authSendData - ERROR: GetSignature requires challenge data\n`
