# `_UIHDRUsageCoordinatorSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIWindowSceneComponentProviding`
- 2 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="isAttachedToWindowScene"b1"canUpdateTraitOverrides"b1"sceneHasScreen"b1"isActive"b1"isOccludedByOtherApp"b1"isOccludedBySystemApp"b1} _flags;
@"UIScene" _scene;
```

## Properties

```
@property (T@"UITraitCollection",?,R,N) _traitOverrides;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHDRUsageCoordinatorSceneComponent _scene:willTransitionToActivationState:withReasonsMask:];
-[_UIHDRUsageCoordinatorSceneComponent _scene];
-[_UIHDRUsageCoordinatorSceneComponent _traitOverrides];
-[_UIHDRUsageCoordinatorSceneComponent _setSystemOcclusionRects:];
-[_UIHDRUsageCoordinatorSceneComponent dealloc];
-[_UIHDRUsageCoordinatorSceneComponent _setApplicationOcclusionRects:];
-[_UIHDRUsageCoordinatorSceneComponent initWithScene:];
-[_UIHDRUsageCoordinatorSceneComponent _invalidateTraitOverrides];
-[_UIHDRUsageCoordinatorSceneComponent _settingsDiffActionsForScene:];
-[_UIHDRUsageCoordinatorSceneComponent _powerStateDidChange:];
-[_UIHDRUsageCoordinatorSceneComponent _setScene:];
```
