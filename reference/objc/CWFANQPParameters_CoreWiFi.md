# `CWFANQPParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 8 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _includeMatchingKnownNetworkProfiles;
@"NSArray" _scanResults;
@"NSArray" _ANQPElementIDList;
Q _acceptableCacheAge;
Q _maximumAge;
Q _minimumTimestamp;
```

## Properties

```
@property (T@"NSArray",C,N,V_scanResults) scanResults;
@property (T@"NSArray",C,N,V_ANQPElementIDList) ANQPElementIDList;
@property (TQ,N,V_acceptableCacheAge) acceptableCacheAge;
@property (TQ,N,V_maximumAge) maximumAge;
@property (TQ,N,V_minimumTimestamp) minimumTimestamp;
@property (TQ,D,N) maximumCacheAge;
@property (TB,D,N) cacheOnly;
@property (TB,N,V_includeMatchingKnownNetworkProfiles) includeMatchingKnownNetworkProfiles;
```

## Class methods

```
+[CWFANQPParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFANQPParameters cacheOnly];
-[CWFANQPParameters ANQPElementIDList];
-[CWFANQPParameters setIncludeMatchingKnownNetworkProfiles:];
-[CWFANQPParameters scanResults];
-[CWFANQPParameters setANQPElementIDList:];
-[CWFANQPParameters acceptableCacheAge];
-[CWFANQPParameters setCacheOnly:];
-[CWFANQPParameters setScanResults:];
-[CWFANQPParameters minimumTimestamp];
-[CWFANQPParameters maximumCacheAge];
-[CWFANQPParameters includeMatchingKnownNetworkProfiles];
-[CWFANQPParameters encodeWithCoder:];
-[CWFANQPParameters hash];
-[CWFANQPParameters description];
-[CWFANQPParameters initWithCoder:];
-[CWFANQPParameters maximumAge];
-[CWFANQPParameters setMaximumCacheAge:];
-[CWFANQPParameters setAcceptableCacheAge:];
-[CWFANQPParameters setMaximumAge:];
-[CWFANQPParameters copyWithZone:];
-[CWFANQPParameters isEqual:];
-[CWFANQPParameters setMinimumTimestamp:];
-[CWFANQPParameters isEqualToANQPParameters:];
```
