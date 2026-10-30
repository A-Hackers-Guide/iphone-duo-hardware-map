# `_UISceneRegionHostInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `BSDescriptionStreaming`, `UIInteraction`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="enabled"b1"driving"b1} _flags;
@"_UISceneRegionHostComponent" _hostComponent;
@"NSArray" _lastSentSceneRegions;
@"UIView" _view;
```

## Properties

```
@property (TB,N,G_isEnabled,S_setEnabled:) _enabled;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneRegionHostInteraction debugDescription];
-[_UISceneRegionHostInteraction _setEnabled:];
-[_UISceneRegionHostInteraction _isEnabled];
-[_UISceneRegionHostInteraction dealloc];
-[_UISceneRegionHostInteraction succinctDescription];
-[_UISceneRegionHostInteraction view];
-[_UISceneRegionHostInteraction willMoveToView:];
-[_UISceneRegionHostInteraction description];
-[_UISceneRegionHostInteraction appendDescriptionToStream:];
-[_UISceneRegionHostInteraction _sceneRegionsDidChange];
-[_UISceneRegionHostInteraction didMoveToView:];
```
