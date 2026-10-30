# `CAMMotionController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSAccelerometerDelegate`, `CAMLevelViewModelChangeObserver`, `CAMOrientationModelDelegate`
- 17 instance variables, 25 properties, 63 instance methods, 0 class methods

## Instance variables

```
B __cachedCaptureOrientationIsInitialQuery;
B __active;
B __didNotifyCaptureOrientationWasInvalid;
q _deviceOrientation;
q _allowedOrientations;
@"CAMLevelViewModel" _activeLevelViewModel;
@"CAMPreviewAlignmentModel" _activePreviewAlignmentModel;
@"CAMOrientationModel" _activeOrientationModel;
q __cachedCaptureOrientation;
q __fallbackCaptureOrientation;
@"CAMOrientationSeedSampler" __orientationSeedSampler;
@"BKSAccelerometer" __accelerometer;
q __numberOfDominantPhysicalButtonObservers;
@"CMMotionManager" __physicalButtonMotionManager;
q _dominantPhysicalButton;
@"CMMotionManager" __motionManager;
q __orientationIfForcedToLandscape;
```

## Properties

```
@property (Tq,N,S_setCachedCaptureOrientation:,V__cachedCaptureOrientation) _cachedCaptureOrientation;
@property (Tq,R,N,V__fallbackCaptureOrientation) _fallbackCaptureOrientation;
@property (TB,N,S_setCachedCaptureOrientationIsInitialQuery:,V__cachedCaptureOrientationIsInitialQuery) _cachedCaptureOrientationIsInitialQuery;
@property (T@"CAMOrientationSeedSampler",R,N,V__orientationSeedSampler) _orientationSeedSampler;
@property (TB,N,S_setActive:,V__active) _active;
@property (TB,R,N) _wantsGravitySeedOrientation;
@property (TB,N,S_setDidNotifyCaptureOrientationWasInvalid:,V__didNotifyCaptureOrientationWasInvalid) _didNotifyCaptureOrientationWasInvalid;
@property (T@"BKSAccelerometer",&,N,S_setAccelerometer:,V__accelerometer) _accelerometer;
@property (Tq,N,S_setNumberOfDominantPhysicalButtonObservers:,V__numberOfDominantPhysicalButtonObservers) _numberOfDominantPhysicalButtonObservers;
@property (T@"CMMotionManager",R,N,V__physicalButtonMotionManager) _physicalButtonMotionManager;
@property (Tq,N,S_setDominantPhysicalButton:,V_dominantPhysicalButton) dominantPhysicalButton;
@property (T@"CMMotionManager",R,N,V__motionManager) _motionManager;
@property (T@"CAMLevelViewModel",&,N,S_setActiveLevelViewModel:,V_activeLevelViewModel) activeLevelViewModel;
@property (T@"CAMPreviewAlignmentModel",&,N,S_setActivePreviewAlignmentModel:,V_activePreviewAlignmentModel) activePreviewAlignmentModel;
@property (T@"CAMOrientationModel",&,N,S_setActiveOrientationModel:,V_activeOrientationModel) activeOrientationModel;
@property (Tq,N,S_setOrientationWhenForcedToLandscape:,V__orientationIfForcedToLandscape) _orientationIfForcedToLandscape;
@property (Tq,N,V_deviceOrientation) deviceOrientation;
@property (TB,R,N) _shouldEndUpdatingOrientationModel;
@property (Tq,R,N) captureOrientation;
@property (Tq,R,N) panoramaCaptureOrientation;
@property (Tq,N,V_allowedOrientations) allowedOrientations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMMotionController setDeviceOrientation:];
-[CAMMotionController _debugStringForDeviceOrientation:];
-[CAMMotionController deviceOrientation];
-[CAMMotionController _handleApplicationWillEnterForeground:];
-[CAMMotionController activeOrientationModel];
-[CAMMotionController endUpdatingPreviewAlignmentModel];
-[CAMMotionController _cachedCaptureOrientation];
-[CAMMotionController _didNotifyCaptureOrientationWasInvalid];
-[CAMMotionController _accelerometer];
-[CAMMotionController init];
-[CAMMotionController _updateInterfaceOrientationIfAllInterfaceOrientationsAreAllowed];
-[CAMMotionController observable:didPublishChange:withContext:];
-[CAMMotionController _handleApplicationDidEnterBackground:];
-[CAMMotionController _active];
-[CAMMotionController dealloc];
-[CAMMotionController _setDidNotifyCaptureOrientationWasInvalid:];
-[CAMMotionController _setActive:];
-[CAMMotionController _handleLevelMotionUpdate:error:];
-[CAMMotionController _setActiveOrientationModel:];
-[CAMMotionController _handleApplicationDidBecomeActive:];
-[CAMMotionController _orientationSeedSampler];
-[CAMMotionController _beginUpdatingOrientationModelIfNeeded];
-[CAMMotionController activePreviewAlignmentModel];
-[CAMMotionController _motionManager];
-[CAMMotionController _endUpdatingOrientationModelIfNeeded];
-[CAMMotionController _updateMotionManager];
-[CAMMotionController _cachedCaptureOrientationIsInitialQuery];
-[CAMMotionController accelerometer:didChangeDeviceOrientation:];
-[CAMMotionController allowedOrientations];
-[CAMMotionController _debugStringForInterfaceOrientation:];
-[CAMMotionController beginUpdatingLevelViewModel:];
-[CAMMotionController _setActivePreviewAlignmentModel:];
-[CAMMotionController _numberOfDominantPhysicalButtonObservers];
-[CAMMotionController _setNumberOfDominantPhysicalButtonObservers:];
-[CAMMotionController _updateGravitySeedOrientationWithDeviceMotion:];
-[CAMMotionController _physicalButtonMotionManager];
-[CAMMotionController debugValidateCaptureOrientationForMode:];
-[CAMMotionController _shouldEndUpdatingOrientationModel];
-[CAMMotionController _currentHorizontalSizeClass];
-[CAMMotionController activeLevelViewModel];
-[CAMMotionController orientationModel:didChangeInterfaceOrientation:];
-[CAMMotionController _fallbackCaptureOrientation];
-[CAMMotionController _setAccelerometer:];
-[CAMMotionController beginUpdatingPreviewAlignmentModel:];
-[CAMMotionController dominantPhysicalButton];
-[CAMMotionController endUpdatingOrientationModel];
-[CAMMotionController _setActiveLevelViewModel:];
-[CAMMotionController _setDominantPhysicalButton:];
-[CAMMotionController endUpdatingActiveLevelViewModel];
-[CAMMotionController panoramaCaptureOrientation];
-[CAMMotionController setAllowedOrientations:];
-[CAMMotionController _orientationIfForcedToLandscape];
-[CAMMotionController _wantsGravitySeedOrientation];
-[CAMMotionController accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:];
-[CAMMotionController _setCachedCaptureOrientation:];
-[CAMMotionController _setCachedCaptureOrientationIsInitialQuery:];
-[CAMMotionController beginUpdatingOrientationModel:];
-[CAMMotionController orientationModelDidBecomeUpright:];
-[CAMMotionController _updateInitialOrientation];
-[CAMMotionController _interfaceOrientationRotated90:];
-[CAMMotionController _beginUpdatingOrientationModel];
-[CAMMotionController captureOrientation];
-[CAMMotionController _setOrientationWhenForcedToLandscape:];
```
