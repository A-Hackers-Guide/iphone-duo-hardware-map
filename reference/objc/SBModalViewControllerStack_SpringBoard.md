# `SBModalViewControllerStack`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<SBModalViewControllerStackDelegate>" _delegate;
@"UIViewController" _presentingViewController;
@"NSMutableArray" _viewControllerStack;
@"_SBModalViewControllerStackTransition" _currentTransition;
@"NSMutableArray" _pendingTransitions;
```

## Properties

```
@property (T@"<SBModalViewControllerStackDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,D,N) viewControllers;
@property (T@"UIViewController",R,D,N) topViewController;
```

## Instance methods

```
-[SBModalViewControllerStack _setCurrentTransition:];
-[SBModalViewControllerStack _popNextPendingTransition];
-[SBModalViewControllerStack _noteDidDismissViewController:];
-[SBModalViewControllerStack _removePendingTransition:forSuccess:];
-[SBModalViewControllerStack _removeViewController:completion:];
-[SBModalViewControllerStack setDelegate:];
-[SBModalViewControllerStack _addPendingTransition:];
-[SBModalViewControllerStack initWithPresentingViewController:];
-[SBModalViewControllerStack _performPendingTransitionIfNecessary];
-[SBModalViewControllerStack delegate];
-[SBModalViewControllerStack removeViewControllerAnimated:completion:];
-[SBModalViewControllerStack _noteDidPresentViewController:];
-[SBModalViewControllerStack addViewController:animated:completion:];
-[SBModalViewControllerStack viewControllers];
-[SBModalViewControllerStack _queuePendingTransition:];
-[SBModalViewControllerStack topViewController];
-[SBModalViewControllerStack removeViewController:animated:completion:];
-[SBModalViewControllerStack _noteWillDismissViewController:animated:];
-[SBModalViewControllerStack _addViewController:completion:];
-[SBModalViewControllerStack _noteWillPresentViewController:];
```
