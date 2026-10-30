# `MTLToolsResource`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLResourceSPI`
- 2 instance variables, 18 properties, 30 instance methods, 0 class methods

## Instance variables

```
Q _options;
@"MTLToolsHeap" _heap;
```

## Properties

```
@property (TQ,R,N,V_options) options;
@property (Ti) responsibleProcess;
@property (TQ,R) allocationID;
@property (TQ,R) protectionOptions;
@property (TQ,R) unfilteredResourceOptions;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) storageMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (T@"<MTLHeap>",R) heap;
@property (TQ,R) heapOffset;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsResource resourceOptions];
-[MTLToolsResource isComplete];
-[MTLToolsResource hazardTrackingMode];
-[MTLToolsResource setOwnerWithIdentity:];
-[MTLToolsResource cpuCacheMode];
-[MTLToolsResource storageMode];
-[MTLToolsResource unfilteredResourceOptions];
-[MTLToolsResource protectionOptions];
-[MTLToolsResource label];
-[MTLToolsResource setLabel:];
-[MTLToolsResource allocatedSize];
-[MTLToolsResource dealloc];
-[MTLToolsResource waitUntilComplete];
-[MTLToolsResource setPurgeableState:];
-[MTLToolsResource heap];
-[MTLToolsResource options];
-[MTLToolsResource isAliasable];
-[MTLToolsResource makeAliasable];
-[MTLToolsResource isPurgeable];
-[MTLToolsResource heapOffset];
-[MTLToolsResource setResponsibleProcess:];
-[MTLToolsResource allocationID];
-[MTLToolsResource doesAliasAllResources:count:];
-[MTLToolsResource doesAliasAnyResources:count:];
-[MTLToolsResource doesAliasResource:];
-[MTLToolsResource initWithBaseObject:parent:];
-[MTLToolsResource responsibleProcess];
-[MTLToolsResource initWithBaseObject:parent:heap:];
-[MTLToolsResource validateCPUReadable];
-[MTLToolsResource validateCPUWriteable];
```
