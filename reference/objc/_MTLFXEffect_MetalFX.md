# `_MTLFXEffect`

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLFXEffectBase`
- Protocols: `MTLFXEffectTracing`
- 1 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"<MTLFXEffectTracingDelegate>" _tracingDelegate;
```

## Properties

```
@property (T@"<MTLFXEffectTracingDelegate>",W,V_tracingDelegate) tracingDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLFXEffect tracingDelegate];
-[_MTLFXEffect _didCreateBlitCommandEncoder:forEncode:];
-[_MTLFXEffect _didCreateComputeCommandEncoder:forEncode:];
-[_MTLFXEffect _didCreateRenderCommandEncoder:forEncode:];
-[_MTLFXEffect setTracingDelegate:];
```
