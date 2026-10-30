# `CAMPortraitModeInstructionLabel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMInstructionLabel`
- 9 instance variables, 9 properties, 20 instance methods, 2 class methods

## Instance variables

```
B _flashSupported;
B _nightModePortraitSupported;
q _shallowDepthOfFieldStatus;
q _flashMode;
Q _numberOfPeopleFound;
q _devicePosition;
q _lightingType;
q _nightModeStatus;
q _nightMode;
```

## Properties

```
@property (Tq,N,V_shallowDepthOfFieldStatus) shallowDepthOfFieldStatus;
@property (TB,N,GisFlashSupported,V_flashSupported) flashSupported;
@property (Tq,N,V_flashMode) flashMode;
@property (TQ,N,V_numberOfPeopleFound) numberOfPeopleFound;
@property (Tq,N,V_devicePosition) devicePosition;
@property (Tq,N,V_lightingType) lightingType;
@property (Tq,N,V_nightModeStatus) nightModeStatus;
@property (Tq,N,V_nightMode) nightMode;
@property (TB,N,V_nightModePortraitSupported) nightModePortraitSupported;
```

## Class methods

```
+[CAMPortraitModeInstructionLabel _textForShallowDepthOfFieldStatus:numberOfPeopleFound:flashSupported:flashMode:devicePosition:lightingType:nightMode:nightModeStatus:nightModePortraitSupported:];
+[CAMPortraitModeInstructionLabel shouldDisplayInstructionForShallowDepthOfFieldStatus:];
```

## Instance methods

```
-[CAMPortraitModeInstructionLabel setLightingType:];
-[CAMPortraitModeInstructionLabel shallowDepthOfFieldStatus];
-[CAMPortraitModeInstructionLabel setShallowDepthOfFieldStatus:];
-[CAMPortraitModeInstructionLabel nightMode];
-[CAMPortraitModeInstructionLabel nightModeStatus];
-[CAMPortraitModeInstructionLabel _updateTextWithPriorStatus:];
-[CAMPortraitModeInstructionLabel lightingType];
-[CAMPortraitModeInstructionLabel setNightMode:];
-[CAMPortraitModeInstructionLabel setNumberOfPeopleFound:];
-[CAMPortraitModeInstructionLabel setNightModeStatus:];
-[CAMPortraitModeInstructionLabel sizeThatFits:];
-[CAMPortraitModeInstructionLabel nightModePortraitSupported];
-[CAMPortraitModeInstructionLabel isFlashSupported];
-[CAMPortraitModeInstructionLabel setFlashSupported:];
-[CAMPortraitModeInstructionLabel setFlashMode:];
-[CAMPortraitModeInstructionLabel devicePosition];
-[CAMPortraitModeInstructionLabel flashMode];
-[CAMPortraitModeInstructionLabel numberOfPeopleFound];
-[CAMPortraitModeInstructionLabel setNightModePortraitSupported:];
-[CAMPortraitModeInstructionLabel setDevicePosition:];
```
