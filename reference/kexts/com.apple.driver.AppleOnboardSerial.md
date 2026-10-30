# `com.apple.driver.AppleOnboardSerial`

- Name: AppleOnboardSerial
- Version: `1.0`
- UUID: `F86BC733-3035-3EF5-BADB-D01AF5324B69`
- Source version: `211.0.0.0.0`
- Depends on: [`com.apple.iokit.IOSerialFamily`](com.apple.iokit.IOSerialFamily.md) 1.0.4, [`com.apple.iokit.IOSkywalkFamily`](com.apple.iokit.IOSkywalkFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleOnboardSerialBSDClient
- `CFBundleIdentifier`: `com.apple.driver.AppleOnboardSerial`
- `IOClass`: `AppleOnboardSerialBSDClient`
- `IOMatchCategory`: `AppleOnboardSerialBSDClient`
- `IOPersonalityPublisher`: `com.apple.driver.AppleOnboardSerial`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleOnboardSerialSync`
- `IOResourceMatch`: `IOBSD`


## C++ classes (14) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleMMIOSerial` | 0xb0 | AppleOnboardSerialBusInterface → IOService → IORegistryEntry |
| `AppleOnboardSerialBSDClient` | 0x118 | IOService → IORegistryEntry |
| `AppleOnboardSerialBusInterface` | 0x98 | IOService → IORegistryEntry |
| `AppleOnboardSerialDebugDevice` | 0x10 |  |
| `AppleOnboardSerialPool` | 0x38 | IOCommandPool |
| `AppleOnboardSerialSkywalkInterface` | 0xf8 | IOSkywalkInterface → IOService → IORegistryEntry |
| `AppleOnboardSerialSkywalkPacketPool` | 0xc0 | IOSkywalkPacketBufferPool |
| `AppleOnboardSerialSync` | 0x98 | IOSerialStreamSync → IOService → IORegistryEntry |
| `AppleSimpleUARTCommand` | 0xd0 | IODMACommand → IOCommand |
| `AppleSimpleUARTSync` | 0x608 | AppleOnboardSerialSync → IOSerialStreamSync → IOService → IORegistryEntry |
| `IOConditionGate` | 0x60 | IOEventSource |
| `IOSimpleMbufMemoryDescriptor` | 0x70 | IOMemoryDescriptor |
| `OSLiveNumber` | 0x18 |  |
| `_HACK_RingBuffer` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000020d8 off=0x00685d20-0x00687df8 addr=0xfffffe0007689d20-0xfffffe000768bdf8 r--/r--   __TEXT            
	sz=0x0000192f off=0x00686438-0x00687d67 addr=0xfffffe000768a438-0xfffffe000768bd67               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000088 off=0x00687d70-0x00687df8 addr=0xfffffe000768bd70-0xfffffe000768bdf8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00012040 off=0x022ddd90-0x022efdd0 addr=0xfffffe00092e1d90-0xfffffe00092f3dd0 r-x/r-x   __TEXT_EXEC       
	sz=0x00011810 off=0x022ddd90-0x022ef5a0 addr=0xfffffe00092e1d90-0xfffffe00092f35a0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000830 off=0x022ef5a0-0x022efdd0 addr=0xfffffe00092f35a0-0xfffffe00092f3dd0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000007b0 off=0x049828d8-0x04983088 addr=0xfffffe000b9868d8-0xfffffe000b987088 rw-/rw-   __DATA            
	sz=0x00000280 off=0x049828d8-0x04982b58 addr=0xfffffe000b9868d8-0xfffffe000b986b58               __DATA.__data             
	sz=0x000002a8 off=0x00000000-0x000002a8 addr=0xfffffe000b986b58-0xfffffe000b986e00               __DATA.__common           (Zerofill)
	sz=0x00000288 off=0x00000000-0x00000288 addr=0xfffffe000b986e00-0xfffffe000b987088               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00003bf8 off=0x01180408-0x01184000 addr=0xfffffe0008184408-0xfffffe0008188000 rw-/rw-   __DATA_CONST      
	sz=0x00000058 off=0x01180408-0x01180460 addr=0xfffffe0008184408-0xfffffe0008184460         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000058 off=0x01180460-0x011804b8 addr=0xfffffe0008184460-0xfffffe00081844b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00003280 off=0x011804b8-0x01183738 addr=0xfffffe00081844b8-0xfffffe0008187738         __DATA_CONST.__const            
	sz=0x00000380 off=0x01183738-0x01183ab8 addr=0xfffffe0008187738-0xfffffe0008187ab8         __DATA_CONST.__kalloc_type      
	sz=0x00000064 off=0x01183ab8-0x01183b1c addr=0xfffffe0008187ab8-0xfffffe0008187b1c         __DATA_CONST.__assert           
	sz=0x00000418 off=0x01183b20-0x01183f38 addr=0xfffffe0008187b20-0xfffffe0008187f38         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000c0 off=0x01183f38-0x01183ff8 addr=0xfffffe0008187f38-0xfffffe0008187ff8         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01183ff8-0x01184000 addr=0xfffffe0008187ff8-0xfffffe0008188000         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 286 at 0x04ae0be4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F86BC733-3035-3EF5-BADB-D01AF5324B69
008: LC_SOURCE_VERSION           211.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab6f8 size=0x260
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleOnboardSerial`
- `CFBundleGetInfoString`: `Copyright © 2018-2026 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleOnboardSerial`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleOnboardSerial`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Safe Boot`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleOnboardSerial.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898959072`
- `_PrelinkExecutableRelativePath`: `AppleOnboardSerial`
- `_PrelinkExecutableSize`: `99520`
- `_PrelinkExecutableSourceAddr`: `-2198898959072`
- `_PrelinkKmodInfo`: `-2198828717864`

## Strings (243) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `serial state`
- `%s:%d avail=%u`
- `%s:%d unknown event=%#x<%d:%d>`
- `setStateInternal`
- `programRTS`
- `AppleOnboardSerialSkywalkInterface`
- `#### Init: no node for %s\n`
- `AppleOnboardSerialBSDClient: could not make kernel control socket for %s: %d\n`
- `%s:%d (direction=%d, count=%d, offset=%d)`
- `%s:%d _maxBaud=%d.%d, _FIFOSize=%d, _dmaSupport=%#x`
- ` enqueue{%p} `
- `rxUpdateDMA`
- `txDataSendInternal`
- `site.AppleOnboardSerialBSDClient`
- `%s.debug.dma_max_commands`
- `%s:%d count=%lu`
- `1211111212221212111112`
- `%s:%d (%p): _rxMode=%x _rxDMACount=%u _rxQueueHeadCount=%llu ret=%x`
- `rxStartDMA`
- `AppleOnboardSerialPool`
- `uart%d`
- `%s:%d (%p *%08x, %08x):`
- `%s:%d => %#x`
- `AppleOnboardSerialSkywalkPacketPool`
- `%s:%d (%d,%d):`
- `%s:%d (%#x<%d:%d>, %#x):`
- `dequeueEvent`
- `nextEvent`
- `rxUpdateQueueState`
- `>>> %s:[%d] %p Warning \"%s\"\n`
- `%s:%d (%p, %p):`
- `%s:%d => %#x _rxDMACount=%u`
- `saveUART`
- `121112222221111111111112`
- `uart.log.size`
- `serial`
- `uart.panic_on_delay`
- ` dequeue{%p} `
- `executeEventFiltered`
- `rxStopDMA`
- `121`
- `com.apple.uart.%s`
- `%s:%d enqueue failed (_rxDMACount=%d)`
- `AppleOnboardSerialBSDClient`
- `uart.%s%s`
- `%s: could not enqueue data (%d)\n`
- `%s::%s: error starting DMA: %s\n`
- `resetUART`
- `#### Init: no debugBuffer for %s\n`
- `AppleOnboardSerialBSDClient: could not make skywalk-enabled socket for %s\n`
- `%s:%d (%08x, %08x):`
- `site.AppleOnboardSerialPool`
- `DevWrite: logging %s`
- `Identified Serial Port %s at %#llx(%#llx)\n`
- `%s:%d (%08x, %08x, %#x): _state=%08x`
- `%s:%d () _txCommandsPending=%d`
- `AppleSimpleUARTSync.cpp`
- `%s:%d => %#x (%lld<->%lld)`
- `%s:%d command %p not found`
- `IOConditionGate.cpp`
- `requestEvent`
- `%s:%d  [ %p:%#x %lu,%lu %lu %llu %#x ]`
- `enqueueData(mbuf_t):completion`
- `site.IOConditionGate`
- `IOSkywalkNexusUUID`
- `%s:%d overrun: _rxStatus=%#x`
- `1211111212221212111111221121212122212211211211111122222211211111111111111111111111111111111111211111111111111111111111111111111111111111111111111111111111111112111111111111111111111111111111112`
- `%s:%d => %#x state=%08x`
- `rxUpdateDMAQueueState`
- `1211211`
- `%s:%d (%llu): _rxQueueHeadCount=%lld`
- `OSLiveNumber`
- `uart.log.level`
- `%s:%d => %#x _state=%08x`
- `%s:%d => %#x count=%d`
- `site.AppleOnboardSerialSkywalkInterface`
- `enqueueRxPackets: no packet available\n`
- `uart.debug.trap`
- `%s:%d => _state=%08x`
- `Soft`
- `%s:%d (%p, %d, %d, %p):`
- `com.apple.uart.sk.%s`
- `txDataGated`
- `%s:%d =>`
- `%s:%d  _rxMbufEventCallback: event=%#x data=%#x`
- `%s:%d (%p:%lu, %#x, %lu):`
- `#### %s: override dma-max-commands=%d\n`
- `getState`
- `%s:%d (overrun=%d, gotBreak=%d, framingError=%d, parityError=%d):`
- `site.AppleOnboardSerialSkywalkPacketPool`
- `dcc`
- `serial baud rate`
- `executeEvent`
- `rxCompleteCommandGated`
- `%s:%d (%d,%d): _state=%#x, _suspend=%d`
- `%s:%d (%p, %p, %p):`
- `dequeueData`
- `%s:%d cannot enqueue command (#x)\n`
- `AppleSimpleUARTCommand`
- `AppleSimpleUARTSync`
- `AppleOnboardSerialBSDClient: could not make sk kernel control socket for %s: %d\n`
- `AppleOnboardSerialBSDClient: could not allocate device node for %s\n`
- `%s:%d => ret=%#x event=%#x<%d:%d>`
- `\"AppleOnboardTestBSDClient::watchDogTimer detected an unexpected delay in ctl_send()\\n\" @%s:%d`
- `_txStopDMA`
- `AppleSimpleUARTSync::rxErrorInterrupt(%s, overrun=%d, gotBreak=%d, framingError=%d, parityError=%d)\n`
- `0123456789abcdef`
- `uart%u`
- `AppleOnboardSerialBSDClient.cpp`
- `site.AppleOnboardSerialSync`
- `current==((last+1)%4)`
- `%s:%d (%d) _rxDMACount=%d`
- `AppleOnboardSerialParent%08X`
- `%s:%d cannot allocate mbuf for command %p\n`
- `hwEnqueueDMA`
- `HiddenPort`
- `%s:%d (%llu):`
- `%s:%d (%p, %u, %p, %u):`
- `%s:%d (%u.%u)`
- `IOSimpleMbufMemoryDescriptor`
- `%s: Serial %sware Overflow\n`
- `%s:%d (%#x<%d:%d>, %#x, %d):`
- `%s::%s: error starting DMA at base offset %lld: %s\n`
- `%s:%d  rxQueueCount=%lu, _rxStatus=%#x transferCount=%lu, _rxTimeoutInterval=%d, _rxQueueTailCount=%d`
- `%s:%d => %#x transferCount=%d`
- `boot-console`
- `acquirePort`
- `%s:%d ():`
- `%s:%d => %#x event=%#x<%d:%d> data=%#x`
- `%s:%d => %#x wake error`
- `uart.log`
- `%s:%d => %#x offline`
- `12112121212212`
- `_HACK_RingBuffer`
- `AppleMMIOSerial`
- `serial stop bits`
- `dmaCompleteCommand`
- `rxDataInterrupt`
- `%s:%d bad state change %#x => %#x`
- `1211111212221212111`
- `Hard`
- `AppleOnboardSerialSync`
- `rxDataGated`
- `%s:%d rts=%d`
- `1211111212221212111111111111111`
- `_HACK_debugDevWrite`
- `AppleOnboardSerialDebug.cpp`
- `%s:%d (%p, %d):`
- ` %s{%p} `
- `%s:%d (%p, %d, %p, %d):`
- `%s:%d (%p, %d, %d): _rxMode=%#x`
- `%s:%d (%p, %08x): *state=%08x watchForInactive=%d`
- `DevWrite: debugLevel=%d`
- `%s:%d (%#x<%d:%d>, %p):`
- `rxErrorInterrupt`
- `IOConditionGate`
- `site._HACK_RingBuffer`
- `%s:%d cannot read data retval=%d\n`
- `serial data width`
- `%s:%d _rxMbuf: PD_E_SW_OVERRUN_ERROR`
- `%s:%d () _rxMode=%d`
- `rxMbufInterruptEventGated`
- `%s:%d => %#x (%lld<->%d)`
- `AppleOnboardSerialBSDClient: could not make devfs node for %s\n`
- `%s:%d (): _state=%#x`
- `%s:%d avail=%lu`
- `%s:%d _dataWidth=%u.%u, _stopBits=%u.%u, _parity=%u, _baudRate=%u.%u, level=%u`
- `121112111211`
- `watchState`
- `registerEventFilter`
- `%s:%d uio=%p size=%d`
- `\n`
- `start`
- `%s:%d (%p) direction=%d actualByteCount=%llu status=%#x`
- `%s:%d  [ %p:%#x %lu,%lu %lu %llu %#x ] byteCount=%lu`
- `builtin-serial`
- `enqueueEvent`
- `registerMbufCallback`
- `\"actualByteCount is smaller than buffer size\\n\" @%s:%d`
- `%s:%d cannot reset mbuf for command %p\n`
- `%s:%d => _rxQueueHeadCount=%llu`
- `12122`
- `%s %lu.%03lu `
- `IOTTYBaseName`
- `site.AppleSimpleUARTSync`
- `\"%s: Serial Debug Trap for datarate=%d (%d)\" @%s:%d`
- `%s%s`
- `>>> %s:[%d] %p SoftAssert (%s) failed\n`
- `DevWrite: _uartName=%s, _debugLevel=%d\n`
- `enqueueData`
- `%s:%d (): `
- `_newCommandWait`
- `site.AppleOnboardSerialDebugDevice`
- `dma-max-commands`
- `AppleOnboardSerialBusInterface`
- `12111112122212121121221211222111221`
- `%s:%d error send uart<n> or <loglevel>\n`
- `%s: AppleOnboardSerialBSDClient recevied unexpected serial event %#llx/%#llx\n`
- `#### Init: debug enabled for %s\n`
- `err == 0`
- `%s:%d => %#x data=%#x`
- `%s:%d (%p):`
- `%s:%d (): _rxMode=%d _rxQueueLength=%d`
- `%s:%d  queue_enter[ %p:%#x %lu,%lu %lu %llu %#x ]`
- `programUART`
- `(*mdesc) != NULL`
- `site.OSLiveNumber`
- `#### Init: no major for %s\n`
- `IOTTYSuffix`
- `site.AppleMMIOSerial`
- `uart`
- `serial flow control`
- `%s:%d unknown event=%#x<%d:%d> data=%#x`
- `rxResizeQueue`
- ` %s{%p}: `
- `12111222111222122222221112`
- `restoreUART`
- `AppleOnboardSerial`
- `%s:%d out of mbufs (_rxDMACount=%d)`
- `!workLoop->inGate()`
- `no-control-socket`
- `%s: more than one subnode in device tree!  Ignoring all but the first.\n`
- `debug`
- `%s:%d bad watch mask %#x`
- `site.IOSimpleMbufMemoryDescriptor`
- `12`
- `watchStateInternal`
- `%s:%d (%08x, %08x, %#x): => 0 _state=%08x`
- `AppleSimpleUARTSync::txDataGated: incomplete\n`
- `rxAutobaudInterrupt`
- `uart.skywalk`
- `%s:%d (%p, %p, %d):`
- `%s:%d (): _rxMode=%d`
- `AppleOnboardSerialDebugDevice`
- `setState`
- `%s:%d () => %#x before=%d after=%d consumed=%d`
- `%s:%d  %c[ %p:%#x:%d %lu,%lu %lu %llu %#x ] ret=%#x`
- `releasePort`
- `site.AppleOnboardSerialBusInterface`
- `serial parity`
- `rxMbufDataCallback`
- `%s:%d => %p`
- `site.AppleSimpleUARTCommand`
