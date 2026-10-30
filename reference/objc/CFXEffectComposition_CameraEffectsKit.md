# `CFXEffectComposition`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _filters;
@"NSMutableArray" _overlays;
@"NSMutableArray" _animojis;
@"NSObject<OS_dispatch_queue>" _concurrentQueue;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_filters) filters;
@property (T@"NSMutableArray",&,N,V_overlays) overlays;
@property (T@"NSMutableArray",&,N,V_animojis) animojis;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_concurrentQueue) concurrentQueue;
@property (TQ,R,N) count;
@property (T@"NSArray",R,N) effects;
@property (T@"NSArray",R,N) jtEffects;
@property (TB,R,N) hasFaceTrackedOverlays;
@property (TB,R,N) isEmpty;
@property (TB,R,N) requiresFaceTracking;
```

## Instance methods

```
-[CFXEffectComposition setConcurrentQueue:];
-[CFXEffectComposition concurrentQueue];
-[CFXEffectComposition effects];
-[CFXEffectComposition init];
-[CFXEffectComposition setFilters:];
-[CFXEffectComposition count];
-[CFXEffectComposition filters];
-[CFXEffectComposition overlays];
-[CFXEffectComposition isEmpty];
-[CFXEffectComposition setOverlays:];
-[CFXEffectComposition CFX_effectsForJettyType:];
-[CFXEffectComposition addEffect:completion:];
-[CFXEffectComposition animojis];
-[CFXEffectComposition hasEffectOfType:];
-[CFXEffectComposition hasFaceTrackedOverlays];
-[CFXEffectComposition indexOfEffect:];
-[CFXEffectComposition insertEffectAtIndex:atIndex:];
-[CFXEffectComposition jtEffects];
-[CFXEffectComposition jtEffectsForType:];
-[CFXEffectComposition removeAllEffects:];
-[CFXEffectComposition removeAllEffectsOfType:completion:];
-[CFXEffectComposition removeAllOverlayEffects:];
-[CFXEffectComposition removeEffect:completion:];
-[CFXEffectComposition requiresFaceTracking];
-[CFXEffectComposition setAnimojis:];
```
