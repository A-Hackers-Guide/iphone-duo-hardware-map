# `MTLIOAccelAccelerationStructure`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- Protocols: `MTLAccelerationStructureSPI`
- 4 instance variables, 22 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"MTLIOAccelBuffer<MTLBuffer>" _buffer;
Q _bufferOffset;
Q _resourceIndex;
@"MTLAccelerationStructureDescriptor" _descriptor;
```

## Properties

```
@property (TQ,R,N) uniqueIdentifier;
@property (T@"MTLIOAccelBuffer<MTLBuffer>",R,N) buffer;
@property (TQ,R,N) bufferOffset;
@property (T@"MTLAccelerationStructureDescriptor",&,N,V_descriptor) descriptor;
@property (TQ,R,N,V_resourceIndex) resourceIndex;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R,N) accelerationStructureUniqueIdentifier;
@property (TQ,R) gpuHandle;
@property (TQ,R,N) size;
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
-[MTLIOAccelAccelerationStructure buffer];
-[MTLIOAccelAccelerationStructure resourceIndex];
-[MTLIOAccelAccelerationStructure setDescriptor:];
-[MTLIOAccelAccelerationStructure descriptor];
-[MTLIOAccelAccelerationStructure dealloc];
-[MTLIOAccelAccelerationStructure uniqueIdentifier];
-[MTLIOAccelAccelerationStructure size];
-[MTLIOAccelAccelerationStructure gpuHandle];
-[MTLIOAccelAccelerationStructure bufferOffset];
-[MTLIOAccelAccelerationStructure gpuResourceID];
-[MTLIOAccelAccelerationStructure copyPropertiesFromBuffer:];
-[MTLIOAccelAccelerationStructure initWithBuffer:offset:];
-[MTLIOAccelAccelerationStructure initWithBuffer:offset:resourceIndex:];
```
