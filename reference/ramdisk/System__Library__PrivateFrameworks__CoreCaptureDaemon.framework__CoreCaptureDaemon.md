# `/System/Library/PrivateFrameworks/CoreCaptureDaemon.framework/CoreCaptureDaemon`

From the upgrade restore ramdisk (141-29011-104.dmg). 744,064 bytes.

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
Received Capture Event entry:%u Owner:%s Name:%s\n
CCLogTap::setWatermarkLevel\n
CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory errno %d\n
CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n
CCDatabase::findPipe: pipeName is NULL\n
CCDatabase::addOwner: ownerName is NULL\n
CCDaemon purge notification enabled\n
(CCLogTap) CCPipeInterface::withRegistryEntry failed\n
CCDaemon::%s:%d filePath may get truncated. Returning...
CCServiceMonitor::scanServices fMatching Dictionary Retain count(1) is %ld\n
owner=%s pipe=%s dirName=%s
result=failed reason=null_allChannels
CCLogFile::initWithConfig: pthread_mutexattr_init failed\n
CCDataTap_initWithRegistryEntry
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe, getting config from database\n
CCLogFile::initWithConfig\n
CCConfigure::captureDirectoryCFDictionaryApplier Pipe: %s\n
result=failed reason=bad_args
CoreCaptureStop non daemon stopping, calling quiesceAllTaps()\n
CCLogPipeInterface_setLogLevel
CCIOReporterFormatter::addRegistryChildToChannelDictionary  dictionary doesn't contain %s\n
CCProfileMonitor::applyConfiguration profile is already removed or not installed
CCLogFile::writeLog - File roll needed\n
CCDaemon_ResumeAll
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj %s is NULL, with type %ld, but has type %ld\n
(CCLogTap) CFNumberGetValue failed\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap pipe with rc[0x%08x]\n
forEachTapWithOwnerAndPipe:Failed to malloc memory for keyArray
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in dict at i %ld for %s\n
CCProfileMonitor::setStreamEventHandler eventType unhandled:%@
CCLogFile::initWithConfig: CFNumberCreate failed for pipeType\n
CCConfigure::configureOptions Not found the tap owner:%s, pipe: %s\n
CCDaemon::enablePurgeNotification failed to get save location\n
CCFile::captureLogRun Current File %s (reason: %s) Owner:%s Pipe:%s\n
%s:%06u: Allocation failure\n
CCIOReporterFormatter::writeLog  Didn't find channels\n
CCProfileMonitor_ApplyProfile
CCDatabase::findPipe: owner->pipes is NULL\n
result=complete
IOReportCreateSamplesRaw() returned 0 sized dictionary %s
owner=%s pipe=%s reason=%s
CCFile::moveFile Moved '%s' -> '%s' (reason: %s) Owner:%s Pipe:%s\n
result=mutex_failed
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
CCPcapngFormatter::writeLogHeader Failed to write. %ld\n
CCPcapngFormatter::searchStreamIdInRegistry: Found matching stream in database\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate log identifier memory\n
result=active
Entitlement exists, but check failed. \n
%s - localLogMetadata.payloadLength + logPayloadOffset IS BEYOND RINGSIZE. ADJUST entry:%u
CCLogFile::initWithRegistryEntry buildFileTables\n
owner=%s pipe=%s streamName=%s
plist1=%s plist2=%s
CCXPCService::handleIncomingMessage keycount : %ld\n
Token is [0]: 0x%x... [7]:%x \n
CoreCaptureStop complete\n
CCDaemon received system sleep notification (0x%x), all cctap quiesced\n
result=failed reason=property_value_failed
%s - no fFile entry:%u
profileLoaded:no tap found
resumeAllTapsFromQuiesced:Failed to malloc memory for valueArray
%s:%06u keycount : %ld\n
Unable to create IOReport Aggregate\n
CCConfigure::findTapWithOwnerAndPipe found CCTap, Owner: %s, Pipe: %s\n
CoreCaptureStop non daemon cleanup, calling ccfree\n
%s:%06u: Invalid argument\n
%s::%s no key %s in dictionary\n
CCPipeEntry copy constructor: malloc failed for %zu bytes\n
CCOwnerEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::hasStream: ownerName is NULL\n
CCDatabase::getStreamProperty: stream not found\n
CCFile_writeDataFiles
result=exception exception=%s
result=failed reason=invalid_args
result=failed reason=log_directory_creation_failed
CCPipeMonitor::isActive: recent serviceTerminated, staying active\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream header bytes: %s\n
CoreCapture_Start
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCPipeMonitor::ccfree Exit\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  key %s has wrong type in dictionary\n
result=failed reason=mutex_lock_failed
CCProfileMonitor_ApplyConfiguration
CCTap_cleanCaptureDirectories
CCDatabase::setPipeProperty: owner not found\n
CCPipeInterface::setNotificationPort(), mach_port_allocate failed kr[0x%08x]\n
CCPipeMonitor::%s:%d Release Tap for entry:%u
CCProfileMonitor_ProfileRemoved
CCDatabase::getPipeConfig: pipe not found\n
CCDatabase::setStreamProperty: owner not found\n
result=success numberOfFiles=%u maxFiles=%u
%s:%06u: Failed getting number\n
CCDaemon::%s CCDaemon::getInstance().isShutdownPending() == true, skipping activityCheck()
CCFormatter::withLogType Unsupported log data type(%d) \n
%s:%d CCTap::withRegistryEntry Registry entry:%u not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream header memory\n
CCConfigure::capture Reason: %s\n
result=success
CCPipeInterface::setDispatchQueue re-targeted dispatch source to continuous queue entry:%u Owner:%s Pipe:%s\n
%s::%s !subscriptionLegendDictionaryArray\n
CCDatabase::getStreamPropertyKeys: stream not found\n
%s@%d: Will write to: %s\n
CCXPCService::handleIncomingMessage: incoming, incomingConnection from '%s' with pid '%d', XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n
CCLogFile::withRegistryEntry() Invalid log type %d\n
CCOSSerializeFormatter::writeLog CFDataGetBytePtr() failed
CCDaemon::shutdown is fired\n
CCDaemon_ActivityCheck
CCDaemon_PowerEvent
CCDaemon::init failed to create come.apple.corecaptured.service_notify\n
CCDataPipeInterface_readData
CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n
getOsVersion %s\n
CCConfigure::captureDirectoryCFDictionaryApplier dirName: %s\n
Failed to mark %s as purgeable %d (%s) (flags 0x%llx)\n
CCPipeMonitor::ccfree Entered\n
CCPipeMonitor_ProfileRemoved
%s::%s failed to store Channel Description\n
CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n
%s:%06u memory alloc failed\n
CCDatabase::getPipeProperty: entry->properties is NULL\n
CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions (attempt %d/%d)
CCDaemon::Not all taps got quiesced, tap %ld was not ready
CCDatabase::getPipeProperty: owner not found\n
No channels found\n
%s:%d: mmap failed\n
CCLogFile::initWithConfig: Number of files cannot be 0\n
CCLogFile::configureLogOptions Configured Log Type:%d, File Size=%u, Max Number Of Files:%u\n
CCDaemon::%s:%d dirPath is invalid
%s::%s clearing out any previous subscriptions\n
CCProfileMonitor::withPipeMonitor Failed to create CCProlieMonitor\n
CCDatabase::getStreams: pipe->streams is NULL\n
ERROR: cannot build the XML data\n
CCPcapngFormatter::writeLog Failed to write(1) Length=%lu, tempLength=%lu\n
Received a connection event\n
Entitlement couldnt be found \n
CCFile::copyFile gzwrite error: %s\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCIOReporterFormatter::writeLog  Can't copy rawData\n
CCDatabase::getStreams: pipe not found\n
CCLogFile::initWithConfig: CFNumberCreate failed for logDataType\n
result=failed reason=log_dir_path_invalid
CCLogTap::tapLoopImpl() isLogdirExists failed\n
result=malloc_failed
%s::%s Can't create subscriptionLegendDictionary\n
CCTap_initWithRegistryEntry
CCDatabase::getPipePropertyKeys: pipe not found\n
CCDatabase::getStreamConfig: pipe not found\n
CCPcapngFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCDaemon::startPipeMonitor CCDaemon not yet initialized, exiting
Unexpected log parameters ring state3(0x%llx), ring buffer(0x%llx), ring size(%llu), logSize(%lu), logContinueSize(%lu) entry:%u\n
CCLogPipeInterface_setConsoleLogLevel
forEachTapWithOwnerAndPipe:no tap found
CCProfileMonitor::freeResources done\n
CCDatabase::removeStream: stream not found\n
filePath=%s
CCXPCService::handleConnectionEvent CCDaemon::getInstance().isShutdownPending() true, dropping xpc event and exiting\n
result=already_shutdown
CCDaemon::%s:%d failed to open source buffer %s\n
CFPropertyListCreateData() failed
CCIOReportDumpQueue_ProcessorThread
CCConfigure::pipeConfigureCFDictionaryApplier Unsupported Key %s\n
owner=%s pipe=%s policy=%u
CCLogTap::configureLogOptions\n
CCPipeMonitor::CCPipeMonitor Failed to CCIOReportDumpProcessor.\n
CCProfileMonitor::cancelObservers removing event stream handler and Darwin observer\n
source=%d previousState=%d fProfileToken=%d
CCXPCService_FreeResources
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  failed to store Channel Description\n
(CCLogTap) IORegistryEntryCreateCFProperty failed\n
owner=%s pipe=%s timeout=%u
CCDaemon::%s:%d unable to create filePathRef\n
CCDaemon::%s:%d Error reading from source buffer %s\n
owner=%s pipe=%s reason=resumeFromQuiesced
CCOwnerEntry copy constructor: malloc failed for %zu bytes\n
CCDatabase::addPipe: CFStringCreateCopy failed\n
CCDaemon::sendProfileChangeNotification profile change notification received\n
CCLogPipeInterface_updateConsoleLogFlags
CCPipeMonitor::ccfree - fails to destroy lock. Error[%d]\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCProfileMonitor::sendProfileChangeNotification profile change notification received\n
CCDatabase::addPipe: pipeName is NULL\n
CCDatabase::removePipe: ownerName is NULL\n
CCDatabase::getStreamEntry: owner not found\n
CCPipeMonitor::isActive:no tap found
CCDaemon::%s:%d Error writing to destination buffer %s: %s\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
result=failed reason=dict_alloc_failed
result=failed reason=keys_alloc_failed
CCTap_freeResources
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get CCFile object\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate dlt memory\n
%s:%d CCDataTap::tapLoopImpl for entry:%u
result=%s logDataType=%d
%s Ring offset out of range: %u > %llu entry:%u\n
CCCacheDelete: framework not available on this platform\n
CCDatabase::getPipeEntry: owner not found\n
CCLogFile::initWithRegistryEntry: Invalid arguments\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_init failed\n
CCLogFile::addFile Failed to create %s\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in array at i %ld\n
CCDatabase::removeStreamProperty: owner not found\n
%s@%d: fCancelableBlock bailing out\n
result=failed reason=mkdir_failed
%s@%d: Unable to create subscribtion: %s\n
CCXPCService::startXPCService() Failed to start XPC service \n
CCXPCService::cancelActiveConnections cancelling %lu connections\n
CCConfigure::captureDirectoryCFDictionaryApplier Key: %s\n
CCDaemon IORegisterForSystemPower failed\n
Found blob timestamp: %s:%d %llu %llu.%llu\n
CCLogPipeInterface_dumpToDiskComplete
CCCacheDelete: no directories provided\n
CCDatabase::getStreamProperty: owner not found\n
%s@%d: fExitNextIteration bailing out\n
CCPcapngFormatter::writeLogFooter logMetaData is NULL\n
CCConfigure::applyConfiguration Configuration type is not dictionary\n
CCDaemon: CacheDelete disabled via boot-arg\n
CCOSSerializeWithIOReporterFormatter::processAllDictionarieswithinIncommingArray  didnt find or wrong type in array at i %ld\n
Incorrect number [numberOfDirArrayEntries: %lld, readIndex %lld] of directory entries. Skip sorting.\n
%s:%06u Unable to copy arguments
pruneDirectoryNDaysDo lstat failed on %s:\n%s\n
CCProfileMonitor::setStreamEventHandler Registered for notification callback.\n
CCDatabase::removePipe: pipe not found\n
CCDaemon::%s initial scan not complete, staying active
Found blob length: %s:%d %llu %zu\n
getting CC session id failed for entry:%u
CCDatabase::~CCDatabase: malloc failed for %zu bytes\n
CCDatabase::removeStreamProperty: pipe not found\n
%s@%d: bail - !hash\n
result=unexpected_event_type type=%s
CCLogFile::configureLogOptions Current Log Type:%d, File Size=%u, Max Number Of Files:%u\n
result=success profile=%s
%s:%d Owner:%s Name:%s entry:%u
%s:%06u: CFStringGetCString failure\n
CCPcapngFormatter::writeLogHeader logMetaData is NULL\n
result=xpc_error
result=failed reason=not_entitled
CCXPCService::handleIncomingMessage Unable to get remote connection\n
Got an XPC error: %s\n
%s Owner:%s Name:%s entry:%u\n
fileCount=%ld
CCLogFile::initWithRegistryEntry \n
CCFile::initWithTap Failed to get log directory \n
gzflush failed errno = %d, errnum = %d, reason : %s, %s\n
result=%s sourceSize=%lld destSize=%lld
seed build (or boot-arg) and device hasn't been unlocked since boot. Won't process event and continue when next event is posted entry:%u\n
result=success tap=released
CCProfileMonitor::profileCallback exiting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCProfileMonitor::setStreamEventHandler \n
CCPcapngFormatter::writeLog Unexpected log data \n
workingDir=%s saveDir=%s isDaemon=%s
getInstance result=%s
result=0x%x bytesRead=%llu
CCFile_captureLog
owner=%s pipe=%s level=%u
CCTextFormatter::buildLogIdentTable -- alloc failed\n
CCLogFile::initWithRegistryEntry: pthread_mutex_init failed\n
CCConfigure::captureDictionaryCFDictionaryApplier dirName: %s\n
cleanCaptureDirectories:Failed to malloc memory for valueArray
result=already_running
result=failed reason=already_called
CCDaemon::init Failed to create CCProfileMonitor\n
CCLogTap::isActive idle < duration, Owner:%s Name:%s entry:%u duration:%f\n
CCDatabase::findStream: pipe->streams is NULL\n
CCPcapngFormatter::writeLogHeader fStreamHeaderArray failed to write length %ld. %s\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_settype failed\n
CCFile::moveFile Failed to delete source file after copy: '%s', errno: %d\n
CCFile::captureLogRun Failed to stat file %s%s, errno: %d Owner:%s Pipe:%s\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  no key %s in dictionary\n
CCServiceMonitor::servicesPublished ignoring processing servicePublished due to isShutdownPending
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.\n
result=xpc_error error=%s
CCConfigure::pipePipeCFDictionaryApplier Pipe: %s\n
CCDaemon::getInstance isInitialized false
CCDaemon_DisablePowerNotification
CCPipeMonitor::%s:%d Release Tap i %zu
isActive:Failed to malloc memory for valueArray
result=no_taps
findTapWithOwnerAndPipe:no tap found
CCFile::mkdirRecursive Unable to mkdir on '%s', errno %d\n
CCDaemon:: Num of matching CCPipe %ld\n
CCIOReporterFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCProfileMonitor::profileCallback failed to get fMutex, exiting\n
CCProfileMonitor::profileCallback unchanged mask. previous state: %d, current state: %d\n
success=%s
CCDatabase::findOwner: ownerName is NULL\n
CCDaemon received power notification (0x%x) \n
CCFile::populateCommonTelemetryDictionary - Failed to get config from database for owner/pipe\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate Interface ID memory\n
CCLogFile::withRegistryEntry()\n
%s:%06u: Invalid type\n
CCConfigure::pipeConfigureCFDictionaryApplier Pipe: %s\n
result=shutdown_pending
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  rawData or interests not available\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  didnt find or not a dict in array\n
owner=%s pipe=%s
CCDataTap::isActive idle < duration  3 entry:%u duration:%f\n
result=failed reason=no_profile_loaded
CCDaemon will calling shutdown()\n
CCLogTap::%s invalid logPipeInterface\n
CCPipeMonitor::ccfree Exit - Destroyed lock\n
result=success configurationsApplied=%ld
CCDatabase::hasPipe: ownerName is NULL\n
ERROR: FileURL not created\n
CCPcapngFormatter::searchStreamIdInRegistry: Stream not found in database\n
CCLogFile_closeFile
CCFile_captureLogRun
result=both_null
CCXPCService::handleIncomingMessage XPC message is not dictionary\n
CCLogFile::deleteFile failed to delete: %s, errno: %d\n
CCLogFile::cleanupCapturedFiles log type is %d, current file is %s\n
CCFile::initWithTap Failed to create log directory  %s\n
Invalid argument @'%s':%06u
%s::%s failed to store description\n
CCIOReporterFormatter::writeLog Unexpected log data \n
CFDataGetBytePtr() failed
CCIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCXPCService::initWithConfigureAndPipeMonitor ERROR INIT MUTEX: %d\n
owner=%s pipe=%s nextFileIndex=%u logType=%d fileSize=%u
CCDaemon::getInstance failed with exception: %s
CCDaemon::init invalid arguments passed for non-daemon case\n
CCDataTap: Unable to create CCFile. entry:%u Owner:%s Name:%s\n
CCPipeMonitor_ServiceTerminated
forEachTapWithDirectory:Failed to malloc memory for keyArray
CCCacheDelete: purge notification enabled\n
CCDaemon::%s:%d unable to create class with protection flag\n
%s::%s shapeIOReportLibraryFriendlyDictionary failed\n
CCDaemon_QuiesceAll
CCLogPipeInterface_setConsoleLogFlags
CCPipeInterface::dispatch_source_create failed
CCProfileMonitor::profileCallback empty dictionary. fProfileLoaded %d fProfileRemoveApplied %d\n
CCProfileMonitor::setStreamEventHandler calling profileCallback(CCProfileChangeSourceXPCStream)\n
CCIOReportDumpQueue_SaveChannels
CCPcapngFormatter::writeLog  Inconsistent data (1) length=%lu\n
Unexpected event type %s\n
CCDaemon::setupDirectInstance failed with exception: %s
Found SessionName: %s:%d %llu %s\n
CCFile::initWithTap fLogDirPath is invalid\n
result=success profile=skipped
%s:%d %s::withRegistryEntry entry:%u Owner:%s Name:%s
CCLogFile::initWithConfig: Failed to initialize PCAP formatter\n
CCLogFile::deleteFile file already deleted: %s\n
Unknown type: %llu %s:%d\n
ERROR INIT MUTEX: %d\n
forEachTapWithDirectory:no tap found
findTapWithOwnerAndPipe:Failed to malloc memory for valueArray
CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n
Entitlement exists, and check is successful\n
Entitlement is NULL \n
CCOSSerializeWithIOReporterFormatter::writeLog CFDataGetBytePtr() failed
CCPipeInterface::%s:%d mach_msg SEND_MSG kr:%u entry:%u
result=success tapCount=%ld
CCCacheDelete: purge notification already enabled\n
%s::%s didn't find matching subscription\n
owner=%s pipe=%s profileLoaded=%d
%s:%d CCPipe::withOwnerNameCapacity Registry entry:%u Unsupported pipe type(%d)\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=rollover
CCDaemon::ccstart to create CCDaemon\n
CCDataTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
CCDataTap::profileRemoved, Owner: %s, Name: %s\n
CCDatabase::hasPipe: owner not found\n
CCDatabase::getStreamEntry: pipe not found\n
%s@%d: bail - !saveDir\n
CCLogFile::deleteFile successfully deleted: %s\n
CCConfigure::pipeConfigureCFDictionaryApplier Owner: %s\n
CoreCaptureStop called when no CCDaemon running, CCDaemon::isInitialized() returned false, ignoring
CCDaemon::%s Compression successful, deleting uncompressed file %s
%s:%06u Daily stackshot limit reached (%zu stackshots). Skipping stackshot for id %s (reason: %s)\n
CCDatabase::hasStream: owner not found\n
CCPcapngFormatter::writeFileHeader Uninitialized fDLTArray, i: %d\n
CCLogFile::initWithConfig: pthread_mutexattr_settype failed\n
pruneDirectoryOnOSUpgrade: activity enabled; failed to get osversion\n
owner=%s pipe=%s reason=prepareQuiescing
previous and current sequence numbers are same %u prev read offset %u,new read offset %u, previous write offset %u, new write offset %u, entry %u\n
CCDaemon::%s:%d dirPath is invalid\n
CCDatabase::findPipe: owner is NULL\n
CCDatabase::setPipeProperty: pipe not found\n
CCDatabase::getPipePropertyKeys: no properties in pipe\n
CCDatabase::getStreams: no streams in pipe\n
%s@%d: Problem merging channels\n
CoreCaptureStop failed with exception: %s
CCDaemon::runShutdownThread Exiting via xpc_transaction_try_exit_clean
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
Invalid State readOffset : %d, writeOffset : %d state %c, entry %u 
%s - STATE IS RESERVED. BREAK entry:%u
CCProfileMonitor::profileCallback during shutdown at %d\n
CCConfigure::pipeOwnerCFDictionaryApplier Owner: %s\n
message=0x%x
CCDaemon::init failed to create com.apple.corecaptured.serial_queue\n
CCDataFile::sendTelemetry failed
%s@%d: bail - !legend\n
owner=%s pipe=%s keyCount=%ld
result=cannot_acquire_lock
CCConfigure::applyConfiguration CCSTART key \n
CCPipeMonitor::ccfree - fails to unlock. Error[%d]\n
CCDaemon::%s:%d unable to allocate destination buffer\n
CCDataTap_withRegistryEntry
CCDatabase::addOwner: CFStringCreateCopy failed\n
CCPcapngFormatter::writeFileHeader: Missing pipeOwner or pipeName\n
CCPcapngFormatter::searchStreamIdInRegistry: Non-IORegistry pipe, querying CCDatabase for streamId=%u\n
owner=%s pipe=%s fileName=%s reason=%s
CCDataFile_openFile
%s:%d processEvent entry:%u Owner:%s Name:%s
CCPipeInterface::setNotificationPort(), mach_port_get_attributes failed kr[0x%08x]\n
CCIOReporterFormatter::getChannelsForSubscription  didn't find matching subscription\n
CCProfileMonitor::profileCallback Loaded\n
CCDatabase::getPipes: malloc failed for %zu bytes\n
CCDatabase::setPipeProperty: key is NULL\n
CCDaemon power notification disabled\n
CCOSSerializeWithIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
pruneDirectoryNDaysRead strtol EINVAL\n
%s::%s empty array\n
CCProfileMonitor::profileCallback changed. previous state: %d, current state: %d\n
CCProfileMonitor::setStreamEventHandler event received:%s\n
%s:%d registry entry:%u
CCDatabase::getPipes: no pipes in owner\n
CCConfigure::pipeConfigureCFDictionaryApplier notify timeout\n
CCDataPipeInterface_profileRemoved
%s::%s Failed to create IOReporter library friendly channel list\n
CCProfileMonitor::freeResources Entered\n
CCProfileMonitor_ProfileCallback
CCDatabase::removeStream: ownerName is NULL\n
CCXPCService_HandleConnectionEvent
result=not_enabled
CCDaemon_initWithOptions
result=failed reason=memory_allocation_failed
CCFile::moveFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCFile_moveFile
CCLogTap::tapLoop(), Error setting notification port rc[0x%08x]\n
CCDataTap::tapLoop(), Error setting notification port rc[0x%08x]\n
CCFile::copyFile: Unable to stat source path errno %d, reason %s\n
CCLogTap::isActive tap is busy, Owner:%s Name:%s entry:%u\n
can reduce logging: %d\n
CCLogFile::withConfig() Invalid log type %d\n
%s:%d processEvent for entry:%u Owner:%s Name:%s
CCFile::copyFile Wrote '%s' source length: %lld archive length: %lld (reason: %s) Owner:%s Pipe:%s\n
CCLogPipeInterface_unmapPipe
CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe entry:%u Owner:%s Pipe:%s\n
CCPipeMonitor::ccfree Failed to acquire lock\n
result=tap_not_found
CCCacheDelete: cannot register for purge notifications ret=0x%x\n
result=retain_plist2
CCConfigure::pipeConfigureCFDictionaryApplier pipe policy\n
CCLogTap::setConsoleLogLevel Owner:%s Name:%s entry:%u\n
CCPipeMonitor_CleanCaptureDirectories
IOReportCreateSamplesRaw() returned 0 sized dictionary
CCDatabase::findStream: pipe is NULL\n
CCLogFile::initWithConfig: Failed to create working directory string\n
CCLogFile::initWithConfig: Failed to create log directory path\n
CCLogFile::configureLogOptions Configuration is %s\n
result=shutdown_triggered
Failed to get fCaptureDirPath for purgeable marking\n
CCLogPipeInterface_capture
CCPipeInterface::initWithRegistryEntry entry:%u fConnectRef(%u)\n
CCCacheDelete: purge history lost, rescan needed\n
CCDatabase::addPipe: failed to find/create owner\n
CCDatabase::hasPipe: pipeName is NULL\n
CCDatabase::addStream: streamName is NULL\n
CCDaemon::init Failed to create timer dispatch source\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
CCOSSerializeWithIOReporterFormatter::writeLog unsupported root type for JSON Serialization
CCFile::captureLogRun moving files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u, Owner:%s
CCLogTap::setConsoleLogFlags Owner:%s Name:%s entry:%u\n
CCLogTap::profileRemoved, Owner:%s Name:%s entry:%u\n
pruneDirectoryOnOSUpgrade: activity disabled\n
CCLogPipeInterface_profileRemoved
IOConnectCallAsyncStructMethod FAILED CCPipeInterface::%s::%d fNotificationPortIsSet:%d entry:%u kr[0x%08x]
%s NULL value.\n
%s:%06u Configuration type is not dictionary\n
CCDatabase::setStreamProperty: key is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to convert stream name\n
CCLogFile_sendTelemetry
CCLogFile::sendTelemetry analytics_send_event_lazy weak link import failed
owner=%s pipe=%s fileName=%s fileSize=%ld
result=success tapCount=%zu
CCXPCService::handleIncomingMessage Key is %s\n
result=profile_active
CCFile::captureLog Received Capture notice id: %d.%06d, reason = %s\n
CCDaemon::%s Compressed '%s%s' -> %lld bytes
%s::%s channelStreamArray at i %ld not valid\n
CCProfileMonitor::profileCallback read WiFi profile plist valid: %d mask: %d\n
CCDatabase::addPipe: ownerName is NULL\n
CCDatabase::getStreamPropertyKeys: entry->properties is NULL\n
CCConfigure::pipeConfigureCFDictionaryApplier Key: %s\n
CCConfigure::notifyTimeout notifyTimeout: %u\n
CCFile::withRegistryEntry() entered entry:%u\n
%s:%06u Stackshot rate limit: a stackshot was triggered within the last %d seconds. Skipping stackshot for id %s (reason: %s)\n
CCDatabase::removeStream: owner not found\n
CCXPCService_StartXPCService
result=failed
CCDaemon::%s monitor NOT active, shutdown
CCDaemon::init CoreCaptureStart was already called\n
result=failed reason=formatter_creation_failed
CCIOReporterFormatter::addRegistryChildToChannelDictionary  not array\n
CCDatabase::getPipeConfig: owner not found\n
CCDatabase::getStreamConfig: stream not found\n
%s@%d: bail - !filePath\n
CCConfigure::configure keycount : %ld\n
CCLogTap::updateLogFlags\n
CCPipeInterface::%s::%d fNotificationPortIsSet:%d rc:%d entry:%u
%s Tap Found tap with Owner:%s Name:%s\n
CCPipeMonitor_ProfileLoaded
profileLoaded:Failed to malloc memory for keyArray
CCPipeMonitor_ResumeAllTaps
%s::%s not a matching Stream id\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj %s is NULL, with type %ld, but has type %ld\n
(CCLogTap) CFNumberGetValue failed for LogPolicy\n
deleteDirectory: deleting '%s' reason: %s
CCOwnerEntry::~CCOwnerEntry: malloc failed for %zu bytes\n
CCDatabase::removeStream: pipeName is NULL\n
CCXPCService::handleIncomingMessage release, incomingConnection\n
CCLogFile_closeMMAP
CCLogFile::initWithConfig: Failed to create directory/file name strings\n
CCFile::copyFile Unable to stat dest path '%s' errno: %d reason: %s prevErr: %s\n
CCDataTap::capture, Owner: %s, Name: %s\n
CCLogTap::%s:%d cast failed\n
Notification to dump to disk failed for entry:%u
quiesceAllTaps:Failed to malloc memory for valueArray
CCCacheDelete: purge history processing complete\n
result=success state=%d
CCPcapngFormatter::searchStreamIdInRegistry: Found %ld streams in database\n
result=0x%x
Received Skip Event %u\n
result=timeout tapCount=%ld notQuiescedTap=%ld
%s:%06u invalid configuration\n
CCXPCService::handleIncomingMessage No %s is received\n
result=connection_established
result=failed reason=mutex_init_failed error=%d
owner=%s pipe=%s fileName=%s fileSize=%ld logEvents=%u
CoreCaptureStart called when CCDaemon already running, returning existing instance
CCLogPipeInterface_setLogFlags
CCLogTap::setPolicy, Owner:%s Name:%s entry:%u\n
CCDaemon::%s:%d fileName is invalid\n
CCLogFile::sendTelemetry failed
result=failed reason=file_creation_failed
CCConfigure::capture capture reason can not be NULL\n
CCLogTap::isActive policy is %d, Owner:%s Name:%s entry:%u\n
CCPipeMonitor::%s:%d Tap corresponding to Pipe not found
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCIOReporterFormatter::writeLog  Inconsistent data (1) length=%lu\n
CCProfileMonitor::applyProfile owner:%s, pipe:%s\n
CCDatabase::setStreamProperty: stream not found\n
CCDatabase::reset: malloc failed for %zu bytes\n
CCOSSerializeFormatter::writeLog unsupported root type for JSON Serialization
CoreCaptureStop called when isShutdownPending true, ignoring
CCDataFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCPipeInterface_setNotificationPort
CCFile::captureLogRun Skipping current file Dir file %s, Current File %s Owner:%s Pipe:%s\n
result=failed reason=property_creation_failed
CCDatabase::setStreamProperty: pipe not found\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream name memory\n
CCDaemon received system wake or will not sleep (0x%x), all cctap resumed from quiesced state\n
result=%s fileD=%d
CCDataPipeInterface_queryMetaData
quiesceAllTaps:no tap found
CCCacheDelete: cannot create monitored directories\n
%s:%06u Invalid reason
%s::%s didn't find or wrong type in array at i %ld\n
CCProfileMonitor::profileCallback getting owners from profile failed
CCDataTap::initWithRegistryEntry invalid fPipeInterface\n
CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next. entry:%u Owner:%s Name:%s\n
result=failed reason=directory_creation_failed
CCDaemon::%s:%d unable to allocate source buffer\n
CCDatabase::removePipeProperty: property key not found\n
CCDatabase::getPipePropertyKeys: owner not found\n
CCXPCService::handleIncomingMessage empty configuration\n
Entitlement query did not succeed \n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
Created a bad offset, don't save it! newOffset %u, payload length %u, padding %u,sizeof metadata %lu, STATE %c, entry:%u
CCPipeMonitor::CCPipeMonitor Failed to create pipe dictionary.\n
%s::%s Can't create channelStreamDictionary\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCIOReporterFormatter::writeLog  Insufficient length=%lu to hold IOReporterHeader_t\n
CCProfileMonitor::applyConfiguration  shutdown pending, dropping request and exiting\n
CCConfigure::captureDirectoryCFDictionaryApplier capture\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is %s NULL, with type %ld, but has type %ld\n
CCDataTap::%s:%d cast failed\n
profileRemoved:no tap found
%s Unexpected CF object type ID. Expected (%lu), have (%lu) \n
result=success finalProfileLoaded=%d keyCount=%ld
CCDatabase::getPipePropertyKeys: malloc failed for %zu bytes\n
CCDatabase::removeStream: streamName is NULL\n
CCDaemon::runShutdownThread Failed to exit cleanly after %d attempts, forcing exit
owner=%s pipe=%s entry=%u
resumeAllTapsFromQuiesced:Failed to malloc memory for keyArray
CCProfileMonitor::profileRemoved Entered %d\n
CCTap::%s:%d entry:%u
CCDatabase::removeStreamProperty: property key not found\n
result=failed reason=xpc_service_creation_failed
CCLogFile::initWithConfig: Failed to create log directory\n
CCOSSerializeFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCDaemon::enablePurgeNotification failed to create CFString for other save location\n
CCDataTap::%s invalid dataPipeInterface\n
CCFile::captureLog Failed to create directory %s (reason: %s)\n
CCPipeInterface::withRegistryEntry Unsupported pipe type(%d) \n
CCPipeInterface::setDispatchQueue re-targeted notification port to continuous queue entry:%u Owner:%s Pipe:%s\n
CCDaemon::%s Failed to delete file %s errno: %d
CCIOReportDumpQueue_DoSaveChannels
CCPipeInterface::%s:%d rcvd terminate msg:0x%x entry:%u
pruneDirectoryNDaysRead cap %ld\n
CCProfileMonitor::profileRemoved Exited :%d\n
CCOwnerEntry operator=: malloc failed for %zu bytes\n
CCDatabase::getOwners: no owners in database\n
CCPcapngFormatter::writeFileHeader: Non-IORegistry pipe - owner=%s, name=%s\n
CCLogFile::initWithConfig: Invalid arguments\n
CCLogFile_openFile
result=xpc_active
CCFile::captureLog Capture(%s) is in progress. Ignoring new one.\n
CCLogTap::%s:%d tapLoopImpl entry:%u Owner:%s Name:%s\n
CCPipeInterface::setNotificationPort(), mach_port_insert_right failed kr[0x%08x]\n
result=failed reason=no_keys
CCPcapngFormatter::buildStreamToInterfaceTable: Found %ld streams in database\n
Stream Name is %s\n
CCXPCService::handleIncomingMessage shutdown pending true, dropping message and exiting\n
newInstance result=%s
CCDataTap::processEvent quiesce pending entry:%u Owner:%s Name:%s\n
CCLogTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
%s::%s didn't find %s or wrong type in array at i %ld\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find %s\n
result=success mergedKeys=%ld
CCDatabase::addStream: CFStringCreateCopy failed\n
Error creating plist...\n
CoreCaptureStop setShutdownAlreadyTrue, exiting without doing anything
CCDaemon power notification enabled\n
Invalid Meta Key. Bail.
CCFile::moveFile failed: %s file: '%s' Owner:%s Pipe:%s\n
CCLogPipeInterface_profileLoaded
forEachTapWithDirectory:Failed to malloc memory for valueArray
profileLoaded:Failed to malloc memory for valueArray
CCProfileMonitor::initWithConfigure ERROR INIT MUTEX: %d\n
CCFile::withTap Unsupported file type(%d) \n
CCLogPipeInterface_setNotifyTimeout
CCPipeMonitor::%s:%d Tap corresponding to terminated Pipe not found Owner:%s Name:%s entry:%u
CCFile::writeMetadataFiles failed malloc\n
CCProfileMonitor::profileCallback no profile installed. previous state: %d, current state: %d\n
CCProfileMonitor::setStreamEventHandler Unable to get notification center for configuration reader.
CCProfileMonitor::applyConfiguration profile is already removed
CCPcapngFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCConfigure::pipeConfigureCFDictionaryApplier Configure Log Options\n
CCDataPipeInterface_capture
CCFile::initWithTap Failed to create formatter\n
CCFile::captureLog\n
gzflush error code = %d\n
CCPipeInterface::resetDispatchQueue re-targeted dispatch source to capture queue entry:%u Owner:%s Pipe:%s\n
fMutexCleanDirectories not acquired, bail out\n
result=failed reason=tap_creation_failed
result=not_initialized
CCDaemon::init failed to create com.apple.corecaptured.background_queue\n
CCDataFile_closeFile
CCFile::generateCaptureDirPath failed malloc\n
CCPipeInterface::IOServiceClose entry:%u fConnectRef(%d)\n
CCPipeInterface::%s:%d rcvd terminate signal entry:%u
profileRemoved:Failed to malloc memory for valueArray
%s::%s key %s has wrong type in dictionary\n
CCDataTap::processEvent already quiesced entry:%u Owner:%s Name:%s\n
CCLogTap::setNotifyTimeout\n
%s::%s streams %ld\n
CCPipeEntry operator=: malloc failed for %zu bytes\n
%s@%d: Unable to create samples: %s\n
CCXPCService::handleIncomingMessage Unable to allocate scratch buffer\n
CCLogFile::initWithConfig: Failed to create formatter\n
result=init_scan_pending
CCDataFile_sendTelemetry
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
CCLogTap::tapLoop entry:%u Owner:%s Name:%s Exiting taploop\n
owner=%s pipe=%s streamName=%s flagName=%s
%s:%d Owner:%s skipping profileLoaded
CCProfileMonitor::profileCallback Entered source:%d token:%d\n
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d)\n
CCServiceMonitor::ccfree()\n
cleanCaptureDirectories:Failed to malloc memory for keyArray
CCDaemon::%s:%d fileName is invalid
%s::%s channelStreamArray empty\n
CCDatabase::getPipes: owner not found\n
CCDatabase::addStream: owner not found\n
CCDatabase::hasStream: pipeName is NULL\n
CCDatabase::getStreamPropertyKeys: owner not found\n
CCDaemon_EnablePowerNotification
CCFile::copyFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCLogPipeInterface_setPolicy
CCDatabase::removeOwner: ownerName is NULL\n
CCDatabase::hasStream: streamName is NULL\n
CCDatabase::getStreamPropertyKeys: malloc failed for %zu bytes\n
CCPcapngFormatter::writeFileHeader: Failed to cast fWriteObject to CCFile\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d phase=fileWillClose
owner=%s pipe=%s fileName=%s doCompress=%d
forEachTapWithOwnerAndPipe:Failed to malloc memory for valueArray
CCDaemon::%s:%d Trying to compress file %s%s\n
%s::%s channelStreamArray not valid\n
CCPipeEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::removeOwner: owner not found\n
CCDatabase::removeStream: pipe not found\n
CCPcapngFormatter::writeLog Failed to write(2) Length=%lu, tempLength=%lu\n
owner=%s pipe=%s registryEntry=%u
CCPipeInterface::initWithRegistryEntry [pipeOwner: %s, pipeName: %s] Failed to initialize returned %x\n
CCDaemon::%s:%d failed to open dest buffer %s\n
CCDatabase::getStreams: malloc failed for %zu bytes\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe, querying database\n
CCPcapngFormatter::buildStreamToInterfaceTable: Found stream header (%ld bytes) for stream\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream[%u]: name=%s, id=%u, dlt=%u\n
configure=%p pipeMonitor=%p
CCDataPipeInterface_profileLoaded
CCDatabase::getPipes: owner->pipes is NULL\n
CCDatabase::removePipeProperty: pipe not found\n
CCXPCService_InitWithConfigureAndPipeMonitor
CoreCaptureStart: ENTRY - workingDir=%p, saveDir=%p, isCCDaemon=%d, isInitialized=%d\n
fileCount=%ld timeTaken=%f
resumeAllTapsFromQuiesced:no tap found
CCCacheDelete: failed to create dispatch queue\n
CCDaemon::%s unable to stat compressed file '%s'
%s::%s rawStreamAndSubscriptionArray not valid\n
CCDatabase::removeStreamProperty: stream not found\n
CCIOReportDumpQueue::_processorThread bail - !keysTypeRef\n
CCDataTap::tapLoopImpl exit entry:%u Owner:%s Name:%s Exiting taploop\n
CCFile::copyFile failed: %s file: '%s' Owner:%s Pipe:%s\n
Couldn't update read ptr.\n
profileRemoved:Failed to malloc memory for keyArray
%s:%06u failed to allocate memory\n
CCConfig is %s\n
CCLogFile_buildFileTables
CCLogFile_addFile
CCFile::initWithTap create with cstring failed\n
CCFile::initWithTap memory allocation failed\n
%s CANNOT FIND tap with Owner:%s Name:%s\n
pruneDirectoryOnOSUpgrade: activity enabled; snapshot %s, osversion %s\n
CCPipeInterface_wakeupTapLoop
CCDatabase::findStream: streamName is NULL\n
CCDatabase::getPipePropertyKeys: entry->properties is NULL\n
CCDatabase::addStream: pipe not found\n
CCDaemon::init Failed to create CCPipeMonitor\n
CCLogPipeInterface_mapPipe
CCLogFile::initWithConfig: buildFileTables failed\n
owner=%s pipe=%s fileName=%s offset=%zu length=%zu fileDesc=%d
CCFile::copyFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
%s - STATE IS EMPTY. CONTINUE entry:%u
isActive:Failed to malloc memory for keyArray
%s::%s  didn't find or wrong type in dict at i %ld for %s\n
%s:%06u unable to create set\n
CCDatabase::getStreams: owner not found\n
CCDatabase::getStreamConfig: owner not found\n
CCDaemon::setupDirectInstance success
CCDaemon::init Failed to initialize mutex\n
CCFile::captureLogRun() Exiting CCFile::captureLogRun (reason: %s) Owner:%s Pipe:%s\n
CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n
findTapWithOwnerAndPipe:Failed to malloc memory for keyArray
CCCacheDelete: file purged: %s (inode: %llu)\n
result=not_dictionary_types
CCXPCService::handleIncomingMessage Unable to allocate config data\n
CCConfigure::pipeConfigureCFDictionaryApplier watermark level to notify\n
result=failed reason=IORegisterForSystemPower_failed
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  contains %s %d contains %s %d\n
CCFile::mkpath fails to create path '%s' as '%s' is not a directory\n
filesSaved=%ld
CCLogFile::initWithRegistryEntry Number of files can not be 0.\n
CCFile::writeDataFiles memory allocation failed (reason: %s)\n
CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback to check for installed profiles\n
CCLogFile::initWithConfig: Successfully initialized for non-IORegistry pipe\n
result=failed reason=device_locked
CoreCapture_Stop
owner=%s pipe=%s fileName=%s captureId=%u.%06u reason=%s logSize=%zu
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe missing owner or name\n
CCLogTap::freeResources() entry:%u failed to unmap pipe with rc[0x%08x]\n
CCPipeMonitor::ccfree - fails to destroy fMutex lock. Error[%d]\n
CCCacheDelete: purge notification disabled\n
%s:%06u Triggering stackshot with id %s due to %s\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  Cant create channelStreamDictionary\n
CCDataTap::profileLoaded, Owner: %s, Name: %s\n
CCLogTap::setLogLevel Owner:%s Name:%s entry:%u\n
CCLogTap::profileLoaded, Owner:%s Name:%s\n
CCProfileMonitor::profileCallback starting states -> source %d fProfileToken %d isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n
result=failed reason=profile_removed
CCDatabase::getOwners: malloc failed for %zu bytes\n
result=failed reason=null_saveDir
CCXPCService_HandleIncomingMessage
CCDataFile::open Failed to create %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCFile::moveFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
result=duplicate
%s:%06u: opendir failure - %s\n
getHwModel %s\n
CCPcapngFormatter::writeFileHeader Uninitialized fStreamNameArray, i: %d\n
CCDatabase::removePipe: pipeName is NULL\n
ERROR INIT COND: %d\n
CCLogFile::withConfig() Invalid parameters\n
CCConfigure::watermarkLevel watermarkLevel: %u\n
CCDaemon:: No name matching CCPipe service found \n
CCLogTap_initWithRegistryEntry
result=retain_plist1
CCDatabase::hasStream: pipe not found\n
%s@%d: bail - !mkdirRecursive\n
result=failed reason=working_directory_creation_failed
CCFile_copyFile
(CCLogTap) IORegistryEntryCreateCFProperty failed for LogPolicy\n
CCPipeInterface::resetDispatchQueue re-targeted notification port to capture queue entry:%u Owner:%s Pipe:%s\n
CCDatabase::getPipeProperty: pipe not found\n
CCDatabase::removePipeProperty: owner not found\n
CCXPCService: logging command received but not supported on this platform\n
CCLogFile::initWithConfig: Unsupported log data type %d\n
CCConfigure::applyConfiguration CCSTOP key  \n
CCDaemon received system shutdown notification, all cctap quiesced\n
Found session timestamp: %s:%d %llu %llu.%llu\n
CCDataTap::isActive tap is fBusy Active 2 entry:%u\n
CCPipeMonitor::cleanCaptureDirectories - fails to unlock\n
%s Tap Find Tap with Owner:%s Name:%s\n
%s::%s didn't find or not a dict in array\n
CCProfileMonitor_MergeProfilePlist
%s Read Ptr is not multiple of %lu (%d) entry:%u \n
%s:%06u Invalid captureId
%s:%06u unable to allocate dictionary\n
CCDatabase::removePipe: owner not found\n
CCDatabase::addStream: ownerName is NULL\n
CCDatabase::getStreamProperty: entry->properties is NULL\n
result=failed reason=filePath_failed
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe initialized with %u total interfaces\n
CCDaemon::enablePurgeNotification failed to create CFString for save location\n
CCLogTap::capture, Owner:%s Name:%s\n
quiesceAllTaps:Failed to malloc memory for keyArray
CCDatabase::hasOwner: ownerName is NULL\n
CCDatabase::getStreamPropertyKeys: pipe not found\n
%s@%d: bail - !allChannels\n
CCPcapngFormatter:: failed to get stream id\n
CCLogFile::addFile: No log before device first unlocked for PROTECTION_CLASS_C\n
CCConfigure::policy policy: %u\n
CCDatabase::findOwner: database is NULL\n
event_type=%s
%s:%06u: Failed reading '%s' from registry\n
CCPipeInterface::setDispatchQueue entry:%u Owner:%s Pipe:%s\n
Unable to initialize logging subsystem for corecapture
%s::%s didn't find %s\n
CCIOReporterFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCPcapngFormatter::writeFileHeader: Empty pipeOwner or pipeName string\n
CCPcapngFormatter::buildStreamToInterfaceTable numberofStreams : %d\n
CCConfigure::configure key is %s\n
CCConfigure::captureDirectoryCFDictionaryApplier Owner: %s\n
owner=%s pipe=%s fileName=%s
Found blob name: %s:%d %llu %s\n
result=failed reason=values_alloc_failed
CCServiceMonitor::scanServices fMatching Dictionary Retain count(2) is %ld\n
CCDatabase::getStreamPropertyKeys: no properties in stream\n
previous and current sequence numbers are same %u prev read offset %u,previous write offset %u, new write offset %u, entry %u\n
CCLogTap::updateConsoleLogFlags Owner:%s Name:%s entry:%u\n
CCPipeMonitor::CCPipeMonitor Failed to initialize mutex\n
CCPipeMonitor_QuiesceAllTaps
CCDaemon::%s Failed to compress '%s%s'
CCIOReporterFormatter::addRegistryChildToChannelDictionary  no %s found in %s\n
CCLogTap_withRegistryEntry
CCLogFile::initWithConfig: pthread_mutex_init failed\n
CCDaemon_shutdown
CCIOReporterFormatter::getChannelsForStreamAndSubscription  Couldnt find %s\n
previousProfileLoaded=%d
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
%s Read pointer moved while copying metadata. Retrying entry:%u\n
CCPipeMonitor_ServicePublished
result=failed reason=malloc_failed
Error: %s
CoreCaptureStart called with bad args, crashing
result=0x%x ringSize=%llu
CCLogTap::setLogFlags Owner:%s Name:%s entry:%u\n
CCPipeEntry::~CCPipeEntry: malloc failed for %zu bytes\n
CCDatabase::addStream: pipeName is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable: Missing owner or pipe name\n
CCConfigure::pipeConfigureCFDictionaryApplier capture\n
CCLogPipeInterface_setWatermarkLevel
%s Duplicate Owner:%s Name:%s entry:%u\n
connection=%p type=%s
CCLogFile::withConfig()\n
CCDataFile_openCaptureFile
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  failed to duplicate dictionary\n
Session Name: %s, Blob Name: %s %llu.%llu Owner:%s Name:%s\n
CCFile_initWithRegistryEntry
CCLogTap::withRegistryEntry failed\n
CCLogPipeInterface_updateLogFlags
CCDaemon::%s:%d fileName %s is already compressed...\n
CCProfileMonitor::profileCallback read BT profile plist valid: %d mask: %d\n
result=already_set
result=%s
CCPipeMonitor::CCPipeMonitor Failed to initialize fMutex\n
CCDatabase::getStreamProperty: pipe not found\n
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get stream entry for stream %ld\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.
CCLogFile::buildFileTables fNumberOfArrayEntries is zero\n
CCFile::captureLogRun copying files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
CCFile::isLogdirExists Failed to create  %s\n
max_preserved_captures
CCIOReporterFormatter::addRegistryChildToChannelDictionary  Cant create channelStreamDictionary\n
CCLogFile::initWithConfig: buildFileTables failed\n
CCFile::initWithTap Failed to get log directory \n
marconi-wifi
CCDataFile::sendTelemetry failed
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
Failed to get fCaptureDirPath for purgeable marking\n
CCLogTap::isActive tap is busy, Owner:%s Name:%s entry:%u\n
/System/Library/Extensions/corecapture.kext/Contents/version.plist
CCDaemon::%s initial scan not complete, staying active
CCIOReportInterests
CCProfileMonitor::getOwnersFromPipesAndStreams
CCDatabase::reset: malloc failed for %zu bytes\n
/
DriverID
CCPipeMonitor::isActive: recent serviceTerminated, staying active\n
%s Tap Found tap with Owner:%s Name:%s\n
CCProfileMonitor::sendProfileChangeNotification profile change notification received\n
CCLogFile::writeLog - File roll needed\n
CCDaemon::init failed to create com.apple.corecaptured.serial_queue\n
getHwModel %s\n
%s::%s  didn't find or wrong type in dict at i %ld for %s\n
CCLogFile::deleteFile file already deleted: %s\n
CCDaemon power notification disabled\n
Failed to mark %s as purgeable %d (%s) (flags 0x%llx)\n
mergeProfilePlist
Unable to create IOReport Aggregate\n
CCConfigure::policy
activityCheck
%s::%s clearing out any previous subscriptions\n
CCConfigure::findTapWithOwnerAndPipe found CCTap, Owner: %s, Pipe: %s\n
OSSerializeWithIOReporter
CCDaemon::%s:%d failed to open source buffer %s\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream header bytes: %s\n
%s:%d processEvent for entry:%u Owner:%s Name:%s
wb
CCProfileMonitor
%s:%d registry entry:%u
withRegistryEntry
XPC_TYPE_ARRAY
CCLogFile::initWithRegistryEntry \n
CCFile::initWithTap create with cstring failed\n
MaxFileSize
rename_failed
CCPipeMonitor::ccfree Entered\n
forEachTapWithOwnerAndPipe
%s::%s channelStreamArray empty\n
unknown
Couldn't update read ptr.\n
resumeAllTapsFromQuiesced:Failed to malloc memory for keyArray
%s@%d: bail - !filePath\n
MiscInfo
XPC_TYPE_DICTIONARY
CCConfigure::setLevel
CCCacheDelete: purge history lost, rescan needed\n
Unknown
CCIOReporterFormatter::getChannelsForStreamAndSubscription  key %s has wrong type in dictionary\n
no_keys
CCDaemon::init Failed to create CCPipeMonitor\n
Invalid Meta Key. Bail.
CCLogTap::freeResources() entry:%u failed to unmap pipe with rc[0x%08x]\n
ProductType
CCOwnerEntry operator=: malloc failed for cleanup, %zu bytes\n
CCDatabase::removeStream: pipeName is NULL\n
CCDatabase::getStreamPropertyKeys: no properties in stream\n
CCIOReportRdata
CCDaemon::%s:%d fileName is invalid
CCProfileMonitor::withPipeMonitor Failed to create CCProlieMonitor\n
CaptureReason
%s::%s failed to store description\n
CCPcapngFormatter::buildStreamToInterfaceTable: Stream[%u]: name=%s, id=%u, dlt=%u\n
%u.%06u
CCStop
IOReportSubGroupName
\nIncident Identifier:     %@\nCrashReporter Key:       %@\nHardware Model:          %@\nProcess:                 WiFi Firmware\nPath:                    NA\nIdentifier:              WiFi Firmware Trap\nVersion:                 NA\nCode Typ
CCDaemon::%s Compression successful, deleting uncompressed file %s
freeResources
CCPcapngFormatter::writeFileHeader Uninitialized fDLTArray, i: %d\n
CCDataTap::profileLoaded, Owner: %s, Name: %s\n
Raw
CCPipeMonitor::ccfree - fails to destroy fMutex lock. Error[%d]\n
pruneDirectoryOnOSUpgrade: activity enabled; snapshot %s, osversion %s\n
prune_dir_days
CCIOReporterFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
processEvent
CCConfigure::configure key is %s\n
LogFileSize
pruneDirectoryOnOSUpgrade: activity enabled; failed to get osversion\n
getOwnersFromProfile
shutdown_pending
CCDatabase::removePipe: owner not found\n
CCLogTap::%s invalid logPipeInterface\n
previous and current sequence numbers are same %u prev read offset %u,new read offset %u, previous write offset %u, new write offset %u, entry %u\n
boot-args
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj %s is NULL, with type %ld, but has type %ld\n
CCPipeMonitor
CCProfileMonitor::profileCallback Entered source:%d token:%d\n
CCLogFile::initWithConfig: CFNumberCreate failed for pipeType\n
CCLogTap::isActive policy is %d, Owner:%s Name:%s entry:%u\n
CCXPCService
CCLogFile::initWithConfig: Successfully initialized for non-IORegistry pipe\n
%s::%s didn't find matching subscription\n
file:///private/var/Managed%20Preferences/mobile/com.apple.corecapture.configure.bt.plist
Got an XPC error: %s\n
CCDataTap: Unable to create CCFile. entry:%u Owner:%s Name:%s\n
CCDaemon::%s:%d Error reading from source buffer %s\n
%s@%d: bail - !allChannels\n
/IOReporters.%s
MaxNumberOfFiles
*
CCOSSerializeFormatter::writeLog unsupported root type for JSON Serialization
CCDaemon::%s monitor NOT active, shutdown
getting CC session id failed for entry:%u
CCServiceMonitor::ccfree()\n
com.apple.corecaptured.cachedelete
can reduce logging: %d\n
pruneDirectoryNDaysRead cap %ld\n
Policy
LogPolicy
CCCacheDelete: file purged: %s (inode: %llu)\n
CCDatabase::removePipeProperty: property key not found\n
CCProfileMonitor::profileCallback failed to get fMutex, exiting\n
CCDatabase::getStreams: owner not found\n
CCDatabase::setStreamProperty: pipe not found\n
CCPcapngFormatter::writeLogFooter logMetaData is NULL\n
CCIOReportRkey
Error: %s
%s::%s not a matching Stream id\n
CCIOReporterFormatter::writeLog  Can't copy rawData\n
com.apple.notifyd.matching
CCDatabase::removeStreamProperty: pipe not found\n
ERROR: FileURL not created\n
Received Skip Event %u\n
Carrier
%s::%s didn't find %s\n
 NOT
CCDaemonProfile Changed
CCDatabase::getPipeConfig: pipe not found\n
CCPcapngFormatter::writeLogHeader fStreamHeaderArray failed to write length %ld. %s\n
CCLogFile::initWithConfig: Unsupported log data type %d\n
CCDaemon::startPipeMonitor CCDaemon not yet initialized, exiting
txt
0x%016x
CCLogFile::configureLogOptions Configured Log Type:%d, File Size=%u, Max Number Of Files:%u\n
NotifyTimeout
deleteDirectory
CCDatabase::getStreams: no streams in pipe\n
CCDaemon::init CoreCaptureStart was already called\n
CCLogTap::capture, Owner:%s Name:%s\n
no_config_string
XPC_TYPE_UUID
CCPipeInterface::setDispatchQueue re-targeted dispatch source to continuous queue entry:%u Owner:%s Pipe:%s\n
profileRemoved:Failed to malloc memory for keyArray
%s@%d: Will write to: %s\n
CCPcapngFormatter::writeFileHeader: Empty pipeOwner or pipeName string\n
LogEvents
CCDaemon received system shutdown notification, all cctap quiesced\n
IOReporter
%s:%d Owner:%s Name:%s entry:%u
DYLD_IMAGE_SUFFIX
%s NULL value.\n
/private/var/tmp/com.apple.corecaptured/com.apple.bluetooth.logging.plist
CCDatabase::addPipe: ownerName is NULL\n
profile_removed_notification
tick-frequency
CCProfileMonitor::getOwnersFromCCConfig
%s::%s rawStreamAndSubscriptionArray not valid\n
CCLogFile::initWithRegistryEntry: pthread_mutex_init failed\n
CCDaemon::sendProfileChangeNotification profile change notification received\n
CCFile::generateCaptureDirPath failed malloc\n
Unexpected log parameters ring state3(0x%llx), ring buffer(0x%llx), ring size(%llu), logSize(%lu), logContinueSize(%lu) entry:%u\n
CCDaemon::%s:%d unable to allocate source buffer\n
CCDatabase::getPipes: owner->pipes is NULL\n
CCDaemon::%s:%d Trying to compress file %s%s\n
CCDaemon::%s Failed to compress '%s%s'
ReleaseType
%s Ring offset out of range: %u > %llu entry:%u\n
CCPipeMonitor::ccfree Exit - Destroyed lock\n
CCDaemon::Not all taps got quiesced, tap %ld was not ready
rb
CCFormatter::withLogType Unsupported log data type(%d) \n
CCDaemon::%s:%d filePath may get truncated. Returning...
CoreCaptureStop called when no CCDaemon running, CCDaemon::isInitialized() returned false, ignoring
CCCacheDelete: purge notification enabled\n
CCDaemon::%s:%d dirPath is invalid
%s/%s
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCLogFile::initWithConfig: Invalid arguments\n
CCDataTap::processEvent already quiesced entry:%u Owner:%s Name:%s\n
CCDaemon::%s:%d unable to create class with protection flag\n
%s::%s Can't create subscriptionLegendDictionary\n
IOService
CCTerminate
com.apple.corecaptured.CCIOReportDumpQueue
XPC_TYPE_DATE
CCLogFile::deleteFile failed to delete: %s, errno: %d\n
createDictionaryWithProcessedIOReporter
source_read_failed
CCPipeMonitor::CCPipeMonitor Failed to create pipe dictionary.\n
CCIOReporterFormatter::writeLog Unexpected log data \n
%s@%d: Problem merging channels\n
empty_configuration
CCDatabase::findOwner: database is NULL\n
CCDatabase::getStreamPropertyKeys: malloc failed for %zu bytes\n
CCConfig
dest_open_failed
dest_write_failed
WiFiFWTrap
%s:%06u: Failed getting number\n
CCDataTap::capture, Owner: %s, Name: %s\n
%s - STATE IS EMPTY. CONTINUE entry:%u
pruneDirectoryOnOSUpgrade: upgraded from %s to %s
CCLogEnable
CCConfigure::notifyTimeout notifyTimeout: %u\n
CCOSSerializeFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCOSSerializeWithIOReporterFormatter::writeLog CFDataGetBytePtr() failed
%s Read pointer moved while copying metadata. Retrying entry:%u\n
Metadata
IOServiceTerminate
CCDatabase::getPipeEntry: owner not found\n
forEachTapWithOwnerAndPipe:Failed to malloc memory for keyArray
pruneDirectoryNDaysRead strtol EINVAL\n
CCDatabase::removeStreamProperty: owner not found\n
invalid_plist
CCLogFile::initWithConfig: Failed to create working directory string\n
CCDataTap::%s:%d cast failed\n
CCDatabase::getPipePropertyKeys: malloc failed for %zu bytes\n
CCPipeInterface::initWithRegistryEntry [pipeOwner: %s, pipeName: %s] Failed to initialize returned %x\n
CCProfileMonitor::profileCallback during shutdown at %d\n
CCDatabase::hasStream: owner not found\n
CCConfigure::setConsoleLevel
CCDaemon::enablePurgeNotification failed to create CFString for other save location\n
pruneDirectoryOnOSUpgrade: activity disabled\n
LogTimeSpan
CCConfigure::pipeConfigureCFDictionaryApplier Pipe: %s\n
CCConfigure::pipeConfigureCFDictionaryApplier Unsupported Key %s\n
_
CCDaemon::enablePurgeNotification failed to create CFString for save location\n
CCPipeInterface::resetDispatchQueue re-targeted dispatch source to capture queue entry:%u Owner:%s Pipe:%s\n
%s:%06u: Invalid argument\n
bluetooth.logging
CCXPCService::handleConnectionEvent CCDaemon::getInstance().isShutdownPending() true, dropping xpc event and exiting\n
CCConfigure::captureDirectoryCFDictionaryApplier
CCPipeInterface::setNotificationPort(), mach_port_insert_right failed kr[0x%08x]\n
cleanCaptureDirectories:Failed to malloc memory for valueArray
cc.file.forcecopy
CCDatabase::setStreamProperty: stream not found\n
CCXPCService::handleIncomingMessage No %s is received\n
CCLogFile::deleteFile successfully deleted: %s\n
CCDaemon::enablePurgeNotification failed to get save location\n
%@ %@ (%@)
CCCacheDelete: purge notification disabled\n
WiFi 
v16@?0^v8
CCLogFile::initWithConfig: Number of files cannot be 0\n
CCLogFile::addFile: No log before device first unlocked for PROTECTION_CLASS_C\n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  contains %s %d contains %s %d\n
tapLoop
waitForEvent
CCDaemon::%s:%d fileName %s is already compressed...\n
%s%s
CCXPCService::handleIncomingMessage: incoming, incomingConnection from '%s' with pid '%d', XPC_TYPE_CONNECTION, %d, XPC_TYPE_ERROR, %d, XPC_TYPE_DICTIONARY, %d\n
CCFile::populateCommonTelemetryDictionary - Failed to get config from database for owner/pipe\n
cleanupLogFile
CCDaemon::%s Failed to delete file %s errno: %d
unchanged
CoreCaptureStop non daemon cleanup, calling ccfree\n
CCDataFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
LogType
CCFile::copyFile Wrote '%s' source length: %lld archive length: %lld (reason: %s) Owner:%s Pipe:%s\n
CCDaemon::ccstart to create CCDaemon
CCFile::captureLog Failed to create directory %s (reason: %s)\n
CCFile::copyFile: Unable to stat source path errno %d, reason %s\n
CCFile::captureLogRun Current File %s (reason: %s) Owner:%s Pipe:%s\n
CCProfileMonitor::profileCallback no profile installed. previous state: %d, current state: %d\n
CCPcapngFormatter::writeLog  Inconsistent data (1) length=%lu\n
CCPcapngFormatter:: failed to get stream id\n
v16@?0@\"NSFileHandle\"8
CCProfileMonitor::profileCallback read WiFi profile plist valid: %d mask: %d\n
CCPcapngFormatter::writeLogHeader Failed to write. %ld\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate log identifier memory\n
config_alloc_fail
CCXPCService::handleIncomingMessage Key is %s\n
CCDaemon received power notification (0x%x) \n
servicePublished
storeChannelDescriptionFromStreamAndSubscription
CCDatabase::getPipePropertyKeys: no properties in pipe\n
CCDatabase::getStreams: malloc failed for %zu bytes\n
%Y-%m-%d %H:%M:%S.%F %z
hw.model
CCProfileMonitor::profileRemoved Exited :%d\n
xml
vector
(CCLogTap) CCPipeInterface::withRegistryEntry failed\n
Session Name: %s, Blob Name: %s %llu.%llu Owner:%s Name:%s\n
Time usecs
%s::%s no key %s in dictionary\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  dictionary doesn't contain %s\n
CCDatabase::removePipeProperty: owner not found\n
CCPcapngFormatter::writeFileHeader: Missing pipeOwner or pipeName\n
CCConfigure::notifyTimeout
BootArgs
%s::%s Failed to create IOReporter library friendly channel list\n
CCProfileMonitor::applyConfiguration profile is already removed
CCDatabase::getStreamProperty: stream not found\n
%s@%d: fCancelableBlock bailing out\n
%s@%d: bail - !mkdirRecursive\n
CCPcapngFormatter::buildStreamToInterfaceTable numberofStreams : %d\n
setNotificationPort
%s Duplicate Owner:%s Name:%s entry:%u\n
CoreCaptureStop complete\n
CCDaemon::init Failed to initialize mutex\n
refreshSubscriptionsFromStreamRegistry
owners_extraction_failed
invalid_plist_type
pruneDirectoryNDaysDo: older than %ld days (age=%.0fs)
CCProfileMonitor::applyProfile owner:%s, pipe:%s\n
CCPcapngFormatter::buildStreamToInterfaceTable: Missing owner or pipe name\n
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  rawData or interests not available\n
CCOSSerializeWithIOReporterFormatter::processAllDictionarieswithinIncommingArray  didnt find or wrong type in array at i %ld\n
CCLogTap::configureLogOptions\n
???
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected \n
CCProfileMonitor::cancelObservers removing event stream handler and Darwin observer\n
CCDatabase::removePipe: pipeName is NULL\n
rc.ok
CCConfigure::pipeConfigureCFDictionaryApplier watermark level to notify\n
CCDatabase::removeStreamProperty: stream not found\n
%s:%06u: Allocation failure\n
CCLogFile::sendTelemetry failed
CCConfigure::streamConfigureCoreCaptureCFDictionaryApplier
CoreCaptureStop setShutdownAlreadyTrue, exiting without doing anything
CCDatabase::findPipe: pipeName is NULL\n
XPC_TYPE_FD
CCLogTap::tapLoopImpl() entry:%u failed to map pipe with rc[0x%08x] ringSize[%llu]\n
writeMetadataSystemPlist
CCDatabase::findStream: streamName is NULL\n
com.apple.corecapture.manager-access
CCXPCService::handleIncomingMessage empty configuration\n
CCLogFile::initWithConfig: Failed to create formatter\n
CCConfigure::captureDirectoryCFDictionaryApplier dirName: %s\n
CoreCaptureStop called when isShutdownPending true, ignoring
source_open_failed
v8@?0
?
CaptureEvent
prune_dir_os_upgrade_ctl
false
ERROR INIT MUTEX: %d\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream name memory\n
CCConfigure::capture capture reason can not be NULL\n
CoreCaptureStop non daemon stopping, calling quiesceAllTaps()\n
profileLoaded
mutex_lock_failed
no_profiles_installed
CCPipeEntry copy constructor: malloc failed for %zu bytes\n
CCPipe::withOwnerNameCapacity Unsupported pipe type(%d)\n
CCCaptureDirectory
CCDaemon::init failed to create com.apple.corecaptured.background_queue\n
LogDataType
CCDaemon::%s:%d fileName is invalid\n
Stream
CCDaemon: CacheDelete disabled via boot-arg\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is %s NULL, with type %ld, but has type %ld\n
CCDatabase::setPipeProperty: key is NULL\n
CCPcapngFormatter::searchStreamIdInRegistry: Non-IORegistry pipe, querying CCDatabase for streamId=%u\n
CCOSSerializeWithIOReporterFormatter::writeLog unsupported root type for JSON Serialization
CCDatabase::getStreamProperty: entry->properties is NULL\n
invalid_plist_format
DirectoryName
CCFile::initWithTap memory allocation failed\n
CCFile::initWithTap Failed to create log directory  %s\n
CCLogTap::%s:%d cast failed\n
CCPipeInterface::initWithRegistryEntry entry:%u fConnectRef(%u)\n
forEachTapWithDirectory:Failed to malloc memory for valueArray
MGCopyAnswer
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCPipeMonitor::ccfree Exit\n
wlan
triggerStackshot_block_invoke
prune_dir_os_upgrade_snapshot
CCProfileMonitor::setStreamEventHandler Registered for notification callback.\n
IOReportChannelInfo
CCFile::mkdirRecursive Unable to create path '%s' as '%s' is not a directory errno %d\n
%s:%d CCDataTap::tapLoopImpl for entry:%u
CCFile::captureLog Capture(%s) is in progress. Ignoring new one.\n
(CCLogTap) CFNumberGetValue failed for LogPolicy\n
%s Unexpected CF object type ID. Expected (%lu), have (%lu) \n
CCPipeEntry operator=: malloc failed for %zu bytes\n
Unknown type: %llu %s:%d\n
Invalid State readOffset : %d, writeOffset : %d state %c, entry %u 
[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s
%s::%s channelStreamArray at i %ld not valid\n
... (%ld more bytes)
FileSize
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey invalid value \n
CCDataTap::%s invalid dataPipeInterface\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCDatabase::setPipeProperty: pipe not found\n
%s@%d: Unable to create samples: %s\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate Interface ID memory\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_settype failed\n
CCDataTap::processEvent quiesce pending entry:%u Owner:%s Name:%s\n
CCPipeInterface::resetDispatchQueue re-targeted notification port to capture queue entry:%u Owner:%s Pipe:%s\n
cleanCaptureDirectories:Failed to malloc memory for keyArray
CCDaemon::ccstart to create CCDaemon\n
CCPipe
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  didnt find or not a dict in array\n
CCFile::writeDataFiles memory allocation failed (reason: %s)\n
OSSerialize
%s/%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s/%s
%s:%06u Invalid captureId
XPC_TYPE_DATA
CCDaemon::shutdown is fired\n
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in array at i %ld\n
%s:%d CCPipe::withOwnerNameCapacity Registry entry:%u Unsupported pipe type(%d)\n
CCDatabase::addStream: streamName is NULL\n
CCLogFile::initWithRegistryEntry: Invalid arguments\n
%s Read Ptr is not multiple of %lu (%d) entry:%u \n
%s:%d %s::withRegistryEntry entry:%u Owner:%s Name:%s
CCDatabase::getStreamPropertyKeys: pipe not found\n
CCIOReporterFormatter::addRegistryChildToChannelDictionary  no %s found in %s\n
CCDatabase::removeOwner: ownerName is NULL\n
%s@%d: bail - !saveDir\n
%02x 
CCXPCService::handleIncomingMessage Unable to allocate scratch buffer\n
CCConfigure::configure keycount : %ld\n
CCConfigure::streamOwnerCFDictionaryApplier
CCConfigure::pipeOwnerCFDictionaryApplier
gzflush error code = %d\n
CCFile::isLogdirExists Failed to create  %s\n
CCLogTap::%s:%d tapLoopImpl entry:%u Owner:%s Name:%s\n
CCLogTap::profileRemoved, Owner:%s Name:%s entry:%u\n
%s::%s empty array\n
CCLogFile::withConfig()\n
Log
file:///private/var/Managed%20Preferences/mobile/com.apple.corecapture.configure.plist
CCDatabase::removeStream: stream not found\n
CCPcapngFormatter::writeFileHeader Uninitialized fStreamNameArray, i: %d\n
%b %d %H:%M:%S
CCConfigure::watermarkLevel watermarkLevel: %u\n
Found blob timestamp: %s:%d %llu %llu.%llu\n
%s@%d: Unable to create subscribtion: %s\n
%s:%06u: Invalid type\n
CCDatabase::findPipe: owner is NULL\n
CCConfigure::configureLogOptions
debug_data
Pcapng
quiesceAllTaps:Failed to malloc memory for valueArray
CCProfileMonitor::setStreamEventHandler Unable to get notification center for configuration reader.
CCDatabase::removeStream: streamName is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate dlt memory\n
CCDaemon::%s CCDaemon::getInstance().isShutdownPending() == true, skipping activityCheck()
Created a bad offset, don't save it! newOffset %u, payload length %u, padding %u,sizeof metadata %lu, STATE %c, entry:%u
CCPipeInterface::%s:%d mach_msg SEND_MSG kr:%u entry:%u
%@\n%@\n
BT 
CCIOReporterFormatter::getChannelsForSubscription  didnt find or wrong type in dict at i %ld for %s\n
CCDatabase::hasPipe: owner not found\n
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get stream entry for stream %ld\n
tapLoopImpl
CCLogTap::tapLoopImpl() isLogdirExists failed\n
fileID
CCPcapngFormatter::buildStreamToInterfaceTable Failed to allocate stream header memory\n
XPC_TYPE_INT64
Filename
CCFile::moveFile Failed to delete source file after copy: '%s', errno: %d\n
IOConnectCallAsyncStructMethod FAILED CCPipeInterface::%s::%d fNotificationPortIsSet:%d entry:%u kr[0x%08x]
%s:%06u Invalid reason
CCDatabase::getPipeProperty: pipe not found\n
Token is [0]: 0x%x... [7]:%x \n
CCLogFile::cleanupCapturedFiles log type is %d, current file is %s\n
resumeAllTapsFromQuiesced:no tap found
CCCacheDelete: purge history processing complete\n
Time
CFPropertyListCreateData() failed
Circular
%s:%06u Unable to copy arguments
CCDatabase::addStream: pipe not found\n
buildFileTables
CCDataFile::open Failed to create %s\n
CCPcapngFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
gzopen_failed
%s:%d processEvent entry:%u Owner:%s Name:%s
profileLoaded:Failed to malloc memory for keyArray
%s.%06llu %s
%s:%06u memory alloc failed\n
CCDataTap
CCPipeEntry operator=: malloc failed for cleanup, %zu bytes\n
221
CCConfigure::captureDictionaryCFDictionaryApplier
CCFile::copyFile gzwrite error: %s\n
kern.bootargs
CCLogTap
CCPcapngFormatter::searchStreamIdInRegistry: Stream not found in database\n
Unexpected event type %s\n
CCLogFile::initWithConfig: Failed to create log directory path\n
WiFiFWTrapBinary
CCDaemon::freeResources: clearing working directory on shutdown
CCIOReporterFormatter
CCDatabase::setPipeProperty: owner not found\n
Found session timestamp: %s:%d %llu %llu.%llu\n
applied
CCProfileMonitor 10 seconds since CCProfileMonitor initted, calling profileCallback to check for installed profiles\n
CCProfileMonitor::applyConfiguration  shutdown pending, dropping request and exiting\n
profile_loaded_notification
CCOSSerializeWithIOReporterFormatter::createDictionaryWithProcessedIOReporter  failed to duplicate dictionary\n
stopPipeMonitor
Incorrect number [numberOfDirArrayEntries: %lld, readIndex %lld] of directory entries. Skip sorting.\n
Received Capture Event entry:%u Owner:%s Name:%s\n
findTapWithOwnerAndPipe:Failed to malloc memory for keyArray
capture.plist
CCPcapngFormatter::writeLogHeader logMetaData is NULL\n
CCLogFile::initWithRegistryEntry: pthread_mutexattr_init failed\n
CCPipeMonitor::%s:%d Release Tap i %zu
BuildVariant
%s:%d: mmap failed\n
CCConfigurePipe
CCDaemon
CCIOReporterFormatter::writeLog  Inconsistent data (1) length=%lu\n
%z
_processorThread
CCFile::moveFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCLogTap::profileLoaded, Owner:%s Name:%s\n
isActive:Failed to malloc memory for valueArray
CCOwnerEntry operator=: malloc failed for %zu bytes\n
CCConfigure::configureOptions Not found the tap owner:%s, pipe: %s\n
/tmp/cc.locktest
servicesTerminated
Error creating plist...\n
CCXPCService::handleIncomingMessage
XPC_TYPE_DOUBLE
Entitlement exists, but check failed. \n
CCConfigure::captureDirectoryCFDictionaryApplier Pipe: %s\n
cc.recovery.allow
CCPcapngFormatter::writeLog Failed to write(2) Length=%lu, tempLength=%lu\n
CCLogFile::initWithConfig: pthread_mutexattr_settype failed\n
CCDaemon::init invalid arguments passed for non-daemon case\n
CCDaemon:: No name matching CCPipe service found \n
CCFile::captureLog\n
CCFile::captureLogRun Skipping current file Dir file %s, Current File %s Owner:%s Pipe:%s\n
(CCLogTap) IORegistryEntryCreateCFProperty failed for LogPolicy\n
set_protection_class_failed
CCLogTap::updateLogFlags\n
CCPipeMonitor::CCPipeMonitor Failed to initialize mutex\n
CCPcapngFormatter::writeFileHeader: Failed to cast fWriteObject to CCFile\n
Dropped Log message expected sequence number = %u, Received %u\n
deleteDirectory: deleting '%s' reason: %s
CCDaemon::%s:%d unable to create filePathRef\n
%s:%06u Configuration type is not dictionary\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe, querying database\n
CCConfigure::streamStreamCFDictionaryApplier
IOReportCreateSamplesRaw() returned 0 sized dictionary %s
209
IOReportCreateSamplesRaw() returned 0 sized dictionary
CCDatabase::getPipeProperty: entry->properties is NULL\n
forEachTapWithDirectory:no tap found
v16@?0^{__CFArray=}8
CCXPCService::cancelActiveConnections cancelling %lu connections\n
MultiFunctionManager
pcapng
XPC_TYPE_ERROR
CCFile::moveFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
CCConfigure::streamConfigureConsoleCFDictionaryApplier
CCPipeInterface::setNotificationPort(), mach_port_get_attributes failed kr[0x%08x]\n
com.apple.ManagedConfiguration.profileListChanged
CCPcapngFormatter::buildStreamToInterfaceTable Failed to convert stream name\n
CCConfig is %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
Id
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected \n
CCPipeInterface::%s:%d rcvd terminate msg:0x%x entry:%u
CCCacheDelete: cannot register for purge notifications ret=0x%x\n
CCPcapngFormatter::writeLog  Inconsistent data (2) lengthContinue=%lu\n
CCConfigureStream
CCDaemon received system wake or will not sleep (0x%x), all cctap resumed from quiesced state\n
CCLogTap::setWatermarkLevel\n
amfm-sunrise
CCDaemon::%s:%d unable to allocate destination buffer\n
CCDaemon::%s unable to stat compressed file '%s'
true
/var/log/CoreCapture
%s CANNOT FIND tap with Owner:%s Name:%s\n
CCDaemon::%s:%d Error writing to destination buffer %s: %s\n
CCDatabase::getStreamConfig: stream not found\n
CCDatabase::getStreamEntry: owner not found\n
CCXPCService::startXPCService() Failed to start XPC service \n
CCLogFile::withRegistryEntry() Invalid log type %d\n
CCConfigure::capture
CCConfigure::streamConfigureCFDictionaryApplier
CCConfigure::policy policy: %u\n
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<array>\n
CCConfigure::captureDirectoryCFDictionaryApplier Key: %s\n
CCPipeInterface::%s::%d fNotificationPortIsSet:%d rc:%d entry:%u
UniqueDeviceID
CCProfileMonitor::setStreamEventHandler \n
CCLogTap::pipeEvent EXIT Event Count - Empty (%d) Reserved (%d) Written (%d) Padding (%d) Capture (%d) Skip (%d),prevread offset %u, new read offset %u, prev seq %u, expected seq %u entry %u, ring state readoff %u, write offset %u, Owner:%s
addRegistryChildToChannelDictionary
CCProfileMonitor::profileCallback empty dictionary. fProfileLoaded %d fProfileRemoveApplied %d\n
CCTap::%s:%d entry:%u
CCIOReporterFormatter::addRegistryChildToChannelDictionary  not array\n
CCDatabase::removeStreamProperty: property key not found\n
CCFile::withTap Unsupported file type(%d) \n
CCPipeInterface::dispatch_source_create failed
CCConfigure::applyConfiguration Configuration type is not dictionary\n
none
DeviceFusing
CCConfigure::applyConfiguration
ips
CompressionDisabled
CCLogTap::tapLoop(), Error setting notification port rc[0x%08x]\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected, couldn't resolve device \n
CCOSSerializeFormatter::writeLog CFDataGetBytePtr() failed
com.apple.corecaptured.shutdown
%s:%d Owner:%s skipping profileLoaded
%s:%06u Stackshot rate limit: a stackshot was triggered within the last %d seconds. Skipping stackshot for id %s (reason: %s)\n
%s:%06u unable to create set\n
CCDatabase::getStreamConfig: owner not found\n
source_buffer_alloc_failed
%s:%06u unable to allocate dictionary\n
CCProfileMonitor::profileCallback Loaded\n
CCConfigure::pipeConfigureCFDictionaryApplier Key: %s\n
CCDaemon:: Num of matching CCPipe %ld\n
getOwnersFromCCConfig
CCDatabase::getStreamEntry: pipe not found\n
^v8@?0
Found SessionName: %s:%d %llu %s\n
CCProfileMonitor::profileCallback starting states -> source %d fProfileToken %d isShutdownPending %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCProfileMonitor::applyProfile fProfileLoaded is not set, not applying owner:%s, pipe:%s\n
CCDatabase::addOwner: ownerName is NULL\n
CCDaemon power notification enabled\n
CCPipeMonitor::cleanCaptureDirectories - fails to unlock\n
%s 
%s@%d: fExitNextIteration bailing out\n
cc.log.seed
LogLevel
present
Console
CCFile::captureLogRun Failed to stat file %s%s, errno: %d Owner:%s Pipe:%s\n
CCLogTap::setConsoleLogFlags Owner:%s Name:%s entry:%u\n
forEachTapWithOwnerAndPipe:Failed to malloc memory for valueArray
/Library/Logs/CrashReporter/CoreCapture
/%s/%s/
CCFile::captureLog Received Capture notice id: %d.%06d, reason = %s\n
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe, getting config from database\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap pipe with rc[0x%08x]\n
CCXPCService::handleIncomingMessage shutdown pending true, dropping message and exiting\n
failed
disable
CCDatabase::removePipe: ownerName is NULL\n
CCDatabase::hasPipe: pipeName is NULL\n
CCDatabase::getPipePropertyKeys: owner not found\n
CCProfileMonitor::initWithConfigure ERROR INIT MUTEX: %d\n
CCDatabase::hasStream: pipeName is NULL\n
CCXPCService::handleIncomingMessage Unable to get remote connection\n
CCLogFile::initWithConfig\n
CCLogTap::tapLoopImpl() entry:%u failed to unmap zero-length pipe with rc[0x%08x]\n
%s - localLogMetadata.payloadLength + logPayloadOffset IS BEYOND RINGSIZE. ADJUST entry:%u
CCProfileMonitor::freeResources done\n
PipeType
CCFile::initWithTap fLogDirPath is invalid\n
CCDatabase::removeStream: ownerName is NULL\n
PipeSize
findTapWithOwnerAndPipe:Failed to malloc memory for valueArray
SourceVersion
CCDatabase::findPipe: owner->pipes is NULL\n
CCXPCService::handleIncomingMessage XPC message is not dictionary\n
CCLogFile::sendTelemetry analytics_send_event_lazy weak link import failed
CCProfileMonitor::setStreamEventHandler event received:%s\n
CCIOReportDumpQueue
CCLogFile::addFile Failed to create %s\n
CCDaemon::init Failed to create timer dispatch source\n
com.apple.corecapture.fileclose
%s - STATE IS RESERVED. BREAK entry:%u
CCConfigure::pipeConfigureCFDictionaryApplier notify timeout\n
CCFile::captureLogRun copying files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
%s:%06u: opendir failure - %s\n
CCServiceMonitor::scanServices fMatching Dictionary Retain count(2) is %ld\n
CCConfigure::captureDirectory
%s::%s didn't find or wrong type in array at i %ld\n
%s::%s streams %ld\n
CCDatabase::hasStream: pipe not found\n
CCDaemon received system sleep notification (0x%x), all cctap quiesced\n
dest_stat_failed
CCLogTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
no_remote_connection
CCConfigure::capture Reason: %s\n
json
profileRemoved:no tap found
CCServiceMonitor::scanServices fMatching Dictionary Retain count(1) is %ld\n
Entitlement query did not succeed \n
CCPipeInterface::setDispatchQueue entry:%u Owner:%s Pipe:%s\n
%s:%06u invalid configuration\n
CCDatabase::getOwners: no owners in database\n
XPC_TYPE_STRING
CCLogTap::setConsoleLogLevel Owner:%s Name:%s entry:%u\n
User
v12@?0i8
CCDatabase::getPipes: no pipes in owner\n
com.apple.corecaptured.service_notify
CCProfileMonitor::freeResources Entered\n
Received a connection event\n
%s::%s Can't create channelStreamDictionary\n
CCLogFile::initWithConfig: Failed to initialize PCAP formatter\n
SigningFuse
CCDatabase::removePipeProperty: pipe not found\n
CCLogFile::withRegistryEntry()\n
CCLogFile::withConfig() Invalid parameters\n
CCConfigure::captureDictionaryCFDictionaryApplier dirName: %s\n
CCConfigure::captureDirectoryCFDictionaryApplier Owner: %s\n
fMutexCleanDirectories not acquired, bail out\n
compressFile
CCDatabase::hasStream: streamName is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable: Found stream header (%ld bytes) for stream\n
CCConfigure::applyConfiguration CCSTOP key  \n
CCConfigure::setConsoleFlags
CCConfigure::pipeConfigureCFDictionaryApplier Owner: %s\n
Couldn't update read ptr. Cannot guarantee integrity of message %d\n
cleanCaptureDirectory: count %lld exceeds max %lld, deleting %lld oldest
CCPcapngFormatter::buildStreamToInterfaceTable: Found %ld streams in database\n
DeviceInfo
CCDatabase::getStreamProperty: owner not found\n
wakeupTapLoopInternal
forEachTapWithOwnerAndPipe:no tap found
historyDone
CCProfileMonitor::setStreamEventHandler calling profileCallback(CCProfileChangeSourceXPCStream)\n
seed build (or boot-arg) and device hasn't been unlocked since boot. Won't process event and continue when next event is posted entry:%u\n
%s Tap Find Tap with Owner:%s Name:%s\n
ProfileLoaded
CCIOReporterFormatter::writeLog  Insufficient length=%lu to hold IOReporterHeader_t\n
CCXPCService::handleIncomingMessage keycount : %ld\n
CCLogFile::initWithConfig: Failed to create log directory\n
</array>\n</plist>\n
CCDatabase::getPipes: malloc failed for %zu bytes\n
CCDatabase::getStreamPropertyKeys: owner not found\n
CCPipeInterface::setDispatchQueue re-targeted notification port to continuous queue entry:%u Owner:%s Pipe:%s\n
CCPipeMonitor::CCPipeMonitor Failed to initialize fMutex\n
IOServicePublish
CCConfigure::streamPipeCFDictionaryApplier
CCConfigure::pipePipeCFDictionaryApplier
CCConfigure::pipeConfigureCFDictionaryApplier
CCFile::copyFile failed: source_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
com.apple.corecaptured.CCTap
Rollover
Prod
CCDatabase::removeStream: pipe not found\n
CCPcapngFormatter::searchStreamIdInRegistry: Found matching stream in database\n
CCPipeMonitor::%s:%d Release Tap for entry:%u
CCCacheDelete: purge notification already enabled\n
CCCacheDelete: failed to create dispatch queue\n
CCIOReporterFormatter::getChannelsForSubscription  didn't find matching subscription\n
CCDatabase::getPipes: owner not found\n
CoreCaptureStart called with bad args, crashing
cc.debug.keepwd
CCPcapngFormatter::writeLog Unexpected log data \n
CoreCaptureStart called when CCDaemon already running, returning existing instance
CCDaemon::runShutdownThread Exiting via xpc_transaction_try_exit_clean
CCDatabase::removePipe: pipe not found\n
CoreCapture
CCConfigure::pipeOwnerCFDictionaryApplier Owner: %s\n
hw-model
CCDatabase::findStream: pipe->streams is NULL\n
StreamHeader
Data
com.apple.MCX._managementStatusChangedForDomains
CCDatabase::getPipeConfig: owner not found\n
CCTextFormatter::buildLogIdentTable -- alloc failed\n
Owner
CCLogTap::withRegistryEntry failed\n
CCPipeInterface::withRegistryEntry Unsupported pipe type(%d) \n
CCDatabase::~CCDatabase: malloc failed for %zu bytes\n
rc
CCDaemon::runShutdownThread Cannot xpc_transaction_try_exit_clean, still outstanding transactions (attempt %d/%d)
CCDataTap::tapLoopImpl exit entry:%u Owner:%s Name:%s Exiting taploop\n
Found blob name: %s:%d %llu %s\n
CCLogTap::isActive idle < duration, Owner:%s Name:%s entry:%u duration:%f\n
cancelableBlockFunc_block_invoke
CCPcapngFormatter::buildStreamToInterfaceTable: Failed to get CCFile object\n
serviceTerminated
%s
CCProfileMonitor::profileCallback exiting states CCDaemon::getInstance().isShutdownPending() %d fProfileLoaded %d fProfileRemoveApplied %d\n
CCProfileMonitor::profileRemoved Entered %d\n
CCDatabase::getStreamConfig: pipe not found\n
Stream Name is %s\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromSubscription  failed to store Channel Description\n
osversion
success
CCOSSerializeWithIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCFile::copyFile failed: dest_path_alloc_failed file: '%s' Owner:%s Pipe:%s\n
Dev
NumberOfFiles
IOReturn CCLogTap::processEvent(CCLogPipeInterface *)
CCPipeInterface::setNotificationPort(), mach_port_allocate failed kr[0x%08x]\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.
fileDidOpen
Notification to dump to disk failed for entry:%u
pruneDirectoryNDaysDo lstat failed on %s:\n%s\n
UUID
CCDataTap::tapLoop(), Error setting notification port rc[0x%08x]\n
%s - no fFile entry:%u
com.apple.corecaptured.purge
Reason
CCDatabase::getStreamProperty: pipe not found\n
CCFile::initWithTap Failed to create formatter\n
Continuous
CCPipeInterface::%s:%d rcvd terminate signal entry:%u
%s:%d CCTap::withRegistryEntry Registry entry:%u not found\n
(CCLogTap) CFNumberGetValue failed\n
CCPipeInterface::IOServiceClose entry:%u fConnectRef(%d)\n
/usr/lib/libMobileGestalt.dylib
wifi.megawifi
XPC_TYPE_NULL
DriverName
gzflush failed errno = %d, errnum = %d, reason : %s, %s\n
CCDaemon::%s Compressed '%s%s' -> %lld bytes
CCConfigure::pipeConfigureCFDictionaryApplier capture\n
CCDataTap::processEvent() seed build and device hasn't been unlocked since boot - not processing event and waiting for the next. entry:%u Owner:%s Name:%s\n
CCPipeMonitor::CCPipeMonitor Failed to CCIOReportDumpProcessor.\n
CCCacheDelete: framework not available on this platform\n
CCIOReportInterestSubscriptionIDx
CCIOReporterFormatter::writeLog Failed to write(1) dsize=%lu, tempLength=%lu\n
CCDatabase::getStreams: pipe->streams is NULL\n
IOReportChannels
CCFile::captureLogRun moving files took %f seconds (reason: %s) Owner:%s Pipe:%s\n
CCDatabase::removeOwner: owner not found\n
CCDatabase::addStream: ownerName is NULL\n
CCDatabase::hasStream: ownerName is NULL\n
CCDataTap::initWithRegistryEntry invalid fPipeInterface\n
CCPipeInterface::setDispatchQueue failed to create a serial dispatch queue for continuous pipe entry:%u Owner:%s Pipe:%s\n
.gz
CCDatabase::hasPipe: ownerName is NULL\n
CCIOReportDumpQueue::_processorThread bail - !keysTypeRef\n
invalid_reference
CCFile::moveFile failed: %s file: '%s' Owner:%s Pipe:%s\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  no key %s in dictionary\n
CCProfileMonitor::setStreamEventHandler event received matching kXPCManagedPrefsName, no action from this handler\n
CCDatabase::addPipe: failed to find/create owner\n
CCDaemon::runShutdownThread Failed to exit cleanly after %d attempts, forcing exit
CCFile::populateCommonTelemetryDictionary - Non-IORegistry pipe missing owner or name\n
CCFile::writeMetadataFiles failed malloc\n
CCOwnerEntry copy constructor: malloc failed for %zu bytes\n
CCDatabase::getPipeProperty: owner not found\n
XPC_TYPE_CONNECTION
getOsVersion %s\n
%s::%s key %s has wrong type in dictionary\n
%s:%s
No channels found\n
CCLogTap::setNotifyTimeout\n
NULL
CCDatabase::findStream: pipe is NULL\n
CCLogFile::withConfig() Invalid log type %d\n
%s@%d: bail - !legend\n
\n
CCLogFile::buildFileTables fNumberOfArrayEntries is zero\n
CCDataTap::isActive idle < duration  3 entry:%u duration:%f\n
CCCacheDelete: cannot create monitored directories\n
CCDatabase::getStreamPropertyKeys: entry->properties is NULL\n
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCLogTap::tapLoop entry:%u Owner:%s Name:%s Exiting taploop\n
profileLoaded:no tap found
%s::%s channelStreamArray not valid\n
%s::%s shapeIOReportLibraryFriendlyDictionary failed\n
CCLogFile::initWithRegistryEntry buildFileTables\n
Capture
(CCLogTap) IORegistryEntryCreateCFProperty failed\n
mach-absolute-time
bin
ERROR INIT COND: %d\n
CCPcapngFormatter::writeLog Failed to write(1) Length=%lu, tempLength=%lu\n
shapeIOReportLibraryFriendlyDictionary
%s::%s didn't find %s or wrong type in array at i %ld\n
CrashTracerLog
isActive:Failed to malloc memory for keyArray
resumeAllTapsFromQuiesced:Failed to malloc memory for valueArray
CFDataGetBytePtr() failed
getOwnersFromPipesAndStreams
CCDatabase::findOwner: ownerName is NULL\n
CCPcapngFormatter::buildStreamToInterfaceTable: Non-IORegistry pipe initialized with %u total interfaces\n
CCLogTap::updateConsoleLogFlags Owner:%s Name:%s entry:%u\n
Time localtime
%s:%06u failed to allocate memory\n
CCDatabase::getStreamPropertyKeys: stream not found\n
writeLogFooter
CCFile::withRegistryEntry() entered entry:%u\n
dest_buffer_alloc_failed
CCPipeMonitor::isActive:no tap found
rescan
CCDatabase::addOwner: CFStringCreateCopy failed\n
CCLogTap::setLogLevel Owner:%s Name:%s entry:%u\n
CCDaemon::%s:%d failed to open dest buffer %s\n
%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s/%s
CCDatabase::addStream: owner not found\n
CCPcapngFormatter::writeFileHeader: Non-IORegistry pipe - owner=%s, name=%s\n
CCXPCService: logging command received but not supported on this platform\n
CCLogFile::configureLogOptions Configuration is %s\n
CCDaemon::init Failed to create CCProfileMonitor\n
CCFile::moveFile Moved '%s' -> '%s' (reason: %s) Owner:%s Pipe:%s\n
CCProfileMonitor::profileCallback getting owners from profile failed
%s:%06u keycount : %ld\n
CCDatabase::getPipePropertyKeys: pipe not found\n
CCConfigure::pipeConfigureCFDictionaryApplier Configure Log Options\n
CCPipeMonitor::%s:%d Tap corresponding to terminated Pipe not found Owner:%s Name:%s entry:%u
CCDatabase::addStream: CFStringCreateCopy failed\n
ProfileRemoved
buffer_alloc_fail
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
CCFile::copyFile Unable to stat dest path '%s' errno: %d reason: %s prevErr: %s\n
CCLogTap::setPolicy, Owner:%s Name:%s entry:%u\n
CCLogFile::initWithConfig: pthread_mutex_init failed\n
CCLogFile::initWithConfig: Failed to create directory/file name strings\n
com.apple.corecaptured.serial_queue
cc.cachedelete.disable
%s.%06llu %s %06llu.%06llu %s<%c>[%u] 
CCLogFile::initWithConfig: pthread_mutexattr_init failed\n
CCFile::captureLogRun() Exiting CCFile::captureLogRun (reason: %s) Owner:%s Pipe:%s\n
[%04d-%02d-%02d_%02d,%02d,%02d.%06u]-%s-%03d.%s
CCConfigure::captureDirectoryCFDictionaryApplier capture\n
IOReportGroupName
profileRemoved:Failed to malloc memory for valueArray
quiesceAllTaps:no tap found
corecapture
com.apple.MobileSoftwareUpdate
%s/[%04d-%02d-%02d_%02d,%02d,%02d.%06llu]=%s
findTapWithOwnerAndPipe:no tap found
InverseDeviceID
system.plist
CCDatabase::getPipePropertyKeys: entry->properties is NULL\n
CCDaemon IORegisterForSystemPower failed\n
CCDaemon::init failed to create come.apple.corecaptured.service_notify\n
CCDataTap::profileRemoved, Owner: %s, Name: %s\n
FileCloseReason
v16@?0@\"NSObject<OS_xpc_object>\"8
CCOwnerEntry::~CCOwnerEntry: malloc failed for %zu bytes\n
CCDatabase::addPipe: pipeName is NULL\n
CCLogFile::configureLogOptions Current Log Type:%d, File Size=%u, Max Number Of Files:%u\n
%s:%06u Daily stackshot limit reached (%zu stackshots). Skipping stackshot for id %s (reason: %s)\n
CCPipeEntry::~CCPipeEntry: malloc failed for %zu bytes\n
com.apple.corecaptured.background_queue
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup failed to find required objects legend %d && providerID %d && providerName %d && channelID %d && channelType %d && channelName %d\n
CCPipeMonitor::%s:%d Tap corresponding to Pipe not found
%s Owner:%s Name:%s entry:%u\n
CCProfileMonitor::profileCallback changed. previous state: %d, current state: %d\n
%s.%06llu %s %s<%c>[%u] 
writeLogHeader
XPC_TYPE_SHMEM
CCDaemon purge notification enabled\n
triggerStackshot
CCDatabase::getStreams: pipe not found\n
CCLogDisable
XPC_TYPE_BOOL
default
CCFile::copyFile failed: %s file: '%s' Owner:%s Pipe:%s\n
CCDaemon::%s:%d dirPath is invalid\n
CCConfigure::pipePipeCFDictionaryApplier Pipe: %s\n
CCServiceMonitor::servicesPublished ignoring processing servicePublished due to isShutdownPending
%s:%06u: Failed reading '%s' from registry\n
LogIdentifier
com.apple.corecaptured
%s::%s failed to store Channel Description\n
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup %s expected obj is%s NULL, with type %ld, but has type %ld\n
CCIOReporterFormatter::getChannelsForStreamAndSubscription  Couldnt find %s\n
Found blob length: %s:%d %llu %zu\n
gzwrite_failed
Text
profileLoaded:Failed to malloc memory for valueArray
CCIOReporterFormatter::getChannelsForSubscription  didnt find %s\n
Invalid argument @'%s':%06u
CCPcapngFormatter::searchStreamIdInRegistry: Found %ld streams in database\n
Entitlement couldnt be found \n
Name
CCPipeMonitor::ccfree - fails to destroy lock. Error[%d]\n
path
CCDatabase::addPipe: CFStringCreateCopy failed\n
CCDatabase::setStreamProperty: key is NULL\n
XPC_TYPE_UINT64
CCLogFile::initWithRegistryEntry Number of files can not be 0.\n
CCPipeMonitor::ccfree - fails to unlock. Error[%d]\n
CCFile::mkdirRecursive Unable to mkdir on '%s', errno %d\n
CCProfileMonitor::applyConfiguration profile is already removed or not installed
CCDatabase::hasOwner: ownerName is NULL\n
CCStart
WatermarkLevel
CCPipeMonitor::ccfree Failed to acquire lock\n
%s:%06u Triggering stackshot with id %s due to %s\n
Entitlement is NULL \n
CCLogFile::initWithConfig: CFNumberCreate failed for logDataType\n
ALL
CCDaemon will calling shutdown()\n
CCPcapngFormatter::buildStreamToInterfaceTable: stream specific header not aligned to 64 bits. Dropping.\n
FileOptions
LogFlags
LogOptions
CCConfigure::watermarkLevel
quiesceAllTaps:Failed to malloc memory for keyArray
%s::%s didn't find or not a dict in array\n
CCDatabase::removeStream: owner not found\n
forEachTapWithDirectory:Failed to malloc memory for keyArray
WiFi
CCIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverIDKey expected obj is%s NULL, with type %ld, but has type %ld\n
/private/var
CCProfileMonitor::profileCallback read BT profile plist valid: %d mask: %d\n
doSaveChannels
Unknown type
Entitlement exists, and check is successful\n
%s::%s !subscriptionLegendDictionaryArray\n
CCProfileMonitor got com.apple.ManagedConfiguration.profileListChanged update, calling profileCallback(%d)\n
CCDatabase::setStreamProperty: owner not found\n
CCXPCService::handleIncomingMessage release, incomingConnection\n
CCDaemon::init: clearing working directory on startup
CCOSSerializeWithIOReporterFormatter::storeChannelDescriptionFromDriverGroup kIOReportDriverNameKey expected obj %s is NULL, with type %ld, but has type %ld\n
storeChannelDescriptionFromSubscription
CCDatabase::getOwners: malloc failed for %zu bytes\n
CCDataTap::%s:%d tapLoop entry:%u Owner:%s Name:%s\n
None
CCIOReportStream
%s@%d: bail - !hash\n
ERROR: cannot build the XML data\n
CCLogTap::setLogFlags Owner:%s Name:%s entry:%u\n
CCFile::mkpath fails to create path '%s' as '%s' is not a directory\n
CCDatabase::addStream: pipeName is NULL\n
,
previous and current sequence numbers are same %u prev read offset %u,previous write offset %u, new write offset %u, entry %u\n
os-version
%s:%06u: CFStringGetCString failure\n
CCDataTap::isActive tap is fBusy Active 2 entry:%u\n
CCCacheDelete: no directories provided\n
/Library/Logs/CoreCapture
CCXPCService::initWithConfigureAndPipeMonitor ERROR INIT MUTEX: %d\n
initWithRegistryEntry
CCConfigure::applyConfiguration CCSTART key \n
CoreCaptureStart: ENTRY - workingDir=%p, saveDir=%p, isCCDaemon=%d, isInitialized=%d\n
create_protected_file_failed
CCIOReporterFormatter::writeLog  Inconsistent data (3) payloadLength=%d, length=%lu, lengthContinue=%lu\n
CCXPCService::handleIncomingMessage Unable to allocate config data\n
CCConfigure::pipeConfigureCFDictionaryApplier pipe policy\n
Time secs
CCIOReporterFormatter::writeLog  Didn't find channels\n
CCProfileMonitor::profileCallback unchanged mask. previous state: %d, current state: %d\n
dataWithBytes:length:
dataWithJSONObject:options:error:
descriptionWithCalendarFormat:
initWithUTF8String:
installedProfileIdentifiers
length
containsString:
objectForKeyedSubscript:
sharedConnection
stringWithFormat:
unsignedLongLongValue
writeData:
UTF8String
countByEnumeratingWithState:objects:count:
```
