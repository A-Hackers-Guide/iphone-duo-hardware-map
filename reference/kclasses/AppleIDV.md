# `AppleIDV`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleIDV`](../kexts/com.apple.driver.AppleIDV.md)
- Object size: `0x40d8` (16,600 bytes)
- Metaclass: `0xfffffe000b9510b0`; metaclass vtable `0xfffffe0008113068`; class vtable `0xfffffe0008112b10`
- Registration (init): `0xfffffe0009000764`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleIDV` in [`com.apple.driver.AppleIDV`](../kexts/com.apple.driver.AppleIDV.md): `IOProviderClass` = `IOResources`, `IOResourceMatch` = `SEP`, `IOMatchCategory` = `AppleIDV`

## Strings in its kext that name it (10)

- `site.AppleIDVUserClient`
- `AppleIDV: %-30s: error: require failed at %s line %d\n`
- `site.AppleIDV`
- `[AppleIDVUserClient::start] Attached new client connection, provider at %p\n`
- `genericAppleIDVCommand`
- `[AppleIDVUserClient::initWithTask] entering\n`
- `AppleIDVUserClient::%s out_md = %p  out_md_size = %u\n`
- `AppleIDV`
- `AppleIDVUserClient`
- `AppleIDVUserClient::%s in_md = %p out_md = %p  out_md_size = %u\n`
