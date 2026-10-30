# `MTLVertexDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLVertexDescriptor`
- 2 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"MTLVertexBufferLayoutDescriptorArrayInternal" _vertexBufferArray;
@"MTLVertexAttributeDescriptorArrayInternal" _attributeArray;
```

## Class methods

```
+[MTLVertexDescriptorInternal vertexDescriptor];
```

## Instance methods

```
-[MTLVertexDescriptorInternal newSerializedDescriptor];
-[MTLVertexDescriptorInternal formattedDescription:];
-[MTLVertexDescriptorInternal init];
-[MTLVertexDescriptorInternal validateWithVertexFunction:error:renderPipelineDescriptor:];
-[MTLVertexDescriptorInternal dealloc];
-[MTLVertexDescriptorInternal layouts];
-[MTLVertexDescriptorInternal reset];
-[MTLVertexDescriptorInternal hash];
-[MTLVertexDescriptorInternal description];
-[MTLVertexDescriptorInternal attributes];
-[MTLVertexDescriptorInternal copyWithZone:];
-[MTLVertexDescriptorInternal isEqual:];
```
