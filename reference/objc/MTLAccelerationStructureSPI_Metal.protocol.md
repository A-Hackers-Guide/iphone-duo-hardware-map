# `MTLAccelerationStructureSPI` (protocol)

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLAccelerationStructure`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) uniqueIdentifier;
@property (TQ,R,N) accelerationStructureUniqueIdentifier;
@property (T@"<MTLBuffer>",R,N) buffer;
@property (TQ,R,N) bufferOffset;
@property (T@"MTLAccelerationStructureDescriptor",?,&,N) descriptor;
@property (TQ,R,N) resourceIndex;
@property (TQ,R) gpuHandle;
```

## Instance methods

```
-[MTLAccelerationStructureSPI buffer];
-[MTLAccelerationStructureSPI resourceIndex];
-[MTLAccelerationStructureSPI uniqueIdentifier];
-[MTLAccelerationStructureSPI gpuHandle];
-[MTLAccelerationStructureSPI bufferOffset];
-[MTLAccelerationStructureSPI accelerationStructureUniqueIdentifier];
-[MTLAccelerationStructureSPI setDescriptor:];
-[MTLAccelerationStructureSPI descriptor];
```
