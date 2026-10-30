# `SBFocusActivityManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FCUISystemApertureElementProviding`, `SBFocusActivityPickerTransientOverlayViewControllerDelegate`, `DNDModeSelectionServiceListener`, `SBBannerManagerTransitionObserver`, `SBSystemActionValidating`
- 13 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"DNDModeSelectionService" _modeSelectionService;
@"NSSet" _availableModes;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _modesLock;
@"NSObject<OS_dispatch_queue>" _availableModesFetchQueue;
@"SBFocusActivityPickerTransientOverlayViewController" _transientOverlay;
@"FCUIFocusEnablementIndicatorManager" _focusEnablementIndicatorManager;
@"SBSystemActionCompoundPreviewAssertion" _compoundPreviewAssertion;
@"<SAInvalidatable>" _focusElementAssertion;
@"SBFocusEnablementIndicatorSystemApertureActivityElement" _focusElement;
@"UIViewController" _focusPresentable;
@"NSString" _previewingModeIdentifier;
@"NSString" _activeModeIdentifier;
@"SBFocusActivityBannerAuthority" _focusBannerAuthority;
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
-[SBFocusActivityManager modeSelectionService:didReceiveAvailableModesUpdate:];
-[SBFocusActivityManager modeSelectionService:didReceiveModesUpdate:];
-[SBFocusActivityManager bannerManager:willDismissPresentable:withTransitionCoordinator:userInfo:];
-[SBFocusActivityManager modeSelectionService:didReceiveUpdatedActiveModeAssertion:stateUpdate:];
-[SBFocusActivityManager bannerManager:willPresentPresentable:withTransitionCoordinator:userInfo:];
-[SBFocusActivityManager createPersistentFocusElementForActivityDescription:enabled:];
-[SBFocusActivityManager createPersistentFocusPickerElementForActivityDescription:enabled:];
-[SBFocusActivityManager focusActivityPickerTransientOverlayViewController:didDismiss:];
-[SBFocusActivityManager shouldPreviewSystemAction:];
```
