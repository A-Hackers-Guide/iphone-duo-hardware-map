# `_UIKeyWindowSceneObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventDeliveryPolicyObserving`, `_UIWindowHostingSceneComponentProviding`
- 4 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_UIKeyWindowEvaluator" _keyWindowEvaluator;
@"BKSHIDEventDeliveryPolicyObserver" _hidPolicyObserver;
{?="sceneIsObservable"b1} _observerFlags;
@"UIScene" _scene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
```

## Instance methods

```
-[_UIKeyWindowSceneObserver observerDeliveryPolicyDidChange:];
-[_UIKeyWindowSceneObserver _windowHostingScene:didMoveFromScreen:toScreen:];
-[_UIKeyWindowSceneObserver _scene:willTransitionToActivationState:withReasonsMask:];
-[_UIKeyWindowSceneObserver _scene];
-[_UIKeyWindowSceneObserver _windowHostingScene:willMoveFromScreen:toScreen:];
-[_UIKeyWindowSceneObserver init];
-[_UIKeyWindowSceneObserver _sceneWillInvalidate:];
-[_UIKeyWindowSceneObserver initWithScene:];
-[_UIKeyWindowSceneObserver _settingsDiffActionsForScene:];
-[_UIKeyWindowSceneObserver description];
-[_UIKeyWindowSceneObserver _setScene:];
```
