# `AGXWorkQueue`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x240` (576 bytes)
- Metaclass: `0xfffffe000b92e710`; metaclass vtable `0xfffffe0007f7fd28`; class vtable `0xfffffe0007f7fc08`
- Registration (init): `0xfffffe0008603f20`
- Superclasses: [`IOGPUWorkQueue`](IOGPUWorkQueue.md) → [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (2; 2 in total)

- [`AGX3DWorkQueue`](AGX3DWorkQueue.md) — `com.apple.AGXG19P`
- [`AGXCLWorkQueue`](AGXCLWorkQueue.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (5)

- `virtual void AGXWorkQueue::submitForFenceComplete(AGXIOFenceData *)`
- `void AGXWorkQueue::setPriority(eAGXContextPriorityType, eIOGPUCommandQueueQosLevel)`
- `site.AGXWorkQueue`
- `virtual void AGXWorkQueue::submitCommand(IOGPUCommandDescriptor *)`
- `AGXWorkQueue`
