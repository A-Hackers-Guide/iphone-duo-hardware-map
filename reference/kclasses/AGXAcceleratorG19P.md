# `AGXAcceleratorG19P`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x1d198` (119,192 bytes)
- Metaclass: `0xfffffe000b92aef8`; metaclass vtable `0xfffffe0007f79ca0`; class vtable `0xfffffe0007f78d48`
- Registration (init): `0xfffffe00085c1128`
- Superclasses: [`AGX·PI_400·P·A0·AcceleratorP`](AGX_PI_400_P_A0_AcceleratorP.md) → [`AGX·PI_400·P·A0·Accelerator`](AGX_PI_400_P_A0_Accelerator.md) → [`AGXFamilyAccelerator`](AGXFamilyAccelerator.md) → [`AGXAccelerator`](AGXAccelerator.md) → [`IOGPU`](IOGPU.md) → [`IOAcceleratorES`](IOAcceleratorES.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AGXG19P` in [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['gpu,t8160', 'gpu,t8015', 'gpu,t8027', 'gpu,t8030', 'gpu,t8103', 'gpu,t8122']`, `IOMatchCategory` = `IOAcceleratorES`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) on `gpu,t8160`

## Strings in its kext that name it (2)

- `site.AGXAcceleratorG19P`
- `AGXAcceleratorG19P`
