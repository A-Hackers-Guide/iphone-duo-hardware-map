# `/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 142,304 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3736)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (3 classes, 2 protocols)

Classes: `OSASubmissionClient`, `OSASubmissionClientOptions`, `OSASubmissionScheduler`

Protocols: `NSObject`, `OSASubmissionServices`

## Strings (204)

```
result
com.apple.osanalytics.osanalyticshelper
YES
action
checkEntitlement
urgent
submit
NO
com.apple.osanalytics.submissions.schedulerQueue
retryCount
crk
com.apple.OSASubmission.client
event
permissive
@\"NSDictionary\"8@?0
cleanup
v16@?0@\"NSError\"8
success
dre_overrideMountPath
com.apple.osanalytics.submissions.submit-permissive
com.apple.osanalytics.submissions.scheduler
v8@?0
v16@?0@\"NSObject<OS_xpc_object>\"8
manual
containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist
operation
type
com.apple.osanalytics.submissions.cleanup
/private/var/mnt
lastSuccess
com.apple.osanalytics.submissions.submit
unified
mode
client
v16@?0@\"NSDictionary\"8
v12@?0B8
Failed to override mount path for log-writing service
Failed to rollover CoreAnalytics log
Submission failed
Successfully overrode mount path for log-writing service
Connection error to %s: %s
Successful CoreAnalytics log rollover
Initializing submission activity cadence. Permissive: %{public}s. FastLane: %{public}s.
Scheduling submission. Permissive: %{public}s. FastLane: %{public}s.
Scheduling cleanup.
Submission cadences were unchanged for activity %{public}@. Keeping current cadences parameters %{public}@
Connection error to %@. Error: %@
Submission results: %@
Failed to override mount path locally
Failed to establish connection to %s
Successful sync with ReportCrash
Failed to sync with ReportCrash: %@
Cancelling permissive submission due to recent success at %{public}@ with interval %{public}lli.
Maxed out on retries. Resetting retry count
Error issuing sandbox extension to %@: %i (%s)
Failed to override mount path for submission service
Unexpected reply from %s
Successful submission
Did not receive reply from %s
Connection initiated
Issued sandbox extension to %@
Failed to issue all necessary sandbox extensions
Successfully overrode mount path for submission service
OSASubmissionClient
OSADRESubmissionClient
OSASubmissionScheduler
OSASubmissionClientOptions
OSASubmissionServices
NSObject
numberWithBool:
conformsToProtocol:
invalidate
submitDRETelemetryAndDiagnostics:
autorelease
countByEnumeratingWithState:objects:count:
isKindOfClass:
isMemberOfClass:
pathContainerRoot
self
TB,V_urgentSubmission
_synchRemoteObjectProxy
interfaceWithProtocol:
isEqual:
mutableCopy
_retryCount
addEntriesFromDictionary:
fetchMainConfigFileWithOverrrides:withReply:
performSelector:
setRemoteObjectInterface:
updateConfigFile
cleanupForUser:
canSubmitLogOfType:withReply:
cleanupWithHomeDirectoryLocation:
dateWithTimeIntervalSinceReferenceDate:
dictionaryWithObjects:forKeys:count:
fetchTypeBlackListWithReply:
initWithMachServiceName:options:
recordEvent:
_getCurrentCadenceParametersFromActivity:
addObject:
encodeObject:forKey:
fastLane
finishEncoding
hash
isEqualToDictionary:
scheduleCleanupForUser:
release
stringByAppendingPathComponent:
_urgentSubmission
performSelector:withObject:
resume
sharedInstance
zone
_calculateNewCadenceParametersWithPermissive:fastLane:
arrayWithObjects:count:
retain
scheduleSubmission
setDouble:forKey:
setInteger:forKey:
setUrgentSubmission:
submitWithOptions:resultsCallback:
TQ,R
dealloc
count
pathRoot
setObject:forKeyedSubscript:
submitWithOptions:
synchronousRemoteObjectProxyWithErrorHandler:
_incrementRetryCount
_updateCadenceForActivity:newCadenceParameters:
debugDescription
overrideMountPath
retainCount
standardUserDefaults
submissionOptionsFromClientOptions:
.cxx_destruct
_lastSuccessTime
cleanupWithHomeDirectoryLocation:options:
overrideSubmissionServiceMountPath:withReply:
submit
superclass
timeIntervalSinceReferenceDate
urgentSubmission
T@\"NSString\",R,C
_scheduleSubmissionWithPermissive:
_resetRetryCount
_saveLastSuccessTime
class
description
init
initWithErrorHandler:
localizedDescription
respondsToSelector:
isProxy
T@\"NSString\",?,R,C
_connection
crashReporterKey
longLongValue
numberWithLongLong:
objectForKeyedSubscript:
performSelector:withObject:withObject:
integerForKey:
beginEncoding
doubleForKey:
stringWithUTF8String:
initWithSandboxExtensions:
T#,R
boolValue
v24@0:8@\"NSString\"16
B24@0:8@\"Protocol\"16
v16@0:8
v32@0:8@\"NSString\"16@?<v@?B>24
v24@0:8@?<v@?@\"NSSet\">16
v32@0:8@\"OverrideMountPathRequest\"16@?<v@?B>24
@24@0:8@16
q16@0:8
v32@0:8@16@?24
v32@0:8@16@24
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\">24
@\"<OSASubmissionServices>\"
B24@0:8#16
B24@0:8:16
@\"NSString\"16@0:8
d16@0:8
B
@24@0:8:16
Q16@0:8
@16@0:8
v24@0:8@16
v32@0:8@\"NSString\"16@\"NSDictionary\"24
@24@0:8@?16
B16@0:8
v20@0:8B16
^{_NSZone=}16@0:8
B20@0:8B16
#16@0:8
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24
@\"NSXPCConnection\"
@24@0:8B16B20
B24@0:8@16
@32@0:8:16@24
@40@0:8:16@24@32
Vv16@0:8
v24@0:8@?16
```
