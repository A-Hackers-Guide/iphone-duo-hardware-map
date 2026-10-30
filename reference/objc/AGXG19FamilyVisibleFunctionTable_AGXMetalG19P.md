# `AGXG19FamilyVisibleFunctionTable`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalVisibleFunctionTable`
- 3 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
{VisibleFunctionTable="resource_indirection_heap_allocation"{Allocation="index"I"size"I"pool"^v"directly_assigned"B}} _impl;
i _type;
@ _pipelineState;
```

## Properties

```
@property (TQ,R,N) gpuAddress;
```

## Instance methods

```
-[AGXG19FamilyVisibleFunctionTable setBuffers:offsets:withRange:];
-[AGXG19FamilyVisibleFunctionTable setValue:atIndex:];
-[AGXG19FamilyVisibleFunctionTable resourceIndex];
-[AGXG19FamilyVisibleFunctionTable setVisibleFunctionTables:withBufferRange:];
-[AGXG19FamilyVisibleFunctionTable setBuffer:offset:atIndex:];
-[AGXG19FamilyVisibleFunctionTable setVisibleFunctionTable:atBufferIndex:];
-[AGXG19FamilyVisibleFunctionTable dealloc];
-[AGXG19FamilyVisibleFunctionTable gpuAddress];
-[AGXG19FamilyVisibleFunctionTable setFunction:atIndex:];
-[AGXG19FamilyVisibleFunctionTable uniqueIdentifier];
-[AGXG19FamilyVisibleFunctionTable setValue:withRange:];
-[AGXG19FamilyVisibleFunctionTable bufferAddressAtIndex:];
-[AGXG19FamilyVisibleFunctionTable setFunctions:withRange:];
-[AGXG19FamilyVisibleFunctionTable clone:clonedResourceIndex:clonedVisibleFunctionHeap:cloneHandleMap:];
-[AGXG19FamilyVisibleFunctionTable initWithDevice:functionCount:options:isSuballocDisabled:clonedResourceIndex:clonedVisibleFunctionHeap:type:];
-[AGXG19FamilyVisibleFunctionTable initWithDevice:functionCount:options:isSuballocDisabled:resourceIndex:pipelineState:stage:];
-[AGXG19FamilyVisibleFunctionTable initWithDevice:functionCount:options:isSuballocDisabled:resourceIndex:pipelineState:type:];
```
