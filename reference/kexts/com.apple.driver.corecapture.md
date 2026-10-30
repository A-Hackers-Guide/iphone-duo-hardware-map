# `com.apple.driver.corecapture`

- Name: corecapture
- Version: `1.0.4`
- UUID: `C4B6E78A-789C-3C7D-96FB-02FBCF558276`
- Source version: `1355.45.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (21) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `CCCapture` | 0x90 | IOService → IORegistryEntry |
| `CCDataPipe` | 0x98 | CCPipe → IOService → IORegistryEntry |
| `CCDataPipeBlob` | 0x18 |  |
| `CCDataPipeBlobMD` | 0x20 | CCDataPipeBlob |
| `CCDataPipeBlobOD` | 0x20 | CCDataPipeBlob |
| `CCDataPipeBlobOS` | 0x20 | CCDataPipeBlob |
| `CCDataPipeUserClient` | 0xe8 | CCPipeUserClient → IOUserClient → IOService → IORegistryEntry |
| `CCDataSession` | 0x28 |  |
| `CCDataStream` | 0x98 | CCStream → IOService → IORegistryEntry |
| `CCFaultReport` | 0x28 | IOCommand |
| `CCFaultReporter` | 0x90 | IOService → IORegistryEntry |
| `CCIOReporterDataStream` | 0xa0 | CCDataStream → CCStream → IOService → IORegistryEntry |
| `CCIOReporterHub` | 0x90 | IOService → IORegistryEntry |
| `CCIOReporterLogStream` | 0xa0 | CCLogStream → CCStream → IOService → IORegistryEntry |
| `CCIOService` | 0x88 | IOService → IORegistryEntry |
| `CCLogPipe` | 0x98 | CCPipe → IOService → IORegistryEntry |
| `CCLogPipeUserClient` | 0xe0 | CCPipeUserClient → IOUserClient → IOService → IORegistryEntry |
| `CCLogStream` | 0x98 | CCStream → IOService → IORegistryEntry |
| `CCPipe` | 0x90 | IOService → IORegistryEntry |
| `CCPipeUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `CCStream` | 0x90 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00007074 off=0x00dfb650-0x00e026c4 addr=0xfffffe0007dff650-0xfffffe0007e066c4 r--/r--   __TEXT            
	sz=0x000047bc off=0x00dfbd68-0x00e00524 addr=0xfffffe0007dffd68-0xfffffe0007e04524               __TEXT.__os_log           
	sz=0x00000110 off=0x00e00530-0x00e00640 addr=0xfffffe0007e04530-0xfffffe0007e04640               __TEXT.__const            
	sz=0x00002084 off=0x00e00640-0x00e026c4 addr=0xfffffe0007e04640-0xfffffe0007e066c4               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00027fd0 off=0x03b00240-0x03b28210 addr=0xfffffe000ab04240-0xfffffe000ab2c210 r-x/r-x   __TEXT_EXEC       
	sz=0x00027880 off=0x03b00240-0x03b27ac0 addr=0xfffffe000ab04240-0xfffffe000ab2bac0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000750 off=0x03b27ac0-0x03b28210 addr=0xfffffe000ab2bac0-0xfffffe000ab2c210          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000067c off=0x04a37480-0x04a37afc addr=0xfffffe000ba3b480-0xfffffe000ba3bafc rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04a37480-0x04a37544 addr=0xfffffe000ba3b480-0xfffffe000ba3b544               __DATA.__data             
	sz=0x00000308 off=0x00000000-0x00000308 addr=0xfffffe000ba3b548-0xfffffe000ba3b850               __DATA.__common           (Zerofill)
	sz=0x000002ac off=0x00000000-0x000002ac addr=0xfffffe000ba3b850-0xfffffe000ba3bafc               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000086f8 off=0x014b2708-0x014bae00 addr=0xfffffe00084b6708-0xfffffe00084bee00 rw-/rw-   __DATA_CONST      
	sz=0x00000088 off=0x014b2708-0x014b2790 addr=0xfffffe00084b6708-0xfffffe00084b6790         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000080 off=0x014b2790-0x014b2810 addr=0xfffffe00084b6790-0xfffffe00084b6810         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00007010 off=0x014b2810-0x014b9820 addr=0xfffffe00084b6810-0xfffffe00084bd820         __DATA_CONST.__const            
	sz=0x000010c0 off=0x014b9820-0x014ba8e0 addr=0xfffffe00084bd820-0xfffffe00084be8e0         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x014ba8e0-0x014ba980 addr=0xfffffe00084be8e0-0xfffffe00084be980         __DATA_CONST.__kalloc_var       
	sz=0x000003a8 off=0x014ba980-0x014bad28 addr=0xfffffe00084be980-0xfffffe00084bed28         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d8 off=0x014bad28-0x014bae00 addr=0xfffffe00084bed28-0xfffffe00084bee00         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 261 at 0x04affc48
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     C4B6E78A-789C-3C7D-96FB-02FBCF558276
008: LC_SOURCE_VERSION           1355.45.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004acdec0 size=0x478
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `corecapture`
- `CFBundleIdentifier`: `com.apple.driver.corecapture`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `corecapture`
- `CFBundleNumericVersion`: `17072128`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2008-2009 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Network-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/corecapture.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891137456`
- `_PrelinkExecutableRelativePath`: `corecapture`
- `_PrelinkExecutableSize`: `228792`
- `_PrelinkExecutableSourceAddr`: `-2198891137456`
- `_PrelinkKmodInfo`: `-2198827977600`

## Strings (679) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `Bad arrayOfLegendChannels\n`
- `Fail: Could not save %s as dict, retval 0x%x\n`
- `%s::%s(): failed to attach\n`
- `%s::%s CCStreamLogLevel:%d ccLevel:%d\n`
- `%s::%s() Failed to set property dictionary Owner:%s Pipe:%s\n`
- `CCPipe::createReportersAndLegend failed tp create ivars->fCoreCapturePipeReporter %p`
- `No matches found for %s\n`
- `%s FAILED - channelCount overflow!\n`
- `%s::%s(): Failed to create fCoreCaptureReporter\n`
- `%s - No ivars->_hub found yet\n`
- `CCLogPipe::setStreamLogLevel - Unknown Stream %s\n`
- `CCLogPipe::setStreamConsoleLogFlags - Unknown Stream %s\n`
- `Couldn't make IOReportStreamArrayDict\n`
- `CCDataPipeUserClient::externalMethodGated Unexpected selector %d value\n`
- `Failed to process extraFiles\n`
- `CoreCapture logging throttled for fault %llu:%llu - %s\n`
- `Bad ivars->_interestBuffers\n`
- `Failed to create ring MD Owner:%s Pipe:%s\n`
- `%s::%s(): CCFlags is overriden %s\n`
- `CCLogStream::logHeaderAndMbuf - Comment too long (%d)\n`
- `%s::%s() Failed to createReportersAndLegend\n`
- `Couldn't create dict\n`
- `%llu.%llu\t %s\n`
- `%s - No ivars->_interestLists or ivars->_interestBuffers\n`
- `CCLogPipe::updateStreamLogFlags - Unknown Stream %s\n`
- `%s::%s: invalid stream log level %d\n`
- `%s::%s():Failed to set CC Flag property (%llx) \n`
- `[IOKit] entitlement check failed\n`
- `%s::%s():  failed super init\n`
- `Looking for num %lld found %lld \n`
- `Missing ivars in %s\n`
- `CCLogPipe::setStreamConsoleLogFlags stream:%s flags: 0x%llx\n`
- `%s::%s:%d Owner: %s Name: %s LogIdentifier: %s`
- `%s::%s() Done Creating Legend for owner: %s pipe %s\n`
- `%s::%s():Failed to set stream ID property (%u) \n`
- `CCLogPipe::capture pipe not ready for capture owner: %s pipe %s\n`
- `%s::%s() retVal:%d:\n`
- `Failed to create fPipeName\n`
- `Couldn't find %s\n`
- `IOMallocType failed Owner:%s Pipe:%s\n`
- `CCDataPipe::enqueueBlob queue full, dropping blob: %s session: %s Owner: %s Name: %s queueSize: %zu maxSize: %zu`
- `%s:%d Invalid Key in Dictionary`
- `Done calling all deferred capture callbacks\n`
- `Failed to create dictionary from unpublished legend\n`
- `%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd)\n`
- `%s does not have immediate callback\n`
- `Couldnt find tmpMemory %d or interestsDict %d\n`
- `%s::%s(): NumberOfFiles is overriden %s\n`
- `Release mach port %llu\n`
- `%s::%s(): super failed to init!\n`
- `Done calling all complete report callbacks\n`
- `Callback %s is not inGate!!!\n`
- `%s::%s(): Min Log Size To Notify(%zd) is greater than Log Size(%zd) Owner:%s Pipe:%s\n`
- `CCLogPipe::setStreamLogFlags Flags: 0x%llx\n`
- `CCLogStream::initWithPipeAndName failed setIORegistry\n`
- `Couldn't make subIdxNum\n`
- `Failed to find %s\n`
- `%s failed\n`
- `%s::%s()\n`
- `triggerCoreCapture: Unexpected typeID %p\n`
- `%s - _createInterestsDictionary() failed\n`
- `CCIOService::%s Found %d streams > %d`
- `%s FAILED - alloc clist!\n`
- `memory allocation failed`
- `CCFaultReporter: Failed to create properties dictionary\n`
- `%s::%s():Failed to set pipe Log type property (%d) Owner:%s Pipe:%s\n`
- `%s: driver %llx idx = %d, channelCount = %u\n`
- `CCLogPipe::log - Required size (%zu) is greater than max (%zu)\n`
- `CCLogPipe::capture Failed notify user client for owner: %s pipe: %s\n`
- `%s::%s(): \n`
- `%s - ivars->_hub->getReportBufferSize(): %x`
- `invoke %s complete report callback\n`
- `%s::%s(): LogPolicy is overriden %s\n`
- `%s::%s(): Failed to add CCCapture nub\n`
- `_copyServiceGetChannels returned error\n`
- `Not appending. Bail.\n`
- `%s does not have deferred capture callback\n`
- `%s::%s():Failed to set pipe policy property (%d)\n`
- `bufSize >= totalSize\n`
- `Couldn't make return dictionary\n`
- `CCDataPipe::notifyTimeout Failed notify user client for owner: %s pipe: %s \n`
- `Fail: Missing argument - OSSerialize (%s) OSDictionary (%s)\n`
- `%s::%s(): Pipe size resolved to zero Owner:%s Pipe:%s\n`
- `%s::%s:invalid stream log level %d\n`
- `%s::%s(): Invalid log policy - %d\n`
- `%s::%s(): Failed to attach\n`
- `%s::%s(): MinLogSizeToNotify is overriden %s\n`
- `%s::%s():Failed to set pipe type property (%d) Owner:%s Pipe:%s\n`
- `CCDataPipe::stop Owner: %s Name: %s enqueued: %llu dequeued: %llu dropped: %llu`
- `Failed to add %s. Break.\n`
- `!!! Someone broke ivars->_CCIOReportRootDict %p, doesnt contain %s\n`
- `%s::%s(): Invalid Boot_Arg[%d] %s`
- `CCFaultReporter: Failed to create service name string\n`
- `%s core capture enable %d\n`
- `CCLogStream::%s: invalid stream log level %d\n`
- `CCLogStream::initWithPipeAndName failed CCStream init\n`
- `IOLockAlloc failed\n`
- `Failed to create interestDict\n`
- `%s::%s:%d logFlags:0x%llx`
- `CCLogStream::profileLoaded failed setIORegistry\n`
- `CCLogStream::profileRemoved failed setIORegistry\n`
- `Couldn't find chChannel\n`
- `%s PREPARE REPORT FAILED %x\n`
- `Failed to add History.txt\n`
- `Failed to collected immediate data for report\n`
- `CCLogPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n`
- `%s::%s(): Invalid log type - %d Owner:%s Pipe:%s\n`
- `%s::%s(): Failed to attach log pipe %s to %s\n`
- `%s objType:%d `
- `Failed to create interestList\n`
- `CCLogPipe::updateLogFlags: Unknown flag action\n`
- `%s::%s():Failed to set CC Level property (%d) \n`
- `CCLogStream::logHeaderAndBuf - Comment too long (%d)\n`
- `%s::%s(): Boot-Arg Key: %s, Value=%s\n`
- `%s FAILED - alloc interestsDict!\n`
- `CCPipe::initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n`
- `CCDataPipe::notifyTimeout notification sent user client for owner: %s pipe: %s\n`
- `%s - ERROR for index %lld`
- `%s::%s(): Boot-Arg cc.debug.CollectLogAtLowPriority, Value=%d\n`
- `fail to record History [%lld] %s\n`
- `%s - ERROR loging results for subscription %lld, %s\n`
- `Maformed CCIOReportInterestsDict %d %d\n`
- `%s COMPLETE REPORT FAILED %x\n`
- `%s - No ivars->_hub attached\n`
- `%s - Failed to get subscription number\n`
- `%s::%s() ring buffer allocation is deferred\n`
- `CCPipe::withOwnerNameCapacity Unsupported pipe type(%d) \n`
- `%s::%s(): CCCapture object already exists. Bail.\n`
- `bad ioReportChannels\n`
- `bad channels\n`
- `CCIOService::%s:%d Unexpected type children for Pipe, expected CCIOService`
- `No Service found %llx\n`
- `Failed to configure interests\n`
- `Failed to create newInterestArray\n`
- `IOMallocType failed\n`
- `%s::%s(): LogType is overriden %s\n`
- `Failed to create fPipeOwner\n`
- `%s::%s  startPipe fail`
- `Created CCDataStream (Name: %s)\n`
- `reason string is not updated during report fault`
- `%06llu.%06llu %s.%c[%lu] %s`
- `%s::%s(): CCLevel is overriden %s\n`
- `Failed to create Notify timer\n`
- `Fault reporter is busy - Active: %s - New request: %s\n`
- `%s::%s():Failed to set pipe file name property (%s) Owner:%s Pipe:%s\n`
- `%s - No ivars->_hub attached`
- `fail to record addFile %s\n`
- `no in progress fault reporter and reason string can't be updated`
- `%s::%s(): ConsoleFlags is overriden %s\n`
- `CCDataPipe::capture pipe not ready for capture owner: %s pipe %s\n`
- `collect deferred data %d\n`
- `%s DEFERRED CAPTURE FAILED %x\n`
- `Failed to create iterator for extraFiles\n`
- `Bad ivars->_interestLists\n`
- `%s::%s(): initWithOwnerNameCapacity failed Owner:%s Pipe:%s\n`
- `%s::%s():Failed to set pipe owner property (%s) Owner:%s Pipe:%s\n`
- `%s - _createInterestsDictionary() failed`
- `empty file data`
- `CCLogStream::initWithPipeAndName requires valid stream options\n`
- `%s::%s:%d flags:0x%llx`
- `%s::%s:%d flag:0x%llx`
- `%s::%s():Failed to set total file size property (%u) Owner:%s Pipe:%s\n`
- `%s::%s():Failed to set pipe file option flags property (%u) Owner:%s Pipe:%s\n`
- `%s - No ivars->_hub found yet`
- `invalid argument`
- `Done calling all prepare report callbacks\n`
- `Begin calling all immediate callbacks\n`
- `Failed to add FaultReportState.txt\n`
- `%s - failed to getValues for interests for subscription %lld, %s\n`
- `%s FAILED - validate channelCount!\n`
- `Warning: driver->Copy[ReportChannelData] failed\n`
- `Examine (%d of %d) - %s\n`
- `%s::%s() failed to cast hub on %s \n`
- `%s - ivars->_hub->getReportBufferSize(): %x\n`
- `Unexpected memory descriptor typeId\n`
- `%s::%s():Failed to set Min Log Size To Notify property (%zd)\n`
- `Begin calling all deferred capture callbacks\n`
- `Someone changed state@readPtr %d.\n`
- `%s::%s():Failed to set CC Flag property (%llu) \n`
- `%s::%s(): Unknown arg[%d] Value is %s\n`
- `%s::%s(): Failed to start log pipe\n`
- `bad channelID, or value is 0\n`
- `Couldn't make new rootDict\n`
- `Mach port %llu release failed\n`
- `%s alloc fail`
- `collect immediate data %d\n`
- `Failed to prepare the report\n`
- `%s::%s() IOReporters setup for %s\n`
- `CCIOReporterDataStream::getIOReporterDictionaryForSubscription %s empty\n`
- `Couldn't find %s in ioReportStreamDict\n`
- `%s::%s(): Failed to start log pipe %s\n`
- `Updating a reason string failed`
- `CCIOReporterLogStream::addSubscriptionForThisReporter failed - Need groupName and subGroupName\n`
- `CCLogPipe::setStreamLogLevel stream:%s Level: 0x%x\n`
- `%s:%06u: ERROR: Return code not sucessfull [%08x]\n`
- `%s No valid objType in Dictionary:%d`
- `Force panic for %x\n`
- `creating a history string failed for %s`
- `Subscription not found for sub1 %d sub2 %d\n`
- `%s::%s(): Pipe is not started. Bail.\n`
- `%s::%s(): super::start( provider ) failed\n`
- `Failed to create matching dictionary\n`
- `IOLockAlloc failed Owner:%s Pipe:%s\n`
- `%s does not have complete report callback\n`
- `invalid report\n`
- `Failed to create ring buffer Owner:%s Pipe:%s\n`
- `CCLogPipe::notifyUserSpace capture notification dropped - no user client for owner: %s pipe: %s\n`
- `%s::%s():Failed to set pipe compression property (%d) Owner:%s Pipe:%s\n`
- `%s::%s() streamName %s\n`
- `%s::%s():  failed to get ivars->_hub\n`
- `%s::%s() super::start(provider) failed\n`
- `dumping to disk has started and reason string can not be modified`
- `%s::%s Invalid ivars`
- `Couldn't find channelNumber\n`
- ` Unable to create timer for deferred data collection\n`
- `invoke %s immediate callback\n`
- `%s:%d Unknown Stream %s\n`
- `%s::%s():Failed to set pipe size property (%zd) Owner:%s Pipe:%s\n`
- `%s::%s():Failed to set unified log policy property (%d) Owner:%s Pipe:%s\n`
- `%s::%s:%d Name: %s LogIdentifier: %s`
- `CCLogPipe::setStreamConsoleLogLevel - Unknown Stream %s\n`
- `CCLogPipeUserClient::setPipeStreamLogFlags stream: %s, flags: 0x%llx\n`
- `Dropping log of size %ld larger than max allowable of size %ld\n`
- `(%s) super::init failed\n`
- `bad sub, malformed rootDict\n`
- `%s FAILED - missing channels!\n`
- `CCDataPipe::capture No privilege, not capturing owner: %s pipe %s\n`
- `Failed to create lock Owner:%s Pipe:%s\n`
- `CCLogPipe::updateStreamLogFlags stream:%s flags: 0x%s\n`
- `scratchBuffer\n`
- `Bad arrayWithinIOReportLegend\n`
- `CCFaultReport::initWithFaultInfo called with 0 length functionName\n`
- `Done calling all immediate callbacks\n`
- `CCLogPipe::setStreamConsoleLogLevel: stream:%s level:%u\n`
- `Created CCLogStream (Name: %s)\n`
- `%s::%s(): Terminating CCCapture object\n`
- `%s - %s > INT_MAX / sizeof(%s)!`
- `missing argument\n`
- `%s::%s():Failed to set pipe policy property (%d) Owner:%s Pipe:%s\n`
- `%s::%s(): NotifyTimeout is overriden %s\n`
- `%s::%s():Failed to set Min Log Size To Notify property (%zd) Owner:%s Pipe:%s\n`
- `dumping to disk is disabled\n`
- `%s::%s():Failed to set pipe directory name property (%s) Owner:%s Pipe:%s\n`
- `%d extraFiles\n`
- `%s::%s():Failed to set notify timeout property (%u)\n`
- `%s::%s(): FileSize is overriden %s\n`
- `ivars->_CCIOReportRootDict, size %d\n`
- `Fail: Could not save %s as data, retval 0x%x, pMem %p, len %zu\n`
- `%s %p \t\tpriority %d\n`
- `Begin calling all prepare report callbacks\n`
- `%s COLLECT IMMEDIATE FAILED %x\n`
- `Cannot extract data for %s\n`
- `%s::%s():Failed to set notify timeout property (%u) Owner:%s Pipe:%s\n`
- `Failed to make return interest dictonary\n`
- `Couldn't find channelType\n`
- `Couldn't find %s in ivars->_CCIOReportRootDict\n`
- `Set Action to %x\n`
- `Fail: Could not save %s as data, retval 0x%x, dat %p, len %zu\n`
- `%s:%d Invalid Obj type in Dictionary`
- `[FaultReporter] will watchdog due to: %s \n`
- `%s FAILED - alloc tmpData!\n`
- `CCDataPipe::withOwnerNameCapacity: Invalid pipe type(%d)\n`
- `%s does not have prepare callback\n`
- `Couldnt find sub %lld interestListDict %d or interestBufferDict %d\n`
- `Failed to find %s in driver\n`
- `Failed to create scratch bufferes Owner:%s Pipe:%s\n`
- `CCLogPipe::getMemoryDescriptor mapPipe(0) failed rv:0x%x map:%p owner:%s pipe:%s`
- `CCLogPipe::updateStreamConsoleLogFlags stream:%s flags: 0x%s\n`
- `%s::%s():Failed to set total file number property (%u) Owner:%s Pipe:%s\n`
- `CCPipe::publishStatistics():%06d - No memory\n`
- `Failed !chID || !chType || !chName\n`
- `CCFaultReporter::callCompleteReportCallbacks already completed, skipping\n`
- `%s::%s(): Invalid log policy - %d Owner:%s Pipe:%s\n`
- `%s::%s(): Log Size must be non-zero Owner:%s Pipe:%s\n`
- `%s::%s(): Failed to get log policy - %d\n`
- `CCFaultReport::initWithFaultInfo called with 0 length fileName\n`
- `invalid summary and reason string lengths`
- `too long summary string`
- `%s::%s:%d level:%d`
- `CCPipe::initWithOwnerNameCapacity Failed to create CoreCapture IORegistry plane\n`
- `%s::%s():Failed to set stream log identifier property (%s) \n`
- `Failed to create ring state Owner:%s Pipe:%s\n`
- `CCLogPipe::updateStreamConsoleLogFlags - Unknown Stream %s\n`
- `CCLogPipe::capture No privilege, not capturing owner: %s pipe %s\n`
- `generateOptionPacket - Insufficient room to add opt_endofopt to this buffer in subsequent call (%zd)\n`
- `%s::%s():Failed to set pipe name property (%s) Owner:%s Pipe:%s\n`
- `missing pipeOptions\n`
- `missing pipeOptions Owner:%s Pipe:%s\n`
- `invoke %s prepare callback\n`
- `%s::%s():Failed to set pipe log identifier property (%s) Owner:%s Pipe:%s\n`
- `ERROR driver (%u) and channel (%u) array dimension mismatch!\n`
- `%s::%s():Failed to set Console Level property (%d) \n`
- `%s::%s() Failed to createReportSet\n`
- `bad channelType for ChannelID %lld\n`
- `%s::%s(): Unable to allocate provider\n`
- `Warning: service->...Get[Report]Dimensions failed\n`
- `Couldn't make OSDictionary\n`
- `Fail: Could not save %s as string, retval 0x%x\n`
- `CCFaultReporter enable is %d\n`
- `updateFile failed for %s`
- `%s::%s(): LogSize is overriden %s\n`
- `CCPipe::createReportersAndLegend no getReportersSet()`
- `%s::%s():Failed to set set property dictionary \n`
- `CCLogPipe::log -- Attempting to write outside ring buffer\n`
- `Failed opening CCLogPipeUserClient Owner:%s Pipe:%s\n`
- `Ignoring timer notification\n`
- `Couldn't find chDriver\n`
- `%s:%d Invalid key:|%s|`
- `FaultReporter is stopped\n`
- `No Channels\n`
- `Couldn't create newRootDictionary\n`
- `Someone changed readPtr %d->%d.\n`
- `%s::%s(): Failed to create ivars->fCoreCaptureReporter\n`
- `Unknown stream type\n`
- `%s::%s() failed to create ivars->_lock\n`
- `%s::%s(): ConsoleLevel is overriden %s\n`
- `%s - %s <= 0!`
- `Begin calling all complete report callbacks\n`
- `%s::%s(): Invalid log data type - %d Owner:%s Pipe:%s\n`
- `CCPipe::withOwnerNameCapacity pipeOwner %s pipeName %s\n`
- `%s::%s():Failed to set pipe data type property (%d) Owner:%s Pipe:%s\n`
- `Disabled. Bail.\n`
- `Unsupported, need to implement - for now provide the driverID where these reporters lie\n`
- `CCLogPipe::getMemoryDescriptor mapPipe(1) failed rv:0x%x map:%p owner:%s pipe:%s`
- `CCLogStream::initWithPipeAndName requires valid name\n`
- `Couldn't find %s in rootDict\n`
- `%s::%s():Failed to set stream name property (%s) \n`
- `recording %s\n`
- `%s - IOLockAlloc failed\n`
- `invoke %s deferred capture\n`
- `Bad interestArrayForSubscription2\n`
- `%s:%d pipe is stopped\n`
- `CCLogPipe::capture Failed to add capture event for owner: %s pipe: %s\n`
- `ERROR could not unpack interest dict\n`
- `empty file name`
- `pipe is not a CCDataPipe\n`
- `empty Client list!\n`
- `Created CCLogPipe (Owner: %s - Name: %s)\n`
- `%s::%s() Failed to create ivars->fRingBufferMap\n`
- `%s:%06u: ERROR: Return code not successful [%08x]\n`
- `%s::%s() fCoreCaptureReporter %p\n`
- `Created CCDataPipe (Owner: %s - Name: %s)\n`
- `%s::%s():Failed to set Console Flag property (%llx) \n`

**[__TEXT.__cstring]**

- `cc.debug.CollectLogAtLowPriority`
- `[%lld]%llu.%llu\t %s - Logged: %s\n`
- `enableCoreCapture`
- `CCIOReportLogStream`
- `111122222221112212222222221121`
- `cc.debug.pipe.statistics`
- `site.CCPipeUserClient`
- `site.CCDataStream`
- `site.CCPipe`
- `%s - unable to get valid iterator for ccKextPlane\n`
- `site.CCDataPipeUserClient`
- `122221111221111221111221111221111221111221111221111221111221111221111221111221111221111221111221111`
- `\"CCFaultReport::saveFileName called with 0 length fileName\" @%s:%d`
- `\n\nduration: %lld.%llds\n`
- `FileOptions`
- `initWithStreamWorkloop`
- `site.CCCapture`
- `allocCapture`
- `freeCCCaptureObject`
- `NumberOfFiles`
- `CCIOReporterLogStream`
- `site.struct CCRingState`
- `setPipeStreamLogFlags`
- `setConsoleLevel`
- `Dumped %d kext pipes owned by: %s\n`
- `%llu.%llu`
- ` Failed to create ivars->fRingStateMap\n`
- `\"Cannot resize in ring buffers\" @%s:%d`
- `Name`
- `CCLogPipeUserClient`
- `setPipeStreamLogLevel`
- `setConsoleLogFlag`
- `cc.internal.client`
- `updateReport`
- `watchdog@`
- `profileLoaded`
- `   Log Calls Dropped Console Filters`
- `CCOSSerializeWithIOReportDataStream`
- `1211`
- `cc.debug.logThrottleWindow`
- `site.CCLogStream_IVars`
- `site.CCDataPipeUserClient_IVars`
- `buf`
- `close`
- `withPipeAndName`
- `ConsoleLevel`
- `metaDataCounts: invalidPaddingSize`
- `%s:%06u: ERROR: Return code not sucessfull [%08x]\n`
- `CCIOServiceObjType`
- `[%lld]%llu.%llu\t %s\t - Logged: %s watchdog result=%s\n`
- `either driverID %lld or channelID %lld is bad\n`
- `122222222221111111111111111111111111111111111111111111111111111111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `DriverID`
- `12111112122212121`
- `22222222222222222222222222222222222222111`
- `1111111`
- `Filename`
- `CCFaultReporter`
- `%s::%s(): Boot-Arg cc.debug.logThrottleWindow, Value=%d\n`
- `removeSubscription`
- `site.CCIOReporterHub`
- `11`
- `2211211111`
- `readDataDispatchDesc`
- `CCFaultReporterService`
- `setStreamLogFlags`
- `CoreCaptureLevel`
- `setFlags`
- `cc.logging.oslog`
- `IOReportSubGroupName`
- `site.CCDataPipeBlobMD_IVars`
- `list`
- `NotifyThreshold`
- `metaDataCounts: invalidPayloadSize`
- `CCDataPipeBlobOD`
- `12111`
- `updateStreamConsoleLogFlags`
- `Unknown reason`
- `CCStream`
- `CCDataSession`
- `12111112122212121111111111111`
- `CCCapture`
- `site.CCPipeUserClient_IVars`
- `~%s`
- `0x%08x`
- `ConsoleFlag`
- `site.CCPipe_IVars`
- `ccpipe:`
- `site.CCStream_IVars`
- `createIOReporterRawDataForSubscription`
- `mapPipe`
- `                           Log Calls`
- `%s Dictionary has %d entries [%d succeeded %d failed]\n`
- `IOReportGroupName`
- `CCDataPipeUserClient`
- `startPipe`
- `IOReportDictionaryDriverEntryIDsKey`
- `FaultReportState.txt`
- `Triggering faultReport with reason '%s'\n`
- `AttachToDKPlane_Impl`
- `CCIOService_Kext.cpp`
- `222121222222222222222222222222222222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `Owners`
- `IOReportLegend`
- `221`
- `               Log Calls [Emergency]`
- `cc.debug.logThrottleCount`
- `setPipeStreamConsoleLogFlags`
- `setLevel`
- `clearLogFlag`
- `clearConsoleLogFlag`
- `cc.internal`
- `%s:%d CCIOService Attached pipe to DK CC root - %s\n`
- `Attach_Impl`
- `site.CCDataPipeBlobOD_IVars`
- `site.CCIOReporterDataStream_IVars`
- `PRESENT`
- `MISSING`
- `CoreCapture errorCodeStr for last fault status code %d : \n`
- `\"CC Forced: %s\" @%s:%d`
- `site.CCDataPipe_IVars`
- `LogDataType`
- `logIOReporterSubscriptions`
- `%06llu.%06llu %s.%c[%lu] %s`
- `site.CCLogPipeUserClient`
- `open`
- `MiscInfo`
- `112211212222`
- `readData`
- `               Log Calls      [Spam]`
- `site.CCStream`
- `site.CCDataPipeBlob_IVars`
- `site.CCCapture_IVars`
- `CCSetProperties_Impl`
- `CCPipeUserClient`
- `updatePipeStreamConsoleLogFlags`
- `setPipeWatermarkLevel`
- `CopyCCIOServicesWithOwner_Impl`
- `Unknown`
- `site.CCIOReporterDataStream`
- `site.DumpFile_t`
- `%s::%s(): Boot-Arg cc.debug.logThrottleCount, Value=%d\n`
- `metaDataCounts: invalidLogLevel`
- `createInterestsDictionary`
- `%s - Missing parameter\n`
- `IOClass`
- `createReportersAndLegend`
- `111112111222222222222222222222222222222222221221112`
- `i8@?0`
- `start`
- `site.CCIOService`
- `122`
- `CCDataPipeBlobOS`
- `site.CCDataPipeBlobOS`
- `site.CCIOReporterLogStream_IVars`
- `CCIOReportStream`
- `%s::%s() Failed to create ivars->fSharedRingStateMD\n`
- `setStreamConsoleLogFlags`
- `12221`
- `setConsoleFlags`
- `getLevel`
- `121`
- `stopPipe`
- `Pipe`
- `Failed to allocate IOReportInterestList\n`
- `%s~%s`
- `CCSetPropertiesValidateCCObject`
- `%s CCIOServiceInit clean up DK CoreCapture plane\n`
- `UnifiedPolicy`
- `%s::%s(): Called with invalid ivars\n`
- `DumpKernelCCPipesWithOwner_Impl`
- `IOReportElement`
- `               Log Calls      [Info]`
- `cc.logging.iolog`
- `setCCaptureInRegistryLocked`
- `History.txt`
- `site.ScratchBufferDB`
- `1211111212221212111111111111`
- `CCIOReportRdata`
- `%s::%s(): Boot-Arg cc.debug.logAfterWD, Value=%d\n`
- `AddFileList.txt`
- `1211111212221212111`
- `               Log Calls      [Crit]`
- `%s - ccKextPlane invalid\n`
- `Owner`
- `initWithPipeAndName`
- `12`
- `1121111112222`
- `Yes`
- `configureInterests`
- `CCPipe`
- `StreamHeader`
- `free`
- `Errors`
- `%s - Failed to attach to provider\n`
- `sub`
- `%s - registryRoot invalid\n`
- `site.CCDataPipeBlobOS_IVars`
- `panic@`
- `FileSize`
- `metaDataCounts: invalidState`
- `Detach_Impl`
- `CCDataPipeBlobMD`
- `site.CCFaultReport`
- `PipeType`
- `CCIOReportInterests`
- `MinLogSizeToNotify`
- `%d`
- `CoreCapture`
- `site.CCDataPipe`
- `readDataDispatchStruct`
- `CCIOServiceValidatorInit`
- `site.CCFaultReporter_IVars`
- `setStreamLogLevel`
- `removeCapture`
- `ccForcePanic_Impl`
- `site.CCFaultReport_IVars`
- `%s%s~%s`
- `-------------- Fault Report State ------------- \n%s\n%s:%d:%s\nTimestamp: %llu.%llu\nPC: 0x%llx LR: 0x%llx\nfAction 0x%x\nfEventID 0x%x\n`
- `nElements`
- `profileRemoved`
- `withOwnerNameCapacity`
- `configureReport`
- `CCLogPipe.cpp`
- `LogPolicy`
- `                              Log Calls`
- `                       Capture Requests`
- `setPipePolicy`
- `setLogFlag`
- `*`
- `CCDataStream`
- `cc.debug.logAfterWD`
- `init`
- `site.CCDataPipeBlob`
- `%s - CCIOService ccForcePanic ENTRY reason = %s\n`
- `setStreamConsoleLogLevel`
- `setPolicyInt`
- `setPipeStreamConsoleLogLevel`
- `setPipeNotifyTimeout`
- `CCIOService`
- `SUCCESS`
- `DirectoryName`
- `updateStreamLogFlags`
- `%s - CCIOService ccForcePanic EXIT\n`
- `CCOSSerializeDataStream`
- `Stream`
- `site.CCDataSession_IVars`
- `site.CCFaultReporter`
- `spinDeferredCapture`
- `CCIOReportInterestSubscriptionIDx`
- `CoreCaptureFlag`
- `IOReportChannels`
- `%s Invalid dictionary`
- `createReportSet`
- `attachHub`
- `logIOReporterSubscription`
- `setNotifyTimeout`
- `ccstream:`
- `reserveRingEntryDrops`
- `FAIL`
- `site.CCDataSession`
- `LogIdentifier`
- `bool CCFaultReporter::initWithStreamWorkloop(CCDataStream *, IOWorkLoop *)`
- `?`
- `getPolicy`
- `updatePipeStreamLogFlags`
- `        Log Calls Dropped CC Filters`
- `timestamp`
- `%s - CCIOService is missing an owner property\n`
- `PipeSize`
- `site.CCDataStream_IVars`
- `FaultReporterHistory`
- `site.CCIOReporterLogStream`
- `CCIOServiceInit_Impl`
- `1`
- `site.CCDataPipeBlobOD`
- `CCFaultReport`
- `dumpToDiskComplete`
- `%s - CCIOService is missing the IOClass property\n`
- `com.apple.corecapture.userclient`
- `site.CCIOReporterHub_IVars`
- `CCDataPipe::dequeueBlob - no IOUC to RX blob\n`
- `121111121222121211`
- `CoreCapture errorCodeStr for last fault reason code %d : \n`
- `CCLogPipe`
- `12111111111112`
- `IOReportDictionaryInterestChannelListKey`
- `_`
- `221111111111111122122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212222122221222212`
- `111111121`
- `CCIOReportRkey`
- `root`
- `unknown`
- `CCRegistryCopyStreams_Impl`
- `site.CCDataPipeBlobMD`
- `CCIOReporterDataStream`
- `12111112122212121111`
- `capture`
- `Statistics`
- `StartReg_Impl`
- `queryMetaDataDispatch`
- `setPolicy`
- `site.CCLogStream`
- `               Log Calls     [Debug]`
- `cc.debug.enable`
- `CCIOService Attached stream to pipe - %s\n`
- `%s:%06u: ERROR: Return code not expected [%08x]\n`
- `%s\n`
- `inducer@`
- `site.CCLogPipe`
- `CCLogStream`
- `<unknown>`
- `Couldn't create iterator of arrayIter\n`
- `CCIOReporterHub`
- `CCDataPipeBlob`
- `CCDataPipe`
- `CCFaultReport.cpp`
- `LogType`
- `CompressionDisabled`
- `   Log Messages Dropped Short Of Buffer`
- `%s - Not a CCIOService\n`
- `Id`
- `site.CallbackClient_t`
- `NamedFlags`
- `               Log Calls     [Alert]`
- `%s %s`
- `queryMetaData`
- `initWithOwnerNameCapacity`
- `site.CCLogPipe_IVars`
- `setWatermarkLevelToNotify`
- `               Log Calls    [Notice]`
- `No`
- `%s NO PROVIDER\n`
- `111`
- `CCSetPropertiesValidate`
- `               Log Calls      [Warn]`
