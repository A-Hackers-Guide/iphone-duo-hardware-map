# `AppleS8000AESAccelerator`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleS8000AES`](../kexts/com.apple.driver.AppleS8000AES.md)
- Object size: `0xa00` (2,560 bytes)
- Metaclass: `0xfffffe000b9941d8`; metaclass vtable `0xfffffe00081c67d0`; class vtable `0xfffffe00081c6200`
- Registration (init): `0xfffffe00094847dc`
- Superclasses: [`IOAESAccelerator`](IOAESAccelerator.md) → [`IOCryptoAccelerator`](IOCryptoAccelerator.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleS8000AES` in [`com.apple.driver.AppleS8000AES`](../kexts/com.apple.driver.AppleS8000AES.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `aes,s8000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/aes`](../devicetree/root__arm-io__aes.md) on `aes,s8000`

## Strings in its kext that name it (38)

- `AppleS8000AESAccelerator`
- `\"AppleS8000AESAccelerator: AppleS8000AESAccelerator failed to register with IOAESAccelerator\" @%s:%d`
- `%s: WARNING: AppleS8000AESAccelerator::bad descrambler configuration\n`
- `IOReturn AppleS8000AESAccelerator::_configureAES(IOAESAcceleratorCommand *, UInt32)`
- `void AppleS8000AESAccelerator::_completeAES()`
- `bool AppleS8000AESAccelerator::_isKeyDisabled(UInt32)`
- `UInt32 AppleS8000AESAccelerator::_keySelectionForHandle(UInt32)`
- `%s: WARNING: AppleS8000AESAccelerator::attempt to disable unsuported key %u\n`
- `%s: WARNING: AppleS8000AESAccelerator::bad configuration for IOAESOperationH16Scrambler operation\n`
- `UInt32 AppleS8000AESAccelerator::_key_size(UInt8)`
- `virtual void AppleS8000AESAccelerator::stop(IOService *)`
- `%s: WARNING: AppleS8000AESAccelerator::attempt to look up unsuported key %u\n`
- `void AppleS8000AESAccelerator::_push_command(void *, UInt32)`
- `\"AppleS8000AESAccelerator::_enableAES: DPA has not been seeded!\" @%s:%d`
- `\"AppleS8000AESAccelerator::performAESQuantum: Unknown Operation %d\" @%s:%d`
- `void AppleS8000AESAccelerator::_interruptOccurred(IOInterruptEventSource *, int)`
- `virtual IOReturn AppleS8000AESAccelerator::performAESQuantum(IOAESAcceleratorCommand *)`
- `bool AppleS8000AESAccelerator::_push_command_key(UInt32, UInt32, UInt8 *, UInt8 *, bool)`
- `virtual bool AppleS8000AESAccelerator::start(IOService *)`
- `%s: WARNING: AppleS8000AESAccelerator::operation with no key data\n`
- `%s: WARNING: AppleS8000AESAccelerator::bad wrapped key configuration\n`
- `AppleS8000AESAccelerator: WARNING: DPA is not seeded, but not panicking!\n`
- `%s: WARNING: AppleS8000AESAccelerator::unsupported operation %u\n`
- `\"AppleS8000AESAccelerator::Wrapped Key Policy is undefined\" @%s:%d`
- `IOAppleS8000AESAcceleratorCommand`
- `\"AppleS8000AESAccelerator::Powering Down AES Block while Commands still in FIFO.\" @%s:%d`
- `site.AppleS8000AESAccelerator`
- `\"AppleS8000AESAccelerator::_distribute_dkey: DKey distribution failure (aes-version=%u)\" @%s:%d`
- `void AppleS8000AESAccelerator::_enableAES(bool)`
- `%s: WARNING: AppleS8000AESAccelerator::bad IOAESH16Descrambler configuration\n`
- `%s: WARNING: AppleS8000AESAccelerator::unsupported key %u\n`
- `void AppleS8000AESAccelerator::_handleIVBounce(IOAESIV *, UInt16)`
- `virtual void AppleS8000AESAccelerator::disableHardwareKey(UInt32)`
- `bool AppleS8000AESAccelerator::_space_available(UInt32)`
- `site.IOAppleS8000AESAcceleratorCommand`
- `%s: WARNING: AppleS8000AESAccelerator::bad LegacySKG configuration\n`
- `%s: WARNING: AppleS8000AESAccelerator::bad operation for kIOAESAcceleratorKeyHandleScrambledH16 configuration\n`
- `\"AppleS8000AESAccelerator::AES Error: IntStatus 0x%#x\\n\" @%s:%d`
