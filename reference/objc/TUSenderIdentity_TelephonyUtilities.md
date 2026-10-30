# `TUSenderIdentity`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
@"NSUUID" _accountUUID;
@"TUHandle" _handle;
@"NSString" _ISOCountryCode;
@"NSString" _localizedName;
@"NSString" _localizedShortName;
@"NSString" _localizedServiceName;
```

## Properties

```
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (T@"NSUUID",R,N,V_accountUUID) accountUUID;
@property (T@"TUHandle",R,N,V_handle) handle;
@property (T@"NSString",R,C,N,V_ISOCountryCode) ISOCountryCode;
@property (T@"NSString",R,C,N,V_localizedName) localizedName;
@property (T@"NSString",R,C,N,V_localizedShortName) localizedShortName;
@property (T@"NSString",R,C,N,V_localizedServiceName) localizedServiceName;
```

## Class methods

```
+[TUSenderIdentity supportsSecureCoding];
```

## Instance methods

```
-[TUSenderIdentity localizedShortName];
-[TUSenderIdentity accountUUID];
-[TUSenderIdentity UUID];
-[TUSenderIdentity localizedName];
-[TUSenderIdentity handle];
-[TUSenderIdentity encodeWithCoder:];
-[TUSenderIdentity hash];
-[TUSenderIdentity description];
-[TUSenderIdentity initWithCoder:];
-[TUSenderIdentity copyWithZone:];
-[TUSenderIdentity isEqual:];
-[TUSenderIdentity ISOCountryCode];
-[TUSenderIdentity initWithUUID:accountUUID:localizedName:localizedShortName:localizedServiceName:handle:];
-[TUSenderIdentity initWithSenderIdentity:];
-[TUSenderIdentity initWithUUID:accountUUID:ISOCountryCode:localizedName:localizedShortName:localizedServiceName:handle:];
-[TUSenderIdentity initWithUUID:accountUUID:localizedName:localizedShortName:handle:];
-[TUSenderIdentity isEqualToSenderIdentity:];
-[TUSenderIdentity localizedServiceName];
```
