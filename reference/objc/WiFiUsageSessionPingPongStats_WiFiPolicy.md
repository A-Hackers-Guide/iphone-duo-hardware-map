# `WiFiUsageSessionPingPongStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _pingPongSequenceIsLowRssiOnly;
B _pingPongSequenceIsReassocOnly;
B _pingPongSequenceIsReassocOrLowRSSIOnly;
Q _pingPongNth;
@"NSArray" _sequence;
```

## Properties

```
@property (TQ,N,V_pingPongNth) pingPongNth;
@property (T@"NSArray",&,N,V_sequence) sequence;
@property (TB,N,V_pingPongSequenceIsLowRssiOnly) pingPongSequenceIsLowRssiOnly;
@property (TB,N,V_pingPongSequenceIsReassocOnly) pingPongSequenceIsReassocOnly;
@property (TB,N,V_pingPongSequenceIsReassocOrLowRSSIOnly) pingPongSequenceIsReassocOrLowRSSIOnly;
```

## Instance methods

```
-[WiFiUsageSessionPingPongStats sequence];
-[WiFiUsageSessionPingPongStats setSequence:];
-[WiFiUsageSessionPingPongStats setPingPongNth:];
-[WiFiUsageSessionPingPongStats initWithPingPongSequence:];
-[WiFiUsageSessionPingPongStats pingPongNth];
-[WiFiUsageSessionPingPongStats pingPongSequenceIsLowRssiOnly];
-[WiFiUsageSessionPingPongStats pingPongSequenceIsReassocOnly];
-[WiFiUsageSessionPingPongStats pingPongSequenceIsReassocOrLowRSSIOnly];
-[WiFiUsageSessionPingPongStats setPingPongSequenceIsLowRssiOnly:];
-[WiFiUsageSessionPingPongStats setPingPongSequenceIsReassocOnly:];
-[WiFiUsageSessionPingPongStats setPingPongSequenceIsReassocOrLowRSSIOnly:];
```
