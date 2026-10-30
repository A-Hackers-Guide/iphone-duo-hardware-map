# `CLRacingRouteParameters`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _routeMatrixIndexVec;
@"CLRacingRouteVariables" _racingRouteVariables;
@"CLRacingRouteState" _startPointOnCurrentRoute;
@"CLRacingRouteState" _startPointOnReferenceRoute;
@"CLRacingRouteState" _lastOnRouteDataPoint;
@"CLRacingRouteState" _lastProjectedDataPoint;
@"CLRouteBoundingBox" _routeBoundingBox;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_routeMatrixIndexVec) routeMatrixIndexVec;
@property (T@"CLRacingRouteVariables",R,C,N,V_racingRouteVariables) racingRouteVariables;
@property (T@"CLRacingRouteState",R,C,N,V_startPointOnCurrentRoute) startPointOnCurrentRoute;
@property (T@"CLRacingRouteState",R,C,N,V_startPointOnReferenceRoute) startPointOnReferenceRoute;
@property (T@"CLRacingRouteState",R,C,N,V_lastOnRouteDataPoint) lastOnRouteDataPoint;
@property (T@"CLRacingRouteState",R,C,N,V_lastProjectedDataPoint) lastProjectedDataPoint;
@property (T@"CLRouteBoundingBox",R,C,N,V_routeBoundingBox) routeBoundingBox;
```

## Class methods

```
+[CLRacingRouteParameters supportsSecureCoding];
```

## Instance methods

```
-[CLRacingRouteParameters encodeWithCoder:];
-[CLRacingRouteParameters initWithCoder:];
-[CLRacingRouteParameters copyWithZone:];
-[CLRacingRouteParameters initWithRouteMatrixIndexVec:racingRouteVariables:startPointOnCurrentRoute:startPointOnReferenceRoute:lastOnRouteDataPoint:lastProjectedDataPoint:routeBoundingBox:];
-[CLRacingRouteParameters lastOnRouteDataPoint];
-[CLRacingRouteParameters lastProjectedDataPoint];
-[CLRacingRouteParameters racingRouteVariables];
-[CLRacingRouteParameters routeBoundingBox];
-[CLRacingRouteParameters routeMatrixIndexVec];
-[CLRacingRouteParameters startPointOnCurrentRoute];
-[CLRacingRouteParameters startPointOnReferenceRoute];
```
