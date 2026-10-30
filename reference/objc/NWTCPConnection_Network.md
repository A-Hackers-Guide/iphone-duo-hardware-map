# `NWTCPConnection`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 8 instance variables, 22 properties, 46 instance methods, 2 class methods

## Instance variables

```
B _viable;
B _hasBetterPath;
q _state;
@"NWEndpoint" _endpoint;
@"NSError" _internalError;
@"NSObject<OS_nw_connection>" _internalConnection;
@"<NWTCPConnectionAuthenticationDelegate>" _delegate;
@"NWParameters" _parameters;
```

## Properties

```
@property (T@"NWEndpoint",&,N,V_endpoint) endpoint;
@property (T@"NSError",&,V_internalError) internalError;
@property (T@"NSObject<OS_nw_connection>",&,V_internalConnection) internalConnection;
@property (Tq,N,V_state) state;
@property (TB,N,GisViable,V_viable) viable;
@property (TB,N,V_hasBetterPath) hasBetterPath;
@property (T@"<NWTCPConnectionAuthenticationDelegate>",W,V_delegate) delegate;
@property (T@"NWParameters",R,N,V_parameters) parameters;
@property (T@"NSString",R,C,N) privateDescription;
@property (TB,R,N) TFOSucceeded;
@property (TB,R,N) isMultipath;
@property (TQ,R,N) multipathSubflowCount;
@property (TQ,R,N) multipathConnectedSubflowCount;
@property (Ti,R,N) multipathPrimarySubflowInterfaceIndex;
@property (T@"NSDictionary",R,N) multipathSubflowSwitchCounts;
@property (T@"NSDictionary",R,N) TCPInfo;
@property (T@"NSData",R,N) metadata;
@property (T@"NWPath",R,N) connectedPath;
@property (T@"NWEndpoint",R,N) localAddress;
@property (T@"NWEndpoint",R,N) remoteAddress;
@property (T@"NSData",R,N) txtRecord;
@property (T@"NSError",R,N) error;
```

## Class methods

```
+[NWTCPConnection automaticallyNotifiesObserversForKey:];
+[NWTCPConnection stringFromNWTCPConnectionState:];
```

## Instance methods

```
-[NWTCPConnection parameters];
-[NWTCPConnection setState:];
-[NWTCPConnection setEndpoint:];
-[NWTCPConnection txtRecord];
-[NWTCPConnection dealloc];
-[NWTCPConnection endpoint];
-[NWTCPConnection error];
-[NWTCPConnection metadata];
-[NWTCPConnection privateDescription];
-[NWTCPConnection isMultipath];
-[NWTCPConnection descriptionWithIndent:showFullContent:];
-[NWTCPConnection setDelegate:];
-[NWTCPConnection remoteAddress];
-[NWTCPConnection isViable];
-[NWTCPConnection delegate];
-[NWTCPConnection description];
-[NWTCPConnection startInternal];
-[NWTCPConnection initWithEndpoint:parameters:];
-[NWTCPConnection localAddress];
-[NWTCPConnection cancel];
-[NWTCPConnection state];
-[NWTCPConnection TCPInfo];
-[NWTCPConnection TFOSucceeded];
-[NWTCPConnection connectedPath];
-[NWTCPConnection fillOutTCPConnectionInfo:];
-[NWTCPConnection handleIdentityRequestWithMetadata:completionHandler:];
-[NWTCPConnection handlePeerCertificateTrustEvaluationWithMetadata:trust:completionHandler:];
-[NWTCPConnection hasBetterPath];
-[NWTCPConnection initWithAcceptedInternalConnection:];
-[NWTCPConnection initWithEndpoint:parameters:delegate:];
-[NWTCPConnection initWithUpgradeForConnection:];
-[NWTCPConnection internalConnection];
-[NWTCPConnection internalError];
-[NWTCPConnection multipathConnectedSubflowCount];
-[NWTCPConnection multipathPrimarySubflowInterfaceIndex];
-[NWTCPConnection multipathSubflowCount];
-[NWTCPConnection multipathSubflowSwitchCounts];
-[NWTCPConnection readLength:completionHandler:];
-[NWTCPConnection readMinimumLength:maximumLength:completionHandler:];
-[NWTCPConnection setHasBetterPath:];
-[NWTCPConnection setInternalConnection:];
-[NWTCPConnection setInternalError:];
-[NWTCPConnection setViable:];
-[NWTCPConnection setupEventHandler];
-[NWTCPConnection write:completionHandler:];
-[NWTCPConnection writeClose];
```
