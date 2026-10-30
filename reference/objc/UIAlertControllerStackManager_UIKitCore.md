# `UIAlertControllerStackManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneComponentProviding`
- 3 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _alertControllerStack;
@"NSMutableArray" _hiddenAlertControllers;
@"UIScene" _scene;
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
-[UIAlertControllerStackManager _addAlertControllerToStack:];
-[UIAlertControllerStackManager _scene];
-[UIAlertControllerStackManager _alertControllerWillDisappear:];
-[UIAlertControllerStackManager _didHideAlertController:];
-[UIAlertControllerStackManager initWithScene:];
-[UIAlertControllerStackManager _willShowAlertController:];
-[UIAlertControllerStackManager _alertControllerStackCount];
-[UIAlertControllerStackManager _willHideAlertController:];
-[UIAlertControllerStackManager _removeAlertControllerFromStack:];
-[UIAlertControllerStackManager _hideStackedAlertControllers];
-[UIAlertControllerStackManager _alertControllerDidDisappear:];
-[UIAlertControllerStackManager _setScene:];
-[UIAlertControllerStackManager _alertControllerShouldBeTrackedInStack:];
-[UIAlertControllerStackManager _showHiddenStackedAlertControllers];
-[UIAlertControllerStackManager _alertControllerWillAppear:];
-[UIAlertControllerStackManager _topAlertControllerInStack];
-[UIAlertControllerStackManager _alertControllerDidAppear:];
```
