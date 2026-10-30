# `CLTripSegmentRoadData`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 23 instance methods, 1 class methods

## Instance variables

```
i _roadClass;
i _formOfWay;
Q _roadID;
Q _clRoadID;
@"NSArray" _coordinates;
Q _connectingCLRoadID;
@"CLLocationCoordinate" _connectingRoadStartCoordinate;
@"CLLocationCoordinate" _connectingRoadEndCoordinate;
d _familiarityIndex;
d _sequenceNumber;
```

## Properties

```
@property (TQ,R,N,V_roadID) roadID;
@property (TQ,R,N,V_clRoadID) clRoadID;
@property (Ti,R,N,V_roadClass) roadClass;
@property (Ti,R,N,V_formOfWay) formOfWay;
@property (T@"NSArray",R,N,V_coordinates) coordinates;
@property (TQ,R,N,V_connectingCLRoadID) connectingCLRoadID;
@property (T@"CLLocationCoordinate",R,N,V_connectingRoadStartCoordinate) connectingRoadStartCoordinate;
@property (T@"CLLocationCoordinate",R,N,V_connectingRoadEndCoordinate) connectingRoadEndCoordinate;
@property (Td,R,N,V_familiarityIndex) familiarityIndex;
@property (Td,R,N,V_sequenceNumber) sequenceNumber;
```

## Class methods

```
+[CLTripSegmentRoadData supportsSecureCoding];
```

## Instance methods

```
-[CLTripSegmentRoadData roadID];
-[CLTripSegmentRoadData setSequenceNumber:];
-[CLTripSegmentRoadData dealloc];
-[CLTripSegmentRoadData sequenceNumber];
-[CLTripSegmentRoadData setFamiliarityIndex:];
-[CLTripSegmentRoadData encodeWithCoder:];
-[CLTripSegmentRoadData isValid];
-[CLTripSegmentRoadData description];
-[CLTripSegmentRoadData initWithCoder:];
-[CLTripSegmentRoadData familiarityIndex];
-[CLTripSegmentRoadData copyWithZone:];
-[CLTripSegmentRoadData coordinates];
-[CLTripSegmentRoadData formOfWay];
-[CLTripSegmentRoadData roadClass];
-[CLTripSegmentRoadData clRoadID];
-[CLTripSegmentRoadData connectingCLRoadID];
-[CLTripSegmentRoadData connectingRoadEndCoordinate];
-[CLTripSegmentRoadData connectingRoadStartCoordinate];
-[CLTripSegmentRoadData getLength];
-[CLTripSegmentRoadData initWithRoadID:clRoadID:roadClass:formOfWay:coordinates:];
-[CLTripSegmentRoadData isEqualStartLatitude:startLongitude:endLatitude:endlongitude:];
-[CLTripSegmentRoadData setConnectingCLRoadID:];
-[CLTripSegmentRoadData setConnectingRoadStartCoordinate:endCoordinate:];
```
