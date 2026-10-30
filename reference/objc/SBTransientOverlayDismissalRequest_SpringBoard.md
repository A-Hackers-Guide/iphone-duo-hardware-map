# `SBTransientOverlayDismissalRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 6 instance variables, 6 properties, 10 instance methods, 3 class methods

## Instance variables

```
B _animated;
@? _completionHandler;
B _preserveViewControllersMovingToNewWindowScene;
q _requestType;
@"SBTransientOverlayViewController" _viewController;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TB,R,N,GisAnimated,V_animated) animated;
@property (T@?,R,C,N,V_completionHandler) completionHandler;
@property (Tq,R,N,V_requestType) requestType;
@property (T@"SBTransientOverlayViewController",R,N,V_viewController) viewController;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N,V_preserveViewControllersMovingToNewWindowScene) preserveViewControllersMovingToNewWindowScene;
```

## Class methods

```
+[SBTransientOverlayDismissalRequest dismissalRequestForAllViewControllers];
+[SBTransientOverlayDismissalRequest dismissalRequestForAllViewControllersInWindowScene:];
+[SBTransientOverlayDismissalRequest dismissalRequestForViewController:];
```

## Instance methods

```
-[SBTransientOverlayDismissalRequest requestType];
-[SBTransientOverlayDismissalRequest mutableCopyWithZone:];
-[SBTransientOverlayDismissalRequest completionHandler];
-[SBTransientOverlayDismissalRequest isAnimated];
-[SBTransientOverlayDismissalRequest viewController];
-[SBTransientOverlayDismissalRequest _init];
-[SBTransientOverlayDismissalRequest copyWithZone:];
-[SBTransientOverlayDismissalRequest windowScene];
-[SBTransientOverlayDismissalRequest _copyWithClass:];
-[SBTransientOverlayDismissalRequest preserveViewControllersMovingToNewWindowScene];
```
