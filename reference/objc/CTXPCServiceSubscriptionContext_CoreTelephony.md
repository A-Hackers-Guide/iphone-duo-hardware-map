# `CTXPCServiceSubscriptionContext`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTXPCLogging`, `NSCopying`, `NSSecureCoding`
- 11 instance variables, 13 properties, 32 instance methods, 5 class methods

## Instance variables

```
B _isSimPresent;
B _isSimGood;
B _isSimHidden;
B _isSimDataOnly;
q _slotID;
@"NSUUID" _uuid;
@"NSString" _labelID;
@"NSString" _label;
@"NSString" _phoneNumber;
@"NSNumber" _userDataPreferred;
@"NSNumber" _userDefaultVoice;
```

## Properties

```
@property (T@"NSString",R,N) ct_shortName;
@property (T@"NSString",R,N) ct_shortDescription;
@property (T@"NSString",&,N,V_labelID) labelID;
@property (T@"NSString",&,N,V_label) label;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSNumber",&,N,V_userDataPreferred) userDataPreferred;
@property (T@"NSNumber",&,N,V_userDefaultVoice) userDefaultVoice;
@property (TB,N,V_isSimPresent) isSimPresent;
@property (TB,N,V_isSimGood) isSimGood;
@property (TB,N,V_isSimHidden) isSimHidden;
@property (TB,N,V_isSimDataOnly) isSimDataOnly;
@property (Tq,R,N,V_slotID) slotID;
@property (T@"NSUUID",R,N,V_uuid) uuid;
```

## Class methods

```
+[CTXPCServiceSubscriptionContext supportsSecureCoding];
+[CTXPCServiceSubscriptionContext contextWithXPCContextInfo:];
+[CTXPCServiceSubscriptionContext contextWithServiceDescriptor:];
+[CTXPCServiceSubscriptionContext contextWithSlot:];
+[CTXPCServiceSubscriptionContext contextWithUUID:];
```

## Instance methods

```
-[CTXPCServiceSubscriptionContext phoneNumber];
-[CTXPCServiceSubscriptionContext ct_shortDescription];
-[CTXPCServiceSubscriptionContext uuid];
-[CTXPCServiceSubscriptionContext label];
-[CTXPCServiceSubscriptionContext setLabel:];
-[CTXPCServiceSubscriptionContext initWithUUID:];
-[CTXPCServiceSubscriptionContext ct_shortName];
-[CTXPCServiceSubscriptionContext setPhoneNumber:];
-[CTXPCServiceSubscriptionContext redactedDescription];
-[CTXPCServiceSubscriptionContext encodeWithCoder:];
-[CTXPCServiceSubscriptionContext slotID];
-[CTXPCServiceSubscriptionContext description];
-[CTXPCServiceSubscriptionContext initWithCoder:];
-[CTXPCServiceSubscriptionContext copyWithZone:];
-[CTXPCServiceSubscriptionContext context];
-[CTXPCServiceSubscriptionContext isEqual:];
-[CTXPCServiceSubscriptionContext initWithSlot:];
-[CTXPCServiceSubscriptionContext labelID];
-[CTXPCServiceSubscriptionContext isSimDataOnly];
-[CTXPCServiceSubscriptionContext isSimHidden];
-[CTXPCServiceSubscriptionContext setLabelID:];
-[CTXPCServiceSubscriptionContext userDataPreferred];
-[CTXPCServiceSubscriptionContext userDefaultVoice];
-[CTXPCServiceSubscriptionContext setIsSimHidden:];
-[CTXPCServiceSubscriptionContext initWithUUID:andSlot:];
-[CTXPCServiceSubscriptionContext isSimGood];
-[CTXPCServiceSubscriptionContext isSimPresent];
-[CTXPCServiceSubscriptionContext setIsSimDataOnly:];
-[CTXPCServiceSubscriptionContext setIsSimGood:];
-[CTXPCServiceSubscriptionContext setIsSimPresent:];
-[CTXPCServiceSubscriptionContext setUserDataPreferred:];
-[CTXPCServiceSubscriptionContext setUserDefaultVoice:];
```
