# `AppleSPUSphereDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPUSphere`](../kexts/com.apple.driver.AppleSPUSphere.md)
- Object size: `0x270` (624 bytes)
- Metaclass: `0xfffffe000b99e0a0`; metaclass vtable `0xfffffe0008228e08`; class vtable `0xfffffe00082288b0`
- Registration (init): `0xfffffe00097210f8`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUSphereDriver` in [`com.apple.driver.AppleSPUSphere`](../kexts/com.apple.driver.AppleSPUSphere.md): `IOProviderClass` = `AppleSPUAppInterface`, `IONameMatch` = `['AOP_spherecontrol']`, `IOMatchCategory` = `AppleSPUSphereDriver`

## Strings in its kext that name it (8)

- `AppleSPUSphereDriver setEnable(%d) for %s\n`
- `AppleSPUSphereDriver:setData[0x%x] isp-ext-swgen-reg_rx, int_num=0x%x \n`
- `AppleSPUSphereDriver:setData[0x%x] kSpuPropertySphereEndpointConfiguration -> 0x%x\n`
- `AppleSPUSphereDriver`
- `AppleSPUSphereDriver:setData[0x%x] aop-isp-buffer, address=0x%llx, size=0x%x\n`
- `site.AppleSPUSphereDriver`
- `AppleSPUSphereDriver:setData[0x%x] isp-aop-buffer, address=0x%llx, size=0x%x\n`
- `AppleSPUSphereDriver:setData[0x%x] isp-ext-swgen-reg, reg=0x%llx, value=0x%x\n`
