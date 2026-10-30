# `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 438,576 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 42 (Size: 5816)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (24)

- `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/IDS.framework/IDS (compatibility version 1.0.0, current version 800.0.0, weak)`
- `/System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Trial.framework/Trial (compatibility version 1.0.0, current version 511.1.2, weak)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC (compatibility version 1.0.0, current version 3298.52.1, weak)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9, weak)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation (compatibility version 1.0.0, current version 800.0.0, weak)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (19 classes, 11 protocols)

Classes: `NSMutableDictionary`, `OSADeviceRecoveryEnvHelper`, `OSAEphemeralLog`, `OSAEventPublisher`, `OSAHttpSubmitter`, `OSALog`, `OSAStreamDeflater`, `OSASubmissionPolicy`, `OSASubmitter`, `OverrideMountPathRequest`, `PCCBridgeEndpoint`, `PCCEndpoint`, `PCCGroupJob`, `PCCIDSEndpoint`, `PCCJob`, `PCCProxiedDevice`, `PCCProxyingDevice`, `PCCRequest`, `PCCUtilities`

Protocols: `IDSServiceDelegate`, `NSCoding`, `NSObject`, `NSSecureCoding`, `NSURLSessionDataDelegate`, `NSURLSessionDelegate`, `NSURLSessionTaskDelegate`, `NSXPCListenerDelegate`, `OSASyncProxyCallbacks`, `OSASyncProxyHandler`, `OSASyncProxyServices`

## Strings (1,369)

```
rejects
set-expire
Ok
<inactive>
x-hardware-model
POST
kOSAFetchCrashReporterKey
jobTimeout set to %.0f secs
PCCProxyingDevice.m
submission_info
%@-%@
responseError
<unknown>
crashreporter_key
No remote device found
no send tracking id
requestTimeout set to %.0f secs
x-fast-lane
-[OSAHttpSubmitter URLSession:task:didCompleteWithError:]
operation
DiagnosticPipeline
\t
deviceMetadata.proxy
remote
type
YES
com.apple.osanalytics.submissionsByLog
1.2.840.113635.100.6.52
-[OSAHttpSubmitter URLSession:dataTask:didReceiveResponse:completionHandler:]
OSAHttpSubmitter
autoCleanupProxiedFiles
jobType
failed-path
logFile
test-expire
PayloadContent
failed untrusted path validation
failed untrusted proxy validation
failed-opt-out
transfer-%@
endpoint
DUConfigSigning
uuid
log-aggregated
deviceMetadata
standard
metadata
unchanged
<descend>
synchronize
x-os-version
i
result
taskId
com.apple.osanalytics.tasking
<unknown-job>
x-tasking-requested
diagnostics
deviceType
com.apple.pcc.request-xfer
taskingLastSuccessfulRequest
<metadata>
blob
error_info
211
failed opt-out
taskingID
SKIPPING (pre-Rizz Apple TV)
<preface>
x-routing
com.apple.osanalytics.logRelay
received unknown event
initiateLogTransfer
remote-Ok
error_code
ProxyCompanionLogTransferErrorDomain
compression
\n
bugType
affirmed
submission-%@
LastSuccess
/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/sysdiagnose
jobStatus
<preserve>
dnu-override
com.apple.osanalytics.submissionStatus.plist
Throughput threshold violation
com.apple.osanalytics.endpoint.remoteXPC.initialization
subdir
group %@ %d/%d %@
initiateLogList
totalBytes
ProxyGizmoLogTransferErrorDomain
delivered
pending
I
PayloadType
value
tasking
event
com.apple.ProxiedCrashCopier
stability
connections
gz
txt
crashReporterKey
transfer_paths
DeviceClassNumber
<bogus-tracker>
x-product-release
name
failed
method not supported
Configuration
SKIPPING (pre-Rizz)
transfer
received
failed to create reply message to fetch crash reporter key
Unable to transfer file
<unsolicited>
failed-move
Unable to create pinned policy
com.apple.private.alloy.proxiedcrashcopier
com.apple.osanalytics.monitors
options
onDeviceLog
OS_ANALYTICS_STABILITY_MONITOR
anon
v8@?0
com.apple.osanalytics.endpoint.remoteXPC.events
proxyingDeviceTimeAtLastUpdate
custom
UAT
device_class
-[PCCGroupJob registerResult:error:]
group transfer already in progress
Retired
failed-duplicate
response
updateProxiedDeviceMetadata
timer
Content-Type
ProxyEndpointErrorDomain
service
transferred
job expired due to lack of progress
error
failed untrusted filename validation
complete
contentLength
OHTTP
nearby
com.apple.osanalytics.logTransfer
stability_parameters
requests
connection
logCount
v20@?0@\"OS_remote_device\"8B16
stability_result
com.apple.osanalytics.factoryproxysync
connect
files
ProxiedDevice-
proxied
aggdCount
unknown
<sync>
initiateMetadataUpdate
AppleTV
OSAnalyticsPrivate.OSAEventPublisher
core-analytics-tasking-key
legacy-homePath
/private/var/mobile/Library/Logs/DiagnosticPipeline
status
tracking
com.apple.OSASyncProxy.conn_queue
x-target-audience
com.apple.private.alloy.proxiedcrashcopier.icloud
fileMetadata
com.apple.pcc.job-xfer
<legacy>
unsolicited
primary
job_%@-%u-%@
Could not extract signature from blob, error %d
generateTransparencyLogs
path
bogus-test
summary
-[OSAHttpSubmitter cancelCurrentTask]
allFiles
xfer-group
description
Q
com.apple.ProxiedCrashCopier.request_queue
com.apple.CoreReporting.GenerateSensorDataLog
opt-out
, 
jobs
init()
messageType
sysdiagnose
ca
<untrusted>
extensions
received unknown dictionary
error_desc
Path non-accessible
synced
proxy
x-incident-id
!
<*>
submissions
x-crashreporter-key
rejected-capviolation
Unified
error_domain
supported
postHeaders
OUT
model
v16@?0@\"OS_remote_device\"8
metriclog
-1
single %@ %@
content
time
ProxyBridgeErrorDomain
jobEvent
<sort>
total
wantsProgress
sentBytes
Primary
-[OSAHttpSubmitter URLSession:dataTask:didReceiveData:]
jobProgress
FAILED
parameters
withTaskingId
v16@?0@\"NSError\"8
allow-optout
responseHeaders
url
stability_bundleID
ProxyJobErrorDomain
jobId
acceptTasking
includeMetadata
routing
-[OSAHttpSubmitter abort]
com.apple.ProxiedCrashCopier.job_queue
transaction
includeDPLogs
v12@?0i8
action
v16@?0@\"NSObject<OS_xpc_object>\"8
No remote connection to target device
ca1-ohttp
<whitelist>
submitted
version
da3
received message with missing/unknown sender
xfer-file
panic
expirations
%@ %@
failed-filename
policy
display
stability_coalitionName
PCCJob.m
prefaces
skipped - no metadata for proxy device
<ephemeral>
File unavailable
xattr_list
attempt
https://gateway-oblivious.apple.com/iphonesubmissions/convert.jsp
<file_xfer>
UniqueDeviceID
xfer-all
x-task-id
NO
IN
https://iphonesubmissions-uat.corp.apple.com/convert.jsp
settings
currentTaskingIDByRouting
sendAsMessage
expired due to lack of progress
default
logs
ips
<exempt>
all
<file>
bug_type
x-os-train
partial success
id
kOSASender
forRouting
reportType
x-dre-submission
length
ca1
UATSubmissionServer
r
build
OK
local-Ok
v16@?0@\"NSURL\"8
deflate
taskings
disablePushOnConnection
timeout
none
requesting
memgraph
failed-proxy-data
templates
%ld
submissions disabled
<cleanup>
com.apple.dataprotection.policy.exception-applied-by
core_analytics
errors
_package
results
msgs
<nil>
retirement-summary
https://iphonesubmissions.apple.com/convert.jsp
v32@?0@\"NSString\"8@\"NSString\"16^B24
proxied_dev
current
count
\t1
beta
com.apple.OTACrashCopier.capViolation
seconds
1.2.12
 NO
Bridge
bridge-xfer
-[PCCProxyingDevice handleMessage:from:]
com.apple.osanalytics.submissions
bytes
lastId
authenticationError
payloadLength
193
1.2.840.113635.100.6.2.10
includeSysdiagnoses
success
session
application/vnd.apple.ips
getFilenames
OSASubmitter
transfer progress %{public}@: %ld / %ld bytes
UNEXPECTED: incoming msg BEFORE outgoing connection established! *** consider deferring listener initialization ***
Got a NULL device from the remote device browser
Failed to send tasking payload to target '%@': %@
Received error from XPC request to run stability monitor: %{public}s
file send failure limit, abandoning job
Event publisher for stream '%s' sent synchronous event to subscriber with token %llu
no tasking id returned for %@
IDS(%@) connected with %d accounts and %d devices
received message '%@'
Browser is down; proceeding with setup
Unknown message %@
Browser was canceled
Error establishing connection to osanalyticshelper.
failed to get xattr value size for key: %s
ignoring %{public}@ during Opt-OUT
canceling remote connection with %@
Couldn't create the listener connection for %s
overwriting file at %{public}@
Ignoring device of type %s
jobProgress: no clientConnection on request %{public}@
Error triggering targeted stability monitor: %{public}s.
received request %@ (%@); posting %@ logs
Requesting tasking for routing %{public}@ using key %{public}@ with task_id %{public}@
Event publisher for stream '%s' sent async event to subscriber with token %llu
Set up failed: remote UDID was unavailable.
unknown job id %@
received file '%@'
failed to transfer file to remote device: failed to create temporary file
%@ is exiting interruped state; reconnecting
No identifier for %@ because there are no outgoing connections.
unknown payload format for ca1 routing
request expiration event; releasing transaction
Submission Result: %{public}@ after %u job(s), elapsed time %.2f s
Browser is already up; skipping setup
Failed to transfer log file at %@, error: %s
unable to package %@
Signature on blob is not trusted, %@
A bundle ID is required to evaluate the stability of a single process.
remote ProxyingDevice connected, initiating group xfer
Failed to read tasking update content: %@
Publishing event to %ld subscribers for stream '%s'
RSD device unexpectedly has more than one outgoing connection: need to specify a target.
local synchronization
%@ is already in interruped state; passing
Event publisher for stream '%s' finished processing all pending subscriber events
received request %@-%@ '%@'
%@ for device %@: productVersion=%{public}@ -> %{public}s
request %@ (%@) sent
%@ tasking needs refresh for routing (time elapsed: %f)
No connection to %@ on which to send message of type %@
Crash reporter key was not available in reply from %@
Including sysdiagnoses in log list
ERROR: PCCEndpoint::sendFile:metadata doesn't do anything
sent %@, tracking: %@
Browser found %s-%s: %s
Failed to validate CA tasking file: first line was not valid JSON
requesting remote synchronization with options: %@
sent %{public}@, tracking: %{public}@
updated staged tasking %@ '%@ <- %@'
%@ is not in interruped state; passing
received request %@ (%@)
posted %@ (unsolicited)
Event publisher timed out after 2 minutes while waiting for initial barrer
Connection failed: %@
job expiration event; releasing transaction
Submission jobs will include additional request headers %{public}@
'%@' payload %ld, metadata: %@
Serialization of settings to plist failed: %@
jobProgress: no request found for jobId %{public}@
Failed to get the data vault submission path.
%@:
incoming connection from %s ERROR %s\n
remote connection active
Forcing preservation of sysdiagnose or diagnostic pipeline log: %{public}@
unknown finishing message %@
Event publisher XPC error: %d
Attempted to send file before connecting
RemoteXPC and/or RemoteServiceDiscovery are not available on this platform
starting bogus job; wait for expiration in %.1f mins
Not including diagnostic pipeline logs in log list: DiagnosticRequest framework unavailable on current platform
request expiration event (with no outstanding requests!); releasing transaction
'%@' posting content of %lu bytes from %lu logs
%s '%s'
Device %@ disconnected before registration.
consecutive file send failure #%u
declining job %{public}@; group transfer already in progress (%{public}@)
writing: %@
re-starting request timer thereby extending transaction
Error persisting submission results: %@
 # Name/DeviceID        Model                Build      Near Pair Cntd Actv iCld
Not setting up endpoint for unsupported device.
starting job timer and creating transaction
updateProxiedDeviceMetadata:\n%@
transferLog options %@
no outstanding requests; releasing transaction
%s
  deltat: %.5f, threshold: %.1f (warnings %d)
deflateStream abort at cap limit %u
sendFile FAILED for %{public}@: %{public}@
failed to write results file, saving as txt
received jobProgress for %{public}@: %lld / %lld
UDID string was not available in property
Unable to fetch identifier from remote bridge.
Got unexpected xpc message from %s: %s\n
Unexpected response data; already installed tasking blob of type %@ this session
canceling remote connection for %@.
Failed to copy UDID property from remote device.
Got XPC_ERROR_CONNECTION_INVALID from %s\n
Parameters file not available.
PCCProxiedDevice asked to handle an unexpected file
Submission archive too big (> %u) for submission with file %@
FAILED to activate %{public}@ -> %{public}@ : %{public}@
Error handling %{public}@ from proxying device (%{public}@): %{public}@
request %@ (%@) enroute
Failed to copy remote service %s of connected device
Missing expected completion handler.
finished transferring %u logs successfully (%u rejected, %u errors) for job %@
starting job %{public}@, transfer group '%@'
Event publisher for stream '%s' received unknown event '%u'
failed to decode xattr value for key: %@
Including diagnostic pipeline logs in log list
re-starting job timer and extending transaction
incoming connection from %s is DOWN
Failed to find UUID from disconnected device
Skipping group transfer from proxy-configured device with disablePushOnConnection set
Failed to set proxied device ID xattr on %@
file status update %@
No submission parameters found from '%{public}@'
Error loading parameters: %{public}@
completed job %@: %@
nothing to do for %@-%@
Trial is not available on this platform.
FAILED to write metadata update: %@
request %@ (%@) complete %@
Event publisher for stream '%s' registered subscriber with token %llu
failed to write tmp remote file: [%d] %s
Device '%s' in connected state; attempting to establish service
Set up failed: RSD UUID was unavailable.
Sending request to stash crash reporter key for %@
Failed to get the root submission path.
no staged tasking %@
no handler installed?
%2d %-20@ %-20@ %-10@ %@  %@  %@  %@  %@
Outgoing connection to %@ is already valid
Error converting parameters to an XPC object: %{public}@
requestTimeout set to %.0f secs
remote ProxiedDevice disconnected
Timed out waiting for remote device CR key.
jobTimeout set to %.0f secs
no change staged tasking %@ '%@'
%@ for device %@: model=%{public}@ productVersion=%{public}@ -> %{public}s
Event publisher for stream '%s' removed subscriber with token %llu
submission template '%@:%@' includes [%@]; excludes [%@]
Handling request to fetch crash reporter key
Failed to fetch UDID: remote device was NULL.
Registering connection to remote device: %@
Got xpc error message from %s: %s\n
Failed to connect to remote service %s
re-starting request timer and extending transaction
Submissions have been disabled. To enable submissions, run osatool re-enable-submissions
incoming connection from %s is UP
Got XPC_ERROR_CONNECTION_INTERRUPTED from %s\n
received request %@ (%@); posting %@
Setting %@=%@ xattr on %@
aborting job %@; file send failure: %@
no outstanding jobs (and no transactions were in play)
specific file not available, abandoning job
finished transferring log successfully
Identifier not available for %@
relaying progress for job %{public}@: %ld / %ld bytes
%@ tasking key is %@
FAIL: no IDS accounts. Ensure the service plist is in place and try restarting identityservicesd.
sendMessage FAILED for %@: %@
removing registered device
path non-accessible, abandoning job
remote ProxyingDevice disconnected
Failed to read tasking payload at %@: %@
job %@ %@ completed %@
config: %@\npolicy: %@
deflateStream error reading (errno %d)
delivery receipt tracked %@
Could not safely open submission results path: %@
preface payload %ld, metadata: %@
Error loading parameters from Trial.
da3 tasking results: %@
jobProgress: no filePath on request %{public}@ (group transfer?), skipping
progress callback error: %{public}@
Attempted to send message before connecting
Adding xattr to incoming file %@: %@
Device %s is disconnected
Device %@ disconnected before outgoing connections were set up.
Missing identifier with which to fetch remote connection
posted %@-%@
msg callback %s tracked %@ %@
canceling listening connection
Tearing down connections for disconnected device %@.
gathered %u files for transfer
remote synchronization
starting request timer and creating transaction
Submission archive too big (> %u) for submission with preface
didSendBodyData %d (total %d of %d)
Failed to fetch CR key due to no outgoing connection for %@
no outstanding jobs; releasing transaction
remote ProxiedDevice connected
OTALogArchive unable to initialize zlib (ret %d)
Unexpected metadata from RemoteXPC: '%@'\nOriginal xpc message %s
'%@' server responded %d with %lu-byte payload
----- '%{public}@' -----
Initiating submission for '%{public}@' optIn: %@
No logs/tasking found for submission from '%{public}@'
ERROR: PCCEndpoint::sendMessage: doesn't do anything
Got a NULL UUID; remote device may not be connected.
failed to get xattr value for key: %s
FAILED untrusted filename validation '%{public}@'
%@
Registering new sender from incoming message.
failed to get xattr list size for file: %s
CA tasking results: %@
Cannot find identifier: local system is neither an RSD device nor host.
file send failure, abandoning job: %@
starting job %{public}@, %{public}@ '%{public}@'
Not clearing past submission artifacts because path is not available.
Failed to release sandbox extension: %s (%i)
IDS(%@) connected with no accounts.
request %@ (%@) acknowledged
Initializing event publisher with stream %s
No connection to %@ on which to send file
Remote device was NULL
Duplicate log detected at %{public}@
device is already in the correct %@ investigation
   %@
%@ is entering interrupted state; disconnecting
sent %@
Received unexpected reply message from %@: %s
received request %@-%@ '%@' payload %@ %p
starting bogus request; wait for expiration in %.1f mins
incoming log %{public}@
unable to create xpc file xfer object for %{public}@
OSADeviceRecoveryEnvHelper
PCCEndpoint
NSXPCListenerDelegate
OSASubmitterExtension
OSAEphemeralLog
IDSServiceDelegate
PCCGroupJob
OSASyncProxyHandler
NSCoding
OSAHttpSubmitter
PCCBridgeEndpoint
PCCJob
OSAStreamDeflater
OSASubmitter
OverrideMountPathRequest
NSSecureCoding
NSURLSessionTaskDelegate
NSObject
NSURLSessionDataDelegate
PCCIDSEndpoint
PCCProxiedDevice
OSASyncProxyServices
OSASyncProxyCallbacks
PCCUtilities
NSURLSessionDelegate
PCCExtension
PCCRequest
OSAEventPublisher
OSASubmissionPolicy
PCCProxyingDevice
_log_sets
deviceForTarget:
numberWithUnsignedInteger:
_clientConnection
_group_type
_jobCount
addSenderToMessage:
fileURLWithPath:
_in
UDIDForRemoteDevice:
retire:
_callback
_last_thoughput_check
sendDeviceMetadata:
service:account:incomingMessage:fromID:
JSONObjectWithData:options:error:
_specific_files
_identifier
copyDeflatedDataFromStream:withCap:
hasTasking
initWithUUIDString:
isNearby
T@\"NSDictionary\",R
debugDescription
diagnosticPipelineLogs
setHTTPBody:
valueForKey:
T@\"NSString\",R,V_jid
allHeaderFields
options
URLSessionDidFinishEventsForBackgroundURLSession:
_dryRun
URLSession:didCreateTask:
T@\"NSSet\",N,C
pathDiagnostics
_responseError
arrayByAddingObjectsFromArray:
file_count
initWithCapacity:
createRetiredDirectoriesForUser:
initWithID:forTarget:options:forFile:
submissionsDisabled
taskingLastSuccessfulRequest
_device_browser
productBuildVersion
releaseType
submissionParam:
updateProxiedDeviceMetadata:from:
serviceSpaceDidBecomeAvailable:
expire_count
initiate:transferLog:withOptions:job:
primarySubmissionPaths
service:account:incomingOpportunisticData:withIdentifier:fromID:context:
setupDeviceStateChangeHandler
shouldSubmitRouting:
URLSession:dataTask:didReceiveResponse:completionHandler:
numberWithBool:
_responseData
service:account:identifier:didSendWithSuccess:error:context:
startTimer
_package
cheaterTaskingWithSets:usingConfig:resultsCallback:
containsObject:
endpointToString:
removeObjectAtIndex:
scanLogs:from:options:
send:message:error:
type
URLSession:task:didReceiveInformationalResponse:
metaData
msg_count
setExportedInterface:
targetAudience
URLSession:dataTask:didBecomeStreamTask:
arrayWithCapacity:
iterateLogsWithOptions:usingBlock:
subscriberTokens
_eventQueue
dictionaryWithContentsOfURL:error:
preserveFiles
removeAllObjects
up_count
service:account:incomingData:fromID:context:
setValue:forHTTPHeaderField:
performSelector:
requestProxyMetadata:onComplete:
requestTimeout
service:connectedDevicesChanged:
temporaryFileWithPrefix:fd:
_jid
applyTasking:taskId:usingConfig:fromBlob:
releaseSandboxExtensions
service:account:incomingMessage:fromID:context:
service:account:incomingUnhandledProtobuf:fromID:context:
_preserveFiles
_reqByTracker
dataTaskWithRequest:
fastLane
initiate:transferGroupWithOptions:job:
isWhitelisted:forDomain:
numberWithInt:
setHTTPMethod:
request:generateTransparencyLogs:
serviceAllowedTrafficClassifiersDidReset:
timeIntervalSince1970
validateFirstLineAsJSON:
currentConnection
data
service:account:receivedGroupSessionParticipantDataUpdate:
supportsSecureCoding
synchronize:withOptions:
URLSession:task:didReceiveChallenge:completionHandler:
_primary_template
applyTasking:taskId:fromBlob:
scanLogs:from:
sendResourceAtURL:metadata:toDestinations:priority:options:identifier:error:
T@\"NSString\",R,V_event
overrideMountPath
packageLog:forRouting:info:options:
TQ,R
_fileTimeout
addSuiteNamed:
self
setLaunchInfo:
timeIntervalSinceNow
URLSession:dataTask:didReceiveData:
sysdiagnoseRoot
_delegate
productVersion
_requestTimeout
dealloc
isLocallyPaired
fileExistsAtPath:isDirectory:
firstObject
identifierForTarget:
locateLog:forRouting:usingConfig:options:error:
addObject:
modelIdentifier
_capViolation
_responseCode
defaultSessionConfiguration
initWithData:andMetadata:
isDeviceNearby:
T@?,C,V_callback
URLSession:task:willBeginDelayedRequest:completionHandler:
addEntriesFromDictionary:
fileTimeout
initialBarrierReceived
removeObjectsForKeys:
send:file:metadata:error:
T@\"OS_dispatch_semaphore\",N,R,VinitialBarrierReceived
closeFile
autorelease
intValue
postContent:withHeaders:toEndpoint:
service:account:receivedGroupSessionParticipantUpdate:context:
_sandboxExtensions
serviceByDeviceID:
writeToFile:atomically:encoding:error:
numberWithLong:
_type
crashReporterKey
fileHandleForReadingFromURL:error:
handleFile:from:metadata:
moveItemAtPath:toPath:error:
taskingNeedsRefreshForRouting:at:
_deviceIds
dictionaryWithDictionary:
identifier
initWithSandboxExtensions:
doubleValue
removeItemAtURL:error:
T@\"NSString\",?,R,C
_allowUnsignedBlobs
addRequest:event:type:onComplete:
dataWithPropertyList:format:options:error:
getUUIDBytes:
levelForFactor:withNamespaceName:
setAllowUnsignedBlobs:
arrayWithArray:
_error_count
_options
acceptTaskingPayload:forRouting:withId:
hasPrefix:
zone
request:transferLog:onComplete:
_rejected_count
_internalWhitelist
_jobTimeout
_total_count
enterInterruptedStateFrom:
service:account:inviteReceivedForSession:fromID:withContext:
accounts
compare:options:
removeItemAtPath:error:
setJobTimeout:
addDelegate:queue:
diagnosticPipelineRoot
scanOptions
service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:
Td,V_requestTimeout
cancel
numberWithUnsignedInt:
service:account:receivedGroupSessionParticipantUpdate:
_txn
initWithSuiteName:
name
setFileTimeout:
T@\"OS_xpc_event_publisher\",N,R,Vpublisher
_event
buildVersion
init
pathSubmissionDataVault
processSubmissionJobs:usingConfig:summarize:
service:activeAccountsChanged:
attributesOfItemAtPath:error:
service:devicesChanged:
service:didSwitchActivePairedDevice:acknowledgementBlock:
stringByAppendingString:
_dataTask
_lastTouch
fileValue
_errObj
cleanupRetired:
_sync_proxy_queue
isDiagnosticPipelineLog:
sharedInstance
_scanOptions
service:account:incomingResourceAtURL:fromID:context:
submissionPathsWithHomeDirectory:withProxies:
set
defaultManager
T#,R
_initializationQueue
_tasking_summary
clientConnection
finish:target:event:type:result:
initWithPath:forRouting:usingConfig:options:error:
_connectionType
T@\"NSString\",R,V_target
_remoteCRKeys
registerRouting:result:
T@\"NSString\",C,V_connectionType
fileSystemRepresentation
generateLogList:
uniqueID
_results
dataWithContentsOfURL:options:error:
finishRequestWithMessage:result:
appleInternal
diagnosticResultsEvent:type:result:
dictionaryWithContentsOfFile:
performSelector:withObject:withObject:
superclass
service:account:identifier:fromID:hasBeenDeliveredWithContext:
_outgoingConnections
productVersionForDevice:
_endpoint
_metadata
callback
floatValue
optInApple
sendEventToSubscribers:waitForReplies:
service:linkedDevicesChanged:
T@\"NSDate\",R,V_lastTouch
_serviceByDevice
initWithFileDescriptor:closeOnDealloc:
lock
publisher
setWithObject:
taskingKeyForRouting:withConfig:
service:account:inviteDroppedForSessionID:fromID:context:error:
URLSession:task:didFinishCollectingMetrics:
UUID
count
isEqualToString:
latestResults
synchronize:withOptions:onComplete:
_prefaces
fileExistsAtPath:
getResourceValue:forKey:error:
job_count
submitToUAT
T@\"NSLock\",N,R,VtokensLock
URLWithString:
initWithEndpoint:
interfaceWithProtocol:
setObject:forKeyedSubscript:
unlock
_content
isInDeviceRecoveryEnvironment
length
pathWithComponents:
stringWithUTF8String:
_hasTasking
osTrain
_interruptedDevices
_wantsProgress
transferProgressForFilePath:sentBytes:totalBytes:
remoteDeviceForIdentifier:
.cxx_destruct
_request_queue
_success_count
dictionary
hash
URLSession:dataTask:didBecomeDownloadTask:
_listeningConnection
connectionForIdentifier:
request:logList:
setExportedObject:
_consecutive_error_count
enumerateKeysAndObjectsUsingBlock:
pathSubmission
performSelector:withObject:
tokensLock
T@\"NSXPCConnection\",W,V_clientConnection
_remoteDevices
dataWithContentsOfFile:
setSubscriberTokens:
arrayWithObjects:count:
processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:
T@\"NSDictionary\",R,V_metadata
URLByAppendingPathExtension:
URLSession:didBecomeInvalidWithError:
deviceIds
filePath
getFilenames
handleConnection:from:
objectForKey:
TB,R,V_hasTasking
countByEnumeratingWithState:objects:count:
getAvailableTaskingRoutings
launchInfo
setIgnoreProxies:
setNetworkServiceType:
submitLogsUsingPolicy:resultsCallback:
summarizeLog:reason:
TB,R
T@\"NSArray\",R,V_deviceIds
description
localizedDescription
proxyTasking:taskId:usingConfig:fromBlob:
retainCount
setValue:forKey:
URLSession:task:needNewBodyStream:
ack:result:error:
encodeObject:forKey:
recordEvent:with:
service:account:inviteReceivedForSession:fromID:withOptions:
setInternalWhitelist:
setupIncomingEventListener
statusCode
doWork:
_submissionSem
service:nearbyDevicesChanged:
startRequest:message:callerConnection:onComplete:
URLSession:task:needNewBodyStreamFromOffset:completionHandler:
UUIDString
listDevices:
service:account:didReceiveLocalNetworkHandshake:fromID:context:
connectionType
finishTasksAndInvalidate
ignoreProxies
setLength:
URLSession:taskIsWaitingForConnectivity:
initFromPath:
set_usesNWLoader:
timeIntervalSinceReferenceDate
T@\"NSString\",R,V_type
TB,V_capViolation
_out
T@\"NSArray\",C,V_internalWhitelist
_filePath
appendBytes:length:
errorWithDomain:code:userInfo:
markFile:withKey:value:
allKeys
TB,V_wantsProgress
T@\"NSString\",N,R
isDefaultPairedDevice
jobTimeout
assembleMetadataAt:withOptions:
addObjectsFromArray:
prepareNext
stashCrashReporterKeyForIdentifier:
stringByDeletingPathExtension
_reqById
exitInterruptedStateFrom:
finishRequest:result:
isDataVaultEnabled
service:account:identifier:hasBeenDeliveredWithContext:
writeToFile:atomically:
_job_queue
abort
conformsToProtocol:
initWithCoder:
mutableCopy
T@\"NSDictionary\",R,V_options
T@\"NSString\",R
_accumulateKey:value:
cancelCurrentTask
date
domain
filepath
stream
persist
stringByAppendingPathExtension:
release
_strm
currentTaskingIDByRouting
prefaceSubmission:withData:usingArchive:andHeaders:
result
setClientConnection:
clientWithIdentifier:
URLSession:dataTask:willCacheResponse:completionHandler:
generateSensorDataLog
propertyListWithData:options:format:error:
removeObjectForKey:
setWantsProgress:
URLSession:didReceiveChallenge:completionHandler:
ensureUsablePath:component:options:
getXattrWithName:at:
identifierForRemoteDevice:
recoveryModeReason
sendMessage:toDestinations:priority:options:identifier:error:
setRemoteObjectInterface:
initWithUUIDBytes:
isSupportedRemoteDeviceType:
acceptTaskingFile:forRouting:withId:
initWithBytes:length:encoding:
isEqual:
longLongValue
request:transferGroupWithOptions:onComplete:
componentsJoinedByString:
numberWithInteger:
pathExtension
userInfo
T@\"NSArray\",R,V_sandboxExtensions
URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:
modelCode
removeObject:
resume
service:didSendOpportunisticDataWithIdentifier:toIDs:
_default_template
isCloudConnected
isSysdiagnose:
scanProxies:
service:account:identifier:sentBytes:totalBytes:
setObject:forKey:
transferProgress:sentBytes:totalBytes:
boolForKey:
_loadPreviousResults
initWithMessage:options:
setCallback:
writeData:error:
_expiryTimer
bytes
isKindOfClass:
requestWithURL:cachePolicy:timeoutInterval:
decodeArrayOfObjectsOfClass:forKey:
isFilenameReasonable:
remoteObjectProxyWithErrorHandler:
service:account:inviteReceivedForSession:fromID:
request:logListWithOptions:onComplete:
runWithDelegate:
bugType
service:account:incomingResourceAtURL:metadata:fromID:context:
appendData:
boolValue
modelIdentifierForDevice:
T@\"NSString\",R,V_filePath
_pairedWatchService
allValues
logDomain
objectForKeyedSubscript:
overrideMountPath:
URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:
allowUnsignedBlobs
updateTaskingLastSuccessfulRequest:at:
TI,V_fileTimeout
pathComponents
setConnectionType:
stringByAppendingPathComponent:
UTF8String
readDataOfLength:
request_count
setPreserveFiles:
startPublisher
initWithTemplate:options:
numberWithLongLong:
retain
URLSession:task:didCompleteWithError:
_recordRetirement:reason:
_response
isConnected
respondsToSelector:
T@\"NSMutableDictionary\",R,V_scanOptions
registerResult:error:
sandboxExtensions
setRequestTimeout:
extractAuthenticatedBlob:error:
capViolation
encodeWithCoder:
initWithService:
prepConfig:
service:didCancelMessageWithSuccess:error:identifier:
sessionWithConfiguration:delegate:delegateQueue:
stringByDeletingLastPathComponent
_thoughput_warnings
path
stringByReplacingOccurrencesOfString:withString:
isProxy
_ignoreProxies
_setQueue:
initWithID:forTarget:options:
setXattrWithName:value:at:
startService:
lastTouch
numberWithDouble:
wantsProgress
T@\"NSString\",R,C
_requestURL
array
deliver:taskingFile:routing:taskId:asMessage:overRSD:
fileURLWithPathComponents:
isMemberOfClass:
_jobByTracker
_payload
event
nextFilepath
service:account:identifier:didSendWithSuccess:error:
setCapViolation:
closeFileStream
initWithStream:
_launchInfo
listener:shouldAcceptNewConnection:
receivedReport:from:metadata:
request:transferLog:withOptions:onComplete:
standardUserDefaults
copy
dictionaryWithObjects:forKeys:count:
handleMessage:from:
class
getAdditionalRequestHeaders
metadata
T@\"NSDictionary\",C,V_launchInfo
_allowOptOutByRouting
_sync_summary
dataWithJSONObject:options:error:
getXattrBoolValWithName:at:
lastPathComponent
fileModificationDate
handleSubscriptionEventWithAction:token:descriptor:
isActive
stringWithFormat:
Td,V_jobTimeout
TB,V_preserveFiles
_responseHeaders
setHTTPShouldHandleCookies:
devices
TB,V_allowUnsignedBlobs
isOnDeviceLogType:
_groupXferJob
buildSubmissionTemplateForConfig:
installCATasking:withId:untasked:
internalWhitelist
setupOutgoingConnection:
target
_target
TB,V_ignoreProxies
jid
_homeDeviceService
code
service:account:incomingPendingMessageOfType:fromID:context:
stringByStandardizingPath
T@,R
v32@0:8@\"NSDictionary\"16@\"NSString\"24
v32@0:8@16q24
@56@0:8@16@24@32@40^@48
@\"NSMutableData\"
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40
v24@0:8d16
Q16@0:8
v64@0:8@16@24@32@40@?48@56
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56
@\"IDSService\"
d16@0:8
v12@?0i8
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32
@28@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16I24
v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32
v32@0:8@\"IDSService\"16@\"NSArray\"24
@40@0:8@16@24@32
v56@0:8@16@24q32q40q48
{z_stream_s=\"next_in\"*\"avail_in\"I\"total_in\"Q\"next_out\"*\"avail_out\"I\"total_out\"Q\"msg\"*\"state\"^{internal_state}\"zalloc\"^?\"zfree\"^?\"opaque\"^v\"data_type\"i\"adler\"Q\"reserved\"Q}
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48
@\"PCCEndpoint\"
i
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@@\"NSError\">32
@32@0:8@16@24
@\"NSError\"
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
I16@0:8
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32
v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@@\"NSError\">32
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v28@0:8@16B24
v48@0:8@16@24@32@40
v24@0:8@\"IDSService\"16
v20@0:8I16
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48
v24@0:8@\"NSURLSession\"16
@24@0:8@16
@\"NSMutableDictionary\"
@48@0:8@16@24@32@40
v36@0:8@16@24i32
@32@0:8:16@24
@28@0:8@16B24
v56@0:8@16@24@32q40q48
v36@0:8@\"NSString\"16B24@\"NSError\"28
v56@0:8@16@24@32@40B48B52
v20@0:8B16
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48
v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48
v24@0:8@?16
@\"NSObject<OS_dispatch_semaphore>\"
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56
v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32
@\"PCCGroupJob\"
B32@0:8@16d24
@48@0:8@16@24@32^@40
v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36
@\"OS_xpc_remote_connection\"
@\"OS_dispatch_semaphore\"
v32@0:8@16@24
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40
v64@0:8@16@24@32@40@48@56
B16@0:8
B
@32@0:8@16^@24
B24@0:8@16
v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44
v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40B48B52
v24@0:8@16
v36@0:8I16Q20@28
v56@0:8@16@24@32@40@?48
@\"NSDictionary\"
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40
@\"OSALog\"
@24@0:8@\"NSCoder\"16
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32
B32@0:8@16@24
?
#16@0:8
@40@0:8:16@24@32
B24@0:8#16
Vv16@0:8
@24@0:8:16
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48
B20@0:8I16
v40@0:8@16q24q32
v40@0:8@\"NSString\"16q24q32
v24@0:8@?<v@?@@\"NSError\">16
v48@0:8@16@24q32@?40
v32@0:8@\"IDSService\"16@\"NSSet\"24
@\"NSObject<OS_dispatch_queue>\"
v28@0:8B16@20
v36@0:8@16B24@28
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
v16@0:8
@\"NSHTTPURLResponse\"
v44@0:8@16B24@28@36
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48
@\"NSObject<OS_dispatch_source>\"
v32@0:8@16@?24
v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40
v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44
v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32
@72@0:8@16@24@32@40@48@56@64
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48
v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52
@\"NSDate\"
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
v28@?0I8Q12@\"<OS_xpc_object>\"20
v52@0:8@16@24@32B40@44
^{_NSZone=}16@0:8
B24@0:8@\"Protocol\"16
v24@0:8@\"NSCoder\"16
B24@0:8:16
v56@0:8@16@24@32@40@48
@\"NSXPCConnection\"
@\"NSLock\"
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48
@\"NSURLSessionDataTask\"
@40@0:8@16@24^@32
v28@0:8B16@\"NSString\"20
@?
v60@0:8@16@24@32B40@44@52
i28@0:8@16B24
q
@\"NSString\"16@0:8
*
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48
v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSDictionary\"32
@16@0:8
v40@0:8@16@24@?32
v24@0:8r*16
v56@0:8@16@24q32@40@48
v52@0:8@16@24B32@36@44
@\"OS_remote_device_browser\"
@?16@0:8
v32@0:8@16d24
@\"NSMutableSet\"
v40@0:8@16@24@32
@\"NSArray\"
@\"NSString\"
@\"NSObject<OS_os_transaction>\"
@\"OS_xpc_event_publisher\"
@\"NSData\"
v48@0:8@16@24@32@?40
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40
@20@0:8i16
I
@\"NSMutableArray\"
d
@\"<OSASyncProxyHandler>\"
```
