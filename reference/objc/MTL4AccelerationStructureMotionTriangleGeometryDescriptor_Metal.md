# `MTL4AccelerationStructureMotionTriangleGeometryDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTL4AccelerationStructureGeometryDescriptor`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _indexType;
Q _triangleCount;
Q _vertexStride;
Q _vertexFormat;
q _transformationMatrixLayout;
{MTL4BufferRange="bufferAddress"Q"length"Q} _vertexBuffers;
{MTL4BufferRange="bufferAddress"Q"length"Q} _indexBuffer;
{MTL4BufferRange="bufferAddress"Q"length"Q} _transformationMatrixBuffer;
```

## Properties

```
@property (T{MTL4BufferRange=QQ},N,V_vertexBuffers) vertexBuffers;
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
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor indexType];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor vertexBuffers];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor init];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setIndexType:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor dealloc];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor type];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor hash];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor copyWithZone:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor isEqual:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setIndexBuffer:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor indexBuffer];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setTransformationMatrixBuffer:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setTransformationMatrixLayout:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setTriangleCount:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setVertexBuffers:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setVertexFormat:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor setVertexStride:];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor transformationMatrixBuffer];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor transformationMatrixLayout];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor triangleCount];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor vertexFormat];
-[MTL4AccelerationStructureMotionTriangleGeometryDescriptor vertexStride];
```
