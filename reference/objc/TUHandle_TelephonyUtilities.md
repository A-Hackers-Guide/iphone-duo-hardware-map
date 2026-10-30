# `TUHandle`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 8 properties, 33 instance methods, 16 class methods

## Instance variables

```
B _hasSetISOCountryCode;
q _type;
@"NSString" _value;
@"NSString" _siriDisplayName;
@"NSString" _isoCountryCode;
@"NSString" _normalizedValue;
```

## Properties

```
@property (TB,N,V_hasSetISOCountryCode) hasSetISOCountryCode;
@property (T@"NSString",C,N,V_isoCountryCode) isoCountryCode;
@property (T@"NSString",R,C,N,V_normalizedValue) normalizedValue;
@property (T@"NSDictionary",R,C,N) dictionaryRepresentation;
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_value) value;
@property (T@"NSString",C,V_siriDisplayName) siriDisplayName;
@property (TB,R,N,GshouldHideContact) shouldHideContact;
```

## Class methods

```
+[TUHandle supportsSecureCoding];
+[TUHandle normalizedEmailAddressHandleForValue:];
+[TUHandle handleWithPersonHandle:];
+[TUHandle handleWithDictionaryRepresentation:];
+[TUHandle handleWithPerson:];
+[TUHandle handleForCHRecentCall:validHandlesOnly:];
+[TUHandle handleWithDestinationID:];
+[TUHandle handlesForCHRecentCall:];
+[TUHandle handlesForCHRecentCall:validHandlesOnly:];
+[TUHandle normalizedPhoneNumberHandleForValue:isoCountryCode:];
+[TUHandle handleFromMessagingData:];
+[TUHandle handleForCHRecentCall:];
+[TUHandle normalizedHandleWithDestinationID:];
+[TUHandle handleTypeForCHHandle:];
+[TUHandle normalizedGenericHandleForValue:];
+[TUHandle stringForType:];
```

## Instance methods

```
-[TUHandle isoCountryCode];
-[TUHandle initWithType:value:];
-[TUHandle setIsoCountryCode:];
-[TUHandle initWithHandle:];
-[TUHandle hasSetISOCountryCode];
-[TUHandle init];
-[TUHandle initWithType:value:siriDisplayName:];
-[TUHandle setHasSetISOCountryCode:];
-[TUHandle value];
-[TUHandle isCanonicallyEqualToHandle:isoCountryCode:];
-[TUHandle messagingData];
-[TUHandle personHandle];
-[TUHandle shouldHideContact];
-[TUHandle setValue:];
-[TUHandle setType:];
-[TUHandle type];
-[TUHandle canonicalHandleForISOCountryCode:];
-[TUHandle encodeWithCoder:];
-[TUHandle isEquivalentToHandle:];
-[TUHandle isEqualToHandle:];
-[TUHandle hash];
-[TUHandle description];
-[TUHandle initWithCoder:];
-[TUHandle initWithType:value:normalizedValue:];
-[TUHandle siriDisplayName];
-[TUHandle normalizedValue];
-[TUHandle isValidForISOCountryCode:];
-[TUHandle copyWithZone:];
-[TUHandle isEqual:];
-[TUHandle shouldHideContactWithLockState:];
-[TUHandle initWithDestinationID:];
-[TUHandle dictionaryRepresentation];
-[TUHandle setSiriDisplayName:];
```
