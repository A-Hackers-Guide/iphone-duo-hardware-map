# `CLCircularRegion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLRegion`
- 6 instance variables, 8 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _isLowPower;
B _allowMonitoringWhileNearby;
i _geoReferenceFrame;
d _geoRadius;
d _desiredAccuracy;
{CLLocationCoordinate2D="latitude"d"longitude"d} _geoCenter;
```

## Properties

```
@property (T{CLLocationCoordinate2D=dd},R,N,V_geoCenter) geoCenter;
@property (Td,R,N,V_geoRadius) geoRadius;
@property (Ti,N,V_geoReferenceFrame) geoReferenceFrame;
@property (TB,R,N,V_isLowPower) isLowPower;
@property (Td,R,N,V_desiredAccuracy) desiredAccuracy;
@property (TB,R,N,V_allowMonitoringWhileNearby) allowMonitoringWhileNearby;
@property (T{CLLocationCoordinate2D=dd},R) center;
@property (Td,R) radius;
```

## Class methods

```
+[CLCircularRegion supportsSecureCoding];
```

## Instance methods

```
-[CLCircularRegion initNearbyAllowedWithCenter:radius:identifier:];
-[CLCircularRegion initWithCenter:radius:referenceFrame:allowMonitoringWhenNearby:lowPower:identifier:onBehalfOfBundleId:notifyOnEntry:notifyOnExit:conservativeEntry:emergency:requiresWirelessClientInfo:];
-[CLCircularRegion setGeoReferenceFrame:];
-[CLCircularRegion referenceFrame];
-[CLCircularRegion initWithCenter:radius:identifier:];
-[CLCircularRegion geoReferenceFrame];
-[CLCircularRegion initForLowPowerWithCenter:radius:identifier:];
-[CLCircularRegion geoRadius];
-[CLCircularRegion radius];
-[CLCircularRegion initWithCenter:radius:identifier:onBehalfOfBundleId:];
-[CLCircularRegion center];
-[CLCircularRegion encodeWithCoder:];
-[CLCircularRegion isLowPower];
-[CLCircularRegion initWithCenter:radius:identifier:nearbyAllowed:];
-[CLCircularRegion allowMonitoringWhileNearby];
-[CLCircularRegion hash];
-[CLCircularRegion initLegacyObjectWithCoder:];
-[CLCircularRegion description];
-[CLCircularRegion initWithCoder:];
-[CLCircularRegion containsCoordinate:];
-[CLCircularRegion desiredAccuracy];
-[CLCircularRegion copyWithZone:];
-[CLCircularRegion initWithCenter:radius:referenceFrame:allowMonitoringWhenNearby:lowPower:identifier:onBehalfOfBundleId:notifyOnEntry:notifyOnExit:conservativeEntry:emergency:requiresWirelessClientInfo:deviceId:handoffTag:];
-[CLCircularRegion geoCenter];
-[CLCircularRegion isEqual:];
-[CLCircularRegion setReferenceFrame:];
```
