# `MTLIndirectConstantArgument`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- 5 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
S _dataType;
S _alignment;
S _dataSize;
Q _pixelFormat;
Q _aluType;
```

## Instance methods

```
-[MTLIndirectConstantArgument bufferPixelFormat];
-[MTLIndirectConstantArgument dealloc];
-[MTLIndirectConstantArgument bufferALUType];
-[MTLIndirectConstantArgument formattedDescription:withPrintedTypes:];
-[MTLIndirectConstantArgument isEqual:];
-[MTLIndirectConstantArgument indirectConstantAlignment];
-[MTLIndirectConstantArgument indirectConstantDataSize];
-[MTLIndirectConstantArgument indirectConstantDataType];
-[MTLIndirectConstantArgument initWithName:type:access:isActive:locationIndex:dataType:pixelFormat:aluType:dataSize:alignment:];
```
