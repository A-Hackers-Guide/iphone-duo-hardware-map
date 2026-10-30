# `MTL4AccelerationStructureBoundingBoxGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureGeometryDescriptor`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _boundingBoxStride;
Q _boundingBoxCount;
{MTL4BufferRange="bufferAddress"Q"length"Q} _boundingBoxBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_boundingBoxBuffer) boundingBoxBuffer;
@property (TQ,N,V_boundingBoxStride) boundingBoxStride;
@property (TQ,N,V_boundingBoxCount) boundingBoxCount;
```

## Instance methods

```
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor init];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor dealloc];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor type];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor hash];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor boundingBoxBuffer];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor boundingBoxCount];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor boundingBoxStride];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxBuffer:];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxCount:];
-[MTL4AccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxStride:];
```
