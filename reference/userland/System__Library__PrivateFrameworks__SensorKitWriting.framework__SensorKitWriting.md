# `/System/Library/PrivateFrameworks/SensorKitWriting.framework/SensorKitWriting`

iOS 27.2 dyld shared cache image. Version `1039.0.1.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/TCC.framework/TCC`
- `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime`
- `/usr/lib/libz.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 18 classes, 18 protocols, 318 methods, 80 properties

### Class pages

Every class and protocol, with its methods: [`NSCoding`](../objc/NSCoding_SensorKitWriting.protocol.md), [`NSCopying`](../objc/NSCopying_SensorKitWriting.protocol.md), [`NSFastEnumeration`](../objc/NSFastEnumeration_SensorKitWriting.protocol.md), [`NSObject`](../objc/NSObject_SensorKitWriting.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_SensorKitWriting.protocol.md), [`SRAuthorizationClient`](../objc/SRAuthorizationClient_SensorKitWriting.md), [`SRAuthorizationClientDelegate`](../objc/SRAuthorizationClientDelegate_SensorKitWriting.protocol.md), [`SRAuthorizationStore`](../objc/SRAuthorizationStore_SensorKitWriting.md), [`SRAuthorizationStoreDelegate`](../objc/SRAuthorizationStoreDelegate_SensorKitWriting.protocol.md), [`SRAuthorizationStoreReaderAuthorizationDelegate`](../objc/SRAuthorizationStoreReaderAuthorizationDelegate_SensorKitWriting.protocol.md), [`SRDaemonNotification`](../objc/SRDaemonNotification_SensorKitWriting.md), [`SRDaemonNotificationDelegate`](../objc/SRDaemonNotificationDelegate_SensorKitWriting.protocol.md), [`SRDatastore`](../objc/SRDatastore_SensorKitWriting.md), [`SRDefaults`](../objc/SRDefaults_SensorKitWriting.md), [`SRError`](../objc/SRError_SensorKitWriting.md), [`SRFrameStore`](../objc/SRFrameStore_SensorKitWriting.md), [`SRFramesStoreOffsetEnumerator`](../objc/SRFramesStoreOffsetEnumerator_SensorKitWriting.md), [`SRMemoryMapping`](../objc/SRMemoryMapping_SensorKitWriting.md), [`SRSensorDescription`](../objc/SRSensorDescription_SensorKitWriting.md), [`SRSensorDescriptionEnumerator`](../objc/SRSensorDescriptionEnumerator_SensorKitWriting.md), [`SRSensorKitServiceClientAuthorizationListening`](../objc/SRSensorKitServiceClientAuthorizationListening_SensorKitWriting.protocol.md), [`SRSensorKitServiceClientProtocol`](../objc/SRSensorKitServiceClientProtocol_SensorKitWriting.protocol.md), [`SRSensorKitServiceClientWriting`](../objc/SRSensorKitServiceClientWriting_SensorKitWriting.protocol.md), [`SRSensorKitServiceServerAuthorizationListening`](../objc/SRSensorKitServiceServerAuthorizationListening_SensorKitWriting.protocol.md), [`SRSensorKitServiceServerWriting`](../objc/SRSensorKitServiceServerWriting_SensorKitWriting.protocol.md), [`SRSensorWriter`](../objc/SRSensorWriter_SensorKitWriting.md), [`SRSensorWriterAuthorizationDelegate`](../objc/SRSensorWriterAuthorizationDelegate_SensorKitWriting.protocol.md), [`SRSensorWriterClient`](../objc/SRSensorWriterClient_SensorKitWriting.md), [`SRSensorWriterDelegate`](../objc/SRSensorWriterDelegate_SensorKitWriting.protocol.md), [`SRSensorWriterSensorConfigurationDelegate`](../objc/SRSensorWriterSensorConfigurationDelegate_SensorKitWriting.protocol.md), [`SRSensorsCache`](../objc/SRSensorsCache_SensorKitWriting.md), [`SRSourceDevice`](../objc/SRSourceDevice_SensorKitWriting.md), [`SRTCCStore`](../objc/SRTCCStore_SensorKitWriting.protocol.md), [`SRTCCStorePassThrough`](../objc/SRTCCStorePassThrough_SensorKitWriting.md), [`SRWritingStats`](../objc/SRWritingStats_SensorKitWriting.md)

### Classes

`NSString`, `SRAuthorizationClient`, `SRAuthorizationStore`, `SRDaemonNotification`, `SRDatastore`, `SRDefaults`, `SRError`, `SRFrameStore`, `SRFramesStoreOffsetEnumerator`, `SRMemoryMapping`, `SRSensorDescription`, `SRSensorDescriptionEnumerator`, `SRSensorWriter`, `SRSensorWriterClient`, `SRSensorsCache`, `SRSourceDevice`, `SRTCCStorePassThrough`, `SRWritingStats`

### Protocols

`NSCoding`, `NSCopying`, `NSFastEnumeration`, `NSObject`, `NSSecureCoding`, `SRAuthorizationClientDelegate`, `SRAuthorizationStoreDelegate`, `SRAuthorizationStoreReaderAuthorizationDelegate`, `SRDaemonNotificationDelegate`, `SRSensorKitServiceClientAuthorizationListening`, `SRSensorKitServiceClientProtocol`, `SRSensorKitServiceClientWriting`, `SRSensorKitServiceServerAuthorizationListening`, `SRSensorKitServiceServerWriting`, `SRSensorWriterAuthorizationDelegate`, `SRSensorWriterDelegate`, `SRSensorWriterSensorConfigurationDelegate`, `SRTCCStore`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSArray",R,N) legacyResearchStudyBundleIDs;
@property (T@"NSString",R,N) legacyResearchStudyEntitlement;
@property (TB,N) dataCollectionEnabled;
@property (TB,N) firstRunOnboardingCompleted;
@property (T@"NSDictionary",C,V_readerAuthorizationValues) readerAuthorizationValues;
@property (T@"NSDictionary",C,V_readerLastModifiedAuthorizationTimes) readerLastModifiedAuthorizationTimes;
@property (T@"NSDictionary",C,V_writerAuthorizationValues) writerAuthorizationValues;
@property (TB,V_sensorKitActive) sensorKitActive;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_updateQueue) updateQueue;
@property (T@"NSDictionary",C,V_readerAuthorizationGroups) readerAuthorizationGroups;
@property (T@"NSDictionary",C,V_writerAuthorizationGroups) writerAuthorizationGroups;
@property (T@"NSSet",&,V_sensors) sensors;
@property (T@"NSString",R,C,V_name) name;
@property (T@"NSString",R,C,V_authorizationService) authorizationService;
@property (T@"NSArray",R,C,V_relatedSettingsCategories) relatedSettingsCategories;
@property (T@"NSString",R,C,V_publicEntitlementValue) publicEntitlementValue;
@property (T@"NSString",R,C) sampleClass;
@property (T@"NSString",R,C) exportingSampleClass;
@property (T@"NSString",R,C) localizedAdditionalSampleDataNote;
@property (T@"NSString",R,C,V_infoPlistAuthorizationCategory) infoPlistAuthorizationCategory;
@property (TB,R) metadataEnabled;
@property (TB,R) sensorConfigurationEnabled;
@property (T@"NSString",R,C,V_writerAuthorizationService) writerAuthorizationService;
@property (Tq,R,V_authorizationVersion) authorizationVersion;
@property (T@"NSString",R,C,V_onDemandWriterService) onDemandWriterService;
@property (TB,R) supportsCurrentPlatform;
@property (T@"NSString",R,C,V_authorizationStoreCohort) authorizationStoreCohort;
@property (T@"NSString",R,C,V_legacyName) legacyName;
@property (T@"NSArray",R,C,N,V_filters) filters;
@property (T@"NSSet",R,C,N) eligibleDaemons;
@property (Td,R,N,V_roundingInterval) roundingInterval;
@property (Tq,R,N,V_datastoreBackend) datastoreBackend;
@property (T@"NSString",C,V_sensorIdentifier) sensorIdentifier;
@property (T@"SRDatastore",R,&) datastore;
@property (T@"NSDictionary",&,V_nextDatastoreFiles) nextDatastoreFiles;
@property (TB,V_requestNewSegmentInFlight) requestNewSegmentInFlight;
@property (TB,V_authorized) authorized;
@property (TB,V_connectionDidInterrupt) connectionDidInterrupt;
@property (TB,V_connectionDidInvalidate) connectionDidInvalidate;
@property (T@"NSXPCConnection",&,V_connection) connection;
@property (TB,V_retryGetMonitoring) retryGetMonitoring;
@property (Tq,V__writerAuthorizationStatus) _writerAuthorizationStatus;
@property (T@"NSString",R,&,N,V_writerAuthorizationService) writerAuthorizationService;
@property (T@"<SRTCCStore>",&,V_tccStore) tccStore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_writerAuthorizationUpdateQueue) writerAuthorizationUpdateQueue;
@property (T@"SRAuthorizationStore",&,N,V_authStore) authStore;
@property (T@"NSCache",&,N,V_eligibilityCache) eligibilityCache;
@property (Td,N,V_roundingInterval) roundingInterval;
@property (T@"NSDictionary",&,V_lastMetadata) lastMetadata;
@property (TQ,V_lastMetadataContinuousTime) lastMetadataContinuousTime;
@property (T@"NSDictionary",&,V_lastConfiguration) lastConfiguration;
@property (TQ,V_lastConfigurationContinuousTime) lastConfigurationContinuousTime;
@property (T@"SRWritingStats",&,N,V_writingStats) writingStats;
@property (T@"NSArray",C,N,V__requestedConfigurations) _requestedConfigurations;
@property (TB,GisMonitoring) monitoring;
@property (T@"<SRSensorWriterDelegate>",W) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SRSensorWriter",W,V_writer) writer;
@property (T@"NSString",&,N,V_ephemeralIdentifier) ephemeralIdentifier;
@property (T@"NSData",&,N,V_encryptedIdentifier) encryptedIdentifier;
@property (T@"NSString",R,C,N) localIdentifier;
@property (T@"NSString",R,C,N,V_manufacturer) manufacturer;
@property (T@"NSString",R,C,N,V_model) model;
@property (T@"NSString",R,C,N,V_hardwareVersion) hardwareVersion;
@property (T@"NSString",R,C,N,V_firmwareVersion) firmwareVersion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N,V_totalSegmentsCreated) totalSegmentsCreated;
@property (Td,R,N,V_totalFillDuration) totalFillDuration;
@property (Td,N,V_segmentCreationTime) segmentCreationTime;
```

## Strings (312)

```
StorageBackend
com.apple.SensorKit.mobilityMetrics
v12@?0i8
No space available to write samples
@\"NSString\"16@?0@\"SRSensorDescription\"8
PublicEntitlementValue
com.apple.SensorKit.wristTemperature
com.apple.SensorKit.hearing.acousticSettings
com.apple.private.SensorKit.audio.siri
MetadataSize
SegmentMinimumFactor
SRErrorNoAuthorizationRecovery
manufacturer
localIdentifier
v16@?0@\"NSString\"8
Phone
com.apple.SensorKit.sleep.sessions
OnDemandWriterService
Writer Not Monitoring
SRErrorPromptDeclined
!
SRAuthorizationStore.updateQueue
WriterAuthorizationService
source
SegmentFillDuration
com.apple.SensorKit
com.apple.SensorKit.resetDatastore
SRDeletionRecord
Metadata
com.apple.SensorKit.motion.gyroscope
eligible
Global setting not enabled
SRErrorFetchRequestInvalid
Name
com.apple.private.SensorKit.fallstatistics
com.apple.SensorKit.heart.rate
v24@?0@\"NSDictionary\"8@?<@\"NSString\"@?@\"SRSensorDescription\">16
TelephonyApp
RoundingIntervalSecs
com.apple.SensorKit.als
sensorConfiguration
Datastore
Writer Input was invalid
hardwareVersion
/System/Library
AuthorizationStore
com.apple.SensorKit.faceMetrics
com.apple.private.SensorKit.pedometer.stridecalibration
com.apple.SensorKit.speechMetrics.siri
com.apple.SensorKit.bedSensing.beddit
No device identifier could be found
Provided sample is out of order from previous samples
com.apple.SensorKit.visits
.tombstones
defaults
SRMemoryMapping
com.apple.SensorKit.writer
SRErrorDataInaccessibleRecovery
v40@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSDictionary\"24q32
AuthorizationVersion
EligibleDaemons
%@ (%p): name: %@, authService: %@, relatedSettings: %@, publicEntitlement: %@, sampleClass: %@, exportingSampleClass: %@, additions: %@, onDemandWriterId: %@, writerAuthService: %@, supportedPlatforms: %@, auth store cohort: %@, legacyName
com.apple.SensorKit.onWristState
com.apple.SensorKit.mediaEvents
Internal Error
No available memory mapped to write sample
Additions
com.apple.SensorKit.odometer
com.apple.SensorKit.soundDetection.siri
SegmentResizeFactor
TCCStore
Provided sample is too large
SRErrorNoAuthorization
model
(null)
com.apple.SensorKit.deviceUsageReport
SegmentSize
v16@?0@\"NSError\"8
v12@?0C8
Sensor Configuration is invalid
com.apple.SensorKit.significantTimeChange
v16@?0@\"NSArray\"8
com.apple.SensorKit.speechEmotion.siri
com.apple.sensorkitd.updateAuthorizations
com.apple.private.SensorKit.audio.telephony
com.apple.private.SensorKit.odometer.suitability
SourceHMACKey
com.apple.SensorKit.phoneUsageReport
SensorsCache
SRLogDaemonNotification
SRInfoPlistAuthCategory
com.apple.SensorKit.ambientPressure
<%@ (%p)> [%@]:\n{\n  sessionStart: %f (CF: %f),\n  bytesWritten: %llu,\n  samplesWritten: %lu,\n  segmentCreationTime: %f,\n  rateAdjustedSegmentSize: %lu,\n  averageFillDuration: %f\n}
FrameStore
LegacySampleClassLinkedBefore
AuthorizationStoreCohort
SRErrorInvalidEntitlement
com.apple.SensorKit.authorization
@\"NSMutableDictionary\"16@?0@\"NSString\"8
AdditionalDataNote
SensorConfiguration
com.apple.SensorKit.ECG
SRLogSourceDevice
com.apple.SensorKit.writerAuthorizationUpdate
v20@?0B8@\"NSError\"12
RelatedSettingsCategories
LegacySampleClass
not eligible
SRErrorDomain
com.apple.tcc.access.changed
Writer does not have explicit authorization
error
DatastoreVersion
Your bundle's Info.plist must have an %@ key
Required app is not installed
Provided sample is from the future
encryptedIdentifier
com.apple.SensorKit.prerequisitesUpdated
com.apple.SensorKit.motion.headphone
com.apple.sensorkit.dummy-bundle-id
MessagingApp
com.apple.SensorKit.speechEmotion.telephony
Frameworks
AuthorizationClient
Writer
com.apple.private.SensorKit._compositeBundle
AuthService
LegacyName
Enabled
samples
No new authorization groups were requested
Framework datastore state is invalid
SRSensorReader
com.apple.SensorKit.motion.accelerometer
com.apple.private.SensorKit.speech.metrics
com.apple.SensorKit.soundDetection.telephony
com.apple.SensorKit.physicalActivityEvents
v16@?0@\"NSDictionary\"8
Required onboarding not completed
Writer Not Authorized
firmwareVersion
SensorKit
Prompt is cancelled
SensorDescriptions
com.apple.SensorKit.pedometer.data
com.apple.SensorKit.cardioMetrics
Potentially overwriting whatever data is currently there
SRErrorDataInaccessible
MaxAllowedMappedPages
com.apple.SensorKit.messagesUsageReport
com.apple.SensorKit.hearing.headphoneSettings
Prompt Busy
/var/mobile/Library
DeveloperOptOut
com.apple.private.SensorKit.elevation
metadata
The requested bundle authorization is being requested for could not be found
plist
SensorKit.framework
SRLogDataStream
Filters
SegmentPaddingFactor
v8@?0
SampleClass
com.apple.SensorKit.keyboardMetrics
com.apple.SensorKit.PPG
com.apple.SensorKit.speechMetrics.telephony
Connection Not Found
Time synchronization state is invalid
%@ (%p): localIdentifier:%@, manufacturer:%@, model:%@, hardwareVersion:%@, firmwareVersion:%@
ExportingSampleClass
SupportedPlatforms
Data stream defined without an authorization service: %{public}@
Writing Stats: %@\nExpected segment lifetime: %{public}f\nDefault segment size: %lu
Failed to register for prerequisites notification status %{public}d, registration token %{public}d
Failed to get sync proxy to daemon, error %{public}@
Failed to get file descriptor for NSFileHandle. %{public}@
TCC has returned from prompt with status: %{public, bool}d
Bundle identifier %{public}@ %{public}@ for writing
Failed to register for TCC notifications.  Got status %{public}d
Authorized Bundle Ids for %{public}@, %{public}@
Failed to register for darwin notification %{public}@, status %{public}d, registration token %{public}d
Data stream defined without an Info.plist authorization category: %{public}@
Unable to read frames file segment header %{public}@. Received data of %{public}lu length. Potentially overwriting whatever data is currently there
Error carrying over previous configuration because %{public}@
[%@] monitoring set to %{public, bool}d
[%{public}@] does not have explicit writer authorization (status: %{public}ld). Setting monitoring to %{public, bool}d
[%{public}@] Flushing datastore to disk
Resizing file %{private}@ to %llu bytes
Writer instance is nil so not setting the monitoring flag
No last modified date for authorization of bundle %{public}@, service: %{public}@
Failed to cancel notification %{public}@. status %{public}d
Segment header magic number %{public}.4s doesn't match %{public}.4s in file %{public}@. Potentially overwriting whatever data is currently there
Could not retrieve authorization override information for TCC service %{public}@
Timestamp is from the future. Input %f, Current: %f
Registering for prerequisites notification
Failed to cancel notification status %{public}d
Got a notification for %{public}@ to re-connect to the daemon
writing to %{public}p with length %{public}lu would go past end of file (%{public}p)
Authorization set to %{public, bool}d for %@
No segment name provided for the segment header
Trying to write a sample of 0 bytes
[%@] Error registering with daemon because %{public}@. Setting monitoring to false
Ignoring duplicate daemon authorization update
[%@] monitoring is already %{public, bool}d. Ignoring update
Authorization state has not yet been sent from the daemon.
Deauthorized Bundle Ids for %{public}@, overridden %{public, bool}d, %{public}@
No disk space available, dropping data
metadata segment: %@, metadata frame time: %f, sample time: %f, current metadata object: %p
Daemon has synced time. Requesting a new segment and time info
Error requesting new segment %{public}@
Trying to get monitoring flag after daemon restart
Expanding the mapped region to %llu bytes while a new segment is fetched
No space left to write to the mapped region
Trying to write %{public}zd but only have %{public}llul available. Dropping the data.
No sample file received so clearing the datastore
Failed to find authorization service for %{public}@. Unable to request authorization
Source object should not have both an encrypted identifier and nonencrypted identifier.
Received notification of prerequisite change
Asked to stop listen for TCC updates but we are already not listening
Connection to daemon interrupted
Failed to register for TCC notifications. Got status %{public}d
Shouldn't be getting an auth update for %{public}@
Source Device identifier not yet encrypted.
Asked to listen for TCC updates but we're already listening
Found a linked before version but no legacy sample class
Sample too large %{public}zu but only %u supported
[%@] Error requesting file handle %{public}@. Setting monitoring to false
Retrieving initial authorization state
Not enough free space (%{public}zu) to write %{public}zu. Attempting to expand the mapped region
Failed to connect to daemon because %{public}@
Unregistering for prerequisites notification
Deauthorized Bundle Ids for %{public}@, %{public}@
Unable to mmap storage file %{public}@ because %{public, darwin.errno}d
Failed to msync because %{public, darwin.errno}d
More bytes requested %{public}zu than the capacity %{public}zu. Client should call -freeSpace: to avoid this
Daemon has reset our datastore. Requesting a new segment
Trying to write null sample
Set source to %{private}@
Frame should come in chronological order. Input %f < last %f
Segment name is too large to store in the segment header. Truncating the segment name of %{public}zu to %{public}lu
Got a notification for %{public}@
[%{public}@] Daemon is resetting the writer datastore, asking for a new segment
Carrying over previous configuration: %@
Writer is authorized for %{public}@ connecting to daemon to determine monitoring state
Cached description for %{public}@, %{public}@
Connection to daemon invalidated
Unable to get proxy object to request a new segment because %{public}@
[%{public}@] Got authorization client update: data collection: %{public, bool}d, onboarding: %{public, bool}d, authorized: %{public}@, denied: %{public}@
reset authorization for services %@
Unregistering for darwin notification on %{public}@
Failed to connect with daemon
Missing encrypted identifier.
Finalizing %{public}@ to %{public}llu bytes
Daemon has restarted after being invalidated. Re-establishing connection
%{public}@ not found
Failed to locate the /System/Library directory because %{public}@
Failed to resize backing file
Tearing down frame store for %{public}@
Checksums don't match. Header: %llu, Generated checksum: %{public}lu. Skipping frame.
Reset authorization for service %@ and bundle id: %{public}@
Frames file %{public}@ is invalid because the current size is less than a valid segment header. Potentially overwriting whatever data is currently there.
Failed to find a segment header while writing. Dropping incoming data
Unable to unmap %{public}p size %zu because %{public, darwin.errno}d
Error fetching eligibility %{public}@
Failed to parse %{public}@ because %{public}@
%{public}@ authorized: %{private}@
Couldn't find a TCC service in the TCC access dictionary %{public}@
Authorized Bundle Ids for %{public}@, overridden %{public, bool}d, %{public}@
Not mapping an empty file %{public}@
Authorization Changed for bundle id %{public}@ for sensors %{public}@
[%{public}@] Creating a new datastore with samples: %{public}@, metadata: %{public}@, configuration: %{public}@, defaults: %{public}@
Error trying to archive metadata %{public}@ %{public}@
Missing key to secure identifier with.
%{public}@ last modified times: %{private}@
reset reader authorization for bundle %@ service %@
Could not retrieve authorization information for TCC service %{public}@
Failed to write frames
Segment versions of %{public}@ don't match. Received %{public}d, expected %{public}d.%s
Unexpectedly trying to iterate beyond the maximum number of directories
Registering for TCC updates
Setting authorization for %{public}@ is not allowed
Unmapping %{public}p
%{public}zu is too large to write
Failed to find a sensor description for service: %{public}@
%{public}@ denied: %{private}@
Unregistering for TCC updates
Registering for darwin notification on %{public}@
Exception when truncating file. %{public}@
Failed to madvise() because %{public, darwin.errno}d
Retrieving fresh authorizations from TCC
Failed to write metadata because %{public}@
Failed to connect with daemon because %{public}@
[%@] Got a writer authorization change notification but the delegate (%{public}p) does not conform to SRSensorWriterAuthorizationDelegate
Daemon authorization update for bundle: %{public}@, prerequisites: %{public}ld, authorized: %{public}@, denied: %{public}@, last modified times: %{private}@
Segment header in %{public}@ says file size is %llu but that is larger than the max size (%{public}lu) we can support.
Attempting to resize a non-writable file
Carrying over previous metadata: %@
Error registering with daemon because %{public}@
Requesting local identifier before identifier has been secured.
Retrieved initial authorization state. prerequisites: %ld
Connection was interrupted, retrying...
[%{public}@] Request for a new segment is already inflight
Failed to find description for %{public}@ in %{public}@
No sensor description found for %{public}@
Syncing %{public}zu bytes from segment %{public}@ to disk
Writer is not authorized so not asking for a new segment
Unable to secure source identifier because %{public}@. Not calling setMetadata because source is not secure.
[%@] monitoring requested to set to %{public, bool}d
[%{public}@] Got writer authorization status update. Current: %{public}ld, TCC: %{public}ld, Data Collection: %{public, bool}d, New: %{public}ld
Unable to get proxy object to request eligibility because %{public}@
Data stream defined without a name: %{public}@
```
