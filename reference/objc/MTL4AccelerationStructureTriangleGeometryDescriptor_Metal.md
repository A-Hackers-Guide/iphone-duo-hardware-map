# `MTL4AccelerationStructureTriangleGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureGeometryDescriptor`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _vertexStride;
Q _indexType;
Q _triangleCount;
Q _vertexFormat;
q _transformationMatrixLayout;
{MTL4BufferRange="bufferAddress"Q"length"Q} _vertexBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _indexBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _transformationMatrixBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_vertexBuffer) vertexBuffer;
@property (TQ,N,V_vertexFormat) vertexFormat;
@property (TQ,N,V_vertexStride) vertexStride;
@property (T{MTL4BufferRange=QQ},N,V_indexBuffer) indexBuffer;
@property (TQ,N,V_indexType) indexType;
@property (TQ,N,V_triangleCount) triangleCount;
@property (T{MTL4BufferRange=QQ},N,V_transformationMatrixBuffer) transformationMatrixBuffer;
@property (Tq,N,V_transformationMatrixLayout) transformationMatrixLayout;
```

## Instance methods

```
-[MTL4AccelerationStructureTriangleGeometryDescriptor indexType];
-[MTL4AccelerationStructureTriangleGeometryDescriptor init];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setIndexType:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor dealloc];
-[MTL4AccelerationStructureTriangleGeometryDescriptor type];
-[MTL4AccelerationStructureTriangleGeometryDescriptor hash];
-[MTL4AccelerationStructureTriangleGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setIndexBuffer:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor indexBuffer];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setTransformationMatrixBuffer:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setTransformationMatrixLayout:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setTriangleCount:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setVertexBuffer:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setVertexFormat:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor setVertexStride:];
-[MTL4AccelerationStructureTriangleGeometryDescriptor transformationMatrixBuffer];
-[MTL4AccelerationStructureTriangleGeometryDescriptor transformationMatrixLayout];
-[MTL4AccelerationStructureTriangleGeometryDescriptor triangleCount];
-[MTL4AccelerationStructureTriangleGeometryDescriptor vertexBuffer];
-[MTL4AccelerationStructureTriangleGeometryDescriptor vertexFormat];
-[MTL4AccelerationStructureTriangleGeometryDescriptor vertexStride];
```
