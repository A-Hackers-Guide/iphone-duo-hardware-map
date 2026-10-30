# `ACCTransportIOAccessoryAuthCP`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ACCTransportIOAccessoryBase`
- 35 instance variables, 35 properties, 95 instance methods, 0 class methods

## Instance variables

```
B _authTimedOut;
B _representsInductiveTransport;
C _authTryCurrent;
C _authTryMaximum;
C _authVersionMajor;
B _bIsShuttingDown;
B _certIsCached;
C _softwareErrorRetry;
B _notificationsAvailable;
S _deviceID;
i _authStatus;
i _representsInternalModule;
i _accConnectionType;
i _authType;
I _ioServiceUpstream;
i _certType;
I _authFlags;
i _fdrValidationStatus;
i _authErrorDescription;
I _forcedReAuthCount;
I _battery_iter;
@"<ACCTransportIOAccessoryAuthCPProtocol>" _delegate;
@"NSData" _pAuthCertificate;
@"NSString" _connectionUUID;
@"NSString" _endpointUUID;
@"NSObject<OS_dispatch_queue>" _authWorkQueue;
@"NSObject<OS_dispatch_source>" _authTimerSource;
r^v _pAuthCertCache;
@"NSDictionary" _certInfo;
Q _authTimerStartTimestamp;
^{IONotificationPort=} _batteryNotifyPortRef;
^{IONotificationPort=} _transportNotifyPortRef;
@"NSObject<OS_dispatch_semaphore>" _pairedSema;
@"NSData" _deferredAuthChallenge;
{_AuthCertCapsInt_t="authCertCaps0"Q"authCertCaps1"Q"authCertCaps2"Q"authCertCaps3"Q} _authCertCaps;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_authWorkQueue) authWorkQueue;
@property (T@"NSObject<OS_dispatch_source>",&,V_authTimerSource) authTimerSource;
@property (TC,V_authTryCurrent) authTryCurrent;
@property (TC,V_authTryMaximum) authTryMaximum;
@property (TC,V_authVersionMajor) authVersionMajor;
@property (TS,V_deviceID) deviceID;
@property (T{_AuthCertCapsInt_t=QQQQ},V_authCertCaps) authCertCaps;
@property (Tr^v,V_pAuthCertCache) pAuthCertCache;
@property (TI,V_ioServiceUpstream) ioServiceUpstream;
@property (Ti,N,V_accConnectionType) accConnectionType;
@property (TB,V_bIsShuttingDown) bIsShuttingDown;
@property (Ti,V_certType) certType;
@property (T@"NSDictionary",&,V_certInfo) certInfo;
@property (TB,N,V_representsInductiveTransport) representsInductiveTransport;
@property (Ti,N,V_representsInternalModule) representsInternalModule;
@property (TI,V_authFlags) authFlags;
@property (TQ,V_authTimerStartTimestamp) authTimerStartTimestamp;
@property (Ti,V_fdrValidationStatus) fdrValidationStatus;
@property (Ti,V_authErrorDescription) authErrorDescription;
@property (TI,V_forcedReAuthCount) forcedReAuthCount;
@property (TB,V_certIsCached) certIsCached;
@property (TC,V_softwareErrorRetry) softwareErrorRetry;
@property (T^{IONotificationPort=},V_batteryNotifyPortRef) batteryNotifyPortRef;
@property (TI,V_battery_iter) battery_iter;
@property (T^{IONotificationPort=},V_transportNotifyPortRef) transportNotifyPortRef;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_pairedSema) pairedSema;
@property (TB,V_notificationsAvailable) notificationsAvailable;
@property (T@"NSData",&,V_deferredAuthChallenge) deferredAuthChallenge;
@property (T@"<ACCTransportIOAccessoryAuthCPProtocol>",W,N,V_delegate) delegate;
@property (Ti,R,N,V_authStatus) authStatus;
@property (TB,R,N,V_authTimedOut) authTimedOut;
@property (T@"NSData",R,N,V_pAuthCertificate) pAuthCertificate;
@property (T@"NSString",&,N,V_connectionUUID) connectionUUID;
@property (T@"NSString",&,N,V_endpointUUID) endpointUUID;
@property (Ti,R,N,V_authType) authType;
```

## Instance methods

```
-[ACCTransportIOAccessoryAuthCP authType];
-[ACCTransportIOAccessoryAuthCP setCertIsCached:];
-[ACCTransportIOAccessoryAuthCP authStatus];
-[ACCTransportIOAccessoryAuthCP authTryMaximum];
-[ACCTransportIOAccessoryAuthCP setAuthTimerStartTimestamp:];
-[ACCTransportIOAccessoryAuthCP setDeferredAuthChallenge:];
-[ACCTransportIOAccessoryAuthCP setBatteryNotifyPortRef:];
-[ACCTransportIOAccessoryAuthCP _copyCertificateAttribute:forAttributeKey:withAttributeValue:];
-[ACCTransportIOAccessoryAuthCP setPairedSema:];
-[ACCTransportIOAccessoryAuthCP deferredAuthChallenge];
-[ACCTransportIOAccessoryAuthCP batteryNotifyPortRef];
-[ACCTransportIOAccessoryAuthCP _validateModuleCertificate];
-[ACCTransportIOAccessoryAuthCP authTimerStartTimestamp];
-[ACCTransportIOAccessoryAuthCP battery_iter];
-[ACCTransportIOAccessoryAuthCP doPostAuthentication];
-[ACCTransportIOAccessoryAuthCP _publishAuth:fdrStatus:trusted:publishToUI:ioconnect:];
-[ACCTransportIOAccessoryAuthCP deviceID];
-[ACCTransportIOAccessoryAuthCP setAuthFlags:];
-[ACCTransportIOAccessoryAuthCP authCertCaps];
-[ACCTransportIOAccessoryAuthCP authFlags];
-[ACCTransportIOAccessoryAuthCP setRepresentsInternalModule:];
-[ACCTransportIOAccessoryAuthCP setAuthErrorDescription:];
-[ACCTransportIOAccessoryAuthCP authTimerSource];
-[ACCTransportIOAccessoryAuthCP dealloc];
-[ACCTransportIOAccessoryAuthCP _findFDRCertData:];
-[ACCTransportIOAccessoryAuthCP _validateCertCapsForCertificate:authError:];
-[ACCTransportIOAccessoryAuthCP _validateDownstreamCertSerialNumber];
-[ACCTransportIOAccessoryAuthCP _finishAuthentication:authCert:];
-[ACCTransportIOAccessoryAuthCP _publishAuthStats:fdrStatus:];
-[ACCTransportIOAccessoryAuthCP setAuthTryMaximum:];
-[ACCTransportIOAccessoryAuthCP startShutdownProcess];
-[ACCTransportIOAccessoryAuthCP _authInternalModuleWithCert:withError:];
-[ACCTransportIOAccessoryAuthCP setCertInfo:];
-[ACCTransportIOAccessoryAuthCP initWithDelegate:andIOService:connectionType:];
-[ACCTransportIOAccessoryAuthCP authTryCurrent];
-[ACCTransportIOAccessoryAuthCP _logToAnalytics];
-[ACCTransportIOAccessoryAuthCP ioServiceUpstream];
-[ACCTransportIOAccessoryAuthCP setAuthVersionMajor:];
-[ACCTransportIOAccessoryAuthCP _handleAuthSignature:certData:nonceData:];
-[ACCTransportIOAccessoryAuthCP setRepresentsInductiveTransport:];
-[ACCTransportIOAccessoryAuthCP _handleAuthDeviceInfo:versionMajor:versionMinor:];
-[ACCTransportIOAccessoryAuthCP _resetAfterAuthCompletion];
-[ACCTransportIOAccessoryAuthCP fdrValidationStatus];
-[ACCTransportIOAccessoryAuthCP authVersionMajor];
-[ACCTransportIOAccessoryAuthCP representsInductiveTransport];
-[ACCTransportIOAccessoryAuthCP _representsHardwareComponent];
-[ACCTransportIOAccessoryAuthCP certIsCached];
-[ACCTransportIOAccessoryAuthCP certType];
-[ACCTransportIOAccessoryAuthCP setDeviceID:];
-[ACCTransportIOAccessoryAuthCP requiresAuthenticationProcess];
-[ACCTransportIOAccessoryAuthCP setDelegate:];
-[ACCTransportIOAccessoryAuthCP setAuthWorkQueue:];
-[ACCTransportIOAccessoryAuthCP forcedReAuthCount];
-[ACCTransportIOAccessoryAuthCP pAuthCertificate];
-[ACCTransportIOAccessoryAuthCP setConnectionUUID:];
-[ACCTransportIOAccessoryAuthCP accConnectionType];
-[ACCTransportIOAccessoryAuthCP startAuthenticationProcess];
-[ACCTransportIOAccessoryAuthCP setEndpointUUID:];
-[ACCTransportIOAccessoryAuthCP _copyOrCreateStatsSubDict:forSerialNumber:];
-[ACCTransportIOAccessoryAuthCP representsInternalModule];
-[ACCTransportIOAccessoryAuthCP setAuthTimerSource:];
-[ACCTransportIOAccessoryAuthCP endpointUUID];
-[ACCTransportIOAccessoryAuthCP authTimedOut];
-[ACCTransportIOAccessoryAuthCP _validateAuthCPFlagsForCertificate];
-[ACCTransportIOAccessoryAuthCP authWorkQueue];
-[ACCTransportIOAccessoryAuthCP setBIsShuttingDown:];
-[ACCTransportIOAccessoryAuthCP bIsShuttingDown];
-[ACCTransportIOAccessoryAuthCP certInfo];
-[ACCTransportIOAccessoryAuthCP _incrementAuthStat:dict:];
-[ACCTransportIOAccessoryAuthCP delegate];
-[ACCTransportIOAccessoryAuthCP transportNotifyPortRef];
-[ACCTransportIOAccessoryAuthCP _fdrCertCheck];
-[ACCTransportIOAccessoryAuthCP setNotificationsAvailable:];
-[ACCTransportIOAccessoryAuthCP _handleBusyComponentAuth];
-[ACCTransportIOAccessoryAuthCP setAccConnectionType:];
-[ACCTransportIOAccessoryAuthCP setSoftwareErrorRetry:];
-[ACCTransportIOAccessoryAuthCP setIoServiceUpstream:];
-[ACCTransportIOAccessoryAuthCP pAuthCertCache];
-[ACCTransportIOAccessoryAuthCP pairedSema];
-[ACCTransportIOAccessoryAuthCP authErrorDescription];
-[ACCTransportIOAccessoryAuthCP connectionUUID];
-[ACCTransportIOAccessoryAuthCP softwareErrorRetry];
-[ACCTransportIOAccessoryAuthCP _authWithAuthIC:withCert:withError:];
-[ACCTransportIOAccessoryAuthCP setForcedReAuthCount:];
-[ACCTransportIOAccessoryAuthCP _handleAuthCertificate:serialNumber:authError:];
-[ACCTransportIOAccessoryAuthCP setAuthCertCaps:];
-[ACCTransportIOAccessoryAuthCP setPAuthCertCache:];
-[ACCTransportIOAccessoryAuthCP setBattery_iter:];
-[ACCTransportIOAccessoryAuthCP _handleAuthTimerTimeout];
-[ACCTransportIOAccessoryAuthCP setFdrValidationStatus:];
-[ACCTransportIOAccessoryAuthCP setAuthTryCurrent:];
-[ACCTransportIOAccessoryAuthCP _handleAuthCertSerialNumber:certData:];
-[ACCTransportIOAccessoryAuthCP notificationsAvailable];
-[ACCTransportIOAccessoryAuthCP setCertType:];
-[ACCTransportIOAccessoryAuthCP setTransportNotifyPortRef:];
```
