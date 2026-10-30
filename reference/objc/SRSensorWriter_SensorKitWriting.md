# `SRSensorWriter`

- Image: [`/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`](../userland/System__Library__PrivateFrameworks__SensorKitWriting.framework__SensorKitWriting.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRAuthorizationStoreReaderAuthorizationDelegate`, `SRDaemonNotificationDelegate`, `SRAuthorizationClientDelegate`
- 27 instance variables, 28 properties, 95 instance methods, 4 class methods

## Instance variables

```
@"<SRSensorWriterDelegate>" _delegate;
@"SRDaemonNotification" _daemonNotification;
@"SRDefaults" _defaults;
@"SRDatastore" _datastore;
AB _monitoring;
i _notifyToken;
B _requestNewSegmentInFlight;
B _authorized;
B _connectionDidInterrupt;
B _connectionDidInvalidate;
B _retryGetMonitoring;
@"NSString" _sensorIdentifier;
@"NSDictionary" _nextDatastoreFiles;
@"NSXPCConnection" _connection;
q __writerAuthorizationStatus;
@"NSString" _writerAuthorizationService;
@"<SRTCCStore>" _tccStore;
@"NSObject<OS_dispatch_queue>" _writerAuthorizationUpdateQueue;
@"SRAuthorizationStore" _authStore;
@"NSCache" _eligibilityCache;
d _roundingInterval;
@"NSDictionary" _lastMetadata;
Q _lastMetadataContinuousTime;
@"NSDictionary" _lastConfiguration;
Q _lastConfigurationContinuousTime;
@"SRWritingStats" _writingStats;
@"NSArray" __requestedConfigurations;
```

## Properties

```
@property (T@"NSString",C,V_sensorIdentifier) sensorIdentifier;
@property (T@"SRDatastore",R,&) datastore;
@property (T@"NSDictionary",&,V_nextDatastoreFiles) nextDatastoreFiles;
@property (TB,V_requestNewSegmentInFlight) requestNewSegmentInFlight;
@property (TB,V_authorized) authorized;
@property (TB,V_connectionDidInterrupt) connectionDidInterrupt;
@property (TB,V_connectionDidInvalidate) connectionDidInvalidate;
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TB,V_retryGetMonitoring) retryGetMonitoring;
@property (Tq,V__writerAuthorizationStatus) _writerAuthorizationStatus;
@property (T@"NSString",R,&,N,V_writerAuthorizationService) writerAuthorizationService;
@property (T@"<SRTCCStore>",&,V_tccStore) tccStore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_writerAuthorizationUpdateQueue) writerAuthorizationUpdateQueue;
@property (T@"SRAuthorizationStore",&,N,V_authStore) authStore;
@property (T@"NSCache",&,N,V_eligibilityCache) eligibilityCache;
@property (Td,N,V_roundingInterval) roundingInterval;
@property (T@"NSDictionary",&,V_lastMetadata) lastMetadata;
@property (TQ,V_lastMetadataContinuousTime) lastMetadataContinuousTime;
@property (T@"NSDictionary",&,V_lastConfiguration) lastConfiguration;
@property (TQ,V_lastConfigurationContinuousTime) lastConfigurationContinuousTime;
@property (T@"SRWritingStats",&,N,V_writingStats) writingStats;
@property (T@"NSArray",C,N,V__requestedConfigurations) _requestedConfigurations;
@property (TB,GisMonitoring) monitoring;
@property (T@"<SRSensorWriterDelegate>",W) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRSensorWriter remoteInterface];
+[SRSensorWriter initialize];
+[SRSensorWriter clientInterface];
+[SRSensorWriter connectionToDaemon];
```

## Instance methods

```
-[SRSensorWriter setupConnection];
-[SRSensorWriter defaults];
-[SRSensorWriter isMonitoring];
-[SRSensorWriter init];
-[SRSensorWriter dealloc];
-[SRSensorWriter lastConfiguration];
-[SRSensorWriter setLastConfiguration:];
-[SRSensorWriter setDelegate:];
-[SRSensorWriter authorized];
-[SRSensorWriter connection];
-[SRSensorWriter setMetadata:];
-[SRSensorWriter delegate];
-[SRSensorWriter setConnection:];
-[SRSensorWriter datastore];
-[SRSensorWriter initWithIdentifier:];
-[SRSensorWriter setMonitoring:];
-[SRSensorWriter connectionDidInterrupt];
-[SRSensorWriter connectionDidInvalidate];
-[SRSensorWriter setAuthorized:];
-[SRSensorWriter sensorIdentifier];
-[SRSensorWriter provideSampleData:error:];
-[SRSensorWriter provideSampleData:timestamp:error:];
-[SRSensorWriter chooseAuthStore];
-[SRSensorWriter lastConfigurationContinuousTime];
-[SRSensorWriter updateWriterAuthorizationStatus];
-[SRSensorWriter _requestWriterAuthorizationWithCompletion:];
-[SRSensorWriter _requestedConfigurations];
-[SRSensorWriter _setSensorConfiguration:continuousTimestamp:error:];
-[SRSensorWriter _setSensorConfiguration:error:];
-[SRSensorWriter _writerAuthorizationStatus];
-[SRSensorWriter authStore];
-[SRSensorWriter authorizationStore:didDetermineInitialAuthorizationValues:];
-[SRSensorWriter authorizationStore:didUpdateAuthorizationsForBundleId:sensors:];
-[SRSensorWriter authorizedServicesDidChange:deniedServices:dataCollectionEnabled:onboardingCompleted:lastModifiedTimes:forBundleIdentifier:];
-[SRSensorWriter bundleEligibility:completion:];
-[SRSensorWriter checkForMonitoring];
-[SRSensorWriter daemonForcedResetDatastoreFiles:];
-[SRSensorWriter daemonNotificationDaemonDidChangeTimeSignificantly:];
-[SRSensorWriter daemonNotificationDaemonDidResetDatastore:];
-[SRSensorWriter daemonNotificationDaemonDidStart:];
-[SRSensorWriter didReceiveUpdateToConfigurationRequests];
-[SRSensorWriter eligibilityCache];
-[SRSensorWriter evaluateAuthorizationState];
-[SRSensorWriter evaluateAuthorizationStateWithNewValue:];
-[SRSensorWriter flushDatabase];
-[SRSensorWriter initWithIdentifier:xpcConnection:daemonNotification:authStore:tccStore:];
-[SRSensorWriter lastMetadata];
-[SRSensorWriter lastMetadataContinuousTime];
-[SRSensorWriter nextDatastoreFiles];
-[SRSensorWriter provideSample:];
-[SRSensorWriter provideSample:continuousTimestamp:error:];
-[SRSensorWriter provideSample:error:];
-[SRSensorWriter provideSample:timestamp:];
-[SRSensorWriter provideSample:timestamp:error:];
-[SRSensorWriter provideSampleBytes:length:];
-[SRSensorWriter provideSampleBytes:length:continuousTimestamp:];
-[SRSensorWriter provideSampleBytes:length:continuousTimestamp:error:];
-[SRSensorWriter provideSampleBytes:length:error:];
-[SRSensorWriter provideSampleBytes:length:timestamp:];
-[SRSensorWriter provideSampleBytes:length:timestamp:error:];
-[SRSensorWriter provideSampleData:];
-[SRSensorWriter provideSampleData:continuousTimestamp:];
-[SRSensorWriter provideSampleData:continuousTimestamp:error:];
-[SRSensorWriter provideSampleData:timestamp:];
-[SRSensorWriter registerWithDaemonForWritingIfNeededWithReply:];
-[SRSensorWriter requestNewSegment];
-[SRSensorWriter requestNewSegmentInFlight];
-[SRSensorWriter resetDatastoreFiles:];
-[SRSensorWriter retryGetMonitoring];
-[SRSensorWriter roundingInterval];
-[SRSensorWriter setAuthStore:];
-[SRSensorWriter setConnectionDidInterrupt:];
-[SRSensorWriter setConnectionDidInvalidate:];
-[SRSensorWriter setEligibilityCache:];
-[SRSensorWriter setLastConfigurationContinuousTime:];
-[SRSensorWriter setLastMetadata:];
-[SRSensorWriter setLastMetadataContinuousTime:];
-[SRSensorWriter setMetadata:continuousTimestamp:];
-[SRSensorWriter setMetadata:continuousTimestamp:datastore:];
-[SRSensorWriter setNextDatastoreFiles:];
-[SRSensorWriter setRequestNewSegmentInFlight:];
-[SRSensorWriter setRetryGetMonitoring:];
-[SRSensorWriter setRoundingInterval:];
-[SRSensorWriter setSensorIdentifier:];
-[SRSensorWriter setSourceDevice:error:];
-[SRSensorWriter setTccStore:];
-[SRSensorWriter setWriterAuthorizationUpdateQueue:];
-[SRSensorWriter setWritingStats:];
-[SRSensorWriter set_requestedConfigurations:];
-[SRSensorWriter set_writerAuthorizationStatus:];
-[SRSensorWriter startUpdatingAuthorizations];
-[SRSensorWriter tccStore];
-[SRSensorWriter writerAuthorizationService];
-[SRSensorWriter writerAuthorizationUpdateQueue];
-[SRSensorWriter writingStats];
```
