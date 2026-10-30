# `UIPointerLockState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 2 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _status;
@"UIScene" _scene;
```

## Properties

```
@property (TB,R,D,N,GisLocked) locked;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPointerLockState _windowScene];
-[UIPointerLockState isLocked];
-[UIPointerLockState _scene];
-[UIPointerLockState initWithScene:];
-[UIPointerLockState _settingsDiffActionsForScene:];
-[UIPointerLockState windowHostingScene];
-[UIPointerLockState _setScene:];
-[UIPointerLockState _pointerLockStatusUpdated];
-[UIPointerLockState _preferredPointerLockStatusUpdated];
```
