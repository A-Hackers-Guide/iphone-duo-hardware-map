# `_UISEVelocityDirectionEdgesGestureFeature`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISEGestureFeature`
- Protocols: `_UISETouchedEdgesProvider`
- 5 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<_UISEGestureFeatureSettings>" _settings;
@"<_UISETouchedEdgesProvider>" _provider;
B _exactMatchEdges;
{CGPoint="x"d"y"d} _initialLocation;
Q _touchedEdges;
```

## Properties

```
@property (TQ,R,N,V_touchedEdges) touchedEdges;
```

## Instance methods

```
-[_UISEVelocityDirectionEdgesGestureFeature _incorporateSample:];
-[_UISEVelocityDirectionEdgesGestureFeature touchedEdges];
-[_UISEVelocityDirectionEdgesGestureFeature initWithSettings:touchedEdgesProvider:exactMatchEdges:];
-[_UISEVelocityDirectionEdgesGestureFeature debugDictionary];
```
