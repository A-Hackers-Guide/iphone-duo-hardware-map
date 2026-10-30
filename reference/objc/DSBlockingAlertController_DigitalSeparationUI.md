# `DSBlockingAlertController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAlertController`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"DSNavigationController" _safetyCheckController;
@"UIViewController" _alertPresentingViewController;
```

## Properties

```
@property (T@"DSNavigationController",&,N,V_safetyCheckController) safetyCheckController;
@property (T@"UIViewController",&,N,V_alertPresentingViewController) alertPresentingViewController;
```

## Class methods

```
+[DSBlockingAlertController emergencyContactAlertControllerWithFetchResult:];
+[DSBlockingAlertController sharingAlertControllerWithFetchResult:];
```

## Instance methods

```
-[DSBlockingAlertController viewDidAppear:];
-[DSBlockingAlertController viewDidDisappear:];
-[DSBlockingAlertController alertPresentingViewController];
-[DSBlockingAlertController emergencyContactOKHandlerWithFetchResult:];
-[DSBlockingAlertController safetyCheckController];
-[DSBlockingAlertController setAlertPresentingViewController:];
-[DSBlockingAlertController setSafetyCheckController:];
-[DSBlockingAlertController showSafetyCheckHandler];
```
