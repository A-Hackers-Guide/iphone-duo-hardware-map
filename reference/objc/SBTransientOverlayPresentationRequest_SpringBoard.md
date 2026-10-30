# `SBTransientOverlayPresentationRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _animated;
@? _completionHandler;
B _shouldDismissSiri;
@"SBTransientOverlayViewController" _viewController;
@"BSProcessHandle" _originatingProcess;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TB,R,N,GisAnimated,V_animated) animated;
@property (T@?,R,C,N,V_completionHandler) completionHandler;
@property (TB,R,N,V_shouldDismissSiri) shouldDismissSiri;
@property (T@"SBTransientOverlayViewController",R,N,V_viewController) viewController;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"BSProcessHandle",R,N,V_originatingProcess) originatingProcess;
```

## Instance methods

```
-[SBTransientOverlayPresentationRequest initWithViewController:];
-[SBTransientOverlayPresentationRequest mutableCopyWithZone:];
-[SBTransientOverlayPresentationRequest completionHandler];
-[SBTransientOverlayPresentationRequest shouldDismissSiri];
-[SBTransientOverlayPresentationRequest isAnimated];
-[SBTransientOverlayPresentationRequest originatingProcess];
-[SBTransientOverlayPresentationRequest viewController];
-[SBTransientOverlayPresentationRequest copyWithZone:];
-[SBTransientOverlayPresentationRequest windowScene];
-[SBTransientOverlayPresentationRequest _copyWithClass:];
```
