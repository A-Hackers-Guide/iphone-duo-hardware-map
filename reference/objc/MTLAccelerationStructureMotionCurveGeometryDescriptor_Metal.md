# `MTLAccelerationStructureMotionCurveGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 15 instance variables, 16 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _controlPointBuffers;
Q _controlPointCount;
Q _controlPointStride;
Q _controlPointFormat;
@"NSArray" _radiusBuffers;
Q _radiusFormat;
Q _radiusStride;
@"<MTLBuffer>" _indexBuffer;
Q _indexBufferOffset;
Q _indexType;
Q _segmentCount;
Q _segmentControlPointCount;
q _curveBasis;
q _curveType;
q _endCaps;
```

## Properties

```
@property (Tq,N) endCaps;
@property (T@"NSArray",C,N,V_controlPointBuffers) controlPointBuffers;
@property (TQ,N,V_controlPointCount) controlPointCount;
@property (TQ,N,V_controlPointStride) controlPointStride;
@property (TQ,N,V_controlPointFormat) controlPointFormat;
@property (T@"NSArray",C,N,V_radiusBuffers) radiusBuffers;
@property (TQ,N,V_radiusFormat) radiusFormat;
@property (TQ,N,V_radiusStride) radiusStride;
@property (T@"<MTLBuffer>",&,N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexBufferOffset) indexBufferOffset;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_segmentCount) segmentCount;
@property (TQ,N,V_segmentControlPointCount) segmentControlPointCount;
@property (Tq,N,V_curveType) curveType;
@property (Tq,N,V_curveBasis) curveBasis;
@property (Tq,N,V_endCaps) curveEndCaps;
```

## Class methods

```
+[MTLAccelerationStructureMotionCurveGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureMotionCurveGeometryDescriptor indexType];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor segmentCount];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor init];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setIndexType:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor dealloc];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor type];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor hash];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setSegmentCount:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor isEqual:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setIndexBuffer:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor endCaps];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor controlPointBuffers];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor controlPointCount];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor controlPointFormat];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor controlPointStride];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor curveBasis];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor curveEndCaps];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor curveType];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor indexBuffer];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor indexBufferOffset];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor radiusBuffers];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor radiusFormat];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor radiusStride];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor segmentControlPointCount];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setControlPointBuffers:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setControlPointCount:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setControlPointFormat:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setControlPointStride:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setCurveBasis:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setCurveEndCaps:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setCurveType:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setEndCaps:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setIndexBufferOffset:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setRadiusBuffers:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setRadiusFormat:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setRadiusStride:];
-[MTLAccelerationStructureMotionCurveGeometryDescriptor setSegmentControlPointCount:];
```
