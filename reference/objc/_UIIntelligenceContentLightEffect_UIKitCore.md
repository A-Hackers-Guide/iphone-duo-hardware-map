# `_UIIntelligenceContentLightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- Protocols: `_UIVisualEffectDirectionalTransitioning`, `_UIVisualEffectDirectionalActivationTransitioning`, `_UIVisualEffectDirectionalDeactivationTransitioning`
- 4 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
lightSource;
material;
Q activationTransitionDirection;
Q deactivationTransitionDirection;
```

## Properties

```
@property (TQ,N,VactivationTransitionDirection) activationTransitionDirection;
@property (TQ,N,VdeactivationTransitionDirection) deactivationTransitionDirection;
```

## Instance methods

```
-[_UIIntelligenceContentLightEffect _expectedUsage];
-[_UIIntelligenceContentLightEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[_UIIntelligenceContentLightEffect init];
-[_UIIntelligenceContentLightEffect _updateEffectDescriptor:forEnvironment:usage:];
-[_UIIntelligenceContentLightEffect initWithCoder:];
-[_UIIntelligenceContentLightEffect isEqual:];
-[_UIIntelligenceContentLightEffect deactivationTransitionDirection];
-[_UIIntelligenceContentLightEffect activationTransitionDirection];
-[_UIIntelligenceContentLightEffect initWithLightSource:];
-[_UIIntelligenceContentLightEffect initWithLightSource:blurStyle:];
-[_UIIntelligenceContentLightEffect initWithLightSource:lightMaterial:darkMaterial:bundle:];
-[_UIIntelligenceContentLightEffect setActivationTransitionDirection:];
-[_UIIntelligenceContentLightEffect setDeactivationTransitionDirection:];
```
