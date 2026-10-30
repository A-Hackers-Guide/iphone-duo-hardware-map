# `com.apple.driver.AppleSPMI`

- Name: AppleSPMI
- Version: `1.0.1`
- UUID: `324054AB-6F51-3C5C-85CD-A06BD4033F31`
- Source version: `143.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (5) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/nub-spmi0`](../devicetree/root__arm-io__nub-spmi0.md) | `AppleSPMIController` | `aapl,spmi` |
| [`/arm-io/nub-spmi1`](../devicetree/root__arm-io__nub-spmi1.md) | `AppleSPMIController` | `aapl,spmi` |
| [`/arm-io/nub-spmi2`](../devicetree/root__arm-io__nub-spmi2.md) | `AppleSPMIController` | `aapl,spmi` |
| [`/arm-io/aop-spmi0`](../devicetree/root__arm-io__aop-spmi0.md) | `AppleSPMIController` | `aapl,spmi` |
| [`/arm-io/aop-spmi1`](../devicetree/root__arm-io__aop-spmi1.md) | `AppleSPMIController` | `aapl,spmi` |

## IOKit personalities (1) [KC]

### AppleSPMIController
- `CFBundleIdentifier`: `com.apple.driver.AppleSPMI`
- `IOClass`: `AppleSPMIController`
- `IONameMatch`: `aapl,spmi`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSPMI`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSPMIController` | 0x1ac8 | AppleARMSPMIController → IOInterruptController → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000032e3 off=0x0076c740-0x0076fa23 addr=0xfffffe0007770740-0xfffffe0007773a23 r--/r--   __TEXT            
	sz=0x000000f8 off=0x0076ce60-0x0076cf58 addr=0xfffffe0007770e60-0xfffffe0007770f58               __TEXT.__const            
	sz=0x00001f06 off=0x0076cf58-0x0076ee5e addr=0xfffffe0007770f58-0xfffffe0007772e5e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000bc5 off=0x0076ee5e-0x0076fa23 addr=0xfffffe0007772e5e-0xfffffe0007773a23               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000b1bc off=0x026a3630-0x026ae7ec addr=0xfffffe00096a7630-0xfffffe00096b27ec r-x/r-x   __TEXT_EXEC       
	sz=0x0000ae6c off=0x026a3630-0x026ae49c addr=0xfffffe00096a7630-0xfffffe00096b249c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000350 off=0x026ae49c-0x026ae7ec addr=0xfffffe00096b249c-0xfffffe00096b27ec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000108 off=0x04997b38-0x04997c40 addr=0xfffffe000b99bb38-0xfffffe000b99bc40 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04997b38-0x04997bfc addr=0xfffffe000b99bb38-0xfffffe000b99bbfc               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b99bc00-0xfffffe000b99bc38               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000b99bc38-0xfffffe000b99bc40               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002a60 off=0x012036b8-0x01206118 addr=0xfffffe00082076b8-0xfffffe000820a118 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012036b8-0x012036c0 addr=0xfffffe00082076b8-0xfffffe00082076c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012036c0-0x012036c8 addr=0xfffffe00082076c0-0xfffffe00082076c8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002278 off=0x012036c8-0x01205940 addr=0xfffffe00082076c8-0xfffffe0008209940         __DATA_CONST.__const            
	sz=0x000003c0 off=0x01205940-0x01205d00 addr=0xfffffe0008209940-0xfffffe0008209d00         __DATA_CONST.__kalloc_type      
	sz=0x00000230 off=0x01205d00-0x01205f30 addr=0xfffffe0008209d00-0xfffffe0008209f30         __DATA_CONST.__kalloc_var       
	sz=0x000001a8 off=0x01205f30-0x012060d8 addr=0xfffffe0008209f30-0xfffffe000820a0d8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x012060d8-0x01206118 addr=0xfffffe000820a0d8-0xfffffe000820a118         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 114 at 0x04ae5ac8
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     324054AB-6F51-3C5C-85CD-A06BD4033F31
008: LC_SOURCE_VERSION           143.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab1ad0 size=0x148
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSPMI`
- `CFBundleIdentifier`: `com.apple.driver.AppleSPMI`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSPMI`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSPMI.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898014400`
- `_PrelinkExecutableRelativePath`: `AppleSPMI`
- `_PrelinkExecutableSize`: `69639`
- `_PrelinkExecutableSourceAddr`: `-2198898014400`
- `_PrelinkKmodInfo`: `-2198828631240`

## Strings (339) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Engine disconnect -- Watchdog timeout for transmission`
- `21121111`
- `[%s]:%s:%d:[error] Entry %d: %X\n`
- `[%s]:%s:%d:[error]   [%d] = 0x%02X  parity=%s\n`
- `BusPr-CmdUnrecog`
- `SW_0 req queue overflow`
- `SW_2 rsp queue underflow`
- `Engine disconnect -- Bus contention: transmission request`
- `[%s]:%s:%d:[error] No SPMI Generation!\n`
- `[%s]:%s:%d:[error] addEventSource(spmiFaultIES)\n`
- `[%s]:%s:%d:[error] IOReporters\n`
- `None-Gen1`
- `xspmi`
- `fatal-interrupts`
- `site.const char *`
- `Could not reset queue queueStatus:%x, resetArbiterStatus:0x%x\n`
- `None-Gen3`
- `[%s]:%s:%d:[error] faultMemoryMap\n`
- `queue-depth`
- `%s.qf`
- `ok`
- `Not enough space %0x < %0lx\n`
- `Engine disconnect -- Bus contention: transmission arbitration`
- `[%s]:%s:%d:[error] spmiIES\n`
- `[%s]:%s:%d:[error] addEventSource(spmiIES)\n`
- `spmi fault`
- `yes`
- `SLEEP`
- `SOC-SW3-RspUnf`
- `spmi-panic-dump-queue`
- `verifyHeaderMatch`
- `Fault queue circular buffer, newest entries printed last: fault,time_sec,time_msec\n`
- `SW_3 req queue overflow`
- `SOC-TxFltr`
- `Any transmit filter write when write disabled`
- `AppleSPMIController`
- `EXT_REG_RD`
- `AUTH`
- `SOC-HWQ-OvfUnf`
- `11211222222222222222122222222`
- `all-spmi.irq`
- `[%s]:%s:%d:[error] fault - 0x%08X\n`
- `REG_0_WR`
- `Queue Pointers:\nResponse read: %d write: %d\nRequest read: %d write: %d\n`
- `[%s]:%s:%d:[error] vectors\n`
- `Address Parity`
- `LPL collision`
- `performPayloadlessTransaction`
- `Any HW Q soft reset when write disabled`
- `11211222222222222222122222122`
- `Engine FSM: 0x%X, Engine Status: 0x%X, Queue FSM: 0x%X\n`
- `initializeFaultInterrupts`
- `REG_RD`
- `SOC-BL-ReqOvf`
- `0x%X`
- `BackLight req queue overflow`
- `aot-power`
- `gen`
- `no`
- `ExtOp-NoACK`
- `no response`
- `SW_1 req queue overflow`
- `Engine disconnect -- Bad command`
- `[%s]:%s:%d:[error] interrupts\n`
- `site.IOInterruptVector`
- `LD_WR`
- `Could not get memory map\n`
- `Engine disconnect -- Bus contention: transmission command frame`
- `Engine disconnect -- MPL collision`
- `ENG_DIS`
- `no provider name\n`
- `[%s]:%s:%d:[error] workoop\n`
- `[%s]:%s:%d: Gen%d\n`
- `.kdbg`
- `SW_2 req queue overflow`
- `Bus contention -- connecting to bus: SDATA`
- `spmi-intmode-dis`
- `[%s]:%s:%d:[error] Queues not empty at startup\n`
- `fifoQueuesEmpty`
- `Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X`
- `[%s]:%s:%d: ret=0x%08x\n`
- `\"%s\" @%s:%d`
- `Fault rsp queue underflow`
- `None-Gen5`
- `[%s]:%s:%d: behaviorMap 0x%04x\n`
- `%X,`
- `[%s]:%s:%d: reqs:%u popQueue hdr 0x%08X\n`
- `REG_WR`
- `RESET`
- `BackLight Q request overflow`
- `%d,0x%X,0x%X,0x%X\n`
- `BUS_CON`
- `.qf`
- `[%s]:%s:%d: Copied %d entries\n`
- `ExtOp-NoRSP`
- `SOC-WrDis-Fltr`
- `SOC-BLQ-ReqOvf`
- `BackLight Q response underflow`
- `Bus contention -- Command frame`
- `DDB_FL_RD`
- `BusPr-CmdPrty-BOM`
- `HW_APB`
- `BusPr-Disconnect`
- `[%s]:%s:%d: pushQueue hdr 0x%08X interrupts:%u\n`
- `0x%08X,0x%08X,0x%08X\n`
- `SOC-HW1-ReqOvf`
- `Fault Counters:\n`
- `Could not map fault counters\n`
- `[%s]:%s:%d: pushQueue pay 0x%08X\n`
- `[%s]:%s:%d: popQueue hdr 0x%08X\n`
- `\nBad Response Count: %d\n`
- `fault-counters-enabled`
- `Bus contention -- arbitration`
- `site.char`
- `[%s]:%s:%d:[error] spmiMemoryMap\n`
- `spmi-fault-dis`
- `InterruptControllerName`
- `unmapped write`
- `MPL collision`
- `SW_1 rsp queue underflow`
- `Index,Response,Request\n`
- `BusPr-Contention`
- `spmi-fault-msg`
- `[%s]:%s:%d: Process responses request_count:%u, timeout:%uus\n`
- `WAKEUP`
- `Response queue:\n`
- `Bus contention -- Data frame`
- `error-interrupts`
- `executeCommand`
- `queue-reset`
- `HW_DIS`
- `None-Gen4`
- `[%s]:%s:%d:[error] getHeaderMatch failed, ret=%08x\n`
- `[%s]:%s:%d: %s\n`
- `SOC-SW3-ReqOvf`
- `Any SW Q overflow/underflow`
- `polling-mode`
- `[%s]:%s:%d:[error] spmiFaultIES\n`
- `SPMI read out-of-bounds multi`
- `resetQueueBase`
- `UNKN`
- `SOC-HW0-ReqOvf`
- `SOC-SW1-ReqOvf`
- `SOC-HW1-RspUnf`
- `super::start(provider)=false\n`
- `[%s]:%s:%d: Start\n`
- `[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X irq status: %#X num tries: %d bad responses: %s\n`
- `[%s]:%s:%d: reset arbiter was successful!\n`
- `SW_BLK`
- `%s - Failed to allocate memory for paniclog string with debug info`
- `SOC-BL-RspUnf`
- `None-Gen0`
- `interrupts`
- `[%s]:%s:%d:[error] parity error\n`
- `Could not map fault counters.`
- `HW_0 rsp queue underflow`
- `HW_1 rsp queue underflow`
- `site.uint64_t`
- `dumpResponseQueue`
- `[%s]:%s:%d: cmd:%u opts: 0x%08X\n`
- `[%s]:%s:%d: done\n`
- `[%s]:%s:%d:[error] Queues not empty at command start\n`
- `Data Parity`
- `[%s]:%s:%d:[error] Queues not empty at command end\n`
- `0x%X\n`
- `[%s] Fatal (%d) %s!`
- `AppleSPMIController.cpp`
- `Could not get virtual address of queue reset register.`
- `Event Log:\nBus pointer: %d num entries: %d\narb pointer: %d num entries: %d\n`
- `all-spmi.qf`
- `other-interrupts`
- `Fault Queue Empty\n`
- `BusPr-AdrPrty`
- `SOC-SW0-RspUnf`
- `Engine disconnect -- Bus contention: transmission SSC`
- `spmi-fault-panic`
- `max-transaction-time`
- `1`
- `[%s]:%s:%d: pushQueue hdr 0x%08X intEn:%u\n`
- `[%s]:%s:%d: popQueue pay 0x%08X\n`
- `Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X irq status: %#X num tries: %d bad responses: %s`
- `[%s]:%s:%d:[error] SPMI command timed out, respIrq=%d\n`
- `TRANS`
- `0x%X: %d\n`
- `Cmd Parity, BOM`
- `HW_0 req queue overflow`
- `BackLight rsp queue underflow`
- `Engine disconnect -- Bus contention: connect SCL`
- `None-Gen6`
- `getHeaderMatch`
- `%.20s.0x%02X`
- `SOC-SW0-ReqOvf`
- `extendedReadWriteCommand`
- `[%s]:%s:%d:[error] parity error: parity_rcv=0x%04X parity_exp=0x%04X\n`
- `copyFaultQueue`
- `EXT_REG_WRL`
- `DDB_LD_RD`
- `SOC-WrDis-Rset`
- `[%s]:%s:%d:[error] runPolledMode ret=%08x\n`
- `registerReadWriteCommand`
- `[%s]:%s:%d:[error] queuePopFailed, ret=%08x\n`
- `BusPr-ExtColl`
- `[%s]:%s:%d:[error] batchHeaders\n`
- `IOHibernateState`
- `None-Gen2`
- `[%s]:%s:%d:[error] waitForResponseFailed, ret=%08x\n`
- `SOC-FLT-RspUnf`
- `%s.irq`
- `dumpFaultQueue`
- `Bus contention -- ACK`
- `[%s]:%s:%d: entered polling mode!!!\n`
- `%s:%u Timeout header:%x queueStatus:%x USE_INTERRUPTS:%x intMode:%x\n`
- `[%s]:%s:%d: bytesQueued packetLen:%u\n`
- `Fault Queue status: 0x%08X, entries:\n`
- `ExtOp-RD`
- `unsupported read`
- `LD_RD`
- `ExtOp-WR`
- `SOC-SW2-RspUnf`
- `Cmd not recognized`
- `Any HW Q overflow/underflow`
- `Bus contention -- SSC sequence`
- `[%s]:%s:%d: waiting...\n`
- `[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X\n`
- `SW_0 rsp queue underflow`
- `%s: Skipping XSPMI controller\n`
- `[%s]:%s:%d: address 0x%X length:%u\n`
- `EXT_REG_RDL`
- `site.T`
- `Index,Arb Log,Bus Log Hi,Bus Log Lo\n`
- `Bus contention -- Address frame`
- `losesPowerInSleep`
- `HW_1 req queue overflow`
- `1121122222222222222212222122`
- `SOC-SWQ-OvfUnf`
- `Engine disconnect -- Bus contention: connect SDA`
- `SPMI Fault Interrupts`
- `SOC-HW0-RspUnf`
- `Engine disconnect -- Watchdog timeout for request`
- `[%s]:%s:%d: NACK\n`
- `handleFaultInterrupt`
- `Could not map queue reset register.`
- `Bus contention -- connecting to bus: SCLK`
- `.irq`
- `[%s]:%s:%d:[error] queuePop failed, ret=%08x\n`
- `SW_3 rsp queue underflow`
- `start`
- `Engine disconnect -- LPL collision`
- `site.AppleSPMIController`
- `[%s]:%s:%d:[error] queue-depth\n`
- `irq-behavior-map`
- `[%s]:%s:%d:[error] runInterruptMode ret=%08x\n`
- `%s: command %u unsupported`
- `BusPr-DatPrty`
- `[%s]:%s:%d:[error] Queues not empty reqEmpty: %s rspEmpty: %s\n`
- `EXT_REG_WR`
- ` (0x%08x)`
- `%s.kdbg`
- `[%s]:%s:%d: MQL=%08x for %08llx bytes of %s\n`
- `nack response`
- `[%s]:%s:%d:[error] handler init failed!\n`
- `req-resp-mismatch-no-panic`
- `%s Count`
- `SHUTDOWN`
- `SW_DIS`
- `Bus contention -- bus request`
- `Engine disconnect -- Command frame parity`
- `112112222222222222221222221222222`
- `waitForResponse`
- `SOC-SW1-RspUnf`
- `Cmd Parity, not BOM`
- `Any SW Q request transmission when blocked by filter`
- `121111121222121211111122212111112112221222221112122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `BusPr-CmdPrty-NoBOM`
- `Queue Status: 0x%X\n`
- `[%s]:%s:%d:[error] interruptControllerName\n`
- `BAD`
- `%s[%s]: `
- `%d,0x%X,0x%X\n`
- ` %s 0x%08x`
- `[%s]:%s:%d:[error] interruptLock\n`
- `SOC-SW2-ReqOvf`
- `SOC-BLQ-RspUnf`

**[__TEXT.__os_log]**

- `[%s]:%s:%d: pushQueue hdr 0x%08X interrupts:%u\n`
- `[%s]:%s:%d:[error] interrupts\n`
- `[%s]:%s:%d:[error] interruptControllerName\n`
- `[%s]:%s:%d:[error] spmiIES\n`
- `[%s]:%s:%d: NACK\n`
- `[%s]:%s:%d: address 0x%X length:%u\n`
- `[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X\n`
- `[%s]:%s:%d:[error] SPMI command timed out, respIrq=%d\n`
- `[%s]:%s:%d: %s\n`
- `[%s]:%s:%d:[error] workoop\n`
- `[%s]:%s:%d:[error] Queues not empty at startup\n`
- `[%s]:%s:%d: bytesQueued packetLen:%u\n`
- `[%s]:%s:%d:[error] queuePop failed, ret=%08x\n`
- `[%s]:%s:%d:[error] getHeaderMatch failed, ret=%08x\n`
- `[%s]:%s:%d:[error] fault - 0x%08X\n`
- `[%s]:%s:%d:[error] spmiMemoryMap\n`
- `[%s]:%s:%d: behaviorMap 0x%04x\n`
- `[%s]:%s:%d: pushQueue hdr 0x%08X intEn:%u\n`
- `[%s]:%s:%d:[error] waitForResponseFailed, ret=%08x\n`
- `[%s]:%s:%d:[error] parity error\n`
- `[%s]:%s:%d:[error] Queues not empty at command start\n`
- `[%s]:%s:%d: ret=0x%08x\n`
- `[%s]:%s:%d: entered polling mode!!!\n`
- `[%s]:%s:%d:[error] IOReporters\n`
- `[%s]:%s:%d:[error] runPolledMode ret=%08x\n`
- `[%s]:%s:%d: Copied %d entries\n`
- `[%s]:%s:%d: Gen%d\n`
- `[%s]:%s:%d:[error] batchHeaders\n`
- `[%s]:%s:%d:[error] Queues not empty reqEmpty: %s rspEmpty: %s\n`
- `[%s]:%s:%d:[error] Entry %d: %X\n`
- `[%s]:%s:%d: MQL=%08x for %08llx bytes of %s\n`
- `[%s]:%s:%d: pushQueue pay 0x%08X\n`
- `[%s]:%s:%d:[error] parity error: parity_rcv=0x%04X parity_exp=0x%04X\n`
- `[%s]:%s:%d:[error] No SPMI Generation!\n`
- `[%s]:%s:%d:[error] queue-depth\n`
- `[%s]:%s:%d:[error] addEventSource(spmiFaultIES)\n`
- `[%s]:%s:%d:[error] Request/Response header mismatch: Req: %#X Rsp: %#X cmd: %#X irq status: %#X num tries: %d bad responses: %s\n`
- `[%s]:%s:%d: Process responses request_count:%u, timeout:%uus\n`
- `[%s]:%s:%d:[error] queuePopFailed, ret=%08x\n`
- `[%s]:%s:%d:[error] Queues not empty at command end\n`
- `[%s]:%s:%d: reset arbiter was successful!\n`
- `[%s]:%s:%d: cmd:%u opts: 0x%08X\n`
- `[%s]:%s:%d:[error] interruptLock\n`
- `[%s]:%s:%d: Start\n`
- `[%s]:%s:%d:[error] faultMemoryMap\n`
- `[%s]:%s:%d:[error] handler init failed!\n`
- `[%s]:%s:%d:[error] vectors\n`
- `[%s]:%s:%d:[error] spmiFaultIES\n`
- `[%s]:%s:%d: popQueue pay 0x%08X\n`
- `[%s]:%s:%d:[error] addEventSource(spmiIES)\n`
- `[%s]:%s:%d:[error] runInterruptMode ret=%08x\n`
- `[%s]:%s:%d: reqs:%u popQueue hdr 0x%08X\n`
- `[%s]:%s:%d: waiting...\n`
- `[%s]:%s:%d: done\n`
- `[%s]:%s:%d: popQueue hdr 0x%08X\n`
- `[%s]:%s:%d:[error]   [%d] = 0x%02X  parity=%s\n`
