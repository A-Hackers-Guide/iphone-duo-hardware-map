# `_UISceneZoomTransitionClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UIDismissInteractionDelegate`, `BSDescriptionStreaming`, `FBSSceneObserver`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"_UIDismissInteraction" _dismissInteraction;
@"UIWindow" _dismissInteractionWindow;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneZoomTransitionClientComponent trackingViewForInteraction:];
-[_UISceneZoomTransitionClientComponent dismissInteraction:didCancelWithVelocity:originalPosition:];
-[_UISceneZoomTransitionClientComponent debugDescription];
-[_UISceneZoomTransitionClientComponent scene:didUpdateSettings:];
-[_UISceneZoomTransitionClientComponent dismissInteraction:didBeginAtLocation:withVelocity:];
-[_UISceneZoomTransitionClientComponent hysteresisForInteraction:];
-[_UISceneZoomTransitionClientComponent succinctDescription];
-[_UISceneZoomTransitionClientComponent dismissInteraction:didIssueUpdate:];
-[_UISceneZoomTransitionClientComponent description];
-[_UISceneZoomTransitionClientComponent appendDescriptionToStream:];
-[_UISceneZoomTransitionClientComponent dismissInteraction:didDismissWithVelocity:];
-[_UISceneZoomTransitionClientComponent dismissInteraction:shouldBeginWithAxis:location:velocity:proposal:];
```
