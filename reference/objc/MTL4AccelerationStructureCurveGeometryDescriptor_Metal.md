# `MTL4AccelerationStructureCurveGeometryDescriptor`

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
{MTL4BufferRange="bufferAddress"Q"length"Q} _controlPointBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _radiusBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _indexBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_controlPointBuffer) controlPointBuffer;
@property (TQ,N,V_controlPointCount) controlPointCount;
@property (TQ,N,V_controlPointStride) controlPointStride;
@property (TQ,N,V_controlPointFormat) controlPointFormat;
@property (T{MTL4BufferRange=QQ},N,V_radiusBuffer) radiusBuffer;
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
-[MTL4AccelerationStructureCurveGeometryDescriptor indexType];
-[MTL4AccelerationStructureCurveGeometryDescriptor segmentCount];
-[MTL4AccelerationStructureCurveGeometryDescriptor init];
-[MTL4AccelerationStructureCurveGeometryDescriptor setIndexType:];
-[MTL4AccelerationStructureCurveGeometryDescriptor dealloc];
-[MTL4AccelerationStructureCurveGeometryDescriptor type];
-[MTL4AccelerationStructureCurveGeometryDescriptor hash];
-[MTL4AccelerationStructureCurveGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setSegmentCount:];
-[MTL4AccelerationStructureCurveGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setIndexBuffer:];
-[MTL4AccelerationStructureCurveGeometryDescriptor controlPointBuffer];
-[MTL4AccelerationStructureCurveGeometryDescriptor controlPointCount];
-[MTL4AccelerationStructureCurveGeometryDescriptor controlPointFormat];
-[MTL4AccelerationStructureCurveGeometryDescriptor controlPointStride];
-[MTL4AccelerationStructureCurveGeometryDescriptor curveBasis];
-[MTL4AccelerationStructureCurveGeometryDescriptor curveEndCaps];
-[MTL4AccelerationStructureCurveGeometryDescriptor curveType];
-[MTL4AccelerationStructureCurveGeometryDescriptor indexBuffer];
-[MTL4AccelerationStructureCurveGeometryDescriptor radiusBuffer];
-[MTL4AccelerationStructureCurveGeometryDescriptor radiusFormat];
-[MTL4AccelerationStructureCurveGeometryDescriptor radiusStride];
-[MTL4AccelerationStructureCurveGeometryDescriptor segmentControlPointCount];
-[MTL4AccelerationStructureCurveGeometryDescriptor setControlPointBuffer:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setControlPointCount:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setControlPointFormat:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setControlPointStride:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setCurveBasis:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setCurveEndCaps:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setCurveType:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setRadiusBuffer:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setRadiusFormat:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setRadiusStride:];
-[MTL4AccelerationStructureCurveGeometryDescriptor setSegmentControlPointCount:];
```
