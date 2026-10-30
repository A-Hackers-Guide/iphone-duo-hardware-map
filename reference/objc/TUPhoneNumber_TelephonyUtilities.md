# `TUPhoneNumber`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSSecureCoding`
- 1 instance variables, 6 properties, 13 instance methods, 4 class methods

## Instance variables

```
^{__CFPhoneNumber=} _phoneNumberRef;
```

## Properties

```
@property (T^{__CFPhoneNumber=},V_phoneNumberRef) phoneNumberRef;
@property (T@"NSString",R,D) digits;
@property (T@"NSString",R,D) countryCode;
@property (T@"NSString",R,D) formattedRepresentation;
@property (T@"NSString",R,D) formattedInternationalRepresentation;
@property (T@"NSString",R,D) unformattedInternationalRepresentation;
```

## Class methods

```
+[TUPhoneNumber supportsSecureCoding];
+[TUPhoneNumber phoneNumberWithDigits:countryCode:];
+[TUPhoneNumber areDigits:equalToDigits:usingCountryCode:];
+[TUPhoneNumber phoneNumberWithCFPhoneNumberRef:];
```

## Instance methods

```
-[TUPhoneNumber dealloc];
-[TUPhoneNumber countryCode];
-[TUPhoneNumber encodeWithCoder:];
-[TUPhoneNumber initWithCoder:];
-[TUPhoneNumber isEqual:];
-[TUPhoneNumber digits];
-[TUPhoneNumber phoneNumberRef];
-[TUPhoneNumber initWithDigits:countryCode:];
-[TUPhoneNumber formattedInternationalRepresentation];
-[TUPhoneNumber formattedRepresentation];
-[TUPhoneNumber initWithCFPhoneNumberRef:];
-[TUPhoneNumber setPhoneNumberRef:];
-[TUPhoneNumber unformattedInternationalRepresentation];
```
