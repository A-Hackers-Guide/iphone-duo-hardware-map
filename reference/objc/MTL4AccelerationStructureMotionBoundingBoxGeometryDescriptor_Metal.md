# `MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureGeometryDescriptor`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _boundingBoxCount;
Q _boundingBoxStride;
{MTL4BufferRange="bufferAddress"Q"length"Q} _boundingBoxBuffers;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_boundingBoxBuffers) boundingBoxBuffers;
@property (TQ,N,V_boundingBoxStride) boundingBoxStride;
@property (TQ,N,V_boundingBoxCount) boundingBoxCount;
```

## Instance methods

```
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor init];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor dealloc];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor type];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor hash];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxBuffers];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxCount];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxStride];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxBuffers:];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxCount:];
-[MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxStride:];
```
