# `WiFiSettlementConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _maxScansWithoutMatchForUnsettlement;
Q _maxNetworksForSettlement;
d _lowConfidenceSettlementTime;
d _highConfidenceSettlementTime;
```

## Properties

```
@property (TQ,N,V_maxScansWithoutMatchForUnsettlement) maxScansWithoutMatchForUnsettlement;
@property (TQ,N,V_maxNetworksForSettlement) maxNetworksForSettlement;
@property (Td,N,V_lowConfidenceSettlementTime) lowConfidenceSettlementTime;
@property (Td,N,V_highConfidenceSettlementTime) highConfidenceSettlementTime;
```

## Instance methods

```
-[WiFiSettlementConfiguration init];
-[WiFiSettlementConfiguration description];
-[WiFiSettlementConfiguration setLowConfidenceSettlementTime:];
-[WiFiSettlementConfiguration highConfidenceSettlementTime];
-[WiFiSettlementConfiguration lowConfidenceSettlementTime];
-[WiFiSettlementConfiguration maxNetworksForSettlement];
-[WiFiSettlementConfiguration maxScansWithoutMatchForUnsettlement];
-[WiFiSettlementConfiguration setHighConfidenceSettlementTime:];
-[WiFiSettlementConfiguration setMaxNetworksForSettlement:];
-[WiFiSettlementConfiguration setMaxScansWithoutMatchForUnsettlement:];
```
