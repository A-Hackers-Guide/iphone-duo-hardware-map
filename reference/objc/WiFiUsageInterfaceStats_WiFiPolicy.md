# `WiFiUsageInterfaceStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 14 instance methods, 4 class methods

## Instance variables

```
Q _txBytes;
Q _rxBytes;
Q _txL3Packets;
Q _rxL3Packets;
@"NSDate" _timestamp;
```

## Properties

```
@property (TQ,N,V_txBytes) txBytes;
@property (TQ,N,V_rxBytes) rxBytes;
@property (TQ,N,V_txL3Packets) txL3Packets;
@property (TQ,N,V_rxL3Packets) rxL3Packets;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
```

## Class methods

```
+[WiFiUsageInterfaceStats _statsFromMIB:];
+[WiFiUsageInterfaceStats _statsFromNetIF:];
+[WiFiUsageInterfaceStats netIFStatsForInterfaceName:];
+[WiFiUsageInterfaceStats statsForInterfaceName:];
```

## Instance methods

```
-[WiFiUsageInterfaceStats setTxL3Packets:];
-[WiFiUsageInterfaceStats setRxL3Packets:];
-[WiFiUsageInterfaceStats txL3Packets];
-[WiFiUsageInterfaceStats setTxBytes:];
-[WiFiUsageInterfaceStats rxL3Packets];
-[WiFiUsageInterfaceStats setRxBytes:];
-[WiFiUsageInterfaceStats setTimestamp:];
-[WiFiUsageInterfaceStats timestamp];
-[WiFiUsageInterfaceStats rxBytes];
-[WiFiUsageInterfaceStats isEqualToInterfaceStats:];
-[WiFiUsageInterfaceStats description];
-[WiFiUsageInterfaceStats copyWithZone:];
-[WiFiUsageInterfaceStats txBytes];
-[WiFiUsageInterfaceStats isEqual:];
```
