# `MTLBVHCurveGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBVHGeometryDescriptor`
- 14 instance variables, 14 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _controlPointBuffers;
Q _controlPointStride;
@"NSArray" _radiusBuffers;
Q _radiusStride;
@"<MTLBuffer>" _indexBuffer;
Q _indexBufferOffset;
Q _indexType;
Q _controlPointFormat;
Q _radiusFormat;
Q _segmentControlPointCount;
q _curveType;
q _curveBasis;
q _curveEndCaps;
Q _controlPointCount;
```

## Properties

```
@property (T@"NSArray",W,N,V_controlPointBuffers) controlPointBuffers;
@property (TQ,N,V_controlPointStride) controlPointStride;
@property (TQ,N,V_controlPointCount) controlPointCount;
@property (T@"NSArray",W,N,V_radiusBuffers) radiusBuffers;
@property (TQ,N,V_radiusStride) radiusStride;
@property (T@"<MTLBuffer>",W,N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexBufferOffset) indexBufferOffset;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_controlPointFormat) controlPointFormat;
@property (TQ,N,V_radiusFormat) radiusFormat;
@property (TQ,N,V_segmentControlPointCount) segmentControlPointCount;
@property (Tq,N,V_curveType) curveType;
@property (Tq,N,V_curveBasis) curveBasis;
@property (Tq,N,V_curveEndCaps) curveEndCaps;
```

## Instance methods

```
-[MTLBVHCurveGeometryDescriptor indexType];
-[MTLBVHCurveGeometryDescriptor setIndexType:];
-[MTLBVHCurveGeometryDescriptor primitiveType];
-[MTLBVHCurveGeometryDescriptor setIndexBuffer:];
-[MTLBVHCurveGeometryDescriptor controlPointBuffers];
-[MTLBVHCurveGeometryDescriptor controlPointCount];
-[MTLBVHCurveGeometryDescriptor controlPointFormat];
-[MTLBVHCurveGeometryDescriptor controlPointStride];
-[MTLBVHCurveGeometryDescriptor curveBasis];
-[MTLBVHCurveGeometryDescriptor curveEndCaps];
-[MTLBVHCurveGeometryDescriptor curveType];
-[MTLBVHCurveGeometryDescriptor indexBuffer];
-[MTLBVHCurveGeometryDescriptor indexBufferOffset];
-[MTLBVHCurveGeometryDescriptor radiusBuffers];
-[MTLBVHCurveGeometryDescriptor radiusFormat];
-[MTLBVHCurveGeometryDescriptor radiusStride];
-[MTLBVHCurveGeometryDescriptor segmentControlPointCount];
-[MTLBVHCurveGeometryDescriptor setControlPointBuffers:];
-[MTLBVHCurveGeometryDescriptor setControlPointCount:];
-[MTLBVHCurveGeometryDescriptor setControlPointFormat:];
-[MTLBVHCurveGeometryDescriptor setControlPointStride:];
-[MTLBVHCurveGeometryDescriptor setCurveBasis:];
-[MTLBVHCurveGeometryDescriptor setCurveEndCaps:];
-[MTLBVHCurveGeometryDescriptor setCurveType:];
-[MTLBVHCurveGeometryDescriptor setIndexBufferOffset:];
-[MTLBVHCurveGeometryDescriptor setRadiusBuffers:];
-[MTLBVHCurveGeometryDescriptor setRadiusFormat:];
-[MTLBVHCurveGeometryDescriptor setRadiusStride:];
-[MTLBVHCurveGeometryDescriptor setSegmentControlPointCount:];
```
