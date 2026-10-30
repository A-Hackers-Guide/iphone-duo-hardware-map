# `_UIHomeAffordanceHostSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `FBSceneObserver`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="needsProxyInteractionEvaluation"b1} _flags;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeAffordanceScreenFixedFrame;
@"_UIHomeAffordanceObserverProxyInteraction" _proxyHomeAffordanceObserverInteraction;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) homeAffordanceScreenFixedFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) homeAffordanceSceneReferenceFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHomeAffordanceHostSceneComponent homeAffordanceScreenFixedFrame];
-[_UIHomeAffordanceHostSceneComponent sceneWillActivate:];
-[_UIHomeAffordanceHostSceneComponent debugDescription];
-[_UIHomeAffordanceHostSceneComponent scene:didUpdateSettings:];
-[_UIHomeAffordanceHostSceneComponent setScene:];
-[_UIHomeAffordanceHostSceneComponent homeAffordanceSceneReferenceFrame];
-[_UIHomeAffordanceHostSceneComponent setHomeAffordanceScreenFixedFrame:];
-[_UIHomeAffordanceHostSceneComponent description];
-[_UIHomeAffordanceHostSceneComponent appendDescriptionToStream:];
-[_UIHomeAffordanceHostSceneComponent setHomeAffordanceSceneReferenceFrame:];
-[_UIHomeAffordanceHostSceneComponent doubleTapGestureDidSucceed:];
```
