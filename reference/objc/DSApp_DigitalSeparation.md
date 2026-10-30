# `DSApp`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSMutableCopying`
- 4 instance variables, 4 properties, 11 instance methods, 4 class methods

## Instance variables

```
@"NSString" _displayName;
@"NSString" _appID;
@"NSMutableSet" _permissionsGranted;
Q _locationAuthorization;
```

## Properties

```
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSString",C,N,V_appID) appID;
@property (T@"NSMutableSet",&,N,V_permissionsGranted) permissionsGranted;
@property (TQ,N,V_locationAuthorization) locationAuthorization;
```

## Class methods

```
+[DSApp app:hasPermission:];
+[DSApp app:hasPermissionAcceptingAnyLocationAuthorization:];
+[DSApp appHasNoPermissions:];
+[DSApp skipTCCCheck:];
```

## Instance methods

```
-[DSApp setAppID:];
-[DSApp appID];
-[DSApp mutableCopyWithZone:];
-[DSApp compare:];
-[DSApp displayName];
-[DSApp setDisplayName:];
-[DSApp setLocationAuthorization:];
-[DSApp locationAuthorization];
-[DSApp hasLocationAccess];
-[DSApp permissionsGranted];
-[DSApp setPermissionsGranted:];
```
