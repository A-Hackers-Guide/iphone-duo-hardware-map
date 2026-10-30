# `AGXG19FamilyMLContext`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetal4MachineLearningCommandEncoder`
- 2 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _impl;
@"AGXG19FamilyCommandAllocator_mtlnext" _allocator;
```

## Instance methods

```
-[AGXG19FamilyMLContext endEncoding];
-[AGXG19FamilyMLContext dealloc];
-[AGXG19FamilyMLContext updateFence:afterEncoderStages:];
-[AGXG19FamilyMLContext barrierAfterEncoderStages:beforeEncoderStages:options:];
-[AGXG19FamilyMLContext barrierAfterQueueStages:beforeStages:options:];
-[AGXG19FamilyMLContext barrierAfterStages:beforeQueueStages:options:];
-[AGXG19FamilyMLContext endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:];
-[AGXG19FamilyMLContext initWithCommandBuffer:allocator:];
-[AGXG19FamilyMLContext waitForFence:beforeEncoderStages:];
-[AGXG19FamilyMLContext destroyImpl];
```
