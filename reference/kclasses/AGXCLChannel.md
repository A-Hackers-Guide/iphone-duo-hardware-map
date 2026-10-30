# `AGXCLChannel`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b929f18`; metaclass vtable `0xfffffe0007f6f7f8` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe0008555800`
- Superclasses: [`AGXChannel`](AGXChannel.md) → [`IOGPUChannel`](IOGPUChannel.md)

## Direct subclasses (1; 3 in total)

- [`AGXCLChannelSKSM`](AGXCLChannelSKSM.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (11)

- `AGXCLChannel`
- `AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: priority_type out of bounds (%u)\n`
- `AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: event_flag_idx out of bounds (priority_type=%u, context_id=%u)\n`
- `AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: context_id is out of range (%u)\n`
- `virtual void AGXCLChannelSKSM::submitBuffer(IOGPUCommandDescriptor *)`
- `site.AGXCLChannelSKSMG19P`
- `AGXCLChannelSKSMG19P`
- `site.AGXCLChannel`
- `site.AGXCLChannelSKSM`
- `AGXk: %s:%d:%s: !!! AGXCLChannelSKSM::submitBuffer: context_id is negative (%d)\n`
- `AGXCLChannelSKSM`
