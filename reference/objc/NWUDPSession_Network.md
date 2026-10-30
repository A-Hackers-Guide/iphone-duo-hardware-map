# `NWUDPSession`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 14 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _viable;
B _hasBetterPath;
q _state;
@"NWEndpoint" _endpoint;
@"NWEndpoint" _resolvedEndpoint;
@"NWPath" _currentPath;
@"NWDatagramConnection" _connection;
Q _maxReadDatagrams;
@? _readHandler;
Q _internalMTU;
@"NWParameters" _parameters;
```

## Properties

```
@property (T@"NWDatagramConnection",&,V_connection) connection;
@property (TQ,V_maxReadDatagrams) maxReadDatagrams;
@property (T@?,C,V_readHandler) readHandler;
@property (T@"NWEndpoint",&,N,V_resolvedEndpoint) resolvedEndpoint;
@property (T@"NWPath",&,N,V_currentPath) currentPath;
@property (TB,N,GisViable,V_viable) viable;
@property (TB,N,V_hasBetterPath) hasBetterPath;
@property (Tq,N,V_state) state;
@property (TQ,V_internalMTU) internalMTU;
@property (T@"NWParameters",R,V_parameters) parameters;
@property (T@"NSString",R,N) localPort;
@property (T@"NSString",R,C,N) privateDescription;
@property (T@"NWEndpoint",R,V_endpoint) endpoint;
@property (TQ,R,N) maximumDatagramLength;
```

## Class methods

```
+[NWUDPSession automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[NWUDPSession parameters];
-[NWUDPSession setState:];
-[NWUDPSession observeValueForKeyPath:ofObject:change:context:];
-[NWUDPSession dealloc];
-[NWUDPSession endpoint];
-[NWUDPSession initWithConnection:];
-[NWUDPSession privateDescription];
-[NWUDPSession descriptionWithIndent:showFullContent:];
-[NWUDPSession localPort];
-[NWUDPSession connection];
-[NWUDPSession isViable];
-[NWUDPSession setConnection:];
-[NWUDPSession description];
-[NWUDPSession initWithEndpoint:parameters:];
-[NWUDPSession cancel];
-[NWUDPSession setReadHandler:];
-[NWUDPSession state];
-[NWUDPSession setCurrentPath:];
-[NWUDPSession setInternalMTU:];
-[NWUDPSession currentPath];
-[NWUDPSession hasBetterPath];
-[NWUDPSession initWithUpgradeForSession:];
-[NWUDPSession internalMTU];
-[NWUDPSession maxReadDatagrams];
-[NWUDPSession maximumDatagramLength];
-[NWUDPSession readHandler];
-[NWUDPSession readInternal];
-[NWUDPSession resolvedEndpoint];
-[NWUDPSession setHasBetterPath:];
-[NWUDPSession setMaxReadDatagrams:];
-[NWUDPSession setReadHandler:maxDatagrams:];
-[NWUDPSession setResolvedEndpoint:];
-[NWUDPSession setViable:];
-[NWUDPSession setupEventHandler];
-[NWUDPSession tryNextResolvedEndpoint];
-[NWUDPSession writeDatagram:completionHandler:];
-[NWUDPSession writeMultipleDatagrams:completionHandler:];
```
