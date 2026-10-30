# `MTLLegacySVIntersectionFunctionTable`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsIntersectionFunctionTable`
- Protocols: `MTLLegacySVResource`
- 6 instance variables, 21 properties, 19 instance methods, 0 class methods

## Instance variables

```
Q _gpuIdentifier;
Q _functionCount;
@"MTLLegacySVComputePipelineState" _computePipelineState;
@"MTLLegacySVRenderPipelineState" _renderPipelineState;
@"<MTLBuffer>" _handleBuffer;
Q _stage;
```

## Properties

```
@property (T@"<MTLIntersectionFunctionTable>",&,D,N) baseObject;
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
-[MTLLegacySVIntersectionFunctionTable setBuffers:offsets:withRange:];
-[MTLLegacySVIntersectionFunctionTable setVisibleFunctionTables:withBufferRange:];
-[MTLLegacySVIntersectionFunctionTable setBuffer:offset:atIndex:];
-[MTLLegacySVIntersectionFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[MTLLegacySVIntersectionFunctionTable dealloc];
-[MTLLegacySVIntersectionFunctionTable gpuAddress];
-[MTLLegacySVIntersectionFunctionTable setFunction:atIndex:];
-[MTLLegacySVIntersectionFunctionTable length];
-[MTLLegacySVIntersectionFunctionTable bufferAddressAtIndex:];
-[MTLLegacySVIntersectionFunctionTable setFunctions:withRange:];
-[MTLLegacySVIntersectionFunctionTable _initHandleBuffer];
-[MTLLegacySVIntersectionFunctionTable _setupIdentifier];
-[MTLLegacySVIntersectionFunctionTable handleForOffset:];
-[MTLLegacySVIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:];
-[MTLLegacySVIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:computePipelineState:];
-[MTLLegacySVIntersectionFunctionTable initWithIntersectionFunctionTable:device:descriptor:renderPipelineState:stage:];
-[MTLLegacySVIntersectionFunctionTable underlyingGPUAddress];
-[MTLLegacySVIntersectionFunctionTable useWithComputeEncoder:usage:];
-[MTLLegacySVIntersectionFunctionTable useWithRenderEncoder:usage:stages:];
```
