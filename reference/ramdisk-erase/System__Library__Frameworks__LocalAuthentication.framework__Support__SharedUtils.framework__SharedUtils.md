# `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 180,864 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 187 (Size: 9432)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils (compatibility version 1.0.0, current version 2319.52.2)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices (compatibility version 1.0.0, current version 1084.40.7, weak)`
- `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit (compatibility version 0.0.0, current version 878.40.5, upward)`
- `/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore (compatibility version 1.0.0, current version 2319.52.2, weak)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (12 classes, 20 protocols)

Classes: `LAACMBiometricAttemptNotifier`, `LAADMUser`, `LAAssertionsProxy`, `LADFR`, `LADecriptionBuilder`, `LAErrorHelper`, `LAErrorOysterRedactor`, `LAErrorRedactor`, `LAInternalProtocols`, `LAPasscodeHelper`, `LASerialSchedulerInternal`, `LAUtils`

Protocols: `LAAssertionsXPC`, `LACContextCallbackXPC`, `LACContextExternalizingXPC`, `LACDarwinNotificationCenterObserver`, `LACRemoteContext`, `LACRemoteUI`, `LACRemoteUIHost`, `LACUIMechanism`, `LAContextClientEvaluationProt`, `LAContextEventFeedbackProt`, `LAContextPropertiesProt`, `LAContextXPC`, `LADFRDelegate`, `LADFRXPC`, `LADaemonXPC`, `LAErrorRedacting`, `LAPrearmContextXPC`, `LAScheduler`, `LAUIDelegate`, `NSObject`

## Strings (397)

```
com.apple.LocalAuthentication
Subcode
Caller is missing the required '%@' entitlement.
,
v16@?0@\"NSError\"8
@\"NSMutableDictionary\"8@?0
com.apple.LocalAuthentication.Storage
%@
YES
com.apple.LocalAuthentication.DFR
com.apple.LocalAuthentication.logging
isSet
Invalid %s type: %@.
LAErrorHelper
<%@: %p> 
com.apple.BiometricKit.matchOperationStartAttempted
BiometryType
<%@; %p; pendingTasks: %d>
Cannot perform operation while disconnected.
q
skip
v8@?0
-[LAAssertionsProxy _remoteObjectProxyWithErrorHandler:]
Could not obtain remote Assertions proxy.
Unexpected error: %@
1
LADFR
LA.oyster.skipSDKVerification
perform
LAAssertionsProxy.m
Missing %s.
NO
type
Failed to connect to LA UI agent (DFR)
errorHandler != nil
Assertions XPC connection was interrupted.
%{public}@
Already connected to LA UI agent (DFR)
New XPC connection to LA UI agent (DFR)
Using cached SDK version
Did acquire TouchID assertion
Will remove TouchID assertion
Raising exception due to error: %{public}@
Will %@ SDK verification
Failed to acquire TouchID assertion: %@
Cannot perform operation while disconnected.
Could not obtain remote Assertions proxy: %@
XPC error: %{public}@
XPC interruption handler (DFR)
LA logging set up for this process.
Could not determine the current SDK version
Did remove TouchID assertion
Assertions XPC connection was invalidated.
Failed to create XPC connection to LA UI agent (DFR)
Will acquire TouchID assertion
Failed to remove TouchID assertion: %@
LAContextClientEvaluationProt
LACRemoteUI
LACContextCallbackXPC
LAInternalProtocols
LAAssertionsXPC
LAAssertionsProxy
LAADMUser
LAErrorOysterRedactor
LACContextExternalizingXPC
LAPrearmContextXPC
LAScheduler
LACDarwinNotificationCenterObserver
LADFRDelegate
LADFRXPC
LAErrorRedactor
LACRemoteUIHost
LAContextPropertiesProt
LAUtils
LAACMBiometricAttemptNotifier
LADFR
LAErrorRedacting
LAContextEventFeedbackProt
LAErrorHelper
NSObject
LACRemoteContext
LADecriptionBuilder
LADaemonXPC
LACUIMechanism
LAPasscodeHelper
LAContextXPC
LAUIDelegate
LASerialSchedulerInternal
_agentConnection
redactError:
setObject:forKey:
storageErrorWithCode:message:
request
_performPendingOperations
description
objectForKeyedSubscript:
initWithObject:
connectRemoteUI:requestID:reply:
debugDescription
errorWithCode:
failProcessedEvent:failureError:reply:
pauseProcessedEvent:pause:reply:
storageErrorWithCode:message:suberror:
verifyFileVaultUser:volumeUuid:options:reply:
isProxy
.cxx_destruct
build
init
operationNotSupportedError
passcodeType
serverPropertyForOption:reply:
credentialsUUIDWithReply:
isSecureBootCapable
resume
setInterface:forSelector:argumentIndex:ofReply:
setServerPropertyForOption:value:reply:
_object
release
_defaults
_queue
_running
conformsToProtocol:
errorWithDomain:code:userInfo:
setCredentialsUUID:reply:
_connection
_connectToUIAgent
connectToExistingContext:callback:clientId:flags:reply:
createUserInitiatedSerialQueueWithIdentifier:
event:params:reply:
initWithQueue:
internalErrorWithMessage:suberror:
isApplePayPolicy:
dealloc
_workQueue
allowTransferToProcess:receiverAuditTokenData:reply:
isAppleSilicon
missingEntitlementError:
notifyBiometricMatchOperationStartAttempted
operationNotSupportedOnDeviceError:
resetProcessedEvent:reply:
TB,R,N
_schedule:
redactInternalError:
retryProcessedEvent:reply:
storageError:hasCode:
stringWithUTF8String:
uiFailureWithError:
unsafeResume
T#,R
UTF8String
bootstrapSessionServiceType:serviceClientID:completionHandler:
initWithMachServiceName:options:
interfaceWithInternalProtocol:
parameterErrorWithMessage:
setCredential:type:options:reply:
setShowingCoachingHint:event:reply:
addObject:
isCredentialSet:reply:
isPasscodeSetForUser:error:
schedule:
setConnection:
setCredential:forProcessedEvent:credentialType:reply:
userInfo
setWithObjects:
_setQueue:
appendBool:withName:
appendString:withName:
integerValue
interfaceWithProtocol:
isGibraltar
length
credentialOfType:reply:
mutableCopy
notificationCenter:didReceiveNotification:
optionsForInternalOperation:reply:
setInvalidationHandler:
stringByAppendingString:
dictionaryWithObjects:forKeys:count:
setObject:forKeyedSubscript:
takeTouchIdAssertionWithReason:reply:
tokenForTransferToUnknownProcess:
silentInternalErrorWithMessage:
hash
internalInfoWithReply:
isRunning
raise:format:
self
updateDFR:options:delegate:reply:
appendString:
eventDFR:eventHints:
internalErrorWithMessage:
persistentDomainForName:
retain
externalizedContextWithReply:
agentConnection
T@\"NSString\",?,R,C
_xpcQueue
class
clearDFR:
dropTouchIdAssertionWithReason:reply:
error:hasCode:subcode:
_performPendingOperationsWithCompletion:
disconnectRemoteUI
evaluateACL:operation:options:uiDelegate:reply:
isKindOfClass:
notifyEvent:options:reply:
parameterErrorForMissingOrInvalidObject:name:
setClasses:forSelector:argumentIndex:ofReply:
sharedInstance
containsObject:
T@\"NSString\",R,C
_performingPendingOperations
boolValue
code
isEqual:
isEqualToString:
respondsToSelector:
_components
TQ,R
numberWithBool:
_pendingOperations
appendObject:withName:
dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:
firstObject
instanceId
addEntriesFromDictionary:
domain
errorDeviceDoesNotSupportAction:
errorWithCode:subcode:message:
operationNotSupportedOnPlatformError:
raiseExceptionOnError:
removeObjectAtIndex:
setAgentConnection:
TI,R,N
_remoteObjectProxyWithErrorHandler:
errorPlatformDoesNotSupportAction:
errorWithCode:message:
performSelector:
setQueue:
transitionToController:internalInfo:completionHandler:
uiEvent:options:
evaluatePolicy:options:uiDelegate:reply:
isConnected
mechanismEvent:reply:
performSelector:withObject:withObject:
setRemoteObjectInterface:
stringWithFormat:
xctErrorWithMessage:suberror:
authMethodWithReply:
checkHasPendingUIRequestsForRemoteUI:completion:
localizedStringForError:
uiSuccessWithResult:
_resume
dumpStatus
performSelector:withObject:
setWithArray:
zone
_minSDKVersion
error:hasCode:
hasBridge
invalidate
errorWithCode:message:moreInfo:
autorelease
failAuthenticationWithError:
invalidatedWithError:
prearmTouchIdWithReply:
remoteObjectProxyWithErrorHandler:
dumpStatusWithCompletion:
mechanismEvent:value:reply:
T@\"<LACEvaluationRequest>\",R,N
createDefaultQueueWithIdentifier:concurrencyAttribute:
initWithXpcQueue:
retainCount
setMinSDKVersion:
superclass
T@\"NSXPCConnection\",&,V_agentConnection
appendInteger:withName:
count
objectForKey:
setOptions:forInternalOperation:reply:
errorWithCode:message:suberror:
error:hasCodeFromArray:
errorWithCode:userInfo:
interfaceForXPCProtocol:
null
setDefaults:
setInterruptionHandler:
standardUserDefaults
unsafeSchedule:
connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:
credentialEncodingSeedWithReply:
errorNotSupported
getDomainStateWithOptions:reply:
invalidateWithReply:
isMemberOfClass:
numberWithInteger:
errorWithCode:subcode:message:suberror:
I16@0:8
v24@0:8@16
v32@0:8@\"<LACRemoteUI>\"16@?<v@?q>24
v56@0:8@16@24@32@40@?48
v40@0:8@16q24@?32
v36@0:8@16B24@?28
v24@0:8@\"NSDictionary\"16
@24@0:8@?16
@32@0:8q16@24
@40@0:8:16@24@32
Vv16@0:8
@\"NSError\"24@0:8@\"NSError\"16
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32
v32@0:8q16@?24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
@\"<LACEvaluationRequest>\"16@0:8
@24@0:8q16
@\"NSString\"16@0:8
v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56
v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32
v48@0:8@16@24Q32@?40
v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16
v40@0:8@16q24@?<v@?B@\"NSError\">32
v36@0:8q16B24@?28
v40@0:8q16@24@?<v@?>32
v40@0:8@16@24@?32
v40@0:8q16@24@?32
v36@0:8i16@\"NSData\"20@?<v@?B@\"NSError\">28
B
@\"NSObject<OS_dispatch_queue>\"
@\"NSXPCConnection\"
@40@0:8q16q24@32
@32@0:8@16@24
v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16
v32@0:8q16@?<v@?B@\"NSError\">24
v24@0:8@?<v@?B@\"NSError\">16
B32@0:8@16@24
v32@0:8@16^{__CFString=}24
v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24
v24@0:8{?=II}16
v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
B32@0:8@16q24
#16@0:8
v48@0:8q16@24@32@?40
v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40
v48@0:8@\"NSUUID\"16@\"NSUUID\"24Q32@?<v@?B@\"NSError\">40
v48@0:8@16q24q32@?40
v24@0:8@\"NSError\"16
v32@0:8q16@\"NSDictionary\"24
B24@0:8@16
@16@0:8
Q16@0:8
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v36@0:8i16@20@?28
v32@0:8q16@24
@32@0:8@16r*24
B16@0:8
B24@0:8:16
v56@0:8@16@24Q32q40@?48
v32@0:8q16@?<v@?@@\"NSError\">24
v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
@40@0:8q16@24@32
v28@0:8B16@20
@24@0:8@16
v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32
@24@0:8:16
{?=\"platform\"I\"version\"I}
v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48
v48@0:8@16q24@32@?40
v36@0:8q16B24@?<v@?B@\"NSError\">28
@\"NSObject\"
@\"NSMutableDictionary\"
B24@0:8@\"Protocol\"16
v16@0:8
v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24
B40@0:8@16q24q32
v32@0:8@16@24
v48@0:8q16@\"NSDictionary\"24@\"<LADFRDelegate>\"32@?<v@?B@\"NSError\">40
^{_NSZone=}16@0:8
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
v40@0:8q16@\"NSError\"24@?<v@?B@\"NSError\">32
v32@0:8q16@?<v@?>24
v24@0:8@?<v@?@?<v@?>>16
@48@0:8q16q24@32@40
B24@0:8#16
v40@0:8q16@24@?<v@?B@\"NSError\">32
v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24
v36@0:8B16q20@?28
v48@0:8@\"NSData\"16q24q32@?<v@?B@\"NSError\">40
v24@0:8@?<v@?@\"NSDictionary\">16
v32@0:8@16@?24
v64@0:8@16@24Q32@40@48@?56
v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48
v36@0:8B16q20@?<v@?B@\"NSError\">28
@\"NSMutableArray\"
@32@0:8:16@24
@\"NSDictionary\"
v24@0:8@?16
```
