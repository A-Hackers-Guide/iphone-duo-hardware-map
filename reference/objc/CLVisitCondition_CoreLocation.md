# `CLVisitCondition`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLCondition`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _poiCategory;
d _latitude;
d _longitude;
d _radius;
```

## Properties

```
@property (Tq,R,N,V_poiCategory) poiCategory;
@property (Td,R,N,V_latitude) latitude;
@property (Td,R,N,V_longitude) longitude;
@property (Td,R,N,V_radius) radius;
```

## Class methods

```
+[CLVisitCondition supportsSecureCoding];
```

## Instance methods

```
-[CLVisitCondition poiCategory];
-[CLVisitCondition latitude];
-[CLVisitCondition longitude];
-[CLVisitCondition radius];
-[CLVisitCondition encodeWithCoder:];
-[CLVisitCondition description];
-[CLVisitCondition initWithCoder:];
-[CLVisitCondition _initWithPoiCategory:latitude:longitude:radius:];
-[CLVisitCondition initWithPOICategory:];
```
