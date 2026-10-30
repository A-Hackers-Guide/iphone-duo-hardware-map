# `CAMCoverScreenManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMCoverScreenDelegate`
- 4 instance variables, 6 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureVideoPreviewLayer" _videoPreviewLayer;
B _shutterBuddyAssetLoadingAllowed;
@"CAMPartnerModeViewController" _partnerModeViewController;
@"CAMShutterBuddyViewController" _shutterBuddyViewController;
```

## Properties

```
@property (T@"CAMPartnerModeViewController",&,N,V_partnerModeViewController) partnerModeViewController;
@property (T@"CAMShutterBuddyViewController",&,N,V_shutterBuddyViewController) shutterBuddyViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMCoverScreenManager setState:];
-[CAMCoverScreenManager setInterfaceModulation:animated:];
-[CAMCoverScreenManager startVideoCapture];
-[CAMCoverScreenManager stopVideoCapture];
-[CAMCoverScreenManager setCaptureOrientation:animated:];
-[CAMCoverScreenManager allowShutterBuddyAssetLoading];
-[CAMCoverScreenManager endPreviewFlipTransition];
-[CAMCoverScreenManager hideFlashIndicator];
-[CAMCoverScreenManager hideNightModeInstruction];
-[CAMCoverScreenManager hidePersonalPhotographerCountdown];
-[CAMCoverScreenManager initWithVideoPreviewLayer:];
-[CAMCoverScreenManager partnerModeViewController];
-[CAMCoverScreenManager pauseVideoCapture];
-[CAMCoverScreenManager performCaptureAnimation];
-[CAMCoverScreenManager resumeVideoCapture];
-[CAMCoverScreenManager setElapsedTimeBackgroundStyle:animated:];
-[CAMCoverScreenManager setPartnerModeViewController:];
-[CAMCoverScreenManager setPreviewNeedsHalfTurnCorrection:];
-[CAMCoverScreenManager setShutterBuddyViewController:];
-[CAMCoverScreenManager setupAndStartTimerCaptureWith:];
-[CAMCoverScreenManager showFlashIndicatorFor:isFlashActive:];
-[CAMCoverScreenManager showNightModeCountdownFrom:];
-[CAMCoverScreenManager showNightModeInstruction];
-[CAMCoverScreenManager showPersonalPhotographerCountdownWithTicks:];
-[CAMCoverScreenManager shutterBuddyViewController];
-[CAMCoverScreenManager stopTimerCapture];
-[CAMCoverScreenManager synchronizedCaptureTimerDelegateFired];
```
