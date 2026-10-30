# `NWConnection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 16 properties, 33 instance methods, 4 class methods

## Instance variables

```
B _internalIsViable;
B _internalHasBetterPath;
q _internalConnectionState;
@"NSError" _internalError;
@"NWPath" _internalPath;
@"NWConcrete_nw_connection" _internalConnection;
```

## Properties

```
@property (Tq,V_internalConnectionState) internalConnectionState;
@property (TB,V_internalIsViable) internalIsViable;
@property (TB,V_internalHasBetterPath) internalHasBetterPath;
@property (T@"NSError",&,V_internalError) internalError;
@property (T@"NWPath",&,V_internalPath) internalPath;
@property (TI,R,N) tlsConnectionTime;
@property (T@"NWConcrete_nw_connection",&,N,V_internalConnection) internalConnection;
@property (T@"NWPath",R,N) currentPath;
@property (T@"NWEndpoint",R,N) endpoint;
@property (T@"NWParameters",R,N) parameters;
@property (Tq,R,N) connectionState;
@property (T@"NWEndpoint",R,N) connectedLocalEndpoint;
@property (T@"NWEndpoint",R,N) connectedRemoteEndpoint;
@property (T@"NSError",R,N) error;
@property (TB,R,N,GisViable) viable;
@property (TB,R,N) hasBetterPath;
```

## Class methods

```
+[NWConnection automaticallyNotifiesObserversForKey:];
+[NWConnection connectionWithConnectedSocket:];
+[NWConnection connectionWithEndpoint:parameters:];
+[NWConnection connectionWithInternalConnection:];
```

## Instance methods

```
-[NWConnection connectionState];
-[NWConnection parameters];
-[NWConnection setInternalPath:];
-[NWConnection start];
-[NWConnection endpoint];
-[NWConnection error];
-[NWConnection isViable];
-[NWConnection internalPath];
-[NWConnection description];
-[NWConnection initWithEndpoint:parameters:];
-[NWConnection cancel];
-[NWConnection copyCurrentPath];
-[NWConnection cancelCurrentEndpoint];
-[NWConnection connectedLocalEndpoint];
-[NWConnection connectedRemoteEndpoint];
-[NWConnection copyError];
-[NWConnection currentPath];
-[NWConnection forceCancel];
-[NWConnection getConnectedSocket];
-[NWConnection hasBetterPath];
-[NWConnection initWithConnectedSocket:];
-[NWConnection initWithInternalConnection:];
-[NWConnection internalConnection];
-[NWConnection internalConnectionState];
-[NWConnection internalError];
-[NWConnection internalHasBetterPath];
-[NWConnection internalIsViable];
-[NWConnection setInternalConnection:];
-[NWConnection setInternalConnectionState:];
-[NWConnection setInternalError:];
-[NWConnection setInternalHasBetterPath:];
-[NWConnection setInternalIsViable:];
-[NWConnection tlsConnectionTime];
```
