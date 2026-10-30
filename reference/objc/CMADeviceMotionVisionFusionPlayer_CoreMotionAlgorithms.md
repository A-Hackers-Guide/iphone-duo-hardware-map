# `CMADeviceMotionVisionFusionPlayer`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CMVLFDeviceMotionFuser, std::default_delete<CMVLFDeviceMotionFuser>>=""{?="__ptr_"^{CMVLFDeviceMotionFuser}}} fVLFDeviceMotionFuser;
f fMagneticDeclination;
d fMagneticDeclinationTimestamp;
B _fusionEnabled;
B _playerActive;
B _arSessionActive;
```

## Properties

```
@property (TB,N,GisPlayerActive,V_playerActive) playerActive;
@property (TB,N,GisARSessionActive,V_arSessionActive) arSessionActive;
@property (TB,N,GisFusionEnabled,V_fusionEnabled) fusionEnabled;
```

## Instance methods

```
-[CMADeviceMotionVisionFusionPlayer init];
-[CMADeviceMotionVisionFusionPlayer stop];
-[CMADeviceMotionVisionFusionPlayer start];
-[CMADeviceMotionVisionFusionPlayer reset];
-[CMADeviceMotionVisionFusionPlayer updateLocation:];
-[CMADeviceMotionVisionFusionPlayer magneticDeclination];
-[CMADeviceMotionVisionFusionPlayer updateARSessionState:];
-[CMADeviceMotionVisionFusionPlayer isFusionEnabled];
-[CMADeviceMotionVisionFusionPlayer isARSessionActive];
-[CMADeviceMotionVisionFusionPlayer isPlayerActive];
-[CMADeviceMotionVisionFusionPlayer setArSessionActive:];
-[CMADeviceMotionVisionFusionPlayer setEnableFusion:];
-[CMADeviceMotionVisionFusionPlayer setFusionEnabled:];
-[CMADeviceMotionVisionFusionPlayer setPlayerActive:];
-[CMADeviceMotionVisionFusionPlayer getFusedDeviceMotionFrom:];
-[CMADeviceMotionVisionFusionPlayer getFusedDeviceMotionFrom:andAttitudeReferenceFrame:];
-[CMADeviceMotionVisionFusionPlayer updateVLLocalizationResult:];
```
