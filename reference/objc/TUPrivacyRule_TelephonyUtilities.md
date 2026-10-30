# `TUPrivacyRule`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 4 instance variables, 4 properties, 10 instance methods, 3 class methods

## Instance variables

```
i _type;
@"TUPhoneNumber" _phoneNumber;
@"NSString" _email;
@"NSString" _businessID;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (T@"TUPhoneNumber",R,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",R,N,V_email) email;
@property (T@"NSString",R,N,V_businessID) businessID;
```

## Class methods

```
+[TUPrivacyRule ruleForBusinessID:];
+[TUPrivacyRule ruleForEmail:];
+[TUPrivacyRule ruleForPhoneNumber:];
```

## Instance methods

```
-[TUPrivacyRule phoneNumber];
-[TUPrivacyRule businessID];
-[TUPrivacyRule email];
-[TUPrivacyRule type];
-[TUPrivacyRule encodeWithCoder:];
-[TUPrivacyRule initWithCoder:];
-[TUPrivacyRule isEqual:];
-[TUPrivacyRule initForBusinessID:];
-[TUPrivacyRule initForEmail:];
-[TUPrivacyRule initForPhoneNumber:];
```
