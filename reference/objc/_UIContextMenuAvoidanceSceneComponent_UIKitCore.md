# `_UIContextMenuAvoidanceSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIAssertionControllerSubject`, `_UISceneComponentProviding`
- 4 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
Q _assertionID;
@"UIScene" _scene;
@"NSMutableDictionary" _avoidanceRects;
@"_UIAssertionController" _assertionController;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_avoidanceRects) avoidanceRects;
@property (T@"_UIAssertionController",R,N,V_assertionController) assertionController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
```

## Class methods

```
+[_UIContextMenuAvoidanceSceneComponent sceneComponentForView:];
```

## Instance methods

```
-[_UIContextMenuAvoidanceSceneComponent assertionController];
-[_UIContextMenuAvoidanceSceneComponent assertionActivationStateForType:];
-[_UIContextMenuAvoidanceSceneComponent removeAvoidanceRectForKey:];
-[_UIContextMenuAvoidanceSceneComponent _scene];
-[_UIContextMenuAvoidanceSceneComponent initWithScene:];
-[_UIContextMenuAvoidanceSceneComponent _overlapInsetsInCoordinateSpace:];
-[_UIContextMenuAvoidanceSceneComponent _nextAssertionID];
-[_UIContextMenuAvoidanceSceneComponent assertionActivationStateChangedToState:forType:];
-[_UIContextMenuAvoidanceSceneComponent _setScene:];
-[_UIContextMenuAvoidanceSceneComponent addAvoidanceRect:forKey:];
-[_UIContextMenuAvoidanceSceneComponent avoidanceRects];
```
