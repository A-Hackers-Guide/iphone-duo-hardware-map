# `SBHideSharePlayContentFromSharedScreenController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBannerManagerTransitionObserver`, `SBDraggingSystemObserver`, `SBMousePointerHardwareConnectionObserver`, `SBTransientOverlayPresentationManagerObserver`
- 12 instance variables, 4 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _trackedPresentables;
@"NSHashTable" _trackedTransientOverlays;
@"NSHashTable" _windowsBeingHiddenWithDisableUpdateMask;
@"NSHashTable" _viewControllersWithDisableUpdateMasks;
@"UIViewController" _pipViewControllerBeingHiddenWithDisableUpdateMask;
@"NSMutableSet" _activeAssertions;
@"UIWindow" _cloneTerminatingWindow;
@"CALayer" _cloneTerminatingLayer;
B _isControlCenterFullyPresentedOnMainDisplay;
q _numberOfActiveDragSessions;
@"<BSInvalidatable>" _simulatedAssertion;
B _isObservingPIPWindowLevelsAndVisibility;
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
-[SBHideSharePlayContentFromSharedScreenController _windowVisibilityDidChange:];
-[SBHideSharePlayContentFromSharedScreenController init];
-[SBHideSharePlayContentFromSharedScreenController dealloc];
-[SBHideSharePlayContentFromSharedScreenController transientOverlayPresentationManager:didDismissViewController:wasTopmostPresentation:];
-[SBHideSharePlayContentFromSharedScreenController mousePointerManager:hardwarePointingDeviceAttachedDidChange:];
-[SBHideSharePlayContentFromSharedScreenController bannerManager:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBHideSharePlayContentFromSharedScreenController transientOverlayPresentationManager:willPresentViewController:];
-[SBHideSharePlayContentFromSharedScreenController bannerManager:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBHideSharePlayContentFromSharedScreenController dragSessionDidBegin:];
-[SBHideSharePlayContentFromSharedScreenController dragSessionDidEnd:];
-[SBHideSharePlayContentFromSharedScreenController _addAssertion:];
-[SBHideSharePlayContentFromSharedScreenController _handleControlCenterWillDismiss];
-[SBHideSharePlayContentFromSharedScreenController _canShareDaemonScenes];
-[SBHideSharePlayContentFromSharedScreenController _coverSheetWindowLevelForWindowScene:];
-[SBHideSharePlayContentFromSharedScreenController _deviceHasDaemonSceneThatShouldBeShared];
-[SBHideSharePlayContentFromSharedScreenController _deviceHasDaemonSceneThatShouldBeSharedIfPossible];
-[SBHideSharePlayContentFromSharedScreenController _handleControlCenterDidPresent];
-[SBHideSharePlayContentFromSharedScreenController _isCoverSheetFullyPresentedForWindowScene:];
-[SBHideSharePlayContentFromSharedScreenController _isCoverSheetVisibleForWindowScene:];
-[SBHideSharePlayContentFromSharedScreenController _isPipViewControllerToHideOnMainDisplay];
-[SBHideSharePlayContentFromSharedScreenController _pipViewControllerToHide];
-[SBHideSharePlayContentFromSharedScreenController _removeAssertion:];
-[SBHideSharePlayContentFromSharedScreenController _resolveHidingBehavior];
-[SBHideSharePlayContentFromSharedScreenController _startHidingViewControllerFromClonedDisplaysIfNeeded:];
-[SBHideSharePlayContentFromSharedScreenController _startHidingWindowFromClonedDisplaysIfNeeded:];
-[SBHideSharePlayContentFromSharedScreenController _startObservingForActiveHideAssertionIfNeeded];
-[SBHideSharePlayContentFromSharedScreenController _startTrackingPresentable:];
-[SBHideSharePlayContentFromSharedScreenController _startTrackingTransientOverlayViewController:];
-[SBHideSharePlayContentFromSharedScreenController _stopHidingViewControllerFromClonedDisplaysIfNeeded:];
-[SBHideSharePlayContentFromSharedScreenController _stopHidingWindowFromClonedDisplaysIfNeeded:];
-[SBHideSharePlayContentFromSharedScreenController _stopObservingForActiveHideAssertionIfNeeded];
-[SBHideSharePlayContentFromSharedScreenController _stopTrackingPresentable:];
-[SBHideSharePlayContentFromSharedScreenController _stopTrackingTransientOverlayViewController:];
-[SBHideSharePlayContentFromSharedScreenController _systemNotesWindow];
-[SBHideSharePlayContentFromSharedScreenController acquireHideSharePlayContentFromClonedDisplaysAssertionForReason:];
-[SBHideSharePlayContentFromSharedScreenController bannerManagerDidUpdateWindowLevel:];
```
