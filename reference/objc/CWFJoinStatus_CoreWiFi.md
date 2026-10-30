# `CWFJoinStatus`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 20 instance variables, 33 properties, 61 instance methods, 1 class methods

## Instance variables

```
B _autoJoin;
I _EAP8021XSupplicantState;
I _EAP8021XControlMode;
I _EAP8021XControlState;
i _EAP8021XClientStatus;
@"NSUUID" _UUID;
@"NSString" _interfaceName;
@"CWFScanResult" _scanResult;
@"CWFNetworkProfile" _knownNetworkProfile;
@"NSDate" _startedAt;
@"NSDate" _associationEndedAt;
d _durationForJoinPMAssertion;
@"NSDate" _authenticationEndedAt;
@"NSDate" _linkUpAt;
@"NSDate" _IPv4AssignedAt;
@"NSDate" _IPv4PrimaryAt;
Q _durationForAdaptiveInterfaceRankInMilliseconds;
@"NSDate" _IPv6AssignedAt;
@"NSDate" _IPv6PrimaryAt;
@"NSError" _error;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"CWFScanResult",C,N,V_scanResult) scanResult;
@property (T@"CWFNetworkProfile",C,N,V_knownNetworkProfile) knownNetworkProfile;
@property (TI,N,V_EAP8021XSupplicantState) EAP8021XSupplicantState;
@property (TI,N,V_EAP8021XControlMode) EAP8021XControlMode;
@property (TI,N,V_EAP8021XControlState) EAP8021XControlState;
@property (Ti,N,V_EAP8021XClientStatus) EAP8021XClientStatus;
@property (T@"NSDate",C,N,V_startedAt) startedAt;
@property (T@"NSDate",R,N) endedAt;
@property (Td,R) duration;
@property (T@"NSDate",C,N,V_associationEndedAt) associationEndedAt;
@property (Td,R) durationUntilAssociationEnded;
@property (Td,N,V_durationForJoinPMAssertion) durationForJoinPMAssertion;
@property (T@"NSDate",C,N,V_authenticationEndedAt) authenticationEndedAt;
@property (Td,R) durationUntilAuthenticationEnded;
@property (T@"NSDate",C,N,V_linkUpAt) linkUpAt;
@property (Td,R) durationUntilLinkUp;
@property (T@"NSDate",C,N,V_IPv4AssignedAt) IPv4AssignedAt;
@property (Td,R) durationUntilIPv4Assigned;
@property (T@"NSDate",C,N,V_IPv4PrimaryAt) IPv4PrimaryAt;
@property (TQ,N,V_durationForAdaptiveInterfaceRankInMilliseconds) durationForAdaptiveInterfaceRankInMilliseconds;
@property (Td,R) durationUntilIPv4Primary;
@property (T@"NSDate",C,N,V_IPv6AssignedAt) IPv6AssignedAt;
@property (Td,R) durationUntilIPv6Assigned;
@property (T@"NSDate",C,N,V_IPv6PrimaryAt) IPv6PrimaryAt;
@property (Td,R) durationUntilIPv6Primary;
@property (T@"NSError",C,N,V_error) error;
@property (TB,N,GisAutoJoin,V_autoJoin) autoJoin;
```

## Class methods

```
+[CWFJoinStatus supportsSecureCoding];
```

## Instance methods

```
-[CWFJoinStatus setDurationForJoinPMAssertion:];
-[CWFJoinStatus EAP8021XControlState];
-[CWFJoinStatus EAP8021XSupplicantState];
-[CWFJoinStatus EAP8021XControlMode];
-[CWFJoinStatus setError:];
-[CWFJoinStatus EAP8021XClientStatus];
-[CWFJoinStatus JSONCompatibleKeyValueMap];
-[CWFJoinStatus init];
-[CWFJoinStatus setUUID:];
-[CWFJoinStatus UUID];
-[CWFJoinStatus setInterfaceName:];
-[CWFJoinStatus knownNetworkProfile];
-[CWFJoinStatus interfaceName];
-[CWFJoinStatus setKnownNetworkProfile:];
-[CWFJoinStatus error];
-[CWFJoinStatus duration];
-[CWFJoinStatus endedAt];
-[CWFJoinStatus setStartedAt:];
-[CWFJoinStatus encodeWithCoder:];
-[CWFJoinStatus durationForJoinPMAssertion];
-[CWFJoinStatus hash];
-[CWFJoinStatus description];
-[CWFJoinStatus initWithCoder:];
-[CWFJoinStatus setLinkUpAt:];
-[CWFJoinStatus copyWithZone:];
-[CWFJoinStatus startedAt];
-[CWFJoinStatus linkUpAt];
-[CWFJoinStatus isEqual:];
-[CWFJoinStatus setAutoJoin:];
-[CWFJoinStatus IPv4AssignedAt];
-[CWFJoinStatus IPv6AssignedAt];
-[CWFJoinStatus IPv6PrimaryAt];
-[CWFJoinStatus IPv4PrimaryAt];
-[CWFJoinStatus descriptionForEAPOLClientStatus];
-[CWFJoinStatus associationEndedAt];
-[CWFJoinStatus authenticationEndedAt];
-[CWFJoinStatus descriptionForEAP8021XControlState];
-[CWFJoinStatus descriptionForEAPOLControlMode];
-[CWFJoinStatus durationForAdaptiveInterfaceRankInMilliseconds];
-[CWFJoinStatus durationUntilAssociationEnded];
-[CWFJoinStatus durationUntilAuthenticationEnded];
-[CWFJoinStatus durationUntilIPv4Assigned];
-[CWFJoinStatus durationUntilIPv4Primary];
-[CWFJoinStatus durationUntilIPv6Assigned];
-[CWFJoinStatus durationUntilIPv6Primary];
-[CWFJoinStatus durationUntilLinkUp];
-[CWFJoinStatus isAutoJoin];
-[CWFJoinStatus isEqualToJoinStatus:];
-[CWFJoinStatus scanResult];
-[CWFJoinStatus setAssociationEndedAt:];
-[CWFJoinStatus setAuthenticationEndedAt:];
-[CWFJoinStatus setDurationForAdaptiveInterfaceRankInMilliseconds:];
-[CWFJoinStatus setEAP8021XClientStatus:];
-[CWFJoinStatus setEAP8021XControlMode:];
-[CWFJoinStatus setEAP8021XControlState:];
-[CWFJoinStatus setEAP8021XSupplicantState:];
-[CWFJoinStatus setIPv4AssignedAt:];
-[CWFJoinStatus setIPv4PrimaryAt:];
-[CWFJoinStatus setIPv6AssignedAt:];
-[CWFJoinStatus setIPv6PrimaryAt:];
-[CWFJoinStatus setScanResult:];
```
