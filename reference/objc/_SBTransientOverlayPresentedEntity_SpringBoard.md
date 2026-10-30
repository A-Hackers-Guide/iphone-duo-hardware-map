# `_SBTransientOverlayPresentedEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 22 properties, 43 instance methods, 0 class methods

## Instance variables

```
B _rotating;
B _dismissing;
B _hasFinishedWindowInitialization;
B _hasPreservedInputViews;
d _baseWindowLevel;
@"SBTransientOverlayViewController" _viewController;
@"SBTransientOverlayBackgroundWindow" _backgroundWindow;
@"SBTransientOverlayWindow" _window;
Q _presentationSequence;
@"<BSInvalidatable>" _disableAutoUnlockAssertion;
@"<BSInvalidatable>" _proximityEnabledAssertion;
@"<BSInvalidatable>" _wallpaperAnimationSuspensionAssertion;
@"SBFluidDismissalState" _fluidDismissalState;
@"SBPresentationObservationToken" _bannerLongLookPresentationObservationToken;
@"<BSInvalidatable>" _bannerLongLookWindowLevelAssertion;
@"SBPresentationObservationToken" _controlCenterPresentationObservationToken;
@"<BSInvalidatable>" _controlCenterWindowLevelAssertion;
@"SBPresentationObservationToken" _siriPresentationObservationToken;
@"<BSInvalidatable>" _siriWindowLevelAssertion;
@"<BSInvalidatable>" _keyFocusStealingAssertion;
@"<BSInvalidatable>" _keyFocusPreventionAssertion;
@"BSProcessHandle" _originatingProcess;
```

## Properties

```
@property (Td,N,V_baseWindowLevel) baseWindowLevel;
@property (T@"SBTransientOverlayViewController",R,N,V_viewController) viewController;
@property (T@"SBTransientOverlayBackgroundWindow",&,N,V_backgroundWindow) backgroundWindow;
@property (TB,N,GisRotating,V_rotating) rotating;
@property (T@"SBTransientOverlayWindow",R,N,V_window) window;
@property (TB,N,GisDismissing,V_dismissing) dismissing;
@property (TB,N,V_hasFinishedWindowInitialization) hasFinishedWindowInitialization;
@property (TB,N,V_hasPreservedInputViews) hasPreservedInputViews;
@property (TQ,N,V_presentationSequence) presentationSequence;
@property (T@"<BSInvalidatable>",&,N,V_disableAutoUnlockAssertion) disableAutoUnlockAssertion;
@property (T@"<BSInvalidatable>",&,N,V_proximityEnabledAssertion) proximityEnabledAssertion;
@property (T@"<BSInvalidatable>",&,N,V_wallpaperAnimationSuspensionAssertion) wallpaperAnimationSuspensionAssertion;
@property (T@"SBFluidDismissalState",&,N,V_fluidDismissalState) fluidDismissalState;
@property (T@"SBPresentationObservationToken",&,N,V_bannerLongLookPresentationObservationToken) bannerLongLookPresentationObservationToken;
@property (T@"<BSInvalidatable>",&,N,V_bannerLongLookWindowLevelAssertion) bannerLongLookWindowLevelAssertion;
@property (T@"SBPresentationObservationToken",&,N,V_controlCenterPresentationObservationToken) controlCenterPresentationObservationToken;
@property (T@"<BSInvalidatable>",&,N,V_controlCenterWindowLevelAssertion) controlCenterWindowLevelAssertion;
@property (T@"SBPresentationObservationToken",&,N,V_siriPresentationObservationToken) siriPresentationObservationToken;
@property (T@"<BSInvalidatable>",&,N,V_siriWindowLevelAssertion) siriWindowLevelAssertion;
@property (T@"<BSInvalidatable>",&,N,V_keyFocusStealingAssertion) keyFocusStealingAssertion;
@property (T@"<BSInvalidatable>",&,N,V_keyFocusPreventionAssertion) keyFocusPreventionAssertion;
@property (T@"BSProcessHandle",&,N,V_originatingProcess) originatingProcess;
```

## Instance methods

```
-[_SBTransientOverlayPresentedEntity setControlCenterPresentationObservationToken:];
-[_SBTransientOverlayPresentedEntity disableAutoUnlockAssertion];
-[_SBTransientOverlayPresentedEntity baseWindowLevel];
-[_SBTransientOverlayPresentedEntity initWithViewController:window:baseWindowLevel:];
-[_SBTransientOverlayPresentedEntity setControlCenterWindowLevelAssertion:];
-[_SBTransientOverlayPresentedEntity setBannerLongLookWindowLevelAssertion:];
-[_SBTransientOverlayPresentedEntity setBaseWindowLevel:];
-[_SBTransientOverlayPresentedEntity backgroundWindow];
-[_SBTransientOverlayPresentedEntity originatingProcess];
-[_SBTransientOverlayPresentedEntity window];
-[_SBTransientOverlayPresentedEntity bannerLongLookPresentationObservationToken];
-[_SBTransientOverlayPresentedEntity bannerLongLookWindowLevelAssertion];
-[_SBTransientOverlayPresentedEntity hasFinishedWindowInitialization];
-[_SBTransientOverlayPresentedEntity keyFocusStealingAssertion];
-[_SBTransientOverlayPresentedEntity setKeyFocusPreventionAssertion:];
-[_SBTransientOverlayPresentedEntity viewController];
-[_SBTransientOverlayPresentedEntity setPresentationSequence:];
-[_SBTransientOverlayPresentedEntity presentationSequence];
-[_SBTransientOverlayPresentedEntity isDismissing];
-[_SBTransientOverlayPresentedEntity controlCenterWindowLevelAssertion];
-[_SBTransientOverlayPresentedEntity setProximityEnabledAssertion:];
-[_SBTransientOverlayPresentedEntity siriPresentationObservationToken];
-[_SBTransientOverlayPresentedEntity keyFocusPreventionAssertion];
-[_SBTransientOverlayPresentedEntity setBackgroundWindow:];
-[_SBTransientOverlayPresentedEntity setSiriPresentationObservationToken:];
-[_SBTransientOverlayPresentedEntity setDisableAutoUnlockAssertion:];
-[_SBTransientOverlayPresentedEntity isRotating];
-[_SBTransientOverlayPresentedEntity setRotating:];
-[_SBTransientOverlayPresentedEntity hasPreservedInputViews];
-[_SBTransientOverlayPresentedEntity setWallpaperAnimationSuspensionAssertion:];
-[_SBTransientOverlayPresentedEntity setHasPreservedInputViews:];
-[_SBTransientOverlayPresentedEntity setHasFinishedWindowInitialization:];
-[_SBTransientOverlayPresentedEntity setKeyFocusStealingAssertion:];
-[_SBTransientOverlayPresentedEntity setDismissing:];
-[_SBTransientOverlayPresentedEntity wallpaperAnimationSuspensionAssertion];
-[_SBTransientOverlayPresentedEntity controlCenterPresentationObservationToken];
-[_SBTransientOverlayPresentedEntity setSiriWindowLevelAssertion:];
-[_SBTransientOverlayPresentedEntity setOriginatingProcess:];
-[_SBTransientOverlayPresentedEntity setBannerLongLookPresentationObservationToken:];
-[_SBTransientOverlayPresentedEntity setFluidDismissalState:];
-[_SBTransientOverlayPresentedEntity proximityEnabledAssertion];
-[_SBTransientOverlayPresentedEntity siriWindowLevelAssertion];
-[_SBTransientOverlayPresentedEntity fluidDismissalState];
```
