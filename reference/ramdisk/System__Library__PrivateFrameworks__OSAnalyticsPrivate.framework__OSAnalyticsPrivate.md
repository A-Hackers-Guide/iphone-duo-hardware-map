# `/System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate`

From the upgrade restore ramdisk (141-29011-104.dmg). 438,576 bytes.

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
com.apple.osanalytics.submissionStatus.plist
xfer-group
remote
taskingID
display
jobId
failed untrusted path validation
summary
OSAnalyticsPrivate.OSAEventPublisher
-[OSAHttpSubmitter URLSession:task:didCompleteWithError:]
v20@?0@\"OS_remote_device\"8B16
<unsolicited>
files
dnu-override
logs
anon
i
https://gateway-oblivious.apple.com/iphonesubmissions/convert.jsp
OSAHttpSubmitter
com.apple.osanalytics.endpoint.remoteXPC.events
com.apple.osanalytics.logTransfer
xfer-all
%@-%@
rejects
expirations
deviceMetadata.proxy
failed-opt-out
delivered
name
-[OSAHttpSubmitter cancelCurrentTask]
requests
failed opt-out
x-os-train
legacy-homePath
local-Ok
sendAsMessage
device_class
errors
<unknown-job>
failed-filename
Configuration
supported
SKIPPING (pre-Rizz)
transfer
!
jobProgress
<sort>
deviceMetadata
Retired
<whitelist>
v8@?0
panic
<descend>
ProxiedDevice-
custom
stability_bundleID
stability_coalitionName
xattr_list
settings
includeSysdiagnoses
transfer_paths
<preface>
contentLength
FAILED
logFile
connections
jobTimeout set to %.0f secs
primary
content
jobs
OK
failed to create reply message to fetch crash reporter key
UniqueDeviceID
jobEvent
DiagnosticPipeline
1.2.840.113635.100.6.52
unknown
POST
-[OSAHttpSubmitter abort]
No remote connection to target device
synchronize
error_info
diagnostics
da3
UATSubmissionServer
UAT
initiateMetadataUpdate
includeDPLogs
v16@?0@\"NSError\"8
x-tasking-requested
disablePushOnConnection
updateProxiedDeviceMetadata
<bogus-tracker>
currentTaskingIDByRouting
action
method not supported
jobStatus
com.apple.osanalytics.monitors
connection
deflate
v12@?0i8
taskingLastSuccessfulRequest
x-dre-submission
bug_type
bugType
service
allFiles
PCCJob.m
msgs
totalBytes
submission_info
x-fast-lane
metadata
blob
v16@?0@\"NSURL\"8
initiateLogTransfer
x-os-version
submissions disabled
submissions
r
stability_parameters
unsolicited
proxyingDeviceTimeAtLastUpdate
application/vnd.apple.ips
url
https://iphonesubmissions-uat.corp.apple.com/convert.jsp
tasking
results
v16@?0@\"OS_remote_device\"8
memgraph
routing
NO
Primary
skipped - no metadata for proxy device
build
No remote device found
transferred
extensions
ca1-ohttp
bytes
submission-%@
/private/var/mobile/Library/Logs/DiagnosticPipeline
 NO
Unable to transfer file
com.apple.osanalytics.factoryproxysync
getFilenames
<sync>
proxied_dev
forRouting
remote-Ok
attempt
com.apple.osanalytics.submissionsByLog
Throughput threshold violation
bridge-xfer
ProxyJobErrorDomain
<metadata>
Content-Type
parameters
current
LastSuccess
transfer-%@
aggdCount
nearby
I
reportType
Ok
init()
compression
complete
taskings
SKIPPING (pre-Rizz Apple TV)
templates
x-target-audience
ca1
core-analytics-tasking-key
id
options
opt-out
taskId
stability
status
connect
expired due to lack of progress
OUT
metriclog
<*>
ProxyGizmoLogTransferErrorDomain
response
retirement-summary
Bridge
com.apple.osanalytics.logRelay
operation
-[PCCProxyingDevice handleMessage:from:]
<inactive>
result
com.apple.osanalytics.submissions
responseError
received unknown dictionary
<cleanup>
_package
wantsProgress
1.2.840.113635.100.6.2.10
com.apple.private.alloy.proxiedcrashcopier
deviceType
no send tracking id
job expired due to lack of progress
failed-path
beta
endpoint
v32@?0@\"NSString\"8@\"NSString\"16^B24
tracking
error_code
ProxyCompanionLogTransferErrorDomain
type
com.apple.osanalytics.endpoint.remoteXPC.initialization
received message with missing/unknown sender
requesting
failed-duplicate
x-hardware-model
DUConfigSigning
OSASubmitter
v16@?0@\"NSObject<OS_xpc_object>\"8
-[PCCGroupJob registerResult:error:]
AppleTV
Q
bogus-test
, 
received
unchanged
ca
count
PayloadType
<legacy>
com.apple.pcc.request-xfer
default
prefaces
-[OSAHttpSubmitter URLSession:dataTask:didReceiveResponse:completionHandler:]
com.apple.private.alloy.proxiedcrashcopier.icloud
crashreporter_key
single %@ %@
requestTimeout set to %.0f secs
<untrusted>
payloadLength
rejected-capviolation
IN
1.2.12
ProxyEndpointErrorDomain
<file>
log-aggregated
initiateLogList
authenticationError
total
timer
standard
sentBytes
autoCleanupProxiedFiles
x-product-release
failed
responseHeaders
time
group %@ %d/%d %@
211
<ephemeral>
messageType
kOSASender
error_desc
acceptTasking
YES
affirmed
/private/var/mobile/Library/Logs/CrashReporter/DiagnosticLogs/sysdiagnose
sysdiagnose
\t1
seconds
postHeaders
session
partial success
PayloadContent
PCCProxyingDevice.m
x-incident-id
length
ips
version
https://iphonesubmissions.apple.com/convert.jsp
<exempt>
Path non-accessible
test-expire
error
withTaskingId
timeout
failed-proxy-data
Unified
event
com.apple.ProxiedCrashCopier.job_queue
gz
failed untrusted filename validation
<nil>
x-crashreporter-key
submitted
File unavailable
received unknown event
<preserve>
jobType
path
failed-move
x-routing
logCount
Could not extract signature from blob, error %d
model
<unknown>
ProxyBridgeErrorDomain
com.apple.dataprotection.policy.exception-applied-by
all
%ld
generateTransparencyLogs
allow-optout
proxied
OS_ANALYTICS_STABILITY_MONITOR
xfer-file
group transfer already in progress
com.apple.CoreReporting.GenerateSensorDataLog
policy
onDeviceLog
com.apple.ProxiedCrashCopier.request_queue
synced
x-task-id
com.apple.OTACrashCopier.capViolation
lastId
crashReporterKey
stability_result
\t
com.apple.ProxiedCrashCopier
set-expire
success
value
193
Unable to create pinned policy
-[OSAHttpSubmitter URLSession:dataTask:didReceiveData:]
<file_xfer>
kOSAFetchCrashReporterKey
DeviceClassNumber
-1
com.apple.osanalytics.tasking
txt
uuid
core_analytics
description
includeMetadata
com.apple.OSASyncProxy.conn_queue
proxy
\n
job_%@-%u-%@
pending
OHTTP
subdir
transaction
error_domain
fileMetadata
none
com.apple.pcc.job-xfer
%@ %@
failed untrusted proxy validation
Connection failed: %@
%@ is entering interrupted state; disconnecting
Set up failed: RSD UUID was unavailable.
starting job %{public}@, %{public}@ '%{public}@'
Browser is already up; skipping setup
Unknown message %@
Unexpected response data; already installed tasking blob of type %@ this session
incoming connection from %s ERROR %s\n
No connection to %@ on which to send file
Outgoing connection to %@ is already valid
PCCProxiedDevice asked to handle an unexpected file
Event publisher for stream '%s' sent synchronous event to subscriber with token %llu
Got XPC_ERROR_CONNECTION_INVALID from %s\n
'%@' server responded %d with %lu-byte payload
didSendBodyData %d (total %d of %d)
deflateStream abort at cap limit %u
msg callback %s tracked %@ %@
received request %@ (%@); posting %@ logs
%@ tasking needs refresh for routing (time elapsed: %f)
RemoteXPC and/or RemoteServiceDiscovery are not available on this platform
finished transferring log successfully
posted %@ (unsolicited)
incoming connection from %s is UP
UNEXPECTED: incoming msg BEFORE outgoing connection established! *** consider deferring listener initialization ***
no tasking id returned for %@
ERROR: PCCEndpoint::sendFile:metadata doesn't do anything
Browser is down; proceeding with setup
unknown finishing message %@
Error persisting submission results: %@
%@ is exiting interruped state; reconnecting
RSD device unexpectedly has more than one outgoing connection: need to specify a target.
Failed to connect to remote service %s
Duplicate log detected at %{public}@
transferLog options %@
preface payload %ld, metadata: %@
received request %@ (%@); posting %@
requesting remote synchronization with options: %@
%@:
failed to transfer file to remote device: failed to create temporary file
transfer progress %{public}@: %ld / %ld bytes
writing: %@
Attempted to send message before connecting
Not clearing past submission artifacts because path is not available.
No logs/tasking found for submission from '%{public}@'
%s '%s'
request %@ (%@) acknowledged
deflateStream error reading (errno %d)
Tearing down connections for disconnected device %@.
Device %@ disconnected before registration.
remote connection active
Serialization of settings to plist failed: %@
Device %@ disconnected before outgoing connections were set up.
Identifier not available for %@
Failed to fetch CR key due to no outgoing connection for %@
Error triggering targeted stability monitor: %{public}s.
consecutive file send failure #%u
file send failure limit, abandoning job
aborting job %@; file send failure: %@
jobProgress: no request found for jobId %{public}@
Failed to release sandbox extension: %s (%i)
sendFile FAILED for %{public}@: %{public}@
canceling listening connection
Registering new sender from incoming message.
removing registered device
path non-accessible, abandoning job
re-starting request timer thereby extending transaction
Event publisher for stream '%s' finished processing all pending subscriber events
No connection to %@ on which to send message of type %@
Sending request to stash crash reporter key for %@
starting request timer and creating transaction
Unexpected metadata from RemoteXPC: '%@'\nOriginal xpc message %s
Failed to fetch UDID: remote device was NULL.
failed to get xattr value size for key: %s
starting bogus job; wait for expiration in %.1f mins
re-starting job timer and extending transaction
Submissions have been disabled. To enable submissions, run osatool re-enable-submissions
Got XPC_ERROR_CONNECTION_INTERRUPTED from %s\n
Set up failed: remote UDID was unavailable.
completed job %@: %@
Event publisher for stream '%s' removed subscriber with token %llu
  deltat: %.5f, threshold: %.1f (warnings %d)
Handling request to fetch crash reporter key
Failed to find UUID from disconnected device
sent %@
No submission parameters found from '%{public}@'
OTALogArchive unable to initialize zlib (ret %d)
received request %@-%@ '%@' payload %@ %p
Failed to send tasking payload to target '%@': %@
no outstanding requests; releasing transaction
Event publisher for stream '%s' sent async event to subscriber with token %llu
Initiating submission for '%{public}@' optIn: %@
FAIL: no IDS accounts. Ensure the service plist is in place and try restarting identityservicesd.
Failed to copy remote service %s of connected device
Failed to read tasking update content: %@
remote ProxiedDevice disconnected
posted %@-%@
Event publisher timed out after 2 minutes while waiting for initial barrer
Cannot find identifier: local system is neither an RSD device nor host.
no outstanding jobs (and no transactions were in play)
starting job timer and creating transaction
jobProgress: no clientConnection on request %{public}@
%@ for device %@: productVersion=%{public}@ -> %{public}s
submission template '%@:%@' includes [%@]; excludes [%@]
UDID string was not available in property
no change staged tasking %@ '%@'
Not setting up endpoint for unsupported device.
Got xpc error message from %s: %s\n
Missing identifier with which to fetch remote connection
Adding xattr to incoming file %@: %@
FAILED to write metadata update: %@
job %@ %@ completed %@
request expiration event (with no outstanding requests!); releasing transaction
 # Name/DeviceID        Model                Build      Near Pair Cntd Actv iCld
failed to get xattr list size for file: %s
Skipping group transfer from proxy-configured device with disablePushOnConnection set
Crash reporter key was not available in reply from %@
progress callback error: %{public}@
unknown job id %@
Device %s is disconnected
incoming log %{public}@
Error handling %{public}@ from proxying device (%{public}@): %{public}@
Attempted to send file before connecting
Got a NULL device from the remote device browser
gathered %u files for transfer
remote ProxyingDevice disconnected
remote synchronization
Ignoring device of type %s
specific file not available, abandoning job
remote ProxyingDevice connected, initiating group xfer
re-starting request timer and extending transaction
   %@
Couldn't create the listener connection for %s
Timed out waiting for remote device CR key.
Error converting parameters to an XPC object: %{public}@
sent %{public}@, tracking: %{public}@
Received error from XPC request to run stability monitor: %{public}s
jobProgress: no filePath on request %{public}@ (group transfer?), skipping
Publishing event to %ld subscribers for stream '%s'
delivery receipt tracked %@
received request %@ (%@)
local synchronization
%2d %-20@ %-20@ %-10@ %@  %@  %@  %@  %@
canceling remote connection with %@
FAILED to activate %{public}@ -> %{public}@ : %{public}@
CA tasking results: %@
Forcing preservation of sysdiagnose or diagnostic pipeline log: %{public}@
no outstanding jobs; releasing transaction
Got unexpected xpc message from %s: %s\n
Failed to copy UDID property from remote device.
Parameters file not available.
request expiration event; releasing transaction
request %@ (%@) enroute
Unable to fetch identifier from remote bridge.
Submission Result: %{public}@ after %u job(s), elapsed time %.2f s
Browser was canceled
----- '%{public}@' -----
canceling remote connection for %@.
Error loading parameters from Trial.
finished transferring %u logs successfully (%u rejected, %u errors) for job %@
no handler installed?
nothing to do for %@-%@
ERROR: PCCEndpoint::sendMessage: doesn't do anything
incoming connection from %s is DOWN
Trial is not available on this platform.
Including diagnostic pipeline logs in log list
%@ tasking key is %@
unable to package %@
Including sysdiagnoses in log list
sendMessage FAILED for %@: %@
Registering connection to remote device: %@
starting bogus request; wait for expiration in %.1f mins
sent %@, tracking: %@
Could not safely open submission results path: %@
'%@' posting content of %lu bytes from %lu logs
overwriting file at %{public}@
Got a NULL UUID; remote device may not be connected.
Failed to validate CA tasking file: first line was not valid JSON
Requesting tasking for routing %{public}@ using key %{public}@ with task_id %{public}@
%s
%@ is already in interruped state; passing
Not including diagnostic pipeline logs in log list: DiagnosticRequest framework unavailable on current platform
FAILED untrusted filename validation '%{public}@'
Failed to read tasking payload at %@: %@
request %@ (%@) complete %@
Event publisher for stream '%s' registered subscriber with token %llu
device is already in the correct %@ investigation
Error loading parameters: %{public}@
Initializing event publisher with stream %s
Submission archive too big (> %u) for submission with file %@
failed to get xattr value for key: %s
declining job %{public}@; group transfer already in progress (%{public}@)
requestTimeout set to %.0f secs
remote ProxiedDevice connected
Failed to get the root submission path.
%@ is not in interruped state; passing
%@ for device %@: model=%{public}@ productVersion=%{public}@ -> %{public}s
request %@ (%@) sent
relaying progress for job %{public}@: %ld / %ld bytes
Event publisher for stream '%s' received unknown event '%u'
IDS(%@) connected with %d accounts and %d devices
da3 tasking results: %@
Setting %@=%@ xattr on %@
Failed to set proxied device ID xattr on %@
unable to create xpc file xfer object for %{public}@
config: %@\npolicy: %@
Signature on blob is not trusted, %@
updateProxiedDeviceMetadata:\n%@
Missing expected completion handler.
failed to decode xattr value for key: %@
ignoring %{public}@ during Opt-OUT
Device '%s' in connected state; attempting to establish service
file send failure, abandoning job: %@
jobTimeout set to %.0f secs
starting job %{public}@, transfer group '%@'
file status update %@
Received unexpected reply message from %@: %s
Submission archive too big (> %u) for submission with preface
received message '%@'
Browser found %s-%s: %s
Error establishing connection to osanalyticshelper.
failed to write results file, saving as txt
updated staged tasking %@ '%@ <- %@'
no staged tasking %@
Failed to transfer log file at %@, error: %s
job expiration event; releasing transaction
received jobProgress for %{public}@: %lld / %lld
Submission jobs will include additional request headers %{public}@
unknown payload format for ca1 routing
IDS(%@) connected with no accounts.
%@
failed to write tmp remote file: [%d] %s
Event publisher XPC error: %d
A bundle ID is required to evaluate the stability of a single process.
received request %@-%@ '%@'
'%@' payload %ld, metadata: %@
Failed to get the data vault submission path.
received file '%@'
Remote device was NULL
No identifier for %@ because there are no outgoing connections.
OSADeviceRecoveryEnvHelper
PCCBridgeEndpoint
OSASubmissionPolicy
NSURLSessionDelegate
NSObject
PCCProxiedDevice
PCCExtension
OSAEventPublisher
OSASubmitter
PCCGroupJob
PCCRequest
OSASyncProxyServices
OSASubmitterExtension
NSURLSessionDataDelegate
OSASyncProxyHandler
OSAStreamDeflater
PCCUtilities
IDSServiceDelegate
OverrideMountPathRequest
NSSecureCoding
NSCoding
PCCEndpoint
NSURLSessionTaskDelegate
PCCIDSEndpoint
PCCJob
OSASyncProxyCallbacks
PCCProxyingDevice
NSXPCListenerDelegate
OSAHttpSubmitter
OSAEphemeralLog
_preserveFiles
arrayWithObjects:count:
hasTasking
initWithMessage:options:
service:account:inviteReceivedForSession:fromID:
T@\"NSString\",R,V_jid
bytes
fileHandleForReadingFromURL:error:
isWhitelisted:forDomain:
_rejected_count
name
service:account:receivedGroupSessionParticipantUpdate:
tokensLock
_response
initWithID:forTarget:options:forFile:
service:linkedDevicesChanged:
set
initWithFileDescriptor:closeOnDealloc:
shouldSubmitRouting:
T@\"NSDictionary\",R,V_options
attributesOfItemAtPath:error:
self
sendResourceAtURL:metadata:toDestinations:priority:options:identifier:error:
service:account:receivedGroupSessionParticipantDataUpdate:
setExportedObject:
setObject:forKey:
URLSession:dataTask:didReceiveData:
_recordRetirement:reason:
cancel
setRemoteObjectInterface:
_jobTimeout
_lastTouch
metadata
removeItemAtURL:error:
fileURLWithPathComponents:
isActive
request:transferLog:withOptions:onComplete:
taskingNeedsRefreshForRouting:at:
allKeys
_error_count
_txn
addSuiteNamed:
exitInterruptedStateFrom:
fileModificationDate
lastPathComponent
transferProgressForFilePath:sentBytes:totalBytes:
runWithDelegate:
URLSession:dataTask:didBecomeDownloadTask:
_delegate
_responseError
initialBarrierReceived
jobTimeout
performSelector:
receivedReport:from:metadata:
bugType
_package
_primary_template
data
initWithUUIDString:
preserveFiles
stashCrashReporterKeyForIdentifier:
URLSession:didBecomeInvalidWithError:
defaultManager
description
initiate:transferGroupWithOptions:job:
lastTouch
pathSubmission
removeObjectAtIndex:
service:account:identifier:hasBeenDeliveredWithContext:
_serviceByDevice
_sync_proxy_queue
allowUnsignedBlobs
boolForKey:
init
isConnected
service:account:incomingMessage:fromID:
startTimer
respondsToSelector:
_fileTimeout
getXattrBoolValWithName:at:
handleConnection:from:
initWithTemplate:options:
numberWithInteger:
stringByReplacingOccurrencesOfString:withString:
assembleMetadataAt:withOptions:
TB,V_allowUnsignedBlobs
ack:result:error:
path
scanLogs:from:
setLength:
stringByAppendingString:
URLSession:dataTask:willCacheResponse:completionHandler:
numberWithBool:
dictionaryWithContentsOfFile:
expire_count
service:account:inviteReceivedForSession:fromID:withContext:
updateTaskingLastSuccessfulRequest:at:
URLSession:task:needNewBodyStreamFromOffset:completionHandler:
_responseHeaders
_thoughput_warnings
deviceForTarget:
errorWithDomain:code:userInfo:
fileSystemRepresentation
lock
performSelector:withObject:withObject:
sharedInstance
_requestTimeout
closeFileStream
performSelector:withObject:
_outgoingConnections
_prefaces
compare:options:
overrideMountPath
packageLog:forRouting:info:options:
sendDeviceMetadata:
T@\"NSMutableDictionary\",R,V_scanOptions
_total_count
firstObject
propertyListWithData:options:format:error:
result
abort
interfaceWithProtocol:
isOnDeviceLogType:
dataWithContentsOfURL:options:error:
endpointToString:
doWork:
addRequest:event:type:onComplete:
generateLogList:
optInApple
setWantsProgress:
_target
T@\"NSSet\",N,C
getUUIDBytes:
setExportedInterface:
recoveryModeReason
registerRouting:result:
retire:
_expiryTimer
isKindOfClass:
service:account:receivedGroupSessionParticipantUpdate:context:
supportsSecureCoding
sysdiagnoseRoot
code
diagnosticResultsEvent:type:result:
identifier
request:logListWithOptions:onComplete:
scanLogs:from:options:
setInternalWhitelist:
temporaryFileWithPrefix:fd:
_options
_pairedWatchService
initFromPath:
initWithCapacity:
initWithService:
retainCount
userInfo
T@\"NSDictionary\",C,V_launchInfo
T@\"OS_xpc_event_publisher\",N,R,Vpublisher
URLByAppendingPathExtension:
_listeningConnection
_requestURL
_setQueue:
initWithCoder:
setHTTPShouldHandleCookies:
class
countByEnumeratingWithState:objects:count:
deliver:taskingFile:routing:taskId:asMessage:overRSD:
numberWithUnsignedInt:
setJobTimeout:
setupOutgoingConnection:
up_count
_job_queue
service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:
sessionWithConfiguration:delegate:delegateQueue:
setValue:forKey:
_default_template
T@\"NSString\",?,R,C
osTrain
_request_queue
isInDeviceRecoveryEnvironment
startPublisher
TB,V_wantsProgress
_event
_tasking_summary
finish:target:event:type:result:
service:activeAccountsChanged:
T@\"NSArray\",C,V_internalWhitelist
URLSession:task:didReceiveInformationalResponse:
scanOptions
timeIntervalSinceReferenceDate
_metadata
pathWithComponents:
proxyTasking:taskId:usingConfig:fromBlob:
_clientConnection
T@\"NSLock\",N,R,VtokensLock
processJob:forRouting:including:usingConfig:taskings:summarize:additionalRequestHeaders:
setCallback:
setHTTPMethod:
initWithSandboxExtensions:
writeToFile:atomically:
appendBytes:length:
getAvailableTaskingRoutings
numberWithDouble:
writeData:error:
URLSession:task:didFinishCollectingMetrics:
array
getXattrWithName:at:
intValue
logDomain
T@\"OS_dispatch_semaphore\",N,R,VinitialBarrierReceived
URLWithString:
acceptTaskingPayload:forRouting:withId:
crashReporterKey
removeItemAtPath:error:
sendMessage:toDestinations:priority:options:identifier:error:
service:account:incomingUnhandledProtobuf:fromID:context:
setAllowUnsignedBlobs:
TB,R,V_hasTasking
decodeArrayOfObjectsOfClass:forKey:
handleFile:from:metadata:
isSupportedRemoteDeviceType:
T@\"NSArray\",R,V_deviceIds
autorelease
dataWithContentsOfFile:
filePath
listDevices:
listener:shouldAcceptNewConnection:
subscriberTokens
fileTimeout
floatValue
isSysdiagnose:
appleInternal
finishRequestWithMessage:result:
processSubmissionJobs:usingConfig:summarize:
_connectionType
_results
accounts
copy
TB,R
T@\"NSString\",R,C
_dataTask
recordEvent:with:
startRequest:message:callerConnection:onComplete:
_errObj
cheaterTaskingWithSets:usingConfig:resultsCallback:
fileExistsAtPath:isDirectory:
finishRequest:result:
requestProxyMetadata:onComplete:
service:account:incomingMessage:fromID:context:
standardUserDefaults
URLSession:didReceiveChallenge:completionHandler:
prepConfig:
Td,V_jobTimeout
_capViolation
initWithPath:forRouting:usingConfig:options:error:
initiate:transferLog:withOptions:job:
remoteDeviceForIdentifier:
getFilenames
removeObjectForKey:
stream
getResourceValue:forKey:error:
handleMessage:from:
stringByStandardizingPath
UDIDForRemoteDevice:
_interruptedDevices
service:account:incomingPendingMessageOfType:fromID:context:
service:didSendOpportunisticDataWithIdentifier:toIDs:
defaultSessionConfiguration
wantsProgress
T@\"NSString\",R,V_target
UUIDString
_allowOptOutByRouting
_filePath
dataWithPropertyList:format:options:error:
isEqual:
service:account:incomingResourceAtURL:fromID:context:
setIgnoreProxies:
_reqById
currentConnection
dictionary
levelForFactor:withNamespaceName:
retain
setNetworkServiceType:
taskingLastSuccessfulRequest
uniqueID
T@\"NSDictionary\",R
service:account:inviteDroppedForSessionID:fromID:context:error:
initWithSuiteName:
locateLog:forRouting:usingConfig:options:error:
productVersion
productVersionForDevice:
URLSession:task:willBeginDelayedRequest:completionHandler:
appendData:
nextFilepath
containsObject:
addObject:
objectForKey:
setHTTPBody:
URLSessionDidFinishEventsForBackgroundURLSession:
_content
file_count
isCloudConnected
sandboxExtensions
isDeviceNearby:
stringByAppendingPathExtension:
statusCode
submitToUAT
synchronize:withOptions:onComplete:
JSONObjectWithData:options:error:
_callback
debugDescription
numberWithLongLong:
setValue:forHTTPHeaderField:
submissionsDisabled
_payload
_submissionSem
_wantsProgress
mutableCopy
registerResult:error:
T@\"NSString\",R,V_type
modelIdentifier
_consecutive_error_count
_sandboxExtensions
dictionaryWithDictionary:
modelIdentifierForDevice:
service:account:incomingOpportunisticData:withIdentifier:fromID:context:
persist
UTF8String
_internalWhitelist
_strm
encodeObject:forKey:
service:account:identifier:sentBytes:totalBytes:
_success_count
dataWithJSONObject:options:error:
modelCode
service:didSwitchActivePairedDevice:acknowledgementBlock:
_in
_reqByTracker
publisher
TB,V_ignoreProxies
options
addObjectsFromArray:
ignoreProxies
initWithUUIDBytes:
installCATasking:withId:untasked:
isEqualToString:
request_count
_device_browser
_accumulateKey:value:
_homeDeviceService
_identifier
isDiagnosticPipelineLog:
target
requestWithURL:cachePolicy:timeoutInterval:
buildVersion
prefaceSubmission:withData:usingArchive:andHeaders:
service:didCancelMessageWithSuccess:error:identifier:
service:nearbyDevicesChanged:
type
validateFirstLineAsJSON:
stringWithUTF8String:
_dryRun
Td,V_requestTimeout
count
generateSensorDataLog
submitLogsUsingPolicy:resultsCallback:
superclass
T@\"NSXPCConnection\",W,V_clientConnection
applyTasking:taskId:usingConfig:fromBlob:
initWithEndpoint:
internalWhitelist
numberWithUnsignedInteger:
_groupXferJob
currentTaskingIDByRouting
fileExistsAtPath:
remoteObjectProxyWithErrorHandler:
stringByDeletingLastPathComponent
_ignoreProxies
_responseCode
dictionaryWithContentsOfURL:error:
send:file:metadata:error:
submissionParam:
.cxx_destruct
_allowUnsignedBlobs
_jid
encodeWithCoder:
initWithData:andMetadata:
isMemberOfClass:
request:logList:
set_usesNWLoader:
_remoteDevices
latestResults
_sync_summary
applyTasking:taskId:fromBlob:
callback
clientConnection
createRetiredDirectoriesForUser:
moveItemAtPath:toPath:error:
setConnectionType:
extractAuthenticatedBlob:error:
identifierForTarget:
pathExtension
setPreserveFiles:
setupIncomingEventListener
submissionPathsWithHomeDirectory:withProxies:
_jobCount
addDelegate:queue:
diagnosticPipelineRoot
domain
service:connectedDevicesChanged:
setObject:forKeyedSubscript:
_specific_files
connectionForIdentifier:
filepath
conformsToProtocol:
event
primarySubmissionPaths
removeObject:
serviceByDeviceID:
stringByDeletingPathExtension
allHeaderFields
cancelCurrentTask
longLongValue
numberWithInt:
TI,V_fileTimeout
URLSession:dataTask:didBecomeStreamTask:
URLSession:dataTask:didReceiveResponse:completionHandler:
URLSession:task:needNewBodyStream:
_initializationQueue
capViolation
deviceIds
doubleValue
_endpoint
allValues
identifierForRemoteDevice:
iterateLogsWithOptions:usingBlock:
postContent:withHeaders:toEndpoint:
setRequestTimeout:
setXattrWithName:value:at:
arrayWithArray:
_deviceIds
_responseData
launchInfo
productBuildVersion
initWithStream:
writeToFile:atomically:encoding:error:
pathDiagnostics
resume
setLaunchInfo:
sendEventToSubscribers:waitForReplies:
serviceAllowedTrafficClassifiersDidReset:
startService:
isLocallyPaired
hasPrefix:
releaseSandboxExtensions
service:account:identifier:fromID:hasBeenDeliveredWithContext:
_remoteCRKeys
job_count
request:transferGroupWithOptions:onComplete:
valueForKey:
readDataOfLength:
_jobByTracker
handleSubscriptionEventWithAction:token:descriptor:
setSubscriberTokens:
T@,R
fileURLWithPath:
overrideMountPath:
prepareNext
stringWithFormat:
transferProgress:sentBytes:totalBytes:
T@\"NSString\",R
isDefaultPairedDevice
setWithObject:
T@\"NSArray\",R,V_sandboxExtensions
stringByAppendingPathComponent:
_launchInfo
_loadPreviousResults
_scanOptions
_type
URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:
date
setCapViolation:
service:account:identifier:didSendWithSuccess:error:context:
targetAudience
dealloc
URLSession:task:didReceiveChallenge:completionHandler:
_group_type
ensureUsablePath:component:options:
initWithID:forTarget:options:
markFile:withKey:value:
metaData
msg_count
T@?,C,V_callback
enterInterruptedStateFrom:
finishTasksAndInvalidate
taskingKeyForRouting:withConfig:
timeIntervalSinceNow
zone
URLSession:didCreateTask:
unlock
URLSession:taskIsWaitingForConnectivity:
dictionaryWithObjects:forKeys:count:
getAdditionalRequestHeaders
hash
devices
TB,V_capViolation
_last_thoughput_check
_out
addSenderToMessage:
arrayByAddingObjectsFromArray:
closeFile
service:account:inviteReceivedForSession:fromID:withOptions:
enumerateKeysAndObjectsUsingBlock:
send:message:error:
service:account:incomingResourceAtURL:metadata:fromID:context:
synchronize:withOptions:
service:devicesChanged:
T@\"NSString\",N,R
_eventQueue
_log_sets
connectionType
service:account:identifier:didSendWithSuccess:error:
timeIntervalSince1970
UUID
addEntriesFromDictionary:
arrayWithCapacity:
numberWithLong:
setFileTimeout:
_hasTasking
boolValue
fastLane
setClientConnection:
updateProxiedDeviceMetadata:from:
cleanupRetired:
request:transferLog:onComplete:
T@\"NSDictionary\",R,V_metadata
release
clientWithIdentifier:
isFilenameReasonable:
localizedDescription
removeAllObjects
isNearby
scanProxies:
setupDeviceStateChangeHandler
service:account:didReceiveLocalNetworkHandshake:fromID:context:
jid
buildSubmissionTemplateForConfig:
componentsJoinedByString:
copyDeflatedDataFromStream:withCap:
diagnosticPipelineLogs
fileValue
releaseType
T#,R
length
removeObjectsForKeys:
request:generateTransparencyLogs:
service:account:incomingData:fromID:context:
requestTimeout
T@\"NSString\",C,V_connectionType
T@\"NSDate\",R,V_lastTouch
dataTaskWithRequest:
isDataVaultEnabled
TQ,R
URLSession:task:didCompleteWithError:
isProxy
T@\"NSString\",R,V_event
serviceSpaceDidBecomeAvailable:
acceptTaskingFile:forRouting:withId:
initWithBytes:length:encoding:
objectForKeyedSubscript:
summarizeLog:reason:
T@\"NSString\",R,V_filePath
TB,V_preserveFiles
URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:
pathSubmissionDataVault
pathComponents
v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32
@\"NSXPCConnection\"
@24@0:8:16
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40
B20@0:8I16
@\"OS_xpc_remote_connection\"
v56@0:8@\"NSString\"16@\"NSURL\"24@\"NSString\"32@\"NSString\"40B48B52
@24@0:8@16
Vv16@0:8
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32
v20@0:8I16
v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44
v24@0:8@\"IDSService\"16
v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36
v40@0:8@\"NSString\"16q24q32
@\"NSArray\"
Q16@0:8
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56
@\"PCCEndpoint\"
B32@0:8@16@24
v24@0:8@16
?
v28@0:8@16B24
@\"NSURLSessionDataTask\"
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48
@\"IDSService\"
@\"NSObject<OS_dispatch_queue>\"
v24@0:8d16
@\"NSObject<OS_os_transaction>\"
v24@0:8@?<v@?@@\"NSError\">16
v20@0:8B16
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40
v32@0:8@\"IDSService\"16@\"NSSet\"24
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56
@\"OS_xpc_event_publisher\"
@\"NSLock\"
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32
@\"NSHTTPURLResponse\"
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48
@\"NSObject<OS_dispatch_source>\"
v28@?0I8Q12@\"<OS_xpc_object>\"20
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48
v36@0:8@16@24i32
@\"NSString\"16@0:8
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48
@\"NSObject<OS_dispatch_semaphore>\"
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56
@\"NSMutableDictionary\"
v32@0:8@16q24
v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32
@24@0:8@\"NSCoder\"16
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
d
@28@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16I24
v32@0:8@\"IDSService\"16@\"NSArray\"24
v32@0:8@\"NSString\"16@?<v@?@@\"NSError\">24
i28@0:8@16B24
v24@0:8@\"NSCoder\"16
v48@0:8@16@24q32@?40
v36@0:8@\"NSString\"16B24@\"NSError\"28
d16@0:8
B
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32
v64@0:8@16@24@32@40@?48@56
v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48
v32@0:8@16@?24
v24@0:8r*16
v52@0:8@16@24@32B40@44
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@@\"NSError\">32
v12@?0i8
@\"NSMutableSet\"
v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32
v60@0:8@16@24@32B40@44@52
v48@0:8@16@24@32@?40
I16@0:8
v44@0:8@16B24@28@36
@16@0:8
v56@0:8@16@24@32@40@?48
@32@0:8:16@24
B24@0:8@\"Protocol\"16
@\"<OSASyncProxyHandler>\"
v36@0:8I16Q20@28
B32@0:8@16d24
@28@0:8@16B24
@\"NSMutableData\"
{z_stream_s=\"next_in\"*\"avail_in\"I\"total_in\"Q\"next_out\"*\"avail_out\"I\"total_out\"Q\"msg\"*\"state\"^{internal_state}\"zalloc\"^?\"zfree\"^?\"opaque\"^v\"data_type\"i\"adler\"Q\"reserved\"Q}
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40
@72@0:8@16@24@32@40@48@56@64
q
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40
v24@0:8@?16
@?
v64@0:8@16@24@32@40@48@56
@\"NSDate\"
v40@0:8@16q24q32
B24@0:8#16
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32
v56@0:8@16@24@32q40q48
v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52
v48@0:8@16@24@32@40
@56@0:8@16@24@32@40^@48
#16@0:8
B24@0:8:16
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48
@\"OS_remote_device_browser\"
B16@0:8
@32@0:8@16^@24
@40@0:8@16@24^@32
@48@0:8@16@24@32^@40
v52@0:8@16@24B32@36@44
v28@0:8B16@\"NSString\"20
i
v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24
@\"NSDictionary\"
v32@0:8@16@24
@48@0:8@16@24@32@40
@\"OSALog\"
v36@0:8@16B24@28
v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@@\"NSError\">32
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48
v40@0:8@16@24@32
v40@0:8@16@24@?32
B24@0:8@16
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@@\"NSError\">40
@\"OS_dispatch_semaphore\"
v24@0:8@\"NSURLSession\"16
v56@0:8@16@24q32q40q48
*
v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40
v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32
@\"PCCGroupJob\"
@40@0:8@16@24@32
@\"NSMutableArray\"
v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40
v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48
@?16@0:8
v56@0:8@16@24@32@40B48B52
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
@20@0:8i16
v32@0:8@16d24
I
v56@0:8@16@24q32@40@48
v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44
@\"NSError\"
v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40
v40@0:8@\"NSURL\"16@\"NSString\"24@\"NSDictionary\"32
@40@0:8:16@24@32
v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48
v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48
@32@0:8@16@24
@\"NSString\"
v32@0:8@\"NSDictionary\"16@\"NSString\"24
@\"NSData\"
^{_NSZone=}16@0:8
v56@0:8@16@24@32@40@48
v28@0:8B16@20
v16@0:8
```
