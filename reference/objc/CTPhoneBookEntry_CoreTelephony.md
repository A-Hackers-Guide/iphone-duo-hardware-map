# `CTPhoneBookEntry`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isHidden;
@"NSString" _name;
@"NSString" _number;
@"NSString" _altNumber;
@"NSString" _altText;
@"NSString" _email;
@"NSString" _group;
```

## Properties

```
@property (TB,N,V_isHidden) isHidden;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSString",&,N,V_number) number;
@property (T@"NSString",&,N,V_altNumber) altNumber;
@property (T@"NSString",&,N,V_altText) altText;
@property (T@"NSString",&,N,V_email) email;
@property (T@"NSString",&,N,V_group) group;
```

## Class methods

```
+[CTPhoneBookEntry supportsSecureCoding];
```

## Instance methods

```
-[CTPhoneBookEntry setIsHidden:];
-[CTPhoneBookEntry setGroup:];
-[CTPhoneBookEntry email];
-[CTPhoneBookEntry setNumber:];
-[CTPhoneBookEntry group];
-[CTPhoneBookEntry number];
-[CTPhoneBookEntry isHidden];
-[CTPhoneBookEntry encodeWithCoder:];
-[CTPhoneBookEntry description];
-[CTPhoneBookEntry setName:];
-[CTPhoneBookEntry initWithCoder:];
-[CTPhoneBookEntry copyWithZone:];
-[CTPhoneBookEntry name];
-[CTPhoneBookEntry altText];
-[CTPhoneBookEntry setAltText:];
-[CTPhoneBookEntry altNumber];
-[CTPhoneBookEntry setAltNumber:];
-[CTPhoneBookEntry setEmail:];
```
