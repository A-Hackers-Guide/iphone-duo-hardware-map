# `MTLAccelerationStructureBoundingBoxGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"<MTLBuffer>" _boundingBoxBuffer;
Q _boundingBoxBufferOffset;
Q _boundingBoxStride;
Q _boundingBoxCount;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N,V_boundingBoxBuffer) boundingBoxBuffer;
@property (TQ,N,V_boundingBoxBufferOffset) boundingBoxBufferOffset;
@property (TQ,N,V_boundingBoxStride) boundingBoxStride;
@property (TQ,N,V_boundingBoxCount) boundingBoxCount;
```

## Class methods

```
+[MTLAccelerationStructureBoundingBoxGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor init];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor dealloc];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor type];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor hash];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor isEqual:];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor boundingBoxBuffer];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor boundingBoxBufferOffset];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor boundingBoxCount];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor boundingBoxStride];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxBuffer:];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxBufferOffset:];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxCount:];
-[MTLAccelerationStructureBoundingBoxGeometryDescriptor setBoundingBoxStride:];
```
