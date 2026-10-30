# `SBRemoteTransientOverlayPresentationRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _isScreenshotMarkup;
B _shouldDismissSiri;
B _shouldDismissPresentedBanners;
B _shouldStashPictureInPictureIfNeeded;
B _shouldPresentEmbeddedInTargetScene;
B _isSceneBacked;
@"SBTransientOverlayViewController" _viewController;
@"SBSRemoteAlertPresentationTarget" _presentationTarget;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBTransientOverlayViewController",R,N,V_viewController) viewController;
@property (TB,N,GisAnimated,V_animated) animated;
@property (T@"SBSRemoteAlertPresentationTarget",&,N,V_presentationTarget) presentationTarget;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TB,N,V_isScreenshotMarkup) isScreenshotMarkup;
@property (TB,N,V_shouldDismissSiri) shouldDismissSiri;
@property (TB,N,V_shouldDismissPresentedBanners) shouldDismissPresentedBanners;
@property (TB,N,V_shouldStashPictureInPictureIfNeeded) shouldStashPictureInPictureIfNeeded;
@property (TB,N,V_shouldPresentEmbeddedInTargetScene) shouldPresentEmbeddedInTargetScene;
@property (TB,N,V_isSceneBacked) isSceneBacked;
```

## Instance methods

```
-[SBRemoteTransientOverlayPresentationRequest initWithViewController:];
-[SBRemoteTransientOverlayPresentationRequest shouldDismissPresentedBanners];
-[SBRemoteTransientOverlayPresentationRequest setWindowScene:];
-[SBRemoteTransientOverlayPresentationRequest shouldStashPictureInPictureIfNeeded];
-[SBRemoteTransientOverlayPresentationRequest presentationTarget];
-[SBRemoteTransientOverlayPresentationRequest setShouldStashPictureInPictureIfNeeded:];
-[SBRemoteTransientOverlayPresentationRequest shouldDismissSiri];
-[SBRemoteTransientOverlayPresentationRequest isAnimated];
-[SBRemoteTransientOverlayPresentationRequest isScreenshotMarkup];
-[SBRemoteTransientOverlayPresentationRequest setShouldDismissSiri:];
-[SBRemoteTransientOverlayPresentationRequest isSceneBacked];
-[SBRemoteTransientOverlayPresentationRequest setAnimated:];
-[SBRemoteTransientOverlayPresentationRequest setPresentationTarget:];
-[SBRemoteTransientOverlayPresentationRequest viewController];
-[SBRemoteTransientOverlayPresentationRequest setIsSceneBacked:];
-[SBRemoteTransientOverlayPresentationRequest setShouldDismissPresentedBanners:];
-[SBRemoteTransientOverlayPresentationRequest setShouldPresentEmbeddedInTargetScene:];
-[SBRemoteTransientOverlayPresentationRequest shouldPresentEmbeddedInTargetScene];
-[SBRemoteTransientOverlayPresentationRequest copyWithZone:];
-[SBRemoteTransientOverlayPresentationRequest windowScene];
-[SBRemoteTransientOverlayPresentationRequest setIsScreenshotMarkup:];
```
