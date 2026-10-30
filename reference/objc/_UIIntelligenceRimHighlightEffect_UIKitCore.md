# `_UIIntelligenceRimHighlightEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- Protocols: `_UIVisualEffectDirectionalTransitioning`, `_UIVisualEffectDirectionalActivationTransitioning`, `_UIVisualEffectDirectionalDeactivationTransitioning`
- 3 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
config;
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
-[_UIIntelligenceRimHighlightEffect _needsUpdateForTransitionFromEnvironment:toEnvironment:usage:];
-[_UIIntelligenceRimHighlightEffect init];
-[_UIIntelligenceRimHighlightEffect _updateEffectDescriptor:forEnvironment:usage:];
-[_UIIntelligenceRimHighlightEffect initWithCoder:];
-[_UIIntelligenceRimHighlightEffect isEqual:];
-[_UIIntelligenceRimHighlightEffect deactivationTransitionDirection];
-[_UIIntelligenceRimHighlightEffect activationTransitionDirection];
-[_UIIntelligenceRimHighlightEffect initWithThickness:activationDirection:];
-[_UIIntelligenceRimHighlightEffect initWithThickness:color:softRadius:region:activationDirection:];
-[_UIIntelligenceRimHighlightEffect setActivationTransitionDirection:];
-[_UIIntelligenceRimHighlightEffect setDeactivationTransitionDirection:];
```
