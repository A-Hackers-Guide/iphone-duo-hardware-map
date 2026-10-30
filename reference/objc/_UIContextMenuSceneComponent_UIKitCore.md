# `_UIContextMenuSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"UIScene" _scene;
@"NSMutableSet" _activePresentations;
@"NSMutableSet" _outgoingPresentations;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_activePresentations) activePresentations;
@property (T@"NSMutableSet",&,N,V_outgoingPresentations) outgoingPresentations;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIContextMenuSceneComponent sceneComponentForView:];
```

## Instance methods

```
-[_UIContextMenuSceneComponent registerPresentation:];
-[_UIContextMenuSceneComponent addDismissalCompletion:];
-[_UIContextMenuSceneComponent _scene];
-[_UIContextMenuSceneComponent removePresentation:];
-[_UIContextMenuSceneComponent setActivePresentations:];
-[_UIContextMenuSceneComponent initWithScene:];
-[_UIContextMenuSceneComponent outgoingPresentations];
-[_UIContextMenuSceneComponent activePresentations];
-[_UIContextMenuSceneComponent _setScene:];
-[_UIContextMenuSceneComponent dismissActiveMenus];
-[_UIContextMenuSceneComponent removePresentationOnDismissal:];
-[_UIContextMenuSceneComponent setOutgoingPresentations:];
```
