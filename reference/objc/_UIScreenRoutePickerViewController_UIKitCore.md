# `_UIScreenRoutePickerViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIAlertControllerContaining`, `UIPopoverPresentationControllerDelegate`
- 3 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"UIAlertController" _alertController;
@"_UIResilientRemoteViewContainerViewController" _childViewController;
@"NSObject<OS_dispatch_semaphore>" _remoteViewControllerSemaphore;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIScreenRoutePickerViewController adaptivePresentationStyleForPresentationController:traitCollection:];
-[_UIScreenRoutePickerViewController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIScreenRoutePickerViewController init];
-[_UIScreenRoutePickerViewController dealloc];
-[_UIScreenRoutePickerViewController remoteViewController];
-[_UIScreenRoutePickerViewController initWithNibName:bundle:];
-[_UIScreenRoutePickerViewController setModalPresentationStyle:];
-[_UIScreenRoutePickerViewController initWithCoder:];
-[_UIScreenRoutePickerViewController modalPresentationStyle];
-[_UIScreenRoutePickerViewController disconnectRoute];
-[_UIScreenRoutePickerViewController _addCustomChildViewController:];
-[_UIScreenRoutePickerViewController _commonInitWithCompletion:];
-[_UIScreenRoutePickerViewController _containedAlertController];
-[_UIScreenRoutePickerViewController _presentationControllerForPresentedController:presentingController:sourceController:];
-[_UIScreenRoutePickerViewController _requiresCustomPresentationController];
-[_UIScreenRoutePickerViewController _setChildViewController:];
-[_UIScreenRoutePickerViewController setCurrentOutputDeviceEnabled:];
```
