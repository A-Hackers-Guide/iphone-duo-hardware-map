# `TUAdhocResult`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSearchResult`
- 2 instance variables, 17 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"TUSearchController" _searchController;
@"NSString" _value;
```

## Properties

```
@property (T@"NSString",&,N,V_value) value;
@property (T@"TUSearchController",W,V_searchController) searchController;
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
-[TUAdhocResult isoCountryCode];
-[TUAdhocResult initWithString:];
-[TUAdhocResult setSearchController:];
-[TUAdhocResult searchController];
-[TUAdhocResult displayName];
-[TUAdhocResult value];
-[TUAdhocResult setValue:];
-[TUAdhocResult handles];
-[TUAdhocResult destinationId];
-[TUAdhocResult backingContact];
-[TUAdhocResult backingContactId];
-[TUAdhocResult backingContactIdentifier];
-[TUAdhocResult callerId];
-[TUAdhocResult idsCanonicalDestinations];
-[TUAdhocResult mostRecentCallType];
-[TUAdhocResult mostRecentCallWasMissed];
```
