# `com.apple.driver.AppleGenericMultitouch`

- Name: AppleGenericMultitouch
- Version: `30`
- UUID: `AAC86B7A-89D9-3A0E-9948-2B5340F6B3C7`
- Source version: `30.0.0.0.0`
- Depends on: [`com.apple.driver.AppleHIDTransportFIFO`](com.apple.driver.AppleHIDTransportFIFO.md) 1, [`com.apple.driver.AppleHIDTransportMailbox`](com.apple.driver.AppleHIDTransportMailbox.md) 1, [`com.apple.driver.AppleHIDTransportSPI`](com.apple.driver.AppleHIDTransportSPI.md) 1, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### Decider - DockChannel
- `CFBundleIdentifier`: `com.apple.driver.AppleGenericMultitouch`
- `IOClass`: `AppleGenericMultitouchDecider`
- `IONameMatch`: `gen-mt-decider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGenericMultitouch`
- `IOProviderClass`: `AppleDockChannelDevice`

### Decider - Mailbox
- `CFBundleIdentifier`: `com.apple.driver.AppleGenericMultitouch`
- `IOClass`: `AppleGenericMultitouchDecider`
- `IONameMatch`:
  - `MTPEndpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGenericMultitouch`
- `IOProviderClass`: `RTBuddyEndpointService`

### Decider - SPI
- `CFBundleIdentifier`: `com.apple.driver.AppleGenericMultitouch`
- `IOClass`: `AppleGenericMultitouchDecider`
- `IONameMatch`: `gen-mt-decider`
- `IOPersonalityPublisher`: `com.apple.driver.AppleGenericMultitouch`
- `IOProviderClass`: `AppleARMSPIDevice`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleGenericMultitouchDecider` | 0xb8 | IOService → IORegistryEntry |
| `AppleGenericMultitouchDeciderHelper` | 0x40 |  |
| `AppleGenericMultitouchHIDDeviceBase` | 0xe0 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleGenericMultitouchHIDSPI` | 0x100 | AppleGenericMultitouchHIDDeviceBase → IOHIDDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000a1b2 off=0x00475390-0x0047f542 addr=0xfffffe0007479390-0xfffffe0007483542 r--/r--   __TEXT            
	sz=0x00006d1b off=0x00475a58-0x0047c773 addr=0xfffffe0007479a58-0xfffffe0007480773               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000236 off=0x0047c780-0x0047c9b6 addr=0xfffffe0007480780-0xfffffe00074809b6               __TEXT.__const            
	sz=0x00002b8c off=0x0047c9b6-0x0047f542 addr=0xfffffe00074809b6-0xfffffe0007483542               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000a938 off=0x01d0ce20-0x01d17758 addr=0xfffffe0008d10e20-0xfffffe0008d1b758 r-x/r-x   __TEXT_EXEC       
	sz=0x0000a5b8 off=0x01d0ce20-0x01d173d8 addr=0xfffffe0008d10e20-0xfffffe0008d1b3d8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000380 off=0x01d173d8-0x01d17758 addr=0xfffffe0008d1b3d8-0xfffffe0008d1b758          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000181 off=0x049426c8-0x04942849 addr=0xfffffe000b9466c8-0xfffffe000b946849 rw-/rw-   __DATA            
	sz=0x000000d4 off=0x049426c8-0x0494279c addr=0xfffffe000b9466c8-0xfffffe000b94679c               __DATA.__data             
	sz=0x000000a8 off=0x00000000-0x000000a8 addr=0xfffffe000b9467a0-0xfffffe000b946848               __DATA.__common           (Zerofill)
	sz=0x00000001 off=0x00000000-0x00000001 addr=0xfffffe000b946848-0xfffffe000b946849               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001c38 off=0x010b4668-0x010b62a0 addr=0xfffffe00080b8668-0xfffffe00080ba2a0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x010b4668-0x010b4680 addr=0xfffffe00080b8668-0xfffffe00080b8680         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x010b4680-0x010b4698 addr=0xfffffe00080b8680-0xfffffe00080b8698         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001780 off=0x010b4698-0x010b5e18 addr=0xfffffe00080b8698-0xfffffe00080b9e18         __DATA_CONST.__const            
	sz=0x00000200 off=0x010b5e18-0x010b6018 addr=0xfffffe00080b9e18-0xfffffe00080ba018         __DATA_CONST.__kalloc_type      
	sz=0x000001c0 off=0x010b6018-0x010b61d8 addr=0xfffffe00080ba018-0xfffffe00080ba1d8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c8 off=0x010b61d8-0x010b62a0 addr=0xfffffe00080ba1d8-0xfffffe00080ba2a0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 137 at 0x04ada648
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AAC86B7A-89D9-3A0E-9948-2B5340F6B3C7
008: LC_SOURCE_VERSION           30.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa09c8 size=0x158
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleGenericMultitouch`
- `CFBundleIdentifier`: `com.apple.driver.AppleGenericMultitouch`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleGenericMultitouch`
- `CFBundleNumericVersion`: `805339136`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `30`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `30`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleGenericMultitouch.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901124208`
- `_PrelinkExecutableRelativePath`: `AppleGenericMultitouch`
- `_PrelinkExecutableSize`: `92323`
- `_PrelinkExecutableSourceAddr`: `-2198901124208`
- `_PrelinkKmodInfo`: `-2198828980536`

## Strings (326) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `agm-challenge`
- `report && (reportType == kIOHIDReportTypeFeature)`
- `authentic`
- `void AppleGenericMultitouchDeciderHelper::setAuthCPService(IOService *)`
- `%u`
- `agm-primary`
- `site.AppleGenericMultitouchHIDSPI`
- `auto AppleGenericMultitouchHIDSPI::performChallengeSequence()::(anonymous class)::operator()(bool &) const`
- `ErrorIDMismatch`
- `virtual bool AppleGenericMultitouchHIDDeviceBase::handleStart(IOService *)`
- `report->getLength() >= cached->getLength()`
- `InputReportWhitelist`
- `Error`
- `void AppleGenericMultitouchDeciderHelper::trustStateDetermined(bool)`
- `legacy`
- `LLPreamble`
- `LossyOutput`
- `void AppleGenericMultitouchHIDDeviceBase::setExtraProperties()`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `md`
- `hid-merge-personality`
- `12111112122212121111112`
- `configProviderName`
- `cached`
- `super::start(provider)`
- `result != Failed`
- `firstHelper`
- `non-auth-personality`
- `auth-required`
- `newStringData`
- `SetReportWhitelist`
- `SPIConfig`
- `ChallengeSequence`
- `createDeciderHelpers()`
- `setupMatchingCallback()`
- `classToLaunch`
- `eeprom-property`
- `SetResultData`
- `site.AGMFemtoHIDSPI`
- `downloaders`
- `mappings`
- `void AppleGenericMultitouchDecider::recordUltimateDecision(bool, bool)`
- `service->init()`
- `UltimateDecision`
- `newStringSizeNullTerminated <= sizeof(newStringBuffer)`
- `static OSSharedPtr<OSString> AppleGenericMultitouchHIDDeviceBase::copyPersonality(IOService *)`
- `12112111`
- `ReportDescriptor`
- `0x%02x`
- `i8@?0`
- `void AppleGenericMultitouchHIDSPI::logAck(const AGMFemtoHIDSPI::AckPacket &, const AGMFemtoHIDSPI::AckPacket &)`
- `virtual bool AppleGenericMultitouchDecider::start(IOService *)`
- `Control`
- `Invalid`
- `KeepCS`
- `LossyInput`
- `StartEnd`
- `authReqStr`
- `IsTrusted`
- `LosslessInput`
- `GetOutputReport`
- `/Library/Caches/com.apple.xbs/18870140-AD72-47E9-90F7-D7C84661AAD4/TemporaryDirectory.zANmYd/Sources/AppleGenericMultitouch/Kext/hiddevice/AppleGenericMultitouchHIDDeviceBase.cpp`
- `props`
- `site.AppleGenericMultitouchDecider`
- `void AppleGenericMultitouchDeciderHelper::authenticityStateDetermined(bool)`
- `service`
- `IsAuthentic`
- `GetResultData`
- `SetOutputReport`
- `bool AppleGenericMultitouchDeciderHelper::processStatesReady()`
- `bool AppleGenericMultitouchDecider::setupMatchingCallback()`
- `static bool AppleGenericMultitouchDecider::launchIOService(const char *, IOService *)`
- `non-auth-suffix`
- `void AppleGenericMultitouchHIDSPI::handleHIDRxGated(const AGMFemtoHIDSPI::HIDPacket &)`
- `CSDelay`
- `HalfClockDelay`
- `isTrusted`
- `void AppleGenericMultitouchHIDSPI::interrupt(IOInterruptEventSource *, int)`
- `personalityProp`
- `helpers`
- `dict`
- `PeriodNS`
- `site.AGMConfigManagerHIDSPI`
- `NoData`
- `rd`
- `site.AppleGenericMultitouchDeciderHelper`
- `agm-authentic`
- `configProvider`
- `Ack`
- `site.AppleGenericMultitouchHIDDeviceBase`
- `_authCPMatch`
- `Apple`
- `virtual void AppleGenericMultitouchHIDDeviceBase::inputReport(uint8_t, const void *, size_t)`
- `bool AppleGenericMultitouchDecider::createDeciderHelpers()`
- `auto AppleGenericMultitouchDecider::createDeciderHelpers()::(anonymous class)::operator()(IORegistryEntry *) const`
- `void AppleGenericMultitouchHIDSPI::logTransfer(const AGMFemtoHIDSPI::LLPacket &, const AGMFemtoHIDSPI::LLPacket &)`
- `ExpectedRx`
- `Nak`
- `auth-supported`
- `Name`
- `super::init(dictionary)`
- `_wl`
- `super::handleStart(provider)`
- `baseString`
- `StartSequence`
- `Value2`
- `not authentic`
- `success`
- `/Library/Caches/com.apple.xbs/18870140-AD72-47E9-90F7-D7C84661AAD4/TemporaryDirectory.zANmYd/Sources/AppleGenericMultitouch/Kext/AppleGenericMultitouchDecider.cpp`
- `StartBegin`
- `virtual void AppleGenericMultitouchDecider::stop(IOService *)`
- `const char *AppleGenericMultitouchDecider::getInterfaceNameForIndex(UInt32)`
- `LosslessOutput`
- `virtual bool AppleGenericMultitouchHIDDeviceBase::init(OSDictionary *)`
- `agm-secondary`
- `service->start(provider)`
- `ComponentIndex`
- `Value0`
- `12111112122212121121112221121111`
- `Phase`
- `GetFeatureReport`
- `Success`
- `personalityData`
- `bool AppleGenericMultitouchDecider::authCPMatched(void *, IOService *, IONotifier *)`
- `flags`
- `bool AppleGenericMultitouchHIDSPI::performChallengeSequence()`
- `ErrorIncorrectLength`
- `virtual IOReturn AppleGenericMultitouchHIDDeviceBase::getReport(IOMemoryDescriptor *, IOHIDReportType, IOOptionBits)`
- `AuthPassed`
- `AppleGenericMultitouchDeciderHelper *AppleGenericMultitouchDecider::findHelperForInterface(UInt32)`
- `agm-bytes`
- `DelayUS`
- `Polarity`
- `InterStageDelayUS`
- `Tx`
- `flagsNum`
- `IOReturn AppleGenericMultitouchDecider::helperStateChangedGated(AppleGenericMultitouchDeciderHelper *)`
- `ExtraProperties`
- `AppleGenericMultitouchHIDSPI`
- `void AppleGenericMultitouchHIDSPI::handleRxGated(const AGMFemtoHIDSPI::LLPacket &)`
- `MaxLLPayloadLength`
- `SetFeatureReport`
- `void AppleGenericMultitouchDecider::processAllStatesReady()`
- `descriptor`
- `FirstInputReceived`
- `Value1`
- `11222`
- `1211111212221212112111222112`
- `not trusted`
- `_commandGate`
- `getWorkLoop()->addEventSource(_commandGate.get()) == 0`
- `1`
- `Busy`
- `bool AppleGenericMultitouchDeciderHelper::init(StateChangedCallback, void *, UInt32, IORegistryEntry *)`
- `agm-trusted`
- `virtual IOService *AppleGenericMultitouchDecider::probe(IOService *, SInt32 *)`
- `bool AppleGenericMultitouchDecider::areAllStatesDetermined()`
- `auth-source-index`
- `bool appendStringToDataProperty(IORegistryEntry *, const char *, const char *)`
- `AppleGenericMultitouchHIDDeviceBase`
- `virtual IOReturn AppleGenericMultitouchHIDDeviceBase::newReportDescriptor(IOMemoryDescriptor **) const`
- `AppleGenericMultitouchDeciderHelper`
- `AppleGenericMultitouchDecider`
- `trusted`
- `failed`
- `GetInputReport`
- `IOReturn AppleGenericMultitouchDeciderHelper::authCPInterest(void *, UInt32, IOService *, void *, vm_size_t)`
- `AppleAuthCP`
- `service->attach(provider)`
- `HIDSPIConfig`
- `void AppleGenericMultitouchDeciderHelper::checkBootArgs()`
- `numberVal`
- `auto AppleGenericMultitouchDecider::start(IOService *)::(anonymous class)::operator()(AppleGenericMultitouchDecider *) const`
- `<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n<plist version=\"1.0\">\n<dict>\n\t<key>C1FC0,2</key>\n\t<dict>\n\t\t<key>ChallengeSequence</key>\n\t\t<array>\n\t\t\t<dict>\n\t\t\t\t<key>DelayAfte`
- `SPI`
- `DelayAfterUS`
- `getConfigManager()`
- `virtual void AppleGenericMultitouchDeciderHelper::free()`
- `static void AppleGenericMultitouchDecider::helperStateChangedCallback(AppleGenericMultitouchDeciderHelper *, void *)`
- `succeeded`
- `multi-interface`
- `GetReportCachedResponse`
- `ErrorUnsupported`
- `helpers->getCount() > 0`
- `WordDelay`
- `SetInputReport`
- `flagsObj`

**[__TEXT.__os_log]**

- `%s, %s file: %s, line: %d, value: 0x%08X\n%s line %d`
- `[Helper %u] Interface %u authenticity determined: %s\n%s line %d`
- `[Decider] All states determined, processing final decision\n%s line %d`
- `[Decider] Interface %s uses legacy auth (no AuthSourceIndex), defaulting to index 0\n%s line %d`
- `[Decider] Processing all states ready - making final launch decision\n%s line %d`
- `[Helper %u] Interface %u trust determined: %s\n%s line %d`
- `[Decider] Searching parent, name: %s\n%s line %d`
- `[Decider] Found auth-required child: %s\n%s line %d`
- `[Decider] Successfully set up AuthCP matching callback\n%s line %d`
- `Dropping input report rID = 0x%02x\n%s line %d`
- `[Helper %u] super::init() failed for interface %u\n%s line %d`
- `[Decider] AuthCP service matched: %s\n%s line %d`
- `[Decider] Maximum string size exceeded\n%s line %d`
- `Ignoring rx with invalid length requested/payload length\n%s line %d`
- `ACK TX: [type = %s]\n%s line %d`
- `[Helper %u] Interface %u: Found boot arg agm-trusted=%u\n%s line %d`
- `[Helper %u] Interface %u: No non-auth-personality or non-auth-suffix found\n%s line %d`
- `[Decider] Failed to parse AuthSourceIndex for interface %s, using legacy mode\n%s line %d`
- `[Helper %u] Interface %u: Appending hid-merge-personality with non-auth-suffix: %s\n%s line %d`
- `[Decider] Searching for entries with auth-required property\n%s line %d`
- `[Decider] No helpers pointer, or helpers count = 0\n%s line %d`
- `LL TX: [type = %s, interface = %u, payloadOffset = %zu, payloadRemaining = %zu, payloadLength = %zu, crc = 0x%04x]\n%s line %d`
- `Dispatched report rID = 0x%02x\n%s line %d`
- `[Helper %u] Duplicate trust state determined for interface %u, ignoring\n%s line %d`
- `[Helper %u] Processing states ready for interface %u (authentic=%u, trusted=%u)\n%s line %d`
- `[Decider] %s\n%s line %d`
- `LL RX: [type = %s, interface = %u, payloadOffset = %zu, payloadRemaining = %zu, payloadLength = %zu, crc = 0x%04x]\n%s line %d`
- `[Helper %u] Successfully initialized helper for interface %u\n%s line %d`
- `[Decider] Finding AID image downloaders\n%s line %d`
- `[Decider] No auth-required entries found\n%s line %d`
- `[Decider] Cannot find helper - helpers array is null\n%s line %d`
- `[Decider] Launch %s\n%s line %d`
- `Challenge sequence step %u\n%s line %d`
- `[Helper %u] Checking boot args for interface %u\n%s line %d`
- `[Decider] Starting AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Cleaning up %u helper(s)\n%s line %d`
- `[Decider] Legacy mode detected, stopping search after first interface\n%s line %d`
- `[Decider] Interface 0 is %s\n%s line %d`
- `[Decider] Multi-interface mode with %u interfaces\n%s line %d`
- `[Decider] Launching IOService: %s\n%s line %d`
- `[Decider] Failed to set up AuthCP matching callback\n%s line %d`
- `[Decider] All interface states are determined\n%s line %d`
- `Rx bytes`
- `Challenge overriden: (%u -> %u)\n%s line %d`
- `[Helper %u] Interface %u: Overwriting hid-merge-personality with non-auth-personality: %s\n%s line %d`
- `[Decider] AuthCP service has interface index: %u\n%s line %d`
- `[Decider] No helpers available to check states\n%s line %d`
- `[Decider] Failed to attach %s\n%s line %d`
- `[Decider] Created %u helper(s) with index mappings\n%s line %d`
- `[Decider] No helper found for interface index %u\n%s line %d`
- `[Decider] Single interface mode\n%s line %d`
- `[Decider] Couldn't retrieve class to launch\n%s line %d`
- `[Decider] Failed to initialize helper for index %u\n%s line %d`
- `HID RX: [type = %s, rID = 0x%02x, status = %s, frameNumber = %u, lengthRequested = %zu, payloadLength = %zu, crc = 0x%04x]\n%s line %d`
- `[Decider] Boot args not set, setting up matching callback\n%s line %d`
- `[Decider] Failed to copy kAppleAuthCPInterfaceIndexKey property from this instance of AppleAuthCPRelay\n%s line %d`
- `Tx bytes`
- `Interrupt occurred\n%s line %d`
- `Ignoring rx with invalid CRC (got 0x%04x, computed 0x%04x)\n%s line %d`
- `[Decider] AuthCP service has no interface index, using default 0\n%s line %d`
- `[Decider] Failed to init %s\n%s line %d`
- `Ignoring rx of status %s\n%s line %d`
- `[Helper %u] Freeing helper for interface %u\n%s line %d`
- `[Helper %u] Interface %u received authCP interest callback, messageType=0x%x, argSize=%zu\n%s line %d`
- `[Decider] Recorded start begin time\n%s line %d`
- `[Decider] Couldn't cast flagsObj!\n%s line %d`
- `[Decider] Helper state changed callback for interface %u\n%s line %d`
- `[Decider] Failed to allocate helper for index %u\n%s line %d`
- `xferResult = 0x%08x, rxCorrect = %u\n%s line %d`
- `ACK RX: [type = %s]\n%s line %d`
- `[Decider] Helper for interface %u still waiting for AuthCP service\n%s line %d`
- `[Decider] Failed to start %s\n%s line %d`
- `[Decider] Interface %s uses multi-interface auth with index %u\n%s line %d`
- `[Decider] Found touch instance of AppleAuthCPRelay\n%s line %d`
- `[Decider] Using config provider: %s\n%s line %d`
- `[Decider] Stopping AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Failed to process config provider\n%s line %d`
- `[Decider] Boot args check complete: all states determined = %u\n%s line %d`
- `Challenge end: %u\n%s line %d`
- `[Decider] Creating decider helpers\n%s line %d`
- `[Decider] Failed to process child\n%s line %d`
- `[Decider] Found helper for interface index %u\n%s line %d`
- `[Decider] Waiting for more states to be determined\n%s line %d`
- `[Decider] Cannot get interface name - mappings not initialized\n%s line %d`
- `[Decider] Found auth-required on config provider: %s\n%s line %d`
- `[Decider] helperStateChanged called with null helper\n%s line %d`
- `[Decider] Already launched, ignoring state change\n%s line %d`
- `[Decider] Launching %s\n%s line %d`
- `[Helper %u] No auth consumer for interface %u\n%s line %d`
- `[Decider] Setting up AuthCP matching callback\n%s line %d`
- `%s`
- `Ignoring rx for interface %u\n%s line %d`
- `auth-supported property not found\n%s line %d`
- `Challenge begin\n%s line %d`
- `Ignoring rx with invalid payload offset/length\n%s line %d`
- `[Helper %u] Interface %u received authenticity callback: %u\n%s line %d`
- `[Decider] Failed to create key symbol for index %u\n%s line %d`
- `[Decider] Interface %u states not ready (auth=%u, trust=%u)\n%s line %d`
- `[Helper %u] Initializing helper for interface %u\n%s line %d`
- `[Helper %u] Received authCP interest from unexpected service for interface %u\n%s line %d`
- `[Helper %u] Interface %u: Failed to process states ready\n%s line %d`
- `[Decider] All interfaces matched, disabling notifier\n%s line %d`
- `[Decider] No interface name found for index %u\n%s line %d`
- `[Decider] Failed to create interface name string for index %u\n%s line %d`
- `[Helper %u] Setting AuthCP service for interface %u\n%s line %d`
- `[Decider] Stopped AppleGenericMultitouchDecider\n%s line %d`
- `[Helper %u] Interface %u received trust callback: %u\n%s line %d`
- `[Decider] Ultimate decision recorded: %u\n%s line %d`
- `[Helper %u] Interface %u received unhandled message type 0x%x\n%s line %d`
- `[Decider] Successfully started AppleGenericMultitouchDecider\n%s line %d`
- `[Decider] Checking if all %u interface(s) have states determined\n%s line %d`
- `[Helper %u] Interface %u: Successfully processed states ready\n%s line %d`
- `[Helper %u] Interface %u: Device not authentic, processing personality override\n%s line %d`
- `[Decider] flags = 0x%08x\n%s line %d`
- `[Decider] AuthCP service is not a touch controller (flags=0x%08x)\n%s line %d`
- `[Decider] Interface %u is not authentic in multi-interface device\n%s line %d`
- `[Helper %u] Registered interest notifier for interface %u\n%s line %d`
- `[Decider] Creating helpers\n%s line %d`
- `auth-supported property found, matching AGM\n%s line %d`
- `[Decider] Recording ultimate decision: authentic=%u, launchSuccess=%u\n%s line %d`
- `[Helper %u] Polled %s state: %u\n%s line %d`
- `[Decider] Disabling authCP match notifier\n%s line %d`
- `[Decider] Checking boot args for all helpers\n%s line %d`
- `[Helper %u] Interface %u: %s property exists but is not OSBoolean\n%s line %d`
- `[Helper %u] Interface %u: Removing eeprom-property (authentic=%u, trusted=%u)\n%s line %d`
- `[Decider] Failed to create decider helpers\n%s line %d`
- `[Decider] Couldn't get flags property!\n%s line %d`
- `[Decider] Processing state change for interface %u (authDetermined=%u, trustDetermined=%u)\n%s line %d`
- `[Decider] Failed to allocate class %s\n%s line %d`
- `[Decider] Found %u AID image downloaders\n%s line %d`
- `[Decider] Created helper for index %u (interface: %s, %s mode)\n%s line %d`
- `[Helper %u] Interface %u: Found boot arg agm-authentic=%u\n%s line %d`
- `[Helper %u] Duplicate authenticity state determined for interface %u, ignoring\n%s line %d`
- `[Helper %u] Interface %u: %s property not yet available\n%s line %d`
- `[Helper %u] Interface %u: All states ready, disabling interest notifier\n%s line %d`
- `[Decider] Failed start\n%s line %d`
- `[Decider] Legacy mode detected, config provider is the only interface\n%s line %d`
- `[Decider] Multi-interface overall authentic state: %u\n%s line %d`
- `Ignoring rx of type %s\n%s line %d`
