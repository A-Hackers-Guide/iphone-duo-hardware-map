# `TUContinuitySessionContact`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"CNContact" _contact;
@"NSString" _contactIdentifier;
@"NSSet" _anonyms;
```

## Properties

```
@property (T@"CNContact",R,N,V_contact) contact;
@property (T@"NSString",R,N,V_contactIdentifier) contactIdentifier;
@property (T@"NSSet",R,N,V_anonyms) anonyms;
@property (T@"NSString",R,N) displayName;
```

## Class methods

```
+[TUContinuitySessionContact supportsSecureCoding];
```

## Instance methods

```
-[TUContinuitySessionContact contact];
-[TUContinuitySessionContact contactIdentifier];
-[TUContinuitySessionContact displayName];
-[TUContinuitySessionContact encodeWithCoder:];
-[TUContinuitySessionContact description];
-[TUContinuitySessionContact initWithCoder:];
-[TUContinuitySessionContact anonyms];
-[TUContinuitySessionContact initWithContact:contactIdentifier:anonyms:];
```
