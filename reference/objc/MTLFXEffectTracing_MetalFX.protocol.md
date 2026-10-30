# `MTLFXEffectTracing` (protocol)

- Image: [`/System/Library/Frameworks/MetalFX.framework/MetalFX`](../userland/System__Library__Frameworks__MetalFX.framework__MetalFX.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLFXEffectTracingDelegate>",W) tracingDelegate;
```

## Instance methods

```
-[MTLFXEffectTracing tracingDelegate];
-[MTLFXEffectTracing _didCreateBlitCommandEncoder:forEncode:];
-[MTLFXEffectTracing _didCreateComputeCommandEncoder:forEncode:];
-[MTLFXEffectTracing _didCreateRenderCommandEncoder:forEncode:];
-[MTLFXEffectTracing setTracingDelegate:];
```
