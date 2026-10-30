# `IOGPUMetal4CommandAllocator`

- Image: [`/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`](../userland/System__Library__PrivateFrameworks__IOGPU.framework__IOGPU.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandAllocator`
- 7 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
{commandBufferStorageBusyQueue="tqh_first"^{IOGPUMetalCommandBufferStorage}"tqh_last"^^{IOGPUMetalCommandBufferStorage}} _busyQueue;
i _busyQueueCount;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{?="segmentListShmemPool"@"IOGPUMetalDeviceShmemPool""kernelCommandShmemPool"@"IOGPUMetalDeviceShmemPool""sidebandPool"@"IOGPUMetalDeviceShmemPool""hwResourcePools"^@"hwResourcePoolCount"I"akResourceListPool"@"MTLResourceListPool""akPrivateResourceListPool"@"MTLResourceListPool""debugBufferShmemPool"@"IOGPUMetalDeviceShmemPool"} _storageCreateParams;
^{IOGPUMetalCommandBufferStoragePool={gpuStorageQueue=^{IOGPUMetalCommandBufferStorage}^^{IOGPUMetalCommandBufferStorage}}{os_unfair_lock_s=I}iii@^{?}} _commandBufferStoragePool;
I _generation;
B _aliasToDevice;
```

## Instance methods

```
-[IOGPUMetal4CommandAllocator setHwResourcePool:count:];
-[IOGPUMetal4CommandAllocator setCurrentCommandEncoder:];
-[IOGPUMetal4CommandAllocator initWithDevice:];
-[IOGPUMetal4CommandAllocator initWithDevice:descriptor:];
-[IOGPUMetal4CommandAllocator allocatedSize];
-[IOGPUMetal4CommandAllocator dealloc];
-[IOGPUMetal4CommandAllocator reset];
-[IOGPUMetal4CommandAllocator getCommandBufferStorage:retainReferences:generation:];
-[IOGPUMetal4CommandAllocator initAllocatorWithDevice:];
-[IOGPUMetal4CommandAllocator initWithDeviceAndAliasToDevicePools:];
-[IOGPUMetal4CommandAllocator returnCommandBufferStorage:commandAllocatorGeneration:];
```
