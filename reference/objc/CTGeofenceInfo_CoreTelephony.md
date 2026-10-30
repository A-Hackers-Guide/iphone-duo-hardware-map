# `CTGeofenceInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _longitude;
@"NSNumber" _latitude;
@"NSNumber" _radius;
@"NSString" _geofenceId;
```

## Properties

```
@property (T@"NSNumber",&,N,V_longitude) longitude;
@property (T@"NSNumber",&,N,V_latitude) latitude;
@property (T@"NSNumber",&,N,V_radius) radius;
@property (T@"NSString",&,N,V_geofenceId) geofenceId;
```

## Class methods

```
+[CTGeofenceInfo supportsSecureCoding];
```

## Instance methods

```
-[CTGeofenceInfo init];
-[CTGeofenceInfo setLatitude:];
-[CTGeofenceInfo latitude];
-[CTGeofenceInfo longitude];
-[CTGeofenceInfo setLongitude:];
-[CTGeofenceInfo setRadius:];
-[CTGeofenceInfo radius];
-[CTGeofenceInfo encodeWithCoder:];
-[CTGeofenceInfo description];
-[CTGeofenceInfo initWithCoder:];
-[CTGeofenceInfo copyWithZone:];
-[CTGeofenceInfo geofenceId];
-[CTGeofenceInfo setGeofenceId:];
```
