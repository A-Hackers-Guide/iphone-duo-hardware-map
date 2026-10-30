# `LACUserInterfaceRequest`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACRequest`, `NSSecureCoding`
- 13 instance variables, 17 properties, 33 instance methods, 2 class methods

## Instance variables

```
B _isAuditTokenApplicationIdentity;
B _isForSiri;
B _isForSoftwareUpdate;
B _isRunningInRecovery;
B _isRunningInSystemContext;
i _clientProcessId;
I _evaluationRequestIdentifier;
I _identifier;
@"NSXPCListenerEndpoint" _connectionEndpoint;
@"NSData" _clientAuditTokenData;
@"LACClientInfo" _clientInfo;
@"NSNumber" _userId;
@"NSUUID" _contextID;
```

## Properties

```
@property (TI,N,V_identifier) identifier;
@property (TI,N,V_evaluationRequestIdentifier) evaluationRequestIdentifier;
@property (T@"NSUUID",&,N,V_contextID) contextID;
@property (T@"NSData",&,N,V_clientAuditTokenData) clientAuditTokenData;
@property (T@"LACClientInfo",&,N,V_clientInfo) clientInfo;
@property (Ti,N,V_clientProcessId) clientProcessId;
@property (TB,N,V_isAuditTokenApplicationIdentity) isAuditTokenApplicationIdentity;
@property (TB,N,V_isForSiri) isForSiri;
@property (TB,N,V_isForSoftwareUpdate) isForSoftwareUpdate;
@property (TB,N,V_isRunningInRecovery) isRunningInRecovery;
@property (TB,N,V_isRunningInSystemContext) isRunningInSystemContext;
@property (T@"NSNumber",&,N,V_userId) userId;
@property (T@"NSXPCListenerEndpoint",&,N,V_connectionEndpoint) connectionEndpoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACUserInterfaceRequest supportsSecureCoding];
+[LACUserInterfaceRequest unknownInstance];
```

## Instance methods

```
-[LACUserInterfaceRequest setClientInfo:];
-[LACUserInterfaceRequest clientInfo];
-[LACUserInterfaceRequest identifier];
-[LACUserInterfaceRequest setContextID:];
-[LACUserInterfaceRequest init];
-[LACUserInterfaceRequest setIdentifier:];
-[LACUserInterfaceRequest encodeWithCoder:];
-[LACUserInterfaceRequest description];
-[LACUserInterfaceRequest initWithCoder:];
-[LACUserInterfaceRequest clientAuditTokenData];
-[LACUserInterfaceRequest setUserId:];
-[LACUserInterfaceRequest contextID];
-[LACUserInterfaceRequest setClientAuditTokenData:];
-[LACUserInterfaceRequest userId];
-[LACUserInterfaceRequest initWithIdentifier:];
-[LACUserInterfaceRequest connectionEndpoint];
-[LACUserInterfaceRequest setConnectionEndpoint:];
-[LACUserInterfaceRequest isForSiri];
-[LACUserInterfaceRequest setIsForSiri:];
-[LACUserInterfaceRequest clientProcessId];
-[LACUserInterfaceRequest isAuditTokenApplicationIdentity];
-[LACUserInterfaceRequest setEvaluationRequestIdentifier:];
-[LACUserInterfaceRequest evaluationRequestIdentifier];
-[LACUserInterfaceRequest initWithIdentifier:evaluationRequest:];
-[LACUserInterfaceRequest initWithIdentifier:optionalRequest:];
-[LACUserInterfaceRequest isForSoftwareUpdate];
-[LACUserInterfaceRequest isRunningInRecovery];
-[LACUserInterfaceRequest isRunningInSystemContext];
-[LACUserInterfaceRequest setClientProcessId:];
-[LACUserInterfaceRequest setIsAuditTokenApplicationIdentity:];
-[LACUserInterfaceRequest setIsForSoftwareUpdate:];
-[LACUserInterfaceRequest setIsRunningInRecovery:];
-[LACUserInterfaceRequest setIsRunningInSystemContext:];
```
