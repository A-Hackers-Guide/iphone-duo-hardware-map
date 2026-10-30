# `UIDebuggingInformationOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UISplitViewControllerDelegate`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIDebuggingInformationContainerView" _shadowContainer;
@"UINavigationController" _navController;
B _isFullscreen;
@"UIDebuggingInformationRootTableViewController" _rootTableViewController;
{CGPoint="x"d"y"d} _offset;
```

## Properties

```
@property (T{CGPoint=dd},V_offset) offset;
@property (T@"UIView",R,N) containerView;
@property (T@"UIDebuggingInformationRootTableViewController",&,N,V_rootTableViewController) rootTableViewController;
@property (TB,N,V_isFullscreen) isFullscreen;
```

## Instance methods

```
-[UIDebuggingInformationOverlayViewController isFullscreen];
-[UIDebuggingInformationOverlayViewController viewDidLayoutSubviews];
-[UIDebuggingInformationOverlayViewController initWithNibName:bundle:];
-[UIDebuggingInformationOverlayViewController containerView];
-[UIDebuggingInformationOverlayViewController setOffset:];
-[UIDebuggingInformationOverlayViewController offset];
-[UIDebuggingInformationOverlayViewController didReceiveGesture:];
-[UIDebuggingInformationOverlayViewController rootTableViewController];
-[UIDebuggingInformationOverlayViewController setIsFullscreen:];
-[UIDebuggingInformationOverlayViewController setRootTableViewController:];
-[UIDebuggingInformationOverlayViewController toggleFullscreen];
```
