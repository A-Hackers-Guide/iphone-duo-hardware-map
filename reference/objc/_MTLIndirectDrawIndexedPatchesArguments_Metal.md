# `_MTLIndirectDrawIndexedPatchesArguments`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _numberOfPatchControlPoints;
Q _patchStart;
Q _patchCount;
^v _patchIndexBufferVirtualAddress;
Q _patchIndexBufferOffset;
^v _controlPointIndexBufferVirtualAddress;
Q _controlPointIndexBufferOffset;
Q _instanceCount;
Q _baseInstance;
Q _patchIndexBufferGPUVirtualAddress;
Q _controlPointIndexBufferGPUVirtualAddress;
```

## Properties

```
@property (TQ,N,V_numberOfPatchControlPoints) numberOfPatchControlPoints;
@property (TQ,N,V_patchStart) patchStart;
@property (TQ,N,V_patchCount) patchCount;
@property (T^v,N) patchIndexBufferVirtualAddress;
@property (T^v,N) controlPointIndexBufferVirtualAddress;
@property (TQ,N,V_patchIndexBufferGPUVirtualAddress) patchIndexBufferGPUVirtualAddress;
@property (TQ,N,V_controlPointIndexBufferGPUVirtualAddress) controlPointIndexBufferGPUVirtualAddress;
@property (TQ,N,V_instanceCount) instanceCount;
@property (TQ,N,V_baseInstance) baseInstance;
```

## Instance methods

```
-[_MTLIndirectDrawIndexedPatchesArguments setInstanceCount:];
-[_MTLIndirectDrawIndexedPatchesArguments instanceCount];
-[_MTLIndirectDrawIndexedPatchesArguments baseInstance];
-[_MTLIndirectDrawIndexedPatchesArguments controlPointIndexBufferGPUVirtualAddress];
-[_MTLIndirectDrawIndexedPatchesArguments controlPointIndexBufferVirtualAddress];
-[_MTLIndirectDrawIndexedPatchesArguments numberOfPatchControlPoints];
-[_MTLIndirectDrawIndexedPatchesArguments patchCount];
-[_MTLIndirectDrawIndexedPatchesArguments patchIndexBufferGPUVirtualAddress];
-[_MTLIndirectDrawIndexedPatchesArguments patchIndexBufferVirtualAddress];
-[_MTLIndirectDrawIndexedPatchesArguments patchStart];
-[_MTLIndirectDrawIndexedPatchesArguments setBaseInstance:];
-[_MTLIndirectDrawIndexedPatchesArguments setControlPointIndexBufferGPUVirtualAddress:];
-[_MTLIndirectDrawIndexedPatchesArguments setControlPointIndexBufferVirtualAddress:];
-[_MTLIndirectDrawIndexedPatchesArguments setNumberOfPatchControlPoints:];
-[_MTLIndirectDrawIndexedPatchesArguments setPatchCount:];
-[_MTLIndirectDrawIndexedPatchesArguments setPatchIndexBufferGPUVirtualAddress:];
-[_MTLIndirectDrawIndexedPatchesArguments setPatchIndexBufferVirtualAddress:];
-[_MTLIndirectDrawIndexedPatchesArguments setPatchStart:];
```
