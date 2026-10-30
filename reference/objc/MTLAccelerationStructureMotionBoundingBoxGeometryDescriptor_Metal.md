# `MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 3 instance variables, 3 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _boundingBoxBuffers;
Q _boundingBoxCount;
Q _boundingBoxStride;
```

## Properties

```
@property (T@"NSArray",C,N,V_boundingBoxBuffers) boundingBoxBuffers;
@property (TQ,N,V_boundingBoxStride) boundingBoxStride;
@property (TQ,N,V_boundingBoxCount) boundingBoxCount;
```

## Class methods

```
+[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor init];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor dealloc];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor type];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor hash];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor isEqual:];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxBuffers];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxCount];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor boundingBoxStride];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxBuffers:];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxCount:];
-[MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor setBoundingBoxStride:];
```
