# `WiFiUsageSoftApSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 39 instance variables, 39 properties, 89 instance methods, 0 class methods

## Instance variables

```
B _compatibilityEnabled;
B _lastHiddenState;
@"NSString" _requester;
@"NSString" _status;
@"NSString" _tearDownReason;
@"NSDate" _lastAwdlActiveTime;
@"NSDate" _lastInfraActiveTime;
Q _appleClientConnectCount;
Q _otherClientConnectCount;
Q _hiddenClientConnectCount;
Q _broadcastClientConnectCount;
Q _twoFourGHzClientConnectCount;
Q _fiveGHzClientConnectCount;
Q _autoHotspotClientConnectCount;
Q _instantHotspotClientConnectCount;
Q _clientDisconnectCount;
Q _maxConnectedClientCount;
Q _lastChannel;
Q _twoFourGHzChannelCount;
Q _fiveGHzChannelCount;
d _lowPowerModeDurationSec;
d _dynamicPowerModeDurationSec;
d _infraActiveDuration;
d _awdlActiveDuration;
d _requestToUpLatency;
d _idleTimeBeforeTeardownSec;
d _idleTimeAfterLastClientDisconnectedSec;
Q _infraStateChangedCount;
Q _awdlStateChangedCount;
Q _knownNetworkScanCount;
Q _hiddenTransitionCount;
Q _bandTransitionCount;
Q _twoFourGHzDeniedChannelCount;
Q _fiveGHzDeniedUnii1ChannelCount;
Q _fiveGHzDeniedUnii2aChannelCount;
Q _fiveGHzDeniedUnii2cChannelCount;
Q _fiveGHzDeniedUnii3ChannelCount;
Q _appliedCountryCode;
@"NSMutableSet" _connectedClients;
```

## Properties

```
@property (T@"NSString",&,N,V_requester) requester;
@property (T@"NSString",&,N,V_status) status;
@property (T@"NSString",&,N,V_tearDownReason) tearDownReason;
@property (T@"NSDate",&,N,V_lastAwdlActiveTime) lastAwdlActiveTime;
@property (T@"NSDate",&,N,V_lastInfraActiveTime) lastInfraActiveTime;
@property (TB,N,V_compatibilityEnabled) compatibilityEnabled;
@property (TQ,N,V_appleClientConnectCount) appleClientConnectCount;
@property (TQ,N,V_otherClientConnectCount) otherClientConnectCount;
@property (TQ,N,V_hiddenClientConnectCount) hiddenClientConnectCount;
@property (TQ,N,V_broadcastClientConnectCount) broadcastClientConnectCount;
@property (TQ,N,V_twoFourGHzClientConnectCount) twoFourGHzClientConnectCount;
@property (TQ,N,V_fiveGHzClientConnectCount) fiveGHzClientConnectCount;
@property (TQ,N,V_autoHotspotClientConnectCount) autoHotspotClientConnectCount;
@property (TQ,N,V_instantHotspotClientConnectCount) instantHotspotClientConnectCount;
@property (TQ,N,V_clientDisconnectCount) clientDisconnectCount;
@property (TQ,N,V_maxConnectedClientCount) maxConnectedClientCount;
@property (TB,N,V_lastHiddenState) lastHiddenState;
@property (TQ,N,V_lastChannel) lastChannel;
@property (TQ,N,V_twoFourGHzChannelCount) twoFourGHzChannelCount;
@property (TQ,N,V_fiveGHzChannelCount) fiveGHzChannelCount;
@property (Td,N,V_lowPowerModeDurationSec) lowPowerModeDurationSec;
@property (Td,N,V_dynamicPowerModeDurationSec) dynamicPowerModeDurationSec;
@property (Td,N,V_infraActiveDuration) infraActiveDuration;
@property (Td,N,V_awdlActiveDuration) awdlActiveDuration;
@property (Td,N,V_requestToUpLatency) requestToUpLatency;
@property (Td,N,V_idleTimeBeforeTeardownSec) idleTimeBeforeTeardownSec;
@property (Td,N,V_idleTimeAfterLastClientDisconnectedSec) idleTimeAfterLastClientDisconnectedSec;
@property (TQ,N,V_infraStateChangedCount) infraStateChangedCount;
@property (TQ,N,V_awdlStateChangedCount) awdlStateChangedCount;
@property (TQ,N,V_knownNetworkScanCount) knownNetworkScanCount;
@property (TQ,N,V_hiddenTransitionCount) hiddenTransitionCount;
@property (TQ,N,V_bandTransitionCount) bandTransitionCount;
@property (TQ,N,V_twoFourGHzDeniedChannelCount) twoFourGHzDeniedChannelCount;
@property (TQ,N,V_fiveGHzDeniedUnii1ChannelCount) fiveGHzDeniedUnii1ChannelCount;
@property (TQ,N,V_fiveGHzDeniedUnii2aChannelCount) fiveGHzDeniedUnii2aChannelCount;
@property (TQ,N,V_fiveGHzDeniedUnii2cChannelCount) fiveGHzDeniedUnii2cChannelCount;
@property (TQ,N,V_fiveGHzDeniedUnii3ChannelCount) fiveGHzDeniedUnii3ChannelCount;
@property (TQ,N,V_appliedCountryCode) appliedCountryCode;
@property (T@"NSMutableSet",&,N,V_connectedClients) connectedClients;
```

## Instance methods

```
-[WiFiUsageSoftApSession twoFourGHzChannelCount];
-[WiFiUsageSoftApSession setAutoHotspotClientConnectCount:];
-[WiFiUsageSoftApSession lowPowerModeDurationSec];
-[WiFiUsageSoftApSession addSoftApCoexEvent:deniedUnii1ChannelMap:deniedUnii2aChannelMap:deniedUnii2cChannelMap:deniedUnii3ChannelMap:];
-[WiFiUsageSoftApSession setBandTransitionCount:];
-[WiFiUsageSoftApSession setIdleTimeAfterLastClientDisconnectedSec:];
-[WiFiUsageSoftApSession connectedClients];
-[WiFiUsageSoftApSession fiveGHzDeniedUnii3ChannelCount];
-[WiFiUsageSoftApSession setMaxConnectedClientCount:];
-[WiFiUsageSoftApSession lastHiddenState];
-[WiFiUsageSoftApSession lastAwdlActiveTime];
-[WiFiUsageSoftApSession addSoftApClientEvent:identifier:isAppleClient:isInstantHotspot:isAutoHotspot:isHidden:];
-[WiFiUsageSoftApSession bandTransitionCount];
-[WiFiUsageSoftApSession awdlActiveDuration];
-[WiFiUsageSoftApSession setInfraStateChangedCount:];
-[WiFiUsageSoftApSession linkQualityDidChange:];
-[WiFiUsageSoftApSession setTwoFourGHzDeniedChannelCount:];
-[WiFiUsageSoftApSession setFiveGHzDeniedUnii1ChannelCount:];
-[WiFiUsageSoftApSession setOtherClientConnectCount:];
-[WiFiUsageSoftApSession setLastChannel:];
-[WiFiUsageSoftApSession appleClientConnectCount];
-[WiFiUsageSoftApSession metricName];
-[WiFiUsageSoftApSession twoFourGHzClientConnectCount];
-[WiFiUsageSoftApSession status];
-[WiFiUsageSoftApSession setBroadcastClientConnectCount:];
-[WiFiUsageSoftApSession awdlStateChangedCount];
-[WiFiUsageSoftApSession setHiddenClientConnectCount:];
-[WiFiUsageSoftApSession setFiveGHzDeniedUnii2aChannelCount:];
-[WiFiUsageSoftApSession setConnectedClients:];
-[WiFiUsageSoftApSession tearDownReason];
-[WiFiUsageSoftApSession setInfraActiveDuration:];
-[WiFiUsageSoftApSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageSoftApSession setLowPowerModeDurationSec:];
-[WiFiUsageSoftApSession fiveGHzClientConnectCount];
-[WiFiUsageSoftApSession requester];
-[WiFiUsageSoftApSession eventDictionary:];
-[WiFiUsageSoftApSession summarizeSession];
-[WiFiUsageSoftApSession instantHotspotClientConnectCount];
-[WiFiUsageSoftApSession setKnownNetworkScanCount:];
-[WiFiUsageSoftApSession hiddenTransitionCount];
-[WiFiUsageSoftApSession setLastHiddenState:];
-[WiFiUsageSoftApSession clientDisconnectCount];
-[WiFiUsageSoftApSession setFiveGHzDeniedUnii2cChannelCount:];
-[WiFiUsageSoftApSession setTwoFourGHzChannelCount:];
-[WiFiUsageSoftApSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageSoftApSession twoFourGHzDeniedChannelCount];
-[WiFiUsageSoftApSession fiveGHzDeniedUnii1ChannelCount];
-[WiFiUsageSoftApSession fiveGHzDeniedUnii2cChannelCount];
-[WiFiUsageSoftApSession appliedCountryCode];
-[WiFiUsageSoftApSession autoHotspotClientConnectCount];
-[WiFiUsageSoftApSession setClientDisconnectCount:];
-[WiFiUsageSoftApSession setFiveGHzClientConnectCount:];
-[WiFiUsageSoftApSession knownNetworkScanCount];
-[WiFiUsageSoftApSession broadcastClientConnectCount];
-[WiFiUsageSoftApSession setFiveGHzChannelCount:];
-[WiFiUsageSoftApSession maxConnectedClientCount];
-[WiFiUsageSoftApSession infraStateChangedCount];
-[WiFiUsageSoftApSession setLastInfraActiveTime:];
-[WiFiUsageSoftApSession setIdleTimeBeforeTeardownSec:];
-[WiFiUsageSoftApSession idleTimeBeforeTeardownSec];
-[WiFiUsageSoftApSession dynamicPowerModeDurationSec];
-[WiFiUsageSoftApSession idleTimeAfterLastClientDisconnectedSec];
-[WiFiUsageSoftApSession infraActiveDuration];
-[WiFiUsageSoftApSession setInstantHotspotClientConnectCount:];
-[WiFiUsageSoftApSession awdlStateDidChange:inMode:];
-[WiFiUsageSoftApSession compatibilityEnabled];
-[WiFiUsageSoftApSession lastInfraActiveTime];
-[WiFiUsageSoftApSession setDynamicPowerModeDurationSec:];
-[WiFiUsageSoftApSession setAppleClientConnectCount:];
-[WiFiUsageSoftApSession setCompatibilityEnabled:];
-[WiFiUsageSoftApSession setTwoFourGHzClientConnectCount:];
-[WiFiUsageSoftApSession setRequestToUpLatency:];
-[WiFiUsageSoftApSession setStatus:];
-[WiFiUsageSoftApSession copyWithZone:];
-[WiFiUsageSoftApSession setAwdlStateChangedCount:];
-[WiFiUsageSoftApSession otherClientConnectCount];
-[WiFiUsageSoftApSession setHiddenTransitionCount:];
-[WiFiUsageSoftApSession fiveGHzDeniedUnii2aChannelCount];
-[WiFiUsageSoftApSession softApStateDidChange:];
-[WiFiUsageSoftApSession setRequester:];
-[WiFiUsageSoftApSession setTearDownReason:];
-[WiFiUsageSoftApSession requestToUpLatency];
-[WiFiUsageSoftApSession hiddenClientConnectCount];
-[WiFiUsageSoftApSession setAwdlActiveDuration:];
-[WiFiUsageSoftApSession setFiveGHzDeniedUnii3ChannelCount:];
-[WiFiUsageSoftApSession fiveGHzChannelCount];
-[WiFiUsageSoftApSession setLastAwdlActiveTime:];
-[WiFiUsageSoftApSession setAppliedCountryCode:];
-[WiFiUsageSoftApSession lastChannel];
```
