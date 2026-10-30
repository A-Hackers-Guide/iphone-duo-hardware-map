# `CAMConflictingControlConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 11 instance methods, 12 class methods

## Instance variables

```
B _personalPhotographerEnabled;
q _desiredFlashMode;
q _desiredHDRMode;
q _desiredLivePhotoMode;
q _desiredRAWMode;
q _desiredPhotoResolution;
Q _photoFormatConflicts;
Q _desiredNightModeControlMode;
Q _nightModeConflicts;
q _desiredMacroMode;
```

## Properties

```
@property (Tq,R,N,V_desiredFlashMode) desiredFlashMode;
@property (Tq,R,N,V_desiredHDRMode) desiredHDRMode;
@property (Tq,R,N,V_desiredLivePhotoMode) desiredLivePhotoMode;
@property (Tq,R,N,V_desiredRAWMode) desiredRAWMode;
@property (Tq,R,N,V_desiredPhotoResolution) desiredPhotoResolution;
@property (TQ,R,N,V_photoFormatConflicts) photoFormatConflicts;
@property (TQ,R,N,V_desiredNightModeControlMode) desiredNightModeControlMode;
@property (TQ,R,N,V_nightModeConflicts) nightModeConflicts;
@property (Tq,R,N,V_desiredMacroMode) desiredMacroMode;
@property (TB,R,N,V_personalPhotographerEnabled) personalPhotographerEnabled;
```

## Class methods

```
+[CAMConflictingControlConfiguration hasConflictBetweenBurstAndLockedExposureDuration:forCaptureMode:device:];
+[CAMConflictingControlConfiguration hasConflictBetweenDesiredFlashMode:andLockedExposureDuration:forCaptureMode:devicePosition:];
+[CAMConflictingControlConfiguration hasConflictBetweenDesiredLivePhotoMode:andLockedExposureDuration:forCaptureMode:devicePosition:];
+[CAMConflictingControlConfiguration hasConflictBetweenDesiredNightModeControlMode:andLockedExposureDuration:forCaptureMode:device:];
+[CAMConflictingControlConfiguration hasConflictBetweenDesiredTorchMode:andLockedExposureDuration:forCaptureMode:devicePosition:];
+[CAMConflictingControlConfiguration isNightModePhotoModeDepthConflictRelevantForMode:device:photoFormat:];
+[CAMConflictingControlConfiguration resolveDesiredFlashMode:personalPhotographerEnabled:];
+[CAMConflictingControlConfiguration resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:frontRearSimultaneousVideoEnabled:personalPhotographerEnabled:];
+[CAMConflictingControlConfiguration resolveDesiredNightModeControlMode:nightModeConflicts:resolvedFlashMode:captureMode:captureDevice:photoFormat:depthEffectEnabledFromSuggestion:personalPhotographerEnabled:lockedExposureDuration:];
+[CAMConflictingControlConfiguration resolveDesiredRAWMode:photoFormatConflicts:desiredLivePhotoMode:desiredFlashMode:toRAWMode:toLivePhotoMode:toFlashMode:];
+[CAMConflictingControlConfiguration shouldDisableMacroForLockedPortraitForMode:devicePosition:photoFormat:optionalDepthEffectEnabled:];
+[CAMConflictingControlConfiguration validatedNightModeConflicts:forMode:device:photoFormat:];
```

## Instance methods

```
-[CAMConflictingControlConfiguration personalPhotographerEnabled];
-[CAMConflictingControlConfiguration desiredFlashMode];
-[CAMConflictingControlConfiguration desiredHDRMode];
-[CAMConflictingControlConfiguration desiredLivePhotoMode];
-[CAMConflictingControlConfiguration desiredMacroMode];
-[CAMConflictingControlConfiguration desiredNightModeControlMode];
-[CAMConflictingControlConfiguration desiredPhotoResolution];
-[CAMConflictingControlConfiguration desiredRAWMode];
-[CAMConflictingControlConfiguration initWithDesiredFlashMode:desiredHDRMode:desiredLivePhotoMode:desiredRAWMode:desiredPhotoResolution:photoFormatConflicts:desiredNightModeControlMode:nightModeConflicts:desiredMacroMode:personalPhotographerEnabled:];
-[CAMConflictingControlConfiguration nightModeConflicts];
-[CAMConflictingControlConfiguration photoFormatConflicts];
```
