# `_MTLIndirectDrawIndexedArguments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _primitiveType;
Q _indexCount;
Q _indexType;
^v _indexBufferVirtualAddress;
Q _indexBufferGPUVirtualAddress;
Q _indexBufferOffset;
Q _instanceCount;
Q _baseVertex;
Q _baseInstance;
```

## Properties

```
@property (TQ,N,V_primitiveType) primitiveType;
@property (TQ,N,V_indexCount) indexCount;
@property (TQ,N,V_indexType) indexType;
@property (T^v,N) indexBufferVirtualAddress;
@property (TQ,N,V_indexBufferGPUVirtualAddress) indexBufferGPUVirtualAddress;
@property (TQ,N,V_indexBufferOffset) indexBufferOffset;
@property (TQ,N,V_instanceCount) instanceCount;
@property (TQ,N,V_baseVertex) baseVertex;
@property (TQ,N,V_baseInstance) baseInstance;
```

## Instance methods

```
-[_MTLIndirectDrawIndexedArguments indexType];
-[_MTLIndirectDrawIndexedArguments setInstanceCount:];
-[_MTLIndirectDrawIndexedArguments instanceCount];
-[_MTLIndirectDrawIndexedArguments setIndexType:];
-[_MTLIndirectDrawIndexedArguments setPrimitiveType:];
-[_MTLIndirectDrawIndexedArguments primitiveType];
-[_MTLIndirectDrawIndexedArguments indexCount];
-[_MTLIndirectDrawIndexedArguments baseInstance];
-[_MTLIndirectDrawIndexedArguments baseVertex];
-[_MTLIndirectDrawIndexedArguments indexBufferGPUVirtualAddress];
-[_MTLIndirectDrawIndexedArguments indexBufferOffset];
-[_MTLIndirectDrawIndexedArguments indexBufferVirtualAddress];
-[_MTLIndirectDrawIndexedArguments setBaseInstance:];
-[_MTLIndirectDrawIndexedArguments setBaseVertex:];
-[_MTLIndirectDrawIndexedArguments setIndexBufferGPUVirtualAddress:];
-[_MTLIndirectDrawIndexedArguments setIndexBufferOffset:];
-[_MTLIndirectDrawIndexedArguments setIndexBufferVirtualAddress:];
-[_MTLIndirectDrawIndexedArguments setIndexCount:];
```
