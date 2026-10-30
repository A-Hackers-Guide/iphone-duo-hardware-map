# `/System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient`

From the upgrade restore ramdisk (141-29011-104.dmg). 142,304 bytes.

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
com.apple.osanalytics.osanalyticshelper
com.apple.osanalytics.submissions.submit
com.apple.osanalytics.submissions.schedulerQueue
v16@?0@\"NSObject<OS_xpc_object>\"8
client
containers/Shared/SystemGroup/systemgroup.com.apple.configurationprofiles/Library/ConfigurationProfiles/UserSettings.plist
permissive
success
v12@?0B8
dre_overrideMountPath
result
com.apple.osanalytics.submissions.submit-permissive
YES
action
mode
checkEntitlement
NO
@\"NSDictionary\"8@?0
lastSuccess
v8@?0
type
com.apple.OSASubmission.client
v16@?0@\"NSError\"8
manual
urgent
/private/var/mnt
com.apple.osanalytics.submissions.scheduler
unified
submit
retryCount
cleanup
operation
crk
com.apple.osanalytics.submissions.cleanup
event
v16@?0@\"NSDictionary\"8
Successful sync with ReportCrash
Scheduling submission. Permissive: %{public}s. FastLane: %{public}s.
Scheduling cleanup.
Failed to override mount path locally
Failed to issue all necessary sandbox extensions
Successfully overrode mount path for submission service
Successfully overrode mount path for log-writing service
Connection error to %s: %s
Cancelling permissive submission due to recent success at %{public}@ with interval %{public}lli.
Maxed out on retries. Resetting retry count
Submission results: %@
Failed to override mount path for submission service
Failed to override mount path for log-writing service
Unexpected reply from %s
Failed to rollover CoreAnalytics log
Failed to sync with ReportCrash: %@
Successful submission
Initializing submission activity cadence. Permissive: %{public}s. FastLane: %{public}s.
Connection initiated
Did not receive reply from %s
Submission failed
Submission cadences were unchanged for activity %{public}@. Keeping current cadences parameters %{public}@
Connection error to %@. Error: %@
Issued sandbox extension to %@
Error issuing sandbox extension to %@: %i (%s)
Failed to establish connection to %s
Successful CoreAnalytics log rollover
OSASubmissionScheduler
OSASubmissionClientOptions
OSASubmissionServices
NSObject
OSASubmissionClient
OSADRESubmissionClient
_connection
setUrgentSubmission:
updateConfigFile
urgentSubmission
T@\"NSString\",R,C
release
TQ,R
description
isKindOfClass:
localizedDescription
numberWithLongLong:
self
boolValue
initWithErrorHandler:
isMemberOfClass:
overrideMountPath
performSelector:withObject:
resume
setDouble:forKey:
setRemoteObjectInterface:
_calculateNewCadenceParametersWithPermissive:fastLane:
cleanupForUser:
T@\"NSString\",?,R,C
addObject:
respondsToSelector:
scheduleCleanupForUser:
submit
beginEncoding
doubleForKey:
fastLane
overrideSubmissionServiceMountPath:withReply:
standardUserDefaults
dealloc
_retryCount
_synchRemoteObjectProxy
debugDescription
longLongValue
sharedInstance
encodeObject:forKey:
arrayWithObjects:count:
autorelease
isProxy
_incrementRetryCount
_resetRetryCount
_scheduleSubmissionWithPermissive:
_urgentSubmission
_saveLastSuccessTime
submitDRETelemetryAndDiagnostics:
timeIntervalSinceReferenceDate
countByEnumeratingWithState:objects:count:
dictionaryWithObjects:forKeys:count:
initWithMachServiceName:options:
performSelector:withObject:withObject:
setInteger:forKey:
submitWithOptions:resultsCallback:
zone
_lastSuccessTime
conformsToProtocol:
objectForKeyedSubscript:
pathRoot
performSelector:
scheduleSubmission
stringWithUTF8String:
submissionOptionsFromClientOptions:
.cxx_destruct
_updateCadenceForActivity:newCadenceParameters:
fetchTypeBlackListWithReply:
hash
retainCount
submitWithOptions:
stringByAppendingPathComponent:
class
isEqualToDictionary:
mutableCopy
addEntriesFromDictionary:
canSubmitLogOfType:withReply:
setObject:forKeyedSubscript:
synchronousRemoteObjectProxyWithErrorHandler:
T#,R
init
interfaceWithProtocol:
pathContainerRoot
superclass
fetchMainConfigFileWithOverrrides:withReply:
initWithSandboxExtensions:
integerForKey:
numberWithBool:
_getCurrentCadenceParametersFromActivity:
count
isEqual:
retain
finishEncoding
invalidate
TB,V_urgentSubmission
cleanupWithHomeDirectoryLocation:
cleanupWithHomeDirectoryLocation:options:
crashReporterKey
dateWithTimeIntervalSinceReferenceDate:
recordEvent:
@32@0:8:16@24
@40@0:8:16@24@32
Vv16@0:8
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSData\">24
B24@0:8@16
@24@0:8:16
v16@0:8
v24@0:8@\"NSString\"16
q16@0:8
@\"NSString\"16@0:8
v32@0:8@16@24
@\"NSXPCConnection\"
B20@0:8B16
d16@0:8
Q16@0:8
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24
v32@0:8@\"NSString\"16@?<v@?B>24
@24@0:8@16
@24@0:8B16B20
B24@0:8:16
B24@0:8@\"Protocol\"16
v24@0:8@16
v24@0:8@?16
v24@0:8@?<v@?@\"NSSet\">16
@24@0:8@?16
v32@0:8@\"NSString\"16@\"NSDictionary\"24
v32@0:8@\"OverrideMountPathRequest\"16@?<v@?B>24
B16@0:8
v20@0:8B16
@16@0:8
^{_NSZone=}16@0:8
@\"<OSASubmissionServices>\"
B
B24@0:8#16
#16@0:8
v32@0:8@16@?24
```
