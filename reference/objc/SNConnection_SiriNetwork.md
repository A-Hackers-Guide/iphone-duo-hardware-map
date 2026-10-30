# `SNConnection`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNConnectionDelegateInternal`, `SNConnectionProtocol`
- 3 instance variables, 3 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<SNConnectionDelegate>" _delegate;
@"SNConnectionInfo" _connectionInfo;
@"SNConnectionInternal" _underlyingConnection;
```

## Properties

```
@property (T@"SNConnectionInfo",&,N,V_connectionInfo) connectionInfo;
@property (T@"SNConnectionInternal",&,N,V_underlyingConnection) underlyingConnection;
@property (T@"<SNConnectionDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SNConnection connectionInfo];
-[SNConnection underlyingConnection];
-[SNConnection init];
-[SNConnection start];
-[SNConnection setDelegate:];
-[SNConnection delegate];
-[SNConnection barrier:];
-[SNConnection sendData:completion:];
-[SNConnection setConnectionInfo:];
-[SNConnection probeConnection];
-[SNConnection setSendPings:];
-[SNConnection didCloseConnection:];
-[SNConnection cancelSynchronously:isOnConnectionQueue:completion:];
-[SNConnection didEncounterError:error:analysisInfo:];
-[SNConnection didEncounterIntermediateError:error:];
-[SNConnection didOpenConnectionType:type:routeId:delay:method:];
-[SNConnection didReceiveAceObject:object:];
-[SNConnection didReceiveObject:object:];
-[SNConnection getSNConnectionAnalysisInfo:];
-[SNConnection getSNConnectionMetrics:completion:];
-[SNConnection initWithConnectionInfo:connectionQueue:];
-[SNConnection sendCommand:completion:];
-[SNConnection sendCommands:completion:];
-[SNConnection setUnderlyingConnection:];
-[SNConnection willStartConnection:type:];
-[SNConnection willStartConnection:with:];
```
