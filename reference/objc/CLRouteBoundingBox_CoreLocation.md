# `CLRouteBoundingBox`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
i _nRows;
i _nColumns;
d _minLatitude;
d _maxLatitude;
d _minLongitude;
d _maxLongitude;
```

## Properties

```
@property (Td,R,N,V_minLatitude) minLatitude;
@property (Td,R,N,V_maxLatitude) maxLatitude;
@property (Td,R,N,V_minLongitude) minLongitude;
@property (Td,R,N,V_maxLongitude) maxLongitude;
@property (Ti,R,N,V_nRows) nRows;
@property (Ti,R,N,V_nColumns) nColumns;
```

## Class methods

```
+[CLRouteBoundingBox supportsSecureCoding];
```

## Instance methods

```
-[CLRouteBoundingBox encodeWithCoder:];
-[CLRouteBoundingBox initWithCoder:];
-[CLRouteBoundingBox copyWithZone:];
-[CLRouteBoundingBox initWithMinLatitude:maxLatitude:minLongitude:maxLongitude:nRows:nColumns:];
-[CLRouteBoundingBox maxLatitude];
-[CLRouteBoundingBox maxLongitude];
-[CLRouteBoundingBox minLatitude];
-[CLRouteBoundingBox minLongitude];
-[CLRouteBoundingBox nColumns];
-[CLRouteBoundingBox nRows];
```
