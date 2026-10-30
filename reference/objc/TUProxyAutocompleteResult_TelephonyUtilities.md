# `TUProxyAutocompleteResult`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSearchResult`
- 1 instance variables, 16 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"CNAutocompleteResult" _autocompleteResult;
```

## Properties

```
@property (T@"CNAutocompleteResult",&,N,V_autocompleteResult) autocompleteResult;
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R) idsCanonicalDestinations;
```

## Instance methods

```
-[TUProxyAutocompleteResult isoCountryCode];
-[TUProxyAutocompleteResult init];
-[TUProxyAutocompleteResult displayName];
-[TUProxyAutocompleteResult handles];
-[TUProxyAutocompleteResult autocompleteResult];
-[TUProxyAutocompleteResult destinationId];
-[TUProxyAutocompleteResult backingContact];
-[TUProxyAutocompleteResult backingContactId];
-[TUProxyAutocompleteResult backingContactIdentifier];
-[TUProxyAutocompleteResult callerId];
-[TUProxyAutocompleteResult idsCanonicalDestinations];
-[TUProxyAutocompleteResult initWithAutocompleteResult:];
-[TUProxyAutocompleteResult mostRecentCallType];
-[TUProxyAutocompleteResult mostRecentCallWasMissed];
-[TUProxyAutocompleteResult setAutocompleteResult:];
```
