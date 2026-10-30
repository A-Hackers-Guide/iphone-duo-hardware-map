# `UIWindowController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 6 properties, 29 instance methods, 2 class methods

## Instance variables

```
@"UITransitionView" _transitionView;
@"UIWindow" _window;
i _currentTransition;
@ _target;
q _didFinish;
@"UIViewController" _fromViewController;
@"UIViewController" _toViewController;
{CGPoint="x"d"y"d} _beginOriginForToView;
{CGPoint="x"d"y"d} _endOriginForToView;
B _presenting;
q _toModalStyle;
B _needsDidAppear;
B _needsDidDisappear;
B __interactiveTransition;
@"<UIViewControllerAnimatedTransitioning>" _transitionController;
@"<UIViewControllerInteractiveTransitioning>" _interactionController;
```

## Properties

```
@property (T@"UIWindow",W,N,V_window) window;
@property (T@"UITransitionView",R,N,V_transitionView) transitionView;
@property (TB,N,V_presenting) presenting;
@property (T@"<UIViewControllerAnimatedTransitioning>",&,N,S_setTransitionController:,V_transitionController) _transitionController;
@property (T@"<UIViewControllerInteractiveTransitioning>",&,N,S_setInteractionController:,V_interactionController) _interactionController;
@property (TB,N,G_isInteractiveTransition,S_setInteractiveTransition:,V__interactiveTransition) _interactiveTransition;
```

## Class methods

```
+[UIWindowController windowControllerForWindow:];
+[UIWindowController windowWillBeDeallocated:];
```

## Instance methods

```
-[UIWindowController _transitionController];
-[UIWindowController transitionViewShouldUseViewControllerCallbacks];
-[UIWindowController _interactionController];
-[UIWindowController _prepareKeyboardForTransition:fromView:];
-[UIWindowController dealloc];
-[UIWindowController window];
-[UIWindowController transitionView:endOriginForToView:forTransition:defaultOrigin:];
-[UIWindowController durationForTransition:];
-[UIWindowController _adjustOrigin:givenOtherOrigin:forTransition:];
-[UIWindowController transitionView:endOriginForFromView:forTransition:defaultOrigin:];
-[UIWindowController transitionView:beginOriginForToView:forTransition:defaultOrigin:];
-[UIWindowController transitionViewDidStart:];
-[UIWindowController transitionView:startCustomTransitionWithDuration:];
-[UIWindowController setWindow:];
-[UIWindowController transitionViewDidComplete:fromView:toView:removeFromView:];
-[UIWindowController setPresenting:];
-[UIWindowController _boundsForViewController:transition:orientation:fullScreenLayout:inWindow:];
-[UIWindowController _flipSize:];
-[UIWindowController _isInteractiveTransition];
-[UIWindowController _originForViewController:orientation:actualStatusBarHeight:fullScreenLayout:inWindow:];
-[UIWindowController _setInteractionController:];
-[UIWindowController _setInteractiveTransition:];
-[UIWindowController _setTransitionController:];
-[UIWindowController _transition:fromViewController:toViewController:target:didFinish:];
-[UIWindowController _transition:fromViewController:toViewController:target:didFinish:animation:];
-[UIWindowController _transplantView:toSuperview:atIndex:];
-[UIWindowController presenting];
-[UIWindowController transitionView];
-[UIWindowController transitionViewDidCancel:fromView:toView:];
```
