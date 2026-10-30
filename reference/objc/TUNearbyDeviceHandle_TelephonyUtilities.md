# `TUNearbyDeviceHandle`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
@"NSDictionary" _knownIdentifiersByHandleType;
@"NSString" _name;
q _deviceModel;
@"TUNearbyDeviceHandleCapabilities" _capabilities;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_accessorLock) accessorLock;
@property (T@"NSDictionary",R,N,V_knownIdentifiersByHandleType) knownIdentifiersByHandleType;
@property (T@"NSDictionary",R,N) plistRepresentation;
@property (T@"NSString",R,C,N,V_name) name;
@property (Tq,R,N,V_deviceModel) deviceModel;
@property (T@"TUNearbyDeviceHandleCapabilities",R,N,V_capabilities) capabilities;
```

## Class methods

```
+[TUNearbyDeviceHandle supportsSecureCoding];
```

## Instance methods

```
-[TUNearbyDeviceHandle accessorLock];
-[TUNearbyDeviceHandle deviceModel];
-[TUNearbyDeviceHandle encodeWithCoder:];
-[TUNearbyDeviceHandle plistRepresentation];
-[TUNearbyDeviceHandle capabilities];
-[TUNearbyDeviceHandle hash];
-[TUNearbyDeviceHandle description];
-[TUNearbyDeviceHandle initWithCoder:];
-[TUNearbyDeviceHandle copyWithZone:];
-[TUNearbyDeviceHandle isEqual:];
-[TUNearbyDeviceHandle name];
-[TUNearbyDeviceHandle initWithType:identifier:name:];
-[TUNearbyDeviceHandle identifierDescription];
-[TUNearbyDeviceHandle identifierWithType:];
-[TUNearbyDeviceHandle initWithName:knownIdentifiers:];
-[TUNearbyDeviceHandle initWithName:knownIdentifiers:deviceModel:];
-[TUNearbyDeviceHandle initWithName:knownIdentifiers:deviceModel:capabilities:];
-[TUNearbyDeviceHandle initWithType:identifier:name:capabilities:];
-[TUNearbyDeviceHandle isEqualToDeviceHandle:];
-[TUNearbyDeviceHandle isEquivalentToDeviceHandle:];
-[TUNearbyDeviceHandle knownIdentifiersByHandleType];
```
