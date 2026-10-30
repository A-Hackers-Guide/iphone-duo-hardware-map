# `AppleSMCKeysEndpoint`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0x658` (1,624 bytes)
- Metaclass: `0xfffffe000b99b3e0`; metaclass vtable `0xfffffe00081fe6d0`; class vtable `0xfffffe00081fe078`
- Registration (init): `0xfffffe0009673e9c`
- Superclasses: [`AppleSMC`](AppleSMC.md) → [`AppleSMCFamily`](AppleSMCFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCKeysEndpoint` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `RTBuddyEndpointService`, `IONameMatch` = `SMCEndpoint1`, `IOMatchCategory` = `AppleSMCKeysEndpoint`

## Strings in its kext that name it (16)

- `SMCResult AppleSMCKeysEndpoint::_sendKeyMsgAndWaitForResponse(ApcKeyMsg *)`
- `AppleSMCKeysEndpoint::%s(): NTAP result  (%x)]\n`
- `/Library/Caches/com.apple.xbs/54E255AF-DD90-4507-9BE8-379A89574EFC/TemporaryDirectory.eUdRVs/Sources/AppleSMC/AppleSMCKeysEndpoint.cpp`
- `AppleSMCKeysEndpoint::%s(): newState=%ld  _activeKeyCommand=%x ignored\n`
- `SMCResult AppleSMCKeysEndpoint::_sendKeyMsgAndPollForResponse(ApcKeyMsg *)`
- `AppleSMCKeysEndpoint::%s(): now quiesced MBSE result (%x)\n`
- `AppleSMCKeysEndpoint::%s(): newState=%d _activeKeyCommand=%x notifyMBSEMessage=%x\n`
- `void AppleSMCKeysEndpoint::_keyEndpointHandler(void *, void *)`
- `site.AppleSMCKeysEndpoint`
- `AppleSMCKeysEndpoint`
- `AppleSMCKeysEndpoint::%s(): unquiesced\n`
- `Starting AppleSMCKeysEndpoint(%p) - (%s@%s)\n`
- `void *AppleSMCKeysEndpoint::_getSRAMAddressGated()`
- `AppleSMCKeysEndpoint::%s(): MBSE result  (%x)]\n`
- `AppleSMCKeysEndpoint.cpp`
- `AppleSMCKeysEndpoint::%s(): newState=%d _activeKeyCommand=%x\n`
