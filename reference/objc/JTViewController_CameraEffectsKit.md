# `JTViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 4 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _debuggingUIEnabled;
@"UIViewController" _viewControllerDrivingStatusAppearance;
@"NSMutableDictionary" _suspendedChildViewControllerRequests;
@"NSMutableArray" _suspendInteractionTags;
```

## Properties

```
@property (T@"JTView",&,N) view;
@property (T@"NSMutableDictionary",&,N,V_suspendedChildViewControllerRequests) suspendedChildViewControllerRequests;
@property (T@"NSMutableArray",&,N,V_suspendInteractionTags) suspendInteractionTags;
@property (TB,V_debuggingUIEnabled) debuggingUIEnabled;
@property (T@"UIViewController",&,N,V_viewControllerDrivingStatusAppearance) viewControllerDrivingStatusAppearance;
```

## Instance methods

```
-[JTViewController viewDidLoad];
-[JTViewController setView:];
-[JTViewController prefersHomeIndicatorAutoHidden];
-[JTViewController view];
-[JTViewController viewDidAppear:];
-[JTViewController viewDidDisappear:];
-[JTViewController prefersStatusBarHidden];
-[JTViewController debuggingUIEnabled];
-[JTViewController logSuspendedChildViewControllersToString:indentLevel:];
-[JTViewController logSuspendedViewControllers];
-[JTViewController resumeInteractionForChildViewControllersWithTag:];
-[JTViewController resumeInteractionWithTag:];
-[JTViewController setChildViewControllerInteractionEnabledWithRequest:enabled:];
-[JTViewController setDebuggingUIEnabled:];
-[JTViewController setSuspendInteractionTags:];
-[JTViewController setSuspendedChildViewControllerRequests:];
-[JTViewController setViewControllerDrivingStatusAppearance:];
-[JTViewController suspendChildViewControllersInteractionWithTag:timeout:excluding:];
-[JTViewController suspendInteractionTags];
-[JTViewController suspendInteractionWithTag:];
-[JTViewController suspendedChildViewControllerRequests];
-[JTViewController timeoutInteractionSuspended:];
-[JTViewController viewControllerDrivingStatusAppearance];
```
