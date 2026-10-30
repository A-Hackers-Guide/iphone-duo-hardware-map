# `WiFiUsageSoftApStateInfo`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _active;
B _isHidden;
B _isInfraConnected;
B _isAwdlUp;
B _compatibilityMode;
@"NSString" _requester;
@"NSString" _status;
@"NSString" _changeReason;
Q _channelNumber;
Q _countryCode;
d _lowPowerModeDurationSec;
d _dynamicPowerModeDurationSec;
d _requestToUpLatency;
d _idleTimeBeforeTeardownSec;
d _idleTimeAfterLastClientDisconnectedSec;
```

## Properties

```
@property (TB,N,V_active) active;
@property (T@"NSString",&,N,V_requester) requester;
@property (T@"NSString",&,N,V_status) status;
@property (T@"NSString",&,N,V_changeReason) changeReason;
@property (TQ,N,V_channelNumber) channelNumber;
@property (TQ,N,V_countryCode) countryCode;
@property (TB,N,V_isHidden) isHidden;
@property (TB,N,V_isInfraConnected) isInfraConnected;
@property (TB,N,V_isAwdlUp) isAwdlUp;
@property (Td,N,V_lowPowerModeDurationSec) lowPowerModeDurationSec;
@property (Td,N,V_dynamicPowerModeDurationSec) dynamicPowerModeDurationSec;
@property (TB,N,V_compatibilityMode) compatibilityMode;
@property (Td,N,V_requestToUpLatency) requestToUpLatency;
@property (Td,N,V_idleTimeBeforeTeardownSec) idleTimeBeforeTeardownSec;
@property (Td,N,V_idleTimeAfterLastClientDisconnectedSec) idleTimeAfterLastClientDisconnectedSec;
```

## Instance methods

```
-[WiFiUsageSoftApStateInfo setIsHidden:];
-[WiFiUsageSoftApStateInfo active];
-[WiFiUsageSoftApStateInfo lowPowerModeDurationSec];
-[WiFiUsageSoftApStateInfo setIdleTimeAfterLastClientDisconnectedSec:];
-[WiFiUsageSoftApStateInfo setCompatibilityMode:];
-[WiFiUsageSoftApStateInfo init];
-[WiFiUsageSoftApStateInfo changeReason];
-[WiFiUsageSoftApStateInfo status];
-[WiFiUsageSoftApStateInfo compatibilityMode];
-[WiFiUsageSoftApStateInfo setActive:];
-[WiFiUsageSoftApStateInfo setChannelNumber:];
-[WiFiUsageSoftApStateInfo setLowPowerModeDurationSec:];
-[WiFiUsageSoftApStateInfo requester];
-[WiFiUsageSoftApStateInfo isHidden];
-[WiFiUsageSoftApStateInfo countryCode];
-[WiFiUsageSoftApStateInfo setIdleTimeBeforeTeardownSec:];
-[WiFiUsageSoftApStateInfo idleTimeBeforeTeardownSec];
-[WiFiUsageSoftApStateInfo dynamicPowerModeDurationSec];
-[WiFiUsageSoftApStateInfo idleTimeAfterLastClientDisconnectedSec];
-[WiFiUsageSoftApStateInfo description];
-[WiFiUsageSoftApStateInfo setDynamicPowerModeDurationSec:];
-[WiFiUsageSoftApStateInfo setRequestToUpLatency:];
-[WiFiUsageSoftApStateInfo setStatus:];
-[WiFiUsageSoftApStateInfo setRequester:];
-[WiFiUsageSoftApStateInfo requestToUpLatency];
-[WiFiUsageSoftApStateInfo setCountryCode:];
-[WiFiUsageSoftApStateInfo channelNumber];
-[WiFiUsageSoftApStateInfo setChangeReason:];
-[WiFiUsageSoftApStateInfo isAwdlUp];
-[WiFiUsageSoftApStateInfo isInfraConnected];
-[WiFiUsageSoftApStateInfo setIsAwdlUp:];
-[WiFiUsageSoftApStateInfo setIsInfraConnected:];
```
