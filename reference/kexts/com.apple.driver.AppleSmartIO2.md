# `com.apple.driver.AppleSmartIO2`

- Name: AppleSmartIO2
- Version: `1`
- UUID: `A26BAF9D-FBC7-32A4-A6A8-BD8DEA825BE0`
- Source version: `153.0.0.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOCryptoAcceleratorFamily`](com.apple.iokit.IOCryptoAcceleratorFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleSmartIO
- `CFBundleIdentifier`: `com.apple.driver.AppleSmartIO2`
- `IOClass`: `AppleSmartIO`
- `IONameMatch`:
  - `SIOEndpoint1`
  - `SIO1Endpoint1`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSmartIO2`
- `IOPlatformActiveAction`: `80000`
- `IOPlatformQuiesceAction`: `80000`
- `IOPlatformSleepAction`: `590`
- `IOPlatformWakeAction`: `590`
- `IOProviderClass`: `RTBuddyEndpointService`

### AppleSmartIODMA
- `CFBundleIdentifier`: `com.apple.driver.AppleSmartIO2`
- `IOClass`: `AppleSmartIODMAController`
- `IOMatchCategory`: `DMA`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSmartIO2`
- `IOProviderClass`: `AppleSmartIODMANub`


## C++ classes (10) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSmartIO` | 0x858 | IOService → IORegistryEntry |
| `AppleSmartIOCommand` | 0x78 | IOCommand |
| `AppleSmartIOCommandPool` | 0x48 | IOCommandPool |
| `AppleSmartIOControl` | 0x18e0 | AppleSmartIOEndpoint |
| `AppleSmartIODMA` | 0x39f0 | AppleSmartIOEndpoint |
| `AppleSmartIODMAController` | 0x4e0 | IODMAController → IOService → IORegistryEntry |
| `AppleSmartIODMANub` | 0x90 | IOService → IORegistryEntry |
| `AppleSmartIOEndpoint` | 0x1840 |  |
| `AppleSmartIOPerf` | 0x1850 | AppleSmartIOEndpoint |
| `AppleSmartIOUserClient` | 0xe0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004e00 off=0x00790950-0x00795750 addr=0xfffffe0007794950-0xfffffe0007799750 r--/r--   __TEXT            
	sz=0x00004721 off=0x00790fc8-0x007956e9 addr=0xfffffe0007794fc8-0xfffffe00077996e9               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000060 off=0x007956f0-0x00795750 addr=0xfffffe00077996f0-0xfffffe0007799750               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000b898 off=0x0275b890-0x02767128 addr=0xfffffe000975f890-0xfffffe000976b128 r-x/r-x   __TEXT_EXEC       
	sz=0x0000b4e8 off=0x0275b890-0x02766d78 addr=0xfffffe000975f890-0xfffffe000976ad78          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000003b0 off=0x02766d78-0x02767128 addr=0xfffffe000976ad78-0xfffffe000976b128          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000998 off=0x049a03a0-0x049a0d38 addr=0xfffffe000b9a43a0-0xfffffe000b9a4d38 rw-/rw-   __DATA            
	sz=0x000007f8 off=0x049a03a0-0x049a0b98 addr=0xfffffe000b9a43a0-0xfffffe000b9a4b98               __DATA.__data             
	sz=0x000001a0 off=0x00000000-0x000001a0 addr=0xfffffe000b9a4b98-0xfffffe000b9a4d38               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002838 off=0x0122f838-0x01232070 addr=0xfffffe0008233838-0xfffffe0008236070 rw-/rw-   __DATA_CONST      
	sz=0x00000038 off=0x0122f838-0x0122f870 addr=0xfffffe0008233838-0xfffffe0008233870         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000038 off=0x0122f870-0x0122f8a8 addr=0xfffffe0008233870-0xfffffe00082338a8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000021f0 off=0x0122f8a8-0x01231a98 addr=0xfffffe00082338a8-0xfffffe0008235a98         __DATA_CONST.__const            
	sz=0x00000280 off=0x01231a98-0x01231d18 addr=0xfffffe0008235a98-0xfffffe0008235d18         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01231d18-0x01231db8 addr=0xfffffe0008235d18-0xfffffe0008235db8         __DATA_CONST.__kalloc_var       
	sz=0x000001d8 off=0x01231db8-0x01231f90 addr=0xfffffe0008235db8-0xfffffe0008235f90         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x01231f90-0x01232070 addr=0xfffffe0008235f90-0xfffffe0008236070         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 146 at 0x04ae724c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A26BAF9D-FBC7-32A4-A6A8-BD8DEA825BE0
008: LC_SOURCE_VERSION           153.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab3178 size=0x240
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSmartIO2`
- `CFBundleIdentifier`: `com.apple.driver.AppleSmartIO2`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSmartIO2`
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
- `NSHumanReadableCopyright`: `Copyright © 2013-2023 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSmartIO2.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897866416`
- `_PrelinkExecutableRelativePath`: `AppleSmartIO2`
- `_PrelinkExecutableSize`: `79976`
- `_PrelinkExecutableSourceAddr`: `-2198897866416`
- `_PrelinkKmodInfo`: `-2198828596320`

## Strings (380) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `bool AppleSmartIODMAController::_enter_channel(UInt32, AppleSmartIODMA *, UInt32 *)`
- `\"Expected ACK from configure on Channel %s(%d): Received: %d\" @%s:%d`
- `121111121222121211`
- `SPI1_TX`
- `AOP_LEAP5_RX`
- `_enable_count < 0xFFFFFFFF`
- `virtual IOReturn AppleSmartIODMAController::initDMAChannel(IOService *, IODMAEventSource *, UInt32 *, UInt32)`
- `121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `MCA7_TX`
- `UART6_RX`
- `AOP_LEAP11_TX`
- `Oct 13 2026`
- `ASIO: ASIO: EP: %d TAG: %d OP: %d PARAM: %#02X DATA: %#08X %s %s\n`
- `type < kMaxDeviceType`
- `state->count == state->segment_length`
- `DPA4_TX`
- `rtbuddy != nullptr`
- `enable-cpu-power-gating`
- `_channel_state == kSIOChannelIdle`
- `\"bad report tag %u received on EP %s(%d)\" @%s:%d`
- `\"unexpected asynchronous error %u on EP %s(%d)\" @%s:%d`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `virtual IOReturn AppleSmartIOEndpoint::sendMessage(void *, void *, bool)`
- `bool AppleSmartIOEndpoint::initWithOptions(AppleSmartIO *, OSObject *, UInt32)`
- `_shims_memory`
- `void AppleSmartIODMA::_setConfiguration(AppleSmartIODMAConfig *)`
- `state->segment_count == 0`
- `!queue_empty(&_dmaCommandsToComplete)`
- `MCA2_RX`
- `DPA3_TX`
- `AppleSmartIO (RTBuddy-based)::start Could not find valid mapper\n`
- `control != nullptr`
- `ASIO WARNING: attempt to send message to SIO in non-receptive state\n`
- `virtual bool AppleSmartIOCommandPool::returnCommand(AppleSmartIOCommand *)`
- `asio`
- `dmashim`
- `AOP_MCA1_TX`
- `virtual bool AppleSmartIO::start(IOService *)`
- `121121121`
- `site.AppleSmartIOControl`
- `AppleSmartIODMA.cpp`
- `void AppleSmartIODMAController::returnBuffer(BufferHandle, unsigned int)`
- `_dmaes != nullptr`
- `UART8_RX`
- `MCA11_RX`
- `AppleSmartIO.cpp`
- `virtual IOReturn AppleSmartIOUserClient::externalMethod(uint32_t, IOExternalMethodArgumentsOpaque *)`
- `\"%s:%s:%u: REQUIRE failed on endpoint %u: %s\" @%s:%d`
- `pool != nullptr`
- `virtual IOReturn AppleSmartIODMAController::queryDMACommand(UInt32, IODMACommand **, IOByteCount *, bool)`
- `count < _segment_space`
- `_workloop`
- `MCA3_TX`
- `UART4_TX`
- `UART5_TX`
- `\"%s:%s:%u: REQUIRE failed: %s\" @%s:%d`
- `asio-misc-tunables`
- `_channels[i].endpoint != sdma`
- `_channel_configured`
- `MCA4_RX`
- `AppleSmartIOUserClient.cpp`
- `ASIO: user client externalMethod: selector %d\n`
- `void AppleSmartIOControl::sendTunables()`
- `\"Endpoint %s(%d) being used by parent driver when shutdown requested.\" @%s:%d`
- `asio->getWorkLoop()`
- `void AppleSmartIOControl::sendPSRegisters()`
- `MCA0_TX`
- `UART0_TX`
- `(handle + actual) <= _segment_space`
- `site.AppleSmartIODMA`
- `ASIO WARNING: DMA command submission failed with error %u on EP %s(%d)\n`
- `owner != nullptr`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIODMA.cpp`
- `dmaIndex < _max_channels`
- `state->dma_command != nullptr`
- `cmd == dmaCommand`
- `SPI4_TX`
- `UART1_TX`
- `MCA11_TX`
- `AppleSmartIO`
- `nullptr != _rtbuddyEndpoint`
- `121122222221123`
- `site.AppleSmartIOCommand *`
- `_conditionStateLock != nullptr`
- `AOP_MCA2_TX`
- `iodc`
- `void AppleSmartIOControl::populateShimPowerGateProperties()`
- `void AppleSmartIOControl::setupShims()`
- `sio-reg`
- `MCA0_RX`
- `ASIO: starting user client: provider=%p name='%s'\n`
- `\"SmartIO sent unexpected async Message: EP: %2d TAG: %d OP: %3d PARAM: %#02X DATA: %#08X\" @%s:%d`
- `_channels[i].handle != channel_handle`
- `UART0_RX`
- `MCA10_RX`
- `121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `(numEntries > 0) && (numEntries <= kMaxDeviceType) && ((numEntries * sizeof(device_type_dt_entry_t)) == data->getLength())`
- `\"prepareWithSpecification failed (%d), offset = %llu\" @%s:%d`
- `UART7_TX`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.cpp`
- `site.AppleSmartIOCommand`
- `(numEntries * sizeof(sioregister_entry_t)) == data->getLength()`
- `IOReturn AppleSmartIODMAController::_initDMAChannelGated(const AppleSmartIODMAConfig *, IODMAEventSource *, UInt32 *)`
- `SPI3_TX`
- `SPI2_RX`
- `site.AppleSmartIO`
- `debug`
- `_command_gate`
- `AppleSmartIOControl.cpp`
- `asio-ascwrap-tunables`
- `msgw.gmsg.endpoint == SmartIOEndpoint::kEndpointPerf`
- `ASIO WARNING: bad configuration index\n`
- `AOP_MCA3_TX`
- `UART1_RX`
- `UART5_RX`
- `AOP_LEAP1_TX`
- `AOP_LEAP4_RX`
- `provider != nullptr`
- `121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `*(cfg.memory)`
- `clientClassName != nullptr`
- `ASIO WARNING: failed to create DMA controller nub\n`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOCommand.cpp`
- `AppleSmartIOCommand.cpp`
- `workloop != nullptr`
- `virtual void AppleSmartIOEndpoint::ep_disable()`
- `void AppleSmartIOControl::setupDevices()`
- `virtual IOReturn AppleSmartIODMAController::startDMACommand(UInt32, IODMACommand *, IODirection, IOByteCount, IOByteCount)`
- `AOP_MCA0_RX`
- `MCA8_RX`
- `AOP_LEAP3_TX`
- `ASIO WARNING: no DMA controller nub in the devicetree (2)\n`
- `(numEntries > 0) && (numEntries <= kMaxShim) && ((numEntries * sizeof(shim_dt_entry_t)) == data->getLength())`
- `IOReturn AppleSmartIODMA::_configureDMA()`
- `ASIO WARNING: SmartIO DMA driver encountered an error: %#08x\n`
- `virtual IOByteCount AppleSmartIODMA::validFIFODepth(IOByteCount, IODirection)`
- `virtual IOReturn AppleSmartIO::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `command->getPool() == this`
- `AppleSmartIOEndpoint`
- `IOReturn AppleSmartIODMA::_queryDMA(IODMACommand **, IOByteCount *, bool *)`
- `\"tag %u reported on EP %s(%d) while not active\" @%s:%d`
- `AOP_MCA2_RX`
- `nullptr != _slaveProcessor`
- `ASIO: Sync Message Resp: EP: %d TAG:%d OP: %d PARAM: %d DATA: %#08X RecvTime: %lld InFlight: %lldns\n`
- `config != nullptr`
- `\"DMA stop failed with error %u on EP %s(%d)\" @%s:%d`
- `site.AppleSmartIOUserClient`
- `handle < _segment_space`
- `virtual void AppleSmartIODMA::_asyncMessage(void *, void *)`
- `void AppleSmartIODMA::_completeCommand(AppleSmartIOCommand *)`
- `UInt32 AppleSmartIO::shimToPSIndex(UInt32)`
- `MCA7_RX`
- `AOP_LEAP7_TX`
- `device-type`
- `AppleSmartIODMA`
- `AOP_LEAP12_RX`
- `(numEntries * sizeof(SmartIOTunableEntry)) == data->getLength()`
- `void AppleSmartIODMA::_notifyCommand(AppleSmartIOCommand *)`
- `AOP_LEAP9_RX`
- `AOP_LEAP10_TX`
- `_slaveProcessor->setPowerState(kRtbPowerStateOn, nullptr) == kIOReturnSuccess`
- `cmd != nullptr`
- `AppleSmartIOControl`
- `!state->done`
- `MCA9_RX`
- `UART4_RX`
- `DPA1_TX`
- `Out Of Range`
- `ASIO: closing user client\n`
- `virtual IOReturn AppleSmartIODMAController::setFrameSize(UInt32, UInt8)`
- `MCA2_TX`
- `AppleSmartIOUserClient`
- `virtual void AppleSmartIOControl::_asyncMessage(void *, void *)`
- `virtual void AppleSmartIOPerf::_asyncMessage(void *, void *)`
- `ASIO WARNING: could not get DMA endpoint for handle %s(%u)\n`
- `_asio`
- `dmaes != nullptr`
- `_commands_in_flight == 0`
- `UART2_TX`
- `nullptr != _rtbuddyEndpointService`
- `IOUserClientDefaultLockingSetProperties`
- `requested by user client`
- `void AppleSmartIOControl::setupPanicBuffer()`
- `numEntries > 0`
- `virtual bool AppleSmartIODMAController::start(IOService *)`
- `ASIO WARNING: channel index overflow - too many DMA channels allocated\n`
- `IOCommandGate *AppleSmartIOEndpoint::getCommandGate()`
- `ASIO WARNING: no tunable entries for '%s'\n`
- `_segment_memory != nullptr`
- `IOReturn AppleSmartIODMA::_stopDMA(bool *, void *)`
- `AppleSmartIO.h`
- `AOP_LEAP5_TX`
- `AOP_LEAP7_RX`
- `AppleSmartIOCommand`
- `bool AppleSmartIOCommandPool::_initWithOptions(IOWorkLoop *, unsigned int)`
- `_sdma != nullptr`
- `MCA6_RX`
- `maxSize < 0xFF`
- `ASIO WARNING: SetParameter got unexpected return %d\n`
- `(numEntries * sizeof(UInt32)) == data->getLength()`
- `AppleSmartIODMANub`
- `AOP_MCA0_TX`
- `AOP_MCA1_RX`
- `SPI2_TX`
- `AP->SIO`
- `\"Timeout waiting for stop to idle on EP %s(%d) CS: %d\" @%s:%d`
- `\"got DMA completion with unexpected tag %u on EP %s(%d)\" @%s:%d`
- `site.AppleSmartIODMANub`
- `SPI0_RX`
- `(numEntries <= MAX_SUPPORTED_PIO_RANGE) && (numEntries <= kMaxMapRange) && ((numEntries * sizeof(map_range_dt_entry_t)) == data->getLength())`
- `data != nullptr`
- `void AppleSmartIOPerf::setupPerfBuffer()`
- `121111121222121211121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121212121111111111`
- `ASIO WARNING: timed out waiting for space for %u segments\n`
- `_commands_in_flight > 0`
- `Control`
- `SPI3_RX`
- `SPI4_RX`
- `AOP_LEAP10_RX`
- `AOP_LEAP12_TX`
- `AppleSmartIO (RTBuddy-based)::start (%p) - (%s@%s)\n`
- `virtual AppleSmartIOEndpoint *AppleSmartIO::endpointForHandle(OSObject *, IOSlaveEndpoint::Action, UInt32, IODMAEventSource *)`
- `virtual void AppleSmartIOEndpoint::ep_enable()`
- `AOP_LEAP11_RX`
- `\"Unexpected SIO Protocol version %u - %u\" @%s:%d`
- `IOReturn AppleSmartIOUserClient::_extPing()`
- `IOReturn AppleSmartIOEndpoint::getParam(SmartIOParameter, UInt32 *)`
- `dataLength % sizeof(powergate_entry_t) == 0`
- `_sio_regs_memory`
- `IOReturn AppleSmartIODMA::_setFIFODepth(IOByteCount *)`
- `\"unexpected opcode %u received on EP %s(%d)\" @%s:%d`
- `AOP_LEAP2_TX`
- `role`
- `smartio_debug`
- `dataLength > 0`
- `SmartIOResponseBuffer *AppleSmartIODMAController::responseForEndpointAndTag(UInt32, UInt32)`
- `state != nullptr`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIO.h`
- `shimType < kMaxShim`
- `MCA3_RX`
- `root`
- `IOUserClientEntitlements`
- `_enable_count > 0`
- `_nub != nullptr`
- `bool AppleSmartIODMANub::initWithRegistryEntry(AppleSmartIO *, IORegistryEntry *)`
- `SPI5_RX`
- `MCA1_TX`
- `PDM0_RX`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOEndpoint.cpp`
- `ASIO WARNING: GetParameter got unexpected return %d\n`
- `_work_loop->addEventSource(_command_gate) == kIOReturnSuccess`
- `virtual IOReturn AppleSmartIODMAController::stopDMACommand(UInt32, bool, UInt64)`
- `SPI0_TX`
- `UART2_RX`
- `UART8_TX`
- `AOP_LEAP6_TX`
- `ASIO WARNING: no configuration data for client\n`
- `23:19:39`
- `1`
- `ASIO WARNING: SmartIO: send_command - unexpected return %d\n`
- `site.AppleSmartIOPerf`
- `MCA9_TX`
- `AOP_LEAP8_TX`
- `void AppleSmartIOControl::sendSIORegisters()`
- `site.AppleSmartIODMAController`
- `virtual IOReturn AppleSmartIODMAController::setFIFODepth(UInt32, IOByteCount)`
- `SmartIODMABuffer *AppleSmartIODMAController::bufferForHandle(BufferHandle)`
- `virtual bool AppleSmartIOUserClient::start(IOService *)`
- `dma-channels`
- `DPA2_TX`
- `MCA10_TX`
- `kIOReturnSuccess == status`
- `com.apple.driver.AppleSmartIO2.user-client`
- `IOWorkLoop *AppleSmartIOEndpoint::getWorkLoop()`
- `virtual bool AppleSmartIOEndpoint::allocateCommandPool(IOWorkLoop *, unsigned int)`
- `void AppleSmartIOControl::sendPowerConfig()`
- `msgw.gmsg.endpoint == SmartIOEndpoint::kEndpointControl`
- `\"Endpoint %s(%d) being used by parent driver before start.\" @%s:%d`
- `SIO->AP`
- `(msgw->gmsg.endpoint < _max_endpoints) && (_endpoints[msgw->gmsg.endpoint] != nullptr)`
- `AppleSmartIOPerf`
- `AppleSmartIODMAController`
- `SmartIODMASegment *AppleSmartIODMAController::segmentForHandle(BufferHandle)`
- `UInt32 AppleSmartIO::getshimActiveChannelCount(UInt32)`
- `AOP_LEAP0_TX`
- `AppleSmartIOCommandPool`
- `shim-power-gate`
- `service-gates`
- `UART6_TX`
- `AOP_LEAP0_RX`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOUserClient.cpp`
- `iodm`
- `result == kIOReturnSuccess`
- `virtual IOByteCount AppleSmartIODMAController::validFIFODepth(UInt32, IOByteCount, IODirection)`
- `IOReturn AppleSmartIODMA::setParam(SmartIOParameter, UInt32)`
- `SPI1_RX`
- `MCA4_TX`
- `ASIO: EP: %d TAG: %d OP: %d PARAM: %#02X DATA: %#08X %s %s\n`
- `AppleSmartIOEndpoint.cpp`
- `_pio_memory`
- `IOService::init(withEntry, gIODTPlane)`
- `UART7_RX`
- `IOReturn AppleSmartIOUserClient::_extForcePanic()`
- `asio != nullptr`
- `_ps_regs_memory`
- `ASIO: Shim Configured: EP: %s(%2d) XFER:%#08X TIMEOUT: %d FIFO: %d TRIGGER: %d LIMIT: %d\n`
- `MCA5_RX`
- `121111121222121212111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111122222222221111`
- `void AppleSmartIO::_message_unwrap(mbi_msg_t, MessageWrapper *)`
- `\"got unexpected 'tag' on message from SmartIO: EP: %s(%2d) TAG: %d OP: %3d PARAM: %#02X DATA: %#08X\" @%s:%d`
- `!queue_empty(&_dmaStartCommands)`
- `UInt64 AppleSmartIOControl::_getDARTMapping(UInt64, UInt64, IODMACommand *&)`
- `Unknown`
- `UART3_TX`
- `result`
- `perf != nullptr`
- `index < kMaxMapRange`
- `_response_memory != nullptr`
- `DPA0_TX`
- `1211111212221212111111111111`
- `IOReturn AppleSmartIOUserClient::_extResetPerf()`
- `IOReturn AppleSmartIOUserClient::_extQueryPerf(struct PerfData *)`
- `_command_gate != nullptr`
- `getWorkLoop()->inGate()`
- `void AppleSmartIOControl::setupMapRanges()`
- `sdma != nullptr`
- `AOP_MCA3_RX`
- `_slaveProcessor->setPowerState(kRtbPowerStateSleep, nullptr) == kIOReturnSuccess`
- `_asio != nullptr`
- `ASIO: expected output structure\n`
- `ASIO: Sending Sync Message: EP: %d TAG:%d OP: %d PARAM: %d DATA: %#08X StartTime: %lld\n`
- `IOReturn AppleSmartIOEndpoint::setParam(SmartIOParameter, UInt32)`
- `_panic_memory != nullptr`
- `map-range`
- `MCA1_RX`
- `AOP_PDM0_RX`
- `ASIO WARNING: no DMA controller nub in the devicetree (1)\n`
- `site.AppleSmartIOEndpoint`
- `121121122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `_perf_memory != nullptr`
- `state->response != nullptr`
- `AOP_LEAP3_RX`
- `endpoint != nullptr`
- `virtual IOReturn AppleSmartIOEndpoint::synchronousMessage(AppleSmartIOCommand *, void *)`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOControl.cpp`
- `range < kMaxMapRange`
- `enable-shim-power-gating`
- `_devices_memory`
- `index < kMaxSIORegisters`
- `MCA8_TX`
- `AOP_LEAP4_TX`
- `AOP_LEAP6_RX`
- `site.AppleSmartIOCommandPool`
- `type < kMaxShim`
- `AppleSmartIOPerf.cpp`
- `_work_loop != nullptr`
- `\"dma-channels config incorrect length\" @%s:%d`
- `Perf`
- `\"Failed to retrieve SIO Protocol Version\" @%s:%d`
- `IOUserClientDefaultLocking`
- `ASIO: client buffer is a memory descriptor instead of a pointer, likely too big\n`
- `IOReturn AppleSmartIOEndpoint::send_command(UInt8)`
- `virtual IOByteCount AppleSmartIODMAController::getFIFODepth(UInt32, IODirection)`
- `(endpoint_index * COMMANDS_PER_ENDPOINT) + (tag - 1) < (SmartIOEndpoint::kMaxEndpoint * COMMANDS_PER_ENDPOINT)`
- `_admin_commands != nullptr`
- `AOP_LEAP9_TX`
- `\"AppleSmartIO: sent unexpected async Message: EP: %2d TAG: %d OP: %3d PARAM: %#02X DATA: %#08X\" @%s:%d`
- `bool AppleSmartIODMA::_initWithOptions(AppleSmartIO *, AppleSmartIODMAController *, IODMAEventSource *, UInt32)`
- `_config != nullptr`
- `IOReturn AppleSmartIODMA::_startDMACommand(IODMACommand *, IOByteCount *, IOByteCount *)`
- `SPI5_TX`
- `MCA6_TX`
- `UART3_RX`
- `/Library/Caches/com.apple.xbs/EAA9B733-A1DA-4E0A-BE3D-CF401702D627/TemporaryDirectory.CURToW/Sources/AppleSmartIO2/AppleSmartIO/AppleSmartIOPerf.cpp`
- `_commands_in_flight >= 0`
- `MCA5_TX`
- `AOP_LEAP1_RX`
- `AOP_LEAP2_RX`
- `AOP_LEAP8_RX`
- `dump-ps-regs`
