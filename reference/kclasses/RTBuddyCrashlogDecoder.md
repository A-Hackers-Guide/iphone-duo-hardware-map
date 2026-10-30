# `RTBuddyCrashlogDecoder`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000ba23e30`; metaclass vtable `0xfffffe0008496690`; class vtable `0xfffffe0008496600`
- Registration (init): `0xfffffe000a93c338`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (8)

- `RTBuddyCrashlogDecoder.cpp`
- `IOReturn RTBuddyCrashlogDecoder::decodeLog(RTBuddyCrashlogDecodeResult &)`
- `void RTBuddyCrashlogDecoder::writeCrashlog(const char *, va_list)`
- `RTBuddyCrashlogDecoder`
- `OSBoundedPtr<const uint8_t> RTBuddyCrashlogDecoder::_multiCrashlogFindFirstCrash(OSBoundedPtr<const uint8_t>, size_t *)`
- `void RTBuddyCrashlogDecoder::_initDefaultSectionDecoders()`
- `void RTBuddyCrashlogDecoder::writePanicString(const char *, va_list)`
- `site.RTBuddyCrashlogDecoder`
