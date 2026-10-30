# `_UIZoomViewControllerTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewControllerTransition`
- 3 instance variables, 3 properties, 13 instance methods, 2 class methods

## Instance variables

```
@? __viewProvider;
@"UIZoomTransitionOptions" __options;
@"UIViewController" __associatedViewController;
```

## Properties

```
@property (T@"UIViewController",W,N,V__associatedViewController) _associatedViewController;
@property (T@?,C,N,V__viewProvider) _viewProvider;
@property (T@"UIZoomTransitionOptions",&,N,V__options) _options;
```

## Class methods

```
+[_UIZoomViewControllerTransition _zoomWithOptions:sourceItemProvider:];
+[_UIZoomViewControllerTransition zoomWithOptions:sourceViewProvider:];
```

## Instance methods

```
-[_UIZoomViewControllerTransition _options];
-[_UIZoomViewControllerTransition _hasOwnInteractiveExitGestureForTraits:];
-[_UIZoomViewControllerTransition _didDismissViewController:];
-[_UIZoomViewControllerTransition _viewProvider];
-[_UIZoomViewControllerTransition _wasAssignedToViewController:];
-[_UIZoomViewControllerTransition set_options:];
-[_UIZoomViewControllerTransition _isSupportedGivenTraits:];
-[_UIZoomViewControllerTransition _associatedViewController];
-[_UIZoomViewControllerTransition set_viewProvider:];
-[_UIZoomViewControllerTransition _preferredModalPresentationStyle];
-[_UIZoomViewControllerTransition _didMoveToParentViewController:];
-[_UIZoomViewControllerTransition set_associatedViewController:];
-[_UIZoomViewControllerTransition _transitionControllerForViewController:traits:isAppearing:];
```
