# `_UIEditMenuSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"UIScene" _scene;
@"_UIEditMenuPresentation" _activePresentation;
```

## Properties

```
@property (T@"_UIEditMenuPresentation",R,N,V_activePresentation) activePresentation;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIEditMenuSceneComponent sceneComponentForView:];
```

## Instance methods

```
-[_UIEditMenuSceneComponent _scene];
-[_UIEditMenuSceneComponent activePresentation];
-[_UIEditMenuSceneComponent dismissCurrentMenu];
-[_UIEditMenuSceneComponent hasVisibleMenu];
-[_UIEditMenuSceneComponent initWithScene:];
-[_UIEditMenuSceneComponent setActivePresentation:];
-[_UIEditMenuSceneComponent updateCurrentMenuPositionAnimated:];
-[_UIEditMenuSceneComponent removeActivePresentation:];
-[_UIEditMenuSceneComponent _setScene:];
```
