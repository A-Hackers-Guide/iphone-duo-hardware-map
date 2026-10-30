# `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 959,760 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 4224)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9, weak)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/UserManagement.framework/UserManagement (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (32 classes, 4 protocols)

Classes: `NSDictionary`, `NSError`, `NSMutableDictionary`, `SUCore`, `SUCoreCodeCoverage`, `SUCoreConfig`, `SUCoreDevice`, `SUCoreDiag`, `SUCoreDiagPoint`, `SUCoreDiagStats`, `SUCoreErrorAttributes`, `SUCoreErrorInformation`, `SUCoreErrorLayerGroup`, `SUCoreEvent`, `SUCoreEventReporter`, `SUCoreEventReporterActive`, `SUCoreEventReporterDelegate`, `SUCoreFSM`, `SUCoreFSMAttachedAction`, `SUCoreLog`, `SUCoreMAIdentifier`, `SUCorePSUSArguments`, `SUCorePSUSPlugin`, `SUCorePSUSResult`, `SUCorePersistedState`, `SUCoreProgress`, `SUCoreRestoreVersion`, `SUCoreSimulate`, `SUCoreSimulateEvent`, `SUCoreSplunkHistory`, `SUCoreStartup`, `SUCoreUUID`

Protocols: `NSCoding`, `NSObject`, `NSSecureCoding`, `NSURLSessionDelegate`

## Strings (3,263)

First 2,500 of 3,263.
```
[SUCoreDevice] Build version comparison found current version %d, build version %d, isMinorOSUpdate: %{public}@
[PERSISTED_STATE] no data object present in secure coded object persisted state for key %{public}@ and type %{public}@
[SIMULATE] cannot clear events (simulator disabled)
[SUCoreConfig] Attempting to set config with key of unsupported class: %{public}@
[EVENT_REPORTER] CONFIG | dropEventsOnSendFailure=%{public}@
[EVENT_REPORTER] FLUSH | sending last error event
[EVENT_REPORTER] STATUS | sending event [event indicating error when no last error]
[PERSISTED_STATE] setting persisted state for key with object value: %{public}@=%{public}@
Unale to get NSPrincipalClass from bundle info at: %@
[SIMULATE] PERFORM(OFF_QUEUE) - pausing until stop file(%@) has been deleted (running on queue %@)...
[SIMULATE] PERFORM(OFF_QUEUE) - sleeping for %d second%@...
[PERSISTED_STATE] loaded persisted state: %{public}@
[SUCoreDevice] RemoteServiceDiscovery indicates that this is not a bridgeOS device (initializeBridgeOSProperties)
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ - resuming | active:%{public}@
attempting to remove persisted state with summary: %{public}@
[SIMULATE] cannot provide count of alterations (simulator disabled)
...%{public}@ (%{public}@) | SUCCESS
[DIAG_ERROR] ERROR: unable to load encoded data from dump file: %{public}@
[SIMULATE] PERFORM(OFF_QUEUE) - ...pausing [stop file(%@) has been deleted]
[SIMULATE] using updateInfoPlist: '%@'
[SUCoreDevice] Unable to determine SFR restore version (sfrRestoreVersion=%{public}@, sfrRestoreBuildGroup=%{public}@)
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ [ERROR] - dropping | active:%{public}@
[FSM] DUMP_EVENT_IN_STATE | %@:FSM(%@) | STATE(%@) EVENT(%@) ACTION(%@) | occurrences:0
[SIMULATE] using assetAttributesPlist: '%@'
[SUCoreDevice] Using preservedFactoryVersionPlistPath: %{public}@
[FSM] DUMP_EVENT_IN_STATE | %@:FSM(%@) | STATE(%@) EVENT(%@) ACTION(%@) | occurrences:%llu
[SUCoreCodeCoverage] Unable to create output directory: '%{public}@'
[SUCoreDevice] sysctlbyname failed for key %{public}@ with code %d (%s) buffer size %ld
[%{public}@]%{public}@... (%{public}@)
[DIAG_END] ...[%{public}@]%{public}@ | result=%ld error:%{public}@
[EVENT_REPORTER] SYNCHRONIZING | ...getAllTasksWithCompletionHandler | %lu in-flight event%@
[EVENT_REPORTER] SYNCHRONIZING | ignoring NSURLSession task for fileUUID:%{public}@, state:%{public}@ - no longer on the filesystem | active:%{public}@
[FSM] REGISTER_EVENT: FSM(%{public}@) attached action(%{public}@) handling event(%{public}@) in state(%{public}@)
[SIMULATE] PERFORM(OFF_QUEUE) - ...sleeping
[SUCoreCodeCoverage] Unhandled signal: %d (ignored)
[SUCoreDevice] sysctlbyname failed to set buffer for key %{public}@ with code %d (%s) buffer size %ld
[SPLUNK_HISTORY] SETUP | failed opening new log file, errno:%d
[SUCoreDevice] Build version comparison was not provided a build version
[SUCoreDevice] RemoteServiceDiscovery indicates that this is a T1 bridgeOS device via REMOTE_DEVICE_TYPE_EOS (initializeBridgeOSProperties)
...[%{public}@]%{public}@ (%{public}@) | SUCCESS
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ [SUCCESS] - considering done | active:%{public}@
Error: %@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a SplatVersion value
[SIMULATE] cannot adopt event alterations (simulator disabled)
[SIMULATE] PERFORM #%d - %@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a gestalt key
incrementErrorCount when event does not represent an error (no result)
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ [ERROR] - will retry | active:%{public}@
[SUCoreCodeCoverage] Signal handler received SIGUSR1, dumping code coverage
[PERSISTED_STATE] setting persisted state for key with dictionary value: %{public}@=%{public}@
[SUCoreDevice] Using recoveryOSSystemVersionPlistPath: %{public}@
[SIMULATE] syntax error: assetBuildVersions and assetProductVersions must both be defined
[SIMULATE] dump all events - empty simulate events
[SUCoreConfig] Attempting to set config with no defaults path present
[SUCoreDevice] Using splatSystemVersionPlistPath: %{public}@
[DIAG_FAULT] FAULT:%{public}@, result=%ld
[PERSISTED_STATE] encode class name mapping skipped: class %{public}@ not found for coded name %{public}@
[PERSISTED_STATE] persisting the state %{public}@
[SUCoreConfig] Attempting to set unsupported class to configuration file: %{public}@
[SUCoreDevice] Checking if rollback objects are present in preboot at path: %{public}@, exists: %{public}@, isDir: %{public}@
[SUCoreConfig] Failed to write config to defaults path with error: %{public}@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a SplatCryptex1 value
...[%{public}@]%{public}@ | SUCCESS
[DIAG_ERROR] ERROR: failed to unarchive encoded data from dump file: %{public}@, error: %{public}@
[DIAG_ERROR] ANOMALY: [%@] could not remove pre-existing dump file: %{public}@, error: %{public}@
[PERSISTED_STATE] attempting to load persisted state, but state is already loaded - no operation to perform
[SUCoreDevice] RemoteServiceDiscovery methods are not available on this platform (initializeBridgeOSProperties)
[SUCoreDictionary] key '%{public}@' is invalid value: %{public}@, returning default value
[EVENT_REPORTER] INIT(v1.0) | storing to path: %{public}@, access control: %{public}@
[SUCoreDevice] Failed to get path to rollback objects: %{public}@
[DIAG_ERROR] %{public}@: %{public}@, reason=%{public}@ result=%ld error:%{public}@
[EVENT_REPORTER] UMUserManager class does not respond to selector 'sharedManager'
[SUCoreDevice] Unable to determine RecoveryOS restore version (recoveryOSRestoreVersion=%{public}@, recoveryOSRestoreBuildGroup=%{public}@)
[PERSISTED_STATE] setting persisted state for key with data value: %{public}@=%{public}@
[SUCoreDevice] Using factoryVersionPlistPath: %{public}@
[SUCoreDevice] Unsupported query key %{public}@ to reload plist contents
[SUCoreDictionary] key '%{public}@' references value of the incorrect class (%{public}@), returning %{public}@ value: nil
[EVENT_REPORTER] SYNCHRONIZING | no events to retry
[SUCoreDevice] No system volume provided, returning
[SUCoreDevice] Unsupported query key %{public}@ to obtain factory version plist contents.
%{public}@...
[EVENT_REPORTER] STATUS | send events with nothing to send
[SUCoreCodeCoverage] Signal handler received SIGUSR2, resetting code coverage
[SUCoreDevice] Using splatCryptex1RestoreVersionPlistPath: %{public}@
[EVENT_REPORTER] UPLOADING | dropping event with fileUUID:%{public}@ - too many send attempts | active:%{public}@
[EVENT_REPORTER] SYNCHRONIZING | aligning fileUUID:%{public}@ - no longer on filesystem, dropping | active:%{public}@
Unable to create bundle from: %@
[DIAG_FAULT] FAULT:%{public}@, reason=%{public}@ result=%ld
[PERSISTED_STATE] loading persisted state with summary: %{public}@
[PERSISTED_STATE] removing persisted state dictionary for key: %{public}@
[SIMULATE] dump all events - no simulate events
[SPLUNK_HISTORY] acquireSharedLock | failed opening lock file, errno:%d
[RestoreVersion] (%{public}@) Parse: second order split result was not as expected (expected 5 values): %{public}@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a factory version key.
[SPLUNK_HISTORY] SETUP | failed opening log file, errno:%d
[SIMULATE] cannot dump events (simulator disabled)
[SPLUNK_HISTORY] WRITE | wrong format for event UUID %@
[PERSISTED_STATE] setting persisted state for key with date value: %{public}@=%{public}@
[SUCoreDevice] Using recoveryOSRestoreVersionPlistPath: %{public}@
[SUCoreConfig] ClearConfig: Configuration file does not exist at path: %{public}@
[SUCoreDevice] Using systemVersionPlistPath: %{public}@
[SUCoreDictionary] [%{public}@] key '%{public}@' (%{public}@) references value of the incorrect class (%{public}@), returning %{public}@ value: nil
[EVENT_REPORTER] SYNCHRONIZING | retrying (recovered from storage), re-sending fileUUID:%{public}@ | active:%{public}@
[SIMULATE] failed parsing 'startAt' (expected int) for: '%@'
[SUCoreDevice] Build version comparison was unable to find a build regex match for %{public}@
[SIMULATE] dump all events - %@
[SUCoreDevice] Unsupported query method %{public}@ attempted for key %{public}@
...%{public}@ | SUCCESS
[DIAG] DUMP_HISTORY[%04lu]: %{public}@
[EVENT_REPORTER] UPLOADING | sending [UUID: %{public}@] file: %{public}@ payload: %{public}@
[RestoreVersion] (%{public}@) Parse: invalid tuple value string found: %{public}@
[DIAG_END] ...[%{public}@]%{public}@ (%{public}@) | result=%ld error:%{public}@
[EVENT_REPORTER] IDLE_TRACK | decrement active - activeSendTaskCount:%d, awaitingRetry:%lu
[SIMULATE] PERFORM #%d - causing fault: %@
[SUCoreDevice] Using sfrRestoreVersionPlistPath: %{public}@
[SUCoreConfig] ClearConfig: Failed to remove configuration at path '%{public}@': %{public}@
[PERSISTED_STATE] attempting to load encoded data for key %{public}@ with classes: %{public}@
[SUCoreConfig] Successfully updated config at path '%{public}@': %{public}@
[PERSISTED_STATE] returning persisted policy version with string value: %{public}@
[SIMULATE] failed parsing tokens (unexpected format, expected 'key=value') for: '%@'
[SUCoreCodeCoverage] Code coverage is disabled (SUCore not running in debug)
[SUCoreDevice] Using splatRestoreVersionPlistPath: %{public}@
[DIAG_ERROR] DUMP_LOSS: unable to create event to report
[EVENT_REPORTER] FLUSH | sending first awaiting retry
[EVENT_REPORTER] SEND_FINISHED | FAILURE | event for fileUUID:%{public}@ failed to be sent (dropped) | active:%{public}@
[EVENT_REPORTER] SEND_FINISHED | FAILURE | event for fileUUID:%{public}@ failed to be sent (will retry) | active:%{public}@
[SPLUNK_HISTORY] SETUP | failed creating file name
[SPLUNK_HISTORY] SETUP | failed moving old file, errno:%d
[EVENT_REPORTER] UPLOADING | retrying, re-sending fileUUID:%{public}@ | active:%{public}@
[SPLUNK_HISTORY] acquireSharedLock | failed creating file lock
[SPLUNK_HISTORY] WRITE | failed writing event UUID %@, errno:%d
[PERSISTED_STATE] removing persisted state object for key: %{public}@
[TRANSACTION] END   with domain %{public}@ (transaction=%{public}@)
[SPLUNK_HISTORY] WRITE | Wrote UUID %{public}@
[SIMULATE] failed parsing 'duration' (expected int) for: '%@'
[DIAG] dump tracked with reason=%{public}@ dumpToMask=%{public}@ filename=%{public}@ clearStatistics=%{public}@ clearHistory=%{public}@
Unable to create class from: %@
[SUCoreDevice] Using appleInternalVariantPlistPath: %{public}@
[SUCoreDevice] Using splatCryptex1SystemVersionPlistPath: %{public}@
[SUCoreDevice] Unsupported query key %{public}@
[SUCoreDictionary] [%{public}@] key '%{public}@' references value of the incorrect class (%{public}@), returning %{public}@ value: nil
[SUCoreDictionary] set with key = nil, no change to dictionary
[EVENT_REPORTER] SYNCHRONIZING | ...getAllTasksWithCompletionHandler | no in-flight events
[EVENT_REPORTER] SYNCHRONIZING | retrying events discovered on the filesystem
[SPLUNK_HISTORY] SETUP | failed to get file stats, errno:%d
[CORE_ERROR] {checkedIndicationsMatchingMask} error with depthCount=%d yet no stack-error at checked depth(%d) | cannot determine if generic failure for error: %{public}@
[SUCoreDevice] Failed to get path to cryptex1 RestoreVersion: %{public}@
[%{public}@]%{public}@...
[DIAG_ERROR] %{public}@: %{public}@, result=%ld error:%{public}@
[DIAG] DUMP_STATS:\n%{public}@
[RestoreVersion] (%{public}@) Parse: failed to parse int from string found: %{public}@
[SIMULATE] using assetState: '%@'
[SIMULATE] cannot dump events (no persisted state)
[SUCoreDevice] Using splatRollbackRestoreVersionPlistPath: %{public}@
[DIAG_FAULT] FAULT:%{public}@, reason=%{public}@ result=%ld error:%{public}@
[SUCoreDictionary] key '%{public}@' is invalid value: %{public}@, returning SUCoreTriStateNotSet
[SUCoreDictionary] key '%{public}@' is the incorrect class, returning %{public}@ default value: %{public}@
[ERROR_INFORMATION] layer group(%{public}@) already defined
[RestoreVersion] (%{public}@) Parse: invalid build group found: %{public}@
[PERSISTED_STATE] removing persisted state date for key: %{public}@
[SIMULATE] simulate event alterations file does not exist (file non-existent): %@
[SIMULATE] syntax error: assetBuildVersions (%lu) and assetProductVersions (%lu) must have the same count
[SUCoreDevice] Using splatRollbackSystemVersionPlistPath: %{public}@
[DIAG] DUMP_UUID: %{public}@
[DIAG_ERROR] DUMP_LOSS: unable to encode data for dump to file, error: %@
[EVENT_REPORTER] SYNCHRONIZING | ignoring NSURLSession task for fileUUID:%{public}@, state:%{public}@ - no longer on the filesystem
[PERSISTED_STATE] removing persisted state string for key: %{public}@
[SIMULATE] failed parsing option (unexpected/unsupported option key) for: '%@'
[TRANSACTION] BEGIN with domain %{public}@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a core services key
%{public}@... (%{public}@)
[EVENT_REPORTER] STATUS | sending event [event indicating successful operation]
[PERSISTED_STATE] created a new, empty persisted state dictionary: %{public}@
[SUCoreDevice] No system volume provided, returning no initialized device
[DIAG_END] ...%{public}@ (%{public}@) | result=%ld error:%{public}@
[EVENT_REPORTER] UMUserManager class does not exist.
[EVENT_REPORTER] SYNCHRONIZING | aligning encountered invalid key=value, dropped
[EVENT_REPORTER] SEND_FINISHED | SUCCESS (with error) | sent event (status=%ld) validated file: %{public}@, error: %{public}@
[RestoreVersion] (%{public}@) Parse: completed with result: %{public}@
[SIMULATE] failed parsing 'errorUserInfo' (expected {k1=v1;k2=v2;}) for: '%@'
non-nil currentOSType found with value of: %{public}@
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ - dropping | active:%{public}@
[PERSISTED_STATE] successfully removed persisted state file
[SIMULATE] failed parsing 'endAt' (expected int) for: '%@'
[SIMULATE] PERFORM(OFF_QUEUE) - unable to create stop file(%@)
[RestoreVersion] Compare: self=%{public}@ to=%{public}@ | result=%{public}@
[SUCoreDevice] Using restoreVersionPlistPath: %{public}@
%{public}@
nil currentOSType found, setting the currentOSType to: %{public}@
[SIMULATE] failed parsing 'errorCode' (expected SUCoreErrorCode) for: '%@'
[DIAG_ERROR] %{public}@: %{public}@, reason=%{public}@ result=%ld
[DIAG_STATS] DROPPED: dropping tracked statistics [%lld %{public}@ %{public}@ matched %{public}@]
[EVENT_REPORTER] SEND_FINISHED | SUCCESS | sent event (status=%ld) validated file: %{public}@
[EVENT_REPORTER] IDLE_TRACK | awaiting retrying - activeSendTaskCount:%d, awaitingRetry:%lu
Unable to load plugin from: %@, error: %@
[SUCoreDevice] Using sfrSystemVersionPlistPath: %{public}@
[SUCoreDevice] Failed to get path to cryptex1 SystemVersion: %{public}@
[SUCoreDevice] Failed to get path to rollback assets
[SUCoreDevice] Unsupported query key %{public}@ to obtain a SplatVersion/SplatRollbackVersion/SplatCryptex1Version value
[PERSISTED_STATE] returning persisted contents type with string value: %{public}@
[PERSISTED_STATE] no persisted state file found at persistence path
[RestoreVersion] (%{public}@) Init: failed to create a valid parsed restore version from string %{public}@
[RestoreVersion] (%{public}@) Parse: first order split result was not as expected (expected 2 values): %{public}@
[SIMULATE] failed parsing 'errorRecoverable' (expected SUCoreSimulateEventBoolean) for: '%@'
[SUCoreDevice] SystemRecoveryNSIH: Device does not support variable boot policy
[EVENT_REPORTER] STATUS | sending event [event indicating error that is different than last reported]
[EVENT_REPORTER] IDLE_TRACK | sending first awaiting retry - activeSendTaskCount:%d, awaitingRetry:%lu
[EVENT_REPORTER] SYNCHRONIZING | getAllTasksWithCompletionHandler... | synchronizing with NSURLSession to determine in-flight events
[RestoreVersion] Comparable: self=%{public}@ to=%{public}@ | valid=%{public}@
[SUCoreDevice] Build version comparison found current version %d, build version %d, isMajorOSUpdate: %{public}@
[SUCoreDevice] Semi-splat active: %{public}@ (%{public}@)
[SUCoreDevice] Unsupported query key %{public}@ to obtain a SplatRollback value
[CORE_ERROR] {checkedSystemPartitionSize} system partition size error attribute not yet implemented | cannot provide system partition size for error: %{public}@
[EVENT_REPORTER] STATUS | not sending event [event indicating error matching last reported]
Unable to load with nil path
[SUCoreDevice] Unsupported query key %{public}@ to obtain a sysctl value
[DIAG_END] ...%{public}@ | result=%ld error:%{public}@
[EVENT_REPORTER] SYNCHRONIZING | untracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ - ignored
[EVENT_REPORTER] IDLE_TRACK | %{public}@ - activeSendTaskCount:%d, awaitingRetry:%lu
[SUCoreConfig] Attempting to initialize with project name of an unsupported class: %{public}@
[ERROR_INFORMATION] changing attributes of error [%{public}@:%d(%{public}@)] when already have attributes for error [%{public}@:%d(%{public}@)] | new attributes ignored
[EVENT_REPORTER] SETUP | default Splunk URL: %{public}@
[EVENT_REPORTER] SYNCHRONIZING | ignoring NSURLSession task without appropriate description
[EVENT_REPORTER] IDLE_TRACK | not idle (%{public}@) - activeSendTaskCount:%d, awaitingRetry:%lu
[SUCoreConfig] ClearConfig: Successfully removed configuration at path: %{public}@
[SUCoreDevice] Initialized new device: %{public}@
[PERSISTED_STATE] returning persisted core version with string value: %{public}@
[SUCoreConfig] Attempting to initialize with defaultsPath of an unsupported class: %{public}@
[SUCoreDevice] Unsupported query key %{public}@ to obtain a restore version key
[EVENT_REPORTER] Detected shared iPad
[EVENT_REPORTER] ACTIVE | found active event for fileUUID:%{public}@ | activeEvent:%{public}@
[SPLUNK_HISTORY] INIT | failed to create history directory at path: %@, error: %@
[PERSISTED_STATE] setting persisted state for key with ULL value: %{public}@=%lld
[RestoreVersion] Init: failed to create restore version when no version string was provided
[SIMULATE] PERFORM - no simulated action: %@
[CORE_ERROR] {checkedIndications} error with depthCount=%d yet no stack-error at checked depth(%d) | cannot determine if generic failure for error: %{public}@
[DIAG_ERROR] ANOMALY: [%{public}@] could not create dump file: %{public}@
[SIMULATE] located event: %@ | valid=%@
[CORE_ERROR] {_checkedIndicationsMatching} error with depthCount=%d yet no stack-error at checked depth(%d) | cannot determine all indications for error: %{public}@
[SUCoreDevice] RemoteServiceDiscovery indicates that this is a T2 bridgeOS device via REMOTE_DEVICE_TYPE_BRIDGE_COPROC (initializeBridgeOSProperties)
[DIAG_ERROR] %{public}@: %{public}@, result=%ld
[DIAG_ERROR] ANOMALY: failed to create directory: %{public}@, error: %{public}@
[PERSISTED_STATE] removing persisted state data for key: %{public}@
[SIMULATE] cannot provide last alterations (simulator disabled)
[EVENT_REPORTER] ACTIVE | updated active event for fileUUID:%{public}@ | activeEvent:%{public}@
[SUCoreDictionary] key '%{public}@' (%{public}@) references value of the incorrect class (%{public}@), returning %{public}@ value: nil
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ - continuing | active:%{public}@
[EVENT_REPORTER] SYNCHRONIZING | aligning fileUUID:%{public}@ - on filesystem and persisted | active:%{public}@
[SIMULATE] using errorDomain: '%@'
[DIAG_FAULT] FAULT:%{public}@, result=%ld error:%{public}@
[DIAG_STATS] DROPPED: dropping tracked statistics [%lld %{public}@ matched %{public}@]
[EVENT_REPORTER] SYNCHRONIZING | tracked NSURLSession task for fileUUID:%{public}@, state:%{public}@ - awaiting didCompleteWithError | active:%{public}@
[SPLUNK_HISTORY] WRITE | failed writing complete event UUID %@
[SIMULATE] TRIGGER #%d - %@
[EVENT_REPORTER] UMUserManager instance does not respond to selector 'isSharedIPad'
[EVENT_REPORTER] IDLE_TRACK | now idle (%{public}@) - activeSendTaskCount:%d, awaitingRetry:%lu
[EVENT_REPORTER] SEND_FINISHED | FAILURE | event for fileUUID:%{public}@ failed to be sent (max retries) | active:%{public}@
[PERSISTED_STATE] setting persisted state for key with boolean value: %{public}@=%{public}@
[PERSISTED_STATE] setting persisted state for key with string value: %{public}@=%{public}@
[SIMULATE] adding event: %@
[SIMULATE] failed parsing line: %@
kSUCoreErrorConnectClientIsObserverOnly
clientId
ActiveEventsState
[EVENT_REPORTER] REMOVE
follow-up
SUCoreDeviceQueryKeySplatCryptex1ProductVersion
NetworkServer
kSUCoreErrorEventReporterSendFailed
|NVRAM Allowed:%@
%@[%@]
[%@(%@)] >S> %@ >E> %@ >A> %@ info:%@
kSUCoreErrorPSUSOptionalNoSpaceAllowed
batteryIsCharging
SystemVolume(TargetedSystemVolume:%@)
FSM
failureAllIndications
Personalization
kSUCoreErrorScanFailCanceling
[SIMULATED_ERROR] created by %@ (for domain=%@, code=%ld)
SUCoreDeviceQueryMethodRestoreVersion
installTonightArmed
Splat ProductVersionExtra (%@; %@) and Cryptex1 ProductVersionExtra (%@; %@) are not equal
SUCoreDeviceQueryKeySplatCryptex1BuildVersion
%@ <dictionary>:\n{>>>\n
kSUCoreErrorMSUPreviousUpdateStateFailed
kSUCoreErrorPSUSOptionalDisabledByServer
kSUCoreErrorSpaceInsufficient
[FSM] REGISTER_EVENT
BridgeOS
updateCancelled
preflightPrerequisiteCheck
DiscoveredCancelingCount
assetState
[%@:%@
kSUCoreErrorInvalidPolicyAssetType
NoOp
endAt
actionText
activity
scanInterval
callback [send %@ (status=%ld)] without file UUID - event file may be left on filesystem
targetOSBuild
failed to send event (status=%ld) validated file: %@
[FSM] API: registerAllActions
identityName
X
BuildVersion
date
kSUCoreErrorEventReporterNoResponse
kSUCoreErrorSpaceCacheDeletePurgeableFailed
assetAttributesPlist
RestoreLongVersion
hw.model
BATS_TESTPLAN_ID
fsmState
[%@(%@) %@] code:%ld error:%@ | checked(%ld)
MinorDelayPeriod
currentProductVersionExtra
FSM(%@) invalid state table
SoftwareUpdateServices
trackType:%@ location:%@ reason:%@ code:%ld error:%@ | checked(%ld)
|ANOMALY
preflightFDR
unknown archiving exception
[SIMULATE] cannot clear events (simulator disabled)
SUCoreDeviceQueryKeySplatRestoreVersion
failed to write JSON data to file [UUID: %@] file: %@
FSM(%@) start state not provided
errorDomain
 Build(BuildVersion:%@|ProductVersion:%@|RestoreVersion:%@)
|FSM
BatteryIsCharging
DEFAULT
sameErrorSignature
SUControllerError
Canceling
eventTime
DiscoveredSuspendedCount
adopt event alterations (already adopted)
SUCoreDeviceQueryKeySFRRestoreVersion
param
kSUCoreErrorSpaceNoAppOffloadPurgeableResults
lowPowerMode
taskDescription
errorCode
v32@?0@8@16^B24
kSUCoreErrorIgnoredParam
kSUCoreErrorLoadfailed
preflightPersonalize
[FSM] DUMP_EVENT_IN_STATE
ull
NONE
.1
FSM(%@) pending follow-up event(%@) [ending teardown in state(%@)] discarded
Diag
kSUCoreErrorPersistedStateMissingContents
kSUCoreErrorPSUSDisabledForSplatUpdate
unable to create request to reach server [UUID: %@] file: %@
/private/var/MobileSoftwareUpdate/Controller/SplunkHistory/
SUCoreFSM registeredActionTable
[FSM] PERFORM_EVENT
SUCoreDeviceQueryKeyProductBuildVersion
0[NO]
SUS
fsm
UnknownQueryMethod(%ld)
otaAutoTriggered
buddy
persisted state is not loaded, unable to load core version string
failureCount
assetURL
FactoryVersion.plist
integer
kSUCoreErrorExistingTransaction
kSUCoreErrorPSUSOptionalNonUserInitiatedDownloadNotAllowed
[FSM] API: postProtectedEvent
NSPrincipalClass
mdmAudiencePath
dataFsCapacity
succeeded
[FSM] ACTIVATE_MACHINE
kSUCoreErrorPSUSDisabledByPolicy
phase
no-issues
?:
NOT_VALID
Splat RestoreVersion (%@; %@) and Cryptex1 RestoreVersion (%@; %@) are equal
|EVENT_REPORTER
[DIAG] DUMP_UUID: %@
Pallas returned no match found for requested Build Version.
errorInStack domain
MajorDelayPeriod
too many waiting retry
Measurement
NOT-DICTIONARY
send finished with invalid file UUID
FSM(%@) invalid start state
v32@?0@\"NSString\"8#16^B24
phase:%@ stalled:%@ portionComplete:%f totalWrittenBytes:%lld totalExpectedBytes:%lld estimatedTimeRemaining:%f actionText:%@ disableVerboseLogging:%@ CFNetworkTask:%@
Space
Simulate
user
ANOMALY
failure:%ld|
rollbackSuggestionReason
boot-args
wait
alteration
SUCoreDeviceQueryKeySplatRollbackRestoreVersion
<NSDictionary>
kSUCoreErrorPrecisePSUSDisabledByPolicy
preSUStagingMaxOptionalSize
ServerURL
SUCoreOTAPreSUStagingDetermineStarted
state name
kSUCoreErrorUpdateNotDownloadingPSUSAssets
UUID
[EVENT_REPORTER] UPLOADING
/System/Cryptexes/OS/System/Library/CoreServices/
kSUCoreErrorRemoveFailed
%\\
SUCoreDeviceQueryKeyMarketingProductName
rollbackSuggestionErrorCode
Unknown
OSFilesystem
[FSM] SIMULATE
FSM(%@) event info provided when registered handler is not expecting any event info parameter: %@ event(%@) in state(%@)
the plugin doesn't support setTargetsSyncWithArguments:
HWModelStr
beginCount
yyyy-MM-dd
persisted state is not loaded, unable to load ULL value for key: %@
y
shared
AppleInternalVariant.plist
SUCoreDeviceQueryMethodRecoveryOSRestoreVersion
ERROR
%@:FSM(%@) has no defined state table
MobileAssetDownload
endFail
full
rollback
SUTestTool
Unknown Error Code
uploading
too many awaiting retry - not reporting file: %@
AlternateAssetAudienceUUID
Teardown
persisted state is not loaded, unable to load string value for key: %@
SUCoreDeviceQueryMethodCoreServicesAppleInternal
All possible error indications.
dropping on failed send (max retries)
next state
persisted state is not loaded, unable to load policy version string
FakeCustomerProduct
%@/%@
failures
Policy
kSUCoreErrorSpaceMobileAssetEstimateEvictableFailed
SUCoreFSM actionTable
replace_action
preSUStagingCacheDeletePurged
persisted state is not loaded, unable to load data value for key: %@
HomeAccessory
 Device(DeviceClass:%@|MarketingProductName:%@|ProductType:%@|HWModelStr:%@|BoardID:%@|HWTarget:%@)
|FAILURE
sucoreVersion
4`
kSUCoreErrorInvalidPayload
autoUpdate
reportVersion
unable to load fileUUID from awaiting retry array
AttemptedSendCount
FSM(%@) with nextState(%@) that is not defined in state table
SUCorePersistedStateContentsType
unable to persist dictionary for key with value: %@=%@
VerboseLogging
MobileAssetPurge
applyingUpdate
failed to form JSON data file [UUID: %@] file: %@
action:%@ trigger:%@ fsm:%@ event:%@ state:%@ alteration:%@ count:%d startAt:%d endAt:%d assetBuildVersions:%@ assetProductVersions:%@ assetAttributesPlist:%@ assetState:%@ updateInfoPlist:%@ errorDomain:%@ errorCode:%@ errorRecoverable:%@
en_US_POSIX
kSUCoreErrorMSUMissingDescriptor
prepareFinished
[SIMULATE] failed parsing option (unexpected/unsupported option key) for: '%@'
[%@]
kSUCoreErrorDocDataAssetNotLocal
[SIMULATE] simulate event alterations file does not exist (file non-existent): %@
assetProductVersions
UNKNOWN
YES
applyStarted
noPrecisePreSUStagingReason
applyFinished
task description nil or not NSString
[FSM] API: activateMachine
rsrRollbackSuggested
serverURL:%@ attemptedSendCount:%d failedSendCount:%d discoveredRunningCount:%d discoveredSuspendedCount:%d discoveredCancelingCount:%d
ProductVersion
kSUCoreErrorDocManagerDirectoryReadFailure
FSM(%@) event info Class mismatch (nil eventInfo when registered handler expecting non-nil): %@ event(%@) in state(%@)
PreservedFactoryVersion.plist
RestoreBuildGroup
adopt event alterations (load failed)
SerialNumber
com.apple.su.misc_tasks
!
kSUCoreErrorUnexpectedValue
preSUStagingCacheDeleteRequested
operationExpired
SUCoreOTADownloadStarted
teardown
PersistAcrossUpdates
SUCoreDeviceQueryKeyRecoveryOSReleaseType
alternateRampEnabled
DisableSlowRollUpdates
SUCoreDeviceQueryKeySFRProductVersion
UnknownQueryKey(%ld)
[%@(%@)] >S> %@ >E> %@ >A> %@
endFailIndicationsCount
SoftwareUpdate
%lu
No indications associated with error attributes
%@ %ld
[SIMULATE] failed parsing 'duration' (expected int) for: '%@'
SUCoreConfig(%@;%@)
SUCoreDeviceQueryKeyFactoryVersion
 RecoveryOS(Build:%@|ProductVersion:%@|RestoreVersion:%@|ReleaseType:%@)
%@%@/%@
kSUCoreErrorPersistedStateArchiverError
FSM(%@) current state(%@) does not exist in state table when checking %@ event(%@) table:\n%@
kSUCoreErrorEventReporterInvalidTask
FSM(%@) invalid %@ event
anomalyAllIndications
RestoreVersionString
count
unknown value for errorRecoverable:%d
SUCoreDeviceQueryKeyUnknown
SUCoreDeviceQueryKeySplatRollbackProductVersion
failed to create store-to directory: %@
unable to create NSURL session task [UUID: %@] file: %@
[SIMULATE] failed parsing tokens (unexpected format, expected 'key=value') for: '%@'
FALSE
RestrictToProductVersionExtra
%@
END
/var/mobile/Library/Preferences/com.apple.SoftwareUpdateCore
nil-object-class
kSUCoreErrorAssetReloadFailed
kSUCoreErrorConnectServerDecodeException
preSUStagingCacheDeleteLevel
FILE
trackType:%@ fsmName:%@ previousState:%@ fsmEvent:%@ nextState:%@ fsmAction:%@ eventInfo:%@
Scheduler
=
MobileAssetError
[%@(%@)] code:%ld error:%@
supervised
preflightScan
failed
failed to serialize persisted state to plist
[SIMULATE] failed parsing 'errorCode' (expected SUCoreErrorCode) for: '%@'
n
SUCoreDeviceQueryKeySplatCryptex1RestoreVersion
 Build(BuildVersion:%@|ProductVersion:%@)
None
EventReporter
MobileAssetQuery
kSUCoreErrorTypeMismatch
SUCoreErrorLayerGroup(layer=%@,domain=%@,minCode=%d,maxCode=%d,indications=%@)
FSM(%@) current state(%@) does not support %@ event(%@)
%@<<<}
domain(%@),code(%d),codeName(%@),indications(0x%08llX),keyMatchTrue(%@),keyMatchTrueMap(%@)
^([0-9]+).([0-9]+)(.[0-9]+)?$
SUCoreSplunkHistory.log
[SIMULATE] cannot dump events (simulator disabled)
SUCoreDeviceQueryMethodSplatCryptex1
SUDiagDump.plist
kSUCoreErrorMissingAuthentication
mandatoryUpdateOptional
currentOSVersion
[SIMULATE] PERFORM(OFF_QUEUE) - unable to create stop file(%@)
[SIMULATE] PERFORM(OFF_QUEUE)
MarketingProductName
SUCoreDeviceQueryKeySplatRollbackBuildVersion
checkedDomain
errorUserInfo
 
%@ %@%@: ?\n
mandatoryUpdateEligible
SoftwareUpdateCore
kSUCoreErrorSpaceNoAppOffloadPurgeResults
failed to write JSON data
Completed
FSM state
failed to remove persisted state file
persisted state is not loaded, unable to load boolean value for key: %@
ProductBuildVersionOverride
checkedIndications
kSUCoreErrorWriteFailure
kSUCoreErrorDocManagerInstalledBuildCreateFailure
action(%@),delegate(%@),class(%@)
SoftwareUpdateCorePersistedStateFile
F
pause
_%d_%@:%@
BridgeOSAMAuthInstall
kSUCoreErrorPluginFailedToLoad
rollbackSuggestionErrorDomain
[FSM] ACCEPT_EVENT
encode class name mapping failed: class %@ not found for coded name %@
installTonight
MA
simulate
SUCoreErrorInformation{isIndication} errorInformation
purge
SUCoreDeviceQueryKeySplatReleaseType
[FSM] ACTION: FSM(%@), action(%@)
anomalies
All
:
FSM(%@) pending follow-up event(%@) [prior to performing event(%@) in state(%@)] discarded
SUCorePersistedStatePolicyVersion
unable to load persisted state as dictionary
NSKeyedUnarchiver error found when attempting to unarchive data for key %@
SUCoreDeviceQueryMethodSplat
SUCoreDeviceQueryKeyRecoveryOSProductVersion
psr_ota
SUB
[FSM] POST_EVENT
,[%04lu:%@]
SUCoreErrorInformation{codeNameForDomain} errorInformation
failed to create persisted-state directory: %@
BridgeOSSoftwareUpdateError
kSUCoreErrorAlreadyAssigned
kSUCoreErrorConnectClientDecodeException
kSUCoreErrorDocManagerStashedBuildVersionNotFound
preSUStagingOptionalSize
action:%@ trigger:%@ module:%@ function:%@ count:%d startAt:%d endAt:%d duration:%d untilStop:%@ assetBuildVersions:%@ assetProductVersions:%@ assetAttributesPlist:%@ assetState:%@ updateInfoPlist:%@ errorDomain:%@ errorCode:%@ errorRecover
yyyy-MM-dd'T'HH:mm:ssZZZZZ
/System/Volumes/iSCPreboot/SFR/current/
preSUStagingMaxSize
CacheDelete
kSUCoreErrorScanCanceled
2`
FallbackToCoreDuetInactivityPredictor
kSUCoreErrorFSMAlreadyActive
dataFsFree
failed to create core event from provided event information
POST
unable to fully validate and setup FSM
AppleInternal
SUCoreDeviceQueryKeyProductVersion
portionComplete
totalWrittenBytes:%lld totalExpectedBytes:%lld 
|FILE
SUCoreOTAPreSUStagingDetermineFinished
SUCoreEventReporterState.state
BSU
SUCoreDeviceQueryKeyRestoreBuildGroup
v16@?0@\"NSArray\"8
com.apple.SoftwareUpdateCore.SUCoreConfigAccessQueue
kSUCoreErrorCopyFailed
SU
com.apple.su.completions
%@,%@
N
unable to serialize contents of persisted state file
disableVerboseLogging
[SIMULATE] PERFORM
/.nofollow/private/var/tmp/SoftwareUpdateCore
otaInstalling
success
send callback fileUUID invalid (%@) - event file may be left on filesystem
SUCorePersistedState fieldSpecificDictionary
.
NSOrderedSame
|
PowerManagement
currentBaseOSVersion
phase:%@ stalled:%@ portionComplete:%f %@estimatedTimeRemaining:%f task:%@ actionText:%@
modify_param
[SIMULATE] located event: %@ | valid=%@
SUCoreDeviceQueryMethodMobileGestalt
%@.%@.%@
NetworkRequired
kSUCoreErrorScanFoundMultiple
kSUCoreErrorPSUSDisabledByMSUDefault
[EVENT_REPORTER] SEND_FINISHED
unable to persist date for key with value: %@=%@
 SplatCryptex1(RestoreVersion:%@|ProductVersion:%@|ProductVersionExtra:%@|BuildVersion:%@|BuildVersionOverride:%@|ReleaseType:%@|HasSemiSplatActive:%@)
kSUCoreErrorEventReporterInvalidTaskDescriptor
kSUCoreErrorDocManagerFileEvictionFailure
SUCore-%@
CryptegraftFinshed
simTrigger
SUCoreDeviceQueryKeySFRReleaseType
|FAULT
kSUCoreErrorOperationCanceled
/
}
preSUStagingRequiredStagedCount
indicateOnceIdle completion when older completion in place - issuing error to older completion
persisted state is not loaded, unable to load object value for key: %@
kSUCoreErrorScanFoundDifferent
failed to create simulate dispatch queue
^([0-9]+).*
PersistedState
kSUCoreErrorScanFailed
resumingUpdate
/System/Volumes/Hardware/
SUCoreDeviceQueryKeyRecoveryOSRestoreVersion
SUCoreDeviceQueryKeySplatRollbackProductVersionExtra
Connect
FSMOccurrences
installInOneHour
[SIMULATE] failed parsing 'errorRecoverable' (expected SUCoreSimulateEventBoolean) for: '%@'
/System/Volumes/iSCPreboot/SystemRecovery/current/
trackType:%@ location:%@ reason:%@ code:%ld error:%@ | checked(%@) code:%ld domain:%@
kSUCoreErrorPSUSDisabledInBaseSystem
noActivation
SUCorePersistedStateCoreSecureCodedObjectsFields
ConfigurationScanInterval
trackType:%@ location:%@ reason:%@ code:%ld
 ReleaseType(ReleaseType:%@|Internal:%@|BootedOSSecureInternal:%@)
[%@] %@
kSUCoreErrorSpaceMobileAssetSuspendFailed
failureReason
unable to persist data for key with value: %@=%@
anomaly:%ld|
kSUCoreErrorInvalidParam
kSUCoreErrorMSUPreflightSUDownloadFailed
settings
false
FSM(%@) unsupported simulate action: %@
exit
kSUCoreErrorEventReporterInvalidResponse
kSUCoreErrorAssetPurgeFailed
updateType
\t 
ProductBuildVersion
FilesystemSpaceRequired
kSUCoreErrorSpaceCheckFailed
kSUCoreErrorPSUSDisabledByServer
currentOSType
splatSemiSplatActive
Downloading
hw.target
hw.product
SUCoreDeviceQueryMethodSysCtl
|ERROR
%lld
DEFINED
FSM(%@) forEvent(%@) inState(%@) table action(%@) != registered event action(%@)
[SIMULATE] failed parsing 'startAt' (expected int) for: '%@'
controllerStatus
an error occurred when loading the persisted state, but the state was still loaded
isStalled
Recoverable
FSM(%@) follow-up event(%@) in state(%@) ignored - not performing any event
^([0-9]+)[a-zA-Z]([0-9]+)[a-z]?$
Scan
kSUCoreErrorDeprecated
context
failed to write persistence file
\n[>>>\n               action: %@\n              trigger: %@\n               module: %@\n             function: %@\n                count: %d\n              startAt: %d\n                endAt: %d\n             duration: %d\n            unti
yyyy-MM-dd'T'HH:mm:ss
endSuccessCount
kSUCoreErrorScanNotCanceling
assetType
SUCoreRestoreVersion(restoreVersionString:%@|parsedVersion:%@|buildGroup:%ld)
[SIMULATE] dump all events - no simulate events
%@..
kSUCoreErrorInvalidState
systemFsCapacity
[SIMULATE] SETUP
[FSM] API: teardownMachine
kSUCoreErrorPSUSInvalidResults
downloadSize
end
FSM(%@) action delegate registering for event(%@) with Class - not supported
PallasNoPMVMatchFound
kSUCoreErrorMethodNotAvailable
downloadOverCellular
[FSM] FAILURE: initMachine
RestoreVersion.plist
%@(%d)
MSU
 Splat(RestoreVersion:%@|ProductVersion:%@|ProductVersionExtra:%@|BuildVersion:%@|ReleaseType:%@|HasSplatOnlyUpdateInstalled:%@)
error domain
packagePath
batteryLevel
SUCoreDeviceQueryKeySplatRollbackReleaseType
%@ %@%@: <sub-dictionary>:\n%@\n
kSUCoreErrorMSUPurgeFailed
mobile
SUCoreFSM stateTable
com.apple.su.delegate_callbacks
|END
faultCount
%@|
Network access is required.
1.0
com.apple.UpdateMetrics
current state
LoadingBrain
string
kSUCoreErrorFileNotFound
kSUCoreErrorSimulatedFailure
send finished
startAt
action should never be indicated when handling off-queue: %@
[DIAG] DUMP_HISTORY[%04lu]: %@
errorAllIndications
fault:%ld|
%d
kSUCoreErrorAssetReloadNotFound
NSOrderedAscending
SUCoreDeviceQueryKeySplatProductVersionExtra
errors
com.apple.su.core.error.info
alternateTotalRequiredFreeSpace
missing required event resources [UUID: %@]
failed to add serverURL metadata to file: %@
[SIMULATE] failed parsing line: %@
untilStop
SUCoreDeviceQueryKeyDeviceClass
kSUCoreErrorScanCatalogDownloadFailed
(present)
ReleaseType
SUFSReserveSize
application/json
reason
downloadResultCode
EVENT_REPORTER
NVRAM boot-args exist but format unknown - ignored
NSOrderedDescending
root
FullReplacementRequired
kSUCoreErrorConnectNoServerConnection
preSUStagingOptionalStagedSize
1.2
com.apple.su
[%@(%@)] >S> %@ >E> %@
<NSArray>
%@(%@):%@
kSUCoreErrorPSUSOptionalDisabledByPolicy
s
assetBuildVersions
otaDownloaded
[%@(%@)] code:%ld
-> %@
core.simulate
kSUCoreErrorMissingRequired
kSUCoreErrorConnectServerDecodeFailure
unarchived object is not of the expected class %@
none
[DIAG] DUMP_STATS:\n%@
(not shown)
1`
MeasurementAlgorithm
SUCoreDeviceQueryMethodFactoryVersion
SUCoreDeviceQueryMethodSplatRollback
checkedCode
anomalyIndicationsCount
beginCount:%ld,endSuccessCount:%ld,endFailCount:%ld,errorCount:%ld,anomalyCount:%ld,failureCount:%ld,faultCount:%ld,stateEventCount:%ld,allIndications:%@
Unknown Error Indication
kSUCoreErrorPSUSDisabledForSFRUpdate
should be off-queue when performing simulate action: %@
<nil>
kSUCoreErrorSpaceAppOffloadPurgeableFailed
[FSM] FOLLOW_UP_EVENT
%@:%@
kSUCoreErrorInconsistencyDetected
kSUCoreErrorConnectClientDoesNotRespond
updateFinished
 SFR(Build:%@|ProductVersion:%@|RestoreVersion:%@|ReleaseType:%@)
/RecorderSplunkRecords
failed to load the plugin from %@
[%@(%@) %@] code:%ld error:%@
i
|%@
kSUCoreErrorNone
kSUCoreErrorScanFailedToDeterminePSUSAssets
events
reportReason
totalExpectedBytes
NO
Pallas returned no match found for requested PMV (HTTP 422).
hang
|STDOUT
%@ %@%@: %@\n
MobileAssetXPC
reportHistory
synchonize discovered Completed
anomaly
kSUCoreErrorSpaceAppOffloadFailed
delayPeriod
preSUStagingEnabled
[SIMULATE] syntax error: assetBuildVersions and assetProductVersions must both be defined
modify param not yet supported: %@
DisableSFRSoftwareUpdates
[%@(%@) %@] code:%ld
endFailAllIndications
persistDuration
preSUStagingRequiredCount
SUCoreEvent
failed to copy existing files array
SUCoreDeviceQueryKeyPreservedFactoryVersion
%@ %@%@: <sub-dictionary> at depth=%llu\n
[SIMULATE] DISPATCH
SUCoreDeviceQueryKeyProductType
kSUCoreErrorDiagDecoded
kSUCoreErrorScanQueryMetadataFailed
targetOSVersion
FSM(%@) state table not provided
kSUCoreErrorSerializedFailed
Dead
2.1.0
[%04lu:%@]
incremental
SUCoreTriStateUnknown
SoftwareUpdateScanInterval
RestoreVersion
undefined
coreDiagReport
AS
kSUCoreErrorPersistedStateClassMismatch
kSUCoreErrorFSMEventInvalidForState
kSUCoreErrorDocManagerPathCreateFailure
SUCorePersistedStateCoreVersion
splatCombo
SUFSM_%@_%@
totalWrittenBytes
60EF4694-4272-4276-B9A6-DA4F8FFF93F1
location
data
deviceModel
https://xp.apple.com/report
https://xp.apple.com/report/2/psr_ota
invalid instance name
kSUCoreErrorDDMInvalidDeclarationFailure
failed to fsync persistence file
--
KEYMAP(%llu)
SUCoreDeviceQueryKeySFRProductBuildVersion
\n-> %@
kSUCoreErrorPSUSNothingToStage
cleanupLevel
alternateTargetOSVersion
Running
failed to load dictionary for SUCorePersistedStateType=%@
SUCoreSimulateEventBoolean(%d)
Splat RestoreVersion (%@) and Cryptex1 RestoreVersion (%@) are not equal
[%@(%@)] >S> %@ >E> %@ >N> %@ >A> %@
kSUCoreErrorDocManagerDirectoryCopyFailure
%@.%@
[SIMULATE] failed parsing 'errorUserInfo' (expected {k1=v1;k2=v2;}) for: '%@'
Update
DocManager
kSUCoreErrorConnectMessagedIDMismatch
preflightWakeup
Applying
targetOSTrain
ProductType
kSUCoreErrorScanAbortedStale
invalid SUCorePersistedStateType (%@) provided for secure coded object persistence
errorCount
kSUCoreErrorPSUSNotSupported
ddm
core.splunk.history
psusAssetPath
\r\n
no
unknown simulate action: %@
SUCoreDeviceQueryKeySplatProductVersion
code
[%@(%@)] >S> %@ >E> %@ >N> %@
boolean
TATSU declined to authorize this user for this install.
kSUCoreErrorDocManagerCreateInstalledStashedDataDictFailed
<%@> targetOSVersion: %@, targetOSBuild: %@, targetOSTrain: %@, psusAssetPath: %@
 EmbeddedOS(Build:%@|RestoreVersion:%@|Internal:%@)
Preflight
t
kSUCoreErrorTooManyQueued
reportStats
[EVENT_REPORTER] DROP
  %@ = %@
AppleTV
SUCoreDeviceQueryKeySplatBuildVersion
post
%@%@
alternateUpdateType
[FSM] TEARDOWN
SUCorePersistedStateTypeUnknown(%d)
Splat is not supported on this platform; semi-splat is not possible
 | %@
SUCoreErrorInformation{codeNameForError} errorInformation
kSUCoreErrorFSMInvalidTable
MobileSoftwareUpdateErrorDomain
FSM(%@) event where action indicated (but table / registration mismatch) %@ event(%@) in state(%@) action(%@)!=attached(%@)
faultIndicationsCount
numPlatformAssetsFound
core.fsm.extended
adopt event alterations (parsing failed)
ll
\n%@
failed to get existing files error: %@
callback where send considered successful yet may not have been [completely sent]
SUCorePersistedState
stabilityMonitor
%@/%d/%@
[EVENT_REPORTER] SEND
moduleName
 FactoryVersion(Version:%@|Preserved:%@)
kSUCoreErrorEventReporterInvalidFileUUID
kSUCoreErrorSpaceNoPurgeResults
Compare called on restore version when other version is not compatible
previous
Network
SUCorePersistedStateCoreFields
[%@(%@)] >S> %@ >E> %@ >N> %@ >A> %@ info:%@
errorIndicationsCount
Download has timedout.
SUCoreOTADownloadFinished
unable to persist state: %@
FAULT
kSUCoreErrorMSUPrepareFailed
SUCoreDeviceQueryMethodUnknown
anomalyCount
<NSNumber>
notification
SUCoreFSM eventsForState
failureIndicationsCount
otaPostponed
clientName
BatteryCurrentCapacity
stateEventCount
\n[>>>\n                beginCount: %ld\n           endSuccessCount: %ld\n\n              endFailCount: %ld\n   endFailIndicationsCount: %ld\n     endFailAllIndications: %@\n\n                errorCount: %ld\n     errorIndicationsCount: %ld
unable to read NVRAM variables - unable to get registry entry for IODeviceTree:/options
*
kSUCoreErrorUnknownFormat
kSUCoreErrorPersistedStateNotLoaded
serialNumber
3`
[SIMULATE] dump all events - %@
TATSUDeclinedAuthorization
indicate once idle
%@%@ <sub-dictionary>:\n%@{>>>\n
Asset
PSUS
kSUCoreErrorConnectClientIDMismatch
requestedPMV
/EventReporterPersistedState
[FSM] API: initMachine
SUCorePersistedStatePolicySecureCodedObjectsFields
v32@?0@8Q16^B24
NoDomain
IODeviceTree:/options
SUC
yes
wheel
SUCoreDeviceQueryMethodSFRRestoreVersion
core.diag.tracking
SUCore
kSUCoreErrorPSUSDisabledInNeRD
task descriptor nil or not NSString (after get)
event name
TRUE
no registered callback when handling off-queue: %@
SUCoreDeviceQueryKeyHWModelStr
failure
OperatingSystem
SUCoreEventReporterServerURL
SUCoreDeviceQueryMethodSFRSystemVersion
SUCoreDeviceQueryKeyRestoreVersion
SUCoreDeviceQueryKeyRecoveryOSRestoreBuildGroup
commandLine
SUCorePersistedStatePolicyFields
q24@?0@\"SUCoreRestoreVersion\"8@\"SUCoreRestoreVersion\"16
One of Splat RestoreVersion (%@) or Cryptex1 RestoreVersion (%@) are not present
%llu
programInitiated
/System/Library/CoreServices/
%@{>>>\n
%@:
AlternateInstallerRecommended
kSUCoreErrorPrecisePSUSNoConfigFound
endFails
faults
ul
kSUCoreErrorDocDataCreateFailed
[SIMULATE] cannot provide last alterations (simulator disabled)
kSUCoreErrorScanNotDeterminingPSUSAssets
kSUCoreErrorConnectClientDecodeFailure
verifyingUpdate
true
v32@?0@\"NSDictionary\"8Q16^B24
FAILURE
invalidKeybag
Context
Power
otaStartedDownloading
FailedSendCount
DiscoveredRunningCount
com.apple.su.waited_operations
SUCoreDeviceQueryKeyReleaseType
[%@(%@)] code:%ld error:%@ | checked(%ld)
int
kSUCoreErrorReadFailure
kSUCoreErrorDocDataAssetRefreshFailed
preSUStagingEffectiveCacheDeleteLevel
storageCapacity
[FSM] API: registerAction
endFail:%ld|
v24@?0@8^B16
BATS_TESTPLAN_ID_%@
%@ - could not remove event file: %@
estimatedTimeRemaining
[SIMULATE] failed parsing 'endAt' (expected int) for: '%@'
simAction
dictionary
Y
CryptegraftStarted
SUCoreSplunkHistory.lock
failed to open persistence file: %d - message: %s
[DIAG] dump tracked with reason=%@ dumpToMask=%@ filename=%@ clearStatistics=%@ clearHistory=%@
kSUCoreErrorSpaceMobileAssetResumeFailed
result
prepareStarted
SoftwareUpdateController
Internal
fault
event
[EVENT_REPORTER] BUILD
com.apple.softwareupdateservices.errors
dumpEventInStateOccurrences
f
Test
kSUCoreErrorDDMNoControllerFailure
preSUStagingOptionalCount
task nil or not NSURLSessionTask
failed to use NSKeyedArchiver to archive the object into encoded NSData
NOT SET
SUCoreDeviceQueryKeySplatCryptex1BuildVersionOverride
[EVENT_REPORTER] SYNC
failed to create file: %@ for attaching of serverURL metadata
NSURLSessionTaskState(%d)
NULL
 SplatRollback(RestoreVersion:%@|ProductVersion:%@|ProductVersionExtra:%@|BuildVersion:%@|ReleaseType:%@|HasEligibleRollback:%@)
faultAllIndications
_%d_%@:%@ | %@
watchInstallType
sharediPad
persisted state is not loaded, unable to load core contents type string
Facility
kSUCoreErrorNotSupported
UsersLoggedIn
systemFsFree
\n[>>>\n    persistencePath: %@\n versionPolicyLayer: %@\n      versionSUCore: %@\n     persistedState: %@\n<<<]
SUCoreDeviceQueryMethodRecoveryOSSystemVersion
SUCoreDeviceQueryKeySplatCryptex1ProductVersionExtra
LOG_ARCHIVE
kSUCoreErrorEventReporterResponseNotHTTP
kSUCoreErrorPSUSDisabledForClient
otaReady
noNetwork
ASError
 BridgeOS(Build:%@|RestoreVersion:%@|Internal:%@)
<NSData>
kSUCoreErrorScanNoDocFound
otaAbandoned
preflightDownload
[EVENT_REPORTER] SETUP
FSMAction
invalid FSM name
networkType
updatingClass
[SIMULATE] cannot provide count of alterations (simulator disabled)
kSUCoreErrorScanNoUpdateFound
kSUCoreErrorDocManagerDirectoryDeleteFailure
[SIMULATE] syntax error: assetBuildVersions (%lu) and assetProductVersions (%lu) must have the same count
NOTNULL
1[YES]
.%@
DeviceClass
#
T
?
STDOUT
Full replacement is required [as opposed to incremental patch].
SUCoreErrorInformation{_attributesOfErrorForDomain} errorInformation
replace_event
SUCoreDeviceQueryKeySplatCryptex1ReleaseType
,
kSUCoreErrorConfiguringDownload
kSUCoreErrorCancelingDownload
updateInfoPlist
kSUCoreErrorDocManagerDetermineOSBuildFailure
unable to persist ULL for key with value: %@=%lld
unable to persist string for key with value: %@=%@
SoftwareUpdateMacController
/DiagDump
endFailCount
FSM(%@) forEvent(%@) inState(%@) indicates event info Class when not supported
/tmp/ASUCodeCoverage
controllerVersion
encountered invalid JSON payload [UUID: %@] file: %@
TestIndication
ProductVersionExtra
_%d_%@(%@):%@
rollbackSuggestionResponsibleProcess
preSUStagingRequiredSize
FSM(%@) unable to create actions for state(%@) so dropping registration of action(%@) for event(%@)
DisableRosettaUpdates
dropping on failed send
Preparing
%@/%@.%d.%@.profraw
plist
SUCoreDeviceQueryKeyRecoveryOSProductBuildVersion
DiskUsage
\n[>>>\n               action: %@\n              trigger: %@\n                  fsm: %@\n                event: %@\n                state: %@\n           alteration: %@\n                count: %d\n              startAt: %d\n                
Current device configuration requires an alternate installer to perform the update.
kSUCoreErrorDocManagerAllocationFailure
persistencePath:%@, versionPolicyLayer:%@, versionSUCore:%@
SUCoreDeviceQueryKeyHWTarget
next
kSUCoreErrorFSMStateInvalidForTable
\n[>>>\n        productVersion: %@\n   productBuildVersion: %@\n           releaseType: %@\n           measurement: %@\n  measurementAlgorithm: %@\n<<<]
persisted state is not loaded, unable to load dictionary value for key: %@
kSUCoreErrorPersistedStateInvalidType
kSUCoreErrorScanInvalidPSUSDetermineResults
spin
fsmEvent
trackType
trackType:%@ location:%@ reason:%@ code:%ld error:%@
otaPersisted
Suspended
FSM(%@) failed to validate state table and registered actions
splatComboVersion
SUCoreOTAPreSUStagingFinished
[FSM] API: postEvent
persisted state is not loaded, unable to load date value for key: %@
<%@> error: %@
<NSNull>
PallasNoBuildVersionMatchFound
kSUCoreErrorCreateFailed
downloadErrorName
FSM name not provided
FSM(%@) pending follow-up event(%@) [starting teardown in state(%@)] discarded
begin
kSUCoreErrorOperationTimedOut
kSUCoreErrorAssetDownloadFailed
SUFSReserveRequestedSize
unable to persist object for key with value: %@=%@
SystemVersion.plist
{
errorDesc
[%@(%@)] code:%ld error:%@ | checked(%@) code:%ld domain:%@ indications:%@
dd-MM-yyyy-hh-mm-ss
<NSString>
kSUCoreErrorPersistedStateLoadFailed
waitingForUnlock
[SIMULATE] dump all events - empty simulate events
AllowLiveAssetServerFallback
<NSDate>
SUCoreError
rampEnabled
preSUStagingOptionalStagedCount
FSM event
kSUCoreErrorAssetRefreshFailed
duration
FSM(%@) forEvent(%@) inState(%@) hasAction(%@) yet event handler has not been registered
FSM(%@) event info Class mismatch (eventInfo of diff Class than registered): %@ event(%@) in state(%@)
v32@?0@\"NSString\"8@\"NSString\"16^B24
[EVENT_REPORTER] SEND_RETURNING_AUGMENTED
v8@?0
_%d_%@(%@):%@ | %@
DownloadTimedOut
kSUCoreErrorAssetNotLocal
[EVENT_REPORTER] QUEUED
SUBError
unable to serialize data into JSON [UUID: %@] file: %@
FSM(%@) follow-up event(%@) in state(%@) ignored - already have follow-up event(%@)
FSMNextState
[%@(%@):%@
\n[>>>\n              layer: %@\n             domain: %@\n            minCode: %d\n            maxCode: %d\n        indications: 0x%08llX\n       keyMatchTrue: %@\n    keyMatchTrueMap: %@\n<<<]
otaScheduled
FSM(%@) not active at %@ event(%@)
[PERSISTED_STATE]
SUCoreOTAPreSUStagingStarted
core.splunk.state
too many send attempts
[SIMULATE] cannot dump events (no persisted state)
SUCoreDeviceQueryMethodCoreServices
deviceClass
unable to persist boolean for key with value: %@=%@
checkedLayer
]
otaAvailable
totalRequiredFreeSpace
splatInstalled
MobileAsset
SUCoreDeviceQueryKeySFRRestoreBuildGroup
error
[%@(%@) %@] code:%ld error:%@ | checked(%@) code:%ld domain:%@ indications:%@
errorRecoverable
preSUStagingRequiredStagedSize
Content-Type
error:%ld|
Extended
kSUCoreErrorSpaceNoCacheDeletePurgeableResults
mdm
inBoxUpdate
[SIMULATE] EVENT
FSM(%@) action delegate already registered as event handler for event(%@)
BEGIN
[%llu]
downloadNotReady
%@\n
[SIMULATE] cannot adopt event alterations (simulator disabled)
Additional filesystem space is required.
NSSecureCoding
NSURLSessionDelegate
SUCoreSimulate
SUCoreDiagStats
SUCoreEventReporter
SUCoreSplunkHistory
SUCoreFSMAttachedAction
SUCoreMAIdentifier
SUCoreProgress
SUCoreDiag
SUCoreError
SUCoreFSM
SUCorePSUSPlugin
SUCoreRestoreVersion
SUCoreSimulateEvent
SUCoreDevice
SUCoreCodeCoverage
SUCoreConfig
NSCoding
SUCoreEventReporterActive
SUCoreStartup
SUCoreDiagPoint
SUCoreDictionary
SUCoreErrorAttributes
SUCoreErrorInformation
SUCoreEvent
SUCoreEventReporterDelegate
NSObject
SUCoreLog
SUCoreErrorLayerGroup
SUCorePersistedState
SUCorePSUSArguments
SUCorePSUSResult
SUCoreUUID
SUCore
T@\"NSMutableDictionary\",&,N,V_persistedState
_eventExtensions
initMachine:ofInstance:withTable:startingIn:
serverURL
_persistedState
_reason
_splatRollbackSystemVersionPlistContents
buildVersion
code
secureCodedObjectForKey:ofClass:encodeClasses:
_checkWhetherIdle:
initWithDictionary:
stringByDeletingLastPathComponent
T@\"NSString\",&,N,V_hwModelString
portionComplete
TB,N,V_hasEmbeddedOS
Tq,N,V_endFailIndicationsCount
_errorCount
_failureCount
_isImmediateEvent:
actionDelegate
T@\"NSString\",&,N,V_sfrRestoreVersionPlistPath
T@\"NSString\",&,V_filesystemBaseDir
T@\"NSString\",R,&,N,V_projectName
Tq,N,V_trackType
_parseErrorCodeFromString:destination:
_performOffQueueEvent:
indicateOnceIdle:
initWithBeginCount:withEndSuccessCount:withEndFailCount:withEndFailIndicationsCount:withEndFailAllIndications:withErrorCount:withErrorIndicationsCount:withErrorAllIndications:withAnomalyCount:withAnomalyIndicationsCount:withAnomalyAllIndica
Tq,R,N,V_maxCode
_errorAllIndications
_reportedUUID
_systemVersionPlistContents
encodeFloat:forKey:
projectName
setSafeObject:forKey:
setTargetsAsyncWithArguments:completion:
T@\"NSMutableDictionary\",&,N,V_eventExtensions
setCheckedCode:
Tq,R,N,V_syncedVersion
_copySplatCryptex1SystemVersionPath
_inProcessConfig
_safeValueName:ofMaxFieldLength:providingSubstitutionMap:
dataForKey:forType:
dataRepresentation
T@\"NSString\",&,N,V_factoryVersionPlistPath
sfrBuildVersion
TB,N,V_deviceSupportsMultiVolumeBoot
_majorVersion
dateForKey:
endFailIndicationsCount
intValue
setSfrRestoreVersion:
followupEvent:
setAllFields:
setObject:forKey:
Tq,N,V_anomalyAllIndications
_checkedIndicationsMatching:
encodeBool:forKey:
nameForSUCoreLayer:
recoveryOSProductVersion
safeBooleanForKey:
setBridgeBuildVersion:
_deviceSupportsFactoryVersion
_initializeBridgeOSProperties
_isSharedDiag
_trackStats
dumpEventInStateOccurrences:
persistSecureCodedObject:forKey:forType:shouldPersist:
copyCurrentState
encodeInteger:forKey:
T@\"NSString\",&,N,V_productType
awaitingRetry
setBuildVersion:
attributesOfErrorForDomain:withCode:codeName:indicating:ifKeyTrue:
checkedNameForCode
safeUserInfoValues
setCurrentState:
setTrackType:
simAction
trackAnomaly:forReason:withResult:withError:
trackEnd:withResult:withError:
T@\"NSString\",&,N,V_splatReleaseType
TB,N,V_volumeIsExternal
_copySysCtlValueForKey:
contentsOfDirectoryAtPath:error:
useFilesystemBaseDir:
bundleWithPath:
T@\"NSString\",&,N,V_factoryRestoreVersion
_buildVersion
_copyGestaltValueForKey:
_handleSignal:forName:
_keyNameForPersistedStateType:
encodeInt64:forKey:
_productVersion
_preservedFactoryRestoreVersion
_copyCoreServicesAppleInternalValue
_sendInterruptedFromStorage:
hasSemiSplatActive
isEqualToString:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_informationQueue
T@\"NSDictionary\",&,N,V_splatCryptex1SystemVersionPlistContents
Tq,R,N,V_code
setSplunkAccessCreated:
T@\"NSDictionary\",&,N,V_appleInternalVariantPlistContents
_sfrRestoreVersionPlistContents
T@\"NSObject<OS_dispatch_queue>\",R,N,V_miscellaneousTaksQueue
TB,N,V_deviceSupportsSplatRollbackRestoreVersion
_measurement
_splunkURL
endFailCount
isActive
dataWithLength:
buildGroup
copyTrackedStatsClearingAfter:
defaultSessionConfiguration
initWithAction:usingDelegate:withInfoClass:
setDefaultLevelLogging:
setInProcessOperationQueue:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_waitedOperationQueue
URLSessionDidFinishEventsForBackgroundURLSession:
_logReturningDefault:forKey:valueType:defaultValueName:
eventInfoClass
T@\"NSString\",R,&,N,V_alteration
T@\"NSDictionary\",&,N,V_restoreVersionPlistContents
T@\"NSString\",&,N,V_location
anomalyIndicationsCount
fsm:forEvent:inState:
persistString:forKey:forType:shouldPersist:
T@\"NSString\",R,&,N,V_assetAttributesPlist
_factoryVersionPlistPath
_lastReportedUUID
errorRecoverable
faultIndicationsCount
recoveryOSRestoreVersion
stringForKey:forType:
ullForKey:
setRestoreVersionPlistContents:
Tq,R,N,V_majorVersion
_checkedStackErrorAtDepth:
_splatRollbackProductVersion
deviceSupportsSplatCryptex1RestoreVersion
isEqualToDate:
setAppleInternalVariantPlistPath:
setKeyMatchTrueMap:
T@\"NSMutableDictionary\",&,N,V_allFields
_errorDomain
fileExistsAtPath:
isMemberOfClass:
preservedFactoryVersionPlistContents
setFactoryVersionPlistPath:
setSplatCryptex1RestoreVersionPlistContents:
sharedDevice
T@\"NSDictionary\",&,N,V_splatRestoreVersionPlistContents
dataIsEqual:to:
_updateActiveEvent:forFileUUID:
T@\"NSString\",&,N,V_recoveryOSReleaseType
_minorVersion
_summaryStateEvent
diag
randomUUIDWithLastThreeCharactersOfUUID:
UUIDForMobileAsset
initWithCoder:
initWithObjects:
registerCallbackHandler:
secureCodedObjectForKey:ofClass:
setEndSuccessCount:
setHwModelString:
setSplatReleaseType:
commonFilesystemBaseDir
errorIndicationsCount
persistULL:forKey:
setErrorDesc:
T@\"NSDictionary\",&,N,V_splatRollbackRestoreVersionPlistContents
_checkedIsSafe:
closeAndReturnError:
initWithObjects:forKeys:
setLockFD:
_buildCheckedErrorForDomain:withCode:safeUnderlying:description:
_triggerAction:usingAttached:onEvent:inState:withInfo:nextState:
param
persistDate:forKey:shouldPersist:
setHasSplat:
setRestoreVersionPlistPath:
setSplatCryptex1RestoreVersionPlistPath:
T@\"NSString\",&,N,V_splatCryptex1BuildVersionOverride
_duration
_supportsSFRSystemVersion
duration
generateError:ofDomain:withCode:
persistString:forKey:
removeItemAtPath:error:
reporter
setFactoryVersionPlistContents:
_errorUserInfo
_informationQueue
_newScrubbedEvents:
_summaryStandard
isLowPowerModeEnabled
null
releaseSharedLock
_parseRestoreVersionString
setCalendar:
setDeviceBoardID:
setDiscoveredCancelingCount:
setUntrackedOccurrences:
writeToURL:error:
_appleInternalVariantPlistPath
_checkedDomain
buildAndLogCheckedSUCoreError:underlying:description:
getFileMetadata:forKey:
persistBoolean:forKey:forType:shouldPersist:
setDeviceSupportsSplatRollbackRestoreVersion:
setServerURL:
TB,N,V_deviceSupportsSFRRestoreVersion
baseDomain
checkedCode
faultCount
initWithData:encoding:
layerForError:
safeULForKey:defaultValue:
stringWithFormat:
_defineErrorLayers
_delegateCallbackQueue
assetBuildVersions
enumerateObjectsUsingBlock:
marketingProductName
recoveryOSReleaseType
sendEvent:toServerURL:returningFinalEventDictionary:
setFailureAllIndications:
_copyEscapeStringsForEventData:
end:atFunction:
hwModelString
setFactoryRestoreVersion:
setPerformingEvent:
setupCoreErrorInformation
appleInternalVariantPlistContents
checkedDepthCount
_adoptLastErrorEvent:
_simulateEventAlteration:fsmEvent:eventInfo:attachedAction:
_systemVersionPlistPath
safeStringForKey:
summaryOfIndications:
trackType
_restoreVersion
T@\"NSString\",&,N,V_splatCryptex1RestoreVersionPlistPath
persistencePath
_accessQueue
_discoveredRunningCount
_projectName
invertedSet
sharedSUCoreDomainAppending:
T#,R
isProxy
TB,N,V_isSharedDiag
_sharedReporter:withAccessControl:
_supportsRecoveryOSRestoreVersion
isEqualToNumber:
newlineCharacterSet
setMarketingProductName:
splatRestoreVersionPlistPath
_deviceClass
_deviceSupportsSFRRestoreVersion
_splatCryptex1ProductVersion
collectTrackedStatsClearingAfter:completion:
getSystemRecoveryNSIHDirectory
productVersion
setSfrSystemVersionPlistContents:
setSplatRestoreVersionPlistContents:
_currentState
_supportsSplat
setAlterationsPerformed:
setPersistedState:
trackBegin:atLevel:forModule:
dealloc
Tq,N,V_faultAllIndications
_reloadPlistContentsForKey:
_splatCryptex1SystemVersionPlistPath
measurementAlgorithm
setConfig:forKey:
setSplatRestoreVersionPlistPath:
T@\"NSString\",&,N,V_deviceClass
_copyRecoveryOSRestoreVersionValueForKey:
_errorDesc
dictionaryWithContentsOfFile:
initByCombining:withBeginCount:withEndSuccessCount:withEndFailCount:withEndFailIndicationsCount:withEndFailAllIndications:withErrorCount:withErrorIndicationsCount:withErrorAllIndications:withAnomalyCount:withAnomalyIndicationsCount:withAnom
initWithProjectName:defaultsPath:
isEqual:
setEstimatedTimeRemaining:
_domain
_alterationsPerformed
numberWithLongLong:
parsedVersion
setSplatBuildVersion:
setSplatRollbackRestoreVersionPlistContents:
setValue:forKey:
valueForKey:
setActiveEventsState:
T@\"NSString\",&,N,V_hwTarget
_bridgeVersionPlistPath
_hasSplat
_minCode
_restoreVersionPlistPath
_synchonizeDiscoveredUnknown:forActiveEvent:withFileUUIDsToRetry:
initializeSharedStartup:usingDomain:usingFilesystemDir:
path
T@\"NSObject<OS_dispatch_queue>\",R,N,V_splunkHistoryQueue
_initWithAction:onTrigger:forModule:atIdentity:atEvent:inState:alteration:startAt:endAt:duration:untilStop:assetBuildVersions:assetProductVersions:assetAttributesPlist:assetState:updateInfoPlist:errorDomain:errorCode:errorUserInfo:errorReco
finishEncoding
getAllTasksWithCompletionHandler:
setCode:
T@\"NSString\",&,N,V_bridgeBuildVersion
_dumpMaskToString:
_storeJSONData:withFileUUID:forEventUUID:
codeNameForError:
domain
propertyListWithData:options:format:error:
recoveryOSSystemVersionPlistPath
setAccessControl:
checkedUserInfo
T@\"NSString\",R,&,N,V_defaultsPath
TB,N,V_deviceSupportsAppleInternalVariant
UUIDv5FromString:
_splatCryptex1BuildVersion
attributesOfErrorForDomain:withCode:codeName:keyMatchTrueMap:
initializeForName:
oslog
_plugin
initWithString:
_anomalyCount
_deviceSupportsSplatRestoreVersion
_moduleName
_nsURLSessionTaskNameForState:
firstMatchInString:options:range:
setEndFailIndicationsCount:
safeIntegerForKey:defaultValue:
T@\"NSDictionary\",&,N,V_factoryVersionPlistContents
T@\"NSString\",R,&,N,V_untilStop
_startState
characterSetWithRange:
isComparable:
reportedUUID
setEventAlterations:
T@\"NSString\",R,&,N,V_moduleName
Tq,R,N,V_minCode
_layerInformation
_splatRestoreVersion
_volumeIsExternal
initWithInteger:
setTargetedSystemVolume:
splatProductVersionExtra
maxCode
Ti,R,N,V_duration
Tq,N,V_attemptedSendCount
hasSplatOnlyUpdateInstalled
setSplatRollbackBuildVersion:
stateSafeSetConfig:forKey:
stringByAppendingFormat:
stringForKey:
T@\"NSObject<OS_dispatch_queue>\",R,N,V_delegateCallbackQueue
Ti,N,V_alterationsPerformed
_errorInformation
safeSummaryForDictionary:
sameProgress:isStalled:portion:remaining:actionText:
setEventExtensions:
syncedVersion
waitedOperationQueue
checkedOfLayer:
release
T@\"NSString\",&,N,V_splatRollbackRestoreVersion
_anomalyAllIndications
_bridgeVersionPlistContents
_discoveredSuspendedCount
_persistencePath
_synchonizeDiscoveredCompleted:forActiveEvent:withFileUUIDsToRetry:
T@\"NSString\",&,N,V_splatCryptex1RestoreVersion
_storeServerURLMetadata:toFileUUID:
discoveredCancelingCount
keyMatchTrue
restoreVersionPlistContents
setKeyMatchTrue:
setTargetOSTrain:
sfrReleaseType
TB,N,V_hasRecoveryOS
Tq,N,V_checkedIndications
_pendingFollowupEvent
_serverURL
_splatCryptex1RestoreVersionPlistPath
bridgeBuildVersion
persistBoolean:forKey:shouldPersist:
splatCryptex1BuildVersion
setDeviceClass:
T@\"NSString\",&,N,V_splatProductVersion
setSplatRollbackRestoreVersion:
T@\"SUCorePersistedState\",&,N,V_activeEventsState
Ti,N,V_activeSendTaskCount
_adoptAllEventAlterations:
_discoveredCancelingCount
persistDate:forKey:
T@\"NSDictionary\",&,N,V_splatRollbackSystemVersionPlistContents
conformsToProtocol:
initWithDispatchQueue:withPersistencePath:forPolicyVersion:issuingDefaultLevelLogging:
postEvent:withInfo:
replaceObjectAtIndex:withObject:
safeObjectForKey:ofClass:
setEventExtensionsDetermined:
simTrigger
_appleInternalVariantPlistContents
_supportsAppleInternalVariant
addOperationWithBlock:
trackEnd:
T@\"NSMutableDictionary\",&,N,V_decodeClassNameMappings
_sendCoreEvent:
setIndications:
buildCheckedSUCoreError:underlying:description:
safeWriteEventUUID:
sharedSimulator
taskDescription
TQ,N,V_untrackedOccurrences
addObject:
persistDate:forKey:forType:shouldPersist:
_getSplunkRequestForURL:
allIndicationsForError:
anomalyAllIndications
hasEmbeddedOS
infoDictionary
performSelector:
persistString:forKey:shouldPersist:
setHTTPMethod:
TB,N,V_deviceSupportsSplatRestoreVersion
TB,N,V_dropEventsOnSendFailure
TB,N,V_splunkAccessCreated
alteration
attributesOfSUCoreErrorCode:indicating:
isSharediPad
longLongValue
restoreVersion
_lockFD
T@\"NSString\",R,&,N,V_domain
TB,N,V_deviceSupportsCoreServices
_alignPersistedStateWithExistingFileUUIDs:
_storeToPath
initWithUnsignedLongLong:
setErrorCount:
sortedArrayUsingComparator:
T@\"NSString\",&,N,V_deviceBoardID
_productBuildVersion
retainCount
setVersionPolicyLayer:
stringByAppendingString:
trackingQueue
unsignedLongValue
untilStop
T@\"NSString\",&,N,V_splatRollbackProductVersionExtra
T@\"NSString\",&,N,V_volumeUUID
Tq,N,V_discoveredRunningCount
Tq,N,V_faultIndicationsCount
_synchronizedAdjustTargetingSystemVolume:
initStateEventForFSM:previousState:fsmEvent:nextState:fsmAction:eventInfo:
initWithProjectName:
_productType
_simTrigger
defaultLevelLogging
encodeClassNameMappings
initWithAppendedDomain:appendingDumpFilename:
setUniqueInstanceName:
faultAllIndications
sendEvent:toServerURL:
setSplatRollbackRestoreVersionPlistPath:
setCheckedIndications:
setLocale:
setSfrRestoreVersionPlistContents:
uniqueInstanceName
_hwTarget
_isBridgeInternal
identityName
stringWithContentsOfFile:encoding:error:
T@\"NSURL\",&,N,V_splunkURL
TB,N,V_deviceSupportsPreservedFactoryVersion
_safeUserInfoValues
fsmEvent
setChangedSinceReported:
simulatorEnabled
_activateMachineWithStateTable:withActionTable:
_coreServicesKeyForQueryKey:
followupEvent:withInfo:
replaceCharactersInRange:withString:
setFileMetadata:forKey:value:
sharedDataAccessor
TB,N,V_hasSFR
mutableCopy
persistedStatePath
defaultsPath
dictionaryForKey:forType:
flushEvent
Tq,N,V_faultCount
_completionQueue
bridgeVersionPlistPath
moduleName
plugin
setEncodeClassNameMappings:
T@\"NSDictionary\",&,N,V_splatCryptex1RestoreVersionPlistContents
_inProcessSession
_removeFileUUID:loggingError:forReason:
_targetOSBuild
buildCheckedError:
debugDescription
descriptionWithLocale:
initForLayer:withDomain:minCode:maxCode:indicating:ifKeyTrue:keyMatchTrueMap:
_hasSFR
attemptedSendCount
currentLocale
setPhase:
setRecoveryOSRestoreVersion:
setSplatCryptex1ReleaseType:
setTargetsSyncWithArguments:
splatRollbackSystemVersionPlistContents
T@\"NSString\",&,N,V_systemVersionPlistPath
_defaultsPath
_hasRecoveryOS
_logReturningNil:forKey:valueType:fromBase:withKeyDescription:
clearConfig
encounteredProblems
objectsForKeys:notFoundMarker:
removePersistedState
T@\"NSString\",&,N,V_versionPolicyLayer
_appendToHistory:
_splatVersionKeyForQueryKey:
setBaseDomain:
setHasEmbeddedOS:
setReporterDelegate:
setSfrSystemVersionPlistPath:
trackEnd:atLevel:forModule:
TB,N,V_hasSplat
_acceptEvent:withInfo:issueType:attachedAction:
synchronizeAndReturnError:
whitespaceAndNewlineCharacterSet
numberWithBool:
T@\"SUCoreDiag\",R,N,V_diag
_errorLayer
currentState
dropOnSendFailure:
setSplatSystemVersionPlistContents:
userInfo
T@\"NSObject<OS_dispatch_queue>\",R,N,V_completionQueue
_copyDeviceBoardID
combineWithStats:
dictionaryForKey:
isBridgeInternal
setDiscoveredSuspendedCount:
sharedLogger
writeToURL:options:error:
_stringForNSComparisonResult:
isCorrectlyFormattedBuildVersion:
limitString:toMaxLength:providingSubstitutionMap:
persistData:forKey:shouldPersist:
requiresDocAssetForUpdate
T@\"NSString\",&,N,V_buildVersion
T@\"NSString\",R,&,N,V_fsmState
_deviceSupportsCoreServices
_trackEventOccurrence:withInfo:issueType:
errorUserInfo
sharedErrorInformation
splatReleaseType
setHasBridgeOS:
T@\"NSString\",&,N,V_uniqueInstanceName
TB,R,N,V_simulatorEnabled
Tq,N,V_code
_buildContextFromNVRAMBootArgs
_endFailCount
_simulateQueue
localeWithLocaleIdentifier:
stringByAppendingPathExtension:
_performingEvent
beginCount
formIntersectionWithCharacterSet:
safeLLForKey:defaultValue:
setDeviceSupportsMultiVolumeBoot:
setDiscoveredRunningCount:
substringToIndex:
Tq,R,N,V_simTrigger
_deviceSupportsSplatRollbackRestoreVersion
booleanForKey:
persistDictionary:forKey:shouldPersist:
registerAction:ForEvent:inState:usingDelegate:withInfoClass:
T@\"NSString\",&,N,V_sfrSystemVersionPlistPath
_usageTable
count
eventAlterations
objectForKey:ofClass:forType:
setVolumeIsExternal:
trackStateEvent:previousState:handlingEvent:nextState:performingAction:withInfo:
TB,N,V_isStalled
_activity
_deviceSupportsSplatCryptex1RestoreVersion
_encodeClassNameMappings
_splatRollbackSystemVersionPlistPath
initRequiringSecureCoding:
restoreVersionString
setStoreToPath:
_copySplatCryptex1RestoreVersionPath
_performSimulatedEventAlteration:
_splatRollbackProductVersionExtra
dictionaryWithDictionary:
factoryVersionPlistPath
initForReadingFromData:error:
isEqualErrorEvent:
setWithObjects:
T@\"NSArray\",R,&,N,V_assetProductVersions
T@\"NSString\",&,N,V_splatRollbackSystemVersionPlistPath
associateLayer:withDomain:keyMatchTrueMap:
persistDictionary:forKey:
regularExpressionWithPattern:options:error:
setReason:
Tq,N,V_discoveredSuspendedCount
Tq,N,V_endFailAllIndications
_persistedStatePath
_supportsSplatRestoreVersion
_versionPolicyLayer
T@\"NSString\",&,N,V_releaseType
formUnionWithCharacterSet:
setTaskDescription:
T@\"NSString\",&,N,V_productVersion
_checkedLayer
fileURLWithPath:
setPendingFollowupEvent:
T#,R,N,V_plugin
T@\"NSString\",R,&,N,V_assetState
TB,N,V_defaultLevelLogging
Tq,R,N,V_errorLayer
_copySplatValueForKey:
_deviceSupportsMobileGestalt
currentAccessControl
fsmAction
_sendSplunkEvents:forEventUUID:toServerURL:
assetProductVersions
getAugmentedEvent
initWithRestoreVersion:
numberOfRanges
stateTable
stringByAddingPercentEncodingWithAllowedCharacters:
usageTable
T@\"NSString\",&,N,V_targetedSystemVolume
TB,N,V_isInternal
_location
safeULLForKey:defaultValue:
setSplatProductVersionExtra:
_accessControl
_gestaltKeyForQueryKey:
countByEnumeratingWithState:objects:count:
onceIdleCompletion
setRecoveryOSReleaseType:
simulateQueue
_errorInStackOfLayer:
_errorRecoverable
calendarWithIdentifier:
setDeviceSupportsSFRRestoreVersion:
setPendingFollowupInfo:
substringFromIndex:
T@\"SUCoreEvent\",&,N,V_lastErrorEvent
_factoryRestoreVersion
_stateEventCount
_versionSUCore
errorInformation
eventForEventString:
sfrRestoreVersionPlistPath
T@\"NSDictionary\",&,N,V_sfrSystemVersionPlistContents
T@\"NSDictionary\",&,N,V_sfrRestoreVersionPlistContents
Tq,N,V_failedSendCount
_supportsSFR
setSplunkURL:
splatCryptex1SystemVersionPlistPath
stringByReplacingOccurrencesOfString:withString:
_locateEventForModule:forIdentity:withTrigger:forEvent:inState:
beginTransactionWithName:
setSplatRollbackProductVersion:
T@\"NSString\",&,N,V_bridgeVersionPlistPath
isBootedOSSecureInternal
setDeviceSupportsCoreServices:
setEndFailCount:
unsignedLongLongValue
endSuccessCount
_copySplatRollbackObjectsPath
_fsmState
_splunkAccessCreated
bytes
deviceSupportsPreservedFactoryVersion
location
setFaultCount:
T@\"NSString\",&,N,V_activity
TB,R
_awaitingRetry
_isValidEvent:
archivedDataWithRootObject:requiringSecureCoding:error:
initByCombining:withAdditonal:
setErrorIndicationsCount:
setRecoveryOSRestoreVersionPlistContents:
zone
arrayWithObjects:count:
endTransaction:withName:
rangeAtIndex:
rangeOfString:
resetCodeCoverageForName:
trackEnd:atLevel:forModule:withIdentifier:withResult:withError:
_deviceSupportsRecoveryOSSystemVersion
getConfig
containsObject:
T@\"NSString\",&,N,V_actionText
T@\"NSDictionary\",R,N,V_stateTable
T@\"NSString\",&,N,V_splatBuildVersion
_extendedStateQueue
_reporterDelegate
layerInformation
numberWithInt:
T@\"NSString\",&,N,V_targetOSBuild
_associateLayer:withDomain:minCode:maxCode:
_copySFRSystemVersionValueForKey:
_isStalled
hasSFR
persistedStateQueue
sharedHistory
trackFault:forReason:withResult:withError:
TB,N,V_deviceSupportsRecoveryOSSystemVersion
Tq,N,V_failureIndicationsCount
_count
_recoveryOSSystemVersionPlistPath
checkedDescription
setLastUUID:
inProcessConfig
_supportsCoreServices
_synchonizeDiscoveredCanceling:forActiveEvent:withFileUUIDsToRetry:
checkedIndicationsSummary
compare:
isMajorOSUpdate:
persistData:forKey:forType:shouldPersist:
splunkAccessCreated
T@\"NSString\",R,C
_fsmName
_restoreVersionKeyForQueryKey:
_splatProductVersionExtra
checkedSystemPartitionSize
decimalDigitCharacterSet
delegateCallbackQueue
initWithPhase:isStalled:portionComplete:totalWrittenBytes:totalExpectedBytes:remaining:actionText:taskDescription:
T@\"NSMutableDictionary\",&,N,V_encodeClassNameMappings
Ti,R,N,V_startAt
decodeObjectOfClasses:forKey:
isStalled
lastUUID
loadPersistedState
processInfo
recoveryOSSystemVersionPlistContents
T@\"NSObject<OS_dispatch_queue>\",R,N,V_trackingQueue
T@\"NSString\",&,N,V_measurementAlgorithm
T@\"NSString\",&,N,V_currentState
deviceSupportsCoreServices
initWithAction:onTrigger:forMachine:atEvent:inState:alteration:startAt:endAt:assetBuildVersions:assetProductVersions:assetAttributesPlist:assetState:updateInfoPlist:errorDomain:errorCode:errorUserInfo:errorRecoverable:
initWithSuiteName:
safeTriStateForKey:defaultValue:
splatCryptex1RestoreVersionPlistPath
T@\"NSString\",&,N,V_checkedDomain
TB,N,V_deviceSupportsRecoveryOSRestoreVersion
Ti,R,N,V_endAt
retain
setVolumeUUID:
performSelector:withObject:
fsmName
_fsmEvent
_splatSystemVersionPlistContents
getCodeCoveragePathForName:
initForDomain:withCode:ofCodeName:indicating:ifKeyTrue:keyMatchTrueMap:
Tq,R,N,V_errorRecoverable
_registerAction:ForEvent:inState:usingDelegate:withInfoClass:actionTable:loggingRegistration:
_supportsFactoryVersion
adjustTargetingSystemVolume:
anomalyCount
checkedSummary
dataUsingEncoding:
longValue
URLSession:didBecomeInvalidWithError:
_awaitRetryingFileUUID:
_bridgeVersion
assetState
recoveryOSRestoreVersionPlistPath
safeSubDescriptionAtNestedLevel:instanceAtLevel:withMaxValueLength:providingSubstitutionMap:
setTargetOSBuild:
targetedSystemVolume
T@\"NSDictionary\",&,N,V_recoveryOSRestoreVersionPlistContents
minCode
_attributesOfErrorForDomain:withCode:codeName:indicating:ifKeyTrue:keyMatchTrueMap:
_hasBridgeOS
_trackingQueue
persistSecureCodedObject:forKey:
_determineEventExtensions
_oslog
_sfrSystemVersionPlistContents
appendFormat:
autorelease
deviceSupportsMultiVolumeBoot
informationQueue
instanceName
UUID
_previous
augmentEvent:withError:
bridgeVersion
errorLayer
removeObjectForKey:
safeDescriptionWithName:
setPsusAssetPath:
T@\"NSString\",&,N,V_splatRollbackRestoreVersionPlistPath
dataForKey:
handleSendFinishedInvalidFileUUID:withError:
reporterDelegate
setFaultIndicationsCount:
splatSystemVersionPlistPath
string
URLSession:task:didCompleteWithError:
_supportsPreservedFactoryVersion
_untrackedOccurrences
deviceSupportsSplatRollbackRestoreVersion
endAt
initIgnoringSuccessRelated
_parseOptionalEntriesInLineFromWords:argStartAt:argEndAt:argDuration:argUntilStop:argAssetBuildVersions:argAssetProductVersions:argAssetAttributesPlist:argAssetState:argUpdateInfoPlist:argErrorDomain:argErrorCode:argErrorUserInfo:argErrorRe
_path
nameForSUCoreCode:
setIsBridgeInternal:
allKeys
T@\"NSURL\",&,N,V_serverURL
assetAttributesPlist
setFailureCount:
trackBegin:
_buildGroup
T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_accessQueue
T@\"NSString\",&,N,V_recoveryOSProductVersion
preservedFactoryVersionPlistPath
setTargetOSVersion:
_releaseType
objectForKey:
T@\"NSArray\",R,N,V_safeUserInfoValues
controlCharacterSet
initWithLong:
_recoveryOSRestoreVersionPlistPath
_synchonizeDiscoveredRunning:forActiveEvent:withFileUUIDsToRetry:
_sysCtlKeyForQueryKey:
clearAllEventAlterations
trackEnd:atLevel:withResult:withError:
indicationsForError:matchingMask:
setLastReportedUUID:
setSfrRestoreVersionPlistPath:
setProductType:
isSuccess
minorVersion
_copyRecoveryOSSystemVersionValueForKey:
copyPathForPersistentData:error:
decodeFloatForKey:
sendEvent:
_endFailIndicationsCount
_supportsRestoreVersion
postProtectedEvent:
_alteration
_synchonizeDiscoveredSuspended:forActiveEvent:withFileUUIDsToRetry:
typeName
T@\"NSObject<OS_dispatch_queue>\",R,N,V_simulateQueue
safeUserInfoValueClasses
T@\"NSString\",?,R,C
TB,N,V_deviceSupportsSFRSystemVersion
_recoveryOSRestoreVersionPlistContents
activeSendTaskCount
getBoolConfigForKey:
substringWithRange:
_copyFactoryVersionValueForKey:
codeName
setTrackStats:
supportsSecureCoding
deviceSupportsSplatSystemVersion
T@\"NSMutableArray\",&,N,V_trackingHistory
setSplatSystemVersionPlistPath:
_copyCoreServicesValueForKey:
bridgeRestoreVersion
setDecodeClassNameMappings:
_psusAssetPath
arrayIsEqual:to:
selectCompletionQueue:
statusCode
_fullName
safeLLForKey:
setFaultAllIndications:
Tq,N,V_accessControl
_indications
buildSplunkServerURLFromBase:
commonDomain
componentsJoinedByString:
initWithUUIDBytes:
_parseEventBooleanFromString:destination:
persistState
setSfrProductVersion:
T@\"NSString\",&,N,V_taskDescription
_simulatorEnabled
initStoringToPath:
persistSecureCodedObject:forKey:shouldPersist:
_parseBridgeOSBuildInformationFromDevice:
_syncedVersion
isSharedDiag
setRecoveryOSSystemVersionPlistPath:
setTrackingHistory:
_recoveryOSRestoreVersion
_splatReleaseType
numberIsEqual:to:
setBridgeVersion:
setFailureIndicationsCount:
splatRollbackReleaseType
T@\"NSString\",&,V_baseDomain
TB,N,V_isBridgeInternal
TB,R,N
_checkedIndications
_restoreVersionPlistContents
allFields
init
initWithUTF8String:
T@\"NSString\",&,N,V_splatRollbackReleaseType
_identityName
_simAction
attributesOfErrorForDomain:withCode:codeName:
deviceSupportsFactoryVersion
next
T@\"NSDictionary\",&,N,V_keyMatchTrueMap
T@\"NSString\",&,N,V_recoveryOSRestoreVersion
dataWithJSONObject:options:error:
_logReturningNil:forKey:valueType:
registeredActionTable
setDropEventsOnSendFailure:
stateSafeGetConfig
useDomain:
_initMachine:ofInstance:withTable:startingIn:usingDelegate:registeringAllInfoClass:registeringAndActivating:
TB,N,V_hasSplatOnlyUpdateInstalled
decodeBoolForKey:
_deviceSupportsSplatSystemVersion
self
setActiveSendTaskCount:
splatRestoreVersion
startState
trackBegin:atLevel:forModule:withIdentifier:
_assetState
stringByPaddingToLength:withString:startingAtIndex:
copyTrackedStatsClearingAfter:droppingMatchedIndications:
setPreservedFactoryVersionPlistPath:
setupLogFile
setSplatCryptex1ProductVersion:
T#,R,&,N,V_eventInfoClass
_factoryVersionPlistContents
_reporter
T@\"NSString\",R,&,N,V_path
_getMajorVersionFromBuildVersion:
sharedDiag
TB,N,V_deviceSupportsSplatCryptex1RestoreVersion
_copyStringValueForKey:
_deviceSupportsSFRSystemVersion
T@\"NSError\",&,N,V_error
psusAssetPath
selectDelegateCallbackQueue:
volumeUUID
T@\"NSString\",&,N,V_phase
setNumberStyle:
_attemptedSendCount
_dropEventsOnSendFailure
safeULForKey:
setRecoveryOSSystemVersionPlistContents:
T@\"NSString\",&,N,V_versionSUCore
_sendCoreEvents:secondEvent:
absoluteString
lockFD
storeToPath
_deviceSupportsMultiVolumeBoot
_factoryVersionPlistContentsForKey:
shouldFallbackToCustomerScan
T@\"NSString\",&,N,V_splatRestoreVersion
_associateLayer:withDomain:minCode:maxCode:indicating:ifKeyTrue:keyMatchTrueMap:
_descriptionStateEvent
_miscellaneousTaksQueue
checkedIndicationsDescription
failureAllIndications
setDeviceSupportsRestoreVersion:
setNext:
T@\"NSString\",&,N,V_restoreVersion
TB,N,V_deviceSupportsFactoryVersion
Tq,N,V_failureAllIndications
_createEmptyPersistedState
_supportsSFRRestoreVersion
adoptAllEventAlterations:
setProductVersion:
splatCryptex1RestoreVersionPlistContents
_portionComplete
sfrProductVersion
stringFromTriState:
Tq,R,N,V_simAction
_actionText
setBridgeVersionPlistContents:
_assetAttributesPlist
initWithBase64EncodedString:options:
setDeviceSupportsSplatSystemVersion:
setFailedSendCount:
splatCryptex1ProductVersion
Tq,N,V_anomalyIndicationsCount
T@\"NSString\",&,N,V_preservedFactoryVersionPlistPath
T@\"NSData\",&,N,V_measurement
TB,N,V_deviceSupportsSplatCryptex1SystemVersion
setHasRecoveryOS:
setSplatCryptex1RestoreVersion:
activeEventsState
checkedLayer
removeAllObjects
.cxx_destruct
T@\"NSString\",R,&,N,V_codeName
_persistedStateQueue
deviceSupportsSplatRollbackSystemVersion
initOfType:fromLocation:forReason:withCode:withError:
targetOSTrain
T@\"NSString\",&,N,V_pendingFollowupEvent
Tq,N,V_indications
_beginCount
_isBootedOSSecureInternal
_recoveryOSSystemVersionPlistContents
collectTrackedStatsClearingAfter:droppingMatchedIndications:completion:
failureIndicationsCount
splunkStateQueue
Tq,N,V_errorIndicationsCount
_splatSystemVersionPlistPath
T@\"NSString\",&,N,V_sfrProductVersion
_eventExtensionsDetermined
_sfrProductVersion
factoryRestoreVersion
setIsBootedOSSecureInternal:
trackEnd:atLevel:
dateIsEqual:to:
T@\"NSString\",&,N,V_splatCryptex1SystemVersionPlistPath
Tq,R,N,V_minorVersion
decodeIntForKey:
isPersistedStateLoaded
persistedPolicyVersion
writeToFile:options:error:
activateMachine
T@\"NSString\",R,&,N,V_fsmName
pendingFollowupInfo
phase
_getJSONDataFromPayload:withFileUUID:forEventUUID:
_hwModelString
_queryMethodForKey:
initWithCategory:
splatRollbackRestoreVersionPlistContents
initMachine:withTable:startingIn:usingDelegate:registeringAllInfoClass:
persistDictionary:forKey:forType:shouldPersist:
T@\"NSURLSessionConfiguration\",&,N,V_inProcessConfig
_getSplunkServerURL:
associateLayer:withDomain:
cStringUsingEncoding:
Tq,N,V_endSuccessCount
_checkedCode
_splatCryptex1SystemVersionPlistContents
sfrSystemVersionPlistContents
splatCryptex1ReleaseType
TB,N,V_deviceSupportsMobileGestalt
splunkURL
timeIntervalSince1970
_marketingProductName
dumpTracked:dumpingTo:usingFilename:clearingStatistics:clearingHistory:
state
T@\"NSString\",&,N,V_splatCryptex1ProductVersion
_lastAlteration
safeDateForKey:
_incrementActiveSendCount:
_param
_splatRollbackBuildVersion
dictionaryIsEqual:to:
productType
TB,N,V_eventExtensionsDetermined
_splatRollbackVersionPlistContentsForKey:
setDeviceSupportsPreservedFactoryVersion:
T@\"NSString\",&,N,V_splatProductVersionExtra
_triggerFromString:
handleSendFinishedWithFileUUID:sendSucceeded:withStatusCode:withError:
integerValue
targetOSVersion
teardownMachine
_filesystemBaseDir
_sfrSystemVersionPlistPath
T@\"NSString\",&,N,V_splatCryptex1BuildVersion
_lastUUID
recoveryOSRestoreVersionPlistContents
setHasSFR:
_loadPluginFromPath:
errorCode
_stateTable
_sfrReleaseType
indications
previous
setSplatCryptex1SystemVersionPlistContents:
_actionDelegate
setDeviceSupportsMobileGestalt:
T@\"NSString\",R,&,N,V_fsmAction
Tq,N,V_beginCount
T@\"NSString\",&,N,V_param
Td,N,V_estimatedTimeRemaining
Tf,N,V_portionComplete
deviceSupportsRecoveryOSSystemVersion
isSharedIPad
T@\"NSString\",R,&,N,V_updateInfoPlist
_newExistingFileUUIDs
setBridgeVersionPlistPath:
splatRollbackRestoreVersion
_pendingFollowupInfo
setDeviceSupportsSFRSystemVersion:
performingEvent
failedSendCount
_activeSendTaskCount
_parseDictionaryFromString:destination:
_supportsSplatSystemVersion
setRecoveryOSBuildVersion:
_splatCryptex1ReleaseType
safeSummary
setIsInternal:
Tq,N,V_anomalyCount
_triggerName
postProtectedEvent:withInfo:
setDeviceSupportsRecoveryOSSystemVersion:
dumpCodeCoverageForName:
objectForKey:ofClass:
extendedStateQueue
hwTarget
initMachine:withTable:startingIn:
setHwTarget:
_descriptionFSM
_next
initWithPhase:isStalled:portionComplete:remaining:
setPrevious:
setSplatRestoreVersion:
sendEvent:returningFinalEventDictionary:
setDeviceSupportsFactoryVersion:
getNumberConfigForKey:
T@\"NSString\",&,N,V_restoreVersionString
T@,R,W,N,V_actionDelegate
date
```
