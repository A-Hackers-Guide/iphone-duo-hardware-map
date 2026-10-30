# `_UIMenuPresentationSourceSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSTimer" _timer;
@"UIScene" _scene;
@"_UIMenuPresentationSource" _lastMenuPresentationSource;
```

## Properties

```
@property (T@"_UIMenuPresentationSource",&,N,V_lastMenuPresentationSource) lastMenuPresentationSource;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMenuPresentationSourceSceneComponent sceneComponentForView:];
```

## Instance methods

```
-[_UIMenuPresentationSourceSceneComponent _scene];
-[_UIMenuPresentationSourceSceneComponent setPresentationSource:];
-[_UIMenuPresentationSourceSceneComponent _sceneWillInvalidate:];
-[_UIMenuPresentationSourceSceneComponent initWithScene:];
-[_UIMenuPresentationSourceSceneComponent _cancelTimer];
-[_UIMenuPresentationSourceSceneComponent _setScene:];
-[_UIMenuPresentationSourceSceneComponent clearPresentationSource:];
-[_UIMenuPresentationSourceSceneComponent lastMenuPresentationSource];
-[_UIMenuPresentationSourceSceneComponent scheduleClearPresentationSourceForSource:];
-[_UIMenuPresentationSourceSceneComponent setLastMenuPresentationSource:];
```
