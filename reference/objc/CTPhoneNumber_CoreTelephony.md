# `CTPhoneNumber`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `CTMessageAddress`
- 4 instance variables, 3 properties, 12 instance methods, 4 class methods

## Instance variables

```
@"NSString" _digits;
@"NSString" _countryCode;
B _isShortCode;
q _slot;
```

## Properties

```
@property (T@"NSString",R,V_digits) digits;
@property (T@"NSString",R,V_countryCode) countryCode;
@property (TB,V_isShortCode) isShortCode;
```

## Class methods

```
+[CTPhoneNumber phoneNumberWithDigits:countryCode:];
+[CTPhoneNumber isValidPhoneNumber:];
+[CTPhoneNumber isValidPhoneNumberChar:];
+[CTPhoneNumber phoneNumberWithDigits:digits:countryCode:];
```

## Instance methods

```
-[CTPhoneNumber encodedString];
-[CTPhoneNumber countryCode];
-[CTPhoneNumber copyWithZone:];
-[CTPhoneNumber digits];
-[CTPhoneNumber setIsShortCode:];
-[CTPhoneNumber canonicalFormat];
-[CTPhoneNumber formatForCallingCountry:];
-[CTPhoneNumber initWithDigits:countryCode:];
-[CTPhoneNumber initWithDigits:digits:countryCode:];
-[CTPhoneNumber isShortCode];
-[CTPhoneNumber numberOfDigitsForShortCodeNumber];
-[CTPhoneNumber numberOfDigitsForShortCodeNumber:];
```
