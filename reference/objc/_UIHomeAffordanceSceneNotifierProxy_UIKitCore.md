# `_UIHomeAffordanceSceneNotifierProxy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIHomeAffordanceNotifyingInternal`, `_UIHomeAffordanceObserver`, `_UIHomeAffordanceNotifying`
- 7 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
{?="hasInvalidated"b1} _flags;
@"<BSInvalidatable>" _stateCaptureToken;
@"UIScene" _scene;
@"NSMutableSet" _registeredObserverRecords;
@"<_UIInvalidatable>" _targetNotifierRegistrationToken;
@"<_UIHomeAffordanceNotifying>" _targetHomeAffordanceNotifier;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastReceivedHomeAffordanceSceneReferenceFrame;
```

## Properties

```
@property (TB,R,N) _hasInvalidated;
@property (T@"NSMutableSet",R,C,N,V_registeredObserverRecords) _registeredObserverRecords;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,W,N) windowHostingScene;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHomeAffordanceSceneNotifierProxy _notifier:homeAffordanceFrameDidChange:];
-[_UIHomeAffordanceSceneNotifierProxy _notifier:homeAffordanceDoubleTapGestureDidSucceed:];
-[_UIHomeAffordanceSceneNotifierProxy _reset];
-[_UIHomeAffordanceSceneNotifierProxy _scene];
-[_UIHomeAffordanceSceneNotifierProxy debugDescription];
-[_UIHomeAffordanceSceneNotifierProxy cleanupForDetachingWindow:];
-[_UIHomeAffordanceSceneNotifierProxy init];
-[_UIHomeAffordanceSceneNotifierProxy _registeredObserverRecords];
-[_UIHomeAffordanceSceneNotifierProxy _sceneWillInvalidate:];
-[_UIHomeAffordanceSceneNotifierProxy dealloc];
-[_UIHomeAffordanceSceneNotifierProxy initWithScene:];
-[_UIHomeAffordanceSceneNotifierProxy homeAffordanceSceneReferenceFrameForWindow:];
-[_UIHomeAffordanceSceneNotifierProxy succinctDescription];
-[_UIHomeAffordanceSceneNotifierProxy _hasInvalidated];
-[_UIHomeAffordanceSceneNotifierProxy windowHostingScene];
-[_UIHomeAffordanceSceneNotifierProxy description];
-[_UIHomeAffordanceSceneNotifierProxy registerHomeAffordanceObserver:inWindow:];
-[_UIHomeAffordanceSceneNotifierProxy appendDescriptionToStream:];
-[_UIHomeAffordanceSceneNotifierProxy _setScene:];
-[_UIHomeAffordanceSceneNotifierProxy _unregisterHomeAffordanceObserverForRecord:];
-[_UIHomeAffordanceSceneNotifierProxy _targetNotifierSceneDidDisconnect:];
-[_UIHomeAffordanceSceneNotifierProxy _targetNotifierSceneDidMoveToScreen:];
-[_UIHomeAffordanceSceneNotifierProxy _windowDidBecomeAppKeyNotification:];
-[_UIHomeAffordanceSceneNotifierProxy _windowDidResignAppKeyNotification:];
```
