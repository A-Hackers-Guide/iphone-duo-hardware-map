# `_UISceneTargetingInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `UIInteraction`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<_UISceneInteractionRegistrationTarget>" _sceneRegistrationTarget;
@? _registrationHandler;
@? _unregistrationHandler;
{?="registrationPendingDidMoveToWindow"b1"registrationPendingWindowMoveToScene"b1} _interactionFlags;
@"UIView" _view;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UISceneTargetingInteraction _windowWillMoveToScene:];
-[_UISceneTargetingInteraction _willMoveFromWindow:toWindow:];
-[_UISceneTargetingInteraction debugDescription];
-[_UISceneTargetingInteraction init];
-[_UISceneTargetingInteraction dealloc];
-[_UISceneTargetingInteraction _didMoveFromWindow:toWindow:];
-[_UISceneTargetingInteraction succinctDescription];
-[_UISceneTargetingInteraction view];
-[_UISceneTargetingInteraction _windowDidMoveToScene:];
-[_UISceneTargetingInteraction willMoveToView:];
-[_UISceneTargetingInteraction description];
-[_UISceneTargetingInteraction appendDescriptionToStream:];
-[_UISceneTargetingInteraction didMoveToView:];
```
