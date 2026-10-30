# `MTLToolsIOCommandQueue`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLIOCommandQueueSPI`
- 0 instance variables, 7 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsIOCommandQueue barrier];
-[MTLToolsIOCommandQueue label];
-[MTLToolsIOCommandQueue setLabel:];
-[MTLToolsIOCommandQueue globalTraceObjectID];
-[MTLToolsIOCommandQueue dealloc];
-[MTLToolsIOCommandQueue commandBuffer];
-[MTLToolsIOCommandQueue commandBufferWithUnretainedReferences];
-[MTLToolsIOCommandQueue enqueueBarrier];
-[MTLToolsIOCommandQueue initWithBaseObject:parent:];
```
