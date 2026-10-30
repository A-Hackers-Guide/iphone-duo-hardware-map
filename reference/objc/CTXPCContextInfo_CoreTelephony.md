# `CTXPCContextInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"NSString" _accountID;
q _slotID;
@"NSString" _labelID;
@"NSString" _label;
@"NSString" _phoneNumber;
```

## Properties

```
@property (T@"NSString",&,N,V_labelID) labelID;
@property (T@"NSString",&,N,V_label) label;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"NSString",R,N,V_accountID) accountID;
@property (Tq,R,N,V_slotID) slotID;
```

## Class methods

```
+[CTXPCContextInfo supportsSecureCoding];
+[CTXPCContextInfo contextWithUUID:andAccountID:andSlot:];
```

## Instance methods

```
-[CTXPCContextInfo phoneNumber];
-[CTXPCContextInfo uuid];
-[CTXPCContextInfo label];
-[CTXPCContextInfo setLabel:];
-[CTXPCContextInfo accountID];
-[CTXPCContextInfo setPhoneNumber:];
-[CTXPCContextInfo encodeWithCoder:];
-[CTXPCContextInfo slotID];
-[CTXPCContextInfo description];
-[CTXPCContextInfo initWithCoder:];
-[CTXPCContextInfo copyWithZone:];
-[CTXPCContextInfo context];
-[CTXPCContextInfo isEqual:];
-[CTXPCContextInfo labelID];
-[CTXPCContextInfo setLabelID:];
-[CTXPCContextInfo initWithUUID:andAccountID:andSlot:];
```
