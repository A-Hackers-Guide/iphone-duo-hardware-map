# `MTLPointerTypeInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLPointerType`
- 9 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _dataType;
Q _elementType;
@"MTLType" _elementTypeInfo;
Q _access;
Q _alignment;
Q _dataSize;
B _elementIsArgumentBuffer;
B _isConstantBuffer;
B _doRetain;
```

## Instance methods

```
-[MTLPointerTypeInternal initWithElementType:elementTypeDescription:access:alignment:dataSize:elementIsIndirectArgumentBuffer:isConstantBuffer:];
-[MTLPointerTypeInternal dealloc];
-[MTLPointerTypeInternal access];
-[MTLPointerTypeInternal initWithElementType:elementTypeDescription:access:alignment:dataSize:elementIsIndirectArgumentBuffer:isConstantBuffer:doRetain:];
-[MTLPointerTypeInternal elementStructType];
-[MTLPointerTypeInternal elementTypeDescription];
-[MTLPointerTypeInternal structType];
-[MTLPointerTypeInternal alignment];
-[MTLPointerTypeInternal formattedDescription:withPrintedTypes:];
-[MTLPointerTypeInternal setAlignment:dataSize:];
-[MTLPointerTypeInternal dataType];
-[MTLPointerTypeInternal elementArrayType];
-[MTLPointerTypeInternal elementType];
-[MTLPointerTypeInternal elementIsIndirectArgumentBuffer];
-[MTLPointerTypeInternal dataSize];
-[MTLPointerTypeInternal elementIsArgumentBuffer];
-[MTLPointerTypeInternal isEqual:];
-[MTLPointerTypeInternal isConstantBuffer];
```
