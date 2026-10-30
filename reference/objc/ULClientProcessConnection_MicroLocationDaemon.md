# `ULClientProcessConnection`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULXPCRequestProtocol`
- 11 instance variables, 15 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _serviceIdentifier;
@"NSUUID" _connectionToken;
@"NSString" _signingIdentity;
@"<ULXPCResponseProtocol>" _remoteObjectProxy;
@"<ULLogicAdapterServiceHandlingInterface>" _serviceHandling;
@"<ULLogicAdapterLegacyServiceHandlingInterface>" _legacyServiceHandling;
@"<ULLogicAdapterDiagnosticsHandlingInterface>" _diagnosticsHandling;
@"<ULLogicAdapterTemporaryMapHandlingInterface>" _temporaryMapHandling;
@"<ULClientProcessConnectionDelegate>" _delegate;
@"NSXPCConnection" _xpcConnection;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"<ULXPCResponseProtocol>",&,N,V_remoteObjectProxy) remoteObjectProxy;
@property (T@"<ULLogicAdapterServiceHandlingInterface>",&,N,V_serviceHandling) serviceHandling;
@property (T@"<ULLogicAdapterLegacyServiceHandlingInterface>",&,N,V_legacyServiceHandling) legacyServiceHandling;
@property (T@"<ULLogicAdapterDiagnosticsHandlingInterface>",&,N,V_diagnosticsHandling) diagnosticsHandling;
@property (T@"<ULLogicAdapterTemporaryMapHandlingInterface>",&,N,V_temporaryMapHandling) temporaryMapHandling;
@property (T@"<ULClientProcessConnectionDelegate>",W,N,V_delegate) delegate;
@property (T@"NSXPCConnection",&,N,V_xpcConnection) xpcConnection;
@property (T@"NSString",&,N,V_signingIdentity) signingIdentity;
@property (T@"NSUUID",&,N,V_connectionToken) connectionToken;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSUUID",&,N,V_serviceIdentifier) serviceIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULClientProcessConnection removeCustomLocationOfInterestWithIdentifier:];
-[ULClientProcessConnection serviceHandling];
-[ULClientProcessConnection legacyServiceHandling];
-[ULClientProcessConnection addLabel:];
-[ULClientProcessConnection setLegacyServiceHandling:];
-[ULClientProcessConnection requestPredictionWithRequestIdentifier:];
-[ULClientProcessConnection requestAllModelsLearningWithRequestIdentifier:];
-[ULClientProcessConnection exportDatabaseWithReply:];
-[ULClientProcessConnection removeAllModelsOfType:reply:];
-[ULClientProcessConnection updateHomeKitUserInteractionLabel:];
-[ULClientProcessConnection setXpcConnection:];
-[ULClientProcessConnection donateMicroLocationTruthTagWithTagUUID:forRecordingEventsBetweenDate:andDate:handler:];
-[ULClientProcessConnection dealloc];
-[ULClientProcessConnection requestMicroLocationRecordingScanWithAdditionalInformation:reply:];
-[ULClientProcessConnection setTemporaryMapHandling:];
-[ULClientProcessConnection createServiceWithServiceType:locationTypes:reply:];
-[ULClientProcessConnection queue];
-[ULClientProcessConnection getMicroLocationInternalVersionWithReply:];
-[ULClientProcessConnection temporaryMapHandling];
-[ULClientProcessConnection setRemoteObjectProxy:];
-[ULClientProcessConnection requestCurrentMicroLocationWithAdditionalInformation:reply:];
-[ULClientProcessConnection xpcConnection];
-[ULClientProcessConnection visualLoggerAddDestinationWithHost:];
-[ULClientProcessConnection addLabel:betweenStartDate:andEndDate:];
-[ULClientProcessConnection peripheralDebugTask:reply:];
-[ULClientProcessConnection imageFeaturesDebugWithTask:additionalInformation:reply:];
-[ULClientProcessConnection purgeDatabaseWithReply:];
-[ULClientProcessConnection getRecordingTriggerUUIDAndRequestMicroLocationRecordingScanWithAdditionalInformation:shouldForceRecording:handler:];
-[ULClientProcessConnection setDelegate:];
-[ULClientProcessConnection setConnectionToken:];
-[ULClientProcessConnection signingIdentity];
-[ULClientProcessConnection requestObservationWithRequestIdentifier:];
-[ULClientProcessConnection diagnosticsHandling];
-[ULClientProcessConnection setServiceHandling:];
-[ULClientProcessConnection initWithXPCConnection:delegate:serviceHandling:legacyServiceHandling:diagnosticsHandling:temporaryMapHandling:queue:];
-[ULClientProcessConnection requestMapReconstructionWithRequestIdentifier:];
-[ULClientProcessConnection exportVisualLoggerDataWithReply:];
-[ULClientProcessConnection delegate];
-[ULClientProcessConnection terminateDaemonWithReply:];
-[ULClientProcessConnection setServiceIdentifier:];
-[ULClientProcessConnection createCustomLocationOfInterestAtCurrentLocationWithConfiguration:];
-[ULClientProcessConnection setSigningIdentity:];
-[ULClientProcessConnection deleteServiceWithIdentifier:reply:];
-[ULClientProcessConnection description];
-[ULClientProcessConnection connectionToken];
-[ULClientProcessConnection disconnectWithRequestIdentifier:];
-[ULClientProcessConnection serviceIdentifier];
-[ULClientProcessConnection runWithConfiguration:serviceIdentifier:legacyServiceIdentifier:andRequestIdentifier:];
-[ULClientProcessConnection queryServicesWithReply:];
-[ULClientProcessConnection injectNPDRFrameData:reply:];
-[ULClientProcessConnection donateMicroLocationTruthTagWithTagUUID:correspondingToTriggerUUID:handler:];
-[ULClientProcessConnection remoteObjectProxy];
-[ULClientProcessConnection clearAllLabelsForContextLayer:reply:];
-[ULClientProcessConnection configureVisualLoggerStreamWithIdentifier:networkHost:networkPort:];
-[ULClientProcessConnection setDiagnosticsHandling:];
-[ULClientProcessConnection setQueue:];
```
