# `MTLAccelerationStructureCurveGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 17 instance variables, 18 properties, 42 instance methods, 1 class methods

## Instance variables

```
@"<MTLBuffer>" _controlPointBuffer;
Q _controlPointBufferOffset;
Q _controlPointCount;
Q _controlPointStride;
Q _controlPointFormat;
@"<MTLBuffer>" _radiusBuffer;
Q _radiusBufferOffset;
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
@property (T@"<MTLBuffer>",&,N,V_controlPointBuffer) controlPointBuffer;
@property (TQ,N,V_controlPointBufferOffset) controlPointBufferOffset;
@property (TQ,N,V_controlPointCount) controlPointCount;
@property (TQ,N,V_controlPointStride) controlPointStride;
@property (TQ,N,V_controlPointFormat) controlPointFormat;
@property (T@"<MTLBuffer>",&,N,V_radiusBuffer) radiusBuffer;
@property (TQ,N,V_radiusBufferOffset) radiusBufferOffset;
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
+[MTLAccelerationStructureCurveGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureCurveGeometryDescriptor indexType];
-[MTLAccelerationStructureCurveGeometryDescriptor segmentCount];
-[MTLAccelerationStructureCurveGeometryDescriptor init];
-[MTLAccelerationStructureCurveGeometryDescriptor setIndexType:];
-[MTLAccelerationStructureCurveGeometryDescriptor dealloc];
-[MTLAccelerationStructureCurveGeometryDescriptor type];
-[MTLAccelerationStructureCurveGeometryDescriptor hash];
-[MTLAccelerationStructureCurveGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureCurveGeometryDescriptor setSegmentCount:];
-[MTLAccelerationStructureCurveGeometryDescriptor isEqual:];
-[MTLAccelerationStructureCurveGeometryDescriptor setIndexBuffer:];
-[MTLAccelerationStructureCurveGeometryDescriptor endCaps];
-[MTLAccelerationStructureCurveGeometryDescriptor controlPointBuffer];
-[MTLAccelerationStructureCurveGeometryDescriptor controlPointBufferOffset];
-[MTLAccelerationStructureCurveGeometryDescriptor controlPointCount];
-[MTLAccelerationStructureCurveGeometryDescriptor controlPointFormat];
-[MTLAccelerationStructureCurveGeometryDescriptor controlPointStride];
-[MTLAccelerationStructureCurveGeometryDescriptor curveBasis];
-[MTLAccelerationStructureCurveGeometryDescriptor curveEndCaps];
-[MTLAccelerationStructureCurveGeometryDescriptor curveType];
-[MTLAccelerationStructureCurveGeometryDescriptor indexBuffer];
-[MTLAccelerationStructureCurveGeometryDescriptor indexBufferOffset];
-[MTLAccelerationStructureCurveGeometryDescriptor radiusBuffer];
-[MTLAccelerationStructureCurveGeometryDescriptor radiusBufferOffset];
-[MTLAccelerationStructureCurveGeometryDescriptor radiusFormat];
-[MTLAccelerationStructureCurveGeometryDescriptor radiusStride];
-[MTLAccelerationStructureCurveGeometryDescriptor segmentControlPointCount];
-[MTLAccelerationStructureCurveGeometryDescriptor setControlPointBuffer:];
-[MTLAccelerationStructureCurveGeometryDescriptor setControlPointBufferOffset:];
-[MTLAccelerationStructureCurveGeometryDescriptor setControlPointCount:];
-[MTLAccelerationStructureCurveGeometryDescriptor setControlPointFormat:];
-[MTLAccelerationStructureCurveGeometryDescriptor setControlPointStride:];
-[MTLAccelerationStructureCurveGeometryDescriptor setCurveBasis:];
-[MTLAccelerationStructureCurveGeometryDescriptor setCurveEndCaps:];
-[MTLAccelerationStructureCurveGeometryDescriptor setCurveType:];
-[MTLAccelerationStructureCurveGeometryDescriptor setEndCaps:];
-[MTLAccelerationStructureCurveGeometryDescriptor setIndexBufferOffset:];
-[MTLAccelerationStructureCurveGeometryDescriptor setRadiusBuffer:];
-[MTLAccelerationStructureCurveGeometryDescriptor setRadiusBufferOffset:];
-[MTLAccelerationStructureCurveGeometryDescriptor setRadiusFormat:];
-[MTLAccelerationStructureCurveGeometryDescriptor setRadiusStride:];
-[MTLAccelerationStructureCurveGeometryDescriptor setSegmentControlPointCount:];
```
