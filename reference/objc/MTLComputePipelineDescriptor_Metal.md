# `MTLComputePipelineDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 21 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _insertLibraries;
```

## Properties

```
@property (TB,D,N) forceResourceIndex;
@property (TQ,D,N) resourceIndex;
@property (TQ,D,N) globalConstantsTag;
@property (T@"NSString",C,D,N) label;
@property (T@"<MTLFunction>",&,D,N) computeFunction;
@property (TB,D,N) threadGroupSizeIsMultipleOfThreadExecutionWidth;
@property (TQ,D,N) maxTotalThreadsPerThreadgroup;
@property (T@"MTLStageInputOutputDescriptor",C,D,N) stageInputDescriptor;
@property (T@"MTLPipelineBufferDescriptorArray",R,D) buffers;
@property (TB,D,N) supportIndirectCommandBuffers;
@property (T@"NSArray",C,N,V_insertLibraries) insertLibraries;
@property (T@"NSArray",C,D,N) preloadedLibraries;
@property (T@"NSArray",C,D,N) binaryArchives;
@property (T@"MTLLinkedFunctions",C,D,N) linkedFunctions;
@property (TB,D,N) supportAddingBinaryFunctions;
@property (TQ,D,N) maxCallStackDepth;
@property (Tq,D,N) shaderValidation;
@property (T{?=QQQ},D,N) requiredThreadsPerThreadgroup;
@property (Tq,D,N) forwardProgressUsage;
@property (Tq,D,N) contentionRelief;
@property (TB,D,N) optimizeForPersistentKernel;
```

## Class methods

```
+[MTLComputePipelineDescriptor allocWithZone:];
+[MTLComputePipelineDescriptor alloc];
```

## Instance methods

```
-[MTLComputePipelineDescriptor reset];
-[MTLComputePipelineDescriptor setInsertLibraries:];
-[MTLComputePipelineDescriptor insertLibraries];
-[MTLComputePipelineDescriptor copyWithZone:];
```
