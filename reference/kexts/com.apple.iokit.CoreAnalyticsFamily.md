# `com.apple.iokit.CoreAnalyticsFamily`

- Name: CoreAnalyticsFamily
- Version: `1`
- UUID: `F7BDDE28-A2D0-3713-BA1F-8F8C844382C4`
- Source version: `577.40.7.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 15.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 15.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### CoreAnalyticsHub
- `CFBundleIdentifier`: `com.apple.iokit.CoreAnalyticsFamily`
- `IOClass`: `CoreAnalyticsHub`
- `IOMatchCategory`: `CoreAnalyticsHub`
- `IOPersonalityPublisher`: `com.apple.iokit.CoreAnalyticsFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `CoreAnalyticsUserClient`


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `CoreAnalyticsEventRatePolicy` | 0x40 |  |
| `CoreAnalyticsHub` | 0x148 | IOService → IORegistryEntry |
| `CoreAnalyticsMessenger` | 0x90 | IOService → IORegistryEntry |
| `CoreAnalyticsPipe` | 0xa8 | IOEventSource |
| `CoreAnalyticsTestUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `CoreAnalyticsUserClient` | 0x110 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00003e67 off=0x00904e10-0x00908c77 addr=0xfffffe0007908e10-0xfffffe000790cc77 r--/r--   __TEXT            
	sz=0x00001eae off=0x00905488-0x00907336 addr=0xfffffe0007909488-0xfffffe000790b336               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001941 off=0x00907336-0x00908c77 addr=0xfffffe000790b336-0xfffffe000790cc77               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00008a24 off=0x02c00520-0x02c08f44 addr=0xfffffe0009c04520-0xfffffe0009c0cf44 r-x/r-x   __TEXT_EXEC       
	sz=0x00008634 off=0x02c00520-0x02c08b54 addr=0xfffffe0009c04520-0xfffffe0009c0cb54          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003f0 off=0x02c08b54-0x02c08f44 addr=0xfffffe0009c0cb54-0xfffffe0009c0cf44          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001d0 off=0x049db298-0x049db468 addr=0xfffffe000b9df298-0xfffffe000b9df468 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049db298-0x049db35c addr=0xfffffe000b9df298-0xfffffe000b9df35c               __DATA.__data             
	sz=0x00000108 off=0x00000000-0x00000108 addr=0xfffffe000b9df360-0xfffffe000b9df468               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002110 off=0x012c2b10-0x012c4c20 addr=0xfffffe00082c6b10-0xfffffe00082c8c20 rw-/rw-   __DATA_CONST      
	sz=0x00000030 off=0x012c2b10-0x012c2b40 addr=0xfffffe00082c6b10-0xfffffe00082c6b40         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000030 off=0x012c2b40-0x012c2b70 addr=0xfffffe00082c6b40-0xfffffe00082c6b70         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001b78 off=0x012c2b70-0x012c46e8 addr=0xfffffe00082c6b70-0xfffffe00082c86e8         __DATA_CONST.__const            
	sz=0x000002c0 off=0x012c46e8-0x012c49a8 addr=0xfffffe00082c86e8-0xfffffe00082c89a8         __DATA_CONST.__kalloc_type      
	sz=0x000001f8 off=0x012c49a8-0x012c4ba0 addr=0xfffffe00082c89a8-0xfffffe00082c8ba0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000078 off=0x012c4ba0-0x012c4c18 addr=0xfffffe00082c8ba0-0xfffffe00082c8c18         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x012c4c18-0x012c4c20 addr=0xfffffe00082c8c18-0xfffffe00082c8c20         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 141 at 0x04aedae4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F7BDDE28-A2D0-3713-BA1F-8F8C844382C4
008: LC_SOURCE_VERSION           577.40.7.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab8ef0 size=0x158
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `CoreAnalyticsFamily`
- `CFBundleIdentifier`: `com.apple.iokit.CoreAnalyticsFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `CoreAnalyticsFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/CoreAnalyticsFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896341488`
- `_PrelinkExecutableRelativePath`: `CoreAnalyticsFamily`
- `_PrelinkExecutableSize`: `60267`
- `_PrelinkExecutableSourceAddr`: `-2198896341488`
- `_PrelinkKmodInfo`: `-2198828354920`

## Strings (327) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `initWithWorkloop`
- `%s::%d:Overriding default count limit for rate limit policy of %d with ca.maxcount of %d\n`
- `IOReturn CoreAnalyticsHub::createReporters()`
- `IOReportLegend`
- `CoreAnalyticsMessenger`
- `%s::%d:success\n`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod invalid payload\n`
- `CoreAnalyticsUserClient`
- `bool CoreAnalyticsEventRatePolicy::initWithWorkloop(IOWorkLoop *)`
- `%s::%d:Failed to create _eventRateMeasurementSpanTimer\n`
- `com.apple.coreanalytics.kextapirateexceeds`
- `CoreAnalyticsHub`
- `IOReturn CoreAnalyticsHub::setClientGated(CoreAnalyticsUserClient *)`
- `EventName Received`
- `EventName SerializeFailure`
- `CoreAnalyticsPipe`
- `12111112122212121111111111111111212121112`
- `void CoreAnalyticsHub::handleDemoTimerExpiry(IOTimerEventSource *)`
- `EventName SharedDataQueueFull`
- `virtual bool CoreAnalyticsUserClient::start(IOService *)`
- `virtual bool CoreAnalyticsUserClient::didTerminate(IOService *, IOOptionBits, bool *)`
- `ca.ratespan`
- `ca.maxcount`
- `%s::%d:Failed to get count for %s\n`
- `EventCountAboveThreshold`
- `IOReturn CoreAnalyticsHub::serializePayload(OSObject *, OSSerialize *, size_t *)`
- `kern_return_t IOCoreAnalyticsSendEvent(uint64_t, OSString *, OSDictionary *)`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod failed to unserialize xml`
- `site.CoreAnalyticsUserClient`
- `%s::%d:Waiting %dms before producing CoreAnalytic message every %dms\n`
- `virtual void CoreAnalyticsHub::free()`
- `virtual void CoreAnalyticsHub::close(IOService *, IOOptionBits)`
- `site.KernelEvent`
- `API dropped and freed`
- `%s::%d:%s::%s bad _sender\n`
- `%s::%d:%s::%s bad _nag\n`
- `virtual IOReturn CoreAnalyticsUserClient::clientDied()`
- `%s::%d:Failed to init eventPayload\n`
- `%s::%d: failed to alloc _dictLock\n`
- `%s::%d:event %s overage count %d\n`
- `%s::%d:Failed to create commandgate\n`
- `virtual void CoreAnalyticsHub::stop(IOService *)`
- `void CoreAnalyticsHub::incrementEventNameSerializeTooLarge(OSString *)`
- `bool CoreAnalyticsMessenger::startMessages()`
- `initWithParams`
- `virtual IOReturn CoreAnalyticsTestUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `EventName`
- `IOReturn CoreAnalyticsHub::__newUserClientGated(task_t, void *, UInt32, OSDictionary *, IOUserClient **)`
- `%s::%d:Failed to init eventName\n`
- `API calls`
- `virtual void CoreAnalyticsTestUserClient::stop(IOService *)`
- `%s::%d:CoreAnalyticsHub start completed\n`
- `%s::%d:Fail to allocate _dictOfEvents\n`
- `void CoreAnalyticsEventRatePolicy::sendBudgetExceededReport()`
- `ca.queue`
- `IOReturn CoreAnalyticsHub::setupNewUserClient(task_t, void *, UInt32, OSDictionary *, IOUserClient *)`
- `%s::%d:core_analytics_hub not found\n`
- `Pending Retained Items`
- `Serialized Message Too Large`
- `%s::%d:Failed to allocate budgetDicts\n`
- `%s::%d:Failed to add _nagTimer to workloop\n`
- `com.apple.coreanalytics.kernel.verifyOversized`
- `EventName Failed`
- `%s::%d: _hub not found\n`
- `static IOReturn CoreAnalyticsUserClient::goto_configureFilter(CoreAnalyticsUserClient *, void *, IOExternalMethodArguments *)`
- `virtual void CoreAnalyticsUserClient::stop(IOService *)`
- `virtual IOReturn CoreAnalyticsUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `12112211`
- `%s::%d:Failed to add _eventRateMeasurementSpanTimer to workloop\n`
- `%s::%d:Setting max queue length %d\n`
- `API accepted`
- `MessageClient Sent`
- `virtual void CoreAnalyticsTestUserClient::free()`
- `%s::%d:%s::%s bad _workloop\n`
- `%s::%d:Failed to set newCount for %s\n`
- `%s::%d:Failed to add _demoTimer to workloop\n`
- `Serialized Message Bytes`
- `User Client IO`
- `EventName API Rate Exceeded`
- `_value`
- `virtual IOReturn CoreAnalyticsUserClient::registerNotificationPort(mach_port_t, UInt32, io_user_reference_t)`
- `%s::%d:Failed to create _reporters\n`
- `site.CoreAnalyticsMessenger`
- `bool CoreAnalyticsPipe::initWithParams(Params)`
- `site.workItem_t`
- `virtual void CoreAnalyticsUserClient::free()`
- `CoreAnalyticsEventRatePolicy`
- `IOReturn CoreAnalyticsHub::sendUpEventAndPayload(OSString *, OSObject *)`
- `void CoreAnalyticsHub::incrementEventNameRateLimit(OSString *)`
- `void CoreAnalyticsHub::testDemoOversizedMessage()`
- `virtual IOReturn CoreAnalyticsUserClient::clientMemoryForType(UInt32, IOOptionBits *, IOMemoryDescriptor **)`
- `EventName SerializeTooLarge`
- `site.CoreAnalyticsTestUserClient`
- `%s::%d:done\n`
- `%s::%d: Failed to set initWithTask\n`
- `void CoreAnalyticsHub::incrementEventNameSerializeFailure(OSString *)`
- `%s::%d:%s::%s bad _provider\n`
- `virtual bool CoreAnalyticsTestUserClient::start(IOService *)`
- `uint32_t CoreAnalyticsEventRatePolicy::incrementCountForEvent(OSString *)`
- `%s::%d:CoreAnalyticsHub start\n`
- `%s`
- `%s::%d:Failed to init dictKey[%d]\n`
- `CoreAnalyticsTestUserClient`
- `site.CoreAnalyticsEventRatePolicy`
- `%s::%d:Failed to allocate dictIter\n`
- `%s::%d:Failed to add _userClientRetryTimer to workloop\n`
- `%s::%d:CoreAnalyticsHub stop\n`
- `UserClient Closed`
- `virtual IOReturn CoreAnalyticsTestUserClient::clientDied()`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod bad selector %d\n`
- `%s::%d:Failed to createDefaultReportersAndLegend\n`
- `1211111212221212111111111111`
- `%s::%d: Failed to super::start\n`
- `virtual IOReturn CoreAnalyticsTestUserClient::clientClose()`
- `%s::%d:Failed to allocate arrayIter\n`
- `site.CoreAnalyticsHub`
- `void CoreAnalyticsHub::incrementEventNameSharedDataQueueFull(OSString *)`
- `121111121222121211`
- `%s::%d:%s::%s bad _maxQueueLen\n`
- `virtual bool CoreAnalyticsPipe::checkForWork()`
- `virtual bool CoreAnalyticsTestUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `virtual bool CoreAnalyticsUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `bool analytics_send_event_lazy(IOService *, OSString *, OSObject *)`
- `Hub Stats`
- `IOClass`
- `_channel`
- `IOReturn CoreAnalyticsUserClient::sendDataToUser(uint8_t *, size_t)`
- `com.apple.iokit.CoreAnalytics.user`
- `uint64_t CoreAnalyticsHub::getIndexForEventName(OSString *)`
- `%s::%d:%s::%s bad _callbackTarget\n`
- `virtual bool CoreAnalyticsTestUserClient::didTerminate(IOService *, IOOptionBits, bool *)`
- `%s::%d:CoreAnalyticsHub failed to successfully start\n`
- `void CoreAnalyticsHub::testDemoNormalMessage()`
- `Serializing Failures`
- `%s::%d: failed to alloc _queueLock\n`
- `virtual IOReturn CoreAnalyticsUserClient::clientClose()`
- `%s::%d:gCoreAnalyticsHub is NULL, returning kIOReturnNotReady\n`
- `%s::%d:_hub is NULL, returning kIOReturnNotReady\n`
- `site.CoreAnalyticsPipe`
- `%s::%d:Failed to create dataQueue\n`
- `bool%d`
- `CAChannel1`
- `UserClient Launches`
- `%s::%d:%s::%s bad _startRetrytTimer\n`
- `%s::%d: %s is not entitled\n`
- `bool CoreAnalyticsUserClient::checkEntitlement(task_t)`
- `%s::%d:Failed to allocate budgetDict\n`
- `void CoreAnalyticsHub::incrementEventNameFailed(OSString *)`
- `void CoreAnalyticsEventRatePolicy::zeroOutPerEventCounts()`
- `%s::%d:Failed to create workloop\n`
- `bool CoreAnalyticsPipe::enqueueEventAndPayload(OSString *, OSObject *)`
- `%s::%d:%s::%s Failed to malloc workItem_t\n`
- `%s::%d:Failed to create _eventNameIndex\n`
- `%s::%d:Failed to add commandGate to workloop\n`
- `%s::%d:Failed to make _ratePolicy\n`
- `Shared Data Queue full, retry`
- `Serialized Messages`
- `1111`
- `1211111212221212111111111111111211`
- `%s::%d:Failed to IOSetCoreAnalyticsSendEventProc\n`
- `%s::%d:Overriding default rate limit policy of %ums with ca.ratespan of %dms\n`
- `%s::%d:Failed to create _userClientLock\n`
- `%s::%d:Failed to call super::start\n`
- `enqueueEventAndPayload`
- `%s::%d:failed\n`
- `void CoreAnalyticsEventRatePolicy::createBudgetDicts(OSArray *) const`
- `virtual bool CoreAnalyticsHub::start(IOService *)`
- `%s::%d:Failed to add dataQueue to workloop\n`
- `ca.interval`
- `%s::%d:Failed to init dictData[%d]\n`
- `virtual bool CoreAnalyticsMessenger::attach(IOService *)`
- `121112111111121111121`
- `%s::%d:Failed to create _eventNameIndexLock\n`
- `%s::%d:CoreAnalyticsHub free\n`
- `void CoreAnalyticsHub::incrementEventNameReceived(OSString *)`
- `void CoreAnalyticsHub::handleNagTimerExpiry(IOTimerEventSource *)`
- `int%d`
- `API per-event rate exceeded`
- `virtual void CoreAnalyticsMessenger::detach(IOService *)`
- `%s::%d:%s::%s bad _isClientAlive\n`
- `void CoreAnalyticsHub::handleUserClientRetryTimerExpiry(IOTimerEventSource *)`
- `com.apple.coreanalytics.kernel.test`
- `%s::%d:unregistering from _hub...\n`

**[__TEXT.__os_log]**

- `%s::%d:Failed to add _eventNameReceived for %s\n`
- `%s::%d: Not Implemented yet\n`
- `%s::%d:Failed to add _eventRateMeasurementSpanTimer to workloop\n`
- `%s::%d:Setting max queue length %d\n`
- `%s::%d:Failed to store _eventNameReceived\n`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod bad selector %d\n`
- `%s::%d: couldn't get memory descriptor\n`
- `%s::%d:CoreAnalyticsSendEvent failed for eventName %s\n`
- `%s::%d:clientClose\n`
- `%s::%d:Failed to add _userClientRetryTimer to workloop\n`
- `%s::%d:Failed to create _reporters\n`
- `%s::%d:Failed to add new eventName %s\n`
- `%s::%d:Failed to get count for %s\n`
- `%s::%d:Failed to allocate budgetDicts\n`
- `%s::%d:Failed to add _eventNameFailed for %s\n`
- `%s::%d:Failed to create _eventNameReceived\n`
- `%s::%d:attaching`
- `%s::%d:%s::%s bad _sender\n`
- `%s::%d:%s::%s bad _workloop\n`
- `%s::%d:Failed to create _eventNameIndex\n`
- `%s::%d:Already open\n`
- `%s::%d:failed to start userClient\n`
- `%s::%d:Failed to init eventPayload\n`
- `%s::%d:Failed to allocate dictIter\n`
- `%s::%d:Failed to add budgetDict to array\n`
- `%s::%d:Failed to create _eventNameAPIRateExceeded\n`
- `%s::%d:Failed to store _eventNameSharedDataQueueFull\n`
- `%s::%d:Failed to store _eventNameSerializeTooLarge\n`
- `%s::%d: _hub not found\n`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod invalid payload\n`
- `%s::%d:CoreAnalyticsUserClient::didTerminate\n`
- `%s::%d:gCoreAnalyticsHub is NULL, returning kIOReturnNotReady\n`
- `%s::%d:%s::%s bad _nag\n`
- `%s::%d:Failed to allocate event\n`
- `%s::%d:Failed to allocate budgetDict\n`
- `%s::%d:Failed to send IOCoreAnalyticsSendEvent\n`
- `%s::%d:Failed to alloc KernelMessage\n`
- `%s::%d:Overriding default count limit for rate limit policy of %d with ca.maxcount of %d\n`
- `%s::%d:Failed to IOSetCoreAnalyticsSendEventProc\n`
- `%s::%d:CoreAnalyticsHub free\n`
- `%s::%d:Failed to store _eventNameFailed\n`
- `%s::%d:Failed to init dictData[%d]\n`
- `%s::%d:Event Sendup Failed %s : %s\n`
- `%s::%d:Failed to create _eventNameFailed\n`
- `%s::%d:Failed to create _eventNameSharedDataQueueFull\n`
- `%s::%d:Failed to create _fieldCounters\n`
- `%s::%d:CoreAnalyticsTestUserClient::externalMethod failed to unserialize xml`
- `%s::%d: request for unsupported memory type %u\n`
- `%s::%d:Invalid type (%u) specified`
- `%s::%d:Failed to init eventName\n`
- `%s::%d:Failed to add dataQueue to workloop\n`
- `%s::%d:%s::%s bad _startRetrytTimer\n`
- `%s::%d:Failed to make _ratePolicy\n`
- `%s::%d:Failed to createDefaultReportersAndLegend\n`
- `%s::%d:Failed to create iter\n`
- `%s::%d:Failed to store _eventNameAPIRateExceeded\n`
- `%s::%d: Failed to super::start\n`
- `%s::%d: failed checkEntitlement\n`
- `%s::%d:Failed to create _userClientLock\n`
- `%s::%d:Successfully opened\n`
- `%s::%d:Couldn't start\n`
- `%s::%d:Failed to alloc OSSerialize\n`
- `%s::%d:Failed to create workloop\n`
- `%s::%d:Failed to serialize\n`
- `%s::%d:Unsupported Type\n`
- `%s::%d:Failed to add _eventNameSharedDataQueueFull for %s\n`
- `%s::%d:Failed to create _eventRateMeasurementSpanTimer\n`
- `%s::%d:Fail to allocate _dictOfEvents\n`
- `%s::%d: _hub or _dataQueue invalid, dropping\n`
- `%s::%d:Failed to create _eventNameIndexLock\n`
- `%s::%d:Testing Oversized Event Messages\n`
- `%s::%d:unregistering from _hub, and clearing _hub reference to CoreAnalyticsUserClient\n`
- `%s::%d:Failed to allocate overage\n`
- `%s::%d:clearing userClient\n`
- `%s::%d:Failed to add _eventNameSerializeTooLarge for %s\n`
- `%s::%d:Failed to add _eventNameSerializeFailure for %s\n`
- `%s::%d:%s::%s Failed to malloc workItem_t\n`
- `%s::%d:done\n`
- `%s::%d: queue full, requeueing\n`
- `%s::%d:Failed to allocate overageCountKey\n`
- `%s::%d:Couldn't initWithTask\n`
- `%s::%d:Failed to create _eventNameSerializeFailure\n`
- `%s::%d:messageClients of %d available events\n`
- `%s::%d:starting CoreAnalyticsMessenger\n`
- `%s::%d:%s::%s bad _provider\n`
- `%s::%d:Failed to set newCount for %s\n`
- `%s::%d:Failed to store _eventNameSerializeFailure\n`
- `%s::%d:startMessage\n`
- `%s::%d:success\n`
- `%s::%d: Failed to make _dataQueue\n`
- `%s::%d:CoreAnalyticsUserClient::registerNotificationPort _notificationPort is unexpectedly already set\n`
- `%s::%d: got memory descriptor with %d\n`
- `%s::%d:CoreAnalyticsHub stop\n`
- `%s::%d:Couldn't attach\n`
- `%s::%d:Failed to serialize eventPayload\n`
- `%s::%d:Failed to store _fieldCounters\n`
- `%s::%d:Overriding default rate limit policy of %ums with ca.ratespan of %dms\n`
- `%s::%d:adding userClient\n`
- `%s::%d:Failed to store _hubCounters\n`
- `%s::%d:Failed to allocate eventNameKey\n`
- `%s::%d:Failed to set budgetDict overageCountKey\n`
- `%s::%d:event %s overage count %d\n`
- `%s::%d:Failed to add _nagTimer to workloop\n`
- `%s::%d:event %s count %d\n`
- `%s::%d:%s::%s Queue length max met %d, dropping\n`
- `%s::%d:Failed to allocate budgetBreakerEventName\n`
- `%s::%d:close\n`
- `%s::%d:Failed to create _eventNameSerializeTooLarge\n`
- `%s::%d:_hub is NULL, returning kIOReturnNotReady\n`
- `%s::%d: failed to alloc _queueLock\n`
- `%s::%d:CoreAnalyticsHub failed to successfully start\n`
- `%s::%d:detaching\n`
- `%s::%d: %s is not entitled\n`
- `%s::%d:failed\n`
- `%s::%d:Failed to create commandgate\n`
- `%s::%d:Failed to add commandGate to workloop\n`
- `%s::%d:Serialized data too large, dropping event with eventName %s\n`
- `%s::%d:Failed to add _eventNameAPIRateExceeded for %s\n`
- `%s::%d:%s::%s bad _isClientAlive\n`
- `%s::%d:unregistering from _hub...\n`
- `%s::%d:CoreAnalyticsTestUserClient::didTerminate\n`
- `%s::%d:Failed to create dataQueue\n`
- `%s::%d:Failed to add _demoTimer to workloop\n`
- `%s::%d:Testing Normal Event Messages\n`
- `%s::%d:core_analytics_hub not found\n`
- `%s::%d:%s::%s bad _maxQueueLen\n`
- `%s::%d: Failed to set initWithTask\n`
- `%s::%d:external clientDied\n`
- `%s::%d: failed to alloc _lock\n`
- `%s::%d:CoreAnalyticsHub start completed\n`
- `%s::%d:Retry UserClient sendup due to due previous kIOReturnNoSpace\n`
- `%s::%d:Failed to init dictKey[%d]\n`
- `%s::%d:Failed to attach\n`
- `%s::%d:%s::%s bad _callbackTarget\n`
- `%s::%d:Couldn't create\n`
- `%s::%d:Failed to create _hubCounters\n`
- `%s::%d:CoreAnalyticsUserClient::externalMethod bad selector %d\n`
- `%s::%d: sending %zu bytes\n`
- `%s::%d: failed to alloc _dictLock\n`
- `%s::%d:Failed to set budgetDict eventNameKey\n`
- `%s::%d:Failed to allocate arrayIter\n`
- `%s::%d:CoreAnalyticsHub start\n`
- `%s::%d:Failed to call super::start\n`
- `%s::%d:Waiting %dms before producing CoreAnalytic message every %dms\n`
