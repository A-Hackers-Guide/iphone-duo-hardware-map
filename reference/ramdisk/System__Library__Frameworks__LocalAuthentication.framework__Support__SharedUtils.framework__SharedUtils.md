# `/System/Library/Frameworks/LocalAuthentication.framework/Support/SharedUtils.framework/SharedUtils`

From the upgrade restore ramdisk (141-29011-104.dmg). 180,864 bytes.

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
Will %@ SDK verification
Assertions XPC connection was invalidated.
Raising exception due to error: %{public}@
Already connected to LA UI agent (DFR)
Failed to create XPC connection to LA UI agent (DFR)
XPC interruption handler (DFR)
Will acquire TouchID assertion
Failed to remove TouchID assertion: %@
Could not obtain remote Assertions proxy: %@
Assertions XPC connection was interrupted.
%{public}@
Could not determine the current SDK version
Failed to acquire TouchID assertion: %@
Did acquire TouchID assertion
Cannot perform operation while disconnected.
XPC error: %{public}@
New XPC connection to LA UI agent (DFR)
Using cached SDK version
Will remove TouchID assertion
Did remove TouchID assertion
LA logging set up for this process.
NSObject
LACUIMechanism
LAPasscodeHelper
LADFRDelegate
LAUIDelegate
LAAssertionsXPC
LAErrorRedacting
LAContextClientEvaluationProt
LAInternalProtocols
LADecriptionBuilder
LACDarwinNotificationCenterObserver
LADFRXPC
LACRemoteUIHost
LADaemonXPC
LAContextXPC
LACRemoteUI
LAUtils
LAADMUser
LAACMBiometricAttemptNotifier
LAErrorOysterRedactor
LAContextPropertiesProt
LAPrearmContextXPC
LAAssertionsProxy
LAErrorHelper
LAErrorRedactor
LASerialSchedulerInternal
LACContextExternalizingXPC
LACRemoteContext
LACContextCallbackXPC
LAContextEventFeedbackProt
LAScheduler
LADFR
connectToExistingContext:callback:clientId:flags:reply:
isApplePayPolicy:
isAppleSilicon
notifyEvent:options:reply:
operationNotSupportedOnPlatformError:
parameterErrorWithMessage:
unsafeSchedule:
_resume
interfaceWithInternalProtocol:
invalidate
setAgentConnection:
clearDFR:
connectRemoteUI:requestID:reply:
numberWithInteger:
errorWithCode:message:suberror:
appendString:withName:
code
internalErrorWithMessage:
pauseProcessedEvent:pause:reply:
performSelector:withObject:
resetProcessedEvent:reply:
setCredential:type:options:reply:
addObject:
credentialEncodingSeedWithReply:
dictionaryWithObjects:forKeys:count:
error:hasCode:subcode:
internalInfoWithReply:
isCredentialSet:reply:
isPasscodeSetForUser:error:
storageErrorWithCode:message:suberror:
evaluateACL:operation:options:uiDelegate:reply:
setInterface:forSelector:argumentIndex:ofReply:
takeTouchIdAssertionWithReason:reply:
_setQueue:
autorelease
count
dropTouchIdAssertionWithReason:reply:
setShowingCoachingHint:event:reply:
uiFailureWithError:
zone
agentConnection
T@\"NSString\",?,R,C
eventDFR:eventHints:
failProcessedEvent:failureError:reply:
setDefaults:
setInvalidationHandler:
setMinSDKVersion:
uiEvent:options:
_connection
allowTransferToProcess:receiverAuditTokenData:reply:
conformsToProtocol:
errorPlatformDoesNotSupportAction:
interfaceForXPCProtocol:
isGibraltar
isKindOfClass:
respondsToSelector:
T#,R
numberWithBool:
request
disconnectRemoteUI
retain
unsafeResume
containsObject:
_defaults
description
externalizedContextWithReply:
performSelector:withObject:withObject:
retainCount
setCredential:forProcessedEvent:credentialType:reply:
setObject:forKey:
_components
_object
TI,R,N
TQ,R
setClasses:forSelector:argumentIndex:ofReply:
transitionToController:internalInfo:completionHandler:
boolValue
build
invalidateWithReply:
notificationCenter:didReceiveNotification:
setCredentialsUUID:reply:
isProxy
authMethodWithReply:
errorWithCode:subcode:message:suberror:
interfaceWithProtocol:
objectForKeyedSubscript:
redactError:
remoteObjectProxyWithErrorHandler:
retryProcessedEvent:reply:
.cxx_destruct
_workQueue
_xpcQueue
appendBool:withName:
bootstrapSessionServiceType:serviceClientID:completionHandler:
createDefaultQueueWithIdentifier:concurrencyAttribute:
debugDescription
firstObject
createUserInitiatedSerialQueueWithIdentifier:
dumpStatus
errorNotSupported
errorWithCode:
storageErrorWithCode:message:
updateDFR:options:delegate:reply:
addEntriesFromDictionary:
setQueue:
_performPendingOperations
getDomainStateWithOptions:reply:
hasBridge
performSelector:
tokenForTransferToUnknownProcess:
dealloc
TB,R,N
_performingPendingOperations
_queue
_remoteObjectProxyWithErrorHandler:
dumpStatusWithCompletion:
errorWithCode:message:
initWithXpcQueue:
appendObject:withName:
dismissRemoteUIWithIdleEndpoint:wasInvalidated:completionHandler:
integerValue
isMemberOfClass:
missingEntitlementError:
persistentDomainForName:
setRemoteObjectInterface:
setServerPropertyForOption:value:reply:
T@\"<LACEvaluationRequest>\",R,N
_schedule:
appendString:
connectToContextWithUUID:callback:clientId:token:senderAuditTokenData:reply:
credentialOfType:reply:
error:hasCode:
error:hasCodeFromArray:
isEqual:
domain
errorWithCode:subcode:message:
errorWithCode:userInfo:
invalidatedWithError:
isEqualToString:
mutableCopy
notifyBiometricMatchOperationStartAttempted
objectForKey:
setWithObjects:
isRunning
localizedStringForError:
operationNotSupportedOnDeviceError:
prearmTouchIdWithReply:
schedule:
self
serverPropertyForOption:reply:
_running
credentialsUUIDWithReply:
errorWithDomain:code:userInfo:
mechanismEvent:value:reply:
parameterErrorForMissingOrInvalidObject:name:
raise:format:
redactInternalError:
removeObjectAtIndex:
initWithObject:
init
internalErrorWithMessage:suberror:
isConnected
mechanismEvent:reply:
resume
setOptions:forInternalOperation:reply:
sharedInstance
_connectToUIAgent
checkHasPendingUIRequestsForRemoteUI:completion:
initWithMachServiceName:options:
null
standardUserDefaults
stringWithUTF8String:
userInfo
T@\"NSString\",R,C
class
errorDeviceDoesNotSupportAction:
failAuthenticationWithError:
instanceId
setConnection:
setInterruptionHandler:
setWithArray:
UTF8String
silentInternalErrorWithMessage:
_minSDKVersion
_pendingOperations
_performPendingOperationsWithCompletion:
event:params:reply:
raiseExceptionOnError:
stringWithFormat:
release
errorWithCode:message:moreInfo:
initWithQueue:
passcodeType
setObject:forKeyedSubscript:
storageError:hasCode:
verifyFileVaultUser:volumeUuid:options:reply:
T@\"NSXPCConnection\",&,V_agentConnection
appendInteger:withName:
isSecureBootCapable
operationNotSupportedError
superclass
uiSuccessWithResult:
xctErrorWithMessage:suberror:
length
stringByAppendingString:
_agentConnection
evaluatePolicy:options:uiDelegate:reply:
hash
optionsForInternalOperation:reply:
v40@0:8q16@\"NSError\"24@?<v@?B@\"NSError\">32
v36@0:8i16@\"NSData\"20@?<v@?B@\"NSError\">28
@40@0:8q16@24@32
#16@0:8
v32@0:8q16@?<v@?@@\"NSError\">24
v48@0:8@16@24Q32@?40
v40@0:8@16q24@?<v@?B@\"NSError\">32
v24@0:8@\"NSError\"16
v32@0:8q16@\"NSDictionary\"24
@\"<LACEvaluationRequest>\"16@0:8
B
v24@0:8@16
v40@0:8q16@\"NSDictionary\"24@?<v@?B@\"NSError\">32
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
@32@0:8q16@24
@32@0:8:16@24
B24@0:8@\"Protocol\"16
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\"@\"NSError\">32
v32@0:8q16@?24
v48@0:8@16q24@32@?40
v24@0:8@?<v@?B@\"NSError\">16
v48@0:8@16q24q32@?40
v36@0:8@16B24@?28
v36@0:8q16B24@?28
@24@0:8@?16
@\"NSMutableDictionary\"
B16@0:8
@\"NSString\"16@0:8
@\"NSDictionary\"
{?=\"platform\"I\"version\"I}
v40@0:8q16@24@?32
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v24@0:8@?<v@?@\"NSUUID\"@\"NSError\">16
v40@0:8q16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32
v16@0:8
@\"NSXPCConnection\"
@32@0:8@16@24
v32@0:8@16@24
v28@0:8B16@20
v32@0:8@\"<LACDarwinNotificationCenter>\"16^{__CFString=}24
@24@0:8:16
B24@0:8#16
B24@0:8:16
Vv16@0:8
v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48
v48@0:8q16@24@32@?40
v40@0:8@16q24@?32
v40@0:8q16@24@?<v@?>32
v40@0:8@16@24@?32
v56@0:8@16@24Q32q40@?48
v24@0:8@\"NSDictionary\"16
@32@0:8@16r*24
v40@0:8q16@24@?<v@?B@\"NSError\">32
v32@0:8@\"NSUUID\"16@?<v@?B@\"NSError\">24
v32@0:8q16@24
v24@0:8@?<v@?@?<v@?>>16
@\"NSMutableArray\"
@24@0:8q16
@40@0:8q16q24@32
B32@0:8@16q24
@16@0:8
^{_NSZone=}16@0:8
v32@0:8@16@?24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\"@\"NSError\">24
v48@0:8@\"NSData\"16q24q32@?<v@?B@\"NSError\">40
I16@0:8
@\"NSObject\"
v32@0:8@16^{__CFString=}24
@24@0:8@16
v32@0:8@\"<LACRemoteUI>\"16@?<v@?q>24
v24@0:8@?16
v36@0:8B16q20@?28
v36@0:8B16q20@?<v@?B@\"NSError\">28
@\"NSObject<OS_dispatch_queue>\"
Q16@0:8
v40@0:8@\"<LACRemoteUI>\"16@\"NSNumber\"24@?<v@?@\"<LACUIMechanism>\"@\"<LACBackoffCounter>\"@\"NSData\"@\"NSError\">32
v56@0:8@16@24@32@40@?48
v48@0:8q16@\"NSDictionary\"24@\"<LADFRDelegate>\"32@?<v@?B@\"NSError\">40
@\"NSError\"24@0:8@\"NSError\"16
v24@0:8{?=II}16
B24@0:8@16
v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56
v24@0:8@?<v@?@\"<LAPrearmContextXPC>\"@\"NSError\">16
v32@0:8q16@?<v@?B@\"NSError\">24
v48@0:8@\"NSData\"16q24@\"NSDictionary\"32@?<v@?B@\"NSError\">40
B40@0:8@16q24q32
v48@0:8q16@\"NSDictionary\"24@\"<LACContextUIDelegate>\"32@?<v@?@\"NSDictionary\"@\"NSError\">40
v36@0:8q16B24@?<v@?B@\"NSError\">28
v36@0:8i16@20@?28
v32@0:8q16@?<v@?>24
v36@0:8@\"NSXPCListenerEndpoint\"16B24@?<v@?>28
v24@0:8@?<v@?@\"NSDictionary\">16
@48@0:8q16q24@32@40
B32@0:8@16@24
@40@0:8:16@24@32
v64@0:8@16@24Q32@40@48@?56
v56@0:8@\"NSData\"16@24@\"NSDictionary\"32@\"<LACContextUIDelegate>\"40@?<v@?@\"NSDictionary\"@\"NSError\">48
v32@0:8q16@?<v@?@\"NSData\"@\"NSError\">24
v48@0:8@\"NSUUID\"16@\"NSUUID\"24Q32@?<v@?B@\"NSError\">40
LA.oyster.skipSDKVerification
BiometryType
errorHandler != nil
Invalid %s type: %@.
LAErrorHelper
YES
com.apple.LocalAuthentication.Storage
type
LADFR
q
Missing %s.
<%@: %p> 
1
Failed to connect to LA UI agent (DFR)
perform
v8@?0
v16@?0@\"NSError\"8
com.apple.LocalAuthentication.DFR
%@
isSet
LAAssertionsProxy.m
Subcode
@\"NSMutableDictionary\"8@?0
NO
com.apple.LocalAuthentication.logging
,
com.apple.LocalAuthentication
Caller is missing the required '%@' entitlement.
Unexpected error: %@
com.apple.BiometricKit.matchOperationStartAttempted
Could not obtain remote Assertions proxy.
skip
<%@; %p; pendingTasks: %d>
-[LAAssertionsProxy _remoteObjectProxyWithErrorHandler:]
Cannot perform operation while disconnected.
```
