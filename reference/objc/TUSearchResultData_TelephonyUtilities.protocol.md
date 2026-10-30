# `TUSearchResultData` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R) displayName;
@property (T@"NSString",R) callerId;
@property (T@"CNContact",R) backingContact;
@property (T@"NSString",R) backingContactId;
@property (T@"NSString",R) backingContactIdentifier;
@property (T@"NSString",R) destinationId;
@property (T@"NSString",R) isoCountryCode;
@property (T@"NSArray",R) handles;
@property (Tq,R) mostRecentCallType;
@property (TB,R) mostRecentCallWasMissed;
```

## Instance methods

```
-[TUSearchResultData isoCountryCode];
-[TUSearchResultData displayName];
-[TUSearchResultData handles];
-[TUSearchResultData destinationId];
-[TUSearchResultData backingContact];
-[TUSearchResultData backingContactId];
-[TUSearchResultData backingContactIdentifier];
-[TUSearchResultData callerId];
-[TUSearchResultData mostRecentCallType];
-[TUSearchResultData mostRecentCallWasMissed];
```
