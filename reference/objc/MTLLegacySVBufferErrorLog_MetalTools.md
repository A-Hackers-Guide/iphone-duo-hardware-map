# `MTLLegacySVBufferErrorLog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLLegacySVGPULog`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
i _addressSpace;
i _operation;
i _specifiedUsage;
@"<MTLBuffer>" _buffer;
Q _offset;
@"MTLArgument" _argument;
```

## Properties

```
@property (Ti,N,V_addressSpace) addressSpace;
@property (T@"<MTLBuffer>",&,N,V_buffer) buffer;
@property (TQ,N,V_offset) offset;
@property (Ti,N,V_operation) operation;
@property (T@"MTLArgument",&,N,V_argument) argument;
@property (Ti,N,V_specifiedUsage) specifiedUsage;
```

## Instance methods

```
-[MTLLegacySVBufferErrorLog buffer];
-[MTLLegacySVBufferErrorLog setBuffer:];
-[MTLLegacySVBufferErrorLog setOperation:];
-[MTLLegacySVBufferErrorLog operation];
-[MTLLegacySVBufferErrorLog init];
-[MTLLegacySVBufferErrorLog dealloc];
-[MTLLegacySVBufferErrorLog description];
-[MTLLegacySVBufferErrorLog setOffset:];
-[MTLLegacySVBufferErrorLog offset];
-[MTLLegacySVBufferErrorLog argument];
-[MTLLegacySVBufferErrorLog setArgument:];
-[MTLLegacySVBufferErrorLog addressSpace];
-[MTLLegacySVBufferErrorLog setAddressSpace:];
-[MTLLegacySVBufferErrorLog setSpecifiedUsage:];
-[MTLLegacySVBufferErrorLog specifiedUsage];
```
