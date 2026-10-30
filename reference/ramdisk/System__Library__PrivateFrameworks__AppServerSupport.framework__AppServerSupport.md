# `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

From the upgrade restore ramdisk (141-29011-104.dmg). 207,376 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 3504)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (5)

- `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport (compatibility version 1.0.0, current version 3298.52.1)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (16 classes, 5 protocols)

Classes: `LASSProperties4RB`, `NSArray`, `NSData`, `NSDictionary`, `NSMutableDictionary`, `NSNumber`, `NSString`, `NSUUID`, `OSLaunchdDeveloperToolsOptions`, `OSLaunchdDomain`, `OSLaunchdError`, `OSLaunchdJob`, `OSLaunchdJobExitStatus`, `OSLaunchdJobInfo`, `OSLaunchdJobInstanceProperties`, `OSLaunchdJobProperties`

Protocols: `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `_OSXPCObjectRepresentable`

## Strings (601)

```
NSCoding
OSLaunchdJob
OSLaunchdJobExitStatus
NSCopying
OSLaunchdJobProperties
LASSProperties4RB
_OSXPCObjectRepresentable
OSLaunchdDomain
OSLaunchdJobInfo
OSLaunchdError
AppServiceSupportAdditions
NSSecureCoding
NSObject
OSLaunchdJobInstanceProperties
OSLaunchdDeveloperToolsOptions
TB,N,V_omitSandboxParameters
roleAccount
_lastSpawnError
T@\"NSString\",C,N,V_runLoopType
remove:
T@\"NSString\",C,N,V_sandboxProfile
hostPID
T@\"NSString\",C,N,V_label
_serviceType
copyJobWithHandle:
enableTransactions
joinExistingSession
lastSpawnError
setEnvironmentVariables:
unpendLaunches:
lightweightCodeRequirement
numberWithUnsignedInt:
setMtAddressSanitizer:
_sandboxProfile
_sandboxContainer
autorelease
conclave
copy
performSelector:
T@\"NSDictionary\",C,N,V_spawnConstraint
TI,R,N,V_os_reason_namespace
setArguments:
submitExtension:overlay:domain:error:
wait4Status
T@\"NSSet\",C,N,V_managedEndpointLaunchIdentifiers
additionalProperties
createDomainForRoleAccount:sessionType:options:error:
T@\"NSDictionary\",C,N,V_arguments
threadSanitizer
T@\"NSString\",R,C
_runAtLoad
_watchdogTimeout
copyJobWithLabel:domain:
_instance
_programArguments
jobStateFromMessage:
programArguments
propertiesForPid:error:
isProxy
TB,R
setLabel:
T@\"NSString\",C,N,V_uiApplicationDelegateClass
_keepAlive
count
encodeBool:forKey:
isMemberOfClass:
setUndefinedBehaviorSanitizer:
T@\"NSString\",C,N,V_serviceType
T@\"NSURL\",C,N,V_sandboxContainer
_createDomainOptions2flags:
serviceType
systemDomain
Ti,R,N,V_wait4Status
arrayWithCapacity:
countByEnumeratingWithState:objects:count:
path
setValue:forKey:
_endpoints
_hostPID
_newSubmitRequest
endpoints
Ti,R,N,V_hostPID
_mtAddressSanitizer
_wait4Status
xpcOverlay
setServiceType:
_os_reason_flags
_removing
_submitExtension:overlay:domain:properties:error:
retainCount
sandboxProfile
submitExtensionAtURL:properties:domain:error:
_domain
T@\"NSString\",R,C,N,V_program
_enterprisePersona
_lightweightCodeRequirement
_runLoopType
performSelector:withObject:
requestedJetsamPriority
watchdogTimeout
overlay
_conclave
arguments
respondsToSelector:
setAddressSanitizer:
_additionalProperties
cancelMonitor
TQ,R,N,V_os_reason_code
addressSanitizer
createInstance:error:
mtAddressSanitizer
processSubmitReply:
setAdditionalProperties:
numberWithBool:
TQ,R
numberWithUnsignedChar:
setOverlay:
setThreadSanitizer:
T@\"NSObject<OS_xpc_object>\",R,N,V_endpoints
T@\"NSURL\",&,N,V_sandboxContainer
_additionalPropertiesDictionary
T@\"NSUUID\",&,N,V_oneShotUUID
TB,N
addObject:
initWithCoder:
xpcBundle
_type
setDisableLogging_4watchdogd:
T@\"NSDictionary\",C,N,V_overlay
T@\"NSString\",C,N,V_processType
TI,R,N,V_processType
_additionalSubServices
_enablePressuredExit
_populateHandle:
oneShotUUID
runAtLoad
setOneShotUUID:
T@\"NSString\",C,N,V_personaString
self
setupMonitorOnQueue:withHandler:reply:
spawnConstraint
_createSubmitExtensionRequest:overlay:domain:properties:
_pid
currentDomain
debugDescription
T@\"NSString\",R,N,V_label
copyWithZone:
developerToolsOptions
omitSandboxParameters
zone
_handlesToJobs:
encodeWithCoder:
initiateRemoval:
start:
T@\"NSUUID\",R,N,V_instance
additionalPropertiesDictionary
length
setAdditionalSubServices:
_os_reason_code
TB,R,N,V_enableTransactions
_managedByServices
_processType
abandonCoalition
init
runLoopType
domainForBackgroundUser:
getCurrentJobInfo
T@\"NSDictionary\",C,N,V_additionalSubServices
_label
_personaString
_threadSanitizer
removing
TB,N,V_mtAddressSanitizer
Ti,R,N,V_requestedJetsamPriority
_createJobFromReplyHandle:
_omitSandboxParameters
boolValue
isEqual:
objectAtIndexedSubscript:
supportsSecureCoding
_program
domainForRoleAccountUser:
isKindOfClass:
performSelector:withObject:withObject:
setWatchdogTimeout:
_handle
createXPCError:
TB,R,N,V_xpcBundle
Tq,R,N,V_serviceType
_monitor_handler
_oneShotUUID
_setupMonitorSourceWithPort:onQueue:withHandler:
description
T@\"NSString\",R,N,V_program
_OS_overlayDictionary:
_xpcBundle
initWithWait4Status:os_reason_namespace:os_reason_code:os_reason_flags:
setEnterprisePersona:
setLightweightCodeRequirement:
stringWithUTF8String:
T@\"OSLaunchdDeveloperToolsOptions\",C,N,V_developerToolsOptions
TB,N,V_threadSanitizer
objectForKeyedSubscript:
retain
stringWithFormat:
T@\"NSString\",C,N,V_roleAccount
setProcessType:
_environmentVariables
bytes
valueForKey:
release
T@\"NSArray\",C,N,V_managedByServices
TB,R,N,V_enablePressuredExit
_os_reason_namespace
copyJobsLoadedByCoalition:error:
copyJobsLoadedByJob:
dictionaryWithObjects:forKeys:count:
setManagedEndpointLaunchIdentifiers:
T@\"NSData\",C,N,V_lightweightCodeRequirement
T@\"NSObject<OS_xpc_object>\",R,N,V_additionalPropertiesDictionary
T@\"NSString\",C,N,V_conclave
TB,R,N,V_keepAlive
_abandonCoalition
_platform
state
_lastExitStatus
_newCreateInstanceRequest:properties:
initWithPlist:domain:
loginwindowDomain
setPlatform:
TI,N,V_platform
T#,R
TB,N,V_addressSanitizer
_propertiesFromAttrs:
_uiApplicationClass
_uiApplicationDelegateClass
hash
initWithPlist:
T@\"NSArray\",C,N,V_programArguments
T@\"NSDictionary\",C,N,V_additionalProperties
copyJobWithPid:
.cxx_destruct
_arguments
_newRequest
createInstance:properties:error:
propertiesForJob:error:
TB,N,V_watchdogTimeout
additionalSubServices
os_reason_code
setJoinExistingSession:
setPersonaString:
submitAll:error:
_monitorNormalizeError:
_requestedJetsamPriority
jobInfoFromMessage:
label
setOmitSandboxParameters:
setSpawnConstraint:
os_reason_flags
domainForAsid:
setUiApplicationClass:
toDictionary
_monitor_source
TB,N,V_joinExistingSession
TI,N,V_enterprisePersona
_monitor_queue
initWithUUIDBytes:
setSandboxContainer:
uiApplicationDelegateClass
undefinedBehaviorSanitizer
TB,N,V_abandonCoalition
type
TB,N,V_undefinedBehaviorSanitizer
TB,R,N,V_runAtLoad
personaString
T@\"NSString\",R,N,V_path
_addressSanitizer
_overlay
_plist
initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:
numberWithUnsignedLong:
setAbandonCoalition:
Ti,R,N,V_pid
_state
setProgramArguments:
superclass
T@\"NSString\",?,R,C
initWithFormat:
T@\"NSUUID\",R,N,V_handle
Tq,R,N,V_state
_OS_xpcObjectRepresentation
environmentVariables
setObject:forKeyedSubscript:
TQ,R,N,V_os_reason_flags
Ti,R,N,V_lastSpawnError
_startMonitoringAfterSubmit:
domainForPid:
enablePressuredExit
_managedEndpointLaunchIdentifiers
_roleAccount
enterprisePersona
handle
initWithLabel:instance:requestedJetsamPriority:additionalProperties:program:processType:keepAlive:runAtLoad:enableTransactions:endpoints:serviceType:path:xpcBundle:hostPID:
initWithType:handle:
setManagedByServices:
submit:
_initWithHandle:
domainForUser:
keepAlive
processType
submitAndStart:
instance
managedEndpointLaunchIdentifiers
monitorOnQueue:withHandler:
setUiApplicationDelegateClass:
uiApplicationClass
setRoleAccount:
setRunLoopType:
_joinExistingSession
disableLogging_4watchdogd
T@\"NSDictionary\",C,N,V_environmentVariables
allocWithZone:
conformsToProtocol:
numberWithInt:
pid
_getPlist
class
managedByServices
sandboxContainer
setSandboxProfile:
T@\"NSObject<OS_xpc_object>\",R,N,V_additionalProperties
_undefinedBehaviorSanitizer
errorWithDomain:code:userInfo:
getUUIDBytes:
lastExitStatus
platform
setConclave:
_spawnConstraint
fileSystemRepresentation
longLongValue
setDeveloperToolsOptions:
copyJobsManagedBy:error:
decodeBoolForKey:
TB,R,N,V_removing
UTF8String
_enableTransactions
_path
os_reason_namespace
program
_developerToolsOptions
objCType
T@\"NSString\",C,N,V_uiApplicationClass
T@\"OSLaunchdJobExitStatus\",R,N,V_lastExitStatus
v16@0:8
@20@0:8i16
@44@0:8I16@20Q28^@36
@68@0:8q16i24i28@32@40B48@52@60
B24@0:8@16
@24@0:8^@16
@40@0:8i16I20Q24Q32
@\"NSData\"
@32@0:8@16^@24
B16@0:8
@32@0:8[16C]16@24
@\"NSArray\"
v32@0:8@16@?24
@24@0:8@16
i
v20@0:8B16
@24@0:8^{_NSZone=}16
@100@0:8@16@24i32@36@44I52B56B60B64@68q76@84B92i96
I
Vv16@0:8
@\"OSLaunchdJobExitStatus\"
@16@0:8
@\"NSObject<OS_xpc_object>\"
q
@24@0:8:16
i20@0:8i16
@32@0:8[16C]16^@24
@\"NSObject<OS_dispatch_source>\"
v20@0:8I16
I16@0:8
q24@0:8@16
@48@0:8@16@24@32^@40
@\"OSLaunchdDomain\"
#16@0:8
@\"NSString\"16@0:8
@\"NSObject<OS_dispatch_queue>\"
q16@0:8
@40@0:8:16@24@32
B24@0:8^@16
v40@0:8@16@?24@32
@20@0:8I16
@\"NSURL\"
v24@0:8@\"NSCoder\"16
@56@0:8r*16@24@32@40^@48
v36@0:8I16@20@?28
Q
B
B24@0:8:16
Q16@0:8
B24@0:8#16
^{_NSZone=}16@0:8
@\"NSObject<OS_xpc_object>\"16@0:8
v24@0:8@16
@48@0:8r*16@24@32@40
@32@0:8Q16^@24
@24@0:8@\"NSCoder\"16
@\"NSString\"
@32@0:8:16@24
B32@0:8@16^@24
@32@0:8@16@24
I24@0:8Q16
@\"NSUUID\"
@\"NSDictionary\"
@\"OSLaunchdDeveloperToolsOptions\"
@\"NSSet\"
i16@0:8
@40@0:8[16C]16@24^@32
@?
B24@0:8@\"Protocol\"16
@28@0:8i16Q20
@28@0:8i16^@20
<unknown>
spawn-error
no-einprogress
_MultipleInstances
_LaunchWatchdogTimeOut
path
sandbox-profile
developer-tools
running
exited, %@
_UIApplicationClass
DeveloperTools
CFBundlePackageType
label
instance
SanitizerFlags
undefinedBehaviorSanitizer
i
_AdditionalProperties
_LightweightCodeRequirement
OSLaunchdErrorDomain
run-at-load
XPCExtensionXPCBundle
pid
os-reason-code
PersonaEnterprise
Label
plist
XPCServiceEndpoints
os-code
handle
handles
threadSanitizer
_UIApplicationDelegateClass
process-type
os-namespace
monitor
type
error
 (EINPROGRESS)
sandbox-container
client-port
client-reply-port
<%@: %p> XPC overlay:\n %@
jp-priority
XPCExtensionHostPID
v8@?0
job-state
manager
spawn failed, error=%d: %s
_SandboxProfile
_OmitSandboxParameters
attrs
<OSLaunchdDomain type %d, handle %qu>
exit reason namespace=%u code=%llu
wait4() status=%d
ProgramArguments
EnvironmentVariables
_Conclave
XPC!
spawn-constraint
session
flags
addressSanitizer
_AdditionalSubServices
_ProcessType
envvars
wait4-status
%s
ServiceType
Platform
SpawnConstraint
XPCService
keep-alive
removing
%s, pid=%d
com.apple.libxpc.OSLaunchdJob
os-reason-ns
name
service-type
job-handle
_AbandonCoalition
additional-properties
com.apple.libxpc.AppServerSupport
all
os-reason-flags
properties
<%@> addressSanitizer=%d threadSanitizer=%d mtAddressSanitizer=%d undefinedBehaviorSanitizer=%d
RunLoopType
never ran
mtAddressSanitizer
JoinExistingSession
_RoleAccount
_SandboxContainer
enable-transactions
termination-state
instance-uuid
<%@ | handle=%@>
overlay
coalition-id
4
_ManagedBy_Services
program
all-jobs
results
assertion failure: \"_handle == ((void *)0)\" -> %llu
%{public}@: job failed to spawn, plist=%{public}s
monitoring will start once the job is submitted
assertion failure: \"wait4Status != ((void *)0)\" -> %llu
copyJobWithPid:%d failed with error %d: %s
assertion failure: \"job != ((void *)0)\" -> %llu
%{public}@: submitAndStart completed, info=%{public}@
submit failed with error %d: %s
unexpected state after START: %d
%{public}@: error creating monitor %d: %s
assertion failure: \"[[job handle] isEqual:handle]\" -> %llu
%{public}@: copyJobWithHandle: created a job
%{public}@: start failed with error %d: %s
assertion failure: \"(((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu
copyJobsLoadedByCoalition failed with error %d: %s
assertion failure: \"job.handle != ((void *)0)\" -> %llu
submit (%@) with label %s failed with error %d: %s
assertion failure: \"xpc_get_type(plist) == (&_xpc_type_dictionary)\" -> %llu
assertion failure: \"handle != ((void *)0)\" -> %llu
%{public}@: copyJobWithLabel for label %{public}@ created a job
assertion failure: \"os_reason_namespace != ((void *)0)\" -> %llu
unexpected state after SUBMIT_AND_START: %d
assertion failure: \"handler != ((void *)0)\" -> %llu
unexpected state %d
copyJobsManagedBy failed with error %d: %s
assertion failure: \"domain != ((void *)0)\" -> %llu
copyJobsLoadedByJob failed with error %d: %s
%{public}@: submitExtension created a job
%{public}@: copyJobWithPid:%d created a job
%{public}@: remove on a job with no handle (ESRCH)
assertion failure: \"_plist != ((void *)0)\" -> %llu
%{public}@: remove succeeded%s
%{public}@ monitor: failed to re-arm monitor poll, error %d: %s
assertion failure: \"pid == 0\" -> %llu
%{public}@: start succeeded, info=%{public}@
assertion failure: \"plist != ((void *)0)\" -> %llu
assertion failure: \"os_reason_flags != ((void *)0)\" -> %llu
assertion failure: \"kr\" -> %llu
assertion failure: \"xpc_array_get_count(results) == jobs.count\" -> %llu
%{public}@: remove failed with error %d %s
%{public}@: createInstance on a job with no handle (ESRCH)
%{public}@: createInstance failed with error %d: %s
%{public}@ monitor: got an update with info %{public}@
copyJobWithHandle:%{public}@ failed with error %d: %s
assertion failure: \"bundleExecutable != ((void *)0)\" -> %llu
submitExtension failed with error %d: %s
assertion failure: \"label != ((void*)0)\" -> %llu
assertion failure: \"_monitor_handler != ((void *)0)\" -> %llu
%{public}@: starting monitoring
assertion failure: \"handle\" -> %llu
copyJobWithLabel for label %{public}@ failed with error %d: %s
assertion failure: \"status == ((void *)0)\" -> %llu
assertion failure: \"program != ((void*)0)\" -> %llu
assertion failure: \"monitor_port != 0\" -> %llu
assertion failure: \"manager != ((void *)0)\" -> %llu
assertion failure: \"xhandle != ((void*)0)\" -> %llu
assertion failure: \"_monitor_handler == ((void *)0)\" -> %llu
%{public}@: createInstance created a job %{public}@
assertion failure: \"pid != 0\" -> %llu
assertion failure: \"error != 0\" -> %llu
unable to get attrs for pid %d: %s
assertion failure: \"_domain != ((void *)0)\" -> %llu
submitAndStart failed with error %d: %s
%{public}@: monitor initial info is %{public}@
assertion failure: \"os_reason_code != ((void *)0)\" -> %llu
%{public}@ monitor: got error %d: %s
assertion failure: \"pid > 0\" -> %llu
assertion failure: \"error == 0\" -> %llu
unable to get attrs for job %@: %s
assertion failure: \"handles != ((void *)0)\" -> %llu
assertion failure: \"_monitor_source == ((void *)0)\" -> %llu
assertion failure: \"status != ((void *)0)\" -> %llu
```
