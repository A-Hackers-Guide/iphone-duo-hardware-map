# `CTPhoneNumberInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isPresent;
B _isEditable;
B _isRead;
@"NSString" _label;
@"NSString" _number;
@"NSString" _displayPhoneNumber;
@"NSString" _altPhoneNumber;
```

## Properties

```
@property (T@"NSString",&,N,V_label) label;
@property (T@"NSString",&,N,V_number) number;
@property (T@"NSString",&,N,V_displayPhoneNumber) displayPhoneNumber;
@property (T@"NSString",&,N,V_altPhoneNumber) altPhoneNumber;
@property (TB,N,V_isPresent) isPresent;
@property (TB,N,V_isEditable) isEditable;
@property (TB,N,V_isRead) isRead;
```

## Class methods

```
+[CTPhoneNumberInfo supportsSecureCoding];
```

## Instance methods

```
-[CTPhoneNumberInfo isEditable];
-[CTPhoneNumberInfo isPresent];
-[CTPhoneNumberInfo setIsRead:];
-[CTPhoneNumberInfo label];
-[CTPhoneNumberInfo setNumber:];
-[CTPhoneNumberInfo setLabel:];
-[CTPhoneNumberInfo number];
-[CTPhoneNumberInfo displayPhoneNumber];
-[CTPhoneNumberInfo isRead];
-[CTPhoneNumberInfo setIsEditable:];
-[CTPhoneNumberInfo altPhoneNumber];
-[CTPhoneNumberInfo setIsPresent:];
-[CTPhoneNumberInfo encodeWithCoder:];
-[CTPhoneNumberInfo description];
-[CTPhoneNumberInfo initWithCoder:];
-[CTPhoneNumberInfo setAltPhoneNumber:];
-[CTPhoneNumberInfo copyWithZone:];
-[CTPhoneNumberInfo setDisplayPhoneNumber:];
```
