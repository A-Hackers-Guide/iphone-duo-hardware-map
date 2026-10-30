# `_UIIntelligenceEdgeLightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- Protocols: `_UIVisualEffectDirectionalTransitioning`, `_UIVisualEffectDirectionalActivationTransitioning`, `_UIVisualEffectDirectionalDeactivationTransitioning`
- 5 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q activationTransitionDirection;
Q deactivationTransitionDirection;
lightSource;
region;
radius;
```

## Properties

```
@property (TQ,N,VactivationTransitionDirection) activationTransitionDirection;
@property (TQ,N,VdeactivationTransitionDirection) deactivationTransitionDirection;
```

## Instance methods

```
-[_UIIntelligenceEdgeLightEffect _expectedUsage];
-[_UIIntelligenceEdgeLightEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[_UIIntelligenceEdgeLightEffect init];
-[_UIIntelligenceEdgeLightEffect _updateEffectDescriptor:forEnvironment:usage:];
-[_UIIntelligenceEdgeLightEffect initWithCoder:];
-[_UIIntelligenceEdgeLightEffect isEqual:];
-[_UIIntelligenceEdgeLightEffect deactivationTransitionDirection];
-[_UIIntelligenceEdgeLightEffect activationTransitionDirection];
-[_UIIntelligenceEdgeLightEffect initWithLightSource:radius:region:];
-[_UIIntelligenceEdgeLightEffect setActivationTransitionDirection:];
-[_UIIntelligenceEdgeLightEffect setDeactivationTransitionDirection:];
```
