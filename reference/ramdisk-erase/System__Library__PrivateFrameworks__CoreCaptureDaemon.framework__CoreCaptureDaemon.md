# `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 744,064 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 35 (Size: 4112)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (18)

- `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam (compatibility version 1.0.0, current version 631.40.4, weak)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC (compatibility version 1.0.0, current version 3298.52.1, weak)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9, weak)`
- `/System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libIOReport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (1,939)

```
initWithUTF8String:
installedProfileIdentifiers
objectForKeyedSubscript:
sharedConnection
dataWithBytes:length:
dataWithJSONObject:options:error:
length
stringWithFormat:
unsignedLongLongValue
writeData:
containsString:
UTF8String
countByEnumeratingWithState:objects:count:
descriptionWithCalendarFormat:
result=duplicate
CCFile::moveFile Moved '%s' -> '%s' (reason: %s) Owner:%s Pipe:%s\n
forEachTapWithDirectory:Failed to malloc memory for keyArray
CCCacheDelete: purge history processing complete\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCProfileMonitor::profileCallback unchanged mask. previous state: %d, current state: %d\n
CCDatabase::removePipe: owner not found\n
CCDatabase::getPipes: owner not found\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=rollover
CCDaemon::startPipeMonitor CCDaemon not yet initialized, exiting
result=xpc_active
pruneDirectoryOnOSUpgrade: activity enabled; snapshot %s, osversion %s\n
CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n
owner=%s pipe=%s profileLoaded=%d
CCXPCService_FreeResources
result=failed reason=log_dir_path_invalid
CCFile::moveFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCLogTap::profileLoaded, Owner:%s Name:%s\n
CCPipeMonitor::isActive:no tap found
CCDaemon::%s:%d Error writing to destination buffer %s: %s\n
result=retain_plist2
CCProfileMonitor::setStreamEventHandler eventType unhandled:%@
CCServiceMonitor::scanServices fMatching Dictionary Retain count(1) is %ld\n
CCDataFile_sendTelemetry
CCDataFile::sendTelemetry failed
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
Unknown type: %llu %s:%d\n
CCLogPipeInterface_mapPipe
CCPipeMonitor::CCPipeMonitor Failed to create pipe dictionary.\n
pruneDirectoryNDaysRead cap %ld\n
result=success state=%d
message=0x%x
CCPipeInterface_setNotificationPort
CFPropertyListCreateData() failed
Unable to create IOReport Aggregate\n
CCPcapngFormatter::writeFileHeader Uninitialized fDLTArray, i: %d\n
CCPcapngFormatter:: failed to get stream id\n
CCLogFile_closeMMAP
CCDaemon_ResumeAll
CCDataTap::tapLoop(), Error setting notification port rc[0x%08x]\n
CCDataTap::isActive tap is fBusy Active 2 entry:%u\n
CCLogTap::updateLogFlags\n
CCDaemon::%s:%d Error reading from source buffer %s\n
CCDaemon::%s Failed to compress '%s%s'
pruneDirectoryNDaysDo lstat failed on %s:\n%s\n
%s:%d registry entry:%u
CCConfigure::applyConfiguration Configuration type is not dictionary\n
owner=%s pipe=%s reason=%s
CCPipeInterface::setNotificationPort(), mach_port_allocate failed kr[0x%08x]\n
success=%s
owner=%s pipe=%s reason=prepareQuiescing
CCDatabase::getStreams: pipe not found\n
CCDatabase::getStreamPropertyKeys: entry->properties is NULL\n
CCDaemon::init failed to create com.apple.corecaptured.background_queue\n
CCDaemon: CacheDelete disabled via boot-arg\n
result=0x%x ringSize=%llu
result=failed reason=tap_creation_failed
result=failed reason=no_profile_loaded
CCDatabase::getStreams: pipe->streams is NULL\n
CCXPCService::initWithConfigureAndPipeMonitor ERROR INIT MUTEX: %d\n
result=failed reason=device_locked
CCConfigure::pipeConfigureCFDictionaryApplier pipe policy\n
CCConfigure::capture Reason: %s\n
CCDaemon received power notification (0x%x) \n
CCDaemon::init Failed to initialize mutex\n
CCDataTap::processEvent quiesce pending entry:%u Owner:%s Name:%s\n
CCDatabase::getStreamPropertyKeys: pipe not found\n
CCTextFormatter::buildLogIdentTable -- alloc failed\n
CCXPCService::handleIncomingMessage No %s is received\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
CCFile_captureLog
findTapWithOwnerAndPipe:no tap found
%s::%s channelStreamArray empty\n
CCIOReporterFormatter::getChannelsForSubscription  didn't find matching subscription\n
CCXPCService::handleIncomingMessage Unable to allocate config data\n
CCCacheDelete: cannot register for purge notifications ret=0x%x\n
CCProfileMonitor_MergeProfilePlist
CCDatabase::addOwner: CFStringCreateCopy failed\n
CCDatabase::getPipeConfig: pipe not found\n
CCDatabase::getStreamProperty: owner not found\n
result=connection_established
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
result=failed reason=keys_alloc_failed
CCProfileMonitor::profileCallback Entered source:%d token:%d\n
CCXPCService::handleIncomingMessage XPC message is not dictionary\n
CCOSSerializeFormatter::writeLog unsupported root type for JSON Serialization
CCDataTap::isActive idle < duration  3 entry:%u duration:%f\n
CCFile::initWithTap memory allocation failed\n
CCLogTap::freeResources() entry:%u failed to unmap pipe with rc[0x%08x]\n
CCLogPipeInterface_profileLoaded
CCLogTap_withRegistryEntry
result=unexpected_event_type type=%s
configure=%p pipeMonitor=%p
CCOSSerializeWithIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCDataPipeInterface_queryMetaData
CCLogTap::setLogFlags Owner:%s Name:%s entry:%u\n
CCPcapngFormatter::writeFileHeader: Empty pipeOwner or pipeName string\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.
CCXPCService::startXPCService() Failed to start XPC service \n
result=failed reason=log_directory_creation_failed
CCPipeMonitor::CCPipeMonitor Failed to CCIOReportDumpProcessor.\n
%s::%s  didn't find or wrong type in dict at i %ld for %s\n
CCDatabase::removeStreamProperty: property key not found\n
CCConfigure::pipeConfigureCFDictionaryApplier Pipe: %s\n
newInstance result=%s
%s Read pointer moved while copying metadata. Retrying entry:%u\n
owner=%s pipe=%s streamName=%s flagName=%s
CCPipeMonitor::%s:%d Release Tap i %zu
CCPipeMonitor::isActive: recent serviceTerminated, staying active\n
%s:%06u Invalid captureId
CCIOReporterFormatter::addRegistryChildToChannelDictionary  no %s found in %s\n
result=0x%x
CCLogTap::setWatermarkLevel\n
CCIOReporterFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCProfileMonitor::cancelObservers removing event stream handler and Darwin observer\n
CCProfileMonitor::profileCallback failed to get fMutex, exiting\n
CCPipeEntry operator=: malloc failed for %zu bytes\n
CCDatabase::getPipeProperty: pipe not found\n
CCLogFile::cleanupCapturedFiles log type is %d, current file is %s\n
CCConfigure::captureDirectoryCFDictionaryApplier Pipe: %s\n
CCConfigure::policy policy: %u\n
result=failed reason=IORegisterForSystemPower_failed
CCDataTap: Unable to create CCFile. entry:%u Owner:%s Name:%s\n
(CCLogTap) CFNumberGetValue failed\n
%s::%s channelStreamArray not valid\n
%s::%s Can't create channelStreamDictionary\n
CCDatabase::findPipe: pipeName is NULL\n
CCDaemon_shutdown
result=failed reason=property_creation_failed
CCLogPipeInterface_profileRemoved
CCPipeMonitor::CCPipeMonitor Failed to initialize mutex\n
quiesceAllTaps:no tap found
%s::%s Can't create subscriptionLegendDictionary\n
%s:%d %s::withRegistryEntry entry:%u Owner:%s Name:%s
CCDatabase::setStreamProperty: stream not found\n
CCPipeInterface::%s:%d mach_msg SEND_MSG kr:%u entry:%u
CCProfileMonitor::initWithConfigure ERROR INIT MUTEX: %d\n
CCProfileMonitor::profileCallback changed. previous state: %d, current state: %d\n
CCDatabase::findStream: pipe->streams is NULL\n
CCDatabase::setStreamProperty: key is NULL\n
CCPcapngFormatter::searchStreamIdInRegistry: Stream not found in database\n
CCLogFile_openFile
CCLogFile::configureLogOptions Configuration is %s\n
CCConfigure::notifyTimeout notifyTimeout: %u\n
CCDaemon::enablePurgeNotification failed to create CFString for other save location\n
CCFile::captureLog Capture(%s) is in progress. Ignoring new one.\n
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe, getting config from database\n
forEachTapWithDirectory:no tap found
quiesceAllTaps:Failed to malloc memory for keyArray
resumeAllTapsFromQuiesced:no tap found
%s:%06u failed to allocate memory\n
CCConfigure::captureDirectoryCFDictionaryApplier capture\n
result=already_shutdown
CCDaemon received system shutdown notification, all cctap quiesced\n
CCLogTap::tapLoop(), Error setting notification port rc[0x%08x]\n
CCLogTap::%s:%d cast failed\n
%s Ring offset out of range: %u > %llu entry:%u\n
%s - localLogMetadata.payloadLength + logPayloadOffset IS BEYOND RINGSIZE. ADJUST entry:%u
CCPipeInterface::setDispatchQueue re-targeted dispatch source to continuous queue entry:%u Owner:%s Pipe:%s\n
CCConfigure::configureOptions Not found the tap owner:%s, pipe: %s\n
CCDataTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
can reduce logging: %d\n
Incorrect number [numberOfDirArrayEntries: %lld, readIndex %lld] of directory entries. Skip sorting.\n
getOsVersion %s\n
%s::%s didn't find %s or wrong type in array at i %ld\n
CCProfileMonitor::withPipeMonitor Failed to create CCProlieMonitor\n
CCTap_initWithRegistryEntry
CCDaemon::getInstance failed with exception: %s
%s@%d: bail - !legend\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  didnt find or not a dict in array\n
CCLogTap::tapLoop entry:%u Owner:%s Name:%s Exiting taploop\n
CCProfileMonitor_ProfileRemoved
result=success finalProfileLoaded=%d keyCount=%ld
CCTap_freeResources
CCDatabase::getStreamPropertyKeys: no properties in stream\n
%s:%06u Triggering stackshot with id %s due to %s\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCDatabase::getStreamConfig: owner not found\n
CCDatabase::reset: malloc failed for %zu bytes\n
CCPcapngFormatter::writeFileHeader: Non-IORegistry pipe - owner=%s, name=%s\n
CCPcapngFormatter::searchStreamIdInRegistry: Found %ld streams in database\n
CCPcapngFormatter::searchStreamIdInRegistry: Found matching stream in database\n
CCLogFile::withConfig() Invalid parameters\n
Error: %s
CCDataFile::open Failed to create %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj %s is NULL, with type %ld, but has type %ld\n
CCFile::copyFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCPcapngFormatter::writeFileHeader Uninitialized fStreamNameArray, i: %d\n
result=cannot_acquire_lock
event_type=%s
CCDaemon_QuiesceAll
%s@%d: bail - !filePath\n
CCLogFile::initWithConfig: pthread_mutex_init failed\n
CCDaemon::init CoreCaptureStart was already called\n
Found blob name: %s:%d %llu %s\n
CCFile::populateCommonTelemetryDictionary - Failed to get config from database for owner/pipe\n
result=not_dictionary_types
CCDatabase::addStream: CFStringCreateCopy failed\n
Entitlement query did not succeed \n
CCDaemon::init failed to create com.apple.corecaptured.serial_queue\n
%s Duplicate Owner:%s Name:%s entry:%u\n
CCPipeEntry::~CCPipeEntry: malloc failed for %zu bytes\n
CCDatabase::getPipes: owner->pipes is NULL\n
%s@%d: bail - !allChannels\n
owner=%s pipe=%s registryEntry=%u
CCFile::copyFile failed: %s file: '%s' Owner:%s Pipe:%s\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find %s\n
CCProfileMonitor::setStreamEventHandler Unable to get notification center for configuration reader.
CCDatabase::getOwners: malloc failed for %zu bytes\n
CCDatabase::hasStream: owner not found\n
CCDatabase::setStreamProperty: pipe not found\n
CCDaemon::%s initial scan not complete, staying active
result=active
%s - STATE IS RESERVED. BREAK entry:%u
CCLogTap::setPolicy, Owner:%s Name:%s entry:%u\n
CCPipeInterface::resetDispatchQueue re-targeted dispatch source to capture queue entry:%u Owner:%s Pipe:%s\n
CCCacheDelete: framework not available on this platform\n
%s::%s not a matching Stream id\n
CCDatabase::addPipe: ownerName is NULL\n
%s:%06u: Allocation failure\n
IOReportCreateSamplesRaw() returned 0 sized dictionary
CCProfileMonitor::profileCallback read WiFi profile plist valid: %d mask: %d\n
CCDatabase::addStream: pipe not found\n
CCLogFile::buildFileTables fNumberOfArrayEntries is zero\n
CCLogFile::initWithConfig: pthread_mutexattr_settype failed\n
CCDaemon_EnablePowerNotification
CCDataTap::%s invalid dataPipeInterface\n
%s - no fFile entry:%u
CCIOReporterFormatter::writeLog  Inconsistent data (1) length=%lu\n
owner=%s pipe=%s reason=resumeFromQuiesced
CCDatabase::addStream: streamName is NULL\n
CCLogFile::initWithConfig: Failed to initialize PCAP formatter\n
CCLogFile::sendTelemetry failed
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  failed to duplicate dictionary\n
%s:%06u: opendir failure - %s\n
CCDatabase::getStreamPropertyKeys: owner not found\n
No channels found\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream header bytes: %s\n
CCLogFile::withRegistryEntry()\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d
CCDaemon received system wake or will not sleep (0x%x), all cctap resumed from quiesced state\n
CCFile_copyFile
CCFile::captureLogRun() Exiting CCFile::captureLogRun (reason: %s) Owner:%s Pipe:%s\n
CCPipeMonitor_ResumeAllTaps
%s::%s shapeIOReportLibraryFriendlyDictionary failed\n
CCProfileMonitor::freeResources Entered\n
result=success mergedKeys=%ld
CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n
CCConfigure::watermarkLevel watermarkLevel: %u\n
owner=%s pipe=%s entry=%u
result=success configurationsApplied=%ld
CCIOReportDumpQueue_ProcessorThread
CCPcapngFormatter::buildStreamToInterfaceTable: Missing owner or pipe name\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe initialized with %u total interfaces\n
CCConfig is %s\n
result=failed reason=mutex_init_failed error=%d
Session Name: %s, Blob Name: %s %llu.%llu Owner:%s Name:%s\n
forEachTapWithOwnerAndPipe:Failed to malloc memory for keyArray
CCOwnerEntry::~CCOwnerEntry: malloc failed for %zu bytes\n
CCDatabase::getPipeEntry: owner not found\n
CCDataTap::capture, Owner: %s, Name: %s\n
owner=%s pipe=%s policy=%u
profileRemoved:no tap found
%s:%06u Unable to copy arguments
result=failed reason=null_saveDir
CCPcapngFormatter::writeLogFooter logMetaData is NULL\n
CCXPCService::handleIncomingMessage release, incomingConnection\n
%s:%d processEvent for entry:%u Owner:%s Name:%s
CCPipeInterface::setDispatchQueue re-targeted notification port to continuous queue entry:%u Owner:%s Pipe:%s\n
CCPipeMonitor::ccfree - fails to destroy fMutex lock. Error[%d]\n
isActive:Failed to malloc memory for valueArray
%s CANNOT FIND tap with Owner:%s Name:%s\n
result=timeout tapCount=%ld notQuiescedTap=%ld
CCDatabase::setPipeProperty: owner not found\n
CCDatabase::removeStreamProperty: owner not found\n
Invalid Meta Key. Bail.
fMutexCleanDirectories not acquired, bail out\n
CCDatabase::removeOwner: ownerName is NULL\n
CCLogFile::initWithConfig: Successfully initialized for non-IORegistry pipe\n
CCLogFile::deleteFile file already deleted: %s\n
CCConfigure::applyConfiguration CCSTART key \n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  rawData or interests not available\n
CCIOReporterFormatter::writeLog  Didn't find channels\n
CCDatabase::getOwners: no owners in database\n
CCDatabase::hasStream: ownerName is NULL\n
%s@%d: bail - !mkdirRecursive\n
%s@%d: Unable to create samples: %s\n
owner=%s pipe=%s fileName=%s fileSize=%ld logEvents=%u
CoreCaptureStop complete\n
owner=%s pipe=%s fileName=%s fileSize=%ld
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is %s NULL, with type %ld, but has type %ld\n
(CCLogTap) CCPipeInterface::withRegistryEntry failed\n
CCLogTap::setLogLevel Owner:%s Name:%s entry:%u\n
owner=%s pipe=%s timeout=%u
CCPipeInterface::setDispatchQueue entry:%u Owner:%s Pipe:%s\n
CCDaemon::%s:%d failed to open source buffer %s\n
CCDaemon::setupDirectInstance success
CCDataPipeInterface_profileLoaded
CCCacheDelete: purge notification already enabled\n
getHwModel %s\n
CCProfileMonitor::freeResources done\n
CCDatabase::findPipe: owner->pipes is NULL\n
CCDatabase::addPipe: failed to find/create owner\n
CCDatabase::getStreams: no streams in pipe\n
CCDaemon received system sleep notification (0x%x), all cctap quiesced\n
previous and current sequence numbers are same %u prev read offset %u,previous write offset %u, new write offset %u, entry %u\n
%s:%06u: Invalid type\n
Error creating plist...\n
Got an XPC error: %s\n
result=xpc_error error=%s
Entitlement exists, but check failed. \n
CCLogFile::withConfig() Invalid log type %d\n
CCDaemon purge notification enabled\n
gzflush error code = %d\n
CCPipeMonitor::%s:%d Tap corresponding to Pipe not found
CCPipeMonitor::%s:%d Tap corresponding to terminated Pipe not found Owner:%s Name:%s entry:%u
CCPipeInterface_wakeupTapLoop
CCIOReportDumpQueue::_processorThread bail - !keysTypeRef\n
CCLogFile_buildFileTables
CCLogFile::deleteFile failed to delete: %s, errno: %d\n
CCConfigure::pipeOwnerCFDictionaryApplier Owner: %s\n
Found session timestamp: %s:%d %llu %llu.%llu\n
CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe entry:%u Owner:%s Pipe:%s\n
cleanCaptureDirectories:Failed to malloc memory for valueArray
CCDaemon::%s Compression successful, deleting uncompressed file %s
%s::%s no key %s in dictionary\n
CCDatabase::getStreamConfig: stream not found\n
CCConfigure::configure keycount : %ld\n
CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next. entry:%u Owner:%s Name:%s\n
CCFile::initWithTap Failed to create log directory  %s\n
CCDatabase::hasStream: pipeName is NULL\n
CCDatabase::getStreamProperty: entry->properties is NULL\n
CCXPCService_HandleIncomingMessage
result=failed reason=xpc_service_creation_failed
CoreCaptureStart: ENTRY - workingDir=%p, saveDir=%p, isCCDaemon=%d, isInitialized=%d\n
result=failed reason=memory_allocation_failed
result=malloc_failed
CCDatabase::addOwner: ownerName is NULL\n
CCDatabase::removeStream: ownerName is NULL\n
CCDaemon::sendProfileChangeNotification profile change notification received\n
CCDaemon::init Failed to create timer dispatch source\n
result=%s fileD=%d
result=failed reason=property_value_failed
pruneDirectoryNDaysRead strtol EINVAL\n
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get CCFile object\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.\n
CCXPCService_HandleConnectionEvent
CCFile::moveFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
%s::%s didn't find matching subscription\n
CCDatabase::getStreamProperty: stream not found\n
CCXPCService::handleIncomingMessage keycount : %ld\n
CCLogFile::initWithRegistryEntry \n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_init failed\n
CCConfigure::pipeConfigureCFDictionaryApplier Key: %s\n
result=profile_active
result=%s
CCPipeInterface::%s:%d rcvd terminate signal entry:%u
CCOSSerializeFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCDaemon power notification disabled\n
CCDaemon::init Failed to create CCPipeMonitor\n
forEachTapWithOwnerAndPipe:no tap found
CCDaemon::Not all taps got quiesced, tap %ld was not ready
CCPcapngFormatter::buildStreamToInterfaceTable Failed to convert stream name\n
result=failed reason=bad_args
CCDaemon IORegisterForSystemPower failed\n
CCPipeInterface::setNotificationPort(), mach_port_insert_right failed kr[0x%08x]\n
result=success tapCount=%zu
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d)\n
CCDatabase::hasStream: pipe not found\n
CCDatabase::removeStreamProperty: stream not found\n
filePath=%s
CoreCaptureStop non daemon cleanup, calling ccfree\n
CCFile::isLogdirExists Failed to create  %s\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap pipe with rc[0x%08x]\n
Received Capture Event entry:%u Owner:%s Name:%s\n
result=success profile=skipped
CCProfileMonitor::applyConfiguration profile is already removed or not installed
CCDatabase::removeStream: pipeName is NULL\n
CCPipeInterface::dispatch_source_create failed
CCIOReporterFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCProfileMonitor::profileCallback starting states -> source %d fProfileToken %d isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCDatabase::getPipePropertyKeys: malloc failed for %zu bytes\n
resumeAllTapsFromQuiesced:Failed to malloc memory for valueArray
CCConfigure::applyConfiguration CCSTOP key  \n
CCDaemon::getInstance isInitialized false
CCDaemon_ActivityCheck
Failed to mark %s as purgeable %d (%s) (flags 0x%llx)\n
CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n
CCPipeInterface::resetDispatchQueue re-targeted notification port to capture queue entry:%u Owner:%s Pipe:%s\n
%s:%06u Daily stackshot limit reached (%zu stackshots). Skipping stackshot for id %s (reason: %s)\n
IOReportCreateSamplesRaw() returned 0 sized dictionary %s
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj %s is NULL, with type %ld, but has type %ld\n
CCDataTap::initWithRegistryEntry invalid fPipeInterface\n
Notification to dump to disk failed for entry:%u
%s::%s !subscriptionLegendDictionaryArray\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  Couldnt find %s\n
CCProfileMonitor::profileCallback during shutdown at %d\n
CoreCaptureStart called with bad args, crashing
result=failed reason=already_called
CCLogPipeInterface_updateLogFlags
CCLogTap::configureLogOptions\n
CCPipeMonitor::cleanCaptureDirectories - fails to unlock\n
%s::%s didn't find or not a dict in array\n
CCProfileMonitor::profileCallback empty dictionary. fProfileLoaded %d fProfileRemoveApplied %d\n
%s:%06u Configuration type is not dictionary\n
getInstance result=%s
CCDaemon::runShutdownThread Failed to exit cleanly after %d attempts, forcing exit
CCCacheDelete: no directories provided\n
%s::%s didn't find %s\n
%s::%s streams %ld\n
CCDatabase::hasPipe: pipeName is NULL\n
CCDatabase::addStream: owner not found\n
CCDatabase::getStreamPropertyKeys: malloc failed for %zu bytes\n
CCFile::copyFile: Unable to stat source path errno %d, reason %s\n
plist1=%s plist2=%s
CCOwnerEntry copy constructor: malloc failed for %zu bytes\n
%s@%d: fCancelableBlock bailing out\n
CCLogFile::initWithConfig: Invalid arguments\n
CCLogFile::writeLog - File roll needed\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCFile::captureLogRun Failed to stat file %s%s, errno: %d Owner:%s Pipe:%s\n
%s Owner:%s Name:%s entry:%u\n
CCProfileMonitor::setStreamEventHandler \n
Unexpected event type %s\n
CCDataPipeInterface_readData
CCFile_moveFile
%s Read Ptr is not multiple of %lu (%d) entry:%u \n
Invalid State readOffset : %d, writeOffset : %d state %c, entry %u 
CCPipeMonitor::ccfree Entered\n
profileLoaded:Failed to malloc memory for valueArray
CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory errno %d\n
deleteDirectory: deleting '%s' reason: %s
CCFile::moveFile Failed to delete source file after copy: '%s', errno: %d\n
CCLogTap::tapLoopImpl() isLogdirExists failed\n
findTapWithOwnerAndPipe:Failed to malloc memory for valueArray
CCDaemon::%s:%d failed to open dest buffer %s\n
CCDaemon::%s Failed to delete file %s errno: %d
CCFile::writeMetadataFiles failed malloc\n
CCProfileMonitor::setStreamEventHandler calling profileCallback(CCProfileChangeSourceXPCStream)\n
result=failed reason=profile_removed
CCConfigure::captureDirectoryCFDictionaryApplier dirName: %s\n
CCDaemon will calling shutdown()\n
Found blob length: %s:%d %llu %zu\n
fileCount=%ld timeTaken=%f
CCLogTap::%s:%d tapLoopImpl entry:%u Owner:%s Name:%s\n
%s - STATE IS EMPTY. CONTINUE entry:%u
CCCacheDelete: failed to create dispatch queue\n
CCDaemon::%s unable to stat compressed file '%s'
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCFile::initWithTap Failed to create formatter\n
CCLogPipeInterface_setWatermarkLevel
CCPipeMonitor::ccfree Failed to acquire lock\n
findTapWithOwnerAndPipe:Failed to malloc memory for keyArray
result=success tapCount=%ld
CCDaemon::%s:%d dirPath is invalid\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCIOReporterFormatter::writeLog  Insufficient length=%lu to hold IOReporterHeader_t\n
CCProfileMonitor::sendProfileChangeNotification profile change notification received\n
%s:%06u keycount : %ld\n
CCPipeEntry copy constructor: malloc failed for %zu bytes\n
CCDatabase::removePipe: ownerName is NULL\n
CCDatabase::getPipeProperty: entry->properties is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream[%u]: name=%s, id=%u, dlt=%u\n
CCLogFile::initWithConfig: Failed to create directory/file name strings\n
CCCacheDelete: purge notification enabled\n
CCProfileMonitor::profileCallback read BT profile plist valid: %d mask: %d\n
CCPcapngFormatter::writeLog  Inconsistent data (1) length=%lu\n
CCLogFile::initWithConfig: Failed to create log directory path\n
CCLogFile::configureLogOptions Current Log Type:%d, File Size=%u, Max Number Of Files:%u\n
Invalid argument @'%s':%06u
CCDaemon::%s:%d unable to allocate destination buffer\n
%s::%s key %s has wrong type in dictionary\n
CCProfileMonitor::setStreamEventHandler event received:%s\n
CCOwnerEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::setPipeProperty: pipe not found\n
CCDatabase::getStreamPropertyKeys: stream not found\n
%s@%d: bail - !saveDir\n
CCLogPipeInterface_dumpToDiskComplete
CCIOReporterFormatter::addRegistryChildToChannelDictionary  Cant create channelStreamDictionary\n
CCXPCService_InitWithConfigureAndPipeMonitor
CCLogFile::withConfig()\n
result=init_scan_pending
CCDataFile::sendTelemetry analytics_send_event_lazy weak link import failed
owner=%s pipe=%s fileName=%s captureId=%u.%06u reason=%s logSize=%zu
CCProfileMonitor::setStreamEventHandler Registered for notification callback.\n
CCServiceMonitor::scanServices fMatching Dictionary Retain count(2) is %ld\n
CCDatabase::getStreams: owner not found\n
CoreCaptureStop non daemon stopping, calling quiesceAllTaps()\n
CCDaemon::init failed to create come.apple.corecaptured.service_notify\n
Found SessionName: %s:%d %llu %s\n
CCPipeInterface::withRegistryEntry Unsupported pipe type(%d) \n
%s Unexpected CF object type ID. Expected (%lu), have (%lu) \n
owner=%s pipe=%s dirName=%s
CCPipeEntry operator=: malloc failed for cleanup, %zu bytes\n
CCLogFile_sendTelemetry
CCFile_captureLogRun
CCPipeMonitor_ProfileRemoved
CCFile::mkdirRecursive Unable to mkdir on '%s', errno %d\n
CCDaemon::%s:%d fileName is invalid\n
CCDatabase::removeOwner: owner not found\n
CCDatabase::getPipeProperty: owner not found\n
CCDatabase::removePipeProperty: pipe not found\n
CCDatabase::removeStream: pipe not found\n
result=failed reason=working_directory_creation_failed
CCLogPipeInterface_setNotifyTimeout
CCDaemon::%s:%d unable to create class with protection flag\n
CCPcapngFormatter::writeLog Failed to write(1) Length=%lu, tempLength=%lu\n
CCPcapngFormatter::buildStreamToInterfaceTable: Found %ld streams in database\n
CCDataTap::processEvent already quiesced entry:%u Owner:%s Name:%s\n
gzflush failed errno = %d, errnum = %d, reason : %s, %s\n
CCLogTap::isActive policy is %d, Owner:%s Name:%s entry:%u\n
CCCacheDelete: purge history lost, rescan needed\n
CCDaemon::%s:%d fileName %s is already compressed...\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe, querying database\n
CCLogFile::deleteFile successfully deleted: %s\n
result=shutdown_triggered
CCFile::captureLogRun copying files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
Received Skip Event %u\n
CCPipeInterface::%s::%d fNotificationPortIsSet:%d rc:%d entry:%u
CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n
result=retain_plist1
CCProfileMonitor_ApplyConfiguration
Stream Name is %s\n
result=already_running
CCLogPipeInterface_setConsoleLogFlags
CCPipeMonitor::ccfree - fails to destroy lock. Error[%d]\n
CCLogFile::initWithRegistryEntry: pthread_mutex_init failed\n
CCLogFile::initWithConfig: Unsupported log data type %d\n
result=failed reason=file_creation_failed
CCDaemon::ccstart to create CCDaemon\n
CCFile_writeDataFiles
forEachTapWithOwnerAndPipe:Failed to malloc memory for valueArray
CCProfileMonitor::profileCallback no profile installed. previous state: %d, current state: %d\n
CCDatabase::getPipePropertyKeys: owner not found\n
CCIOReportDumpQueue_SaveChannels
CCIOReportDumpQueue_DoSaveChannels
CCXPCService_StartXPCService
CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions (attempt %d/%d)
CCDataFile_openCaptureFile
result=xpc_error
CCDaemon::enablePurgeNotification failed to get save location\n
CCFile::copyFile gzwrite error: %s\n
CCPcapngFormatter::searchStreamIdInRegistry: Non-IORegistry pipe, querying CCDatabase for streamId=%u\n
CCXPCService: logging command received but not supported on this platform\n
owner=%s pipe=%s nextFileIndex=%u logType=%d fileSize=%u
CCDatabase::addStream: pipeName is NULL\n
CCLogFile::configureLogOptions Configured Log Type:%d, File Size=%u, Max Number Of Files:%u\n
CoreCaptureStart called when CCDaemon already running, returning existing instance
CCDaemon::enablePurgeNotification failed to create CFString for save location\n
result=failed reason=formatter_creation_failed
%s NULL value.\n
%s:%06u unable to allocate dictionary\n
CCProfileMonitor::profileCallback Loaded\n
CCDatabase::findOwner: database is NULL\n
CCDatabase::hasPipe: ownerName is NULL\n
CoreCaptureStop setShutdownAlreadyTrue, exiting without doing anything
result=failed reason=invalid_args
CCDataPipeInterface_profileRemoved
CCLogPipeInterface_setPolicy
CCPipeMonitor::ccfree Exit\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in array at i %ld\n
%s:%d CCPipe::withOwnerNameCapacity Registry entry:%u Unsupported pipe type(%d)\n
CCDatabase::findOwner: ownerName is NULL\n
%s:%d CCDataTap::tapLoopImpl for entry:%u
CCLogTap::capture, Owner:%s Name:%s\n
result=failed reason=mutex_lock_failed
CCDatabase::addPipe: pipeName is NULL\n
CCDatabase::getPipePropertyKeys: pipe not found\n
CCDatabase::removeStream: owner not found\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=fileWillClose
result=failed
result=0x%x bytesRead=%llu
forEachTapWithDirectory:Failed to malloc memory for valueArray
CCXPCService::handleIncomingMessage Key is %s\n
CCLogFile::withRegistryEntry() Invalid log type %d\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_settype failed\n
CCLogFile::initWithConfig: CFNumberCreate failed for pipeType\n
CoreCaptureStop called when isShutdownPending true, ignoring
owner=%s pipe=%s fileName=%s
CCOSSerializeWithIOReporterFormatter::writeLog CFDataGetBytePtr() failed
CCLogTap::setConsoleLogLevel Owner:%s Name:%s entry:%u\n
ERROR INIT MUTEX: %d\n
profileLoaded:no tap found
CCIOReporterFormatter::writeLog  Can't copy rawData\n
CCProfileMonitor::profileCallback exiting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe missing owner or name\n
CCServiceMonitor::ccfree()\n
Unable to initialize logging subsystem for corecapture
previousProfileLoaded=%d
%s:%06u unable to create set\n
CCDatabase::getPipePropertyKeys: entry->properties is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate dlt memory\n
CCLogFile::addFile Failed to create %s\n
result=already_set
CCDaemon:: No name matching CCPipe service found \n
result=%s logDataType=%d
Couldn't update read ptr.\n
owner=%s pipe=%s keyCount=%ld
result=failed reason=malloc_failed
CCFile::generateCaptureDirPath failed malloc\n
CCConfigure::configure key is %s\n
CCFile::withTap Unsupported file type(%d) \n
CCDatabase::hasPipe: owner not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream name memory\n
Failed to get fCaptureDirPath for purgeable marking\n
owner=%s pipe=%s fileName=%s doCompress=%d
CCConfigure::pipeConfigureCFDictionaryApplier watermark level to notify\n
CCFile::initWithTap fLogDirPath is invalid\n
%s::%s channelStreamArray at i %ld not valid\n
%s:%d: mmap failed\n
CCLogFile::addFile: No log before device first unlocked for PROTECTION_CLASS_C\n
CCDataTap_initWithRegistryEntry
Unexpected log parameters ring state3(0x%llx), ring buffer(0x%llx), ring size(%llu), logSize(%lu), logContinueSize(%lu) entry:%u\n
result=success profile=%s
CCDatabase::addPipe: CFStringCreateCopy failed\n
CCDatabase::getPipes: malloc failed for %zu bytes\n
CoreCapture_Start
CCDataTap::tapLoopImpl exit entry:%u Owner:%s Name:%s Exiting taploop\n
owner=%s pipe=%s streamName=%s
CCPipeMonitor::CCPipeMonitor Failed to initialize fMutex\n
result=tap_not_found
CCDataTap_withRegistryEntry
%s:%06u: Failed reading '%s' from registry\n
CCConfigure::pipeConfigureCFDictionaryApplier Configure Log Options\n
result=shutdown_pending
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCFile::initWithTap create with cstring failed\n
CCProfileMonitor::applyProfile owner:%s, pipe:%s\n
CCDatabase::removePipe: pipeName is NULL\n
CCLogFile_closeFile
CCConfigure::findTapWithOwnerAndPipe found CCTap, Owner: %s, Pipe: %s\n
CCDaemon::runShutdownThread Exiting via xpc_transaction_try_exit_clean
CCDaemon::%s monitor NOT active, shutdown
%s Tap Found tap with Owner:%s Name:%s\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  key %s has wrong type in dictionary\n
CCProfileMonitor::applyConfiguration  shutdown pending, dropping request and exiting\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  failed to store Channel Description\n
CCLogPipeInterface_setLogLevel
CCLogTap::setNotifyTimeout\n
CCPcapngFormatter::buildStreamToInterfaceTable: Found stream header (%ld bytes) for stream\n
CCLogFile::initWithConfig: buildFileTables failed\n
CCConfigure::captureDirectoryCFDictionaryApplier Key: %s\n
owner=%s pipe=%s fileName=%s reason=%s
CCPipeMonitor_ServiceTerminated
%s@%d: bail - !hash\n
result=failed reason=null_allChannels
CCLogFile::initWithRegistryEntry buildFileTables\n
CoreCaptureStop failed with exception: %s
isActive:Failed to malloc memory for keyArray
CCPipeMonitor::%s:%d Release Tap for entry:%u
CCPipeMonitor_ProfileLoaded
profileRemoved:Failed to malloc memory for valueArray
%s::%s Failed to create IOReporter library friendly channel list\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
%s:%06u invalid configuration\n
CCConfigure::captureDictionaryCFDictionaryApplier dirName: %s\n
%s:%d processEvent entry:%u Owner:%s Name:%s
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
%s:%d CCTap::withRegistryEntry Registry entry:%u not found\n
CCDatabase::removePipeProperty: property key not found\n
CCDatabase::removeStream: stream not found\n
CCDatabase::getStreamEntry: owner not found\n
CCPcapngFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCLogTap::setConsoleLogFlags Owner:%s Name:%s entry:%u\n
%s:%d Owner:%s Name:%s entry:%u
%s::%s didn't find or wrong type in array at i %ld\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  dictionary doesn't contain %s\n
CCPcapngFormatter::writeLogHeader Failed to write. %ld\n
CCPcapngFormatter::writeLogHeader fStreamHeaderArray failed to write length %ld. %s\n
CCPcapngFormatter::buildStreamToInterfaceTable numberofStreams : %d\n
CCXPCService::handleConnectionEvent CCDaemon::getInstance().isShutdownPending() true, dropping xpc event and exiting\n
CCPipeMonitor::ccfree Exit - Destroyed lock\n
result=mutex_failed
%s Tap Find Tap with Owner:%s Name:%s\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  no key %s in dictionary\n
CCTap_cleanCaptureDirectories
CCDatabase::removePipeProperty: owner not found\n
CCDatabase::getStreams: malloc failed for %zu bytes\n
ERROR: cannot build the XML data\n
CCDataTap::profileLoaded, Owner: %s, Name: %s\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in dict at i %ld for %s\n
result=failed reason=no_keys
result=failed reason=mkdir_failed
CCXPCService::handleIncomingMessage Unable to allocate scratch buffer\n
CCLogFile::initWithConfig\n
CCLogFile_addFile
CCLogTap::%s invalid logPipeInterface\n
CCLogPipeInterface_setConsoleLogLevel
CCPipeMonitor_QuiesceAllTaps
%s::%s failed to store Channel Description\n
CCOwnerEntry operator=: malloc failed for %zu bytes\n
CCDatabase::removePipe: pipe not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate Interface ID memory\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream header memory\n
CCFile::copyFile Wrote '%s' source length: %lld archive length: %lld (reason: %s) Owner:%s Pipe:%s\n
getting CC session id failed for entry:%u
Created a bad offset, don't save it! newOffset %u, payload length %u, padding %u,sizeof metadata %lu, STATE %c, entry:%u
CCPipeInterface::IOServiceClose entry:%u fConnectRef(%d)\n
profileRemoved:Failed to malloc memory for keyArray
%s::%s empty array\n
CCPcapngFormatter::writeLog Unexpected log data \n
CCXPCService::handleIncomingMessage empty configuration\n
%s:%06u: CFStringGetCString failure\n
workingDir=%s saveDir=%s isDaemon=%s
result=not_initialized
CCFile::captureLog\n
CCPipeInterface::initWithRegistryEntry [pipeOwner: %s, pipeName: %s] Failed to initialize returned %x\n
result=no_taps
CFDataGetBytePtr() failed
CCServiceMonitor::servicesPublished ignoring processing servicePublished due to isShutdownPending
result=not_enabled
CCFile::captureLog Failed to create directory %s (reason: %s)\n
CCPipeInterface::%s:%d rcvd terminate msg:0x%x entry:%u
result=success tap=released
CCDaemon::%s:%d unable to create filePathRef\n
CCDatabase::findPipe: owner is NULL\n
CCDatabase::findStream: pipe is NULL\n
CCPcapngFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCDataTap::profileRemoved, Owner: %s, Name: %s\n
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get stream entry for stream %ld\n
Entitlement exists, and check is successful\n
CCLogFile::initWithRegistryEntry: Invalid arguments\n
CCLogFile::initWithConfig: Failed to create log directory\n
CCDaemon::%s CCDaemon::getInstance().isShutdownPending() == true, skipping activityCheck()
CCDaemon_initWithOptions
CCDataFile_closeFile
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  contains %s %d contains %s %d\n
owner=%s pipe=%s
cleanCaptureDirectories:Failed to malloc memory for keyArray
CCIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCProfileMonitor_ProfileCallback
CCConfigure::pipeConfigureCFDictionaryApplier Owner: %s\n
result=success
CCDaemon::%s:%d filePath may get truncated. Returning...
%s:%06u Invalid reason
CCIOReporterFormatter::writeLog Unexpected log data \n
CCProfileMonitor::applyConfiguration profile is already removed
CCDatabase::hasOwner: ownerName is NULL\n
CCDatabase::setStreamProperty: owner not found\n
CCFile::withRegistryEntry() entered entry:%u\n
CCLogTap_initWithRegistryEntry
CCLogPipeInterface_setLogFlags
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCProfileMonitor::profileRemoved Entered %d\n
CCDatabase::setPipeProperty: key is NULL\n
CCDatabase::getStreamEntry: pipe not found\n
result=success numberOfFiles=%u maxFiles=%u
CCConfigure::pipeConfigureCFDictionaryApplier Unsupported Key %s\n
CCDaemon::init Failed to create CCProfileMonitor\n
CCLogPipeInterface_updateConsoleLogFlags
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCDatabase::~CCDatabase: malloc failed for %zu bytes\n
%s@%d: Problem merging channels\n
result=complete
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate log identifier memory\n
CCDaemon:: Num of matching CCPipe %ld\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  not array\n
CCProfileMonitor_ApplyProfile
ERROR INIT COND: %d\n
filesSaved=%ld
connection=%p type=%s
%s:%06u: Failed getting number\n
CCDataPipeInterface_capture
CCLogTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
seed build (or boot-arg) and device hasn't been unlocked since boot. Won't process event and continue when next event is posted entry:%u\n
CCPcapngFormatter::writeFileHeader: Missing pipeOwner or pipeName\n
result=failed reason=not_entitled
CCXPCService::handleIncomingMessage Unable to get remote connection\n
CCXPCService::cancelActiveConnections cancelling %lu connections\n
CCLogFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCFile::initWithTap Failed to get log directory \n
CCPipeInterface::setNotificationPort(), mach_port_get_attributes failed kr[0x%08x]\n
resumeAllTapsFromQuiesced:Failed to malloc memory for keyArray
result=both_null
result=failed reason=dict_alloc_failed
result=failed reason=values_alloc_failed
%s@%d: fExitNextIteration bailing out\n
CCLogFile::initWithConfig: Failed to create formatter\n
CCLogTap::withRegistryEntry failed\n
quiesceAllTaps:Failed to malloc memory for valueArray
CCCacheDelete: cannot create monitored directories\n
%s::%s rawStreamAndSubscriptionArray not valid\n
CCDatabase::findStream: streamName is NULL\n
CCDatabase::removeStreamProperty: pipe not found\n
CCConfigure::pipePipeCFDictionaryApplier Pipe: %s\n
CCPipeMonitor::ccfree - fails to unlock. Error[%d]\n
%s:%06u: Invalid argument\n
pruneDirectoryOnOSUpgrade: activity disabled\n
CCProfileMonitor::profileCallback getting owners from profile failed
CCConfigure::pipeConfigureCFDictionaryApplier capture\n
CCDaemon power notification enabled\n
CCFile::captureLogRun Current File %s (reason: %s) Owner:%s Pipe:%s\n
CCLogPipeInterface_capture
CCDaemon::%s:%d dirPath is invalid
CCDatabase::removeStream: streamName is NULL\n
CCDaemon::setupDirectInstance failed with exception: %s
Found blob timestamp: %s:%d %llu %llu.%llu\n
CCFile_initWithRegistryEntry
CCFile::moveFile failed: %s file: '%s' Owner:%s Pipe:%s\n
%s:%d Owner:%s skipping profileLoaded
result=failed reason=filePath_failed
CCPcapngFormatter::writeLog Failed to write(2) Length=%lu, tempLength=%lu\n
CCLogFile::initWithConfig: Failed to create working directory string\n
CCDaemon::shutdown is fired\n
CCOSSerializeWithIOReporterFormatter::writeLog unsupported root type for JSON Serialization
CCLogTap::isActive idle < duration, Owner:%s Name:%s entry:%u duration:%f\n
%s:%06u Stackshot rate limit: a stackshot was triggered within the last %d seconds. Skipping stackshot for id %s (reason: %s)\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
Entitlement is NULL \n
CCOSSerializeFormatter::writeLog CFDataGetBytePtr() failed
CCDataFile_openFile
CCFormatter::withLogType Unsupported log data type(%d) \n
CCLogPipeInterface_unmapPipe
CCLogTap::profileRemoved, Owner:%s Name:%s entry:%u\n
IOConnectCallAsyncStructMethod FAILED CCPipeInterface::%s::%d fNotificationPortIsSet:%d entry:%u kr[0x%08x]
CoreCapture_Stop
CCFile::captureLogRun moving files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
CCCacheDelete: purge notification disabled\n
CCLogFile::initWithConfig: CFNumberCreate failed for logDataType\n
CCFile::writeDataFiles memory allocation failed (reason: %s)\n
CCPipeMonitor_CleanCaptureDirectories
CCProfileMonitor::profileRemoved Exited :%d\n
CCDataTap::%s:%d cast failed\n
(CCLogTap) IORegistryEntryCreateCFProperty failed\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n
CCDaemon::%s:%d fileName is invalid
%s::%s failed to store description\n
ERROR: FileURL not created\n
Entitlement couldnt be found \n
CoreCaptureStop called when no CCDaemon running, CCDaemon::isInitialized() returned false, ignoring
CCOSSerializeWithIOReporterFormatter::processAllDictionarieswithinIncommingArray  didnt find or wrong type in array at i %ld\n
CCLogTap::updateConsoleLogFlags Owner:%s Name:%s entry:%u\n
%s::%s clearing out any previous subscriptions\n
CCDatabase::addStream: ownerName is NULL\n
CCDatabase::getStreamConfig: pipe not found\n
Received a connection event\n
Token is [0]: 0x%x... [7]:%x \n
CCConfigure::captureDirectoryCFDictionaryApplier Owner: %s\n
CCDaemon::init invalid arguments passed for non-daemon case\n
profileLoaded:Failed to malloc memory for keyArray
CCFile::mkpath fails to create path '%s' as '%s' is not a directory\n
CCTap::%s:%d entry:%u
CCDatabase::getPipePropertyKeys: no properties in pipe\n
%s@%d: Unable to create subscribtion: %s\n
CCLogFile::initWithConfig: pthread_mutexattr_init failed\n
CCConfigure::pipeConfigureCFDictionaryApplier notify timeout\n
result=exception exception=%s
CCDaemon_DisablePowerNotification
CCFile::captureLog Received Capture notice id: %d.%06d, reason = %s\n
(CCLogTap) CFNumberGetValue failed for LogPolicy\n
CCCacheDelete: file purged: %s (inode: %llu)\n
CCDaemon::%s:%d Trying to compress file %s%s\n
CCXPCService::handleIncomingMessage: incoming, incomingConnection from '%s' with pid '%d', XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n
CCFile::copyFile Unable to stat dest path '%s' errno: %d reason: %s prevErr: %s\n
pruneDirectoryOnOSUpgrade: activity enabled; failed to get osversion\n
source=%d previousState=%d fProfileToken=%d
CCDatabase::getPipes: no pipes in owner\n
CCDatabase::hasStream: streamName is NULL\n
CCDatabase::getStreamProperty: pipe not found\n
fileCount=%ld
CCPcapngFormatter::writeFileHeader: Failed to cast fWriteObject to CCFile\n
result=%s sourceSize=%lld destSize=%lld
previous and current sequence numbers are same %u prev read offset %u,new read offset %u, previous write offset %u, new write offset %u, entry %u\n
CCLogTap::isActive tap is busy, Owner:%s Name:%s entry:%u\n
CCDaemon::%s:%d unable to allocate source buffer\n
CCDaemon::%s Compressed '%s%s' -> %lld bytes
CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback to check for installed profiles\n
%s:%06u memory alloc failed\n
CCDatabase::getPipeConfig: owner not found\n
CCConfigure::capture capture reason can not be NULL\n
result=failed reason=directory_creation_failed
CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u, Owner:%s
%s@%d: Will write to: %s\n
CCPcapngFormatter::writeLogHeader logMetaData is NULL\n
CCXPCService::handleIncomingMessage shutdown pending true, dropping message and exiting\n
CCLogFile::initWithRegistryEntry Number of files can not be 0.\n
CCLogFile::initWithConfig: Number of files cannot be 0\n
CCDaemon_PowerEvent
CCFile::copyFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCFile::captureLogRun Skipping current file Dir file %s, Current File %s Owner:%s Pipe:%s\n
(CCLogTap) IORegistryEntryCreateCFProperty failed for LogPolicy\n
owner=%s pipe=%s level=%u
CCPipeInterface::initWithRegistryEntry entry:%u fConnectRef(%u)\n
CCPipeMonitor_ServicePublished
CCDatabase::getPipePropertyKeys: entry->properties is NULL\n
CCDatabase::hasStream: owner not found\n
DriverID
CCDatabase::removeStreamProperty: pipe not found\n
txt
CCPcapngFormatter::searchStreamIdInRegistry: Found matching stream in database\n
Entitlement exists, but check failed. \n
corecapture
CCDatabase::setStreamProperty: owner not found\n
CCDatabase::removeStreamProperty: stream not found\n
%s:%06u: Allocation failure\n
CCLogFile::initWithConfig: CFNumberCreate failed for pipeType\n
CCDaemon: CacheDelete disabled via boot-arg\n
%s::%s streams %ld\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in dict at i %ld for %s\n
CCPipeInterface::withRegistryEntry Unsupported pipe type(%d) \n
quiesceAllTaps:Failed to malloc memory for keyArray
compressFile
CCDatabase::getStreams: no streams in pipe\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe, querying database\n
CCLogEnable
CoreCapture
CCCacheDelete: file purged: %s (inode: %llu)\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCProfileMonitor::applyProfile owner:%s, pipe:%s\n
CCDatabase::getPipePropertyKeys: malloc failed for %zu bytes\n
LogTimeSpan
CCDataTap::processEvent quiesce pending entry:%u Owner:%s Name:%s\n
/usr/lib/libMobileGestalt.dylib
v16@?0^{__CFArray=}8
CCXPCService: logging command received but not supported on this platform\n
Received a connection event\n
CCConfigure::captureDirectoryCFDictionaryApplier Owner: %s\n
.gz
CCDaemon::%s unable to stat compressed file '%s'
%s@%d: bail - !legend\n
CCConfig
CCConfigure::captureDirectoryCFDictionaryApplier dirName: %s\n
pruneDirectoryOnOSUpgrade: activity enabled; failed to get osversion\n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  failed to duplicate dictionary\n
Rollover
applied
prune_dir_os_upgrade_snapshot
CCIOReporterFormatter::writeLog  Insufficient length=%lu to hold IOReporterHeader_t\n
failed
prune_dir_os_upgrade_ctl
com.apple.ManagedConfiguration.profileListChanged
CCDatabase::getPipePropertyKeys: no properties in pipe\n
/tmp/cc.locktest
Unknown type
CCConfigure::notifyTimeout
CCLogTap::setLogLevel Owner:%s Name:%s entry:%u\n
deleteDirectory
CCDatabase::removePipe: ownerName is NULL\n
CCLogFile::initWithRegistryEntry: Invalid arguments\n
CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe entry:%u Owner:%s Pipe:%s\n
IOServicePublish
ERROR INIT MUTEX: %d\n
ERROR: cannot build the XML data\n
%s::%s Failed to create IOReporter library friendly channel list\n
%s::%s no key %s in dictionary\n
CCDaemon IORegisterForSystemPower failed\n
%s:%06u Daily stackshot limit reached (%zu stackshots). Skipping stackshot for id %s (reason: %s)\n
CCProfileMonitor::profileRemoved Entered %d\n
CCDatabase::removeOwner: ownerName is NULL\n
dest_stat_failed
CCFormatter::withLogType Unsupported log data type(%d) \n
profileLoaded
no_config_string
CCDaemon::shutdown is fired\n
CCDaemon::enablePurgeNotification failed to create CFString for save location\n
cc.file.forcecopy
CCProfileMonitor::setStreamEventHandler calling profileCallback(CCProfileChangeSourceXPCStream)\n
profile_loaded_notification
CCLogTap::isActive tap is busy, Owner:%s Name:%s entry:%u\n
wifi.megawifi
CCLogFile::buildFileTables fNumberOfArrayEntries is zero\n
Metadata
\nIncident Identifier:     %@\nCrashReporter Key:       %@\nHardware Model:          %@\nProcess:                 WiFi Firmware\nPath:                    NA\nIdentifier:              WiFi Firmware Trap\nVersion:                 NA\nCode Typ
CCIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
Error creating plist...\n
DriverName
profileLoaded:no tap found
CCLogFile::initWithConfig: Failed to create log directory\n
CCLogTap::isActive idle < duration, Owner:%s Name:%s entry:%u duration:%f\n
CCCacheDelete: purge history lost, rescan needed\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCConfigure::pipeConfigureCFDictionaryApplier notify timeout\n
IOReportCreateSamplesRaw() returned 0 sized dictionary
unchanged
v8@?0
%s
CCProfileMonitor::setStreamEventHandler Registered for notification callback.\n
MiscInfo
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCDataTap::capture, Owner: %s, Name: %s\n
CCFile::captureLog Capture(%s) is in progress. Ignoring new one.\n
CCFile::captureLogRun Current File %s (reason: %s) Owner:%s Pipe:%s\n
previous and current sequence numbers are same %u prev read offset %u,new read offset %u, previous write offset %u, new write offset %u, entry %u\n
forEachTapWithDirectory:Failed to malloc memory for valueArray
CCConfigure::streamPipeCFDictionaryApplier
CoreCaptureStart called when CCDaemon already running, returning existing instance
CCDataTap::tapLoopImpl exit entry:%u Owner:%s Name:%s Exiting taploop\n
shapeIOReportLibraryFriendlyDictionary
%s:%06u unable to allocate dictionary\n
XPC_TYPE_DOUBLE
CCDaemon purge notification enabled\n
gzopen_failed
Carrier
CCDatabase::getStreamPropertyKeys: malloc failed for %zu bytes\n
CCFile::captureLog Received Capture notice id: %d.%06d, reason = %s\n
CCLogTap::setPolicy, Owner:%s Name:%s entry:%u\n
%s - STATE IS EMPTY. CONTINUE entry:%u
CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u, Owner:%s
CCLogTap::capture, Owner:%s Name:%s\n
cleanCaptureDirectory: count %lld exceeds max %lld, deleting %lld oldest
%s::%s channelStreamArray empty\n
CCXPCService
dest_write_failed
v16@?0@\"NSFileHandle\"8
DYLD_IMAGE_SUFFIX
Entitlement query did not succeed \n
CCLogFile::initWithConfig\n
CCLogFile::initWithConfig: pthread_mutexattr_settype failed\n
?
gzflush error code = %d\n
CCDaemon::%s:%d failed to open dest buffer %s\n
getHwModel %s\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
%s:%d registry entry:%u
CCLogFile::withRegistryEntry() Invalid log type %d\n
Couldn't update read ptr. Cannot guarantee integrity of message %d\n
CCProfileMonitor::profileCallback exiting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCPcapngFormatter::writeFileHeader Uninitialized fDLTArray, i: %d\n
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get CCFile object\n
CCDaemon::enablePurgeNotification failed to create CFString for other save location\n
CCDaemon::%s:%d filePath may get truncated. Returning...
CCDatabase::getStreamPropertyKeys: stream not found\n
CCXPCService::handleIncomingMessage Unable to allocate config data\n
fMutexCleanDirectories not acquired, bail out\n
CCPipeMonitor::%s:%d Tap corresponding to terminated Pipe not found Owner:%s Name:%s entry:%u
CCDatabase::addStream: ownerName is NULL\n
CCLogFile::deleteFile file already deleted: %s\n
CCFile::copyFile: Unable to stat source path errno %d, reason %s\n
CCPipeInterface::%s:%d rcvd terminate signal entry:%u
resumeAllTapsFromQuiesced:no tap found
prune_dir_days
Invalid argument @'%s':%06u
CCFile::captureLogRun() Exiting CCFile::captureLogRun (reason: %s) Owner:%s Pipe:%s\n
wakeupTapLoopInternal
CCPipeMonitor
CCDaemon::%s:%d fileName %s is already compressed...\n
present
CCDaemon::init Failed to create timer dispatch source\n
CCFile::captureLogRun copying files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
vector
processEvent
%s::%s  didn't find or wrong type in dict at i %ld for %s\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find %s\n
CCIOReporterFormatter::writeLog  Didn't find channels\n
%s.%06llu %s %s<%c>[%u] 
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate log identifier memory\n
CCConfigure::pipeConfigureCFDictionaryApplier watermark level to notify\n
CCConfigure::configure keycount : %ld\n
%s:%d CCDataTap::tapLoopImpl for entry:%u
CCDataTap::profileRemoved, Owner: %s, Name: %s\n
CCIOReporterFormatter::writeLog Unexpected log data \n
CCProfileMonitor::profileCallback no profile installed. previous state: %d, current state: %d\n
%s@%d: bail - !hash\n
%s Tap Found tap with Owner:%s Name:%s\n
CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory errno %d\n
wb
CCDatabase::removeStreamProperty: property key not found\n
CCDatabase::addStream: pipeName is NULL\n
ProfileRemoved
%s 
dest_buffer_alloc_failed
 NOT
CCIOReporterFormatter::addRegistryChildToChannelDictionary  no %s found in %s\n
CCProfileMonitor::profileCallback unchanged mask. previous state: %d, current state: %d\n
CoreCaptureStop complete\n
Dropped Log message expected sequence number = %u, Received %u\n
CCProfileMonitor::cancelObservers removing event stream handler and Darwin observer\n
CCDatabase::addStream: pipe not found\n
Name
CCFile::copyFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
findTapWithOwnerAndPipe:Failed to malloc memory for valueArray
pruneDirectoryNDaysRead strtol EINVAL\n
getOwnersFromProfile
CCDatabase::getStreamProperty: entry->properties is NULL\n
com.apple.corecaptured
default
CCFile::generateCaptureDirPath failed malloc\n
(CCLogTap) CFNumberGetValue failed for LogPolicy\n
com.apple.MobileSoftwareUpdate
CCXPCService::handleIncomingMessage No %s is received\n
%s Tap Find Tap with Owner:%s Name:%s\n
fileID
%s%s
IOReportChannelInfo
%s Owner:%s Name:%s entry:%u\n
CCDaemon::%s Compression successful, deleting uncompressed file %s
CCProfileMonitor::freeResources done\n
CCDatabase::hasPipe: owner not found\n
CCFile::copyFile Unable to stat dest path '%s' errno: %d reason: %s prevErr: %s\n
Pcapng
CCFile::mkdirRecursive Unable to mkdir on '%s', errno %d\n
CCDatabase::getPipeConfig: pipe not found\n
Filename
CCPcapngFormatter::buildStreamToInterfaceTable numberofStreams : %d\n
CCConfigure::setConsoleFlags
marconi-wifi
system.plist
no_profiles_installed
No channels found\n
CCDataTap::isActive tap is fBusy Active 2 entry:%u\n
%s::%s empty array\n
CCDatabase::addPipe: ownerName is NULL\n
CCDatabase::hasPipe: ownerName is NULL\n
CCConfigure::pipeOwnerCFDictionaryApplier Owner: %s\n
LogPolicy
%Y-%m-%d %H:%M:%S.%F %z
%s:%06u: opendir failure - %s\n
CCCaptureDirectory
CoreCaptureStart: ENTRY - workingDir=%p, saveDir=%p, isCCDaemon=%d, isInitialized=%d\n
CCDaemon::enablePurgeNotification failed to get save location\n
CCCacheDelete: purge notification enabled\n
CCProfileMonitor::profileCallback failed to get fMutex, exiting\n
CCPipeEntry copy constructor: malloc failed for %zu bytes\n
quiesceAllTaps:no tap found
CCProfileMonitor::applyConfiguration  shutdown pending, dropping request and exiting\n
%s:%d CCPipe::withOwnerNameCapacity Registry entry:%u Unsupported pipe type(%d)\n
_processorThread
XPC_TYPE_UINT64
CCLogFile::initWithConfig: Failed to create log directory path\n
CCPcapngFormatter::buildStreamToInterfaceTable: Missing owner or pipe name\n
CCDataTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
%s.%06llu %s %06llu.%06llu %s<%c>[%u] 
CCIOReportDumpQueue::_processorThread bail - !keysTypeRef\n
CCPcapngFormatter::writeLogHeader Failed to write. %ld\n
%s Unexpected CF object type ID. Expected (%lu), have (%lu) \n
ReleaseType
invalid_plist_format
buildFileTables
%s@%d: Will write to: %s\n
CCFile::withTap Unsupported file type(%d) \n
forEachTapWithOwnerAndPipe:Failed to malloc memory for valueArray
/Library/Logs/CrashReporter/CoreCapture
Got an XPC error: %s\n
CCDatabase::getStreamEntry: owner not found\n
%s@%d: bail - !saveDir\n
CCConfigure::policy policy: %u\n
gzflush failed errno = %d, errnum = %d, reason : %s, %s\n
DeviceInfo
Time usecs
CCIOReporterFormatter::getChannelsForSubscription  didn't find matching subscription\n
CCDatabase::removeStream: streamName is NULL\n
CCDatabase::removeStreamProperty: owner not found\n
SigningFuse
CCConfigure::pipeOwnerCFDictionaryApplier
CCLogTap::tapLoop(), Error setting notification port rc[0x%08x]\n
Invalid State readOffset : %d, writeOffset : %d state %c, entry %u 
CCDatabase::hasStream: pipeName is NULL\n
CCConfigurePipe
CCIOReportInterests
CCDaemon::%s Failed to delete file %s errno: %d
CCFile::writeMetadataFiles failed malloc\n
CFDataGetBytePtr() failed
CCPcapngFormatter::buildStreamToInterfaceTable: Stream header bytes: %s\n
XPC_TYPE_DATE
Stream
CCConfigure::pipeConfigureCFDictionaryApplier Key: %s\n
CCDaemon
CCPcapngFormatter::writeFileHeader Uninitialized fStreamNameArray, i: %d\n
storeChannelDescriptionFromStreamAndSubscription
com.apple.MCX._managementStatusChangedForDomains
CCConfigure::setConsoleLevel
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is %s NULL, with type %ld, but has type %ld\n
source_open_failed
CCFile::copyFile Wrote '%s' source length: %lld archive length: %lld (reason: %s) Owner:%s Pipe:%s\n
OSSerialize
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
%s:%d CCTap::withRegistryEntry Registry entry:%u not found\n
LogIdentifier
CCCacheDelete: framework not available on this platform\n
writeLogFooter
CCLogFile::configureLogOptions Configuration is %s\n
triggerStackshot_block_invoke
bin
CCDatabase::removePipe: pipe not found\n
source_read_failed
CCPipeMonitor::ccfree - fails to destroy lock. Error[%d]\n
%s:%d %s::withRegistryEntry entry:%u Owner:%s Name:%s
true
ERROR: FileURL not created\n
pcapng
CCDaemon::%s:%d unable to allocate destination buffer\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
Found blob name: %s:%d %llu %s\n
rescan
%s::%s !subscriptionLegendDictionaryArray\n
CCProfileMonitor::applyConfiguration profile is already removed or not installed
CoreCaptureStart called with bad args, crashing
CCOSSerializeWithIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
bluetooth.logging
%s::%s Can't create channelStreamDictionary\n
previous and current sequence numbers are same %u prev read offset %u,previous write offset %u, new write offset %u, entry %u\n
CCLogTap::isActive policy is %d, Owner:%s Name:%s entry:%u\n
Reason
CCLogTap::tapLoopImpl() entry:%u failed to unmap pipe with rc[0x%08x]\n
quiesceAllTaps:Failed to malloc memory for valueArray
amfm-sunrise
WiFi
refreshSubscriptionsFromStreamRegistry
XPC_TYPE_INT64
FileOptions
CCProfileMonitor::profileCallback read WiFi profile plist valid: %d mask: %d\n
getOwnersFromCCConfig
com.apple.corecapture.manager-access
(CCLogTap) CCPipeInterface::withRegistryEntry failed\n
Incorrect number [numberOfDirArrayEntries: %lld, readIndex %lld] of directory entries. Skip sorting.\n
CCDatabase::removeStream: ownerName is NULL\n
CoreCaptureStop called when no CCDaemon running, CCDaemon::isInitialized() returned false, ignoring
CCDaemon::runShutdownThread Exiting via xpc_transaction_try_exit_clean
%s.%06llu %s
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe initialized with %u total interfaces\n
PipeSize
CCIOReportRkey
forEachTapWithOwnerAndPipe:Failed to malloc memory for keyArray
profileRemoved:Failed to malloc memory for valueArray
%@\n%@\n
CCXPCService::handleIncomingMessage: incoming, incomingConnection from '%s' with pid '%d', XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n
CCXPCService::initWithConfigureAndPipeMonitor ERROR INIT MUTEX: %d\n
Token is [0]: 0x%x... [7]:%x \n
forEachTapWithDirectory:Failed to malloc memory for keyArray
CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n
CCTap::%s:%d entry:%u
... (%ld more bytes)
CCPipeMonitor::cleanCaptureDirectories - fails to unlock\n
%s:%06u memory alloc failed\n
CCDataTap
CCDatabase::addPipe: CFStringCreateCopy failed\n
CCLogFile::initWithConfig: Successfully initialized for non-IORegistry pipe\n
CCLogTap::configureLogOptions\n
waitForEvent
CCConfigure::applyConfiguration Configuration type is not dictionary\n
%s@%d: Problem merging channels\n
CCLogFile::withConfig() Invalid parameters\n
MaxFileSize
CCConfigure::capture Reason: %s\n
IOConnectCallAsyncStructMethod FAILED CCPipeInterface::%s::%d fNotificationPortIsSet:%d entry:%u kr[0x%08x]
cc.cachedelete.disable
Time localtime
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream name memory\n
com.apple.corecaptured.background_queue
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj %s is NULL, with type %ld, but has type %ld\n
getOsVersion %s\n
CCIOReportInterestSubscriptionIDx
CCPcapngFormatter::writeFileHeader: Empty pipeOwner or pipeName string\n
CCConfigure::captureDirectoryCFDictionaryApplier capture\n
activityCheck
CCDaemon::%s Failed to compress '%s%s'
CCProfileMonitor::setStreamEventHandler \n
CCLogFile::deleteFile successfully deleted: %s\n
Unexpected log parameters ring state3(0x%llx), ring buffer(0x%llx), ring size(%llu), logSize(%lu), logContinueSize(%lu) entry:%u\n
rc.ok
CCPipeInterface::initWithRegistryEntry entry:%u fConnectRef(%u)\n
CCFile::mkpath fails to create path '%s' as '%s' is not a directory\n
v12@?0i8
NULL
CCPipeInterface::IOServiceClose entry:%u fConnectRef(%d)\n
CCProfileMonitor::withPipeMonitor Failed to create CCProlieMonitor\n
CCFile::copyFile failed: %s file: '%s' Owner:%s Pipe:%s\n
CCDatabase::setStreamProperty: pipe not found\n
,
cc.recovery.allow
CCFile::populateCommonTelemetryDictionary - Failed to get config from database for owner/pipe\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n
%s:%06u: Invalid argument\n
cleanupLogFile
CCDatabase::findStream: pipe is NULL\n
CCDataFile::open Failed to create %s\n
Error: %s
CCLogTap::setConsoleLogFlags Owner:%s Name:%s entry:%u\n
CCPipeMonitor::ccfree Exit\n
%s:%d Owner:%s skipping profileLoaded
CCPcapngFormatter::searchStreamIdInRegistry: Found %ld streams in database\n
com.apple.corecapture.fileclose
CCFile::moveFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
(CCLogTap) IORegistryEntryCreateCFProperty failed for LogPolicy\n
none
CCPipeMonitor::%s:%d Release Tap for entry:%u
CCDaemon::%s:%d Error writing to destination buffer %s: %s\n
file:///private/var/Managed%20Preferences/mobile/com.apple.corecapture.configure.bt.plist
CCXPCService::handleIncomingMessage
CCFile::copyFile gzwrite error: %s\n
CCPipeInterface::setNotificationPort(), mach_port_get_attributes failed kr[0x%08x]\n
%s:%06u Triggering stackshot with id %s due to %s\n
owners_extraction_failed
CCProfileMonitor::profileRemoved Exited :%d\n
%z
%s - no fFile entry:%u
CCPipeMonitor::ccfree Exit - Destroyed lock\n
pruneDirectoryNDaysDo lstat failed on %s:\n%s\n
CCProfileMonitor::getOwnersFromCCConfig
CCDatabase::removeOwner: owner not found\n
CCDatabase::addStream: streamName is NULL\n
Unable to create IOReport Aggregate\n
CCLogFile::writeLog - File roll needed\n
CCConfigure::capture capture reason can not be NULL\n
%s:%06u Unable to copy arguments
%s@%d: Unable to create samples: %s\n
CCFile::initWithTap memory allocation failed\n
CCDatabase::removeStream: pipeName is NULL\n
CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions (attempt %d/%d)
CCPipeMonitor::isActive:no tap found
path
%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s/%s
mutex_lock_failed
XPC_TYPE_STRING
CCConfigure::streamConfigureCoreCaptureCFDictionaryApplier
OSSerializeWithIOReporter
invalid_plist
CCConfigure::captureDictionaryCFDictionaryApplier
[%04d-%02d-%02d_%02d,%02d,%02d.%06u]-%s-%03d.%s
tapLoop
seed build (or boot-arg) and device hasn't been unlocked since boot. Won't process event and continue when next event is posted entry:%u\n
historyDone
/IOReporters.%s
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get stream entry for stream %ld\n
profile_removed_notification
DeviceFusing
CCLogFile::initWithConfig: Unsupported log data type %d\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
PipeType
CCFile::initWithTap fLogDirPath is invalid\n
CCPcapngFormatter::writeFileHeader: Missing pipeOwner or pipeName\n
Failed to get fCaptureDirPath for purgeable marking\n
Failed to mark %s as purgeable %d (%s) (flags 0x%llx)\n
Notification to dump to disk failed for entry:%u
com.apple.corecaptured.CCIOReportDumpQueue
CCDaemon::ccstart to create CCDaemon\n
%s:%d processEvent for entry:%u Owner:%s Name:%s
CCLogTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
Entitlement is NULL \n
CCLogTap::tapLoopImpl() isLogdirExists failed\n
CCPcapngFormatter::searchStreamIdInRegistry: Stream not found in database\n
CoreCaptureStop setShutdownAlreadyTrue, exiting without doing anything
CCDataTap: Unable to create CCFile. entry:%u Owner:%s Name:%s\n
%s CANNOT FIND tap with Owner:%s Name:%s\n
CCCacheDelete: purge notification disabled\n
%s::%s didn't find or wrong type in array at i %ld\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
mergeProfilePlist
CCDatabase::removeStream: pipe not found\n
CCDatabase::setPipeProperty: owner not found\n
CCDatabase::getStreamConfig: stream not found\n
CCDatabase::getStreamEntry: pipe not found\n
CCLogFile::addFile Failed to create %s\n
CCOSSerializeWithIOReporterFormatter::writeLog unsupported root type for JSON Serialization
stopPipeMonitor
%s/%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s/%s
file:///private/var/Managed%20Preferences/mobile/com.apple.corecapture.configure.plist
CCLogFile::initWithRegistryEntry: pthread_mutex_init failed\n
profileRemoved:no tap found
triggerStackshot
kern.bootargs
CCDatabase::getStreamProperty: owner not found\n
CCStop
CCDataTap::isActive idle < duration  3 entry:%u duration:%f\n
CCDatabase::removeStream: stream not found\n
com.apple.corecaptured.shutdown
Unknown type: %llu %s:%d\n
source_buffer_alloc_failed
%s:%06u Stackshot rate limit: a stackshot was triggered within the last %d seconds. Skipping stackshot for id %s (reason: %s)\n
no_keys
*
CCDaemon::init failed to create come.apple.corecaptured.service_notify\n
LogType
false
CCPipeMonitor::%s:%d Release Tap i %zu
CCDaemon::%s:%d unable to create filePathRef\n
CCDatabase::setPipeProperty: pipe not found\n
CCDatabase::getStreamPropertyKeys: entry->properties is NULL\n
XPC_TYPE_DATA
CoreCaptureStop non daemon cleanup, calling ccfree\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  didnt find or not a dict in array\n
CCFile::isLogdirExists Failed to create  %s\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
XPC_TYPE_NULL
ProductType
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<array>\n
CCDatabase::findPipe: owner->pipes is NULL\n
CCXPCService::handleIncomingMessage Unable to allocate scratch buffer\n
/private/var
os-version
/System/Library/Extensions/corecapture.kext/Contents/version.plist
%s::%s Can't create subscriptionLegendDictionary\n
CCIOReporterFormatter::writeLog  Can't copy rawData\n
CCPipeMonitor::CCPipeMonitor Failed to initialize fMutex\n
CCDatabase::getPipeConfig: owner not found\n
doSaveChannels
%s::%s didn't find matching subscription\n
CCOwnerEntry copy constructor: malloc failed for %zu bytes\n
FileSize
CCFile::copyFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
osversion
CCProfileMonitor::profileCallback Entered source:%d token:%d\n
CCLogFile::withConfig()\n
CCLogFile::withConfig() Invalid log type %d\n
CCLogTap::setLogFlags Owner:%s Name:%s entry:%u\n
DirectoryName
CCDaemon received system shutdown notification, all cctap quiesced\n
CCConfigure::pipeConfigureCFDictionaryApplier capture\n
CCDaemon::init Failed to create CCProfileMonitor\n
dest_open_failed
CCDatabase::addPipe: failed to find/create owner\n
CCDatabase::getPipeProperty: entry->properties is NULL\n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  rawData or interests not available\n
CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next. entry:%u Owner:%s Name:%s\n
CCFile::moveFile Moved '%s' -> '%s' (reason: %s) Owner:%s Pipe:%s\n
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe missing owner or name\n
(CCLogTap) IORegistryEntryCreateCFProperty failed\n
deleteDirectory: deleting '%s' reason: %s
CCDatabase::setStreamProperty: key is NULL\n
CCDatabase::findPipe: owner is NULL\n
CCDatabase::getPipes: owner not found\n
CCDatabase::getStreamPropertyKeys: owner not found\n
CCPipeInterface::setNotificationPort(), mach_port_allocate failed kr[0x%08x]\n
CCPipeMonitor::ccfree Entered\n
CCDatabase::getStreams: owner not found\n
CCXPCService::handleIncomingMessage keycount : %ld\n
IOReportSubGroupName
CCFile::moveFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCLogTap::profileRemoved, Owner:%s Name:%s entry:%u\n
CCPipeInterface::%s::%d fNotificationPortIsSet:%d rc:%d entry:%u
CCDaemon::Not all taps got quiesced, tap %ld was not ready
Time secs
Prod
CCOwnerEntry operator=: malloc failed for %zu bytes\n
CCConfigure::pipeConfigureCFDictionaryApplier pipe policy\n
CCDataTap::processEvent already quiesced entry:%u Owner:%s Name:%s\n
CCPipeMonitor::ccfree - fails to destroy fMutex lock. Error[%d]\n
com.apple.corecaptured.purge
CCDaemon::%s:%d Trying to compress file %s%s\n
CCDaemon::%s:%d unable to allocate source buffer\n
CCDatabase::getPipes: no pipes in owner\n
CCPcapngFormatter::writeLogHeader logMetaData is NULL\n
CCConfigure::pipeConfigureCFDictionaryApplier Unsupported Key %s\n
CCPipeInterface::resetDispatchQueue re-targeted notification port to capture queue entry:%u Owner:%s Pipe:%s\n
CCPipeMonitor::CCPipeMonitor Failed to initialize mutex\n
CCDatabase::reset: malloc failed for %zu bytes\n
CCDatabase::getStreamConfig: owner not found\n
IOService
Entitlement couldnt be found \n
MaxNumberOfFiles
pruneDirectoryOnOSUpgrade: upgraded from %s to %s
CCServiceMonitor::scanServices fMatching Dictionary Retain count(1) is %ld\n
CCDatabase::findOwner: database is NULL\n
CCDatabase::removePipeProperty: owner not found\n
XPC_TYPE_ARRAY
CCDaemon::%s:%d fileName is invalid\n
%s:%06u: CFStringGetCString failure\n
CCDaemon::init: clearing working directory on startup
%s::%s key %s has wrong type in dictionary\n
CCConfigure::pipeConfigureCFDictionaryApplier
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
Session Name: %s, Blob Name: %s %llu.%llu Owner:%s Name:%s\n
CCDaemon::%s:%d failed to open source buffer %s\n
Dev
%s::%s failed to store description\n
CCDatabase::getPipeEntry: owner not found\n
CCDatabase::hasStream: pipe not found\n
IOReportCreateSamplesRaw() returned 0 sized dictionary %s
profileLoaded:Failed to malloc memory for valueArray
%@ %@ (%@)
CCPcapngFormatter::writeLog Failed to write(2) Length=%lu, tempLength=%lu\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.\n
capture.plist
%s::%s didn't find %s or wrong type in array at i %ld\n
CCDatabase::getStreamPropertyKeys: no properties in stream\n
CCConfigure::streamConfigureConsoleCFDictionaryApplier
Text
CCDatabase::addOwner: ownerName is NULL\n
v16@?0^v8
CCLogFile::configureLogOptions Configured Log Type:%d, File Size=%u, Max Number Of Files:%u\n
%s:%06u Invalid captureId
CCLogTap::%s invalid logPipeInterface\n
CCCacheDelete: failed to create dispatch queue\n
Stream Name is %s\n
createDictionaryWithProcessedIOReporter
CCPipeMonitor::ccfree - fails to unlock. Error[%d]\n
CCConfigure::capture
LogFlags
CCLogTap::setWatermarkLevel\n
Id
CCProfileMonitor::setStreamEventHandler Unable to get notification center for configuration reader.
Found SessionName: %s:%d %llu %s\n
forEachTapWithOwnerAndPipe
CCIOReporterFormatter::writeLog  Inconsistent data (1) length=%lu\n
%s:%06u unable to create set\n
CCPipeEntry::~CCPipeEntry: malloc failed for %zu bytes\n
CCDatabase::hasStream: streamName is NULL\n
CCDatabase::getStreams: pipe->streams is NULL\n
CCPcapngFormatter::writeLogFooter logMetaData is NULL\n
CCDataTap::%s:%d cast failed\n
CCDaemon::%s:%d fileName is invalid
Time
com.apple.corecaptured.CCTap
%s@%d: fExitNextIteration bailing out\n
Data
LogFileSize
CCPipeInterface::dispatch_source_create failed
CCIOReporterFormatter::getChannelsForStreamAndSubscription  Couldnt find %s\n
CCProfileMonitor::freeResources Entered\n
CCPipeEntry operator=: malloc failed for %zu bytes\n
CCDatabase::getStreamProperty: stream not found\n
WiFiFWTrapBinary
%s/%s
CCLogFile::initWithRegistryEntry: pthread_mutexattr_settype failed\n
IOReporter
create_protected_file_failed
Raw
disable
SourceVersion
%s::%s failed to store Channel Description\n
CCDatabase::removePipe: owner not found\n
CCLogFile::cleanupCapturedFiles log type is %d, current file is %s\n
CCDaemon::init failed to create com.apple.corecaptured.background_queue\n
cc.debug.keepwd
IOReportChannels
%s::%s not a matching Stream id\n
%s::%s didn't find or not a dict in array\n
CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback to check for installed profiles\n
no_remote_connection
Console
CCPipeMonitor::CCPipeMonitor Failed to CCIOReportDumpProcessor.\n
pruneDirectoryOnOSUpgrade: activity enabled; snapshot %s, osversion %s\n
CCProfileMonitor::applyConfiguration profile is already removed
initWithRegistryEntry
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  failed to store Channel Description\n
CCDataTap::initWithRegistryEntry invalid fPipeInterface\n
CCIOReporterFormatter
CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n
CCDatabase::hasPipe: pipeName is NULL\n
fileDidOpen
CCLogFile::initWithConfig: CFNumberCreate failed for logDataType\n
CCLogFile::initWithConfig: Failed to create formatter\n
cleanCaptureDirectories:Failed to malloc memory for keyArray
servicePublished
CCLogFile::configureLogOptions Current Log Type:%d, File Size=%u, Max Number Of Files:%u\n
CCOSSerializeFormatter::writeLog unsupported root type for JSON Serialization
Invalid Meta Key. Bail.
WiFiFWTrap
CCDatabase::getStreamPropertyKeys: pipe not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream header memory\n
success
isActive:Failed to malloc memory for valueArray
hw-model
CCDatabase::findStream: pipe->streams is NULL\n
CCXPCService::handleIncomingMessage shutdown pending true, dropping message and exiting\n
config_alloc_fail
CCDatabase::removePipe: pipeName is NULL\n
%s Ring offset out of range: %u > %llu entry:%u\n
CCDatabase::getStreamConfig: pipe not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate Interface ID memory\n
^v8@?0
CCStart
CCDaemon::runShutdownThread Failed to exit cleanly after %d attempts, forcing exit
ALL
CCDatabase::findOwner: ownerName is NULL\n
0x%016x
%s:%d processEvent entry:%u Owner:%s Name:%s
Received Capture Event entry:%u Owner:%s Name:%s\n
BT 
unknown
CCFile::moveFile Failed to delete source file after copy: '%s', errno: %d\n
CCPipeInterface::initWithRegistryEntry [pipeOwner: %s, pipeName: %s] Failed to initialize returned %x\n
CCCacheDelete: purge notification already enabled\n
%s@%d: fCancelableBlock bailing out\n
CCPcapngFormatter::writeLog  Inconsistent data (1) length=%lu\n
CCPipeInterface::setDispatchQueue re-targeted notification port to continuous queue entry:%u Owner:%s Pipe:%s\n
CCDataFile::sendTelemetry failed
setNotificationPort
%s:%06u: Failed reading '%s' from registry\n
CCDaemon received power notification (0x%x) \n
CompressionDisabled
CCPipeInterface::setDispatchQueue entry:%u Owner:%s Pipe:%s\n
LogOptions
[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s
CCPipeInterface::resetDispatchQueue re-targeted dispatch source to capture queue entry:%u Owner:%s Pipe:%s\n
%s:%06u Invalid reason
CCPcapngFormatter::buildStreamToInterfaceTable: Found %ld streams in database\n
InverseDeviceID
max_preserved_captures
%s:%s
CCDatabase::getStreamProperty: pipe not found\n
CCDaemon::init CoreCaptureStart was already called\n
CCDatabase::setPipeProperty: key is NULL\n
CCOSSerializeFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
debug_data
Continuous
CCLogTap::withRegistryEntry failed\n
</array>\n</plist>\n
/private/var/tmp/com.apple.corecaptured/com.apple.bluetooth.logging.plist
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d)\n
invalid_plist_type
IOReportGroupName
CCFile::initWithTap Failed to get log directory \n
CCFile::captureLog Failed to create directory %s (reason: %s)\n
CrashTracerLog
WiFi 
CCPcapngFormatter::writeFileHeader: Failed to cast fWriteObject to CCFile\n
rb
boot-args
%s:%06u keycount : %ld\n
CCIOReportDumpQueue
CCFile::captureLog\n
IOReturn CCLogTap::processEvent(CCLogPipeInterface *)
tick-frequency
CCDaemon::sendProfileChangeNotification profile change notification received\n
CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n
CCDatabase::findStream: streamName is NULL\n
CCLogFile::initWithConfig: buildFileTables failed\n
/var/log/CoreCapture
CCIOReporterFormatter::getChannelsForStreamAndSubscription  no key %s in dictionary\n
withRegistryEntry
buffer_alloc_fail
Unexpected event type %s\n
%s:%06u: Failed getting number\n
CCOSSerializeWithIOReporterFormatter::processAllDictionarieswithinIncommingArray  didnt find or wrong type in array at i %ld\n
Found session timestamp: %s:%d %llu %llu.%llu\n
(CCLogTap) CFNumberGetValue failed\n
pruneDirectoryNDaysRead cap %ld\n
CCDaemon received system wake or will not sleep (0x%x), all cctap resumed from quiesced state\n
BootArgs
CCDaemon power notification disabled\n
MGCopyAnswer
Unknown
%s::%s channelStreamArray at i %ld not valid\n
v16@?0@\"NSObject<OS_xpc_object>\"8
CCLogFile::initWithConfig: Number of files cannot be 0\n
CCLogFile::deleteFile failed to delete: %s, errno: %d\n
CCPipeInterface::%s:%d mach_msg SEND_MSG kr:%u entry:%u
resumeAllTapsFromQuiesced:Failed to malloc memory for valueArray
CCDatabase::addOwner: CFStringCreateCopy failed\n
XPC_TYPE_ERROR
CCLogFile::initWithConfig: Failed to create directory/file name strings\n
CCConfigure::configureLogOptions
XPC_TYPE_DICTIONARY
%s Read pointer moved while copying metadata. Retrying entry:%u\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in array at i %ld\n
CCDatabase::removeStream: owner not found\n
CCDaemon received system sleep notification (0x%x), all cctap quiesced\n
%s Read Ptr is not multiple of %lu (%d) entry:%u \n
CCLogFile::initWithConfig: Failed to initialize PCAP formatter\n
CCConfigure::findTapWithOwnerAndPipe found CCTap, Owner: %s, Pipe: %s\n
CCProfileMonitor::profileCallback read BT profile plist valid: %d mask: %d\n
invalid_reference
CCFile::initWithTap Failed to create log directory  %s\n
cleanCaptureDirectories:Failed to malloc memory for valueArray
CCProfileMonitor::sendProfileChangeNotification profile change notification received\n
pruneDirectoryNDaysDo: older than %ld days (age=%.0fs)
CCLogFile::withRegistryEntry()\n
CCLogFile::sendTelemetry failed
CCFile::moveFile failed: %s file: '%s' Owner:%s Pipe:%s\n
???
writeMetadataSystemPlist
CCDatabase::addStream: CFStringCreateCopy failed\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCFile::captureLogRun Skipping current file Dir file %s, Current File %s Owner:%s Pipe:%s\n
Log
CCDatabase::getOwners: no owners in database\n
CCDatabase::addStream: owner not found\n
CCConfigureStream
CCPipe
CCProfileMonitor
CCConfigure::configure key is %s\n
ERROR INIT COND: %d\n
CCXPCService::handleIncomingMessage release, incomingConnection\n
CCLogFile::initWithConfig: pthread_mutex_init failed\n
Found blob length: %s:%d %llu %zu\n
profileRemoved:Failed to malloc memory for keyArray
IOServiceTerminate
CCPcapngFormatter::writeFileHeader: Non-IORegistry pipe - owner=%s, name=%s\n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  contains %s %d contains %s %d\n
LogDataType
CCPipeEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::~CCDatabase: malloc failed for %zu bytes\n
Couldn't update read ptr.\n
_
%s::%s clearing out any previous subscriptions\n
CCProfileMonitor::profileCallback empty dictionary. fProfileLoaded %d fProfileRemoveApplied %d\n
CCProfileMonitor::profileCallback Loaded\n
NumberOfFiles
writeLogHeader
CCPipeMonitor::ccfree Failed to acquire lock\n
CCDaemon will calling shutdown()\n
CCDataTap::%s invalid dataPipeInterface\n
CCDatabase::getPipePropertyKeys: owner not found\n
%s@%d: bail - !filePath\n
%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s
CCConfigure::pipeConfigureCFDictionaryApplier Owner: %s\n
Found blob timestamp: %s:%d %llu %llu.%llu\n
%s - localLogMetadata.payloadLength + logPayloadOffset IS BEYOND RINGSIZE. ADJUST entry:%u
CCConfigure::streamStreamCFDictionaryApplier
CoreCaptureStop non daemon stopping, calling quiesceAllTaps()\n
Created a bad offset, don't save it! newOffset %u, payload length %u, padding %u,sizeof metadata %lu, STATE %c, entry:%u
addRegistryChildToChannelDictionary
CaptureReason
CCConfigure::pipeConfigureCFDictionaryApplier Pipe: %s\n
CCConfigure::watermarkLevel
CCFile::withRegistryEntry() entered entry:%u\n
CCPipeInterface::setDispatchQueue re-targeted dispatch source to continuous queue entry:%u Owner:%s Pipe:%s\n
User
CCXPCService::handleIncomingMessage Key is %s\n
CCConfigure::pipeConfigureCFDictionaryApplier Configure Log Options\n
CCDaemon:: No name matching CCPipe service found \n
cc.log.seed
CCDaemon::%s:%d dirPath is invalid
%s::%s channelStreamArray not valid\n
CCProfileMonitor::profileCallback changed. previous state: %d, current state: %d\n
CCDatabase::hasOwner: ownerName is NULL\n
rc
CCIOReportRdata
FileCloseReason
CCLogTap::freeResources() entry:%u failed to unmap pipe with rc[0x%08x]\n
209
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCServiceMonitor::servicesPublished ignoring processing servicePublished due to isShutdownPending
CCConfigure::pipePipeCFDictionaryApplier
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n
CCLogFile::initWithRegistryEntry buildFileTables\n
UniqueDeviceID
CCIOReporterFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCLogFile::initWithRegistryEntry \n
CCFile::captureLogRun moving files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
CCLogTap::updateConsoleLogFlags Owner:%s Name:%s entry:%u\n
XPC_TYPE_FD
LogLevel
CCDaemon:: Num of matching CCPipe %ld\n
CCDaemon::%s:%d unable to create class with protection flag\n
LogEvents
CCConfigure::setLevel
CCOSSerializeFormatter::writeLog CFDataGetBytePtr() failed
CCDaemon::%s CCDaemon::getInstance().isShutdownPending() == true, skipping activityCheck()
CCServiceMonitor::ccfree()\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  dictionary doesn't contain %s\n
CCDatabase::getPipes: malloc failed for %zu bytes\n
CCTextFormatter::buildLogIdentTable -- alloc failed\n
CCPcapngFormatter::writeLog Failed to write(1) Length=%lu, tempLength=%lu\n
rename_failed
CCCacheDelete: cannot register for purge notifications ret=0x%x\n
mach-absolute-time
CCLogFile::initWithRegistryEntry Number of files can not be 0.\n
CCDaemon::%s initial scan not complete, staying active
CCTerminate
CCProfileMonitor::profileCallback during shutdown at %d\n
CCDatabase::removePipeProperty: pipe not found\n
CCPcapngFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCConfigure::captureDirectoryCFDictionaryApplier Key: %s\n
getting CC session id failed for entry:%u
CCPcapngFormatter::searchStreamIdInRegistry: Non-IORegistry pipe, querying CCDatabase for streamId=%u\n
Policy
CCDaemon::init Failed to initialize mutex\n
findTapWithOwnerAndPipe:no tap found
\n
CoreCaptureStop called when isShutdownPending true, ignoring
CCDaemon::ccstart to create CCDaemon
CCLogTap::profileLoaded, Owner:%s Name:%s\n
CCCacheDelete: no directories provided\n
ProfileLoaded
Owner
com.apple.corecaptured.cachedelete
cancelableBlockFunc_block_invoke
CCXPCService::cancelActiveConnections cancelling %lu connections\n
CCConfigure::watermarkLevel watermarkLevel: %u\n
%s:%06u failed to allocate memory\n
CCDatabase::addPipe: pipeName is NULL\n
/%s/%s/
Entitlement exists, and check is successful\n
CCDaemon::freeResources: clearing working directory on shutdown
CCFile::writeDataFiles memory allocation failed (reason: %s)\n
%s Duplicate Owner:%s Name:%s entry:%u\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream[%u]: name=%s, id=%u, dlt=%u\n
CCConfigure::captureDirectoryCFDictionaryApplier
Capture
CCConfigure::policy
CCPipeInterface::%s:%d rcvd terminate msg:0x%x entry:%u
CCPipeInterface::setNotificationPort(), mach_port_insert_right failed kr[0x%08x]\n
CCPcapngFormatter::buildStreamToInterfaceTable: Found stream header (%ld bytes) for stream\n
CCPipeMonitor::%s:%d Tap corresponding to Pipe not found
%02x 
json
ips
CCDatabase::hasStream: ownerName is NULL\n
CCPcapngFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
Circular
CCDatabase::getStreams: malloc failed for %zu bytes\n
CCLogFile::initWithConfig: Failed to create working directory string\n
UUID
CCFile::initWithTap create with cstring failed\n
forEachTapWithDirectory:no tap found
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCLogTap::setConsoleLogLevel Owner:%s Name:%s entry:%u\n
%s:%d Owner:%s Name:%s entry:%u
CCDaemon::%s Compressed '%s%s' -> %lld bytes
pruneDirectoryOnOSUpgrade: activity disabled\n
NotifyTimeout
WatermarkLevel
/
CCDaemon::init Failed to create CCPipeMonitor\n
CCOSSerializeWithIOReporterFormatter::writeLog CFDataGetBytePtr() failed
CCFile::initWithTap Failed to create formatter\n
CCDaemon::%s:%d Error reading from source buffer %s\n
CCDaemonProfile Changed
CCDaemon power notification enabled\n
CCProfileMonitor::profileCallback getting owners from profile failed
CCProfileMonitor::getOwnersFromPipesAndStreams
freeResources
CCConfigure::pipePipeCFDictionaryApplier Pipe: %s\n
%s NULL value.\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.
CCConfigure::captureDictionaryCFDictionaryApplier dirName: %s\n
CCDataFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCProfileMonitor::initWithConfigure ERROR INIT MUTEX: %d\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to convert stream name\n
%s:%d: mmap failed\n
CCDaemon::init invalid arguments passed for non-daemon case\n
CCConfigure::applyConfiguration
CCDaemon::%s:%d dirPath is invalid\n
CCConfigure::applyConfiguration CCSTOP key  \n
CCDaemon::%s monitor NOT active, shutdown
CCDatabase::getPipePropertyKeys: pipe not found\n
CCDatabase::setStreamProperty: stream not found\n
CCXPCService::handleIncomingMessage Unable to get remote connection\n
%b %d %H:%M:%S
resumeAllTapsFromQuiesced:Failed to malloc memory for keyArray
wlan
%s:%06u: Invalid type\n
%s::%s didn't find %s\n
CCLogFile::initWithConfig: pthread_mutexattr_init failed\n
CCConfigure::applyConfiguration CCSTART key \n
CCDaemon::startPipeMonitor CCDaemon not yet initialized, exiting
CCIOReporterFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCDatabase::removePipeProperty: property key not found\n
CCPipeMonitor::isActive: recent serviceTerminated, staying active\n
servicesTerminated
CCIOReportStream
CCDatabase::getPipeProperty: owner not found\n
%s@%d: bail - !allChannels\n
CCPcapngFormatter::writeLogHeader fStreamHeaderArray failed to write length %ld. %s\n
com.apple.corecaptured.service_notify
CCDataTap::profileLoaded, Owner: %s, Name: %s\n
isActive:Failed to malloc memory for keyArray
xml
CCLogDisable
CCXPCService::handleIncomingMessage XPC message is not dictionary\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  Cant create channelStreamDictionary\n
shutdown_pending
CCOwnerEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::getOwners: malloc failed for %zu bytes\n
None
%s@%d: bail - !mkdirRecursive\n
CCConfigure::captureDirectory
CCDataTap::tapLoop(), Error setting notification port rc[0x%08x]\n
/Library/Logs/CoreCapture
hw.model
CCIOReporterFormatter::addRegistryChildToChannelDictionary  not array\n
%s:%06u Configuration type is not dictionary\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_init failed\n
com.apple.corecaptured.serial_queue
findTapWithOwnerAndPipe:Failed to malloc memory for keyArray
com.apple.notifyd.matching
CCProfileMonitor::profileCallback starting states -> source %d fProfileToken %d isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n
XPC_TYPE_UUID
CCLogFile::initWithConfig: Invalid arguments\n
%u.%06u
tapLoopImpl
MultiFunctionManager
StreamHeader
CCConfig is %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj %s is NULL, with type %ld, but has type %ld\n
serviceTerminated
BuildVariant
empty_configuration
%s:%06u invalid configuration\n
CCDatabase::findPipe: pipeName is NULL\n
CCPcapngFormatter:: failed to get stream id\n
CCXPCService::handleConnectionEvent CCDaemon::getInstance().isShutdownPending() true, dropping xpc event and exiting\n
CCDaemon::init failed to create com.apple.corecaptured.serial_queue\n
CCConfigure::captureDirectoryCFDictionaryApplier Pipe: %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
CCLogTap::updateLogFlags\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  key %s has wrong type in dictionary\n
XPC_TYPE_SHMEM
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate dlt memory\n
storeChannelDescriptionFromSubscription
CCLogTap
CCLogFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCLogTap::%s:%d cast failed\n
XPC_TYPE_BOOL
set_protection_class_failed
CCDatabase::getStreams: pipe not found\n
CCCacheDelete: purge history processing complete\n
CCConfigure::streamOwnerCFDictionaryApplier
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe, getting config from database\n
CCLogTap::%s:%d tapLoopImpl entry:%u Owner:%s Name:%s\n
CCLogTap::tapLoop entry:%u Owner:%s Name:%s Exiting taploop\n
%s::%s shapeIOReportLibraryFriendlyDictionary failed\n
getOwnersFromPipesAndStreams
gzwrite_failed
CaptureEvent
can reduce logging: %d\n
%s@%d: Unable to create subscribtion: %s\n
CCConfigure::streamConfigureCFDictionaryApplier
CCPipeMonitor::CCPipeMonitor Failed to create pipe dictionary.\n
CCCacheDelete: cannot create monitored directories\n
CCConfigure::configureOptions Not found the tap owner:%s, pipe: %s\n
CCProfileMonitor::setStreamEventHandler event received:%s\n
CCPcapngFormatter::writeLog Unexpected log data \n
CCLogFile::addFile: No log before device first unlocked for PROTECTION_CLASS_C\n
%s::%s rawStreamAndSubscriptionArray not valid\n
CCXPCService::handleIncomingMessage empty configuration\n
CCXPCService::startXPCService() Failed to start XPC service \n
%s - STATE IS RESERVED. BREAK entry:%u
CFPropertyListCreateData() failed
CCDatabase::getPipes: owner->pipes is NULL\n
XPC_TYPE_CONNECTION
Received Skip Event %u\n
CCLogTap::setNotifyTimeout\n
CCServiceMonitor::scanServices fMatching Dictionary Retain count(2) is %ld\n
CCDatabase::getPipeProperty: pipe not found\n
forEachTapWithOwnerAndPipe:no tap found
profileLoaded:Failed to malloc memory for keyArray
221
CCConfigure::notifyTimeout notifyTimeout: %u\n
CCFile::captureLogRun Failed to stat file %s%s, errno: %d Owner:%s Pipe:%s\n
CCOwnerEntry::~CCOwnerEntry: malloc failed for %zu bytes\n
```
