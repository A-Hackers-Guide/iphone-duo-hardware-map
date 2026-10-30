# `MTL4AccelerationStructureMotionCurveGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureGeometryDescriptor`
- 14 instance variables, 14 properties, 34 instance methods, 0 class methods

## Instance variables

```
Q _controlPointCount;
Q _controlPointStride;
Q _controlPointFormat;
Q _radiusFormat;
Q _radiusStride;
Q _indexType;
Q _segmentCount;
Q _segmentControlPointCount;
q _curveBasis;
q _curveType;
q _curveEndCaps;
{MTL4BufferRange="bufferAddress"Q"length"Q} _controlPointBuffers;
{MTL4BufferRange="bufferAddress"Q"length"Q} _radiusBuffers;
{MTL4BufferRange="bufferAddress"Q"length"Q} _indexBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_controlPointBuffers) controlPointBuffers;
@property (TQ,N,V_controlPointCount) controlPointCount;
@property (TQ,N,V_controlPointStride) controlPointStride;
@property (TQ,N,V_controlPointFormat) controlPointFormat;
@property (T{MTL4BufferRange=QQ},N,V_radiusBuffers) radiusBuffers;
@property (TQ,N,V_radiusFormat) radiusFormat;
@property (TQ,N,V_radiusStride) radiusStride;
@property (T{MTL4BufferRange=QQ},N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_segmentCount) segmentCount;
@property (TQ,N,V_segmentControlPointCount) segmentControlPointCount;
@property (Tq,N,V_curveType) curveType;
@property (Tq,N,V_curveBasis) curveBasis;
@property (Tq,N,V_curveEndCaps) curveEndCaps;
```

## Instance methods

```
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor indexType];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor segmentCount];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor init];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setIndexType:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor dealloc];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor type];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor hash];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setSegmentCount:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setIndexBuffer:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor controlPointBuffers];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor controlPointCount];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor controlPointFormat];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor controlPointStride];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor curveBasis];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor curveEndCaps];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor curveType];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor indexBuffer];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor radiusBuffers];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor radiusFormat];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor radiusStride];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor segmentControlPointCount];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setControlPointBuffers:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setControlPointCount:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setControlPointFormat:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setControlPointStride:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setCurveBasis:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setCurveEndCaps:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setCurveType:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setRadiusBuffers:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setRadiusFormat:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setRadiusStride:];
-[MTL4AccelerationStructureMotionCurveGeometryDescriptor setSegmentControlPointCount:];
```
