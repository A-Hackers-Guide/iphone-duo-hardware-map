# `CSDMessagingHandle`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _isoCountryCode;
@"NSString" _siriDisplayName;
i _type;
@"NSString" _value;
{?="type"b1} _has;
```

## Properties

```
@property (T@"TUHandle",R,N) tuHandle;
@property (TB,N) hasType;
@property (Ti,N,V_type) type;
@property (TB,R,N) hasValue;
@property (T@"NSString",&,N,V_value) value;
@property (TB,R,N) hasIsoCountryCode;
@property (T@"NSString",&,N,V_isoCountryCode) isoCountryCode;
@property (TB,R,N) hasSiriDisplayName;
@property (T@"NSString",&,N,V_siriDisplayName) siriDisplayName;
```

## Class methods

```
+[CSDMessagingHandle handleWithTUHandle:];
```

## Instance methods

```
-[CSDMessagingHandle isoCountryCode];
-[CSDMessagingHandle setIsoCountryCode:];
-[CSDMessagingHandle writeTo:];
-[CSDMessagingHandle typeAsString:];
-[CSDMessagingHandle setHasType:];
-[CSDMessagingHandle mergeFrom:];
-[CSDMessagingHandle value];
-[CSDMessagingHandle hasType];
-[CSDMessagingHandle StringAsType:];
-[CSDMessagingHandle setValue:];
-[CSDMessagingHandle setType:];
-[CSDMessagingHandle type];
-[CSDMessagingHandle hash];
-[CSDMessagingHandle copyTo:];
-[CSDMessagingHandle description];
-[CSDMessagingHandle hasValue];
-[CSDMessagingHandle siriDisplayName];
-[CSDMessagingHandle readFrom:];
-[CSDMessagingHandle copyWithZone:];
-[CSDMessagingHandle isEqual:];
-[CSDMessagingHandle dictionaryRepresentation];
-[CSDMessagingHandle setSiriDisplayName:];
-[CSDMessagingHandle hasIsoCountryCode];
-[CSDMessagingHandle hasSiriDisplayName];
-[CSDMessagingHandle tuHandle];
```
