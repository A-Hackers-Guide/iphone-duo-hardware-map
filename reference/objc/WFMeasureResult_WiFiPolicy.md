# `WFMeasureResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 47 instance variables, 47 properties, 118 instance methods, 1 class methods

## Instance variables

```
B _dnsSuccess;
B _backhaulResultsValid;
B _gatewayResultsValid;
B _localResultsValid;
B _publicResultsValid;
B _dnsResultsValid;
B _seenSpecificAcFailure;
B _siriTCPResultsValid;
B _siriTLSResultsValid;
B _siriTCPSuccess;
B _siriTLSSuccess;
B _siriACEResultsValid;
B _siriACESuccess;
i _siriTrafficClass;
Q _type;
Q _options;
d _backhaulThroughput;
d _backhaulULThroughput;
@"NSError" _downloadError;
@"NSError" _uploadError;
q _gatewayMinRTT;
q _gatewayMaxRTT;
q _gatewayPacketLoss;
q _localDNSMinRTT;
q _localDNSMaxRTT;
q _localDNSPacketLoss;
q _publicDNSMinRTT;
q _publicDNSMaxRTT;
q _publicDNSPacketLoss;
q _trafficClassBEAttemptedSmall;
q _trafficClassBKAttemptedSmall;
q _trafficClassVOAttemptedSmall;
q _trafficClassVIAttemptedSmall;
q _trafficClassBESucceededSmall;
q _trafficClassBKSucceededSmall;
q _trafficClassVOSucceededSmall;
q _trafficClassVISucceededSmall;
q _trafficClassBEAttemptedLarge;
q _trafficClassBKAttemptedLarge;
q _trafficClassVOAttemptedLarge;
q _trafficClassVIAttemptedLarge;
q _trafficClassBESucceededLarge;
q _trafficClassBKSucceededLarge;
q _trafficClassVOSucceededLarge;
q _trafficClassVISucceededLarge;
@"NSString" _gatewayAddress;
@"NSMutableSet" _dnsServers;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (TQ,N,V_options) options;
@property (Td,N,V_backhaulThroughput) backhaulThroughput;
@property (Td,N,V_backhaulULThroughput) backhaulULThroughput;
@property (T@"NSError",C,N,V_downloadError) downloadError;
@property (T@"NSError",C,N,V_uploadError) uploadError;
@property (Tq,N,V_gatewayMinRTT) gatewayMinRTT;
@property (Tq,N,V_gatewayMaxRTT) gatewayMaxRTT;
@property (Tq,N,V_gatewayPacketLoss) gatewayPacketLoss;
@property (Tq,N,V_localDNSMinRTT) localDNSMinRTT;
@property (Tq,N,V_localDNSMaxRTT) localDNSMaxRTT;
@property (Tq,N,V_localDNSPacketLoss) localDNSPacketLoss;
@property (Tq,N,V_publicDNSMinRTT) publicDNSMinRTT;
@property (Tq,N,V_publicDNSMaxRTT) publicDNSMaxRTT;
@property (Tq,N,V_publicDNSPacketLoss) publicDNSPacketLoss;
@property (TB,N,V_dnsSuccess) dnsSuccess;
@property (TB,N,V_backhaulResultsValid) backhaulResultsValid;
@property (TB,N,V_gatewayResultsValid) gatewayResultsValid;
@property (TB,N,V_localResultsValid) localResultsValid;
@property (TB,N,V_publicResultsValid) publicResultsValid;
@property (TB,N,V_dnsResultsValid) dnsResultsValid;
@property (TB,N,V_siriTCPResultsValid) siriTCPResultsValid;
@property (TB,N,V_siriTLSResultsValid) siriTLSResultsValid;
@property (TB,N,V_siriACEResultsValid) siriACEResultsValid;
@property (TB,N,V_seenSpecificAcFailure) seenSpecificAcFailure;
@property (TB,N,V_siriTCPSuccess) siriTCPSuccess;
@property (TB,N,V_siriTLSSuccess) siriTLSSuccess;
@property (TB,N,V_siriACESuccess) siriACESuccess;
@property (Ti,N,V_siriTrafficClass) siriTrafficClass;
@property (Tq,N,V_trafficClassBEAttemptedSmall) trafficClassBEAttemptedSmall;
@property (Tq,N,V_trafficClassBKAttemptedSmall) trafficClassBKAttemptedSmall;
@property (Tq,N,V_trafficClassVOAttemptedSmall) trafficClassVOAttemptedSmall;
@property (Tq,N,V_trafficClassVIAttemptedSmall) trafficClassVIAttemptedSmall;
@property (Tq,N,V_trafficClassBESucceededSmall) trafficClassBESucceededSmall;
@property (Tq,N,V_trafficClassBKSucceededSmall) trafficClassBKSucceededSmall;
@property (Tq,N,V_trafficClassVOSucceededSmall) trafficClassVOSucceededSmall;
@property (Tq,N,V_trafficClassVISucceededSmall) trafficClassVISucceededSmall;
@property (Tq,N,V_trafficClassBEAttemptedLarge) trafficClassBEAttemptedLarge;
@property (Tq,N,V_trafficClassBKAttemptedLarge) trafficClassBKAttemptedLarge;
@property (Tq,N,V_trafficClassVOAttemptedLarge) trafficClassVOAttemptedLarge;
@property (Tq,N,V_trafficClassVIAttemptedLarge) trafficClassVIAttemptedLarge;
@property (Tq,N,V_trafficClassBESucceededLarge) trafficClassBESucceededLarge;
@property (Tq,N,V_trafficClassBKSucceededLarge) trafficClassBKSucceededLarge;
@property (Tq,N,V_trafficClassVOSucceededLarge) trafficClassVOSucceededLarge;
@property (Tq,N,V_trafficClassVISucceededLarge) trafficClassVISucceededLarge;
@property (T@"NSString",&,N,V_gatewayAddress) gatewayAddress;
@property (T@"NSMutableSet",&,N,V_dnsServers) dnsServers;
```

## Class methods

```
+[WFMeasureResult initialize];
```

## Instance methods

```
-[WFMeasureResult siriTCPResultsValid];
-[WFMeasureResult publicDNSMinRTT];
-[WFMeasureResult statusForAcFailure];
-[WFMeasureResult setTrafficClassBKSucceededLarge:];
-[WFMeasureResult setSiriTCPResultsValid:];
-[WFMeasureResult setPublicDNSMinRTT:];
-[WFMeasureResult setTrafficClassVISucceededLarge:];
-[WFMeasureResult numPingPacketsFailed];
-[WFMeasureResult gatewayMaxRTT];
-[WFMeasureResult siriTLSResultsValid];
-[WFMeasureResult siriTrafficClass];
-[WFMeasureResult setTrafficClassVIAttemptedLarge:];
-[WFMeasureResult publicDNSMaxRTT];
-[WFMeasureResult setOptions:];
-[WFMeasureResult setDnsServers:];
-[WFMeasureResult setLocalDNSMaxRTT:];
-[WFMeasureResult seenSpecificAcFailure];
-[WFMeasureResult setTrafficClassBESucceededLarge:];
-[WFMeasureResult trafficClassVISucceededLarge];
-[WFMeasureResult trafficClassVOAttemptedSmall];
-[WFMeasureResult setTrafficClassVISucceededSmall:];
-[WFMeasureResult dnsSuccess];
-[WFMeasureResult setTrafficClassVOSucceededSmall:];
-[WFMeasureResult setDownloadError:];
-[WFMeasureResult setTrafficClassBKAttemptedSmall:];
-[WFMeasureResult trafficClassBEAttemptedSmall];
-[WFMeasureResult numAcSuccess];
-[WFMeasureResult localDNSPacketLoss];
-[WFMeasureResult setSiriACESuccess:];
-[WFMeasureResult initWithType:];
-[WFMeasureResult dnsResultsValid];
-[WFMeasureResult setLocalDNSPacketLoss:];
-[WFMeasureResult trafficClassBESucceededLarge];
-[WFMeasureResult gatewayMinRTT];
-[WFMeasureResult statusForInternet];
-[WFMeasureResult setTrafficClassVOAttemptedSmall:];
-[WFMeasureResult numAcAttempted];
-[WFMeasureResult setSeenSpecificAcFailure:];
-[WFMeasureResult setPublicDNSMaxRTT:];
-[WFMeasureResult setTrafficClassBKAttemptedLarge:];
-[WFMeasureResult setGatewayMinRTT:];
-[WFMeasureResult binnedProperty:];
-[WFMeasureResult numSmallPingPacketsAttempted];
-[WFMeasureResult setBackhaulResultsValid:];
-[WFMeasureResult uploadError];
-[WFMeasureResult siriTLSSuccess];
-[WFMeasureResult trafficClassBEAttemptedLarge];
-[WFMeasureResult trafficClassBKAttemptedLarge];
-[WFMeasureResult typeAsString];
-[WFMeasureResult numSmallPingPacketsFailed];
-[WFMeasureResult setLocalResultsValid:];
-[WFMeasureResult trafficClassVISucceededSmall];
-[WFMeasureResult setBackhaulThroughput:];
-[WFMeasureResult setTrafficClassBKSucceededSmall:];
-[WFMeasureResult gatewayPacketLoss];
-[WFMeasureResult siriACEResultsValid];
-[WFMeasureResult setTrafficClassBEAttemptedLarge:];
-[WFMeasureResult trafficClassVIAttemptedLarge];
-[WFMeasureResult setSiriTrafficClass:];
-[WFMeasureResult localDNSMaxRTT];
-[WFMeasureResult trafficClassVIAttemptedSmall];
-[WFMeasureResult gatewayAddress];
-[WFMeasureResult trafficClassVOAttemptedLarge];
-[WFMeasureResult publicResultsValid];
-[WFMeasureResult backhaulThroughput];
-[WFMeasureResult gatewayResultsValid];
-[WFMeasureResult setSiriTLSSuccess:];
-[WFMeasureResult numPingPacketsAttempted];
-[WFMeasureResult setType:];
-[WFMeasureResult trafficClassBKAttemptedSmall];
-[WFMeasureResult type];
-[WFMeasureResult statusForLocal];
-[WFMeasureResult setDnsResultsValid:];
-[WFMeasureResult setTrafficClassVIAttemptedSmall:];
-[WFMeasureResult setSiriTCPSuccess:];
-[WFMeasureResult numAcFailed];
-[WFMeasureResult setPublicDNSPacketLoss:];
-[WFMeasureResult setTrafficClassBEAttemptedSmall:];
-[WFMeasureResult localDNSMinRTT];
-[WFMeasureResult setDnsSuccess:];
-[WFMeasureResult numLargePingPacketsFailed];
-[WFMeasureResult setGatewayMaxRTT:];
-[WFMeasureResult backhaulULThroughput];
-[WFMeasureResult statusForSiriTLS];
-[WFMeasureResult downloadError];
-[WFMeasureResult trafficClassVOSucceededSmall];
-[WFMeasureResult numLargePingPacketsAttempted];
-[WFMeasureResult setLocalDNSMinRTT:];
-[WFMeasureResult description];
-[WFMeasureResult setTrafficClassBESucceededSmall:];
-[WFMeasureResult publicDNSPacketLoss];
-[WFMeasureResult trafficClassBESucceededSmall];
-[WFMeasureResult statusForDNS];
-[WFMeasureResult numSmallPingPacketsSuccess];
-[WFMeasureResult siriTCPSuccess];
-[WFMeasureResult setGatewayAddress:];
-[WFMeasureResult trafficClassBKSucceededSmall];
-[WFMeasureResult setPublicResultsValid:];
-[WFMeasureResult numLargePingPacketsSuccess];
-[WFMeasureResult options];
-[WFMeasureResult setGatewayPacketLoss:];
-[WFMeasureResult dnsServers];
-[WFMeasureResult setGatewayResultsValid:];
-[WFMeasureResult copyWithZone:];
-[WFMeasureResult setBackhaulULThroughput:];
-[WFMeasureResult backhaulResultsValid];
-[WFMeasureResult setTrafficClassVOAttemptedLarge:];
-[WFMeasureResult trafficClassBKSucceededLarge];
-[WFMeasureResult trafficClassVOSucceededLarge];
-[WFMeasureResult setSiriACEResultsValid:];
-[WFMeasureResult statusForSiriTCP];
-[WFMeasureResult allPrimitiveProperties];
-[WFMeasureResult setTrafficClassVOSucceededLarge:];
-[WFMeasureResult numPingPacketsSuccess];
-[WFMeasureResult setUploadError:];
-[WFMeasureResult localResultsValid];
-[WFMeasureResult siriACESuccess];
-[WFMeasureResult setSiriTLSResultsValid:];
```
