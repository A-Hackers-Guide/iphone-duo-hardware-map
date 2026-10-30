# `/System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 207,376 bytes.

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
LASSProperties4RB
OSLaunchdJobExitStatus
OSLaunchdJobInfo
OSLaunchdJobInstanceProperties
NSCoding
_OSXPCObjectRepresentable
OSLaunchdDomain
OSLaunchdError
NSCopying
OSLaunchdJob
OSLaunchdDeveloperToolsOptions
NSSecureCoding
AppServiceSupportAdditions
NSObject
OSLaunchdJobProperties
fileSystemRepresentation
submitExtensionAtURL:properties:domain:error:
T@\"NSDictionary\",C,N,V_additionalProperties
_personaString
_propertiesFromAttrs:
_removing
copyJobsManagedBy:error:
class
currentDomain
T#,R
initWithFormat:
T@\"NSString\",C,N,V_roleAccount
_developerToolsOptions
_joinExistingSession
setDeveloperToolsOptions:
T@\"NSString\",C,N,V_conclave
TB,R,N,V_runAtLoad
Ti,R,N,V_wait4Status
_plist
_state
label
mtAddressSanitizer
setEnterprisePersona:
init
_createSubmitExtensionRequest:overlay:domain:properties:
T@\"NSString\",C,N,V_runLoopType
TI,R,N,V_processType
_additionalSubServices
_initWithHandle:
_sandboxContainer
lastSpawnError
endpoints
_conclave
remove:
spawnConstraint
submitAndStart:
_enablePressuredExit
additionalProperties
encodeBool:forKey:
threadSanitizer
_lastExitStatus
_runLoopType
additionalPropertiesDictionary
autorelease
initWithLabel:instance:requestedJetsamPriority:additionalProperties:program:processType:keepAlive:runAtLoad:enableTransactions:endpoints:serviceType:path:xpcBundle:hostPID:
monitorOnQueue:withHandler:
setServiceType:
_OS_xpcObjectRepresentation
_environmentVariables
_pid
_xpcBundle
setOmitSandboxParameters:
submitExtension:overlay:domain:error:
oneShotUUID
runLoopType
T@\"NSObject<OS_xpc_object>\",R,N,V_additionalProperties
submit:
copyJobsLoadedByJob:
setManagedByServices:
setSandboxProfile:
setUndefinedBehaviorSanitizer:
state
stringWithFormat:
initWithType:handle:
respondsToSelector:
setSandboxContainer:
systemDomain
os_reason_flags
numberWithBool:
TB,N,V_joinExistingSession
_endpoints
developerToolsOptions
setSpawnConstraint:
T@\"NSString\",C,N,V_processType
_path
dictionaryWithObjects:forKeys:count:
xpcOverlay
Ti,R,N,V_requestedJetsamPriority
_hostPID
createInstance:error:
setJoinExistingSession:
setWatchdogTimeout:
program
domainForRoleAccountUser:
numberWithUnsignedInt:
os_reason_namespace
processSubmitReply:
watchdogTimeout
TB,N,V_abandonCoalition
_oneShotUUID
_type
cancelMonitor
_handlesToJobs:
copyJobWithHandle:
T@\"NSObject<OS_xpc_object>\",R,N,V_endpoints
keepAlive
propertiesForPid:error:
setValue:forKey:
_newSubmitRequest
_programArguments
addressSanitizer
isMemberOfClass:
T@\"NSData\",C,N,V_lightweightCodeRequirement
arrayWithCapacity:
length
processType
sandboxContainer
_serviceType
_uiApplicationClass
isKindOfClass:
sandboxProfile
T@\"NSSet\",C,N,V_managedEndpointLaunchIdentifiers
_keepAlive
_newCreateInstanceRequest:properties:
_processType
_uiApplicationDelegateClass
copy
setArguments:
T@\"NSArray\",C,N,V_managedByServices
_getPlist
_program
countByEnumeratingWithState:objects:count:
decodeBoolForKey:
os_reason_code
platform
isProxy
T@\"NSString\",R,C,N,V_program
T@\"NSDictionary\",C,N,V_environmentVariables
_lightweightCodeRequirement
lightweightCodeRequirement
setLabel:
T@\"NSString\",R,C
TB,R,N,V_removing
Ti,R,N,V_pid
UTF8String
abandonCoalition
domainForUser:
TB,R,N,V_keepAlive
addObject:
additionalSubServices
initWithPlist:domain:
lastExitStatus
_sandboxProfile
Tq,R,N,V_state
enablePressuredExit
retainCount
uiApplicationClass
domainForBackgroundUser:
encodeWithCoder:
hash
self
supportsSecureCoding
zone
setProcessType:
_createJobFromReplyHandle:
_omitSandboxParameters
_roleAccount
getCurrentJobInfo
setupMonitorOnQueue:withHandler:reply:
valueForKey:
wait4Status
hostPID
TB,R
Ti,R,N,V_hostPID
_overlay
_setupMonitorSourceWithPort:onQueue:withHandler:
setThreadSanitizer:
numberWithUnsignedLong:
xpcBundle
T@\"NSString\",C,N,V_uiApplicationDelegateClass
.cxx_destruct
setRunLoopType:
_additionalProperties
_platform
_watchdogTimeout
T@\"NSString\",C,N,V_personaString
TQ,R,N,V_os_reason_code
_wait4Status
copyJobsLoadedByCoalition:error:
_os_reason_code
T@\"OSLaunchdJobExitStatus\",R,N,V_lastExitStatus
_spawnConstraint
initWithState:pid:lastSpawnError:lastExitStatus:additionalPropertiesDict:removing:instance:program:
loginwindowDomain
setAdditionalProperties:
superclass
copyJobWithPid:
TB,R,N,V_enableTransactions
Tq,R,N,V_serviceType
_submitExtension:overlay:domain:properties:error:
environmentVariables
T@\"NSString\",C,N,V_serviceType
_createDomainOptions2flags:
objectForKeyedSubscript:
enableTransactions
_addressSanitizer
setRoleAccount:
TQ,R,N,V_os_reason_flags
initWithWait4Status:os_reason_namespace:os_reason_code:os_reason_flags:
numberWithUnsignedChar:
T@\"NSString\",C,N,V_sandboxProfile
TQ,R
longLongValue
T@\"NSString\",R,N,V_program
TB,N,V_omitSandboxParameters
TI,R,N,V_os_reason_namespace
_startMonitoringAfterSubmit:
isEqual:
setEnvironmentVariables:
setLightweightCodeRequirement:
T@\"NSURL\",&,N,V_sandboxContainer
TB,N,V_undefinedBehaviorSanitizer
_os_reason_namespace
copyWithZone:
initWithUUIDBytes:
setObject:forKeyedSubscript:
type
T@\"NSDictionary\",C,N,V_arguments
T@\"OSLaunchdDeveloperToolsOptions\",C,N,V_developerToolsOptions
TI,N,V_enterprisePersona
_managedEndpointLaunchIdentifiers
_mtAddressSanitizer
domainForAsid:
jobStateFromMessage:
setAddressSanitizer:
_monitorNormalizeError:
_requestedJetsamPriority
setConclave:
_additionalPropertiesDictionary
arguments
objCType
setMtAddressSanitizer:
stringWithUTF8String:
T@\"NSDictionary\",C,N,V_spawnConstraint
T@\"NSString\",R,N,V_label
TB,R,N,V_xpcBundle
boolValue
omitSandboxParameters
TB,N,V_threadSanitizer
T@\"NSArray\",C,N,V_programArguments
T@\"NSURL\",C,N,V_sandboxContainer
T@\"NSUUID\",&,N,V_oneShotUUID
TB,N,V_mtAddressSanitizer
_managedByServices
errorWithDomain:code:userInfo:
initiateRemoval:
programArguments
_lastSpawnError
release
TB,N
_arguments
_enterprisePersona
disableLogging_4watchdogd
managedEndpointLaunchIdentifiers
numberWithInt:
T@\"NSDictionary\",C,N,V_additionalSubServices
objectAtIndexedSubscript:
performSelector:withObject:withObject:
propertiesForJob:error:
roleAccount
T@\"NSString\",?,R,C
T@\"NSString\",C,N,V_uiApplicationClass
_abandonCoalition
_os_reason_flags
_undefinedBehaviorSanitizer
copyJobWithLabel:domain:
initWithPlist:
submitAll:error:
_domain
jobInfoFromMessage:
setPersonaString:
setProgramArguments:
TI,N,V_platform
TB,N,V_watchdogTimeout
enterprisePersona
T@\"NSDictionary\",C,N,V_overlay
setOneShotUUID:
_monitor_handler
_threadSanitizer
getUUIDBytes:
setDisableLogging_4watchdogd:
uiApplicationDelegateClass
_monitor_source
T@\"NSUUID\",R,N,V_handle
TB,N,V_addressSanitizer
debugDescription
joinExistingSession
Ti,R,N,V_lastSpawnError
_OS_overlayDictionary:
T@\"NSObject<OS_xpc_object>\",R,N,V_additionalPropertiesDictionary
unpendLaunches:
_runAtLoad
allocWithZone:
conformsToProtocol:
T@\"NSString\",C,N,V_label
managedByServices
setAdditionalSubServices:
setUiApplicationDelegateClass:
toDictionary
createInstance:properties:error:
runAtLoad
setAbandonCoalition:
setUiApplicationClass:
pid
overlay
TB,R,N,V_enablePressuredExit
conclave
initWithCoder:
_handle
T@\"NSUUID\",R,N,V_instance
_monitor_queue
bytes
count
_instance
domainForPid:
path
retain
setOverlay:
start:
_newRequest
createDomainForRoleAccount:sessionType:options:error:
instance
serviceType
setPlatform:
createXPCError:
_enableTransactions
_label
handle
requestedJetsamPriority
setManagedEndpointLaunchIdentifiers:
_populateHandle:
description
performSelector:withObject:
personaString
removing
T@\"NSString\",R,N,V_path
performSelector:
undefinedBehaviorSanitizer
i20@0:8i16
@20@0:8i16
v36@0:8I16@20@?28
B24@0:8@16
@24@0:8:16
@\"NSObject<OS_dispatch_source>\"
I
q
^{_NSZone=}16@0:8
@\"OSLaunchdJobExitStatus\"
@\"NSUUID\"
@32@0:8[16C]16@24
I16@0:8
@32@0:8:16@24
B24@0:8:16
@48@0:8r*16@24@32@40
@32@0:8Q16^@24
@24@0:8@\"NSCoder\"16
B
@24@0:8^@16
@\"NSSet\"
i
v40@0:8@16@?24@32
I24@0:8Q16
v24@0:8@\"NSCoder\"16
@32@0:8[16C]16^@24
@\"NSObject<OS_dispatch_queue>\"
@44@0:8I16@20Q28^@36
B16@0:8
q16@0:8
v20@0:8B16
@\"OSLaunchdDeveloperToolsOptions\"
q24@0:8@16
@56@0:8r*16@24@32@40^@48
@\"NSObject<OS_xpc_object>\"16@0:8
B32@0:8@16^@24
@48@0:8@16@24@32^@40
@40@0:8:16@24@32
Q16@0:8
@\"NSString\"16@0:8
B24@0:8^@16
@40@0:8[16C]16@24^@32
@\"OSLaunchdDomain\"
@\"NSURL\"
@\"NSDictionary\"
Vv16@0:8
@\"NSString\"
@16@0:8
i16@0:8
v32@0:8@16@?24
@?
Q
#16@0:8
B24@0:8@\"Protocol\"16
@28@0:8i16Q20
@24@0:8^{_NSZone=}16
@32@0:8@16^@24
v24@0:8@16
@20@0:8I16
@40@0:8i16I20Q24Q32
v20@0:8I16
@\"NSArray\"
@24@0:8@16
@\"NSData\"
B24@0:8#16
@28@0:8i16^@20
@100@0:8@16@24i32@36@44I52B56B60B64@68q76@84B92i96
v16@0:8
@32@0:8@16@24
@68@0:8q16i24i28@32@40B48@52@60
@\"NSObject<OS_xpc_object>\"
EnvironmentVariables
DeveloperTools
monitor
overlay
<%@> addressSanitizer=%d threadSanitizer=%d mtAddressSanitizer=%d undefinedBehaviorSanitizer=%d
_LaunchWatchdogTimeOut
XPCService
OSLaunchdErrorDomain
v8@?0
all
os-namespace
name
results
no-einprogress
running
_MultipleInstances
all-jobs
sandbox-container
coalition-id
_ManagedBy_Services
_OmitSandboxParameters
_AdditionalProperties
_AdditionalSubServices
enable-transactions
job-handle
spawn-constraint
client-reply-port
%s, pid=%d
RunLoopType
_AbandonCoalition
_Conclave
instance
program
XPCServiceEndpoints
type
properties
i
CFBundlePackageType
handles
<unknown>
 (EINPROGRESS)
sandbox-profile
addressSanitizer
_LightweightCodeRequirement
_SandboxContainer
keep-alive
envvars
ProgramArguments
_SandboxProfile
com.apple.libxpc.OSLaunchdJob
XPCExtensionXPCBundle
plist
os-reason-flags
%s
client-port
exited, %@
Platform
XPC!
termination-state
spawn-error
os-reason-code
<OSLaunchdDomain type %d, handle %qu>
mtAddressSanitizer
service-type
handle
threadSanitizer
ServiceType
pid
session
flags
_UIApplicationClass
run-at-load
removing
<%@ | handle=%@>
_RoleAccount
_ProcessType
os-reason-ns
label
XPCExtensionHostPID
os-code
Label
spawn failed, error=%d: %s
<%@: %p> XPC overlay:\n %@
JoinExistingSession
jp-priority
process-type
job-state
never ran
SanitizerFlags
PersonaEnterprise
SpawnConstraint
additional-properties
path
attrs
error
instance-uuid
developer-tools
wait4-status
manager
com.apple.libxpc.AppServerSupport
exit reason namespace=%u code=%llu
wait4() status=%d
4
undefinedBehaviorSanitizer
_UIApplicationDelegateClass
unable to get attrs for job %@: %s
copyJobsLoadedByJob failed with error %d: %s
copyJobsManagedBy failed with error %d: %s
assertion failure: \"handle\" -> %llu
unexpected state after SUBMIT_AND_START: %d
%{public}@: remove on a job with no handle (ESRCH)
assertion failure: \"wait4Status != ((void *)0)\" -> %llu
assertion failure: \"kr\" -> %llu
%{public}@: copyJobWithHandle: created a job
%{public}@: start failed with error %d: %s
monitoring will start once the job is submitted
%{public}@: createInstance created a job %{public}@
assertion failure: \"handle != ((void *)0)\" -> %llu
assertion failure: \"program != ((void*)0)\" -> %llu
assertion failure: \"_domain != ((void *)0)\" -> %llu
assertion failure: \"_monitor_handler == ((void *)0)\" -> %llu
assertion failure: \"os_reason_flags != ((void *)0)\" -> %llu
%{public}@ monitor: got an update with info %{public}@
assertion failure: \"pid > 0\" -> %llu
copyJobWithPid:%d failed with error %d: %s
%{public}@: copyJobWithPid:%d created a job
assertion failure: \"job.handle != ((void *)0)\" -> %llu
assertion failure: \"handler != ((void *)0)\" -> %llu
%{public}@: createInstance failed with error %d: %s
%{public}@ monitor: failed to re-arm monitor poll, error %d: %s
submitAndStart failed with error %d: %s
submit (%@) with label %s failed with error %d: %s
assertion failure: \"pid != 0\" -> %llu
assertion failure: \"job != ((void *)0)\" -> %llu
assertion failure: \"_handle == ((void *)0)\" -> %llu
assertion failure: \"handles != ((void *)0)\" -> %llu
%{public}@: submitAndStart completed, info=%{public}@
%{public}@: start succeeded, info=%{public}@
assertion failure: \"_monitor_source == ((void *)0)\" -> %llu
%{public}@: createInstance on a job with no handle (ESRCH)
%{public}@: submitExtension created a job
%{public}@: job failed to spawn, plist=%{public}s
unexpected state after START: %d
%{public}@: copyJobWithLabel for label %{public}@ created a job
assertion failure: \"label != ((void*)0)\" -> %llu
copyJobWithLabel for label %{public}@ failed with error %d: %s
assertion failure: \"pid == 0\" -> %llu
assertion failure: \"error != 0\" -> %llu
assertion failure: \"xhandle != ((void*)0)\" -> %llu
%{public}@: remove failed with error %d %s
%{public}@: monitor initial info is %{public}@
copyJobsLoadedByCoalition failed with error %d: %s
assertion failure: \"status == ((void *)0)\" -> %llu
%{public}@ monitor: got error %d: %s
assertion failure: \"manager != ((void *)0)\" -> %llu
unexpected state %d
assertion failure: \"os_reason_code != ((void *)0)\" -> %llu
%{public}@: starting monitoring
assertion failure: \"(((reply_port) != 0) && ((reply_port) != ((mach_port_name_t) ~0)))\" -> %llu
assertion failure: \"bundleExecutable != ((void *)0)\" -> %llu
submitExtension failed with error %d: %s
unable to get attrs for pid %d: %s
assertion failure: \"xpc_array_get_count(results) == jobs.count\" -> %llu
%{public}@: error creating monitor %d: %s
%{public}@: remove succeeded%s
assertion failure: \"os_reason_namespace != ((void *)0)\" -> %llu
assertion failure: \"error == 0\" -> %llu
assertion failure: \"_plist != ((void *)0)\" -> %llu
assertion failure: \"xpc_get_type(plist) == (&_xpc_type_dictionary)\" -> %llu
assertion failure: \"status != ((void *)0)\" -> %llu
assertion failure: \"plist != ((void *)0)\" -> %llu
assertion failure: \"monitor_port != 0\" -> %llu
copyJobWithHandle:%{public}@ failed with error %d: %s
assertion failure: \"domain != ((void *)0)\" -> %llu
assertion failure: \"_monitor_handler != ((void *)0)\" -> %llu
submit failed with error %d: %s
assertion failure: \"[[job handle] isEqual:handle]\" -> %llu
```
