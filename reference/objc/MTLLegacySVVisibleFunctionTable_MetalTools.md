# `MTLLegacySVVisibleFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsVisibleFunctionTable`
- Protocols: `MTLLegacySVResource`
- 3 instance variables, 21 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _gpuIdentifier;
@"<MTLBuffer>" _handleBuffer;
Q _stage;
```

## Properties

```
@property (T@"<MTLVisibleFunctionTable>",&,D,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLLegacySVVisibleFunctionTable setBuffers:offsets:withRange:];
-[MTLLegacySVVisibleFunctionTable setBuffer:offset:atIndex:];
-[MTLLegacySVVisibleFunctionTable dealloc];
-[MTLLegacySVVisibleFunctionTable gpuAddress];
-[MTLLegacySVVisibleFunctionTable length];
-[MTLLegacySVVisibleFunctionTable bufferAddressAtIndex:];
-[MTLLegacySVVisibleFunctionTable _setupCommon];
-[MTLLegacySVVisibleFunctionTable handleForOffset:];
-[MTLLegacySVVisibleFunctionTable initWithVisibleFunctionTable:descriptor:computePipeline:];
-[MTLLegacySVVisibleFunctionTable initWithVisibleFunctionTable:descriptor:device:];
-[MTLLegacySVVisibleFunctionTable initWithVisibleFunctionTable:descriptor:renderPipeline:stage:];
-[MTLLegacySVVisibleFunctionTable underlyingGPUAddress];
-[MTLLegacySVVisibleFunctionTable useWithComputeEncoder:usage:];
-[MTLLegacySVVisibleFunctionTable useWithRenderEncoder:usage:stages:];
```
