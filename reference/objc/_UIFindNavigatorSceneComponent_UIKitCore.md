# `_UIFindNavigatorSceneComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFindNavigatorViewControllerDelegate`, `_UIViewSubtreeMonitor`, `_UISceneComponentProviding`, `_UIFindNavigatorHosting`
- 3 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"UIScene" _scene;
@"_UIFindNavigatorResponder" _findNavigatorResponder;
@"_UIFindNavigatorViewController" _findNavigatorViewController;
```

## Properties

```
@property (T@"_UIFindNavigatorResponder",&,N,V_findNavigatorResponder) findNavigatorResponder;
@property (T@"_UIFindNavigatorViewController",&,N,V_findNavigatorViewController) findNavigatorViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene",W,N,G_scene,S_setScene:,V_scene) _scene;
@property (TB,R,N,GisFindNavigatorVisible) findNavigatorVisible;
```

## Class methods

```
+[_UIFindNavigatorSceneComponent sceneComponentForView:];
```

## Instance methods

```
-[_UIFindNavigatorSceneComponent _scene];
-[_UIFindNavigatorSceneComponent initWithScene:];
-[_UIFindNavigatorSceneComponent _monitoredView:didMoveFromSuperview:toSuperview:];
-[_UIFindNavigatorSceneComponent _monitoredView:willMoveFromSuperview:toSuperview:];
-[_UIFindNavigatorSceneComponent _monitorsView:];
-[_UIFindNavigatorSceneComponent _setScene:];
-[_UIFindNavigatorSceneComponent isFindNavigatorVisible];
-[_UIFindNavigatorSceneComponent _searchableView];
-[_UIFindNavigatorSceneComponent setFindNavigatorViewController:];
-[_UIFindNavigatorSceneComponent _keyboardIsPreservingFindNavigatorAsRestorableResponder];
-[_UIFindNavigatorSceneComponent _sendPlacementUpdate];
-[_UIFindNavigatorSceneComponent dismissFindNavigatorEndingActiveSession:];
-[_UIFindNavigatorSceneComponent findNavigatorResponder];
-[_UIFindNavigatorSceneComponent findNavigatorShouldDismissOnResponderChange:];
-[_UIFindNavigatorSceneComponent findNavigatorViewController];
-[_UIFindNavigatorSceneComponent findNavigatorViewControllerDidRequestDismissal:];
-[_UIFindNavigatorSceneComponent findNavigatorViewControllerViewDidChangeIntrinsicContentSize:];
-[_UIFindNavigatorSceneComponent presentFindNavigatorWithFindSession:showingReplace:idiom:];
-[_UIFindNavigatorSceneComponent setFindNavigatorResponder:];
```
