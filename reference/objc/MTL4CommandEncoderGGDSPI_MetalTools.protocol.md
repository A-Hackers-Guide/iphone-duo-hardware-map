# `MTL4CommandEncoderGGDSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandEncoderSPI`
- 0 instance variables, 2 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
```

## Instance methods

```
-[MTL4CommandEncoderGGDSPI globalTraceObjectID];
-[MTL4CommandEncoderGGDSPI barrierAfterEncoderStages:beforeEncoderStages:options:];
-[MTL4CommandEncoderGGDSPI barrierAfterQueueStages:beforeStages:options:];
-[MTL4CommandEncoderGGDSPI barrierAfterStages:beforeQueueStages:options:];
-[MTL4CommandEncoderGGDSPI commandAllocator];
```
