# `UIHingeInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `_UISceneHingeStateClientObserver`, `UIInteraction`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@? _updateHandler;
B _enabled;
@"UIView" _view;
@"_UISceneTargetingInteraction" _registrationInteraction;
@"<BSInvalidatable>" _observationToken;
@"UIHingeInteractionUpdate" _lastUpdate;
```

## Properties

```
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[UIHingeInteraction initWithUpdateHandler:];
-[UIHingeInteraction debugDescription];
-[UIHingeInteraction init];
-[UIHingeInteraction dealloc];
-[UIHingeInteraction isEnabled];
-[UIHingeInteraction succinctDescription];
-[UIHingeInteraction view];
-[UIHingeInteraction _windowWillMoveToNilScene:];
-[UIHingeInteraction setEnabled:];
-[UIHingeInteraction willMoveToView:];
-[UIHingeInteraction description];
-[UIHingeInteraction appendDescriptionToStream:];
-[UIHingeInteraction didMoveToView:];
-[UIHingeInteraction _updateForSceneHingeState:];
-[UIHingeInteraction sceneHingeStateClientComponent:didUpdateFromHingeState:toHingeState:];
-[UIHingeInteraction wantsCurrentHingeStateOnRegistration];
```
