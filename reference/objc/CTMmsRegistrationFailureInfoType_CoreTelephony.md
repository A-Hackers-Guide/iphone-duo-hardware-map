# `CTMmsRegistrationFailureInfoType`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _dataActive;
B _isDataAttached;
B _activationForMms;
@"NSNumber" _pdpContextId;
```

## Properties

```
@property (T@"NSNumber",&,N,V_pdpContextId) pdpContextId;
@property (TB,N,V_dataActive) dataActive;
@property (TB,N,V_isDataAttached) isDataAttached;
@property (TB,N,V_activationForMms) activationForMms;
```

## Class methods

```
+[CTMmsRegistrationFailureInfoType supportsSecureCoding];
```

## Instance methods

```
-[CTMmsRegistrationFailureInfoType init];
-[CTMmsRegistrationFailureInfoType setDataActive:];
-[CTMmsRegistrationFailureInfoType encodeWithCoder:];
-[CTMmsRegistrationFailureInfoType initWithCoder:];
-[CTMmsRegistrationFailureInfoType dataActive];
-[CTMmsRegistrationFailureInfoType copyWithZone:];
-[CTMmsRegistrationFailureInfoType isEqual:];
-[CTMmsRegistrationFailureInfoType activationForMms];
-[CTMmsRegistrationFailureInfoType isDataAttached];
-[CTMmsRegistrationFailureInfoType isEqualToCTMmsRegistrationFailureInfoType:];
-[CTMmsRegistrationFailureInfoType pdpContextId];
-[CTMmsRegistrationFailureInfoType setActivationForMms:];
-[CTMmsRegistrationFailureInfoType setIsDataAttached:];
-[CTMmsRegistrationFailureInfoType setPdpContextId:];
```
