# `SRVisit`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `SRSampling`
- 5 instance variables, 10 properties, 17 instance methods, 1 class methods

## Instance variables

```
d _distanceFromHome;
@"NSDateInterval" _arrivalDateInterval;
@"NSDateInterval" _departureDateInterval;
q _locationCategory;
@"NSUUID" _identifier;
```

## Properties

```
@property (T@"NSString",R,C) label;
@property (Td,R,V_distanceFromHome) distanceFromHome;
@property (T@"NSDateInterval",R,V_arrivalDateInterval) arrivalDateInterval;
@property (T@"NSDateInterval",R,V_departureDateInterval) departureDateInterval;
@property (Tq,R,V_locationCategory) locationCategory;
@property (T@"NSUUID",R,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRVisit supportsSecureCoding];
```

## Instance methods

```
-[SRVisit identifier];
-[SRVisit label];
-[SRVisit dealloc];
-[SRVisit distanceFromHome];
-[SRVisit encodeWithCoder:];
-[SRVisit hash];
-[SRVisit description];
-[SRVisit initWithCoder:];
-[SRVisit copyWithZone:];
-[SRVisit isEqual:];
-[SRVisit binarySampleRepresentation];
-[SRVisit initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRVisit sr_dictionaryRepresentation];
-[SRVisit locationCategory];
-[SRVisit arrivalDateInterval];
-[SRVisit departureDateInterval];
-[SRVisit initWithDistanceFromHome:arrive:depart:category:uuid:];
```
