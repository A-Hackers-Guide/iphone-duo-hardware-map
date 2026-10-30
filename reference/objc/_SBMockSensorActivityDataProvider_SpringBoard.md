# `_SBMockSensorActivityDataProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFSensorActivityDataProvider`
- 5 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
@"NSSet" _activeSensorActivityAttributions;
@"NSSet" _activeCameraAndMicrophoneActivityAttributions;
@"<SBFSensorActivityAttribution>" _mostRecentCameraAndMicrophoneSensorActivityAttribution;
@"NSSet" _activeAndRecentSensorActivityAttributions;
```

## Properties

```
@property (T@"NSSet",R,C,N,V_activeSensorActivityAttributions) activeSensorActivityAttributions;
@property (T@"NSSet",R,C,N,V_activeCameraAndMicrophoneActivityAttributions) activeCameraAndMicrophoneActivityAttributions;
@property (T@"<SBFSensorActivityAttribution>",R,C,N,V_mostRecentCameraAndMicrophoneSensorActivityAttribution) mostRecentCameraAndMicrophoneSensorActivityAttribution;
@property (T@"NSSet",R,C,N,V_activeAndRecentSensorActivityAttributions) activeAndRecentSensorActivityAttributions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBMockSensorActivityDataProvider activeAndRecentSensorActivityAttributions];
-[_SBMockSensorActivityDataProvider mostRecentCameraAndMicrophoneSensorActivityAttribution];
-[_SBMockSensorActivityDataProvider removeObserver:];
-[_SBMockSensorActivityDataProvider init];
-[_SBMockSensorActivityDataProvider activeCameraAndMicrophoneActivityAttributions];
-[_SBMockSensorActivityDataProvider activeSensorActivityAttributions];
-[_SBMockSensorActivityDataProvider addObserver:];
-[_SBMockSensorActivityDataProvider _notifyObserversOfUpdatesAttributions];
-[_SBMockSensorActivityDataProvider removeActiveCameraAttribution];
-[_SBMockSensorActivityDataProvider updateActiveCameraAttributionForBundleIdentifier:];
-[_SBMockSensorActivityDataProvider updateActiveSensorActivityAttributions:];
```
