# `MTLAccelerationStructureCommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLCommandEncoder`
- 0 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance methods

```
-[MTLAccelerationStructureCommandEncoder waitForFence:];
-[MTLAccelerationStructureCommandEncoder useResources:count:usage:];
-[MTLAccelerationStructureCommandEncoder useResource:usage:];
-[MTLAccelerationStructureCommandEncoder updateFence:];
-[MTLAccelerationStructureCommandEncoder useHeap:];
-[MTLAccelerationStructureCommandEncoder useHeaps:count:];
-[MTLAccelerationStructureCommandEncoder sampleCountersInBuffer:atSampleIndex:withBarrier:];
-[MTLAccelerationStructureCommandEncoder buildAccelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:];
-[MTLAccelerationStructureCommandEncoder copyAccelerationStructure:toAccelerationStructure:];
-[MTLAccelerationStructureCommandEncoder copyAndCompactAccelerationStructure:toAccelerationStructure:];
-[MTLAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:];
-[MTLAccelerationStructureCommandEncoder refitAccelerationStructure:descriptor:destination:scratchBuffer:scratchBufferOffset:options:];
-[MTLAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:];
-[MTLAccelerationStructureCommandEncoder writeCompactedAccelerationStructureSize:toBuffer:offset:sizeDataType:];
```
