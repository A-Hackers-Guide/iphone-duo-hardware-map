# `SBFlashlightActivityManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIFlashlightObserver`, `SBFlashlightActivityElementDelegate`, `SBDynamicFlashlightActivityElementDelegate`
- 13 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBFlashlightActivityElement" _flashlightActivityElement;
@"SBFlashlightAlertElement" _flashlightUnavailableAlertElement;
@"SBDynamicFlashlightActivityElement" _dynamicFlashlightActivityElement;
@"SBSystemActionCompoundPreviewAssertion" _compoundPreviewAssertion;
@"<SAInvalidatable>" _flashlightActivityAssertion;
@"<SAInvalidatable>" _flashlightUnavailableAlertAssertion;
@"SBFlashlightPreviewPresentableViewController" _flashlightPreviewPresentableViewController;
B _flashlightWasOnDuringLastUpdate;
@"SBFlashlightActivityBannerAuthority" _bannerAuthority;
B _shouldShowUIForFlashlightLevel;
B _shouldShowDynamicFlashlightUI;
@"SBWindowScene" _windowScene;
@"SBUIFlashlightController" _flashlightController;
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
-[SBFlashlightActivityManager flashlightAvailabilityDidChange:];
-[SBFlashlightActivityManager flashlightLevelDidChange:];
-[SBFlashlightActivityManager flashlightOverheatedDidChange:];
-[SBFlashlightActivityManager dynamicFlashlightActivityElementDidChangeIntensity:width:animated:];
-[SBFlashlightActivityManager dynamicFlashlightActivityElementDidCollapse];
-[SBFlashlightActivityManager dynamicFlashlightActivityElementDidUpdatePersistedIntensity:width:];
-[SBFlashlightActivityManager dynamicFlashlightActivityElementRequestsTogglingFlashlight];
-[SBFlashlightActivityManager flashlightActivityElementRequestsTogglingFlashlight:];
```
