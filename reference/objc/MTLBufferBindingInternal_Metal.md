# `MTLBufferBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- Protocols: `MTLBufferBinding`
- 6 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
b15 _dataType;
b1 _vertexDescriptorBuffer;
S _alignment;
I _dataSize;
Q _pixelFormat;
Q _aluType;
```

## Properties

```
@property (TQ,R) bufferAlignment;
@property (TQ,R) bufferDataSize;
@property (TQ,R) bufferDataType;
@property (T@"MTLStructType",R) bufferStructType;
@property (T@"MTLPointerType",R) bufferPointerType;
@property (T@"NSString",R) name;
@property (Tq,R) type;
@property (TQ,R) access;
@property (TQ,R) index;
@property (TB,R,GisUsed) used;
@property (TB,R,GisArgument) argument;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLBufferBindingInternal formattedDescription:];
-[MTLBufferBindingInternal bufferPixelFormat];
-[MTLBufferBindingInternal setStructType:doRetain:];
-[MTLBufferBindingInternal dealloc];
-[MTLBufferBindingInternal bufferDataSize];
-[MTLBufferBindingInternal setDataSize:];
-[MTLBufferBindingInternal isVertexDescriptorBuffer];
-[MTLBufferBindingInternal setAlignment:];
-[MTLBufferBindingInternal setStructType:];
-[MTLBufferBindingInternal bufferPointerType];
-[MTLBufferBindingInternal structType];
-[MTLBufferBindingInternal bufferAlignment];
-[MTLBufferBindingInternal bufferIndirectArgumentType];
-[MTLBufferBindingInternal bufferDataType];
-[MTLBufferBindingInternal bufferALUType];
-[MTLBufferBindingInternal setVertexDescriptorBuffer:];
-[MTLBufferBindingInternal initWithName:type:access:isActive:locationIndex:arraySize:dataType:pixelFormat:aluType:isConstantBuffer:dataSize:alignment:];
-[MTLBufferBindingInternal isEqual:];
-[MTLBufferBindingInternal bufferStructType];
```
