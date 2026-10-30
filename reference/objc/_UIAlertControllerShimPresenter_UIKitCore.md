# `_UIAlertControllerShimPresenter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPopoverControllerDelegate`
- 6 instance variables, 8 properties, 16 instance methods, 5 class methods

## Instance variables

```
@"UIPopoverController" _popoverController;
@"<UIPopoverControllerDelegate>" _popoverDelegate;
@"UIViewController" _inPopoverViewController;
@"_UIAlertControllerShimPresenterWindow" _window;
@"UIAlertController" _alertController;
@"UIAlertView" _legacyAlert;
```

## Properties

```
@property (T@"UIAlertController",W,N,V_alertController) alertController;
@property (T@"UIAlertView",N,V_legacyAlert) legacyAlert;
@property (T@"_UIAlertControllerShimPresenterWindow",R,N,V_window) window;
@property (T@"<UIPopoverControllerDelegate>",W,N) popoverDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIAlertControllerShimPresenter _addPresenter:];
+[_UIAlertControllerShimPresenter _cancelPendingTouchesIfAppropriateForWindow:];
+[_UIAlertControllerShimPresenter _currentFullScreenAlertPresenters];
+[_UIAlertControllerShimPresenter _removePresenter:];
+[_UIAlertControllerShimPresenter _shouldPresentActionSheetsFullscreen];
```

## Instance methods

```
-[_UIAlertControllerShimPresenter alertController];
-[_UIAlertControllerShimPresenter dealloc];
-[_UIAlertControllerShimPresenter window];
-[_UIAlertControllerShimPresenter setAlertController:];
-[_UIAlertControllerShimPresenter setLegacyAlert:];
-[_UIAlertControllerShimPresenter popoverDelegate];
-[_UIAlertControllerShimPresenter _createWindowIfNecessaryWithScene:];
-[_UIAlertControllerShimPresenter _dismissAlertControllerAnimated:completion:];
-[_UIAlertControllerShimPresenter _popoverController];
-[_UIAlertControllerShimPresenter _presentAlertControllerAnimated:completion:];
-[_UIAlertControllerShimPresenter _presentAlertControllerAnimated:hostingScene:completion:];
-[_UIAlertControllerShimPresenter _presentAlertControllerFromBarButtonItem:animated:completion:];
-[_UIAlertControllerShimPresenter _presentAlertControllerFromRect:inView:direction:animated:completion:];
-[_UIAlertControllerShimPresenter _tearDownInPopoverViewController];
-[_UIAlertControllerShimPresenter legacyAlert];
-[_UIAlertControllerShimPresenter setPopoverDelegate:];
```
