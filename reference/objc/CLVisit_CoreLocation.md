# `CLVisit`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _arrivalDate;
@"NSDate" _departureDate;
d _horizontalAccuracy;
@"NSDate" _detectionDate;
@"_CLPlaceInference" __placeInference;
{CLLocationCoordinate2D="latitude"d"longitude"d} _coordinate;
```

## Properties

```
@property (TB,R,N) hasArrivalDate;
@property (TB,R,N) hasDepartureDate;
@property (T@"NSDate",R,C,N,V_detectionDate) detectionDate;
@property (T@"_CLPlaceInference",R,N,V__placeInference) _placeInference;
@property (T@"NSDate",R,C,N,V_arrivalDate) arrivalDate;
@property (T@"NSDate",R,C,N,V_departureDate) departureDate;
@property (T{CLLocationCoordinate2D=dd},R,N,V_coordinate) coordinate;
@property (Td,R,N,V_horizontalAccuracy) horizontalAccuracy;
```

## Class methods

```
+[CLVisit supportsSecureCoding];
```

## Instance methods

```
-[CLVisit arrivalDate];
-[CLVisit coordinate];
-[CLVisit detectionDate];
-[CLVisit departureDate];
-[CLVisit dealloc];
-[CLVisit horizontalAccuracy];
-[CLVisit hasDepartureDate];
-[CLVisit encodeWithCoder:];
-[CLVisit description];
-[CLVisit initWithCoder:];
-[CLVisit hasArrivalDate];
-[CLVisit copyWithZone:];
-[CLVisit _placeInference];
-[CLVisit initWithCoordinate:horizontalAccuracy:arrivalDate:departureDate:detectionDate:];
-[CLVisit initWithCoordinate:horizontalAccuracy:arrivalDate:departureDate:detectionDate:placeInference:];
```
