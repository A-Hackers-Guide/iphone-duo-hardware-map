# `_MTL4FXEffect`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFXEffectBase`
- Protocols: `MTL4FXEffectTracing`
- 2 instance variables, 5 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"<MTL4FXEffectTracingDelegate>" _tracingDelegate;
@"NSObject<OS_dispatch_semaphore>" _maxFramesInFlightSemaphore;
```

## Properties

```
@property (T@"<MTL4FXEffectTracingDelegate>",W,V_tracingDelegate) tracingDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4FXEffect init];
-[_MTL4FXEffect tracingDelegate];
-[_MTL4FXEffect _beginEncodeWithCommandBuffer:];
-[_MTL4FXEffect _didCreateComputeCommandEncoder:forEncode:];
-[_MTL4FXEffect _didCreateRenderCommandEncoder:forEncode:];
-[_MTL4FXEffect setTracingDelegate:];
```
