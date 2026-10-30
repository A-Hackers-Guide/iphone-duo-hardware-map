# `__CFN_ConnectionMetrics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 38 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} connectionLock;
B _needsCachedTCPInfoAtEnd;
B _needsCachedSubflowCounts;
B _TLSConfigured;
C _http3DiscoveryStatus;
B _cellular;
B _expensive;
B _constrained;
B _multipath;
B _usedTFO;
B _isUnlistedTracker;
B _reusedAfterAPSleepWake;
B _apSleepWakeMonitored;
B _usedByTransaction;
B _coalesced;
B _discretionary;
B _dataBudgetingEnabled;
S _negotiatedTLSProtocolVersion;
S _negotiatedTLSCipherSuite;
I _effectiveTrafficClass;
i _privacyStance;
@"NSObject<OS_nw_connection>" _connection;
@"NSDictionary" _cachedTCPInfoAtEnd;
@"NSDictionary" _cachedSubflowCounts;
@"NSUUID" _UUID;
Q _identifier;
d _beginTime;
d _establishTime;
d _firstByteReceivedTime;
d _endTime;
@"NSObject<OS_nw_endpoint>" _endpoint;
@"NSObject<OS_nw_endpoint>" _localEndpoint;
@"NSObject<OS_nw_endpoint>" _remoteEndpoint;
@"NSString" _interfaceName;
@"NSString" _networkProtocolName;
@"NSObject<OS_nw_establishment_report>" _establishmentReport;
d _idleAtTime;
{weak_ptr<TransportConnection>="__ptr_"^{TransportConnection}"__cntrl_"^{__shared_weak_count}} _transportConnection;
```

## Properties

```
@property (Td,R,N) _daemon_establishTime;
@property (T@"NSString",R,C,N) _daemon_interfaceName;
@property (TB,R,N,G_daemon_isDiscretionary) _daemon_discretionary;
@property (TB,R,N,G_daemon_isDataBudgetingEnabled) _daemon_dataBudgetingEnabled;
```

## Class methods

```
+[__CFN_ConnectionMetrics supportsSecureCoding];
```

## Instance methods

```
-[__CFN_ConnectionMetrics _daemon_interfaceName];
-[__CFN_ConnectionMetrics _daemon_isDataBudgetingEnabled];
-[__CFN_ConnectionMetrics _daemon_isDiscretionary];
-[__CFN_ConnectionMetrics encodeWithCoder:];
-[__CFN_ConnectionMetrics initWithCoder:];
-[__CFN_ConnectionMetrics _daemon_establishTime];
```
