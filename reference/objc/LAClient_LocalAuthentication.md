# `LAClient`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAContextXPC`, `LACContextCallbackXPC`, `LACContextExternalizing`
- 14 instance variables, 19 properties, 81 instance methods, 3 class methods

## Instance variables

```
B _shouldRecoverConnection;
B _willRetryOnInterruptedConnection;
@"<LAUIDelegate>" _uiDelegate;
@"NSUUID" _uuid;
@"NSString" _proxyId;
@"NSError" _permanentError;
@"NSXPCConnection" _serverConnection;
@"NSObject<LAContextXPC>" _remoteContext;
@"NSObject<LAContextXPC>" _synchronousRemoteContext;
@"NSMutableArray" _invalidations;
@"LACExternalizedContextProvider" _externalizedContextProvider;
@"NSNumber" _userSession;
@"NSData" _existingContext;
@"LAContext" _context;
```

## Properties

```
@property (T@"NSXPCConnection",R,N,V_serverConnection) serverConnection;
@property (T@"NSObject<LAContextXPC>",&,N,V_remoteContext) remoteContext;
@property (T@"NSObject<LAContextXPC>",R,N,V_synchronousRemoteContext) synchronousRemoteContext;
@property (T@"NSMutableArray",R,N,V_invalidations) invalidations;
@property (T@"LACExternalizedContextProvider",&,V_externalizedContextProvider) externalizedContextProvider;
@property (T@"NSError",&,V_permanentError) permanentError;
@property (TB,V_shouldRecoverConnection) shouldRecoverConnection;
@property (TB,V_willRetryOnInterruptedConnection) willRetryOnInterruptedConnection;
@property (T@"NSNumber",R,N,V_userSession) userSession;
@property (T@"NSData",&,N,V_existingContext) existingContext;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (T@"NSString",&,N,V_proxyId) proxyId;
@property (T@"LAContext",R,W,N,V_context) context;
@property (T@"NSData",R,N) externalizedContext;
@property (T@"<LAUIDelegate>",W,N,V_uiDelegate) uiDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LAClient _performInvalidationBlocks:];
+[LAClient createConnection:legacyService:];
+[LAClient _queue];
```

## Instance methods

```
-[LAClient _synchronousRemoteObjectProxy:performCall:];
-[LAClient authMethodWithReply:];
-[LAClient permanentError];
-[LAClient _checkIdResultForTCC:synchronous:error:retryBlock:finally:];
-[LAClient setCredential:type:options:reply:];
-[LAClient verifyFileVaultUser:volumeUuid:options:reply:];
-[LAClient _scheduleRecovery];
-[LAClient synchronousRemoteContext];
-[LAClient userSession];
-[LAClient uuid];
-[LAClient proxyId];
-[LAClient invalidations];
-[LAClient shouldRecoverConnection];
-[LAClient bootstrapServiceType:completionHandler:];
-[LAClient initWithUUID:token:senderAuditTokenData:context:];
-[LAClient setCredential:forProcessedEvent:credentialType:reply:];
-[LAClient serverPropertyForOption:error:];
-[LAClient notifyEvent:options:reply:];
-[LAClient _serializedInvalidateWithMessage:];
-[LAClient serverConnection];
-[LAClient credentialEncodingSeedWithReply:];
-[LAClient _connectToServerWithRecovery:userSession:legacyService:];
-[LAClient dealloc];
-[LAClient setUiDelegate:];
-[LAClient setUuid:];
-[LAClient isCredentialSet:reply:];
-[LAClient resetProcessedEvent:reply:];
-[LAClient setCredentialsUUID:reply:];
-[LAClient getDomainStateWithOptions:reply:];
-[LAClient externalizedContext];
-[LAClient existingContext];
-[LAClient evaluatePolicy:options:uiDelegate:reply:];
-[LAClient setExistingContext:];
-[LAClient pauseProcessedEvent:pause:reply:];
-[LAClient invalidateWithMessage:];
-[LAClient setRemoteContext:];
-[LAClient _performCallBool:finally:];
-[LAClient tokenForTransferToUnknownProcess:];
-[LAClient setShowingCoachingHint:event:reply:];
-[LAClient _recoverConnectionIfNeeded];
-[LAClient invalidatedWithError:];
-[LAClient _performSynchronous:callBool:finally:];
-[LAClient remoteContext];
-[LAClient setServerPropertyForOption:value:error:];
-[LAClient _setPermanentError:];
-[LAClient invalidateWithReply:];
-[LAClient setExternalizedContextProvider:];
-[LAClient setProxyId:];
-[LAClient setOptions:forInternalOperation:reply:];
-[LAClient externalizedContextWithError:];
-[LAClient externalizedContextWithReply:];
-[LAClient _updateOptions:];
-[LAClient _handleConnectionResult:uuid:proxyId:error:];
-[LAClient evaluateACL:operation:options:reply:];
-[LAClient setShouldRecoverConnection:];
-[LAClient setServerPropertyForOption:value:reply:];
-[LAClient willRetryOnInterruptedConnection];
-[LAClient credentialsUUIDWithReply:];
-[LAClient getDomainStateWithOptions:synchronous:reply:];
-[LAClient evaluatePolicy:options:reply:];
-[LAClient credentialOfType:reply:];
-[LAClient allowTransferToProcess:receiverAuditTokenData:reply:];
-[LAClient evaluatePolicy:options:uiDelegate:synchronous:reply:];
-[LAClient _resolveUIDelegateFromDelegate:];
-[LAClient initWithExternalizedContext:userSession:flags:context:];
-[LAClient optionsForInternalOperation:reply:];
-[LAClient prearmTouchIdWithReply:];
-[LAClient failProcessedEvent:failureError:reply:];
-[LAClient retryProcessedEvent:reply:];
-[LAClient evaluateACL:operation:options:uiDelegate:synchronous:reply:];
-[LAClient externalizedContextProvider];
-[LAClient resetWithReply:];
-[LAClient uiDelegate];
-[LAClient _performSynchronous:callId:finally:];
-[LAClient context];
-[LAClient _performCallId:finally:];
-[LAClient _invalidateCachedExternalizedContextWithError:];
-[LAClient evaluateACL:operation:options:uiDelegate:reply:];
-[LAClient setPermanentError:];
-[LAClient setWillRetryOnInterruptedConnection:];
-[LAClient serverPropertyForOption:reply:];
```
