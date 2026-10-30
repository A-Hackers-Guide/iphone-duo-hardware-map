# `_MTLIndirectDrawPatchesArguments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
Q _numberOfPatchControlPoints;
Q _patchStart;
Q _patchCount;
^v _patchIndexBufferVirtualAddress;
Q _patchIndexBufferGPUVirtualAddress;
Q _patchIndexBufferOffset;
Q _instanceCount;
Q _baseInstance;
```

## Properties

```
@property (TQ,N,V_numberOfPatchControlPoints) numberOfPatchControlPoints;
@property (TQ,N,V_patchStart) patchStart;
@property (TQ,N,V_patchCount) patchCount;
@property (T^v,N) patchIndexBufferVirtualAddress;
@property (TQ,N,V_patchIndexBufferGPUVirtualAddress) patchIndexBufferGPUVirtualAddress;
@property (TQ,N,V_patchIndexBufferOffset) patchIndexBufferOffset;
@property (TQ,N,V_instanceCount) instanceCount;
@property (TQ,N,V_baseInstance) baseInstance;
```

## Instance methods

```
-[_MTLIndirectDrawPatchesArguments setInstanceCount:];
-[_MTLIndirectDrawPatchesArguments instanceCount];
-[_MTLIndirectDrawPatchesArguments baseInstance];
-[_MTLIndirectDrawPatchesArguments numberOfPatchControlPoints];
-[_MTLIndirectDrawPatchesArguments patchCount];
-[_MTLIndirectDrawPatchesArguments patchIndexBufferGPUVirtualAddress];
-[_MTLIndirectDrawPatchesArguments patchIndexBufferOffset];
-[_MTLIndirectDrawPatchesArguments patchIndexBufferVirtualAddress];
-[_MTLIndirectDrawPatchesArguments patchStart];
-[_MTLIndirectDrawPatchesArguments setBaseInstance:];
-[_MTLIndirectDrawPatchesArguments setNumberOfPatchControlPoints:];
-[_MTLIndirectDrawPatchesArguments setPatchCount:];
-[_MTLIndirectDrawPatchesArguments setPatchIndexBufferGPUVirtualAddress:];
-[_MTLIndirectDrawPatchesArguments setPatchIndexBufferOffset:];
-[_MTLIndirectDrawPatchesArguments setPatchIndexBufferVirtualAddress:];
-[_MTLIndirectDrawPatchesArguments setPatchStart:];
```
