# Symbols: `/System/Library/PrivateFrameworks/SoftwareUpdateCoreConnect.framework/SoftwareUpdateCoreConnect`

Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). The class-level view is on the [image page](../userland/System__Library__PrivateFrameworks__SoftwareUpdateCoreConnect.framework__SoftwareUpdateCoreConnect.md). **[DSC]**

21 public symbols, 290 private symbols, 0 undefined (imported).

## Public (external)

```
0x1ee94e190  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectBoost
0x1ee94e2a8  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectClient
0x1ee94e3e8  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectClientPolicy
0x1ee94e370  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectClientProxy
0x1ee94e3c0  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectConstants
0x1ee94e348  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectMessage
0x1ee94e230  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectServer
0x1ee94e208  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectServerPolicy
0x1ee94e258  __DATA_DIRTY,__objc_data  _OBJC_CLASS_$_SUCoreConnectVersion
0x1ee94e168  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectBoost
0x1ee94e320  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectClient
0x1ee94e410  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectClientPolicy
0x1ee94e2f8  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectClientProxy
0x1ee94e398  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectConstants
0x1ee94e2d0  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectMessage
0x1ee94e1e0  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectServer
0x1ee94e1b8  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectServerPolicy
0x1ee94e280  __DATA_DIRTY,__objc_data  _OBJC_METACLASS_$_SUCoreConnectVersion
0x1e0d93f80  __DATA_CONST,__const  _kSUCoreConnectClientIDTypeAny
0x1e0d93f78  __DATA_CONST,__const  _kSUCoreConnectMonitorReplyErrorKey
0x1e0d93f70  __DATA_CONST,__const  _kSUCoreConnectMonitorReplyMessageKey
```

## Private

```
0x19ef17e78  __TEXT,__text  +[SUCoreConnectClientPolicy setAllowlistedClasses:forKey:]
0x19ef17ef0  __TEXT,__text  +[SUCoreConnectClientPolicy _getSharedClientAccessQueue]
0x19ef17f28  __TEXT,__text  +[SUCoreConnectClientPolicy _getSharedClientAccessQueue].cold.1
0x19ef17f3c  __TEXT,__text  ___56+[SUCoreConnectClientPolicy _getSharedClientAccessQueue]_block_invoke
0x19ef17fa8  __TEXT,__text  ___59+[SUCoreConnectClientPolicy setAllowlistedClasses:forKeys:]_block_invoke
0x19ef18164  __TEXT,__text  +[SUCoreConnectConstants defaultClasses]
0x19ef182ac  __TEXT,__text  ___63+[SUCoreConnectClientPolicy _getSharedClientAllowlistedClasses]_block_invoke
0x19ef182dc  __TEXT,__text  -[SUCoreConnectClient initWithClientPolicy:]
0x19ef18470  __TEXT,__text  +[SUCoreConnectClient _sharedClientLogger]
0x19ef184a8  __TEXT,__text  +[SUCoreConnectClient _sharedClientLogger].cold.1
0x19ef184bc  __TEXT,__text  ___42+[SUCoreConnectClient _sharedClientLogger]_block_invoke
0x19ef184f8  __TEXT,__text  -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]
0x19ef18ad8  __TEXT,__text  -[SUCoreConnectClient _connectMessageMatchesClient:errorPtr:]
0x19ef18c2c  __TEXT,__text  -[SUCoreConnectClient _internalConnectToServer]
0x19ef191fc  __TEXT,__text  ___Block_byref_object_copy_
0x19ef1920c  __TEXT,__text  ___Block_byref_object_copy_
0x19ef1921c  __TEXT,__text  ___Block_byref_object_copy_
0x19ef1922c  __TEXT,__text  ___Block_byref_object_copy_
0x19ef19238  __TEXT,__text  ___57+[SUCoreConnectServerPolicy getAllowlistedClassesForKey:]_block_invoke
0x19ef19280  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.85
0x19ef19398  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:]
0x19ef19970  __TEXT,__text  -[SUCoreConnectClient connectProtocolFromServerRequestClientID:]
0x19ef19a24  __TEXT,__text  -[SUCoreConnectClient clientReplyCompletionQueue]
0x19ef19a2c  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.87
0x19ef19b00  __TEXT,__text  ___64-[SUCoreConnectClient connectProtocolFromServerRequestClientID:]_block_invoke
0x19ef19b60  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.88
0x19ef19b70  __TEXT,__text  ___88-[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:]_block_invoke
0x19ef19d88  __TEXT,__text  ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke
0x19ef1a064  __TEXT,__text  -[SUCoreConnectMessage .cxx_destruct]
0x19ef1a0cc  __TEXT,__text  -[SUCoreConnectClient clientCompletionQueue]
0x19ef1a0d4  __TEXT,__text  -[SUCoreConnectClient _invalidateConnectionIfNonPersistent:]
0x19ef1a2b4  __TEXT,__text  -[SUCoreConnectClient policy]
0x19ef1a2bc  __TEXT,__text  -[SUCoreConnectClient logger]
0x19ef1a2c4  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.112
0x19ef1a2dc  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2
0x19ef1a490  __TEXT,__text  ___Block_byref_object_dispose_
0x19ef1a498  __TEXT,__text  ___Block_byref_object_dispose_
0x19ef1a4a0  __TEXT,__text  ___Block_byref_object_dispose_
0x19ef1a4a8  __TEXT,__text  ___Block_byref_object_dispose_
0x19ef1a4b0  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.15
0x19ef1a4bc  __TEXT,__text  ___57+[SUCoreConnectClientPolicy getAllowlistedClassesForKey:]_block_invoke
0x19ef1a504  __TEXT,__text  +[SUCoreConnectClientPolicy _getSharedClientAllowlistedClasses]
0x19ef1a560  __TEXT,__text  +[SUCoreConnectClientPolicy _getSharedClientAllowlistedClasses].cold.1
0x19ef1a574  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.111
0x19ef1a980  __TEXT,__text  ___41-[SUCoreConnectServer _removeConnection:]_block_invoke
0x19ef1a9d8  __TEXT,__text  -[SUCoreConnectMessage initWithType:messageName:clientID:version:message:]
0x19ef1a9e0  __TEXT,__text  -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]
0x19ef1ae8c  __TEXT,__text  -[SUCoreConnectMessage clientID]
0x19ef1ae94  __TEXT,__text  -[SUCoreConnectClientPolicy clientID]
0x19ef1ae9c  __TEXT,__text  -[SUCoreConnectClientPolicy usesPersistentXPCConnections]
0x19ef1aea8  __TEXT,__text  -[SUCoreConnectClientPolicy serviceName]
0x19ef1aeb0  __TEXT,__text  -[SUCoreConnectMessage description]
0x19ef1afe4  __TEXT,__text  -[SUCoreConnectMessage message]
0x19ef1afec  __TEXT,__text  +[SUCoreConnectMessage nameForMessageType:]
0x19ef1b050  __TEXT,__text  -[SUCoreConnectMessage version]
0x19ef1b058  __TEXT,__text  -[SUCoreConnectMessage error]
0x19ef1b060  __TEXT,__text  -[SUCoreConnectClientPolicy proxyObjectClasses]
0x19ef1b068  __TEXT,__text  -[SUCoreConnectMessage messageType]
0x19ef1b070  __TEXT,__text  -[SUCoreConnectMessage messageName]
0x19ef1b078  __TEXT,__text  -[SUCoreConnectMessage clientIDRaw]
0x19ef1b07c  __TEXT,__text  -[SUCoreConnectMessage encodeWithCoder:]
0x19ef1b1e4  __TEXT,__text  -[SUCoreConnectServer listener:shouldAcceptNewConnection:]
0x19ef1b76c  __TEXT,__text  -[SUCoreConnectServer logger]
0x19ef1b774  __TEXT,__text  -[SUCoreConnectServer connectionPolicy]
0x19ef1b77c  __TEXT,__text  -[SUCoreConnectServerPolicy serverDelegate]
0x19ef1b79c  __TEXT,__text  -[SUCoreConnectServerPolicy connectionQueue]
0x19ef1b7a4  __TEXT,__text  -[SUCoreConnectServer connectionSendMessageQueue]
0x19ef1b7ac  __TEXT,__text  +[SUCoreConnectMessage supportsSecureCoding]
0x19ef1b7b4  __TEXT,__text  -[SUCoreConnectMessage initWithCoder:]
0x19ef1bd3c  __TEXT,__text  +[SUCoreConnectServerPolicy getAllowlistedClassesForKey:]
0x19ef1be88  __TEXT,__text  +[SUCoreConnectServerPolicy _getSharedServerAccessQueue]
0x19ef1bec0  __TEXT,__text  +[SUCoreConnectServerPolicy _getAllowlistedClassesForKey:]
0x19ef1bfc0  __TEXT,__text  +[SUCoreConnectServerPolicy _getSharedServerAllowlistedClasses]
0x19ef1c01c  __TEXT,__text  -[SUCoreConnectMessage setClientConnectionAuditToken:]
0x19ef1c028  __TEXT,__text  -[SUCoreConnectMessage setBoostable:]
0x19ef1c060  __TEXT,__text  -[SUCoreConnectServer connectionsAccessQueue]
0x19ef1c068  __TEXT,__text  -[SUCoreConnectServer _setConnection:forClientID:]
0x19ef1c2dc  __TEXT,__text  -[SUCoreConnectServer _getAllObserverConnections]
0x19ef1c318  __TEXT,__text  -[SUCoreConnectServer observerConnections]
0x19ef1c320  __TEXT,__text  +[SUCoreConnectClientPolicy getAllowlistedClassesForKey:]
0x19ef1c46c  __TEXT,__text  +[SUCoreConnectClientPolicy _getAllowlistedClassesForKey:]
0x19ef1c548  __TEXT,__text  -[SUCoreConnectClientProxy initWithClientID:completionQueue:genericBlock:]
0x19ef1c550  __TEXT,__text  -[SUCoreConnectClientProxy initWithClientID:completionQueue:genericBlock:progressBlock:]
0x19ef1c6f4  __TEXT,__text  -[SUCoreConnectClientProxy .cxx_destruct]
0x19ef1c750  __TEXT,__text  -[SUCoreConnectServer _removeConnection:]
0x19ef1c9b0  __TEXT,__text  -[SUCoreConnectServer connections]
0x19ef1c9b8  __TEXT,__text  -[SUCoreConnectServer _clientIDForConnection:]
0x19ef1cbd8  __TEXT,__text  -[SUCoreConnectMessage summary]
0x19ef1cc84  __TEXT,__text  -[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]
0x19ef1cd5c  __TEXT,__text  +[SUCoreConnectClientPolicy setAllowlistedClasses:forKeys:]
0x19ef1cef4  __TEXT,__text  -[SUCoreConnectClientPolicy initForServiceName:delegate:clientID:]
0x19ef1cfc8  __TEXT,__text  -[SUCoreConnectClientPolicy setProxyObjectClasses:]
0x19ef1d078  __TEXT,__text  -[SUCoreConnectMessage clientConnectionAuditToken]
0x19ef1d084  __TEXT,__text  ___86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke.120
0x19ef1d210  __TEXT,__text  -[SUCoreConnectMessage initWithType:messageName:clientID:requestID:message:]
0x19ef1d390  __TEXT,__text  -[SUCoreConnectMessage constructedClientID]
0x19ef1d404  __TEXT,__text  +[SUCoreConnectMessage generateRequestID]
0x19ef1d41c  __TEXT,__text  -[SUCoreConnectMessage requestID]
0x19ef1d424  __TEXT,__text  -[SUCoreConnectClient dealloc]
0x19ef1d594  __TEXT,__text  -[SUCoreConnectClient _droppedConnection:]
0x19ef1d784  __TEXT,__text  ___42-[SUCoreConnectClient _droppedConnection:]_block_invoke
0x19ef1d878  __TEXT,__text  ___47-[SUCoreConnectClient _internalConnectToServer]_block_invoke
0x19ef1d9ac  __TEXT,__text  ___47-[SUCoreConnectClient _internalConnectToServer]_block_invoke.87
0x19ef1dae0  __TEXT,__text  -[SUCoreConnectClient connectToServerWithSynchronousCompletion:]
0x19ef1db50  __TEXT,__text  -[SUCoreConnectClient connectToServerWithCompletion:]
0x19ef1dc2c  __TEXT,__text  ___53-[SUCoreConnectClient connectToServerWithCompletion:]_block_invoke
0x19ef1dc68  __TEXT,__text  -[SUCoreConnectClient connectClientSendServerMessage:]
0x19ef1dc74  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke
0x19ef1dc8c  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.104
0x19ef1dd08  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.108
0x19ef1df54  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.109
0x19ef1df6c  __TEXT,__text  ___76-[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:]_block_invoke.115
0x19ef1dfc4  __TEXT,__text  ___86-[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:]_block_invoke
0x19ef1e0c0  __TEXT,__text  -[SUCoreConnectClient forceCloseConnection]
0x19ef1e178  __TEXT,__text  -[SUCoreConnectClient connectProtocolFromServerSendClientMessage:]
0x19ef1e180  __TEXT,__text  -[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]
0x19ef1e51c  __TEXT,__text  ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke
0x19ef1e5fc  __TEXT,__text  ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke_2
0x19ef1e66c  __TEXT,__text  ___72-[SUCoreConnectClient connectProtocolFromServerSendClientMessage:reply:]_block_invoke.126
0x19ef1e684  __TEXT,__text  -[SUCoreConnectClient serverConnection]
0x19ef1e68c  __TEXT,__text  -[SUCoreConnectClient setServerConnection:]
0x19ef1e698  __TEXT,__text  -[SUCoreConnectClient stateLock]
0x19ef1e6a0  __TEXT,__text  -[SUCoreConnectClient clientDelegateCallbackQueue]
0x19ef1e6a8  __TEXT,__text  -[SUCoreConnectClient clientMessageQueue]
0x19ef1e6b0  __TEXT,__text  -[SUCoreConnectClient .cxx_destruct]
0x19ef1e724  __TEXT,__text  _OUTLINED_FUNCTION_0
0x19ef1e724  __TEXT,__text  _OUTLINED_FUNCTION_0
0x19ef1e734  __TEXT,__text  _OUTLINED_FUNCTION_1
0x19ef1e734  __TEXT,__text  _OUTLINED_FUNCTION_1
0x19ef1e748  __TEXT,__text  _OUTLINED_FUNCTION_2
0x19ef1e768  __TEXT,__text  -[SUCoreConnectClientProxy initWithClientID:completionQueue:progressBlock:]
0x19ef1e774  __TEXT,__text  -[SUCoreConnectClientProxy executeGenericBlock:]
0x19ef1e77c  __TEXT,__text  -[SUCoreConnectClientProxy executeGenericBlock:disableVerboseLogging:]
0x19ef1e94c  __TEXT,__text  ___70-[SUCoreConnectClientProxy executeGenericBlock:disableVerboseLogging:]_block_invoke
0x19ef1e99c  __TEXT,__text  -[SUCoreConnectClientProxy executeProgressBlock:]
0x19ef1e9a4  __TEXT,__text  -[SUCoreConnectClientProxy executeProgressBlock:disableVerboseLogging:]
0x19ef1eb74  __TEXT,__text  ___71-[SUCoreConnectClientProxy executeProgressBlock:disableVerboseLogging:]_block_invoke
0x19ef1ebc4  __TEXT,__text  +[SUCoreConnectClientProxy supportsSecureCoding]
0x19ef1ebcc  __TEXT,__text  -[SUCoreConnectClientProxy encodeWithCoder:]
0x19ef1ec2c  __TEXT,__text  -[SUCoreConnectClientProxy initWithCoder:]
0x19ef1ecb8  __TEXT,__text  -[SUCoreConnectClientProxy summary]
0x19ef1ed18  __TEXT,__text  -[SUCoreConnectClientProxy description]
0x19ef1ee04  __TEXT,__text  -[SUCoreConnectClientProxy clientID]
0x19ef1ee0c  __TEXT,__text  -[SUCoreConnectClientProxy clientIDRaw]
0x19ef1ee14  __TEXT,__text  -[SUCoreConnectClientProxy completionQueue]
0x19ef1ee1c  __TEXT,__text  -[SUCoreConnectClientProxy genericBlock]
0x19ef1ee24  __TEXT,__text  -[SUCoreConnectClientProxy progressBlock]
0x19ef1ee2c  __TEXT,__text  _OUTLINED_FUNCTION_0
0x19ef1ee44  __TEXT,__text  _OUTLINED_FUNCTION_1
0x19ef1ee58  __TEXT,__text  -[SUCoreConnectBoost initWithMessage:]
0x19ef1efc4  __TEXT,__text  -[SUCoreConnectBoost description]
0x19ef1f068  __TEXT,__text  -[SUCoreConnectBoost dealloc]
0x19ef1f0b0  __TEXT,__text  -[SUCoreConnectBoost invalidate]
0x19ef1f158  __TEXT,__text  -[SUCoreConnectBoost messageClientID]
0x19ef1f160  __TEXT,__text  -[SUCoreConnectBoost messageName]
0x19ef1f168  __TEXT,__text  -[SUCoreConnectBoost xpcActivityBoost]
0x19ef1f174  __TEXT,__text  -[SUCoreConnectBoost setXpcActivityBoost:]
0x19ef1f17c  __TEXT,__text  -[SUCoreConnectBoost .cxx_destruct]
0x19ef1f1c0  __TEXT,__text  _SUCoreConnectMessageAppendValue
0x19ef1f524  __TEXT,__text  -[SUCoreConnectMessage loggableDescriptionForPolicy:]
0x19ef1f5b4  __TEXT,__text  -[SUCoreConnectMessage loggableLogTypeForPolicy:]
0x19ef1f644  __TEXT,__text  -[SUCoreConnectMessage isBoostable]
0x19ef1f67c  __TEXT,__text  -[SUCoreConnectMessage xpcBoost]
0x19ef1f6e4  __TEXT,__text  -[SUCoreConnectMessage usesConciseLogging]
0x19ef1f6f0  __TEXT,__text  -[SUCoreConnectMessage setUsesConciseLogging:]
0x19ef1f6f8  __TEXT,__text  -[SUCoreConnectMessage usesDebugLogging]
0x19ef1f704  __TEXT,__text  -[SUCoreConnectMessage setUsesDebugLogging:]
0x19ef1f70c  __TEXT,__text  -[SUCoreConnectMessage allowlistedClasses]
0x19ef1f714  __TEXT,__text  -[SUCoreConnectMessage stateLock]
0x19ef1f71c  __TEXT,__text  -[SUCoreConnectMessage setStateLock:]
0x19ef1f724  __TEXT,__text  -[SUCoreConnectClientPolicy initForServiceName:delegate:]
0x19ef1f780  __TEXT,__text  -[SUCoreConnectClientPolicy clientIDRaw]
0x19ef1f784  __TEXT,__text  +[SUCoreConnectClientPolicy setAllowlistedClass:forKey:]
0x19ef1f81c  __TEXT,__text  +[SUCoreConnectClientPolicy clearAllowlistedClasses]
0x19ef1f880  __TEXT,__text  ___52+[SUCoreConnectClientPolicy clearAllowlistedClasses]_block_invoke
0x19ef1f920  __TEXT,__text  -[SUCoreConnectClientPolicy usesConciseLoggingForMessageName:]
0x19ef1f998  __TEXT,__text  -[SUCoreConnectClientPolicy usesDebugLoggingForMessageName:]
0x19ef1fa10  __TEXT,__text  -[SUCoreConnectClientPolicy description]
0x19ef1fb54  __TEXT,__text  -[SUCoreConnectClientPolicy clientDelegate]
0x19ef1fb74  __TEXT,__text  -[SUCoreConnectClientPolicy setUsesPersistentXPCConnections:]
0x19ef1fb7c  __TEXT,__text  -[SUCoreConnectClientPolicy usesConciseMessageLogging]
0x19ef1fb88  __TEXT,__text  -[SUCoreConnectClientPolicy setUsesConciseMessageLogging:]
0x19ef1fb90  __TEXT,__text  -[SUCoreConnectClientPolicy conciseLoggingMessages]
0x19ef1fb9c  __TEXT,__text  -[SUCoreConnectClientPolicy setConciseLoggingMessages:]
0x19ef1fba4  __TEXT,__text  -[SUCoreConnectClientPolicy usesDebugMessageLogging]
0x19ef1fbb0  __TEXT,__text  -[SUCoreConnectClientPolicy setUsesDebugMessageLogging:]
0x19ef1fbb8  __TEXT,__text  -[SUCoreConnectClientPolicy debugLoggingMessages]
0x19ef1fbc4  __TEXT,__text  -[SUCoreConnectClientPolicy setDebugLoggingMessages:]
0x19ef1fbcc  __TEXT,__text  -[SUCoreConnectClientPolicy .cxx_destruct]
0x19ef1fc30  __TEXT,__text  -[SUCoreConnectServerPolicy initWithServiceName:entitlements:serverDelegate:]
0x19ef1fd84  __TEXT,__text  ___56+[SUCoreConnectServerPolicy _getSharedServerAccessQueue]_block_invoke
0x19ef1fdf0  __TEXT,__text  ___63+[SUCoreConnectServerPolicy _getSharedServerAllowlistedClasses]_block_invoke
0x19ef1fe20  __TEXT,__text  +[SUCoreConnectServerPolicy setAllowlistedClass:forKey:]
0x19ef1feb8  __TEXT,__text  +[SUCoreConnectServerPolicy setAllowlistedClasses:forKey:]
0x19ef1ff30  __TEXT,__text  +[SUCoreConnectServerPolicy setAllowlistedClasses:forKeys:]
0x19ef200c8  __TEXT,__text  ___59+[SUCoreConnectServerPolicy setAllowlistedClasses:forKeys:]_block_invoke
0x19ef20284  __TEXT,__text  +[SUCoreConnectServerPolicy clearAllowlistedClasses]
0x19ef202e8  __TEXT,__text  ___52+[SUCoreConnectServerPolicy clearAllowlistedClasses]_block_invoke
0x19ef20388  __TEXT,__text  -[SUCoreConnectServerPolicy usesConciseLoggingForMessageName:]
0x19ef20400  __TEXT,__text  -[SUCoreConnectServerPolicy usesDebugLoggingForMessageName:]
0x19ef20478  __TEXT,__text  -[SUCoreConnectServerPolicy description]
0x19ef205a8  __TEXT,__text  -[SUCoreConnectServerPolicy serviceName]
0x19ef205b0  __TEXT,__text  -[SUCoreConnectServerPolicy entitlements]
0x19ef205b8  __TEXT,__text  -[SUCoreConnectServerPolicy delegateQueue]
0x19ef205c0  __TEXT,__text  -[SUCoreConnectServerPolicy usesConciseMessageLogging]
0x19ef205cc  __TEXT,__text  -[SUCoreConnectServerPolicy setUsesConciseMessageLogging:]
0x19ef205d4  __TEXT,__text  -[SUCoreConnectServerPolicy conciseLoggingMessages]
0x19ef205e0  __TEXT,__text  -[SUCoreConnectServerPolicy setConciseLoggingMessages:]
0x19ef205e8  __TEXT,__text  -[SUCoreConnectServerPolicy usesDebugMessageLogging]
0x19ef205f4  __TEXT,__text  -[SUCoreConnectServerPolicy setUsesDebugMessageLogging:]
0x19ef205fc  __TEXT,__text  -[SUCoreConnectServerPolicy debugLoggingMessages]
0x19ef20608  __TEXT,__text  -[SUCoreConnectServerPolicy setDebugLoggingMessages:]
0x19ef20610  __TEXT,__text  -[SUCoreConnectServerPolicy .cxx_destruct]
0x19ef20680  __TEXT,__text  -[SUCoreConnectServer initWithServerPolicy:]
0x19ef20810  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:]
0x19ef20bc8  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke
0x19ef20da0  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.13
0x19ef20dac  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_3
0x19ef20e30  __TEXT,__text  -[SUCoreConnectServer setupListenerAndResumeConnection]
0x19ef20ed8  __TEXT,__text  ___55-[SUCoreConnectServer setupListenerAndResumeConnection]_block_invoke
0x19ef20fec  __TEXT,__text  ___55-[SUCoreConnectServer setupListenerAndResumeConnection]_block_invoke.90
0x19ef21118  __TEXT,__text  -[SUCoreConnectServer suspendListenerAndInvalidate]
0x19ef211c0  __TEXT,__text  ___51-[SUCoreConnectServer suspendListenerAndInvalidate]_block_invoke
0x19ef21250  __TEXT,__text  ___51-[SUCoreConnectServer suspendListenerAndInvalidate]_block_invoke_2
0x19ef21310  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:]
0x19ef2131c  __TEXT,__text  ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke.114
0x19ef213b4  __TEXT,__text  ___74-[SUCoreConnectServer _informObserversOfCompletionReplyWithMessage:error:]_block_invoke_2
0x19ef2148c  __TEXT,__text  -[SUCoreConnectServer connectServerSendClientMessage:]
0x19ef21540  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke
0x19ef21a74  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.115
0x19ef21b2c  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2
0x19ef21bb0  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.116
0x19ef21c48  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117
0x19ef21ccc  __TEXT,__text  -[SUCoreConnectServer _connectionsForClientID:]
0x19ef21dac  __TEXT,__text  -[SUCoreConnectServer description]
0x19ef21e0c  __TEXT,__text  -[SUCoreConnectServer listener]
0x19ef21e14  __TEXT,__text  -[SUCoreConnectServer setListener:]
0x19ef21e20  __TEXT,__text  -[SUCoreConnectServer .cxx_destruct]
0x19ef21e94  __TEXT,__text  _OUTLINED_FUNCTION_0
0x19ef21eb4  __TEXT,__text  _OUTLINED_FUNCTION_1
0x19ef21ec8  __TEXT,__text  _OUTLINED_FUNCTION_4
0x19ef21edc  __TEXT,__text  _OUTLINED_FUNCTION_5
0x19ef21ee8  __TEXT,__text  _OUTLINED_FUNCTION_6
0x19ef21ef8  __TEXT,__text  _OUTLINED_FUNCTION_7
0x19ef21f0c  __TEXT,__text  _OUTLINED_FUNCTION_8
0x19ef21f18  __TEXT,__text  _OUTLINED_FUNCTION_9
0x19ef21f24  __TEXT,__text  -[SUCoreConnectVersion initWithSelector:]
0x19ef21f8c  __TEXT,__text  -[SUCoreConnectVersion initWithString:]
0x19ef22000  __TEXT,__text  +[SUCoreConnectVersion supportsSecureCoding]
0x19ef22008  __TEXT,__text  -[SUCoreConnectVersion encodeWithCoder:]
0x19ef22068  __TEXT,__text  -[SUCoreConnectVersion initWithCoder:]
0x19ef220f4  __TEXT,__text  -[SUCoreConnectVersion description]
0x19ef22154  __TEXT,__text  -[SUCoreConnectVersion selectorString]
0x19ef2215c  __TEXT,__text  -[SUCoreConnectVersion .cxx_destruct]
0x19ef22168  __TEXT,__text  -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:].cold.1
0x19ef221dc  __TEXT,__text  -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:].cold.2
0x19ef2224c  __TEXT,__text  -[SUCoreConnectClient connectClientSendServerMessage:proxyObject:withReply:].cold.3
0x19ef222bc  __TEXT,__text  -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:].cold.1
0x19ef22330  __TEXT,__text  -[SUCoreConnectClient connectClientSendSynchronousServerMessage:proxyObject:errorPtr:].cold.2
0x19ef223a0  __TEXT,__text  -[SUCoreConnectClientProxy executeGenericBlock:disableVerboseLogging:].cold.1
0x19ef22418  __TEXT,__text  -[SUCoreConnectClientProxy executeProgressBlock:disableVerboseLogging:].cold.1
0x19ef22490  __TEXT,__text  +[SUCoreConnectClientPolicy _getAllowlistedClassesForKey:].cold.1
0x19ef224d4  __TEXT,__text  +[SUCoreConnectServerPolicy _getSharedServerAccessQueue].cold.1
0x19ef224e8  __TEXT,__text  +[SUCoreConnectServerPolicy _getSharedServerAllowlistedClasses].cold.1
0x19ef224fc  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:].cold.1
0x19ef2253c  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:].cold.2
0x19ef2257c  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:].cold.3
0x19ef225bc  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:].cold.4
0x19ef225f8  __TEXT,__text  -[SUCoreConnectServer isConnectionEntitled:].cold.5
0x19ef22634  __TEXT,__text  -[SUCoreConnectServer listener:shouldAcceptNewConnection:].cold.1
0x19ef22670  __TEXT,__text  -[SUCoreConnectServer listener:shouldAcceptNewConnection:].cold.2
0x19ef226ac  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.cold.1
0x19ef226e0  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke.cold.2
0x19ef22714  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.cold.1
0x19ef22754  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.cold.2
0x19ef22788  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_2.cold.3
0x19ef227bc  __TEXT,__text  ___58-[SUCoreConnectServer listener:shouldAcceptNewConnection:]_block_invoke_3.cold.1
0x19ef22804  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.1
0x19ef22804  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.1
0x19ef22864  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.2
0x19ef22864  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.2
0x19ef228c4  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.5
0x19ef22924  __TEXT,__text  -[SUCoreConnectServer connectProtocolFromClientSendServerMessage:proxyObject:withReply:].cold.6
0x19ef22968  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke.cold.1
0x19ef229c4  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.cold.1
0x19ef22a60  __TEXT,__text  ___54-[SUCoreConnectServer connectServerSendClientMessage:]_block_invoke_2.117.cold.1
0x19ef22ad4  __TEXT,__text  -[SUCoreConnectServer _setConnection:forClientID:].cold.1
0x19ef22b3c  __TEXT,__text  -[SUCoreConnectServer _setConnection:forClientID:].cold.2
0x19ef22b70  __TEXT,__text  -[SUCoreConnectServer _removeConnection:].cold.1
0x19ef22bac  __TEXT,__text  -[SUCoreConnectServer _connectionsForClientID:].cold.1
```

