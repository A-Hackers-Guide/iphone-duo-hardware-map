# `_UIPlaybackControlsStateManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"UIScene" _scene;
@"NSHashTable" _fullscreenPlaybackAssertions;
@"NSHashTable" _controlsPresentedAssertions;
```

## Properties

```
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPlaybackControlsStateManager _scene];
-[_UIPlaybackControlsStateManager initWithScene:];
-[_UIPlaybackControlsStateManager _setScene:];
-[_UIPlaybackControlsStateManager _beginFullscreenPlaybackSession];
-[_UIPlaybackControlsStateManager _beginPresentingPlaybackControls];
```
