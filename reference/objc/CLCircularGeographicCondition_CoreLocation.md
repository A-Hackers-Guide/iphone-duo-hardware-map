# `CLCircularGeographicCondition`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLCondition`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _requiresWirelessClientInfo;
d _radius;
{CLLocationCoordinate2D="latitude"d"longitude"d} _center;
```

## Properties

```
@property (TB,N,V_requiresWirelessClientInfo) requiresWirelessClientInfo;
@property (T{CLLocationCoordinate2D=dd},R,V_center) center;
@property (Td,R,V_radius) radius;
```

## Class methods

```
+[CLCircularGeographicCondition supportsSecureCoding];
```

## Instance methods

```
-[CLCircularGeographicCondition radius];
-[CLCircularGeographicCondition center];
-[CLCircularGeographicCondition encodeWithCoder:];
-[CLCircularGeographicCondition hash];
-[CLCircularGeographicCondition description];
-[CLCircularGeographicCondition initWithCoder:];
-[CLCircularGeographicCondition copyWithZone:];
-[CLCircularGeographicCondition isEqual:];
-[CLCircularGeographicCondition initWithCenter:radius:];
-[CLCircularGeographicCondition requiresWirelessClientInfo];
-[CLCircularGeographicCondition setRequiresWirelessClientInfo:];
```
