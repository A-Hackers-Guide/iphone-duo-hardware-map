# `TUContinuityFavorite`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"CNContact" _contact;
@"NSString" _contactIdentifier;
@"TUContinuityHandleAnonym" _anonym;
@"NSString" _actionType;
@"NSString" _bundleIdentifier;
```

## Properties

```
@property (T@"CNContact",R,N,V_contact) contact;
@property (T@"NSString",R,N,V_contactIdentifier) contactIdentifier;
@property (T@"TUContinuityHandleAnonym",R,N,V_anonym) anonym;
@property (T@"NSString",R,N) displayName;
@property (T@"NSString",R,N,V_actionType) actionType;
@property (T@"NSString",R,N,V_bundleIdentifier) bundleIdentifier;
```

## Class methods

```
+[TUContinuityFavorite supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityFavorite contact];
-[TUContinuityFavorite contactIdentifier];
-[TUContinuityFavorite displayName];
-[TUContinuityFavorite bundleIdentifier];
-[TUContinuityFavorite actionType];
-[TUContinuityFavorite encodeWithCoder:];
-[TUContinuityFavorite description];
-[TUContinuityFavorite initWithCoder:];
-[TUContinuityFavorite anonym];
-[TUContinuityFavorite initWithContact:contactIdentifier:anonym:actionType:bundleIdentifier:];
```
