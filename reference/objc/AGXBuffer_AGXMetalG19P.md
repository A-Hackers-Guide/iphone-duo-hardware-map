# `AGXBuffer`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalBuffer`
- Protocols: `AGXResource`
- 1 instance variables, 1 properties, 34 instance methods, 0 class methods

## Instance variables

```
{BufferResourceInfo=""(?=""{?="isDriverResource"b1"isCreatedFromBytes"b1"isCreatedFromIOSurface"b1"isCreatedFromHeap"b1"internalBufferType"b3"unused"b25}"value"I)} bufferResourceInfo;
```

## Properties

```
@property (T{BufferResourceInfo=(?={?=b1b1b1b1b3b25}I)},N,VbufferResourceInfo) bufferResourceInfo;
```

## Instance methods

```
-[AGXBuffer setBufferResourceInfo:];
-[AGXBuffer initWithDevice:length:options:isSuballocDisabled:resourceInArgs:pinnedGPULocation:];
-[AGXBuffer emitResourceInfoTraceEvent];
-[AGXBuffer initWithDevice:length:alignment:options:isSuballocDisabled:pinnedGPULocation:];
-[AGXBuffer initWithHeap:length:alignment:pointerTag:options:];
-[AGXBuffer emitBufferResourceInfoSignpost:];
-[AGXBuffer initWithDevice:bytes:length:options:deallocator:pinnedGPUAddress:];
-[AGXBuffer backingResource];
-[AGXBuffer initWithHeap:length:options:atOffset:];
-[AGXBuffer initWithDevice:length:alignment:pointerTag:options:isSuballocDisabled:pinnedGPULocation:];
-[AGXBuffer dealloc];
-[AGXBuffer initUntrackedInternalBufferWithDevice:length:options:type:];
-[AGXBuffer initCounterSampleBufferWithDevice:length:options:];
-[AGXBuffer parentGPUAddress];
-[AGXBuffer initInternalBufferWithDevice:length:options:type:];
-[AGXBuffer initWithDevice:length:alignment:pointerTag:options:isSuballocDisabled:resourceInArgs:pinnedGPULocation:];
-[AGXBuffer initWithDevice:length:alignment:options:isSuballocDisabled:resourceInArgs:pinnedGPULocation:];
-[AGXBuffer initUntrackedInternalBufferWithDevice:length:options:];
-[AGXBuffer initWithHeap:length:alignment:options:atOffset:];
-[AGXBuffer initWithDevice:addressRanges:addressRangeCount:length:alignment:options:pinnedGPUAddress:];
-[AGXBuffer initWithDevice:iosurface:pinnedGPUAddress:];
-[AGXBuffer initImplWithHeap:resource:length:atOffset:];
-[AGXBuffer initWithHeap:length:alignment:pointerTag:options:atOffset:];
-[AGXBuffer initWithDevice:bytes:length:alignment:pointerTag:options:deallocator:pinnedGPUAddress:];
-[AGXBuffer initInternalBufferWithDevice:length:options:];
-[AGXBuffer initWithHeap:length:options:];
-[AGXBuffer initResourceGroupUsage];
-[AGXBuffer initWithDevice:bytes:length:alignment:options:deallocator:pinnedGPUAddress:];
-[AGXBuffer bufferResourceInfo];
-[AGXBuffer parentGPUSize];
-[AGXBuffer initWithDevice:length:options:isSuballocDisabled:pinnedGPULocation:];
-[AGXBuffer initImplWithHeap:resource:length:pointerTag:atOffset:];
-[AGXBuffer initWithHeap:length:alignment:options:];
-[AGXBuffer initWithDevice:length:alignment:options:pointerTag:pinnedGPUAddress:placementSparsePageSize:];
```
