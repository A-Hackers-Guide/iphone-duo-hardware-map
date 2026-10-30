# `MTLGPUDebugBufferErrorLog`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLGPUDebugGPULog`
- 11 instance variables, 11 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _bufferIsResolved;
i _addressSpace;
i _operation;
i _specifiedUsage;
@"<MTLBuffer>" _buffer;
Q _bufferGPUAddress;
Q _bufferLength;
@"NSString" _bufferLabel;
Q _offset;
Q _gpuAddressAtErrorSite;
@"MTLArgument" _argument;
```

## Properties

```
@property (Ti,N,V_addressSpace) addressSpace;
@property (T@"<MTLBuffer>",N,V_buffer) buffer;
@property (TB,N,V_bufferIsResolved) bufferIsResolved;
@property (TQ,N,V_bufferGPUAddress) bufferGPUAddress;
@property (TQ,N,V_bufferLength) bufferLength;
@property (T@"NSString",C,N,V_bufferLabel) bufferLabel;
@property (TQ,N,V_offset) offset;
@property (Ti,N,V_operation) operation;
@property (TQ,N,V_gpuAddressAtErrorSite) gpuAddressAtErrorSite;
@property (T@"MTLArgument",&,N,V_argument) argument;
@property (Ti,N,V_specifiedUsage) specifiedUsage;
```

## Instance methods

```
-[MTLGPUDebugBufferErrorLog buffer];
-[MTLGPUDebugBufferErrorLog setBuffer:];
-[MTLGPUDebugBufferErrorLog setOperation:];
-[MTLGPUDebugBufferErrorLog operation];
-[MTLGPUDebugBufferErrorLog init];
-[MTLGPUDebugBufferErrorLog dealloc];
-[MTLGPUDebugBufferErrorLog description];
-[MTLGPUDebugBufferErrorLog setOffset:];
-[MTLGPUDebugBufferErrorLog offset];
-[MTLGPUDebugBufferErrorLog argument];
-[MTLGPUDebugBufferErrorLog bufferLength];
-[MTLGPUDebugBufferErrorLog setBufferLength:];
-[MTLGPUDebugBufferErrorLog setArgument:];
-[MTLGPUDebugBufferErrorLog addressSpace];
-[MTLGPUDebugBufferErrorLog setBufferLabel:];
-[MTLGPUDebugBufferErrorLog bufferGPUAddress];
-[MTLGPUDebugBufferErrorLog bufferIsResolved];
-[MTLGPUDebugBufferErrorLog bufferLabel];
-[MTLGPUDebugBufferErrorLog gpuAddressAtErrorSite];
-[MTLGPUDebugBufferErrorLog setAddressSpace:];
-[MTLGPUDebugBufferErrorLog setBufferGPUAddress:];
-[MTLGPUDebugBufferErrorLog setBufferIsResolved:];
-[MTLGPUDebugBufferErrorLog setGpuAddressAtErrorSite:];
-[MTLGPUDebugBufferErrorLog setSpecifiedUsage:];
-[MTLGPUDebugBufferErrorLog specifiedUsage];
```
