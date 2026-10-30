# `TUProxyRecentCall`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUSearchResult`
- 2 instance variables, 18 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CHRecentCall" _recentCall;
@"TUSearchController" _searchController;
```

## Properties

```
@property (T@"CHRecentCall",&,N,V_recentCall) recentCall;
@property (T@"NSString",R) mostRecentCallInfo;
@property (T@"TUSearchController",W,V_searchController) searchController;
@property (T@"NSString",R) displayName;
@property (T@"NSString",R,D) callerId;
@property (T@"CNContact",R) backingContact;
@property (T@"NSString",R) backingContactId;
@property (T@"NSString",R) backingContactIdentifier;
@property (T@"NSString",R) destinationId;
@property (T@"NSString",R,D) isoCountryCode;
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
-[TUProxyRecentCall setSearchController:];
-[TUProxyRecentCall init];
-[TUProxyRecentCall searchController];
-[TUProxyRecentCall displayName];
-[TUProxyRecentCall forwardingTargetForSelector:];
-[TUProxyRecentCall handles];
-[TUProxyRecentCall destinationId];
-[TUProxyRecentCall backingContact];
-[TUProxyRecentCall backingContactId];
-[TUProxyRecentCall backingContactIdentifier];
-[TUProxyRecentCall idsCanonicalDestinations];
-[TUProxyRecentCall initWithRecentCall:];
-[TUProxyRecentCall mostRecentCallInfo];
-[TUProxyRecentCall mostRecentCallType];
-[TUProxyRecentCall mostRecentCallWasMissed];
-[TUProxyRecentCall recentCall];
-[TUProxyRecentCall setRecentCall:];
```
