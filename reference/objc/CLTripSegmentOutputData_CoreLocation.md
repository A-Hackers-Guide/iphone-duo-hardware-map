# `CLTripSegmentOutputData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 11 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _isFinalPart;
@"NSUUID" _tripSegmentID;
q _modeOfTransport;
@"NSMutableDictionary" _metaData;
@"NSDate" _startDate;
@"NSDate" _endDate;
d _duration_s;
d _distance_m;
d _distanceUnc_m;
@"NSArray" _tripLocations;
@"NSArray" _routeRoads;
```

## Properties

```
@property (T@"NSUUID",R,V_tripSegmentID) tripSegmentID;
@property (TB,R,N,V_isFinalPart) isFinalPart;
@property (T@"NSMutableDictionary",&,V_metaData) metaData;
@property (Tq,R,N,V_modeOfTransport) modeOfTransport;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
@property (Td,N,V_duration_s) duration_s;
@property (Td,N,V_distance_m) distance_m;
@property (Td,N,V_distanceUnc_m) distanceUnc_m;
@property (T@"NSArray",R,V_tripLocations) tripLocations;
@property (T@"NSArray",R,V_routeRoads) routeRoads;
```

## Class methods

```
+[CLTripSegmentOutputData supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentOutputData startDate];
-[CLTripSegmentOutputData setMetaData:];
-[CLTripSegmentOutputData metaData];
-[CLTripSegmentOutputData dealloc];
-[CLTripSegmentOutputData endDate];
-[CLTripSegmentOutputData encodeWithCoder:];
-[CLTripSegmentOutputData initWithCoder:];
-[CLTripSegmentOutputData copyWithZone:];
-[CLTripSegmentOutputData modeOfTransport];
-[CLTripSegmentOutputData distanceUnc_m];
-[CLTripSegmentOutputData distance_m];
-[CLTripSegmentOutputData duration_s];
-[CLTripSegmentOutputData initWithTripSegmentID:isFinalPart:startDate:endDate:duration:modeOfTransport:distance:distanceUnc:tripLocations:routeRoads:];
-[CLTripSegmentOutputData isFinalPart];
-[CLTripSegmentOutputData routeRoads];
-[CLTripSegmentOutputData setDistanceUnc_m:];
-[CLTripSegmentOutputData setDistance_m:];
-[CLTripSegmentOutputData setDuration_s:];
-[CLTripSegmentOutputData tripLocations];
-[CLTripSegmentOutputData tripSegmentID];
```
