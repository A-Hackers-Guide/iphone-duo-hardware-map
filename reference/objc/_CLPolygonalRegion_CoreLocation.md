# `_CLPolygonalRegion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLRegion`
- 3 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _allowMonitoringWhileNearby;
i _geoReferenceFrame;
@"NSArray" _vertices;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_vertices) vertices;
@property (Ti,V_geoReferenceFrame) geoReferenceFrame;
@property (TB,R,N,V_allowMonitoringWhileNearby) allowMonitoringWhileNearby;
```

## Class methods

```
+[_CLPolygonalRegion supportsSecureCoding];
```

## Instance methods

```
-[_CLPolygonalRegion dealloc];
-[_CLPolygonalRegion setGeoReferenceFrame:];
-[_CLPolygonalRegion geoReferenceFrame];
-[_CLPolygonalRegion encodeWithCoder:];
-[_CLPolygonalRegion allowMonitoringWhileNearby];
-[_CLPolygonalRegion description];
-[_CLPolygonalRegion initWithCoder:];
-[_CLPolygonalRegion containsCoordinate:];
-[_CLPolygonalRegion copyWithZone:];
-[_CLPolygonalRegion containsCoordinate:withDistanceToBorder:];
-[_CLPolygonalRegion initNearbyAllowedWithVertices:identifier:];
-[_CLPolygonalRegion initWithVertices:identifier:];
-[_CLPolygonalRegion pointInPolygonWithCoordinate:withDistanceToBorder:];
-[_CLPolygonalRegion vertices];
```
