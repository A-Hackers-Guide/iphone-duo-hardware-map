# `SBRecordingIndicatorManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBWindowSceneStatusBarAssertionManagerObserver`, `SBRecordingIndicatorViewControllerDelegate`, `SBSensorActivityObserver`, `SBUIActiveOrientationObserver`, `PTSettingsKeyObserver`
- 24 instance variables, 17 properties, 58 instance methods, 1 class methods

## Instance variables

```
@"UIWindow" _recordingIndicatorWindow;
@"UIWindow" _recordingIndicatorWindowUIKitStatusBarPortal;
@"UIWindow" _recordingIndicatorWindowSystemAperturePortal;
@"SBRecordingIndicatorViewController" _recordingIndicatorViewController;
@"SBRecordingIndicatorViewController" _recordingIndicatorViewControllerUIKitStatusBarPortal;
@"SBRecordingIndicatorViewController" _recordingIndicatorViewControllerSystemAperturePortal;
@"SBSensorActivityDataProvider" _dataProvider;
B _indicatorStatusBarPartIsHidden;
B _indicatorIsHiddenForControlCenter;
B _visibilityIsForcedByPrototypeSettings;
B _invalidated;
B _assistantIslandActive;
B _indicatorVisible;
B _indicatorVisibleAtStatusBarLocation;
B _systemApertureIsSoLargeThatTheStatusBarIsProbablyHidden;
B _systemApertureEmpty;
@"SBWindowScene" _windowScene;
Q _displayMode;
@"NSSet" _activeCameraAndMicrophoneActivityAttributions;
@"SBRecordingIndicatorSystemApertureElement" _recordingIndicatorElement;
@"NSString" _recordingIndicatorElementAssociatedBlankingRegionIdentifier;
@"<SAInvalidatable>" _recordingIndicatorElementAssertion;
@"<SBRecordingIndicatorDisplayPowerManaging>" _indicatorDisplayPowerManaging;
@"SBSecureIndicatorMinimumOnTimeCoordinator" _minimumOnTimeCoordinator;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TQ,R,N,V_displayMode) displayMode;
@property (T@"NSSet",&,N,V_activeCameraAndMicrophoneActivityAttributions) activeCameraAndMicrophoneActivityAttributions;
@property (T@"SBRecordingIndicatorSystemApertureElement",&,N,V_recordingIndicatorElement) recordingIndicatorElement;
@property (T@"NSString",C,N,V_recordingIndicatorElementAssociatedBlankingRegionIdentifier) recordingIndicatorElementAssociatedBlankingRegionIdentifier;
@property (T@"<SAInvalidatable>",&,N,V_recordingIndicatorElementAssertion) recordingIndicatorElementAssertion;
@property (TB,N,V_systemApertureIsSoLargeThatTheStatusBarIsProbablyHidden) systemApertureIsSoLargeThatTheStatusBarIsProbablyHidden;
@property (TB,N,GisSystemApertureEmpty,V_systemApertureEmpty) systemApertureEmpty;
@property (T@"<SBRecordingIndicatorDisplayPowerManaging>",R,N,V_indicatorDisplayPowerManaging) indicatorDisplayPowerManaging;
@property (T@"SBSecureIndicatorMinimumOnTimeCoordinator",R,N,V_minimumOnTimeCoordinator) minimumOnTimeCoordinator;
@property (TB,R,N,GisIndicatorVisible,V_indicatorVisible) indicatorVisible;
@property (TB,R,N,GisIndicatorVisibleAtStatusBarLocation,V_indicatorVisibleAtStatusBarLocation) indicatorVisibleAtStatusBarLocation;
@property (TB,N,GisAssistantIslandActive,V_assistantIslandActive) assistantIslandActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBRecordingIndicatorManager _supportsSecureIndicator];
```

## Instance methods

```
-[SBRecordingIndicatorManager minimumOnTimeCoordinator];
-[SBRecordingIndicatorManager activityDidChangeForSensorActivityDataProvider:];
-[SBRecordingIndicatorManager activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBRecordingIndicatorManager systemApertureLayoutDidChange:];
-[SBRecordingIndicatorManager setRecordingIndicatorElement:];
-[SBRecordingIndicatorManager setWindowScene:];
-[SBRecordingIndicatorManager controlCenterWillPresent:];
-[SBRecordingIndicatorManager _createRecordingIndicatorForStandaloneLocation:];
-[SBRecordingIndicatorManager setIndicatorVisible:];
-[SBRecordingIndicatorManager _updateSystemApertureElementForAssociatedCameraIdentifiers:];
-[SBRecordingIndicatorManager _createRecordingIndicatorForSecureIndicator];
-[SBRecordingIndicatorManager systemApertureIsSoLargeThatTheStatusBarIsProbablyHidden];
-[SBRecordingIndicatorManager _setIndicatorVisible:atLocation:];
-[SBRecordingIndicatorManager activeCameraAndMicrophoneActivityAttributions];
-[SBRecordingIndicatorManager recordingIndicatorViewController:didUpdateIndicatorState:];
-[SBRecordingIndicatorManager _updateIndicatorViewForSensorType:associatedCameraIdentifiers:];
-[SBRecordingIndicatorManager setRecordingIndicatorElementAssociatedBlankingRegionIdentifier:];
-[SBRecordingIndicatorManager dealloc];
-[SBRecordingIndicatorManager displayMode];
-[SBRecordingIndicatorManager _controlCenterIsOnTheSameWindowScene:];
-[SBRecordingIndicatorManager isAssistantIslandActive];
-[SBRecordingIndicatorManager _indicatorTypeForSensorType:];
-[SBRecordingIndicatorManager _dataProviderDidUpdate:];
-[SBRecordingIndicatorManager _updateIndicatorStyleForSensorActivityAttributions:];
-[SBRecordingIndicatorManager activeInterfaceOrientationWillChangeToOrientation:];
-[SBRecordingIndicatorManager settings:changedValueForKey:];
-[SBRecordingIndicatorManager setRecordingIndicatorElementAssertion:];
-[SBRecordingIndicatorManager invalidate];
-[SBRecordingIndicatorManager _createRecordingIndicatorForSystemApertureLocation];
-[SBRecordingIndicatorManager _systemApertureHighLevelGainMapDefeatingLayer];
-[SBRecordingIndicatorManager initWithWindowScene:indicatorDisplayPowerManaging:];
-[SBRecordingIndicatorManager recordingIndicatorElementAssociatedBlankingRegionIdentifier];
-[SBRecordingIndicatorManager statusBarAssertionManager:addStatusBarSettingsAssertion:];
-[SBRecordingIndicatorManager isIndicatorVisible];
-[SBRecordingIndicatorManager controlCenterDidDismiss:];
-[SBRecordingIndicatorManager statusBarAssertionManager:removeStatusBarSettingsAssertion:];
-[SBRecordingIndicatorManager setSystemApertureIsSoLargeThatTheStatusBarIsProbablyHidden:];
-[SBRecordingIndicatorManager recordingIndicatorElementAssertion];
-[SBRecordingIndicatorManager _createRecordingIndicatorForStatusBarLocation];
-[SBRecordingIndicatorManager indicatorDisplayPowerManaging];
-[SBRecordingIndicatorManager setAssistantIslandActive:];
-[SBRecordingIndicatorManager _supportsStatusBarItem];
-[SBRecordingIndicatorManager _updateRecordingIndicatorLocationIfNecessary];
-[SBRecordingIndicatorManager setIndicatorVisibleAtStatusBarLocation:];
-[SBRecordingIndicatorManager isSystemApertureEmpty];
-[SBRecordingIndicatorManager setSystemApertureEmpty:];
-[SBRecordingIndicatorManager isIndicatorVisibleAtStatusBarLocation];
-[SBRecordingIndicatorManager _shouldSuppressSystemApertureElementWhileOtherElementsPresent];
-[SBRecordingIndicatorManager _indicatorIdentifierForSensorType:];
-[SBRecordingIndicatorManager _updateSystemApertureElementAssertion];
-[SBRecordingIndicatorManager setActiveCameraAndMicrophoneActivityAttributions:];
-[SBRecordingIndicatorManager windowScene];
-[SBRecordingIndicatorManager differentiateWithoutColorDidChange:];
-[SBRecordingIndicatorManager updateRecordingIndicatorForStatusBarChanges];
-[SBRecordingIndicatorManager _updateRecordingIndicatorForStatusBarChanges];
-[SBRecordingIndicatorManager _invalidateWithReason:];
-[SBRecordingIndicatorManager updateRecordingIndicatorLocationIfNecessary];
-[SBRecordingIndicatorManager recordingIndicatorElement];
```
