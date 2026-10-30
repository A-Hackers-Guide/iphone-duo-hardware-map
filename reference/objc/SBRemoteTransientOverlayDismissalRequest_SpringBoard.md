# `SBRemoteTransientOverlayDismissalRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _shouldInvalidatePresentation;
@? _completionHandler;
@"SBTransientOverlayViewController" _viewController;
```

## Properties

```
@property (TB,N,GisAnimated,V_animated) animated;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (TB,N,V_shouldInvalidatePresentation) shouldInvalidatePresentation;
@property (T@"SBTransientOverlayViewController",R,N,V_viewController) viewController;
```

## Instance methods

```
-[SBRemoteTransientOverlayDismissalRequest initWithViewController:];
-[SBRemoteTransientOverlayDismissalRequest setCompletionHandler:];
-[SBRemoteTransientOverlayDismissalRequest completionHandler];
-[SBRemoteTransientOverlayDismissalRequest isAnimated];
-[SBRemoteTransientOverlayDismissalRequest setAnimated:];
-[SBRemoteTransientOverlayDismissalRequest viewController];
-[SBRemoteTransientOverlayDismissalRequest copyWithZone:];
-[SBRemoteTransientOverlayDismissalRequest setShouldInvalidatePresentation:];
-[SBRemoteTransientOverlayDismissalRequest shouldInvalidatePresentation];
```
