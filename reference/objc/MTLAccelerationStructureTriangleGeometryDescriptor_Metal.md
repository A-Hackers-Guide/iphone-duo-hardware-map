# `MTLAccelerationStructureTriangleGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 11 instance variables, 11 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"<MTLBuffer>" _vertexBuffer;
Q _vertexBufferOffset;
Q _vertexStride;
@"<MTLBuffer>" _indexBuffer;
Q _indexBufferOffset;
Q _indexType;
Q _triangleCount;
Q _vertexFormat;
@"<MTLBuffer>" _transformationMatrixBuffer;
Q _transformationMatrixBufferOffset;
q _transformationMatrixLayout;
```

## Properties

```
@property (T@"<MTLBuffer>",&,N,V_vertexBuffer) vertexBuffer;
@property (TQ,N,V_vertexBufferOffset) vertexBufferOffset;
@property (TQ,N,V_vertexFormat) vertexFormat;
@property (TQ,N,V_vertexStride) vertexStride;
@property (T@"<MTLBuffer>",&,N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexBufferOffset) indexBufferOffset;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_triangleCount) triangleCount;
@property (T@"<MTLBuffer>",&,N,V_transformationMatrixBuffer) transformationMatrixBuffer;
@property (TQ,N,V_transformationMatrixBufferOffset) transformationMatrixBufferOffset;
@property (Tq,N,V_transformationMatrixLayout) transformationMatrixLayout;
```

## Class methods

```
+[MTLAccelerationStructureTriangleGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureTriangleGeometryDescriptor indexType];
-[MTLAccelerationStructureTriangleGeometryDescriptor init];
-[MTLAccelerationStructureTriangleGeometryDescriptor setIndexType:];
-[MTLAccelerationStructureTriangleGeometryDescriptor dealloc];
-[MTLAccelerationStructureTriangleGeometryDescriptor type];
-[MTLAccelerationStructureTriangleGeometryDescriptor hash];
-[MTLAccelerationStructureTriangleGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureTriangleGeometryDescriptor isEqual:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setIndexBuffer:];
-[MTLAccelerationStructureTriangleGeometryDescriptor indexBuffer];
-[MTLAccelerationStructureTriangleGeometryDescriptor indexBufferOffset];
-[MTLAccelerationStructureTriangleGeometryDescriptor setIndexBufferOffset:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setTransformationMatrixBuffer:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setTransformationMatrixBufferOffset:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setTransformationMatrixLayout:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setTriangleCount:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setVertexBuffer:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setVertexBufferOffset:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setVertexFormat:];
-[MTLAccelerationStructureTriangleGeometryDescriptor setVertexStride:];
-[MTLAccelerationStructureTriangleGeometryDescriptor transformationMatrixBuffer];
-[MTLAccelerationStructureTriangleGeometryDescriptor transformationMatrixBufferOffset];
-[MTLAccelerationStructureTriangleGeometryDescriptor transformationMatrixLayout];
-[MTLAccelerationStructureTriangleGeometryDescriptor triangleCount];
-[MTLAccelerationStructureTriangleGeometryDescriptor vertexBuffer];
-[MTLAccelerationStructureTriangleGeometryDescriptor vertexBufferOffset];
-[MTLAccelerationStructureTriangleGeometryDescriptor vertexFormat];
-[MTLAccelerationStructureTriangleGeometryDescriptor vertexStride];
```
