# `MTLToolsAccelerationStructure`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsResource`
- Protocols: `MTLAccelerationStructureSPI`
- 1 instance variables, 22 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MTLToolsBuffer" _toolsBuffer;
```

## Properties

```
@property (TQ,R,N) uniqueIdentifier;
@property (TQ,R,N) accelerationStructureUniqueIdentifier;
@property (T@"<MTLBuffer>",R,N) buffer;
@property (TQ,R,N) bufferOffset;
@property (T@"MTLAccelerationStructureDescriptor",?,&,N) descriptor;
@property (TQ,R,N) resourceIndex;
@property (TQ,R) gpuHandle;
@property (TQ,R,N) size;
@property (T{MTLResourceID=Q},R) gpuResourceID;
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
-[MTLToolsAccelerationStructure buffer];
-[MTLToolsAccelerationStructure resourceIndex];
-[MTLToolsAccelerationStructure setDescriptor:];
-[MTLToolsAccelerationStructure descriptor];
-[MTLToolsAccelerationStructure dealloc];
-[MTLToolsAccelerationStructure uniqueIdentifier];
-[MTLToolsAccelerationStructure size];
-[MTLToolsAccelerationStructure gpuHandle];
-[MTLToolsAccelerationStructure bufferOffset];
-[MTLToolsAccelerationStructure gpuResourceID];
-[MTLToolsAccelerationStructure accelerationStructureUniqueIdentifier];
-[MTLToolsAccelerationStructure initWithBaseObject:parent:];
-[MTLToolsAccelerationStructure initWithBaseObject:parent:heap:];
```
