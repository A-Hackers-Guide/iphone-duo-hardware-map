# `CTSuppServicesNotificationData`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 15 instance variables, 15 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _callForwardingReason;
@"NSNumber" _callClass;
@"NSNumber" _enabled;
@"NSNumber" _active;
@"NSString" _callForwardingNumber;
@"NSNumber" _callForwardingNoReplyTime;
@"NSNumber" _mmiProcedure;
@"NSNumber" _callBarringFacility;
@"NSNumber" _supplementaryServiceType;
@"NSNumber" _callingLineIdRestriction;
@"NSNumber" _callingLineIdRestrictionModification;
@"NSNumber" _connectedLineIdRestriction;
@"NSNumber" _callingNamePresentation;
@"NSNumber" _connectedLinePresentation;
@"NSNumber" _callingLinePresentation;
```

## Properties

```
@property (T@"NSNumber",&,N,V_callForwardingReason) callForwardingReason;
@property (T@"NSNumber",&,N,V_callClass) callClass;
@property (T@"NSNumber",&,N,V_enabled) enabled;
@property (T@"NSNumber",&,N,V_active) active;
@property (T@"NSString",&,N,V_callForwardingNumber) callForwardingNumber;
@property (T@"NSNumber",&,N,V_callForwardingNoReplyTime) callForwardingNoReplyTime;
@property (T@"NSNumber",&,N,V_mmiProcedure) mmiProcedure;
@property (T@"NSNumber",&,N,V_callBarringFacility) callBarringFacility;
@property (T@"NSNumber",&,N,V_supplementaryServiceType) supplementaryServiceType;
@property (T@"NSNumber",&,N,V_callingLineIdRestriction) callingLineIdRestriction;
@property (T@"NSNumber",&,N,V_callingLineIdRestrictionModification) callingLineIdRestrictionModification;
@property (T@"NSNumber",&,N,V_connectedLineIdRestriction) connectedLineIdRestriction;
@property (T@"NSNumber",&,N,V_callingNamePresentation) callingNamePresentation;
@property (T@"NSNumber",&,N,V_connectedLinePresentation) connectedLinePresentation;
@property (T@"NSNumber",&,N,V_callingLinePresentation) callingLinePresentation;
```

## Class methods

```
+[CTSuppServicesNotificationData supportsSecureCoding];
```

## Instance methods

```
-[CTSuppServicesNotificationData active];
-[CTSuppServicesNotificationData callingLinePresentation];
-[CTSuppServicesNotificationData setCallingNamePresentation:];
-[CTSuppServicesNotificationData setCallingLinePresentation:];
-[CTSuppServicesNotificationData enabled];
-[CTSuppServicesNotificationData connectedLinePresentation];
-[CTSuppServicesNotificationData setCallingLineIdRestriction:];
-[CTSuppServicesNotificationData callBarringFacility];
-[CTSuppServicesNotificationData setActive:];
-[CTSuppServicesNotificationData setCallBarringFacility:];
-[CTSuppServicesNotificationData connectedLineIdRestriction];
-[CTSuppServicesNotificationData callForwardingNoReplyTime];
-[CTSuppServicesNotificationData callingLineIdRestrictionModification];
-[CTSuppServicesNotificationData supplementaryServiceType];
-[CTSuppServicesNotificationData callForwardingReason];
-[CTSuppServicesNotificationData setEnabled:];
-[CTSuppServicesNotificationData setMmiProcedure:];
-[CTSuppServicesNotificationData setCallForwardingReason:];
-[CTSuppServicesNotificationData setCallForwardingNumber:];
-[CTSuppServicesNotificationData encodeWithCoder:];
-[CTSuppServicesNotificationData setCallForwardingNoReplyTime:];
-[CTSuppServicesNotificationData callingNamePresentation];
-[CTSuppServicesNotificationData description];
-[CTSuppServicesNotificationData initWithCoder:];
-[CTSuppServicesNotificationData setCallClass:];
-[CTSuppServicesNotificationData callingLineIdRestriction];
-[CTSuppServicesNotificationData mmiProcedure];
-[CTSuppServicesNotificationData callForwardingNumber];
-[CTSuppServicesNotificationData callClass];
-[CTSuppServicesNotificationData setConnectedLineIdRestriction:];
-[CTSuppServicesNotificationData setCallingLineIdRestrictionModification:];
-[CTSuppServicesNotificationData copyWithZone:];
-[CTSuppServicesNotificationData setConnectedLinePresentation:];
-[CTSuppServicesNotificationData setSupplementaryServiceType:];
```
