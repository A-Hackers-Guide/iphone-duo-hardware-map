# `LinkTestMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EventMO`
- 0 instance variables, 31 properties, 0 instance methods, 2 class methods

## Properties

```
@property (TB,D,N) badDNSServers;
@property (TB,D,N) badGateway;
@property (TB,D,N) dnsResultsValid;
@property (TB,D,N) dnsSuccess;
@property (TB,D,N) foundCriticalFailure;
@property (T@"NSDecimalNumber",C,D,N) gatewayMaxRTT;
@property (T@"NSDecimalNumber",C,D,N) gatewayMinRTT;
@property (T@"NSDecimalNumber",C,D,N) gatewayPacketLoss;
@property (TB,D,N) gatewayResultsValid;
@property (T@"NSString",C,D,N) initiatingReason;
@property (TB,D,N) isTriggeredByFault;
@property (T@"NSDecimalNumber",C,D,N) localDNSMaxRTT;
@property (T@"NSDecimalNumber",C,D,N) localDNSMinRTT;
@property (T@"NSDecimalNumber",C,D,N) localDNSPacketLoss;
@property (TB,D,N) localResultsValid;
@property (T@"NSDecimalNumber",C,D,N) publicDNSMaxRTT;
@property (T@"NSDecimalNumber",C,D,N) publicDNSMinRTT;
@property (T@"NSDecimalNumber",C,D,N) publicDNSPacketLoss;
@property (TB,D,N) publicResultsValid;
@property (TB,D,N) seenSpecificAcFailure;
@property (TB,D,N) siriTCPResultsValid;
@property (TB,D,N) siriTCPSuccess;
@property (TB,D,N) siriTLSResultsValid;
@property (TB,D,N) siriTLSSuccess;
@property (Ti,D,N) siriTrafficClass;
@property (T@"NSString",C,D,N) statusForDNS;
@property (T@"NSString",C,D,N) statusForInternet;
@property (T@"NSString",C,D,N) statusForLocal;
@property (T@"NSString",C,D,N) statusForSiriTCP;
@property (T@"NSString",C,D,N) statusForSiriTLS;
@property (T@"FaultMO",&,D,N) fault;
```

## Class methods

```
+[LinkTestMO fetchRequest];
+[LinkTestMO unusedSuperEntityProperties];
```
