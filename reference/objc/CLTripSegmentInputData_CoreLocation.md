# `CLTripSegmentInputData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _isFinalPart;
@"NSUUID" _commuteID;
@"NSUUID" _tripSegmentID;
q _modeOfTransport;
@"NSArray" _inertialData;
@"NSArray" _tripLocations;
@"CLTripSegmentLocation" _startTripLocation;
@"CLTripSegmentLocation" _stopTripLocation;
@"NSArray" _inertialOdometryData;
```

## Properties

```
@property (T@"NSUUID",R,V_commuteID) commuteID;
@property (T@"NSUUID",R,V_tripSegmentID) tripSegmentID;
@property (TB,R,N,V_isFinalPart) isFinalPart;
@property (Tq,R,N,V_modeOfTransport) modeOfTransport;
@property (T@"NSArray",R,V_inertialData) inertialData;
@property (T@"NSArray",R,V_inertialOdometryData) inertialOdometryData;
@property (T@"NSArray",R,V_tripLocations) tripLocations;
@property (T@"CLTripSegmentLocation",R,V_startTripLocation) startTripLocation;
@property (T@"CLTripSegmentLocation",R,V_stopTripLocation) stopTripLocation;
```

## Class methods

```
+[CLTripSegmentInputData supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentInputData dealloc];
-[CLTripSegmentInputData encodeWithCoder:];
-[CLTripSegmentInputData initWithCoder:];
-[CLTripSegmentInputData copyWithZone:];
-[CLTripSegmentInputData modeOfTransport];
-[CLTripSegmentInputData commuteID];
-[CLTripSegmentInputData inertialData];
-[CLTripSegmentInputData inertialOdometryData];
-[CLTripSegmentInputData initWithCommuteID:tripSegmentID:isFinalPart:modeOfTransport:tripLocations:startTripLocation:stopTripLocation:inertialOdometryData:];
-[CLTripSegmentInputData initWithTripSegmentID:isFinalPart:modeOfTransport:tripLocations:startTripLocation:stopTripLocation:inertialData:];
-[CLTripSegmentInputData initWithTripSegmentID:isFinalPart:modeOfTransport:tripLocations:startTripLocation:stopTripLocation:inertialOdometryData:];
-[CLTripSegmentInputData isAutomotiveModeOfTransport];
-[CLTripSegmentInputData isCyclingModeOfTransport];
-[CLTripSegmentInputData isFinalPart];
-[CLTripSegmentInputData isPedestrianModeOfTransport];
-[CLTripSegmentInputData startTripLocation];
-[CLTripSegmentInputData stopTripLocation];
-[CLTripSegmentInputData tripLocations];
-[CLTripSegmentInputData tripSegmentID];
```
