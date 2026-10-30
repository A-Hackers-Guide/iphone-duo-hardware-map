# `CTRegistrationDisplayStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 5 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _isInHomeCountry;
B _changedDueToSimRemoval;
B _isRegistrationForcedHome;
B _isSatelliteSystem;
@"NSString" _registrationDisplayStatus;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSString",&,N,V_registrationDisplayStatus) registrationDisplayStatus;
@property (TB,N,V_isInHomeCountry) isInHomeCountry;
@property (TB,N,V_changedDueToSimRemoval) changedDueToSimRemoval;
@property (TB,N,V_isRegistrationForcedHome) isRegistrationForcedHome;
@property (TB,N,V_isSatelliteSystem) isSatelliteSystem;
```

## Class methods

```
+[CTRegistrationDisplayStatus supportsSecureCoding];
```

## Instance methods

```
-[CTRegistrationDisplayStatus isSatelliteSystem];
-[CTRegistrationDisplayStatus ct_shortDescription];
-[CTRegistrationDisplayStatus ct_shortName];
-[CTRegistrationDisplayStatus registrationDisplayStatus];
-[CTRegistrationDisplayStatus isRegistrationForcedHome];
-[CTRegistrationDisplayStatus setIsRegistrationForcedHome:];
-[CTRegistrationDisplayStatus setChangedDueToSimRemoval:];
-[CTRegistrationDisplayStatus changedDueToSimRemoval];
-[CTRegistrationDisplayStatus encodeWithCoder:];
-[CTRegistrationDisplayStatus description];
-[CTRegistrationDisplayStatus initWithCoder:];
-[CTRegistrationDisplayStatus copyWithZone:];
-[CTRegistrationDisplayStatus setIsSatelliteSystem:];
-[CTRegistrationDisplayStatus isInHomeCountry];
-[CTRegistrationDisplayStatus setIsInHomeCountry:];
-[CTRegistrationDisplayStatus setRegistrationDisplayStatus:];
```
