# `_UISceneHingeStateClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `FBSSceneObserver`, `_UISceneHingeStateClient`, `_UISceneInteractionRegistrationTarget`
- 6 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
{?="hasReceivedHingeState"b1"hasReceivedSceneHingeStateUpdate"b1} _flags;
@"<BSInvalidatable>" _stateCaptureToken;
@"NSHashTable" _observerRegistrations;
@"<_UISceneHingeStateClientObserver>" _observerPendingInitialDelivery;
@"_UISceneHingeState" _sceneHingeState;
@"UIScene<_UISceneUIWindowHosting>" _windowHostingScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UISceneHingeState",R,C,N,V_sceneHingeState) sceneHingeState;
@property (T@"_UIHingeState",R,N) hingeState;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,N,V_windowHostingScene) _windowHostingScene;
```

## Instance methods

```
-[_UISceneHingeStateClientComponent _windowHostingScene];
-[_UISceneHingeStateClientComponent debugDescription];
-[_UISceneHingeStateClientComponent removeObserver:];
-[_UISceneHingeStateClientComponent scene:didUpdateSettings:];
-[_UISceneHingeStateClientComponent setScene:];
-[_UISceneHingeStateClientComponent succinctDescription];
-[_UISceneHingeStateClientComponent addObserver:];
-[_UISceneHingeStateClientComponent invalidate];
-[_UISceneHingeStateClientComponent description];
-[_UISceneHingeStateClientComponent appendDescriptionToStream:];
-[_UISceneHingeStateClientComponent registerObserver:];
-[_UISceneHingeStateClientComponent hingeState];
-[_UISceneHingeStateClientComponent sceneHingeState];
```
