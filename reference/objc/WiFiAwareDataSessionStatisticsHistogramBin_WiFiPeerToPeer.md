# `WiFiAwareDataSessionStatisticsHistogramBin`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _binStart;
d _binEnd;
d _value;
```

## Properties

```
@property (Td,N,V_value) value;
@property (Td,R,N,V_binStart) binStart;
@property (Td,R,N,V_binEnd) binEnd;
```

## Class methods

```
+[WiFiAwareDataSessionStatisticsHistogramBin supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwareDataSessionStatisticsHistogramBin value];
-[WiFiAwareDataSessionStatisticsHistogramBin setValue:];
-[WiFiAwareDataSessionStatisticsHistogramBin encodeWithCoder:];
-[WiFiAwareDataSessionStatisticsHistogramBin description];
-[WiFiAwareDataSessionStatisticsHistogramBin initWithCoder:];
-[WiFiAwareDataSessionStatisticsHistogramBin isEqual:];
-[WiFiAwareDataSessionStatisticsHistogramBin binEnd];
-[WiFiAwareDataSessionStatisticsHistogramBin binStart];
-[WiFiAwareDataSessionStatisticsHistogramBin initWithBinStart:binEnd:value:];
```
