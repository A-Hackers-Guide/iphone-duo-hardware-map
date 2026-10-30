# `WiFiSettlementContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _creationDate;
@"NSArray" _strongestNetworks;
@"NSSet" _strongestBSSIDs;
Q _maxCount;
```

## Properties

```
@property (T@"NSArray",&,N,V_strongestNetworks) strongestNetworks;
@property (T@"NSSet",&,N,V_strongestBSSIDs) strongestBSSIDs;
@property (TQ,N,V_maxCount) maxCount;
@property (T@"NSDate",&,N,V_creationDate) creationDate;
```

## Class methods

```
+[WiFiSettlementContext networkQualifiesForSettlement:];
```

## Instance methods

```
-[WiFiSettlementContext maxCount];
-[WiFiSettlementContext creationDate];
-[WiFiSettlementContext setCreationDate:];
-[WiFiSettlementContext setMaxCount:];
-[WiFiSettlementContext strongestBSSIDs];
-[WiFiSettlementContext updateNetworks:];
-[WiFiSettlementContext _updateStrongestNetworks:];
-[WiFiSettlementContext compareWithScanResults:];
-[WiFiSettlementContext initWithNetworks:maxCount:];
-[WiFiSettlementContext setStrongestBSSIDs:];
-[WiFiSettlementContext setStrongestNetworks:];
-[WiFiSettlementContext strongestNetworks];
```
