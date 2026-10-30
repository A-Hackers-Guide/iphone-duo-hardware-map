# `SBCoverSheetGrabberManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutPublisherObserving`, `PBUIWallpaperObserver`, `SBDisplayContentModeTransitionObserver`
- 18 instance variables, 22 properties, 77 instance methods, 3 class methods

## Instance variables

```
B _inSecureAppOverLockScreen;
B _hasLockScreenInLayout;
B _isWaitingForAppFlyInSettle;
B _appFlyInDidSettle;
B _bannerHandoffInstantAppear;
B _suppressTeachPulse;
q _currentPhase;
@"NSNumber" _featureFlagOverrideForTesting;
@"NSNumber" _uiLockedOverrideForTesting;
@"NSNumber" _inSecureAppOverrideForTesting;
d _appFlyInDidSettleTimestamp;
@? _pendingPhaseCompletion;
@"NSTimer" _phaseTimer;
@"NSTimer" _appFlyInSettleFallbackTimer;
@"SBCoverSheetGrabberWindow" _window;
@"SBCoverSheetGrabberViewController" _grabberViewController;
@"<FBSDisplayLayoutPublishing>" _observedLayoutPublisher;
@"FBSDisplayLayout" _latestDisplayLayout;
```

## Properties

```
@property (Tq,N,V_currentPhase) currentPhase;
@property (T@"NSNumber",C,N,V_featureFlagOverrideForTesting) featureFlagOverrideForTesting;
@property (T@"NSNumber",C,N,V_uiLockedOverrideForTesting) uiLockedOverrideForTesting;
@property (T@"NSNumber",C,N,V_inSecureAppOverrideForTesting) inSecureAppOverrideForTesting;
@property (TB,N,V_inSecureAppOverLockScreen) inSecureAppOverLockScreen;
@property (TB,N,V_hasLockScreenInLayout) hasLockScreenInLayout;
@property (TB,N,V_isWaitingForAppFlyInSettle) isWaitingForAppFlyInSettle;
@property (TB,N,V_appFlyInDidSettle) appFlyInDidSettle;
@property (Td,N,V_appFlyInDidSettleTimestamp) appFlyInDidSettleTimestamp;
@property (TB,N,V_bannerHandoffInstantAppear) bannerHandoffInstantAppear;
@property (TB,N,V_suppressTeachPulse) suppressTeachPulse;
@property (T@?,C,N,V_pendingPhaseCompletion) pendingPhaseCompletion;
@property (T@"NSTimer",&,N,V_phaseTimer) phaseTimer;
@property (T@"NSTimer",&,N,V_appFlyInSettleFallbackTimer) appFlyInSettleFallbackTimer;
@property (T@"SBCoverSheetGrabberWindow",&,N,V_window) window;
@property (T@"SBCoverSheetGrabberViewController",&,N,V_grabberViewController) grabberViewController;
@property (T@"<FBSDisplayLayoutPublishing>",W,N,V_observedLayoutPublisher) observedLayoutPublisher;
@property (T@"FBSDisplayLayout",&,N,V_latestDisplayLayout) latestDisplayLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCoverSheetGrabberManager _isCampoEnabled];
+[SBCoverSheetGrabberManager _isCornerPocketDismissalEnabled];
+[SBCoverSheetGrabberManager _isCoverSheetGrabberEnabled];
```

## Instance methods

```
-[SBCoverSheetGrabberManager wallpaperDidChangeForVariant:];
-[SBCoverSheetGrabberManager uiLockedOverrideForTesting];
-[SBCoverSheetGrabberManager latestDisplayLayout];
-[SBCoverSheetGrabberManager setPhaseTimer:];
-[SBCoverSheetGrabberManager phaseTimer];
-[SBCoverSheetGrabberManager setInSecureAppOverrideForTesting:];
-[SBCoverSheetGrabberManager appFlyInSettleFallbackTimer];
-[SBCoverSheetGrabberManager _updateDisplayLayoutObservation];
-[SBCoverSheetGrabberManager _evaluateVisibilityState];
-[SBCoverSheetGrabberManager init];
-[SBCoverSheetGrabberManager _currentStatusBarResolvedStyle];
-[SBCoverSheetGrabberManager _phaseTimerFired:];
-[SBCoverSheetGrabberManager pendingPhaseCompletion];
-[SBCoverSheetGrabberManager _finishWaitingForAppFlyInSettle];
-[SBCoverSheetGrabberManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBCoverSheetGrabberManager isWaitingForAppFlyInSettle];
-[SBCoverSheetGrabberManager featureFlagOverrideForTesting];
-[SBCoverSheetGrabberManager _beginWaitingForAppFlyInSettle];
-[SBCoverSheetGrabberManager _handleUpdatedDisplayLayout:];
-[SBCoverSheetGrabberManager observedLayoutPublisher];
-[SBCoverSheetGrabberManager _handleCoverSheetWillPresentNotification:];
-[SBCoverSheetGrabberManager dealloc];
-[SBCoverSheetGrabberManager _tearDownWindow];
-[SBCoverSheetGrabberManager setHasLockScreenInLayout:];
-[SBCoverSheetGrabberManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBCoverSheetGrabberManager publisher:didUpdateLayout:withTransition:];
-[SBCoverSheetGrabberManager _isIPhoneLandscape];
-[SBCoverSheetGrabberManager _recomputeLayoutFlags];
-[SBCoverSheetGrabberManager window];
-[SBCoverSheetGrabberManager _handleCoverSheetAppFlyInDidSettleNotification:];
-[SBCoverSheetGrabberManager inSecureAppOverLockScreen];
-[SBCoverSheetGrabberManager _simulateLayoutChange:];
-[SBCoverSheetGrabberManager _isFoldableInWindow:];
-[SBCoverSheetGrabberManager _isGuidedAccessActive];
-[SBCoverSheetGrabberManager setIsWaitingForAppFlyInSettle:];
-[SBCoverSheetGrabberManager setBannerHandoffInstantAppear:];
-[SBCoverSheetGrabberManager setObservedLayoutPublisher:];
-[SBCoverSheetGrabberManager _advanceToEndOfCurrentPhase];
-[SBCoverSheetGrabberManager _handleCoverSheetDismissalNearlyCompleteNotification:];
-[SBCoverSheetGrabberManager setGrabberViewController:];
-[SBCoverSheetGrabberManager _ensureWindowCreatedForActiveScene];
-[SBCoverSheetGrabberManager inSecureAppOverrideForTesting];
-[SBCoverSheetGrabberManager appFlyInDidSettle];
-[SBCoverSheetGrabberManager setCurrentPhase:];
-[SBCoverSheetGrabberManager setInSecureAppOverLockScreen:];
-[SBCoverSheetGrabberManager currentPhase];
-[SBCoverSheetGrabberManager handoffBannerDismiss];
-[SBCoverSheetGrabberManager _isInSecureApp];
-[SBCoverSheetGrabberManager _subscribeToWallpaperLegibilityChanges];
-[SBCoverSheetGrabberManager setLatestDisplayLayout:];
-[SBCoverSheetGrabberManager suppressTeachPulse];
-[SBCoverSheetGrabberManager _unsubscribeFromWallpaperLegibilityChanges];
-[SBCoverSheetGrabberManager setAppFlyInSettleFallbackTimer:];
-[SBCoverSheetGrabberManager _currentLegibilitySettings];
-[SBCoverSheetGrabberManager setPendingPhaseCompletion:];
-[SBCoverSheetGrabberManager _enterPhase:];
-[SBCoverSheetGrabberManager _cancelPendingPhaseCompletion];
-[SBCoverSheetGrabberManager setAppFlyInDidSettle:];
-[SBCoverSheetGrabberManager setSuppressTeachPulse:];
-[SBCoverSheetGrabberManager setUiLockedOverrideForTesting:];
-[SBCoverSheetGrabberManager _activeWallpaperController];
-[SBCoverSheetGrabberManager targetGrabberFrameInCoordinateSpace:];
-[SBCoverSheetGrabberManager setAppFlyInDidSettleTimestamp:];
-[SBCoverSheetGrabberManager _hideImmediately];
-[SBCoverSheetGrabberManager appFlyInDidSettleTimestamp];
-[SBCoverSheetGrabberManager newBannerMorphHandleView];
-[SBCoverSheetGrabberManager _updateGrabberLegibility];
-[SBCoverSheetGrabberManager _resolveForegroundSceneHandle];
-[SBCoverSheetGrabberManager wallpaperLegibilitySettingsDidChange:forVariant:];
-[SBCoverSheetGrabberManager _shouldFireHintNow];
-[SBCoverSheetGrabberManager setWindow:];
-[SBCoverSheetGrabberManager hasLockScreenInLayout];
-[SBCoverSheetGrabberManager _canPresentGrabberForHandoff];
-[SBCoverSheetGrabberManager _applyVisibilityAction:];
-[SBCoverSheetGrabberManager bannerHandoffInstantAppear];
-[SBCoverSheetGrabberManager setFeatureFlagOverrideForTesting:];
-[SBCoverSheetGrabberManager grabberViewController];
```
