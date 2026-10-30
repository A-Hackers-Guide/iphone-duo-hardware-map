# `SBCaptureButtonCoachingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `SBSystemGestureRecognizerDelegate`, `SBCaptureButtonCoachingHUDViewControllerDelegate`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<SBHUDControlling>" _hudController;
@"SBCaptureButtonCoachingHUDViewController" _hudViewController;
@"SBFailingSystemGestureRecognizer" _dismissGestureRecognizer;
@"SBWindowScene" _windowScene;
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
-[SBCaptureButtonCoachingController backlightController:didTransitionToBacklightState:source:];
-[SBCaptureButtonCoachingController _gestureRecognizerFailed:];
-[SBCaptureButtonCoachingController viewForSystemGestureRecognizer:];
-[SBCaptureButtonCoachingController _volumeButtonPressed:];
-[SBCaptureButtonCoachingController setExtraCoachingUIButtonOffset:];
-[SBCaptureButtonCoachingController _startObservingSignalsToDismissIfNeeded];
-[SBCaptureButtonCoachingController _stopObservingSignalsToDismissIfNeeded];
-[SBCaptureButtonCoachingController captureButtonCoachingHUDViewController:didBeginTransitionToState:];
-[SBCaptureButtonCoachingController captureButtonCoachingHUDViewControllerWillRotate:];
-[SBCaptureButtonCoachingController dismissCoachingUI];
-[SBCaptureButtonCoachingController initWithHUDController:windowScene:];
-[SBCaptureButtonCoachingController showCoachingUIWithText:dismissInterval:];
-[SBCaptureButtonCoachingController showCoachingUIWithText:glyphPackageName:glyphLandscapeStateName:dismissInterval:];
```
