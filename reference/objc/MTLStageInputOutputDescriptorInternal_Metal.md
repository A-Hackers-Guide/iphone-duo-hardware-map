# `MTLStageInputOutputDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLStageInputOutputDescriptor`
- 4 instance variables, 0 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"MTLBufferLayoutDescriptorArrayInternal" _vertexBufferArray;
@"MTLAttributeDescriptorArrayInternal" _attributeArray;
Q _indexBufferIndex;
Q _indexType;
```

## Class methods

```
+[MTLStageInputOutputDescriptorInternal vertexDescriptor];
```

## Instance methods

```
-[MTLStageInputOutputDescriptorInternal indexType];
-[MTLStageInputOutputDescriptorInternal newSerializedDescriptor];
-[MTLStageInputOutputDescriptorInternal formattedDescription:];
-[MTLStageInputOutputDescriptorInternal init];
-[MTLStageInputOutputDescriptorInternal setIndexType:];
-[MTLStageInputOutputDescriptorInternal validateWithVertexFunction:error:renderPipelineDescriptor:];
-[MTLStageInputOutputDescriptorInternal dealloc];
-[MTLStageInputOutputDescriptorInternal layouts];
-[MTLStageInputOutputDescriptorInternal reset];
-[MTLStageInputOutputDescriptorInternal hash];
-[MTLStageInputOutputDescriptorInternal description];
-[MTLStageInputOutputDescriptorInternal setIndexBufferIndex:];
-[MTLStageInputOutputDescriptorInternal attributes];
-[MTLStageInputOutputDescriptorInternal copyWithZone:];
-[MTLStageInputOutputDescriptorInternal isEqual:];
-[MTLStageInputOutputDescriptorInternal indexBufferIndex];
```
