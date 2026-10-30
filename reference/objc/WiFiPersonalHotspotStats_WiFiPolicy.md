# `WiFiPersonalHotspotStats`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _successfulJoinAttempt;
d _joinStartedAt;
d _personalHotspotDiscoveryEndedAt;
d _joinEndedAt;
d _latency;
@"NSString" _joinReason;
@"NSString" _failureReporter;
q _joinFailureCode;
q _band;
@"NSString" _deviceName;
```

## Properties

```
@property (Td,R,N,V_joinStartedAt) joinStartedAt;
@property (Td,N,V_personalHotspotDiscoveryEndedAt) personalHotspotDiscoveryEndedAt;
@property (Td,R,N,V_joinEndedAt) joinEndedAt;
@property (Td,R,N,V_latency) latency;
@property (TB,R,N,V_successfulJoinAttempt) successfulJoinAttempt;
@property (T@"NSString",R,N,V_joinReason) joinReason;
@property (T@"NSString",R,N,V_failureReporter) failureReporter;
@property (Tq,R,N,V_joinFailureCode) joinFailureCode;
@property (Tq,R,N,V_band) band;
@property (T@"NSString",R,N,V_deviceName) deviceName;
```

## Class methods

```
+[WiFiPersonalHotspotStats sharedInstance];
```

## Instance methods

```
-[WiFiPersonalHotspotStats latency];
-[WiFiPersonalHotspotStats init];
-[WiFiPersonalHotspotStats joinStartedAt];
-[WiFiPersonalHotspotStats band];
-[WiFiPersonalHotspotStats joinEndedAt];
-[WiFiPersonalHotspotStats deviceName];
-[WiFiPersonalHotspotStats __resetWiFiPersonalHotspotStats];
-[WiFiPersonalHotspotStats failureReporter];
-[WiFiPersonalHotspotStats joinFailureCode];
-[WiFiPersonalHotspotStats personalHotspotDiscoveryEndedAt];
-[WiFiPersonalHotspotStats __submitWiFiPersonalHotspotStats:end:latencyType:];
-[WiFiPersonalHotspotStats joinReason];
-[WiFiPersonalHotspotStats setJoinEndedEvent:successfulJoinAttempt:joinFailureCode:failureReporter:band:deviceName:];
-[WiFiPersonalHotspotStats setJoinStartedEvent:withReason:deviceName:];
-[WiFiPersonalHotspotStats setPersonalHotspotDiscoveryEndedAt:];
-[WiFiPersonalHotspotStats successfulJoinAttempt];
```
