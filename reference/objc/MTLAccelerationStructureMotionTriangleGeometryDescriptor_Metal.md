# `MTLAccelerationStructureMotionTriangleGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLAccelerationStructureGeometryDescriptor`
- 10 instance variables, 10 properties, 26 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _vertexBuffers;
@"<MTLBuffer>" _indexBuffer;
Q _indexBufferOffset;
Q _indexType;
Q _triangleCount;
Q _vertexStride;
Q _vertexFormat;
@"<MTLBuffer>" _transformationMatrixBuffer;
Q _transformationMatrixBufferOffset;
q _transformationMatrixLayout;
```

## Properties

```
@property (T@"NSArray",C,N,V_vertexBuffers) vertexBuffers;
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
+[MTLAccelerationStructureMotionTriangleGeometryDescriptor descriptor];
```

## Instance methods

```
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor indexType];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor vertexBuffers];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor init];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setIndexType:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor dealloc];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor type];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor hash];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor copyWithZone:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor isEqual:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setIndexBuffer:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor indexBuffer];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor indexBufferOffset];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setIndexBufferOffset:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setTransformationMatrixBuffer:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setTransformationMatrixBufferOffset:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setTransformationMatrixLayout:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setTriangleCount:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setVertexBuffers:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setVertexFormat:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor setVertexStride:];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor transformationMatrixBuffer];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor transformationMatrixBufferOffset];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor transformationMatrixLayout];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor triangleCount];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor vertexFormat];
-[MTLAccelerationStructureMotionTriangleGeometryDescriptor vertexStride];
```
