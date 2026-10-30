# `ULServer`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULLogicAdapterDelegate`, `ULClientProcessConnectionDelegate`, `NSXPCListenerDelegate`
- 6 instance variables, 18 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULLogicAdapterServiceHandlingInterface>" _serviceHandling;
@"<ULLogicAdapterLegacyServiceHandlingInterface>" _legacyServiceHandling;
@"<ULLogicAdapterDiagnosticsHandlingInterface>" _diagnosticsHandling;
@"<ULLogicAdapterTemporaryMapHandlingInterface>" _temporaryMapHandling;
@"NSMutableSet" _clientConnections;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULLogicAdapterServiceHandlingInterface>",&,N,V_serviceHandling) serviceHandling;
@property (T@"<ULLogicAdapterLegacyServiceHandlingInterface>",&,N,V_legacyServiceHandling) legacyServiceHandling;
@property (T@"<ULLogicAdapterDiagnosticsHandlingInterface>",&,N,V_diagnosticsHandling) diagnosticsHandling;
@property (T@"<ULLogicAdapterTemporaryMapHandlingInterface>",&,N,V_temporaryMapHandling) temporaryMapHandling;
@property (T@"NSMutableSet",&,N,V_clientConnections) clientConnections;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ULServer serviceHandling];
-[ULServer legacyServiceHandling];
-[ULServer setLegacyServiceHandling:];
-[ULServer listener:shouldAcceptNewConnection:];
-[ULServer setTemporaryMapHandling:];
-[ULServer queue];
-[ULServer temporaryMapHandling];
-[ULServer diagnosticsHandling];
-[ULServer setServiceHandling:];
-[ULServer setDiagnosticsHandling:];
-[ULServer setQueue:];
-[ULServer clientConnections];
-[ULServer setClientConnections:];
-[ULServer _remoteProxyForToken:];
-[ULServer clientConnectionSeveredConnection:];
-[ULServer didCompleteObservationWithMetaInformation:toConnection:];
-[ULServer didCompletePredictionWithMetaInformation:toConnection:];
-[ULServer didCompleteRequest:withError:toConnection:];
-[ULServer didCreateCustomLoiAtCurrentLocationWithError:forConnection:];
-[ULServer didFailWithError:toConnection:];
-[ULServer didRemoveCustomLoiWithIdentifier:forConnection:withError:];
-[ULServer didSendGenericEvent:withDescription:toConnection:];
-[ULServer didSendPredictionContextResults:toConnection:];
-[ULServer didUpdateMap:toConnection:];
-[ULServer didUpdateOccupancyGrid:toConnection:];
-[ULServer didUpdatePredictionContextState:toConnection:];
-[ULServer initWithQueue:serviceHandling:legacyServiceHandling:diagnosticsHandling:temporaryMapHandling:];
```
