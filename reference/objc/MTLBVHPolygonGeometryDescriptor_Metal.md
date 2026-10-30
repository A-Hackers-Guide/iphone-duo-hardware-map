# `MTLBVHPolygonGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBVHGeometryDescriptor`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
Q _polygonType;
@"NSArray" _vertexBuffers;
Q _vertexStride;
@"<MTLBuffer>" _indexBuffer;
Q _indexBufferOffset;
Q _indexType;
Q _vertexFormat;
@"<MTLBuffer>" _transformationMatrixBuffer;
Q _transformationMatrixOffsetBuffer;
q _transformationMatrixLayout;
```

## Properties

```
@property (TQ,N,V_polygonType) polygonType;
@property (T@"NSArray",W,N,V_vertexBuffers) vertexBuffers;
@property (TQ,N,V_vertexStride) vertexStride;
@property (T@"<MTLBuffer>",W,N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexBufferOffset) indexBufferOffset;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_vertexFormat) vertexFormat;
@property (T@"<MTLBuffer>",W,N,V_transformationMatrixBuffer) transformationMatrixBuffer;
@property (TQ,N,V_transformationMatrixOffsetBuffer) transformationMatrixBufferOffset;
@property (Tq,N,V_transformationMatrixLayout) transformationMatrixLayout;
```

## Instance methods

```
-[MTLBVHPolygonGeometryDescriptor indexType];
-[MTLBVHPolygonGeometryDescriptor vertexBuffers];
-[MTLBVHPolygonGeometryDescriptor setIndexType:];
-[MTLBVHPolygonGeometryDescriptor primitiveType];
-[MTLBVHPolygonGeometryDescriptor setIndexBuffer:];
-[MTLBVHPolygonGeometryDescriptor setPolygonType:];
-[MTLBVHPolygonGeometryDescriptor indexBuffer];
-[MTLBVHPolygonGeometryDescriptor indexBufferOffset];
-[MTLBVHPolygonGeometryDescriptor polygonType];
-[MTLBVHPolygonGeometryDescriptor setIndexBufferOffset:];
-[MTLBVHPolygonGeometryDescriptor setTransformationMatrixBuffer:];
-[MTLBVHPolygonGeometryDescriptor setTransformationMatrixBufferOffset:];
-[MTLBVHPolygonGeometryDescriptor setTransformationMatrixLayout:];
-[MTLBVHPolygonGeometryDescriptor setVertexBuffers:];
-[MTLBVHPolygonGeometryDescriptor setVertexFormat:];
-[MTLBVHPolygonGeometryDescriptor setVertexStride:];
-[MTLBVHPolygonGeometryDescriptor transformationMatrixBuffer];
-[MTLBVHPolygonGeometryDescriptor transformationMatrixBufferOffset];
-[MTLBVHPolygonGeometryDescriptor transformationMatrixLayout];
-[MTLBVHPolygonGeometryDescriptor vertexFormat];
-[MTLBVHPolygonGeometryDescriptor vertexStride];
```
