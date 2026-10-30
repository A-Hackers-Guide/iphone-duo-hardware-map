# `WAEventLinkTest`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 7 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"badDNSServers"B"badGateway"B"dnsResultsValid"B"dnsSuccess"B"foundCriticalFailure"B"isTriggeredByFault"B"gatewayMaxRTT"q"gatewayMinRTT"q"gatewayPacketLoss"q"gatewayResultsValid"B"localDNSMaxRTT"q"localDNSMinRTT"q"localDNSPacketLoss"q"localResultsValid"B"publicDNSMaxRTT"q"publicDNSMinRTT"q"publicDNSPacketLoss"q"publicResultsValid"B"seenSpecificAcFailure"B"siriTCPResultsValid"B"siriTCPSuccess"B"siriTLSResultsValid"B"siriTLSSuccess"B"siriTrafficClass"i} _data;
@"NSString" _initiatingReason;
@"NSString" _statusForDNS;
@"NSString" _statusForInternet;
@"NSString" _statusForLocal;
@"NSString" _statusForSiriTCP;
@"NSString" _statusForSiriTLS;
```

## Properties

```
@property (T@"NSString",&,N,V_initiatingReason) initiatingReason;
@property (T@"NSString",&,N,V_statusForDNS) statusForDNS;
@property (T@"NSString",&,N,V_statusForInternet) statusForInternet;
@property (T@"NSString",&,N,V_statusForLocal) statusForLocal;
@property (T@"NSString",&,N,V_statusForSiriTCP) statusForSiriTCP;
@property (T@"NSString",&,N,V_statusForSiriTLS) statusForSiriTLS;
```

## Instance methods

```
-[WAEventLinkTest processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventLinkTest updateRecord:];
-[WAEventLinkTest initiatingReason];
-[WAEventLinkTest statusForInternet];
-[WAEventLinkTest data];
-[WAEventLinkTest initWithBssid:initiatingReason:statusForDNS:statusForInternet:statusForLocal:statusForSiriTCP:statusForSiriTLS:at:data:withLqmHistory:withError:];
-[WAEventLinkTest statusForLocal];
-[WAEventLinkTest setStatusForSiriTLS:];
-[WAEventLinkTest setInitiatingReason:];
-[WAEventLinkTest setStatusForInternet:];
-[WAEventLinkTest statusForSiriTLS];
-[WAEventLinkTest description];
-[WAEventLinkTest statusForDNS];
-[WAEventLinkTest setStatusForDNS:];
-[WAEventLinkTest setStatusForSiriTCP:];
-[WAEventLinkTest statusForSiriTCP];
-[WAEventLinkTest setStatusForLocal:];
```
