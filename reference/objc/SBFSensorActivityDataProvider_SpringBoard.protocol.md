# `SBFSensorActivityDataProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",R,C,N) activeSensorActivityAttributions;
@property (T@"NSSet",R,C,N) activeCameraAndMicrophoneActivityAttributions;
@property (T@"<SBFSensorActivityAttribution>",R,C,N) mostRecentCameraAndMicrophoneSensorActivityAttribution;
@property (T@"NSSet",R,C,N) activeAndRecentSensorActivityAttributions;
```

## Instance methods

```
-[SBFSensorActivityDataProvider activeAndRecentSensorActivityAttributions];
-[SBFSensorActivityDataProvider mostRecentCameraAndMicrophoneSensorActivityAttribution];
-[SBFSensorActivityDataProvider removeObserver:];
-[SBFSensorActivityDataProvider activeCameraAndMicrophoneActivityAttributions];
-[SBFSensorActivityDataProvider activeSensorActivityAttributions];
-[SBFSensorActivityDataProvider addObserver:];
```
