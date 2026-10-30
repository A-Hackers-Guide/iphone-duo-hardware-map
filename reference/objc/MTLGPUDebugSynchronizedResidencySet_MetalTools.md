# `MTLGPUDebugSynchronizedResidencySet`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<MTLResidencySet>" _residencySet;
@"<MTLDevice>" _baseDevice;
{shared_mutex="__base_"{__shared_mutex_base="__mut_"{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}}"__gate1_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__gate2_"{condition_variable="__cv_"{_opaque_pthread_cond_t="__sig"q"__opaque"[40c]}}"__state_"I}} _mutex;
```

## Properties

```
@property (TQ,R,N) allocationCount;
@property (TB,R,N,GisValid) valid;
```

## Instance methods

```
-[MTLGPUDebugSynchronizedResidencySet initWithDevice:];
-[MTLGPUDebugSynchronizedResidencySet dealloc];
-[MTLGPUDebugSynchronizedResidencySet isValid];
-[MTLGPUDebugSynchronizedResidencySet allocationCount];
-[MTLGPUDebugSynchronizedResidencySet addAllocationWithLock:];
-[MTLGPUDebugSynchronizedResidencySet bulkModifyWithLock:remove:];
-[MTLGPUDebugSynchronizedResidencySet commitWithLock];
-[MTLGPUDebugSynchronizedResidencySet initWithDevice:allocations:];
-[MTLGPUDebugSynchronizedResidencySet removeAllocationWithLock:];
-[MTLGPUDebugSynchronizedResidencySet requestResidencyWithLock];
-[MTLGPUDebugSynchronizedResidencySet useInCommandBuffer:];
```
