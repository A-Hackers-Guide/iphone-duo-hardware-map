# `/usr/lib/updaters/libMantaMCUUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 11,925,264 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 43 (Size: 6888)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (26)

- `/usr/lib/updaters/libMantaMCUUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC (compatibility version 1.0.0, current version 3298.52.1, weak)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration (compatibility version 1.0.0, current version 1453.40.1)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_DarwinFoundation2.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_DarwinFoundation3.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_StringProcessing.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (160 classes, 5 protocols)

Classes: `MRUHardwareInfo`, `MRULogHelper`, `MRUPersonalizationInfo`, `MRUPersonalizedFirmware`, `_TtC10Subprocess12CStringArray`, `_TtC11IOKitExtras18IOKitManagedHandle`, `_TtC11IOKitExtras26IOServiceDiscoverySequence`, `_TtC11IOKitExtras40IOServiceDiscoverySequenceImplementation`, `_TtC11NIOEmbedded15EmbeddedChannel`, `_TtC11NIOEmbedded17EmbeddedEventLoop`, `_TtC11NIOEmbedded19EmbeddedChannelCore`, `_TtC11NIOEmbedded22NIOAsyncTestingChannel`, `_TtC11NIOEmbedded24NIOAsyncTestingEventLoop`, `_TtC11NIOEmbeddedP33_B74500E45D63218F027FB4553B6BF95020PromiseCreationStore`, `_TtC11RT13Updater10B2PDecoder`, `_TtC11RT13Updater10B2PEncoder`, `_TtC11RT13Updater11B2PChecksum`, `_TtC11RT13Updater13RT13DFUClient`, `_TtC11RT13Updater14RestoreDecoder`, `_TtC11RT13Updater14RestoreEncoder`, `_TtC11RT13Updater16B2PMessageLogger`, `_TtC11RT13Updater17RT13RestoreClient`, `_TtC11RT13Updater20RestoreMessageLogger`, `_TtC11RT13Updater23B2PClientChannelHandler`, `_TtC11RT13Updater27RestoreClientChannelHandler`, `_TtC13MantaFirmware34MantaLocalDataBaseFirmwareProvider`, `_TtC13TracingExtras14OSSignpostSpan`, `_TtC13TracingExtras16OSSignpostTracer`, `_TtC14KalElUIService15UIServiceClient`, `_TtC14KalElUIService15UIServiceServer`, `_TtC14KalElUIService22UIServiceMessageLogger`, `_TtC14KalElUIService26UIServiceRawMessageDecoder`, `_TtC14KalElUIService26UIServiceRawMessageEncoder`, `_TtC14KalElUIService29UIServiceClientChannelHandler`, `_TtC14KalElUIService29UIServiceServerChannelHandler`, `_TtC14KalElUtilities5Queue`, `_TtC14MantaUtilities5Queue`, `_TtC14MantaUtilities9Semaphore`, `_TtC15Instrumentation13ReadWriteLock`, `_TtC15MantaMCUUpdater19MantaMCUUpdaterShim`, `_TtC16KalElBootService17BootServiceClient`, `_TtC16KalElBootService18BootServiceChannel`, `_TtC16KalElBootService19MantaAsyncUDPRouter`, `_TtC16KalElBootService23BootServiceRemoteDevice`, `_TtC16KalElBootService33BootServiceRemoteDeviceController`, `_TtC16KalElBootService9Semaphore`, `_TtC17KalElFlashService18FlashServiceClient`, `_TtC17KalElFlashService25FlashServiceMessageLogger`, `_TtC17KalElFlashService26FlashServiceMessageDecoder`, `_TtC17KalElFlashService26FlashServiceMessageEncoder`, `_TtC17KalElFlashService38FlashServiceClientUpdateChannelHandler`, `_TtC17MantaAppleConnect19AppleConnectManager`, `_TtC17MantaXPCAPIModule14MantaXPCClient`, `_TtC17MantaXPCAPIModule14MantaXPCServer`, `_TtC17MantaXPCAPIModule22MantaXPCInternalClient`, `_TtC17MantaXPCAPIModule22MantaXPCInternalServer`, `_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicClient`, `_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicServer`, `_TtC17MantaXPCAPIModule5Queue`, `_TtC18KalElSignalService19SignalServiceClient`, `_TtC18KalElSignalService26SignalServiceMessageLogger`, `_TtC18KalElSignalService27SignalServiceMessageDecoder`, `_TtC18KalElSignalService27SignalServiceMessageEncoder`, `_TtC18KalElSignalService33SignalServiceClientChannelHandler`, `_TtC19MantaAsyncXPCModule16XPCObjectDecoder`, `_TtC19MantaAsyncXPCModule16XPCObjectEncoder`, `_TtC19MantaAsyncXPCModule17_XPCObjectDecoder`, `_TtC19MantaAsyncXPCModule17_XPCObjectEncoder`, `_TtC19MantaAsyncXPCModule21MantaAsyncXPCListener`, `_TtC19MantaAsyncXPCModule23MantaAsyncXPCConnection`, `_TtC19MantaAsyncXPCModule32AsyncRemoteDeviceBrowserSequence`, `_TtC19MantaAsyncXPCModule40AsyncRemoteDeviceConnectionEventSequence`, `_TtC19MantaMCUUpdaterCore12OTAPreflight`, `_TtC19MantaMCUUpdaterCore16UpdateController`, `_TtC19MantaMCUUpdaterCore18GenericErrorSource`, `_TtC19MantaMCUUpdaterCore22BootedOSUpdateStrategy`, `_TtC19MantaMCUUpdaterCore23RestoreOSUpdateStrategy`, `_TtC20MantaKalElController15KalElController`, `_TtC20MantaKalElController32KalElControllerMultiplexDelegate`, `_TtC21AsyncAlgorithmsExtras18AsyncInterruptCore`, `_TtC21AsyncAlgorithmsExtras21AsyncInterruptTrigger`, `_TtC21MantaTriageController12MarvinTriage`, `_TtC21MantaTriageController13TriageHelpers`, `_TtC21MantaTriageController15AstrisRawTriage`, `_TtC21MantaTriageController16TriageController`, `_TtC21MantaTriageController18AstrisNativeTriage`, `_TtC21NIOConcurrencyHelpers4Lock`, `_TtC22MantaRetimerController14RetimerWatcher`, `_TtC22MantaRetimerController17RetimerController`, `_TtC22MantaRetimerController7Retimer`, `_TtC23KalElFactoryDataService24FactoryDataServiceClient`, `_TtC23KalElFactoryDataService31FactoryDataServiceMessageLogger`, `_TtC23KalElFactoryDataService32FactoryDataServiceMessageDecoder`, `_TtC23KalElFactoryDataService32FactoryDataServiceMessageEncoder`, `_TtC23KalElFactoryDataService38FactoryDataServiceClientChannelHandler`, `_TtC23MantaMCUTraceController15MCUTraceHandler`, `_TtC23MantaMCUTraceController18MCUTraceController`, `_TtC23MantaMCUTraceController9MCUTracer`, `_TtC7Logging13ReadWriteLock`, `_TtC7Logging4Lock`, `_TtC7NIOCore11DeadChannel`, `_TtC7NIOCore12RepeatedTask`, `_TtC7NIOCore13NIOFileHandle`, `_TtC7NIOCore15ChannelPipeline`, `_TtC7NIOCore16IdleStateHandler`, `_TtC7NIOCore18HeadChannelHandler`, `_TtC7NIOCore18TailChannelHandler`, `_TtC7NIOCore19BackPressureHandler`, `_TtC7NIOCore19NIONetworkInterface`, `_TtC7NIOCore20AcceptBackoffHandler`, `_TtC7NIOCore21ChannelHandlerContext`, `_TtC7NIOCore22NIOCloseOnErrorHandler`, `_TtC7NIOCoreP33_5D1691F81BFB9463F74AA8273C0A4D2D15DeadChannelCore`, `_TtC8MantaEDM17EmbeddedDeviceMap`, `_TtC8NIOPosix10BaseSocket`, `_TtC8NIOPosix12ServerSocket`, `_TtC8NIOPosix13NIOThreadPool`, `_TtC8NIOPosix15ClientBootstrap`, `_TtC8NIOPosix15ServerBootstrap`, `_TtC8NIOPosix16NIOPipeBootstrap`, `_TtC8NIOPosix17DatagramBootstrap`, `_TtC8NIOPosix19GetaddrinfoResolver`, `_TtC8NIOPosix19SelectableEventLoop`, `_TtC8NIOPosix22HappyEyeballsConnector`, `_TtC8NIOPosix26PendingStreamWritesManager`, `_TtC8NIOPosix27MultiThreadedEventLoopGroup`, `_TtC8NIOPosix28PendingDatagramWritesManager`, `_TtC8NIOPosix6Socket`, `_TtC8NIOPosix8PipePair`, `_TtC8NIOPosix9NIOThread`, `_TtC8TCPProxy11GlueHandler`, `_TtC8TCPProxy15TCPProxyHandler`, `_TtC8TCPProxy19CloseOnErrorHandler`, `_TtC8TCPProxy8TCPProxy`, `_TtC9NIOExtras17NIOPCAPRingBuffer`, `_TtC9NIOExtras19NIOWritePCAPHandler`, `_TtC9NIOExtras20LengthFieldPrepender`, `_TtC9NIOExtras21LineBasedFrameDecoder`, `_TtC9NIOExtras21ServerQuiescingHelper`, `_TtC9NIOExtras23FixedLengthFrameDecoder`, `_TtC9NIOExtras25DebugInboundEventsHandler`, `_TtC9NIOExtras26DebugOutboundEventsHandler`, `_TtC9NIOExtras28LengthFieldBasedFrameDecoder`, `_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE16ChannelCollector`, `_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE30CollectAcceptedChannelsHandler`, `_TtC9SerialLog11SerialProxy`, `_TtC9SerialLog16LineToLogHandler`, `_TtC9SerialLog19SerialConsoleClient`, `_TtC9SerialLog19SerialConsoleServer`, `_TtC9SerialLog22SerialLogCaptureClient`, `_TtCC8NIOPosix15ServerBootstrapP33_F13D6D61D4A528D08BD67995505C248713AcceptHandler`, `_TtCC9NIOExtras19NIOWritePCAPHandler20SynchronizedFileSink`, `_TtCE25SystemConfigurationExtrasaSo16SCPreferencesRef4Info`, `_TtCE25SystemConfigurationExtrasaSo17SCDynamicStoreRef4Info`, `_TtCO7Logging13LoggingSystemP33_C9FF2A9F0C61C813477A18DFECB0159A10FactoryBox`, `_TtCO9NIOExtras17NIOJSONRPCFraming31ContentLengthHeaderFrameEncoder`, `_TtCV21NIOConcurrencyHelpers7NIOLock8_Storage`, `_TtCV7NIOCore10ByteBuffer8_Storage`, `_TtCV7NIOCore16NIONetworkDeviceP33_332F4CD194A63D42AC43F87173201E7D7Backing`, `_TtCV7Tracing10NoOpTracer8NoOpSpan`

Protocols: `NSCoding`, `NSObject`, `OS_dispatch_source`, `OS_dispatch_source_signal`, `OS_xpc_object`

## Strings (9,796)

First 2,500 of 9,796.
```
v24@0:8@\"NSCoder\"16
I16@0:8
B16@0:8
^?
@48@0:8@16@24@32@40
@\"MRUHardwareInfo\"
@24@0:8:16
B32@0:8@16^^{__CFError}24
^v
@56@0:8@16@24@32@40@48
@\"NSString\"16@0:8
@16@0:8
B24@0:8:16
^{_NSZone=}16@0:8
v12@?0i8
v8@?0
I
v16@?0@\"<OS_xpc_object>\"8
@40@0:8:16@24@32
B56@0:8@16@24r^{__CFDictionary=}32r^^{__CFDictionary}40^^{__CFError}48
B
@32@0:8@16@24
B24@0:8#16
v16@?0@\"OS_remote_device\"8
B24@?0r*8@\"<OS_xpc_object>\"16
v16@?0@\"NSTask\"8
v16@0:8
@\"NSString\"
@\"NSNumber\"
B24@0:8@16
@48@0:8r^{__CFDictionary=}16^?24^v32^^{__CFError}40
v24@0:8@16
@24@0:8@\"NSCoder\"16
@40@0:8@16^?24^v32
v20@?0@\"OS_remote_device\"8B16
@24@0:8@16
@32@0:8@16^@24
v32@0:8@16*24
@32@0:8:16@24
B24@0:8@\"Protocol\"16
@52@0:8I16I20I24I28B32B36I40Q44
Q
#16@0:8
Vv16@0:8
Q16@0:8
@\"NSData\"
ret.reg.write.K_DA_REG_NAME_NONCE_0
Register file 43
param.op.AXCPU_WP_ENABLE.unsupported
classic
ParrotSWD
NIOCore/NIOAsyncSequenceProducer.swift
NIOEmbedded/Embedded.swift
product-name: %s\n
error %s checking for data abort
~INTDIS
read-back (sys AP) failed
rhs.IsString()
manta-async-xpc-msg-body
Received output 
[ARM32cpu_t::_update_register64] 0x%08x\n
{%s} PRIMECELL [DONE]
fn._ocd_reg_r.OCD.DEVID
No io board mcu found.
update(device:partition:firmware:)
Expected to decode UInt64 but found a 
chassisTriageProgress
Flashing DFU stage
AXconn_t Struct Is NULL
{%s} [!is_64] exec: encode_msr(MDDTRTX_EL0, 0, %d\n
RF12
com.apple.MantaKit.mantad.internal.remote
j226CnodeSensors
wrstn-pipes
End of Operation Bit Is Set - %s
{%s:%s@%d} current_el[%d] <  %d\n
_a64cpu_lower_el_hw
   DPv3 BASEPTR CID does not indicate v9 or v1 ROM TABLE (%X %X %X %X)\n
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
IOKitExtras/IOChipInfo.swift
rt13/14/pgood/1v2
Valid Portal
astris_ide_is_component_present_at_addr
param.halt_group == NULL
%s%s\n
{%s} Failed to single-step %s: %s
{%s:%s@%d} [%s] std::copy failed: %s\n\n
Failed to get panic report: 
result.alloc_table==NULL
{%s:%s@%d} [%s] Couldn't get CPU from AP\n
Reading FLASH_OPTCR failed during mass erase: %s\n
{%s@%d} Drain empty on decr [%s].
com.apple.Manta.MantaMCUUpdaterCore
Invalid IPv6 Address 
internal.clear-auth.debut_auth == NULL
{%s:%s@%d} [%s] wait_for_flash_idle failed (wp): %s\n
regval is NULL.
connection to probe is lost
duration_ms
type >= kNullType && type <= kNumberType
/usr/share/firmware/mantamcu//j236/release
AXjtag_chipcnt(_:)
esr_el3
Failed to execute DRPS, in order to restore PSTATE after exception
astris_jtag_irscan_idle_impl
AXdebug_auth_is_dft_authenticated
fn._write_special_reg.ibreaka1.address
USER
solicitStatus(firmwareSelect: 
 RPM, faster than the expected maximum 
AstrisNativeTriage: calling coredump on probe 
astris_explore_enabler_init
Exception occured after executing MRS to bounce through scratch register
dapcmd->status == K_DAPSTAT_KIS_PORTAL_ERR_PENDING
No connection attempt description
, firmwareSelect: 
udid path 
hwbp_insert
dbgwrap halt failed, falling back to classic method
AMAuthInstallSsoSetStealthMode
{%s:%s@%d} [%s] busy timeout on open: %s\n
{%s:%s@%d} [%s] timeout waiting for R1RDY\n
cpu_mode
--> dpb_wir2   size=%3d wdrmisc=%#x wdrtpser=%#x
dr-length
wrstn-dpcsoc
setup_transaction_objects
Found %d APs
X09 Part
MR3
param.cpu_reg_file_size.invalid.1
Cannot read sbin value
 RPM, slower than the expected minimum 
[KIS] Register Read/Write/Wrote: %d\n
fn._ocd_exec_instr.xsr.ddr.t1
Programming STM32Hxxx...\n
getOrCreateValue
decodedData is not base64
Flash updated successfully
Failed to fetch info for 
!!!! Critical Error:  dspsr_el0 NOT CACHED !!!!\n
EXCSAVE6
param.invalid.reg_file_index.outofrange
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_connect.c
Already connected to
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
FAR_EL3
astris_user_default_remove_all_nicknames
MAC16 data register 2
AXconn_identify_soc_collateral
Invalid response from Map server (len=%d; not all printable and/or no EOL): %s
Kick has been requested by probe server
NIOPosix/BaseSocketChannel.swift
can't register on selector as it's 
AXdp_fromchip(_:)
rt13/13/pgood/1v2
Erasing...\n
[1500] Error parsing bridge: %s
channel-%s
{%s->%s}[dirty] %s[0x%X] = 0x%016llX
Booting retimers.
exit.exception_test_2
{%s} exec: DC_CIVAC_X1_ENC\n
PARTNO_KIS
EPS2
fn._ocd_reg_w.ddr.t2_save
_ocd_enable
EmulatorSWD
run_steps
_invalidate_icache_vaddr
   {%s} (DP,%04X): status=0x%X(%s) -  %s\n
socket(domain:type:protocol:)
Signal service connect failure: 
\t\t%s\n
A64
AXjtag_scanout
High level 4 exception PS
path
MantaMCUUpdaterCore/UpdateMCU.swift
mhdr != NULL
backupSRAMStatusResponse(report: 
CPU Address: 0x%llX\n
[SSTEP] using BP %d\n
RF48
fn._read_general_reg
fn._ocd_reg_r.dsr.1
 is already in tag bundle of 
createVLANInterface(physicalInterface:vlanTag:)
CertificateSecurityMode
Unexpected request.
Attempting to connect to [
{%s:%s@%d} [%s] reading CPSR(1)\n
Unable to read SP
Table 5–160
RT13Updater/B2PClientChannelHandler.swift
products_
{%s:%s@%d} [%s] reading DFSR\n
{%s} [%s] EDSCR with ITO set - recovered (retries=%d).\n
type_hint not NULL, but creating a placeholder, this is off
RF14
_set_single_step
ASTRIS_ERR_MASKERR
writev(descriptor:iovecs:)
_Concurrency/arm64e-apple-ios.private.swiftinterface
Test Mellanox fan fail, fan was below 
nullptr == file_url
IBREAKENABLE
op_RSYNC_encode
shift=%d,opcode=0x%6.6X
ERROR!! write binary data parameters invalid\n
MantaMCUUpdaterCore/MantaMCUUpdaterCore.swift
maxCarrierCount set to 
Termination imminent.
DEBUG_AUTH_REGS
{%s:%s@%d} [%s] getting GPR\n
{%s::%s} ERROR %d(%s) resuming %s\n
   {%s} Read/Write AP's R_MEMAP_CSW to establish 32-bit transfer size\n
ASTRIS_ERR_IFSTATE
previous next 
     ARM %s watchpoints: %u\n
AXmemap_stmflash calling STM32L4xx::reflash()\n
AXmemap_stmflash calling STM32F7xx::eraseflash\n
Atomic Oper, Control
CortexM4
unknown match criteria type: %d
Missing a comma or '}' after an object member.
Encountered multiple errors: 
MCU panic log policy is set to do nothing. Bailing out
Writing START in FLASH_CR failed during mass erase\n
/socs
psr-bit
\tReading left over chunk expected 0x%x got 0x%x\n
IDE ACCESS OUT OF BOUNDS
Warning: Default logging location requested when running as root (using [%s])\n
cio/grp1/0/cable_present
RT13Updater/RestoreMessageLogger.swift
Probe Type (%d) FW Version: %s does not support KIS.
astris_command_lock
{%s:%s@%d} [%s] moving DBGDTRTX to GPR 0\n
op_ROTW_encode
ASTRIS_ERR_DISASM
fn.stmflash.h7.unlock_flash.write.cr2.key1
Sending DYN Bypas Channel Set: %d
ASTRIS_ERR_INVAL
SCANDEBUG
Init objects failed
Setting CPU %s is_boot_core to %d\n
No loggers container
rhs.GetType() == kObjectType
com.apple.Manta.
com.apple.Manta.SerialProxy
calling coprocessor_coredump on probe 
{%s:%s@%d} [%s] executing MOV\n
CPU[%s] Read Reg: %d
   {%s} Read AP's R_MEMAP_CSW\n
probetimeout retrying access...\n
MASK ERROR
com.apple.Manta.SCPreferences.
Unable to collect MCU serial output.
ret.enableAll
consumedAcmds
New Length: %d\n
Accumulator high bits
fn._ocd_reg_r.regval
locationids
MantaMCUUpdater
cpm-offset
Extract Offset: 0x%X for %d\n
kis_target_info %s
Kicking
no debug bus AP present when expected; after sysap is NULL
Initialized %d 1500 bridges\n
Writing PER and PNB in FLASH_CR failed during page erase\n
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
[1500] v2 plist missing required field 'bridges'
_flush_state_hw
_clean_dcache_vaddr
{%s=>%s} null reference to AXcpu_t record, `cpu`
PARTNO_ARM7TDMI2
Blink five times
CPU.ARMv7
Enabled
ret.pka.nonce.status.err
%02u:%02u:%02u:%06u|%s <%s> %s
fn.stmflash.h7.mass_erase.flash_idle.after_mer
ACQ_SAMPLE_I2C
 is not supported.
astris_ide_get_cps_fsm
astris_batch_attitude_detach
{%s:%s@%d} !(prsr[0x%08X] & DLK)\n
{%s::%s@%d} [FALSE] target_el[%d] <= 3 && >= 0\n
ret.write.spsr_elx
clear_authentication
R8
elements delegate 
accept(descriptor:addr:len:)
User chose to continue from escape menu
\tbut is not guaranteed on this device.\n
copyBoardNameForKey
EXPLORE_JTAGAP
AuthDebugWithTimer_t::need_to_authenticate_helper exit false (no need found)\n
{%s:%s@%d} [%s] busy timeout on close: %s\n
com.apple.Manta.SerialConsoleServer
cpu-ascdebug-offset
## armcpu: bad status even though all bytes written (%d)\n
internal.is_probe_authenticated.chip->soc == NULL
Page table virtual address
Probe %s removed during selection process
ARMV8M
dispatchQueue(_:)
No securityDomain in options dict
Clear (1<<1)
\tPrologue Aligned Read Required Read: 0x%x offset: 0x%x @ 0x%llx (0x%llx) Bytes To Align 0x%x
_get_arch_hw
fn._ocd_exec_instr.rfdd
var.num_loops.invalid>3.curr_instr
op_L32I_encode
%@,ProductionMode%@
ChannelPipeline[
sequentiallyConsistent
getCurrentDevicePartition(device:)
MCU powered off, can't establish connection
hostid
ret.cfg.read.swd
{%s::%s} Replacing Existing register (offset 0x%08llx) in memory block
remove(protocolType:)
\n-----END PUBLIC KEY-----
rt13/10/pgood/1v2
{%s:%s@%d} [%s] setting GPR 0 (COPROC)\n
{%s} failed (%s)
Error %d (%s) while expanding ~ for Astris history save\n
host_get_port
SPIXACT
kalelController(_:didDiscover:)
trace
bid
error %s reading DAP PFR1
no device when sending request
createCPUPlaceholder
level_stack_.template Top<Level>()->inArray
Found match - bypass_device: %s; channel: %d\n
~MA
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
%s: []\n
Table 5–133
CHIPCNT
cpu_writereg
.
{%s->%s} exec: encode_mov_vfp_to_gpr(scratch=%d, sysreg=0x%X, %d)\n
wpcr
Failed AP read of R_MEMAP_CSW res: %i
Flash unlocked...(before erase)\n
Could Not Allocate Booster Location Array
Adding new booster path: %s\n
{%s:%s@%d} [%s] setting GPR 0 (COP_ARB)\n
{%s:%s@%d} [%s] executing MOV (diff mode)\n
RF18
Probe %s protocol version %u.%u not compatible: we require %u.%u.\nPlease try updating your Astris console and firmware.
cpu_mmu_get_mair
Perform OTA preflight
com.apple.KalElKit.BootServiceInsecureStateMachine
Enabling power supply on outlet 
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llX) - reg_count=%d - val=0x%X
{%s:%s@%d} [%s] moving DTRTX to GPR\n
AXmemap_stmflash calling STM32Fxxx::reflash(0x40022000)\n
%s (%d)
choice: %d\n
SAM
Breakpoint Enabled: %s
param.cpu_name.invalid.NULL
SOC_t::{%s} Attempting to perform a bus read outside of safe area on an aponly explore (addr: 0x%llx select: %d)
preparePSUFWUpdateResponse(resp: 
DCM
_remove_breakpoint
CPU-level (general and architecture-specific)
Probe %s LocationID Info is %s
Successfully signed FDR challenge using key 
nic/overtemp_warning
Failed to get KIS translator version\n
AXbooster_interface_cleanup_astris_api
[1500] TAP %d missing required field 'chip-index' or 'irlen'
[iter %lu] after_codeblock_execution
KIS translator version : %d\n
[ARCH32] Failed to write transfer register (EDDTRTX) the value to write
High level 5 exception PS
KIS-SIM
no debug bus AP present when expected
performNextStage
MantaAsyncXPCModule/Never.swift
 mcu firmware but got 
master-debug
{%s::%s@%d [%s]} Error %s: translating VA=0x%llX (write=%s)
TatsuServer Found: %s\n
EXCSAVE4
dbgwrap
connected(partnerChannel:myChannel:contextForInitialData:)
temp/exhaust_air
\t Writing 0x%08llX...\n
[READ] cop64 %d -> 0x%016llx\n
get_page_shift
{%s} _pre_halt_hw result = %s
{%s} DBGCOMPONENT: name=%s, base=0x%llx, type_hint=%s
astris_apread
kalelController(_:kalel:didChangeFromState:to:)
/usr/local/bin/python3
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
astris_cpu.cpp
   {%s} (DP,%04X,%08X): status=0x%X(%s) - %s\n
{%s:%s@%d} [%s] CR write (prog) failed: %s\n
fn._read_special_reg.dbreakc0
default
T32
{%s} set=%u (sh=%u), way=%u (sh=%u)
{%s:%s@%d} [%s] FLASH_CR LOCK write failed: %s\n
EPS7
RF62
Invalid data breakpoint index %d
ASTRIS_ERR_NOTOPEN
host %s
com.apple.private.MantaKit.mantad
astris_conn_has_kis
xtensa-non-tie-range-base
%s - runBlock
** Please try using: \"appleconnect authenticate\" in Terminal and re-launch Astris.    **\n
{%s:%s@%d} [%s] CR read (prog) failed: %s\n
fn._ocd_reg_w.ddr.reg_val
Previously dumped the process tree, skipping
AppleANS2NVMeController
Failed to read from FDR 
CG
Error - STM32Lxxx reflash failed (%s).\n
fn.stmflash.h7.unlock_flash.write.cr1.key2
{%s} host:%s, flags:0x%08x
{%s[select]} timeout while waiting for data from the connection
\t[MATCH_IDCODE] %s <= ((0x%08X & 0x%X) == 0x%08X)
service(matching:)
ir-cmds
set_gpr
check_and_clear_cpu_msr_lock
AXcpu_mmu_get_mair
fn._write_special_reg.dbreaka0.address
)
ChassisTriageStart: 
rt13/2/pgood/1v2
astris_init_ap_mem
Error %s opening single_port connection to probe server
AddState
n <= m
pmu-name: %s\n
Dropping error due to previously encountered error
BoosterManager
TBMLocked
Table 5–179
_setup_bp
op_L8UI_encode
cpu_hwwp_disable
/AppleInternal/Library
, sectorOffset: 
SerialNumber
astris_ide_get_bootid
param.chip == NULL
aarch64
R5
Dropping response due to previously encountered error
rt13/13/pgood/0v805
GetCachedPowerByIndex
AXmemap_stmerase(_:baseAddress:length:eraseAll:quiet:)
Update Compute SMC proxy: 
astris_batch_attitude_relax
symbol.check.loaded.AMAuthInstallLogSetHandlerPtr == NULL
ret.production_emulation
com.apple.KalElKit.FactoryDataServiceClientChannelHandler
Failed to connect signal service: 
retimer powered off
\tAstris does not support page-erase beyond first %d KB of flash.\n
{%s:%s@%d} [%s] doing JTAG scan (DTRTX)\n
AXdebug_auth_set_sso_user
R11
APPLETYPE_UNKNOWN
Acdcuc%i,Ticket
 bytes) does not contain enough data to deserialize value of type 
MantaKalElController/KalEl+ConsoleProxy.swift
IOInterfaceUnit
_a64cpu_encode_mrs
[INS_WP] 0x%016llx x %d\n
General register 15
OCD.DEBUGCAUSE = 0x%8.8X
com.apple.MantaXPCAPI
runningHandler(_:_:)
gpr < 32
{%s:%s@%d} el[%d] == m_exception_level[%d]\n
_read_mem
ASTRIS_ERR_NODEVICE
probed USB transaction timer expired
TAP-Only
config/carrier/slot
Invalid page number %d\n
{%s} Failed to extract PID from table (%d); continuing anyway
astris_ide_get_boardid
MISMATCH
{%s:%s@%d} [%s] getting GPR 0 (CPSR)\n
{%s:%s@%d} m_exception_level[%d] == 0|1|2|3\n
ERROR: unable to resume translation for %s
AXcpu_mmu_get_tsz
STM_FLASH_KEYR: 0x%x\n
reg_name (\"%s\") not present.
AXconn_port
SOC_t::{%s} Attempting to perform a bus transaction when stop clock condition detected; aborting
. Ignore the error
Attempted to decode Never
{%s} Failed to extract CID from table (%d); continuing anyway
{%s} %s status failed. error: %d (%s)
PARTNO_ARM7TDMI
ocd_base_address = 0x%8.8X is not 4 KByte aligned
can't find pid in response\n
ARMDAP
unknown sockaddr family 
MantaKalElController/KalEl+FactoryRegion.swift
Die Config Disabled
SPSR_EL2
{%s:%s@%d} [%s] FLASH_WRPR3 write failed: %s (continuing)\n
kext connect name %s\n
No probes
NOP
Created VLAN interface '
ap
carrier/2/throttle
IsObject()
_ACCGetCurrentSSOUserName
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
CPU has no regions, maybe powered off?\n
Optional Key: CPUMonitor not in preferences
ASTRIS_ERR_NOTSUPPORTED
checkSignalPresent(signal:)
{%s::%s} Attempting to add duplicate register (offset 0x%08llx) to memory block
set.wp.len = not supported
ret._setup_wp
Breakpoint Address: 0x%llx
var.bp.invalid
vlanTag()
,%d
AXmemap_write64(_:address:value:)
Algorithms/Product.swift
User interaction
errorCaught0(error:) called on DeadChannelCore
KalElUIService/UIServiceServerChannelHandler.swift
Waiting for flash to idle after starting page erase, failed\n
result.read_vals==
{%s:%s@%d} [%s] writing LOCKACCESS\n
ret.reg.write.K_DA_REG_NAME_AUTH_TIMER_LOCAL_LOAD
{%s:%s@%d} [%s] PECR write (erase) failed: %s\n
probe
Opening flash to write 
didLoseTopologyGroup
{%s::%s} [%s] WP_REMOVE _remove_watchpoint[%d] failed (%s)
{%s:%s@%d} [%s] Error - %s\n
Could not find TAP at chip-index %d for v2 1500 config\n
sys_pwr_up
\tboardID: %u\n
com.apple.Manta.MantaLocalMCUFirmwareProvider
offset = %d
LBEG
Xtensa Option num_high_pri_intr: %d
poo
cpu_cache_info
process_status_transition
EXPLORE_WITH_AUDIO
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
MCUHardwareInfo(chipId: 
_clean_invalidate_l2cache_setway
CCSIDR
AXcpu_hwwp_insert
ApSecurityDomain
Only Auth-Debug, DFT-Auth and Probe-Auth are currently supported.\n
Level-1 exception PC
abort
backupSRAM status: No of chunks: 
Expected to decode Array<Decodable> but found a 
Channel had no remoteAddress
far_el2
{%s:%s@%d} [%s] FLASH_KEYR write (second) failed: %s\n
xfer_length=%u
MemberEnd
Unexpected sequence number 0x
ret.nop
ret.dbgap.memap_read
Reading FLASH_CR1 failed during lock sequence\n
lock()
Running stale firmware
A firmware is already associated with 
sourceid info 
--> latency    tdi=%d wir=%d wir2=%d wdr=%d
!!!! Critical Error: SYSREG TARGET_EL[%d] > CURRENT_EL[%d] !!!!\n
COMPARE1
fn.stmflash.h7.wait_bank_flash_idle.read.sr_reg
misc-wirtestporten
res.setup_transaction_objects
result.extract_group_info==
init_hw.read.dhcr
\tPrologue Aligned Read Failed
{%s:%s@%d} [%s] busy timeout on lock (out): %s\n
\tMass Erase failed: %s\n
Not Creating CPU: %s\n
entryCreateProperty(propertyName:)
AXbooster_init_with_ctx(_:context:)
transitionTimeout
BoardID is missing for: %s. This is a required key. Check that match_info is valid: %s
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
[AstrisAsync] Complete Queue callback returned %d (%s)\n
vvv *** PREVIOUS ASTRIS SAW A HANG *** vvv\n
GetAllocator
 does not conform to the expected format.
triage policy: do nothing
com.apple.Manta.VLAN
/usr/share/firmware/mantamcu/
debug/rt13swd/0_7
BoosterManager.CPU
cpu-subsystem
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
fn._ocd_reg_dsr_clear_and_validate
queryInfo
debug/forcepanic
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/concurrency/astris_attitude.c
Failed to read IDE through DAP\n
Memory error PC register
fn.stmflash.h7.unlock_flash.read.cr1
pon
stack_.GetSize() == sizeof(ValueType)
configured link local address for %s\n
Device is production fused
Existing version matches requested version, skipping update
{%s:%s@%d} [%s] Could not figure out flash size: %s\n
AXchip_get_board_rev
update(bundle:): ecid=
PROGRAMMABLE_HW_FW1
rt13/1/pgood/0v855
Took an exception in EL%u, esr = 0x%08llx, category = 0x%llx\n
{%s::%s} [%s] error %s writing SCTLR_ELx
## armcpu: success status even though not all bytes written\n
Unknown
sent %zd bytes to Probe Map Server when sending %zu
Failed to create update strategy with error: 
 bytes) contains more data than the serialized length of type 
failed to get path for service: 0x%x\n
STM_FLASH_AR: 0x%x\n
_return_from_debug_interrupt
str != 0
com.apple.KalElKit.SignalServiceMessageLogger
Unknown LED mode 
Hardware test failed
=== Found %s Boosters ===\n
Invalid current AP (%d), adopting APTABLE (%d)
{%s:%s@%d} [%s] writevals: %s\n
_tie_write_word32
ASTRIS_ERR_CPUNOTHALTED
AddressedEnvelope { remoteAddress: 
getValue(withTimeout:)
AX1500_transact
Could Not Find Any Boosters of Type: %s\n
Can't find descriptor for group - can't index\n
Waiting for previous in-flight authentication to finish\n
fn._ocd_reg_r.ddr
_write_window_base
Index out of bounds
      JTAG-AP port %u PSTA(0x%08X) is still set, the explore below\n        will probably fail to find any chips. But we are letting it through.\n
Switch back to primate KIS: %s\n
massErase
fn._ocd_reg_dcr_set.debug_interrupt_msk
Access Port
messages
elr_el2
_a64cpu_unhalt_cpu
Table 5–186
MISC1
{%s:%s@%d} [%s] failed to write CMD/STAT\n
ComponentName
boot(device:updatePSU:)
Invalid interface: 
MantaRetimerController/RetimerController+PublicAPI.swift
unable to open IONetworkStack service: 0x%x\n
Waiting for flash to idle after starting mass erase, failed\n
KIS DBG CLK Failed to Power Up. CONTROL0=0x%X
partnum
DestBundlePath
rt13/11/pgood/0v855
{%s} halting %s\n
[1500] %s step %d missing required field 'instr'
{astris_probed_print_events} not supported in this build configuration
ret.pka.verify.valid
FLASH_WRPR2
fn._read_special_reg.dbreaka0
sourceid path 
result.read_vals(table_info)==
L1 dcache
Width: %d not supported
enable_timer_ovr
{%s} probeList has probeCount of zero
{%s@%d} {%s[select]} %d(%s) [RETRYING]
read_resp_via_sock
notificationKeys(_:_:)
RT13Updater/RT13RestoreClient.swift
result.dbgap==NULL
[%s] {%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
_write_reg
Raw level
JSON string output is null
yield(contentsOf:)
No AppleConnect framework.
entry.exception_test_0
AuthDebug::authenticate_probe - no need to authenticate\n
AXdebug_auth_is_authenticated
bool
time out reported by probe
Operation was cancelled
required
astris_jtag_scan_stay_gotorti_impl
setup_bp.not_halted
PROBED_ERROR
Generic
 (bufferCapacity: 
firmwareStatus(status: 
cio/grp1/0/force_red_on
EXCEPTION(throw) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
{%s:%s@%d} [%s] setting DTR MODE to STALL (first abort)\n
ret.drain.half-duplex
[AsyncSnapshot] #%zu: %s | paused=%d barrier_hit=%d last_replay=%d\n
cpu_readreg_vals
com.apple.KalElKit.UIServiceServerChannelHandler
invalid ecid format: 
failed to determine breakpoint instruction
GROUP
{%s} handle ROM entry
{%s} requested TCKRATE (%u Hz) SoC-adjusted to %u Hz
General register 3
RF1
Failed to get manta boot configuration
willChangeState(from: 
astris_ide_get_cpu_halt_group
AXI Error
MINISWD
AXchip_switch_taps
_handle_exception_for_el
astris_cpu_raise_el
partnum & implementer == 0 && type_hint == NULL; This is not a CPU
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/xtensa_cpu/xtensa_cpu.cpp
SWDRESET
set.hostname
Sending set lock byte to MCU
write(context:data:promise:)
Failed to triage mcu '
ret.dlr_el0
AXchip_getinfo
ret.reg.write.K_DA_REG_NAME_AUTH_KEEP_DECISION
internal.is_dft_authenticated.chip == NULL
{%s:%s@%d} [%s] FLASH_CR MER write failed: %s\n
Received info about 
unable to find IONetworkStack service\n
Register file 51
Register file 56
Standard level
Portal Status, Changing STATUS and CMD/STAT to reflect
fn.stmflash.h7.sector_erase.read.cr_reg.before_start
PERSEIS
can't re-register on selector as it's 
m_core_api_serial_queue
error %s checking for data abort(first)
astris_setup_memap_target
Update
{%s:%s@%d} [%s] Waiting for flash to idle before page erase, failed\n\n
fn.stmflash.h7.unlock_flash.flash_idle
\tCould Not Find Bank (%d) or Sector (%d) For Address: 0x%08llX\n
Failed to downcast 
commit()
IMAGE_SIGANTURE_512
Encountered unexpected 
FLASH_ACR
cpu-dbgwrap-status
%04X:
ret.memap.write
Failed to create xpc_file_transfer.
connected
internal.get-timer-count.debut_auth == NULL
Register file 20
/var/log/astrisclient
Astris-%d.%d~%d
{%s} NOMEM
Connection aborted while choosing probe
astris_remove_loaded_cpu_boosters
wir-tdo
AXmemap_read64(desc) failed
{%s:%s@%d} [%s] CR read (clean) failed: %s\n
source[i] == '/'
pow10.h
static_cast<void*>(this) != static_cast<void const*>(&rhs)
Nonce
exchanged original 
j236CarrierSensors
enablePDBPowerSupply(iob:logger:)
Booster Bundle: %s\n
{%s:%s@%d} [%s] setting GPR 0 (switched)\n
[%s] m_dc_max_level %d, m_ic_max_level %d\n
     ARM %s debug CPU rev %d\n
15531444804973541
Channel writability changed to 
developmentLockFactoryDataRegion()
{%s::%s@%d [%s]} Error %s: pre_resuming HW
AXjtag_settck
Failed to convert CFArray to C Array\n
fn.params
Can't get hardware model - failed to allocate data string
This XPC file handle was consumed twice. This is a logic error in the caller.
MantaKalElController/KalElStateMachine.swift
IOPMURequestSystemReset
astris_explore_enabler_get_subsystem_status
{%s} write[ED32] of %s @ address 0x%016llX = 0x%08X [%s]
{%s} exec: IC_IVAU_X1_ENC\n
DEMCR: 0x%08X -> 0x%08X
read memory (permission checks suspended)
Duplicate values for key: '
 bytes>, files:\n
preparePSUFWUpdate(device:)
[PCR]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
{%s:%s@%d} [%s] executing LDCpi\n
PROBETIMEOUT WHILE WRITTING\n
{%s:%s@%d} [%s] FLASH_CR PG write failed: %s\n
Register file 35
Releasing apb mcu 
DLR_EL0
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_stmflash.cpp
fn._ocd_exec_instr.xsr.ddr.t1.1
Timeout waiting for flash idle: SR = 0x%08X\n
Setting STOP CLOCK to TRUE
Failed to create SoC or no booster
setProbeInfo
permanentlyLocked
SECURE_BOOT_SIGNATURES
un-sel-sib-network
Logging Context Is NULL\n
va
ACCHI
Table 5–155
host is going to sleep
buffer iteratorInitialized failure 
RemoteService(name: 
marvin_noradar
Start Page: %d\n
{%s::%s} timeout while waiting for EDSCR ITE
PARTNO_SWDP_M0P2
RF42
Table 5–148
Unable to decode message from byte stream: 
cio/grp1/3/force_red_on
OUTEN_DBG
stderr
{%s} probe device server closed the connection while trying to read data (at recv)
cpu_mmu_get_page_shift
{%s} asc status=%d being reported as Unknown
AXcpu_status_name_detailed
AP[%d]: MEM_AP_AHB\n
{%s:%s@%d} [%s] readval: error %s @ 0x%08llX\n
, boardSerialNumber: \"
{%s:%s@%d} [%s] writing WVR %d\n
ASYNC
{%s::%s} [%s] INS_SWBP error=%s %s [VA=0x%016llX]\n
astris_cpu_mmu_configure
ret.generate_nonce_and_send_request
fn.stmflash.h7.mass_erase.flash_idle
Unable to fetch info for 
failed to get device registry id: 0x%x
mempool-size
result.read_vals(group_info)==
{%s::%s@%d [%s]} Error %s: invalidating icache vaddr: 0x%llX
WRBUF
Table 5–158
Register file 0
com.apple.KalElKit.FlashServiceClientUpdateStateMachine
Expected to decode Int8 but found a 
RegionStart
astris_setup_ap_mem
{%s:%s@%d} [%s] error waiting for loader to complete: %s\n\n
ChassisTriageError: 
subscribe(to:callback:)
AXjtagap_explore
Instruction break enable bits
Error %d (%s) opening cmd snapshost save file
HTTP transaction running in background
{%s@%d} neither socket nor kext connection available
addTimingPhase
switch_regset
_ocd_exec_instr
%d.%dbeta%d
Info
tried to decode as type 
Flash data exceeds device capacity.
/tmp/command-stdoutput-
Process exited with nonzero return code 
EDITR
astris_user_default_set_boardname
kick_req %s
: Unable to clean up String. Printing raw buffer to console
{%s:%s@%d} [%s] Bad len (must be power of 2): %u\n
_log_setup_thread_specific
Too many open files
CopyFrom
Debug Clock Already Enabled
(src_gpr & (0x40000000 | 0x80000000)) == 0
index slot not enabled
{%s} FAILURE - NULL parameter
Table 5–174
Sprocket
document.h
-----BEGIN CERTIFICATE-----\n
cio/grp0/0/force_red_on
Failed to reach 
AXbooster_get_loaded_boosters
CSE
EXCSAVE3
length=%u, width=%d
setLockByteRequest()
com.apple.KalElKit.FlashServiceClientUpdateChannelHandler
Received error response for 
Error: Console server is already invalidated
{%s::%s@%d [%s]} Error %s: cleaning dcache: set=%u, way=%u
AMAuthInstallRequestSendSync
param.cpu_reg_file_size.invalid.2
PORTAL_STS_MULTIPLE_BITS_SET
Management network interface
deinit
AXbooster_interface_init_astris_api
{%s::%s} [%s] error %s reading instruction [VA=0x%016llX, len=%d]
AP Only Explore was asked for, stopping here
AMAuthInstallSsoSetAppleConnectInfo
erase_all
Buttercup
No free port available on the host.
{%s} unaligned %d-byte access at address 0x%09llx
Cleaning up Each Booster Manager\n
{%s} _pre_resume_hw result = %s
_remove_instr_breakpoint
Error while initing probemap during %s : %s collecting probes from %s (%s) [RETRYING]
AXbooster_print_boosters
{%s::%s} NULL parameter
ret._handle_exception_for_el
OCD control register, clear
Failed to lock from 
_D
wir2-tdo
HCR_EL2
reset_connect_state
Could Not Find The Astris Init Function (%s) in %s
_read_pc
param.portal.dcm == NULL
exit.exception_test_0
/Library/Caches/com.apple.xbs/76DBD45B-9C35-4E76-99C5-12B5C8C54BA5/TemporaryDirectory.w58zkN/Sources/Manta_restoreos/Vendor/swift-nio/Sources/NIOEmbedded/Embedded.swift
AXcpu_readmem
param.reg_name.invalid.null
backtrace
param.cpu==NULL
{%s::%s} cpu powered off: R_ARM64DBG_EDPRSR_AON@0x%08x = 0x%08x; M_ARMPRSR_PWRUPSTATUS = 0x%08x
RF44
param.info.invalid.null
ProductBuildVersion
ASTRIS_ERR_EXPIRED
writing triage data to 
We are at max iterations, still didnt get full JSON
AuthDbg,EnProbeFuncExternal
Table 5–168
enable(_:)
Requested firmware UUID: 
{%s} bridge returned DECERR
\t[MATCH_SKIP] skipping entry
Address formatting failed
co_coredump -cpu 
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
EXPLORE_JTAGONLY
Miss fraction part in number.
SoC has been setup using standard instantiation (setup result=%s)
regidx_save=%u
AXchip_dock_disconnect_mode
illegalInput(_:)
didDiscover(device:)
{%s:%s@%d} [%s] switching register set\n
CTI_CH_PULSE
{%s} Unable to read CPSR
AXcpu_lacc_bp_status
AXjtag_setclr
EXPLORE_WITH_DISPLAY
ApSecurityMode
Table 5–182
RF26
connecting to selected probe (user-specified single_port)
{%s[select]} %d(%s) [RETRYING]
Ring ASID values
writeFactoryDataRegion(key:value:)
Failed To Initialize Logging\n
JTAG chain not yet explored
(data_.f.flags & kUint64Flag) != 0
pwrite(descriptor:pointer:size:offset:)
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
ASTRIS_ERR_MISMATCH
KIS-STM
dataBlock(blockNumber: 
supports-chassis-reset
, ProductionStatus=
[AsyncSnapshot] #%zu: %s\n
RF27
NIOCore/ByteBuffer-views.swift
Unable to convert Nonce/HWinfo to data
{%s} error %s at line %d
result.read.dbgwrap_base==
STM32F10x_LowDensity_FLASH
%s: %s\n
AXconn_showname
B2PResponse:Ping [
could not perform cpu_preflight
read_dcc
SOC_t
m->name.IsString()
Malformed manta bootarg count != 2: count 
astris_get_die_count
{%s} %s not HALTED. Status = %d ('%s') [Status Read %d times]\n
%s probe[%s] from Probe Map Server [%s]
backupSRAMChunkResponse(report: 
{%s:%s@%d} Drain is full (at %d packets) [%s].\n
addError
interpretTransitionResult(result:mode:)
AXcpu_detailed_status
MEPC
_a64cpu_raise_el_hw
api.is_prod.debug_auth == NULL
address=0x%8.8X, len=%u, rdwr=%d
unhandled error 
{%s->%s} ERROR=%d(%s)
   Debug Base: %08X\n
RemoveMember
forced firmware update
Register file 53
Single_port connection to probe server unavailable
{%s:%s@%d} [%s] setting GPR 1 (todo 1)\n
internal_dft.is_authenticated.debug_auth == NULL
{%s} connectName[%s]
!!!! FILE RADAR: Don't know how to compare two values\n
KIS Chip Found, Doing KIS Explore Setup
M2
Invalid content key, %d
GRP_0
{%s} %s DC cache clean complete, marking as clean
AuthBase_t::init failed (AuthDebug_t)
write_memblock_dbgwrap
FWUPDATE
is.Peek() == 't'
FilePath.Component must be created from exactly one non-root component
NIOPosix/SocketChannel.swift
GPR
ret.reg.write.K_PKA_REG_NAME_DBG_CMD
Cause of last exception
RF7
fn._write_cpu_reg_file.regval
prettywriter.h
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm64cpu.cpp
VECBASE
SAM2
ret.reg.write.K_DA_REG_NAME_ECID0
PROBED_USB_REQ_NODEVICE
Unknown command: 
powerButtonState
==== User Error Messages ====\n
{%s::%s@%d} [FALSE] dest_reg[%d] < GPR_COUNT && != SP\n
CPU.ARMv7m%s
fn._write_general_reg
There's no updater in 
{%s} address range 0x%09llx-0x%09llx exceeds bridge span 0x%09llx-0x%09llx
DBGWRAP_FULL
SOC_t::{%s=>%s} null reference to AXcpu_t record, `cpu`
AXbooster_print_boosters(_:pluginManager:)
internal.clear_probe_auth.chip->soc == NULL
{%s:%s@%d} [%s] \tFailure: only %u of %u write transfers were done (%s)\n\n
sectorErase
ITLBCFG
com.apple.Manta.MantaMCUUpdater
errorDescription
Failed to write DCM GPIO (0x%x): 0x%x
KIS Readvals putting back the value
AXchip_enum(_:index:)
yyyy_MM_dd'T'HH_mm_ss
probeBoardNames
{%s} no chip found
TatsuServer
required parameter is missing
networkSet()
Erasing A Page
val =0x%X is too large for 32 bit unsigned.
[1500] Detected plist version %d
{%s:%s@%d} [%s] unable to drain response\n
{%s::%s} EDSCR with TXU set - recovered (retries=%d).\n
STM_FLASH_OBR: 0x%x\n
Requested Register Requires EL: %d - Highest EL: %d
_a64cpu_restore_el_and_spsr
Misc register 2
fn.entry
{%s:%s@%d} [%s] executing STCpi\n
      Select port %u: already explored..re-exploring\n
fn._ocd_reg_w.DIR0EXEC.instr_32
IOEthernetInterface
resolve_platform_details
astris_addr_which_die
astris_cpu_get_cl4_debug_signpost
EPC3
j1500d
{%s:%s@%d} [%s] Mismatch at offset %zu: expected 0x%02X vs actual 0x%02X\n\n
Crash level
fn.stmflash.h7.lock_flash.flash_idle
B2PResponse:SendValidate [
acc
bridgeInterface(matching:)
rt13/2/pgood/0v855
invalid retimer position 
!!!! FILE RADAR: Failed To Instantiate CPU From Booster:%s !!!\n\n
{%s:%s@%d} [%s] Could not read MCU_IDCODE\n\n
Gathered:\n
{%s:%s@%d} [%s] executing STRHpi\n
https://fdrds.apple.com:8443
getBackupSRAM(device:forceCollect:)
astris_batch_attitude_lose
{%s:%s@%d} [%s] doing IR scan\n
{%s::%s} [%s] error %s verifying SW BP instr (sys AP) [PA=0x%016llX, len=%d]
Going To Create Generic ARMV8\n
AXcpu_cache_cleaninv
{%s} connectName[local host]
com.apple.Manta.TriageController
mempool-dmem-offset-reg
{%s:%s@%d} [%s] reading PAR[64]\n
AXmemap_read_get_field
Using Built In SoCs\n
, bytesRemainingSize: 
TCPProxy::Inbound channel event: 
handleIOError(_:operation:)
latching: EL%d
_sw_breakpoint_insert
RF0
preparePSUFWUpdateRequest()
_a64cpu_write_vfpreg_hw
{%s::%s} [%s] !bpwp_initted, retrying init
ARC
value=0x%8.8X
data-size
relay_set: %s = CMD_ERR (%s)
 is missing, input 
j236CnodeSensors
--> wrstn_wir2 size=%3d dpcsoc=%d
enabled
EDWXVR0+index
param.tgt->ap->dp->chip.null
Exo
{%s} unable to allocate probeInfo
Apple connect client internal error with code 
writeBlock(flashData: 
dart-apf-address
[MEM] Aborted; DSCR = %08x\n
print_debug_regs
empty USB packet encountered
Starting loop for triage
Missing rrko manifest
~HDE
AXcpu_lacc_status_remove
Communication error occurred while connecting to
Cannot perform vector reads on this operating system
15002APB
{%s:%s@%d} [%s] CR read (clear) failed: %s\n
CLOSE
/usr/local/bin/astrisctl
cpu-apselect
ret.write.msr_lock_reg
_a64cpu_assert_state_valid_entry_exit
internal.authenticate.chip == NULL
unlock()
chassisTriageError
Cleaning up Main Booster Object\n
{%s:%s@%d} [%s] unswitching register set\n
_sstep
[AstrisAsync] Activating async...\n
AuthDbg,ProductionMode
pnav_connect_probemap
.otherReadWriteExecute
probeRT13PersonalizationInfo(interface:carrier:rt13Count:retimerController:eventLoopGroup:)
lock_flash
Failed to write register: 0x%llx val: 0x%llx
{%s:%s@%d} [%s] failed to read CMD/STAT\n
fn._init_configuration.w2.audio.HIFI3_1
ide_checker_diagnostic
 when calling pthread_cond_timedwait
astris_booster_cleanup
generate_nonce_and_send_request
ret.write_hang_breadcrumb
impossible reply: 
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
explore-level
MA
Memory error status register
_read_special_reg
{%s} drain_packets=%d, cmd_rcvd=%d, payload_rcvd=%d [%s]
 is below expected value (
ASTRIS_ERR_PROBEERROR
cpu_hwwp_remove
read_memory_dbgwrap
Please run one of the following commands to collect a jebdump:\nFrom Astris Console: jebdump\nOR\nNew Astris Session: astris %s  --xpl aponly --script /dev/stdin {} <<< \"::astris::jebscantools::jebdump\"\nCreate a radar with the jebdump zi
Could Not Find Booster Entry Function: %s\n
AP is NULL
ret.previous_authenticate.timedout
No portal under found for that type
%s_%d
disabled
{%s:%s@%d} [%s] Address must be aligned to length\n
{%s:%s@%d} [%s] FLASH_KEYR write (first) failed: %s\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/probe_comms/astris_transact.c
astris_batch_attitude_attach
{%s:%s@%d} [%s] reading PRSR (oslsr)\n
VBAR: %#llx\n
GPR_1
param.descr==NULL
Probe %s LocationID Info Decoded: Primate: %s Hub: %s KIS: %s KIS Hub: %s
%s [RETRYING]
TCPProxy/TCPProxyHandler.swift
Please file a radar (Astris | all) describing the issue\nand include a capture of this terminal session.
INTDIS
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_mmuv8.cpp
PARTNO_SWDP_M33
General register 6
Failed to allocate space for table!
[AstrisAsync] conditional_check_counter %lu, conditional_check_watermark %lu\n
ret.reg.write.K_PKA_REG_NAME_DBG_CMD.VERIFY
xfer=%u, xfer_length=%u, address=0x%8.8X
Retrieving chip SBIN information
astris_user_default_set_nickname_for_key
Cause of last debug exception
Apple Fabric Timeout
didDiscoverTopologyGroup
chimp
Listing
dst_ != 0
.otherReadExecute
CERTIFICATES_CHAINS_2
init_hw.read.fpb.rev
CNIODarwin_CMSG_DATA
darts
{%s} exec: DC_CSW_X1_ENC\n
astris_user_default_remove_all_boardnames
EXPLORE_PWRGATE
RF17
RF25
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
{%s::%s@%d [%s]} Error %s: reading register ID 0x%X
checking if relay \"%s\" is valid
cpu_resume
async(group:qos:flags:execute:)
Message contains additional unexpected data.
Unable to read LR
Gone
Unable to get lock status from 
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/disassembly/astris_disassemble.cpp
!!!! Critical Error: Error %d(%s) destroying info %p cmdmutex !!!!\n
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache: set=%u, way=%u
{%s} requested bit count(%d) > limit(%d) [probe csv_maxscan(%d)]
internal.clear_probe_auth.chip == NULL
Register file 17
Acdcuc
Channel configuration missing
virtual int ARM7cpu_t::_halt_hw()
Get
Update failure: 
astris_get_soc_resource_filepath
[INSWP] 0x%08llx wp%d rdwr=%X\n
ret.reg.read.K_DA_REG_NAME_PKA_BASE_LO
%@,ChipID%@
channelActive(context:)
CPU
_init_hw
PARTNO_SWDP
JTAGONLY
EXPLORE_NOCLEAN
{%s} %d-bit access to a %d-bit bridge at address 0x%09llx
!!!! Critical Error: Nested exceptions... get someone to debug this. !!!!\n
cpu_getmode
LAM
astris_user_default_copy_nickname
Prompt
-Lite
{%s:%s@%d} [%s] PECR write (clear) failed: %s\n
Waiting for flash to idle before sector erase\n
{%s} %s: |%s|-|%s|
mtu()
getPanicReport(forceCollect:)
Node State is invalid 
listen(descriptor:backlog:)
com.apple.private.MantaKit.mantahostd
MantaXPCInternalPlatformHasAPBs
EvalQuantifier
{%s:%s@%d} Starting drain when partial (%d cmd, %d buf already) [%s].\n
throttle/assert_us
computeNodePolicy
base-addr: 0x%016llX present: %d comp-id: 0x%X - loc-id: 0x%X - feature-id: 0x%X - subsys-id: 0x%X - midr: 0x%X - type: 0x%X
savePanicReport()
Cached async_replay capability version: %u
astris_dpabort
Exc Cause: 0x%x - Exc Vaddr: 0x%x
DIGITAL_CERTIFICATES0
Index is out of bounds
AppleTypeCRetimerCapability
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
{%s->%s} [is_64] exec: DRPS current_el(%d) -> target_el=%d \n
OCD control register, set
Fetching retimer info via dfu.
[AstrisAsync] Pause when already paused!\n
BananaSplit
parse_soc_info_from_booster
ERROR!! Wrote %zd bytes, expected %zd\n
KIS_RSP_OK
fn.stmflash.h7.reflash.program
pcie/cablepresent
Failed to exec MRS to bounce sysreg into scratch register. scratch=%d, sysreg=0x%X, regname=%s
Error - STM32Fxxx reflash failed (%s).\n
fn._ocd_reg_w.ddr.t1_save
No component name in options dict
astris_exc_bread_test_2
DebugAuth
Register file 3
{%s@%d} Unknown CS code [%u]
SoC must have a DAP
cpu_lacc_count_remove
message
Initial state. MantaKit has not finished discovering the system
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
Bug
AXbooster_interface_create_swdflasher
cpu-group
{%s:%s@%d} [%s] executing MSR\n
PROBED_USB_REQ_EMPTY
relay_get: %s = %d
\t[MATCH_MEMAP] %s <= AXmemap_read(ap, 0x%08X, &value)
KalElBootService/BootServiceRemoteDevice.swift
com.apple.Manta.AstrisProxy
param.conn.connected == false
AXdebug_auth_get_dft_timer_count
Image sections:\n
User created bundle found, ignoring version checking via plist
development
Entry: 0x%X - Type: %d Pages: %d EPP: %d Start Page: %d\n
AXjtag_explore
X12 Part
fn._read_special_reg.ibreakenable
readvals: %s
AXportal_reset_dcm
Invalid file name: \"%s\". File names must not start with '.'
check_for_flash_error
ASTRIS_ERR_USB_NODEVICE
comparing against match entry [pid] %d: %s\n
error
Automatically disconnecting on deinit
Min Component - %s\n
Failed to setup wp=%d
Probe Map comm: request[%s], response[%s]
set.os
KalElBootService/BootServiceInsecureStateMachine.swift
unknown
FLASH_SR (0x%llX) read failed while polling busy bit\n
Outgoing data streaming completed
Register file 48
MiniSWD (USB Comm)
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s\n
bad parameter(s) specified
triageKalElPanic(_:downstreamKalEl:port:)
Generation of the nonce timedout\n
Only Auth-Debug, Auth-DFT and Probe-Auth are currently supported.\n
 did not match expected seal byte 
MEMAP
{%s} Unrecognized Component: %08X (class %u)
PARTNO_SWDP_SOC600
fn._ocd_reg_w.ddr.address
No 1500 bridges or TAPs specified (v2 plist)\n
Not supported SpanAttribute array type: 
Retrying retimer 
{%s::%s@%d} [FALSE] base_reg[%d] < 15\n
com.apple.KalElKit.BootServiceSecureUpdateStateMachine
Tracing/Span.swift
Found another target for the plist\n
cpu-explore-flag
[%s] {%s->%s} current EL (%d) already <= target EL (%d).\n
connection not currently open
%s SoC created
com.apple.Manta.Retimer:
_a64cpu_get_current_el_hw
SSO info present but SSO disabled.
Register file 4
Warning
NIOCore/NIOAsyncWriter.swift
_clean_dcache_setway
ParseFalse
fn.stmflash.h7.mass_erase.read_optcr
sendfile(descriptor:fd:offset:count:)
B2PResponse:ReadID [
dest_gpr < 32
open_flash
fn.AXmemap_read.address.regval
readAsync(upToCount:queue:polling:)
astris_remove_loaded_soc_boosters
{%s} masked_read[ED32] of %s @ address 0x%016llX ERROR %d(%s) (mask=0x%08X, expected=0x%08X)
get_mair
code
devicesDuplicated
cio/grp0/1/force_red_on
irlen
{%s:%s@%d} [%s] flushing state\n
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (2: probe-auth expired)\n
EPC1
op_S8I_encode
No nonce in options dict
isWritable cancelledYields suspendedYields elements delegate 
Required Key-Value is a string, and not an array. Old booster found: %s\n
ret.createKey
{%s:%s@%d} [%s] readvals failed: %s\n
Register file 14
AXbreadcrumbs_read
Got empty panic report from MCU 
Too many portals, we are at portal: %d while max is %d\n
SPSR_EL1
ASTRIS v%s%s [%s]
KobaSWD
AXchip_fromreset
updateRT13s(interface:carrier:)
APCIE_REGS
AXmemap_stmflash calling STM32Fxxx::reflash(0x40023C00)\n
Table 5–170
Table 5–150
_setup_data_bp
no board info file loaded
PAR_EL1
Stale firmware running on device.
Failed to read ide_table from KIS explore
far_el3
AppleTypeCRetimerCapability not found.
callback(callback:context:)
fstat(descriptor:outStat:)
fn._collect_snr.exccause
complex-id
   Created Fake Debug Port Debug Port
Register file 34
astris_clear_user_die_select
{%s} L2 cache operation completed [%s]
internal.authenticate_dft.chip == NULL
Register file 52
%s_%s
ACQ_SETUP
Stringify
Unknown section type value 
[ARM64] exec(DCPSX_BASE_ENC)
porpath
_init_registers
CPU.ARM7
ret.reg.write.K_DA_REG_NAME_CHIPID
signalNotSupported
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
AP[%d]: JTAG_AP (Exploring Later) \n
/AppleInternal/Applications/PurpleRestore 3.app/Contents/Frameworks/MobileDevice.framework
{%s:%s@%d} [%s] PECR read (erase) failed: %s\n
FLASH_WRPR1BR
usb/parrot_reset
Error closing %s [%d]
Failed to boot device: 
Register file 61
PUBLIC_KEYS_4096
error when moving file: 
reset_dcm: %s
.truncate
Resolved triage policy: '
kis_stm_name %s %d
{%s} Error reading PID (%s)
Running hardware test
EPS3
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
Could Not Find Bank (%d) For Address: 0x%08llX\n
\tCould not erase flash\n
Requires OCD option for >1 address breakpoint regs.
 successfully enabled.
can't call whenReady for selector as it's 
sense/i12vfan/alert
fn._write_special_reg.ibreaka0.address
unexpected filter 
KalElBootService/BootServiceClient.swift
Absent
   {%s} Enabling debug unit\n
dpb-size
_setup_wp
AuthDbg,EnSecureTestExternal
ComputeProxy already closed.
setResult
.sharedLock
Invalid value for 'entry' tuple element - can't index
Warning: Unable to access Astris log directory [~/Library/Logs/Astris] (using alternate [%s])\n
{%s} unable to find single_port probedaemon on port %d
No host IP found for interface 
AuthDbg,Nonce
Table 5–156
{%s} Read dbgbase(0x%llx) + R_CS_COMPONENT_ID1: component=0x%X
fn._resume
fn.stmflash.h7.wait_bank_flash_idle.timeout
NoSOC
GetState
supportPSUFirmwareUpdate
Register file 38
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
probe %s on host %s
KalElUIService/UIServiceClientChannelHandler.swift
complex-cpu-id
{%s:%s@%d} [%s] CR read (erase) failed: %s\n
com.apple.Manta.MantaRestoreUtils
{%s} write[ED32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
astris_preferences_subsystem_monitor_list
After Programming (addr: 0x%08llX) Write Protection Error is Set: 0x%08X
Skipping restricted address write: 0x%llx (in range 0x%llx-0x%llx)
Successfully connected to server, %s:%d
RemoveDotSegments
RT13Updater/RT13Updater.swift
{%s:%s@%d} GRPS[0] cached\n
FPI2C
Unknown error.
Heartbeat received
AuthDebugWithTimer_t::check_timer_and_clear_timeouts timer STATUS (1: DFT-auth expired)\n
Table 5–165
Incorrect typeid
rt13/0/pgood/0v855
AXbooster_refresh
{%s} read ESR EL1|EL2|EL3 (%d)
unexpectedResponse(_:)
ret.createKeyWithPrimate
{%s} status=%d being reported as Unknown
UNKNOWN CODE
personalizationInfo(ecid: 
%-16s @ 0x%08llX : 0x%08X\n
ret.raise_el.write
Chip %x Status = %d\n
access to target is blocked
MantaUtilities/IPv4Address.swift
 from ConnectX firmware image.
rt13/0/pgood/0v805
esr_el1
SAR
Parity Error on RUN-SWD Subcommand
Ending loop for triage
socTriageDataReady
{%s:%s@%d} [%s] writing DTRRX\n
newpos == 0 || path_[newpos - 1] == '/'
Application firmware is missing embedded bootloader firmware
Writing FDR key: 
IORegistryEntryGetRegistryEntryID interface failed\n
--> localwrstn size=%3d debug=%d
{%s} Error reading CPUID (%s)
[PREFS] Key: %s - Val: %s
, boot2BSHA384: 
{%s:%s@%d} Nested exceptions... get someone to debug this.\n
symbol.check.loaded.AMAuthInstallGetLocalizedStatusStringPtr == NULL
XPCObjectEncoder or XPCObjectDecoder is required to encode or decode this value.
rt13/3/pgood/0v855
--> 0x%02x = %s
{%s} Failed to extract chip debug base from table (%d); continuing anyway
[%s] EL @ end of Collect: %d\n
AXcpu_readreg
astris_memap_bus_write
fn.stmflash.h7.unlock_flash.write.cr2.key2
No chipRev in options dict
Erasing to write 
wb_u32=%u
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
Carrier manager capability is not present
_set_bpaddr_hw
got a translation error translating VA to PA
AuthDebugWithTimer_t::need_to_authenticate_dft super returned false; continuing \n
Register file 39
{%s} flags:0x%08x
\t[MATCH_TARGETID] %s <= ((0x%08X & 0x%X) == 0x%08X)
Complex CPU Name: %s\n
Section 5.2
CountStringCodePoint
setTargetOS
AXconn_disconnect(_:)
AXbooster_interface_create_cpu
fn._ocd_reg_dsr_w.dsr_status_to_clear
com.apple.Manta.MantaMCUUpdater.TryBootRetimers
internal.get-timer-count.chip == NULL
%s: chip was NULL when attempting to release soc
baseAddr
ioctl(SIOCSIFVLAN): %d\n
Match Count is Zero. This is invalid.
ret.die_count == NULL
lower.safe.aarch32=notsupported
ASTRIS_ERR_BADPARAM
astris_ide_get_pid
AXcpu_read_dcc
cpu_hwbp_disable
first stage bootloader
connect(to:interface:port:logger:timeout:)
unsafeSet(_:value:)
{%s::%s} HDE not set on %s. Will re-enable.
L1_DATA
EPC2
/Library/Caches/com.apple.xbs/76DBD45B-9C35-4E76-99C5-12B5C8C54BA5/TemporaryDirectory.w58zkN/Sources/Manta_restoreos/Vendor/swift-nio/Sources/NIOPosix/Bootstrap.swift
Update MCU proxy: 
Failed to find a plist for this soc %s
{%s:%s@%d} [%s] scanning out\n
HardwareStep
R7
cpu_collect
## memapr %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
implementer
{%s:%s@%d} [%s] reading PRSR (oslk)\n
_a64cpu_read_sysreg_hw
Failed to write CR reg @ 0x%llX\n
GETRELAY
isDone(updater:outError:)
basic_string
!!!! Critical Error: GRPS[1] cached !!!!\n
entrySetProperty(propertyName:property:)
Failed to read register: 0x%llx
RF38
probe [port %u] on localhost
{%s:%s@%d} [%s] unable to read response payload\n
nonceHashResponse(bootloader2ANonce: 
{%s} DAP command requesting nwords=%d not allowed [must reduce to %lu]
fn._ocd_reg_w.ddr.regval_save
Test carriers present pass, carrier(s) present
#/Chipid: (\\d+) Fuse: (\\d+) Secepoch: (\\d+) prod: (\\d+) sec mode: (\\d+) sec dom: (\\d+) rev: (\\d+) chip: (\\d+) Board: (\\d+)/#
Register file 50
superEncoder() is not supported for XPC encoding and Codable still doesn't throw from this method
min max 
entry.exception_test_2
M4
m_wp_details
not in xpc context
{%s} %d(%s) [RETRYING]
CortexA7
Updating boot2A.
[AstrisAsync] Async mode %s
host_to_components
createConsoleProxy(bmcIPv6:bmcIPv6Interface:eventLoopGroup:consoleType:)
AXcpu_hwbp_info
param.reg_index.invalid
Failed to convert primateLoc %s to unsigned long long
i
Unable to convert plist file name to CFString: %s\n
{%s} m_exception_level(%d) != current_el(%d)
{%s} probe [%s] added to list
Exception occured after executing MSR to write into sysreg
ret.get.da
fn.stmflash.h7.sector_erase.flash_idle.after_sector_erase
%s given a NULL conn object
haskis
wir-wirshiften
!!!! Critical Error:  dlr_el0 NOT DIRTY !!!!\n
R12
plist
cpu_halt
XBS Version Modified: %s -> %s\n
.rsd
JsonLogger: Creating new category '%.*s'
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
[AstrisAsync] replayConditionalCheck: condition hit!\n
Invalid update/boot of insecure device with SecureBoot API
cpu_get_cl4_debug_signpost
Parse
This XPC file handle was already consumed and can't be converted to an xpc_file_transfer. This is a logic error in the caller.
Signal service connected 
tdi-wsi
_read_memory_slow
%s: not supported.\n
[%s] TGE is set so we traping to EL2\n
Register file 40
dr ->
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis.cpp
astris_exc_bread_test
{%s->%s} m_exception_level=%u
Table 5–129
, securityEpoch: 
value doesn't fit in UInt8
cio/grp1/3/cable_present
invalid hwinfo format: 
{%s} a=%09llx d=%016llx rdy=%llx err=%llx write=%llx
<unnamed>
fn.local
cpu instr. 0x%8.8X caused an execution exception. OCD.DSR = 0x%8.8X
 <--[TCP]--> Proxy
Size or Count provided are 0.
astris_batch_attitude_suspend
postinc < ARM64_LDRSTR_POSTINC_MAX_IMM
op_SDDR32_encode
(%s) %s
Unknown message type 
discovered
{%s::%s} [%s] length=%u when width=%d
offset element 
, productionStatus: 
{%s} Thread %#llx key %lu exiting when owner of info %p lock - IMPLIED BATCH END
_get_num_hwwp_hw
{%s:%s@%d} [%s] busy timeout before open: %s\n
Failed to get KIS STM Probename\n
_set_wpcr_hw
stdout
ASTRIS_ERR_USB_NOTOPEN
{%s}#%02X %s [%s]
cpu_lacc_pipe
No chipID in options dict
AXcpu_writemem(_:address:buffer:iflush:)
[%s] HCR_EL2 @ collect_hw: 0x%llX\n
gpr != 31
%s (addr=0x%llx -> val: 0x%x)
.nonBlocking
DatagramChannel { 
Form-factor specific channel not found, falling back to generic channel for device '%s'
astris_memap_debug_writebuf
.name
ir <-
Register file 59
stat
addMember.engineer.message
sendmmsg(sockfd:msgvec:vlen:flags:)
## ARM32cpu_t::read_register 64 bit 0x%x\n
CIP_GEN_NUMBER == 0x%08X. Adjusting offsets of PKA_DBG registers by + 0x150000.\n
Invalid SoC Booster. SoC Booster Requires PID\n
{%s} [remaining=%d] exec: ldrstr_postinc(%d, %d, %d, %d, true, %d)\n
fn._ocd_exec_instr.wsr.ddr.t1.1
fn._write_special_reg.ibreakenable
model
Miss exponent in number.
getIPv6Addresses(bsdName:)
KalEl not ready for booting into PSU update mode
unable to read memory (permission checks suspended)
fn.stmflash.h7.sector_erase.param_check
CortexA5
createService(interface:)
[AsyncSnapshot] ===== DONE DUMPING SNAPSHOTS =====\n
CPU%d
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
REG
Connection is null
invalidFactoryDataServiceValue
!!!! Critical Error: batch attitude thread trying to lock - CAN'T LOCK !!!!\n
normal
securityDomain
Outbound channel event: 
_a64cpu_set_singlestep
En masse...\n
Algorithms/FlattenCollection.swift
Existing firmware version: 
Writing MER in FLASH_CR failed during mass erase\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
{%s:%s@%d} [%s] reading CCSIDR\n
is_external_open
ESR_EL2
SWDACKDELAY relay write failed\n
      AXap_read of R_JTAGAP_PSTA failed with error %s
Error status from AMAuthInstallSetSigningServerURLPtr = %i
Debug Port
[PAR]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total read=%u
write(descriptor:pointer:size:)
Internal error: 
j226CarrierSensors
{%s:%s@%d} [%s] FLASH_SR read failed while polling busy bit: %s\n\n
fn.stmflash.g071.mass_erase.flash_idle
result.read.portal.s2r_fsm
   {%s} Clearing HNONSEC on AP \n
Thread pointer
Invalid XPC Object type: Expected file descriptor, received 
{%s} bridge returned an error
SWD
ATOMCTL
Register file 22
/
DefaultConnectAddress
astris_batch_attitude_resume
AXconn_copy_nickname
{%s@%d} astris_command: Astris Async: Outstanding commands detected while paused!
specified CPU is not available
updateRetimerPlug(enable:)
failed to bring up %s\n
ApBoardID
Previous authentication in-flight, wait for it to finish\n
TRANSLATION_ERR_L3
3679.40.30b172
RF59
.os
cpu-die
{%s:%s@%d} [%s] writing CSSELR[L2]\n
HIDBridgeSWD
CreateSchema
DataSource(firmware: 
HardwareWatch
AuthDebug_t::need_to_authenticate error reading ACTIVE reg: err=%s\n
sso_user.sso_data_length == 0
Instruction break 1 address
param.ocd_base_address.invalid.unaligned
current != kRegexInvalidRange
digestInfoRequest
Personalized RT13 Firmware: manifest=
base
_read_memory_fast_try_with_chunk
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
sourceid errorDescription 
pid
Taking gateway control failed
ERR: conn->nchips != 0; looks like chip is explored\n
OK: address translation resumed for %s successfully
_ocd_reg_w
%d.%drc%d
Primate-Null
is.Peek() == '['
, boot2BLength: 
Found a portal of type 0x%x and version 0x%x with a ID 0x%x and name %s (%d)\n
\tWhole chip...\n
MantaRetimerController/RetimerController.swift
ret.AXmemap_read.board_id
ret.storeNicknameForKey
JSON structure error: key '
IOService
BMC serial number not found.
ret.read.edscr.start
AppleARMIODevice
Test Mellanox fan pass, fan was above 
cacheAllRetimersHWInfo()
Failed to read RT13 
{%s:%s@%d} [%s] handling pending async aborts\n
{%s->%s} [!is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
cpu
ret.relay.get.hostid
Invalid GPR Given: %d > %D
Error %d(%s) executing instruction 0x%08X
{%s::%s} [%s] error %s from _synchronize_context.
RF35
GETSETTCK
Device already running other operation
remote-debug.tar.gz
      Select of JTAG-AP port %u failed with %s\n
com.apple.Manta.AppleConnectManager
fn.stmflash.g071.page_erase.read.cr_reg.before_start
taps
[FLUSH]\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_debug_auth.cpp
{%s:%s@%d} [%s] \tFailure: region @ 0x%08llX failed to verify\n\n
Warning: after SoC setup, Astris cannot access the consistent debug root register. Most likely target device is HUNG.\n
MEPS
ff02::0014:1eee:1
com.apple.Manta.Subprocess
soc-revisions
probe [port %u] on host %s
AstrisNativeTriage: Launching Astris with: 
STM32Fxxx flash programming status fault: 0x%08X\n
Error %s connecting to probe server
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
ret.get_current_el.initial
getOrCreateArray.generated_files
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
MAP_CMD
host
personalizationRequestQueue: 
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm32cpu.cpp
_pre_resume_hw
AuthDebugWithTimer_t::check_timer_and_clear_timeouts actual_load: 0x%X (req_type %d)\n
{%s:%s@%d} [%s] Buffer data to RAM failed: %s\n
Table 5–159
backPressureStrategy buffer continuation hasOutstandingDemand iteratorInitialized 
{%s} Failed to get breakpoint mask for %s: %s
Misc register 0
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to clear\n
Target is not a JSON object
read
UPDATE cop64 %d -> 0x%016llx\n
{%s} write[CTI32] of %s @ address 0x%016llX [%s] ERROR %d(%s)
nothing written
addService(service:)
{%s:%s@%d} [%s] reading DIDR\n
AXdebug_auth_clear_sso_user
XTENSA
memap_bus_write
Expected to decode Double but found a 
IONetworkInterface
ELR_EL2
%02u:%02u:%02u:%06u|%s <%s> %s\n
Subsystem Monitor Key does not exists: %s\n
Misc register 1
param.bp_info.invalid.null
!!!! Critical Error: current_el[%d] <  %d !!!!\n
param._tgt.invalid.null
Unable to register assert upcall %s (Insufficient memory)
init(remoteAddress:)
result.extract_version==
{%s:%s@%d} [%s] readval: %s\n
[%s] %d -> %08x\n
Register file 57
Write operation was cancelled
SPI
Invalid IPv4 String literal.
Data break 0 control
{%s:%s@%d} [%s] failed to setup connect\n
parent()
connect(descriptor:addr:size:)
Failed to cleanly disconnect: 
RT13Updater/RT13DFUClient.swift
Unable to connect to probe server
AXbooster_cleanup(_:)
[PAW]: id=%s(0x%X) - addr=0x%llX - count=%u - size=%u - total write=%u
!!!! Critical Error: {%s->%s} EL3 not implemented !!!!\n
Ticket Data is NULL\n
DBREAKC0
Invalid sector %d\n
from
No 1500 bridges specified\n
DeviceInfo
IOInterfaceNamePrefix
ret.clear_edscr_err
/Library/Caches/com.apple.xbs/76DBD45B-9C35-4E76-99C5-12B5C8C54BA5/TemporaryDirectory.w58zkN/Sources/Manta_restoreos/Vendor/KalElKit/Sources/KalElUIService/ClientServer/UIServiceServer.swift
udid info 
{%s:%s@%d} [%s] destination address (0x%08llX) is not %zu-byte aligned: %s\n
[REM_WP] wp%d\n
ret.reg.read.K_PKA_REG_NAME_DBG_STATUS
{%s} FAILURE - malloc error
uri.h
Couldnt figure out the size of flash, defaulting to 1MB\n
MantaTriageController/TriageController.swift
virtual int ARMv6cpu_t::_halt_hw()
General register 2
ASTRIS_ERR_PROBETIMEOUT
enabled(_:)
componentName
Writing block at offset 
cpu-xtensa-reg-size
dart-name
KIS_DOCK
!!!! Critical Error: m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15 !!!!\n
{%s->%s}[cached] %s[0x%X] = 0x%08llX
_NIODataStructures/Heap.swift
Can't advance past endIndex
{%s:%s@%d} [%s] Read DWT Func %u\n
_ocd_reg_dsr_r
rt13/1/pgood/1v2
** CPU %s requires forced explore override flag on this SoC **\n
_write_memory_slow
AXcpu_go
add(protocolType:)
NIOCore/NIOAny.swift
BoosterManager.Utility
CTI_INT_ACK
General register 10
RF9
fn._read_special_reg.dbreaka1
%s/%s%s.bin
ret.reg.write.K_DA_REG_NAME_NONCE_3
param.num_addr_bp_regs.invalid.1
RestorePacket [bus=0x
--> master     size=%3d localwrstn=%d debug=%d
xres = %p, table = %p, key = %d
AuthDebug_t::need_to_authenticate error reading AP_DEBUG_EN reg: err=%s\n
fn._ocd_exec_instr.rsr.ddr.data_reg
Received unexpected reply 
param.booster_bundle==NULL
mempool-base
Failed to get Bypass Config
{%s:%s@%d} [%s] setting DTR MODE to FAST\n
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
{%s:%s@%d} [%s] going to RTI\n
SOC PANIC! Triaging '
CTI_OUT_EN1
{%s=>%s} no soc reference; falling back to direct cpu method
from != 0
{%s:%s@%d} [%s] doing JTAG scan (DSCR data)\n
defaults.nickname.too_long
' written at document root (failed to create parent object '
remove()
!!!! Critical Error: Took an exception that took us to exception level[%d] other than 1, 2, 3? !!!!\n
AXdebug_auth_authenticate_dft
RF22
{%s} masked_read[ED32] of %s @ address 0x%016llX = 0x%08X (mask=0x%08X, expected=0x%08X)
_a64cpu_read_edscr_masked
authenticate_dft
internal.is_authenticated.debut_auth == NULL
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_kis_error.cpp
ASTRIS_ERR_SLEEPING
Unable to connect to %s - %s
XSTAT
BundleDataDict
wait_for_flash_idle
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
\tErasing the entire chip and then programming a larger image may work,\n
{%s:%s@%d} [%s] reading GPR 1\n
get_current_mmu_regs
failed to read memory; can't confirm breakpoint set
Failed to sync prefs at beginning
*
FW_INTERNAL_USAGE
{%s:%s@%d} [%s] timed out waiting for reg_index %d to equal: ((0x%08X & 0x%08X) == 0x%08X)\n
Failed to read transfer register (EDDTRTX)
swdovrrun
INVCHIP
{%s@%d} socket connection is not available
interface(bsdName:)
AXdebug_auth_supported
LoopInstance
.groupRead
Requested To Read %d words, instead %d were read (Requested: %d != Actual: %d)\n
[PCW][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
MantaMCUUpdaterCore/TryBootRetimers.swift
Error: No IPv6 addresses in SCDynamicStore.
wir-size
.groupExecute
Register file 11
PCIE_PHY_UC_CODE
unswitch_regset
## armcpu-w: %s 0x%016llX (%d bytes) -> 0x%08X\n
Reading FLASH_CR1 failed during unlock sequence\n
Unknown error (errno: 
AX1500_listbridges
_a64cpu_read_aarch64_sp_hw
ASTRIS_ERR_MISSINGPARAM
AstrisArmProbeServer-3679.40.30~172 (RavePopB tools)
digestInfo is missing
using multi-target booster products_%s.plist
Unable to read CPSR
couldn't read TCR
Data must be at least 6 bytes
--> misc_wdr   size=%3d wirtestporten=%d
General register 14
AddressedEnvelope<ByteBuffer>
{%s:%s@%d} [%s] FLASH_CR LOCK read failed: %s\n
preparePSUFWUpdateRequest
Unique required when multiple probes
Run
SoC has been setup using standard instantiation (setup result=%d)
PushUnsafe
socTriageComplete
fn._ocd_exec_instr.wsr.ddr.t1
Invalid instruction breakpoint index %d
[Auth Debug] Ticket Active, Debug Interface Locked\n
OCD ID register
param.len.invalid.>64
op_WSR_encode
param.s0.invalid.!=0
allocators.h
 total remaining attempts.
io.swiftnio.extras.WritePCAPHandler.SynchronizedFileSink.workQueue
General register 4
{%s} Batch attitude key created for %p thread %#llx key %lu
Connecting to server, %s:%d
Gathered Info:\n%s
[1500] v2 plist 'taps' must contain exactly one entry (found %d)
JTAG
writeToFile
Cannot get registry entry for product
RF23
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
high word
cpu_lacc_count_read
type == kStringType
appendToArray
Invalid IPv6 String literal.
%@,Nonce%@
Connection invalid.
ioctl(SIOCLL_START): %d\n
!!!! CPU Key %s is INVALID !!!!\n
{%s:%s@%d} [%s] doing IR scan (DIDR SCAN_N)\n
{%s:%s@%d} [%s] clear_flash_errors failed: %s\n
astris_server_send
opcode
FLASH_WRPR1AR
read_resp_cmd_via_sock
if-restore-bringup
{%s::%s@%d [%s]} Error %s: cleaning dcache vaddr: 0x%llX
FLASH_SR
SEP
defaults.get.nickname.not_connected
_synchronize_context
{%s:%s@%d} [%s] Cannot initialize flash for erasure: %s\n
fn.__ocd_reg_w.ddr
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
## apr %u 0x%08X %d -> 0x%08X ...\n
fn._ocd_reg_r.dsr
Unknown message status 
vlan
{%s:%s@%d} [%s] updating CPSR\n
~A
Test carriers present test, carrier(s) missing
WARNING: %d KB flash size detected.\n
mxwrap-address
internal.is_authenticated.chip->soc == NULL
Writevals: %s
 in data source 
Unexpected response.
nothing
UserCreated
Waiting for flash to idle after starting sector erase, failed\n
Failed to enable management network interface
Failed to Identify & Explore Chip via KIS: %d (%s)\n
AuthDebug_t::need_to_authenticate AP_DEBUG_EN reg: 0x%X\n
{%s:%s@%d} [%s] FLASH_CR MER read failed: %s\n
PROBED_LOSTCONN
{%s->%s} exec: encode_msr(MDDTR_EL0, scratch=%d, true)\n
Unable to read FP
{%s::%s} [%s] REM_SWBP error=%s %s [VA=0x%016llX]
param.tgt->ap.null
fn._ocd_reg_r.ddr.regval
Bug detected
Bootloader Version is less than E008. Unable to fetch backup SRAM
IOConnectSetCFProperties failed: 0x%x\n
{%s->%s}
Failed calling AppleSOC_t::switch_taps\n
.ownerWrite
User chose to quit from escape menu
_read_gpr
[AstrisAsync] replay preflight: Async not active!\n
AXconn or json_out are NULL
Toto
AuthDebug: %s - AuthDebug with Timeout: %s - ProbeAuth: %s - DFTAuth: %s\n
SP
_insert_watchpoint
closeSuccessHandler(_:_:)
TagNumber
LoggingExtras/MantaLoggingSystem+SignalHandling.swift
get current mmu registers failed
AXcpu_suspend_translation
fn._write_special_reg.srn.regval
ScheduledTask(readyTime: 
ret.ito.clear_edscr_err
{%s::%s} [%s] error %s reading SCTLR_ELx
[%s] CPU BM Not Found, Bailing\n
MiscCortex
Stepping Stone Val. SW Info Address Relative to VBAR: %#x\n
Communication failure with probe server
ARMV6M
Failed to find paf file/s at/in 
{%s:%s@%d} [%s] writing CSSELR[L1-D]\n
api.is_prod.chip->soc == NULL
SelectableEventLoop { selector = 
Failed to write JSON
Could Not Allocate Info Keys Array
PARTNO_SWDP_M7
[Auth Debug] Auth Active - External Debug Interfaces Closed\n
RF50
KalElSignalService/SignalServiceMessageLogger.swift
set
Result while reading second entry: %s , entry val 1: 0x%X\n
interface not in appropriate state for action
start
failedToConnectToRemoteService
/AppleInternal/Library/marvin/site-packages
/swdflashers
[INIT]\n
2.34.0
schema.h
Wrong type, signal expected to be of type 
failed to create dgram socket\n
Failed to restore EL to %d after writting register: 0x%llx
hwwp_remove
{%s@%d} DP write FAILURE (%s) - performing DP ABORT and retrying
Connected
index < 87
protocols()
PowerController
[INSBP] bp%d addr=%08llx fpr=%08X\n
Couldnt figure out the size of flash (we read: %d), using default\n
astris_server_read
sending abort to clear a timeout\n
 RPM, within expected range 
\tCould not get sector number for address: 0x%llX\n
didReceiveButtonsEvent(withButtonsState: 
{%s:%s@%d} [%s] updating ADFSR\n
AXcpu_translate_par
max_scan_bits is low: %d
\tCould not get sector size for address: 0x%llX\n
Xtensa Option options: 0x%x
coredump_diagnostic
!!!! Check that Buttercup has been configured to route KIS to the Debug Port !!!!\n
status=%u, flags=%u, DSR=0x%8.8X, DCR=0x%8.8X
ASTRIS_ERR_NOTUNIQUE
queryPersonalizationInfo()
No subscribers to post 
{%s:%s@%d} [%s] Waiting for flash to idle before lock, failed\n\n
ret.cfg_write(R_DCM_GPIO).deassert
AXcpu_lacc_count_clear
LITBASE
CPU is not halted
matching(port:query:)
AXmemap_stmflash(_:baseAddress:buffer:eraseAll:quiet:)
[%s] E2H is set, virtualization is supported\n
Invalid bp = %u. Should be in range 0..1.
ARMV7EM
[%s] {%s->%s} clear async abort
ret.init_params.raise_to_min
M3
NIOPosix/BaseSocket.swift
Updating application.
didChangeState(from: 
dfu-type
{%s:%s@%d} [%s] writing ITR\n
clzll.h
configuration(_:)
No hardwareInfo in options dict
fn.stmflash.g071.mass_erase.write.cr_reg
{%s} Failed to extract portal info from table (%d); continuing anyway
{%s->%s} exec: aarch64_add_imm(scratch=%d, REG_SP)\n
Raising to EL2 cause in Guest\n
firmwareVersion1
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/flashers/astris_stmflash_g071xx.cpp
    %s(): %s
[MEM] Uncompleted; DSCR = %08x\n
[%s] {%s->%s} Transitioning to exception level %u.\n
successfully updated DEMCR
{%s} _halt_hw result = %s
{%s:%s@%d} [%s] timeout waiting for flash idle: SR = 0x%08X\n
var.num_loops.invalid.>3.prev_instr
RTKitOS
result.AXproduct_copy_bypass_info_for_bid
Reset
AP[%d]: JTAG_AP (not exploring, use --enable-jtagap to explore)\n
symbol.check.loaded.AMAuthInstallSetSigningServerURLPtr == NULL
FLASH_WRPR2BR
The document root must not be followed by other values.
API.
register lookup by name not supported when Astris is statically linked
The surrogate pair in string is invalid.
init(configuration:)
CPU.ARM32
_init_params
      AXap_write of R_JTAGAP_PSTA failed with error %s
Interrupt enable bits
Register file 47
 (%s)
[1500] TAP key is not a valid integer
{%s::%s@%d} [FALSE] gpr[%d] < T32_GPR_COUNT\n
internal.enable-timer-ovr.debut_auth == NULL
{%s:%s@%d} [%s] Waiting for flash to idle before unlock, failed\n\n
CPU Supported in Runtime: %s\n
Failed to convert %s key @ index %d
{%s->%s} [is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
CPU.ARM
OCDID
Xtensa Core %s NOT configured\n
Process signaled 
{%s} Exploring with option: %s\n
Stop Clock Active
CortexA53
Failed to fetch capability: 
!!!! Critical Error: current_el[%d] == 1|2|3 !!!!\n
No Success after retry on wait
Schema validation failed at: %s (keyword: %s)
Failed to load paf at 
System software is updating
Efficient-Core
{%s:%s@%d} [%s] executing LDRBpi(1,0,1)\n
astris_dump_exploreflags
cpu_hwwp_insert
Finished input queue runloop
{%s:%s@%d} [%s] failed to read cfg reg: %d\n
!!!! Critical Error: m_current_rw_is_64[%d] || val[0x%llX] < UINT32_MAX !!!!\n
_a64cpu_reset_catch
transitionTimeout(to:
astris_command_async
ret.reg.write.K_PKA_REG_NAME_DBG_STATUS
The log file has been updated with all available diagnostics.\n
RESPONSE_PAYLOAD
update(device:application:boot2A:boot2B:)
dr <-
chip->ide_table == NULL
Register file 23
%02u:%02u:%02u.%06u|%s <%s> %s
ASTRIS_ERR_USB_PROBED
primateLoc
{%s} select success without file descriptor set
MantaFirmware/MantaPAFirmware.swift
rt13/11/pgood/1v2
MantaRetimerController/RetimerWatcher.swift
set.wp.len > 4 && addr & 0x7 != 0
Explore: %u chip%s\n
firmware version is too old DEPRECATED
ARMV4
_read_memory_fast
couldn't read TTBR0
[AstrisAsync] Resume when not paused!\n
fn.stmflash.h7.unlock_flash.read.cr2
ret.test.2.1
{%s->%s} (top) current_el=%d
base_reg < 15
init_hw.set.dhcsr.en
[PREFS] Key: %s - Val: NULL
securityMode
Register file 24
Device missed heartbeat check-in.
posix_spawn failed: 
mission mode is not implemented
{%s:%s@%d} [%s] Writing KEY1 During Unlock Sequence Failed: %s\n\n
RF16
TLR
write_register
Failed to read CR reg @ 0x%llX\n
%c
maxAPBCount set to 
AXexplore_set_explicit_mode
New
Successfully Authenticated\n
{%s:%s@%d} [%s] FLASH_CR sz read failed: %s\n
RF2
_write_special_reg
[AstrisAsync] Discarding response due to ASYNCSKIP state!
Acdcuc%i,ApplicationFirmware
personalizationRequest
connecting to remote TCP socket at 
Cant find Debug Auth Registers. Auth not supported
MESR
CPU3
Cannot take retained value for sbin config
param.reg_name.invalid.<0
PersiesSWD
cpu_readreg
Full JSON that failed validation:\n%s
com.apple.Manta.KalElController
param.tgt.null
chip is 0??\n
astris_soc_check_debug_root
cpu-armv7m-dmem-size
cpu_resume_translation
 message, expected 
input closed, forwarding EOF
{%s:%s@%d} [%s] executing STCpi(uint32_t)\n
fn._ocd_reg_dcr_clr.dcr_enable_ocd
target not in appropriate state for action
BYPASSCH
Incorrect hex digit after \\u escape in string.
MantaInternalManagementVLAN
Factory Data Region error
STM32G0B1xx
{%s:%s@%d} [%s] getting GPR 0 (ARB)\n
Verification Mismatch starting at offset %d\n
hid
{%s@%d} timeout waiting for ARMOSLSR_LOCK to clear (oslsr=0x%08X)
rt13/6/pgood/1v2
Failed explore before forced KIS reset: %s\n
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
NIOThrowingAsyncSequenceProducer allows only a single AsyncIterator to be created
{%s} read[ED64] of %s @ address 0x%016llX ERROR %d(%s)
Terminate parsing due to Handler error.
hwbp_remove
internal.authenticate_dft.chip->soc == NULL
Algorithms/Windows.swift
[AstrisAsync] Barrier before pause\n
ASTRIS_ERR_NOTFOUND
manta-async-xpc-msg-type
Ignoring device with duplicate identity 
AuthDebug_t::init failed (AuthDebugWithTimer_t)
TargetSel Before Disable: 0x%x
Getting personalized 
R15
Please file a radar (Astris | all) describing the issue,\nand attach a sysdiagnose from this machine.
%d%s
Wrong width, should be either 4 or 8\n
Misc register 3
SecondBootloaderB
Atomics/IntegerConformances.swift
STM32F10x_XLDensity_FLASH
astris_json_logger_to_json_string
SocketChannel { 
Failed to write in DSPSR_EL0 into SPSR_EL%d before changing Exception Level. (reg_val=0x%08llX)
setAddress
Swift/NativeDictionary.swift
Not enough data to parse 
   --> IDR: %08X\n
/tmp/manta-cores
Unexpected routing number 0x
Complex Address: 0x%llX\n
MantaKitComputeNodeProxyRUSBTrafficV2
RF52
symbol.check.loaded.AMAuthInstallSsoEnablePtr == NULL
** If this doesnt work: Please File A Radar With macOS Sysdiagnose Against Component: **\n
~/Library/Application Support/Astris/astris_prefs.plist
    INFO(%u,%d): %s(%04u): %s(): %s
{%s:%s@%d} [%s] \tFailure: only %u of %u individual write transfers were done (%s)\n\n
fn._ocd_exec_instr.l32i.r1.r0
com.apple.Manta.MantaAsyncXPC.MantaAsyncXPCRSD.browse_present
FAULT
Caught a portal that we dont have a status map for: %d
OCLA_IP_REGS
{%s:%s@%d} [%s] FLASH_PRGKEYR write (second) failed: %s\n
{%s@%d} IORegistryEntryGetParentEntry failed, err = 0x%08x
usbLocationNotFound
FTAB missing expected tag '
!!!! Critical Error: Thread %#llx key %lu losing when suspended for info %p - NOT ALLOWED !!!!\n
{%s} exec: DRPS_ENC\n
AXcpu_sstep
STM32F10x_Connectivity_FLASH
fn._ocd_reg_w.ddr
com.apple.Manta.SCDynamicStoreQueue.
virtual int ARM7cpu_t::_resume_hw(bool)
%s/Library/Logs/Astris
Write Data Length Mismatch
Connection aborted: kick required to probe server. Received eof in stdin
CPU2
_get_num_hwbp_hw
_resume_hw
RF36
fn._return_from_debug_interrupt
postconnect
ret.enableCpu
error %s reading DAP MMFR0
s
IOPlatformExpertDevice
s.Peek() == '\\\"'
astris_soc_release
getsockopt(socket:level:optionName:optionValue:optionLen:)
rt13/9/pgood/1v2
!!! Critical Error msr_cache[%d] IS NOT cached !!!
AXmemap_read(_:address:)
cpu-ps-register
hwbp_enable
PORTAL UNAVAILABLE
is.Peek() == 'f'
MantaRetimerController/Retimer+PublicAPI.swift
instance
read.dlr_el0 NOT CACHED
ret.write.editr
R13
RF31
address=0x%8.8X
MantaKitComputeNodeConnectUSBV2
value doesn't fit in UInt16
{%s:%s@%d} [%s] updating PC\n
 is not supported on this platform.
com.apple.Manta.RetimerController
Wat!: 0x%llx
com.apple.MantaKit.mantad.public.remote
AstrisNativeTriage: issuing reset on 
Unable to read GPR 28
Register file 30
 received writeEOF which is unexpected
selfTest(start:done:fail:step:)
param.num_data_bp_regs.invalid.1
=== Ending Gather and Clear ===
start rev is not of expected format; skipping cpu_desc override\n
systemTriageEvent
ret.read.spsr_elx
COMPARE0
MantaDaemonCommon/MantaDaemonCommon.swift
DBG_WRAP_REGS
internal.is_probe_authenticated.debug_auth == NULL
Problematic JSON value:\n%s
Register file 13
op_ISYNC_encode
GenericValue
R9
KalElFlashService/FlashServiceClientUpdateStateMachine.swift
Invalid UDID format
{%s} [EDSCR_RXFULL is_64] exec: encode_mrs(0, MDDTR_EL0, true)\n
runBlock
failed to read consistent debug root register, fabric may be hung
http://jmet-integration-ca.apple.com/fdrtrustobject
result.ide ==NULL
ARMV7
Device did not report a firmware sha256, but should have reported 
\r\n\r\n
SOC
{%s} MEMAP accesses using KIS connection must be at 4-byte aligned address (addr=%#llx)
Loop-end address
_create_cpus
carrier/0/mcu/reset
ftruncate(descriptor:size:)
RF53
Parameter len = %d > 64.
Probe Map comm error %d(%s) %s
General register 9
host_get_probematch
com.apple.private.MantaKit.mantad.public.remote
!!!!!!!!!! Terminating due to %s call !!!!!!!!!!\n
performing direct connect by port number
Atomics/AtomicBool.swift
[!ARM64] exec(DCPSX_BASE_ENC)
EDWVR0+index
MAC16 Data register 1
RF30
BMC UDID not found.
ASTRIS_ERR_USB_EXPIRED
{%s:%s@%d} [%s] error flags set by erase (0x%08x): %s\n
AstrisSWD
bridges
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
fn.remove_epcn_epsn
PortBridgeSWD
{%s} empty response string provided
ARM64cpu_t
astris_json_logger_init
Missing a name for object member.
codepoint <= 0x10FFFF
config_write_protection
  Nested path: parent='%s', child='%s'
/Library/Caches/com.apple.xbs/76DBD45B-9C35-4E76-99C5-12B5C8C54BA5/TemporaryDirectory.w58zkN/Sources/Manta_restoreos/Vendor/swift-nio/Sources/NIOCore/EventLoop.swift
channel
{%s} read[CTI32] of %s @ address 0x%016llX = 0x%08X
RF24
Invalid Xtensa CPU OCD.DEVID = 0x%8.8X. Should be 0x%8.8X (LE) or 0x%8.8X (BE)
```
