# `/usr/libexec/DumpPanic`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 356,320 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 43 (Size: 5872)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (25)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics (compatibility version 0.0.0, current version 1.0.0)`
- `/usr/lib/libAppleArchive.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/AppleNVMe.framework/AppleNVMe (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/DiagnosticsReporterServices.framework/DiagnosticsReporterServices (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0, weak)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0, weak)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeNamespaceDevice.allow</key>
	<true/>
	<key>com.apple.TapToRadarKit.service-access</key>
	<true/>
	<key>com.apple.frontboard.launchapplications</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.osanalytics.otatasking-service-access</key>
	<true/>
	<key>com.apple.private.ApplePMGRUserClient.access</key>
	<true/>
	<key>com.apple.private.ApplePMGRUserClient.get-bpr</key>
	<true/>
	<key>com.apple.private.AppleSoCMiscUserClient.access</key>
	<true/>
	<key>com.apple.private.AppleSoCMiscUserClient.get-bpr</key>
	<true/>
	<key>com.apple.private.MobileGestalt.AllowedProtectedKeys</key>
	<array>
		<string>InverseDeviceID</string>
	</array>
	<key>com.apple.private.applecredentialmanager.allow</key>
	<true/>
	<key>com.apple.private.coredump-encryption-key</key>
	<true/>
	<key>com.apple.private.diagnostic-intelligence</key>
	<true/>
	<key>com.apple.private.intelligenceplatform.client-identifier</key>
	<string>com.apple.DumpPanic</string>
	<key>com.apple.private.intelligenceplatform.use-cases</key>
	<dict>
		<key>PanicPatternMatching</key>
		<dict>
			<key>Streams</key>
			<dict>
				<key>Diagnostics.Panic</key>
				<dict>
					<key>mode</key>
					<string>read-write</string>
				</dict>
			</dict>
		</dict>
	</dict>
	<key>com.apple.private.iokit.system-nvram-allow</key>
	<true/>
	<key>com.apple.private.roots-installed-read-only</key>
	<true/>
	<key>com.apple.private.security.disk-device-access</key>
	<true/>
	<key>com.apple.private.security.file-unencrypt-access</key>
	<true/>
	<key>com.apple.private.security.storage.DumpPanic</key>
	<true/>
	<key>com.apple.private.security.storage.spindump</key>
	<true/>
	<key>com.apple.rootless.volume.VM</key>
	<true/>
	<key>com.apple.security.exception.mach-lookup.global-name</key>
	<array>
		<string>com.apple.biome.access.user</string>
	</array>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleSoCMiscUserClient</string>
		<string>ApplePMGRUserClient</string>
		<string>AppleNVMeNamespaceUC</string>
	</array>
	<key>com.apple.security.system-groups</key>
	<array>
		<string>systemgroup.com.apple.osanalytics</string>
	</array>
	<key>com.apple.springboard.CFUserNotification</key>
	<true/>
	<key>com.apple.springboard.remote-alert</key>
	<true/>
</dict>
</plist>
```

## Objective-C (14 classes, 2 protocols)

Classes: `ArgParser`, `CoreFileHandler`, `CoreFileHandlerV1`, `CoreFileHandlerV2`, `CoresPruner`, `DumpPanicArgParser`, `KeyStore`, `LockedReadOnlyKeyStore`, `PanicProcessingAdapter`, `PanicUtilArgParser`, `ReadOnlyKeyStore`, `SOCDReportInfo`, `UserCoreFileHandler`, `_TtC9DumpPanic27PanicPatternMatchingWrapper`

Protocols: `NSObject`, `PanicProcessingDelegate`

## Strings (1,344)

```
embedded-panic-header
coreDumpDuration
secure
OTA UUID: %.*s\n
  -i, --iboot-panic-header FILE\n              use iboot panic data binary file (struct iboot_panic_header)\n\n
remote_pmic
864502
ar:chf
  -o, --outputpath DIRECTORY\n\t\t              output directory for logs\n\n
PanicReason
/var/cores/launchd.debug.core
v12@?0i8
Your device has rebooted after an unexpected reset
1176064
DeviceClassNumber
device panic
1028387
iboot_panic_header.bin
remove-socd-data
  -o, --outputpath DIRECTORY\n              output directory for logs\n\n
iBoot indicates storage dump CRC mismatch
failed to clear PMU boot properties
IOService
spmi
 panic save x86 panic diags interrupted
wb
Error getting a reference to IODeviceTree:/options
development-cert
iboot
crash
upc_reset
 (AppleLPM crashed)
 (AIA crashed)
kern.kdp_corefile
hw.memsize
EmbeddedDeviceTypePanicLog
 x86 panic diags
 iBoot panic save entry
 after iBoot panic save power init
!(cur_metadata->lm_flags & IBOOT_PANICLOG_BAD_MAGIC_FLAG)
115
AppleSMC
OnlyUseNvramKeyStore
decompress_stackshot
 after iBoot panic save memory init
\n
IODeviceTree:/options
core
com.apple.DiagnosticExtensions.Panic
IODeviceTree:/chosen
  -b, --bootfault FILE\n              use boot fault JSON file\n\n
Unexpected uncategorized reset occurred
/private/var/mobile/Library/Logs/CrashReporter/Panics
-[CoreFileHandler getCorefileZeroRanges]
hw.osenvironment
BAD MAGIC! (flag set in iBoot panic header), no panic log available
iBoot indicates CRC mismatch
resetType
plane
boot-args
kcd_c_totalout
AppleNVMeReadPanicLogData failed to read data from panic log namespace.
 after iBoot LLB end
 after iBoot end
 (AWL panic)
kern.bootsessionuuid
panicRegionTempFile != NULL
version
corrupt data
Your device has recovered from a panic
Unable to find usable panic log after traversing %d iBoot metadata logs
BSD Name
it rebooted after an unexpected reset
resetCount
File a radar now?
Failed to base64 encode storage dump of length %llu
 while x86 panic diagnostics being saved
socd-iboot async abort
-[CoreFileHandler getCoreDumpNameWithIndex:]
it rebooted after a force reset
dumppanic
chosen
it recovered from a panic
PanicMedicEntryBootTarget
1.2.12
cpu_therm
sstate
/staged
OSAnalytics
rtkit-crashlog
unknown
coreSize
AppleNVMeReadPanicLogData suffered from an unknown error.
DumpPanic.PanicPatternMatchingWrapper
oc
 (iBoot panic)
0 5
socd-data
 after panic save CE trigger
 iBoot panic save memory init
UTC
IOPMUBootErrorClear
rst
corecrypto process rng
-[CoreFileHandler getCorefileLogInfo:::]
key_format
Cancel
Failed to create EmbeddedPanicDataDecoder instance
com.apple.DumpPanic.corefileSummary
-[CoreFileHandler getCoreDumpInfoWithIndex::::]
Shared.m
clock_gettime()
pmu crash
gzipOutputStreamWrite
NumCores
IOMedia
-corefile_paths
path exists but is not directory : %@
core.%llu.gz
launchd
unlock_register
/var/tmp/dumppanic
 during sleep/wake transition
failed to open directory at path : %@ with error : %s
yyyy-MM-dd-HHmmss
[Warning: The attachments may contain privacy-sensitive sensor data.]
PanicMedicEntryTimestamp
ResetCounter
/var/cores/launchd.developm.core
iBoot panic header magic invalid: found 0x%x, expected 0x%x
ARMPanicSupport.m
ntc_shdn
device unexpected reset
 (iBoot sync abort)
fstat of %@ failed with error: %s
ccrng_process_atfork_prepare
embedded_panic_header_corefile_fallback.bin
aeaDecryptStreamRead
gpu_therm
sochot
lz4DecodeStreamClose
%@%skernel.core.log
No panic log found
IONVRAM-FORCESYNCNOW-PROPERTY
panicmedic-telemetry
 panic diags complete
\n%@
kern.bootargs
usage: DumpPanic [OPTIONS] \n
Source: %@
clean restart
Q
kcd_c_totalin
UnexpecteResetReason
PanicMedicEntryBootStage
 (AWL AP Panic)
%s/staged
ccrng_process_atfork_parent
bootfault
 iBoot Stage LLB end
ap watchdog
sectionInputStreamRead
type
fchmod of path : %@ failed with error : %s
.core
%s/%@.
ExclaveCapability
UNKNOWN
hs:i:p:r:b:e:o:
EnablePanicPatternMatching
IOPMUBootErrorFailCount
 iBoot start
i
 while panic diagnostics being saved
AppleDialogSPMIPMU
stress-rack
%02llX
0
Unexpected SoC (system) watchdog reset occurred
unlock_sema != nil
AppleNVMePanicLogGetSize suffered from an internal error.
universalBootFaults
btn_rst
 after AP Watchdog reboot
%s must be implemented
+3Uf0Pm5F8Xy7Onyvko0vA
com.apple.dumppanic
IOPMUBootErrorAppName
invalid iBoot log metadata: (type %d) points outside of panic buffer : offset: %llu, size: %llu, bytes_read: %llu
Unexpected force reset occurred
 after iBoot start
forceReset
EnablePanicMedicTelemetryInRecoveryEnv
SOCD report detected: failed to read socd header
q24@?0@8@16
%@/%@
\n\n%@
skipTTR
(?:^|[ \t\r\n])%@=(0x[a-fA-F0-9]+|-?[0-9]+)(?:[ \t\r\n]|$)
IODeviceTree:/defaults
-[ArgParser usage]
+[ArgParser withArgs:count:]
At least one input file required
AppleNVMePanicLogGetSize failed to query panic log namespace size.
IOPMUBootFaultInfo
 iBoot end
kern.coredump_encryption_key
OK
dbg_rst
 (Unknown)
AppleNVMeReadPanicLogData could not find panic log namespace service in registry.
chg_pok_fall
vdd_hi_and_chg_pok
Force Resets
iBoot panic header indicates invalid number of logs available (%d)
 iBoot panic save reboot
%s must be overridden in a subclass/category
  -f, --force\n\t\t             force DumpPanic to run\n
iBoot header contained bad magic (possible legacy panic data)
iBoot header contains invalid number of logs
Failed to base64 encode SOCD container of length %u
,
supported-legacy-panic-flow
sgpio
  -h, --help\n\t\t              show this help\n\n
-interrupted_coredump_paniclog
UserSpaceCoreCompressed
%@/%llu.key
alloc ws
 panic DRAM flush
AppleNVMePanicLogGetSize received an invalid argument.
Failed to decode embedded panic data
 iBoot panic save power init
btn_shdn
YES
/var/run/com.apple.DumpPanic.finishedPMUFaultHandling
force_off
panic_region
com.apple.DumpPanic.corefileSize
com.apple.osanalytics.preoslog
help
 while panic DRAM flush in progress
 panic save CE trigger
 after panic save chip reset initiated
init()
  -e, --plane FILE\n              use plane panic test input JSON file with multiple nodes\n\n
 after iBoot panic save storage init
Unexpected Resets
socd-smc panic
AppleNVMePanicLogGetSize could not find panic log namespace service in registry.
panic
InDiagnosticsMode
ips
forceSeedFeedbackPrompting
pthread_atfork
invalid reset type
aia
%s
/var/db/com.apple.DumpPanic.panicLogPathBreadcrumb
Error creating directory at : %@ : %s
magic
/var/run/com.apple.DumpPanic.finishedThisBoot
AppleNVMeReadPanicLogData failed to query panic log namespace size.
Reset count
1111324
ccrng failed assert cbc_info->block_size = %lu\n
 after panic save chip reset initiated and x86 panic diagnostics were interrupted
ccrng_process_init
ota-uuid
socd.bin
IOPropertyMatch
;
com.apple.DumpPanic.KernelCoreDump
 (AWL watchdog expired)
-[CoreFileHandler getNumCoreDumps]
check_log_metadata
cp.core.gz
%@%s%s.core.gz
ccrng failed assert key_nbytes = %lu\n
 after iBoot kernel handoff
IOPMUPrimary
panic_pattern_matching
kcd_c_type
IOPMUBootSOCD
Encryption key format
%s/%@
 iBoot panic save storage init
SOCD report detected:
socd-multi
/private/var/mobile/Library/Logs/CrashReporter/Panics/staged/tempUserSpaceCore.XXX
restoreos
 during iBoot panic save reboot
BAD MAGIC! (flag set in iBoot panic header), no SOCD container available
 after panic diagnostics were completed
IOPropertyExistsMatch
/private/var/tmp/panicregion.XXX
 (SMC panic)
PanicMedicEntryTimestampDiff
arm-io
 sleep/wake transition
BATS_TESTPLAN_ID
v16@?0@\"NSError\"8
 (AP watchdog expired)
AppleNVMeReadPanicLogData received an invalid argument.
en_US_POSIX
/private/var/vm/kernelcore
Triage
Panic Triage
debug
check_log_metadata called with invalid log_type
 (iBoot async abort)
  -s, --socd FILE\n              use socd binary file\n\n
 
iBoot panic-save unexpected reset, boot faults: %@
-PanicMedic_info
staged
iOS
socd-ap watchdog
/private/var/db/DumpPanic/Keys
 after panic called
kern.preoslog
No valid SOCD nand container present
864503
-[CoreFileHandler getPanicRegion]
plane_node
bootAppHash
-[CoreFileHandler getCoreDumpEncryptionKey:]
 panic save chip reset
 after iBoot Autoboot
esr: 
com.apple.coreOS.restartReason
corefile with name %s
%x
IOPMUBootErrorStage
IOPMUBootSOCDClear
corefilestreams.m
kernel core log
/private/var/mobile/Library/Logs/CrashReporter/Panics/staged
getentropy
free ws
Unexpected arguments
w
AppleNVMeReadPanicLogData failed to unmap data from panic log namespace.
platformSOCDBuffer
IOParentMatch
socd-data-in-progress
invalid iBoot log metadata: (type %d) size invalid, found %llu, expected at least %lu
bootStage
aeaDecryptStreamClose
/private/var/db/DumpPanic/Coredumps
embedded panic data not available
r
device force reset
unique-chip-id
default
ArgParser.m
usage: PanicUtil [OPTIONS] \n
AppleNVMePanicLogGetSize suffered from an unknown error.
interrupted coredump panic
 panic diags
 after iBoot LLB Autoboot
public_key_hash
 after iBoot LLB start
chip-id
bootfault.json
  -r, --restoreos DIRECTORY\n\t\t               special-case mode for restore environment\n\n
 AP Watchdog reboot
force
/var/root/Library/Application Support/DumpPanic/
.gz
Your device has rebooted after a force reset
v16@?0@\"NSFileHandle\"8
 AP Watchdog expired
uv
/var/mobile/Library/Logs/CrashReporter/ForceResetTailspins
609970
ccdrbg_nistctr: invalid block size
outputpath
  -r, --rtkit-crashlog FILE\n              use raw RTKit crashlog binary file\n\n
Retired
ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n
com.apple.coreOS.resetTelemetry
backpow
timeout
iboot-panic-header
com.apple.PanicUtil
AppleNVMeReadPanicLogData could not connect to panic log namespace service.
chip-revision
 after iBoot panic save entry
embedded_panic_header.bin
%@\n%@
rawBootFaults
@\"NSDictionary\"8@?0
macefi
AppleNVMePanicLogGetSize could not connect to panic log namespace service.
DRAMSizeMB
bootFailCount
  -p, --embedded-panic-header FILE\n              use xnu panic data binary file (struct embedded_panic_header)\n\n
PanicDev
ov
data
coproc.core.gz
panic region
-[CoreFileHandler getCorefileLogEncryptionKey]
Unexpected SPMI fault reset occurred
panicprocessing
ResearchFuse
ot
/private/var/db/DumpPanic
nodeName
socd-iboot sync abort
 iBoot Stage LLB start
por
CorefileDataSize
%@.%s%@.core.gz
full_key
Failed to generate random
iBoot header contained bad magic
/var/root/Library/Application Support/DumpPanic/LegacyDataProcessed
wdog
lz4DecodeStreamRead
com.apple.mobile.keybagd.lock_status
kern.hv_vmm_present
buffer
com.apple.DumpPanic
ccrng_process_atfork_child
Invalid argument
AppleNVMeReadPanicLogData suffered from an internal error.
No usable panic logs available from iBoot headers
AppleDisplay
socd
otherResetCount
v8@?0
socd-iboot panic
  -h, --help\n              show this help\n\n
Incident Identifier: %@\nCrashReporter Key:   %@\nDate: %@\nReset count: %@\nBoot failure count: %@\nBoot faults: %@\nBoot stage: 0x%x\nBoot app: %@\nsocId: %x\nsocRevision: %x
 panic start
.synced
Whole
sys watchdog
panicCount
handlekernelcore.m
ccdrbg_nistctr: key length too long
IOPMUBootErrorPanicCount
 after AP Watchdog expired
coreName
DumpPanic
DRAM panic log missing; corefile fallback log in use
fchown of path : %@ failed with error : %s
LockedReadOnlyKeyStore
ArgParser
DumpPanicArgParser
NSObject
CoreFileHandler
CoreFileHandlerV1
CoresPruner
CoreFileHandlerV2
KeyStore
ReadOnlyKeyStore
PanicUtilArgParser
PanicProcessingAdapter
PanicProcessingDelegate
SOCDReportInfo
UserCoreFileHandler
_TtC9DumpPanic27PanicPatternMatchingWrapper
v48@0:8Q16^Q24^Q32^I40
C
@40@0:8@16d24@32
@\"NSMutableDictionary\"40@0:8@\"NSURL\"16d24@\"NSString\"32
B40@0:8^Q16^Q24^I32
v16@0:8
@16@0:8
v20@0:8I16
B24@0:8@\"Protocol\"16
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}
v20@0:8B16
B24@0:8@16
#16@0:8
@60@0:8*16B24@28Q36^v44Q52
r*24@0:8Q16
v24@0:8^?16
@\"NSNumber\"
v24@0:8@16
@36@0:8@16I24@28
v48@0:8@16@24@32@40
@\"NSMutableDictionary\"
@40@0:8:16@24@32
@32@0:8@16@24
i
^{mach_core_fileheader_v2=QIQQSQQQ[0{mach_core_details_v2=QQQ[16c]}]}
I
@\"NSArray\"16@0:8
B28@0:8i16@20
B56@0:8@16^@24^i32^@40^@48
@44@0:8*16B24@28@36
I16@0:8
@24@0:8:16
@32@0:8r*16r*24
B16@0:8
@\"NSURL\"
@32@0:8:16@24
^{_NSZone=}16@0:8
B28@0:8I16^@20
@24@0:8Q16
Q
@36@0:8*16B24@28
@\"NSMutableArray\"
B24@0:8@\"NSString\"16
@\"NSObject<OS_os_log>\"
?
@\"NSString\"
Vv16@0:8
@28@0:8r*16I24
@\"NSString\"28@0:8r*16I24
@28@0:8i16@20
C16@0:8
@32@0:8Q16Q24
B40@0:8Q16@24^@32
@24@0:8d16
B24@0:8#16
v20@0:8C16
@\"NSData\"
Q16@0:8
B60@0:8Q16Q24@32@40@48I56
@\"ReadOnlyKeyStore\"
^{ccec_cp=QQ^{cczp_funcs}[1Q]}20@0:8i16
@28@0:8^*16i24
B
v24@0:8@\"NSString\"16
@\"NSNumber\"32@0:8@\"NSString\"16@\"NSString\"24
@\"NSError\"
^v
{mach_core_fileheader=\"signature\"Q\"log_offset\"Q\"log_length\"Q\"num_files\"Q\"files\"[16{mach_core_details=\"gzip_offset\"Q\"gzip_length\"Q\"core_name\"[16c]}]}
@24@0:8@16
B24@0:8:16
@\"NSString\"16@0:8
@48@0:8r*16I24d28B36@?40
TB,V_force_run
bootfault_json
getAuxiliaryNVRAMData
numberWithInt:
setForegroundAppHash:
timeZoneWithName:
URLByAppendingPathComponent:
bootIsRecoveryEnvironment
setFilesToScreen:
stringWithFormat:
_corefileHeader
useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:
fileURLWithPathComponents:
initWithArgs:count:
initWithCString:encoding:
objectForKey:
problemType
testPlanID
_data
_filesToScreen
_iph_binary
getSterilizedStringFromData:size:
is_userspace
notes
removeItemAtPath:error:
retainCount
TB,V_restoreos
stringByAppendingPathComponent:
_restoreos
dataUsingEncoding:allowLossyConversion:
initWithName:version:identifier:
initWithUUIDBytes:
isDevFused
matchedActions
JSONObjectWithData:options:error:
bootsessionuuid
setPatternType:
compare:
coreFileWithCoreFilePath::::
dataWithBytesNoCopy:length:freeWhenDone:
defaultManager
exceptionWithName:reason:userInfo:
TB,V_is_userspace
setPatternUUID:
withArgs:count:
T@\"NSMutableDictionary\",&,V_filesToScreen
getNumCoreDumps
countByEnumeratingWithState:objects:count:
eph_binary
initWithUnsignedInt:
hash
initWithArray:
mountVolumeWithRole:mountPath:
numberWithLongLong:
numberWithUnsignedInt:
output_dir
patternType
setClassification:
anyObject
T@\"NSString\",N,C
T@\"NSURL\",&,V_bootfault_json
getCoreDumpNameWithIndex:
isEqualToString:
moveItemAtURL:toURL:error:
panicFlags
removeObjectForKey:
getBytes:range:
stringFromDate:
utilizationInfo
_type
getPanicRegion
isEqual:
performSelector:withObject:withObject:
setPanicProcessingInfo:
product
debugDescription
getHeaderVersion
initWithCoreFilePath::
removeAllObjects
saveCoreDumpWithIndex:named:toFileName:
setAutoDiagnostics:
setDateFormat:
addNotes:
hasInputFiles
initWithData:encoding:
replaceObjectAtIndex:withObject:
setFilesToPullIn:
setForce_run:
setLog_path:
setUUIDIBoot1:AndIBoot2:
useExtPaniclog:
_eph_binary
addObject:
arrayWithCapacity:
fileSize
getCorefileZeroRanges
initWithFileDescriptor:closeOnDealloc:
setRawPanicData:
setRtkit_crashlog_binary:
setSOCId:AndRev:
setType:
setUtilizationInfo:
sortUsingComparator:
stringByAppendingFormat:
stringValue
useSocdContainer:
setCorefileURL:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
removeObjectAtIndex:
setIs_userspace:
setUUIDSPTM:
sharedInstance
socRev
stringWithString:
isResearchFused
appendString:
dataWithBytesNoCopy:length:
getCorefileLogInfo:::
incidentID
initWithCorefileURL:CoresToKeep:userspaceCorefileName:
numberWithDouble:
unsignedIntValue
T@\"NSNumber\",N,&,VpatternType
deviceModelType
_coresToKeep
_socd_binaries
allValues
buildVersion
getValueFromDTForNode:key:
isTagCheckFault:
_agentId
characterAtIndex:
getCoreDumpContentsWithOffset:AndLength:
isTestAutomationDevice
numberWithUnsignedLong:
setPanicProcessingFlags:
setplatformECID:
substringFromIndex:
autorelease
class
isIntentionalPanic
lastPathComponent
setSocDataVersion:
substringToIndex:
writeToFile:options:error:
initWithFormat:
generatePanicSaveOptionsForDirectory:time:prefix:
init:
numberWithUnsignedChar:
substringWithRange:
timeIntervalSinceNow
usage
writeToFile:atomically:
panicMedicTelemetry
saveKernelCoreToDisk:::::
setObject:forKey:
_error
dictionaryWithDictionary:
initWithCoreFilePath::::::
isKindOfClass:
plainPanicData
setComponent:
timeIntervalSince1970
unsignedLongLongValue
UUIDString
RotateKeys:
TC,N,V_type
_input_corefile_path
currentDirectoryPath
errorWithDomain:code:userInfo:
initWithKeyStorePath::
zone
T#,R
lowercaseString
_rtkit_crashlog_binary
numberWithUnsignedLongLong:
setSocd_binaries:
dealloc
_input_corefile_name
count
createDraft:forProcessNamed:withDisplayReason:error:
scanFilesInURL:pullinFiles:screenFiles:andTimeStamps:
timeUsecs
.cxx_destruct
addObjectsFromArray:
fileType
rangeOfString:
saveUserSpaceCoreToDisk:
setAgentId:
componentsJoinedByString:
filesToPullIn
privateKeyChecking
respondsToSelector:
setProduct:
stringWithCString:encoding:
T@\"NSURL\",&,V_iph_binary
T@\"NSString\",&,V_userspaceCorefileName
_scratchBuf
fileExistsAtPath:
initWithPanicString:
panicString
rangeOfString:options:
self
TI,V_coresToKeep
_is_userspace
_plane_json
getCoreDumpInfoWithIndex::::
setEPHVersion:
setPanic_string:
absoluteString
boolForKey:
firstObject
performSelector:withObject:
setBootfault_json:
setDiagnosticExtensionIDs:
setMatchedActions:
setUUIDKernel:
cleanup
containsString:
_corefilePath
force_run
patternTypeString
plane_json
setBootStage:
createForSubmission:metadata:options:error:writing:
patternUUID
setError:
setKeywords:
setUUIDTXM:
dataWithLength:
_filesToPullIn
fileCreationDate
firstMatchInString:options:range:
isMemberOfClass:
performSelector:
setPlane_json:
stringByDeletingLastPathComponent
T@\"NSString\",R,C
_isDefaultKeyStorePath
conformsToProtocol:
fileExistsAtPath:isDirectory:
rootsInstalled
setUserspaceCorefileName:
TC,N,V_agentId
serviceSettings
rtkit_crashlog_binary
setIph_binary:
setKernelVersion:
setPanicInitiator:
setPlaneMetadata:
setTitle:
fileSystemRepresentation
filepath
help
propertyListWithData:options:format:error:
setActions:
setIsUserInitiated:
setOutput_dir:
setTimeZone:
T@\"NSMutableDictionary\",&,V_filesToPullIn
T@\"NSURL\",&,V_output_dir
setCoresToKeep:
initWithPanicString:otherString:buildVersion:panicFlags:panicType:incidentID:rootsInstalled:
readKeyFile:::::
setUUIDKernelCache:
stringByReplacingCharactersInRange:withString:
stringWithUTF8String:
initWithObjectsAndKeys:
corefileURL
dataWithJSONObject:options:error:
getStackshotData
hasSuffix:
restoreos
timeSecs
_force_run
dataWithContentsOfURL:options:error:
type
_userspaceCorefileName
dateWithTimeIntervalSinceReferenceDate:
filesToScreen
integerValue
launchAppWith:options:completion:
localizedDescription
setProblemDescription:
T@\"NSURL\",&,V_eph_binary
_input_core
length
mutableCopy
prune
setRestoreos:
shared
unlock
isZeroes:
userspaceCorefileName
UTF8String
_keyStorePath
panic_string
sharedAdapter
coresToKeep
saveWithOptions:
stringByReplacingOccurrencesOfString:withString:
dateFromString:
_scratchBufSize
T@\"NSData\",&,N,V_data
array
arrayWithObjects:
authorizationStatus
deleteBootArgDumppanic
dictionary
TQ,R
donateToBiome
removeItemAtURL:error:
setFiles_to_attach:
setPanicTimeInSecs:andUsecs:
files_to_attach
setAttachments:
dictionaryWithCapacity:
dictionaryWithObjects:forKeys:count:
initWithBase64EncodedString:options:
kernelVersion
setAppleCareDetails:
setObject:forKeyedSubscript:
setPanicString:
_keystore
_output_dir
createWithPanicBuffer:panicLength:
date
description
getCoreDumpEncryptionKey:
otherString
_corefileSize
fileURLWithPath:
initWithLocaleIdentifier:
iph_binary
log_path
setData:
setLocale:
socd_binaries
T@\"NSURL\",&,V_corefileURL
T@\"NSURL\",&,V_plane_json
agentId
dataWithPropertyList:format:options:error:
panicInitiator
setOriginalPanicReportPath:
standardUserDefaults
base64EncodedStringWithOptions:
_help
enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:
initWithCoreFilePath:::
writeData:error:
initWithLength:
_corefile_fd
appendBytes:length:
initWithBytes:length:encoding:
_singleFileMode
isProxy
dataWithContentsOfFile:options:error:
init
rangeAtIndex:
regularExpressionWithPattern:options:error:
uniqueChipID
copy
data
extPaniclog
hasMatchingPrivateKey::
objectAtIndexedSubscript:
setHelp:
useSocdNandContainer:
setBoardId:AndRevId:
socId
T@\"NSMutableArray\",&,V_socd_binaries
containsObject:
release
getCorefileLogEncryptionKey
getMatchingPrivateKey::
mutableBytes
_encryptionPublicKey
_headerData
_log_handle
dateWithTimeIntervalSince1970:
getEccFormat:
objectAtIndex:
platformECID
setEph_binary:
_bootfault_json
bytes
componentsSeparatedByString:
error
removeObject:
timeIntervalSinceDate:
unsignedCharValue
T@\"NSError\",&,V_error
useCrashlogContainers:
writeData:
_corefileURL
_zero_on_close
crashReporterKey
decode
path
setAWLBuildVersion:
subdataWithRange:
intValue
panicProcessingInfo
saveCoreDumpAtOffset:withLength:named:encryptedWithPublicKey:toFileName:flags:
setDelegate:
stringByAppendingString:
T@\"NSString\",?,R,C
T@\"NSURL\",&,V_rtkit_crashlog_binary
dataWithBytes:length:
objectForKeyedSubscript:
retain
useStoragePanicData:
T@\"NSArray\",N,C
logfile
TB,V_help
arrayWithObjects:count:
superclass
Waiting for DR to launch.
Failed to write initial safe panic log
Use '-f/--force' to run DumpPanic manually
Failed to open report %d: %d
Failed to call the new public key callback with an existing key
Compressed kcdata buffer doesn't contain a stackshot, iter_type is %d
Failed to encode RTKit crashlog data to base64
Pattern matching failed: %@
failed to clear PMU boot-properties with error: %d
unable to read out auxiliary PMU properties
Failed to get the exclusive section for agent %d: %d
Warning: Failed to set AWL platform data from local platform_socd_buff
Read of %lu bytes from fileoffset 0 only read %lu bytes
No %s core found at %s
Failed to allocate compression buffer for %s core
Failed to write to the new key file. Error: %@
No socd data found in local device
Failed to create a SOCD handle: %d
Reading public encryption key from corefile
Failed to stat file: %s (%{errno}d)
attempting to discard safe log at %@
Failed to initialize the z_stream for this panic stackshot: rc = %d
Found donate action type %u with UUID: %s
wrote ResetCounter log to disk: %@
Failed to get SOCD container size if report record ID: %d, error: %d
unable to parse date from filename %@, skipping
failed to find panic region in corefile with %llu files
The kernel core is not encrypted
Misformatted key file. Public key hash not found
Invalid parameters for set_awl_platform_data_in_report
Faled to write panic log breadcrumb: %s
no stackshot found
failed to write boot fault data to file: %@
invalid core file signature: %#llx (expected :%#llx or %#llx)
Failed to open gzip output stream.
Failed to mark %s as purgeable. Error: %s
Failed to parse the Base64-encoded hash
NVRAM is not supported on this system
Failed to allocate memory for preoslog buffer
iBoot panic header indicates %d panic logs available
unable to read out primary PMU properties
Failed to allocate AEA decryption stream data.
copying %llu bytes
%s core is empty
Failed to read content from %s core
Failed to parse the Base64-encoded key
Creating a new key file
Failed to write standalone socd panic report
Breadcrumb file contains invalid data
Removing file %@
Received confirmation that a Tap-to-Radar draft has been started
Lower buffer is at va %p, size %zu bytes
Failed to gather the file attributes for '%@'.
Empty RTKit crashlog data
PMU fault data already processed this boot
Failed to get kern.bootsessionuuid
Found a matching private key
Failed to notify kernel of new public encryption key. Error: %{errno}d
Device tree indicates that device never supported legacy panic path
Failed to open lz4 decode stream.
Failed to mark the coredump output file as purgeable.
Found %s core at %s
No donate type specified in matched actions
read out PMU fault data: resetCount: %d, bootFailCount: %d, boot stage: 0x%x, boot app hash: %d, boot faults: %@, universal boot faults: %@:
Failed to write %s
Failed to close AEA decrypt stream source.
opened corefile, header indicates %llu files present
Failed to create a regex matching expression: %@
Failed to write panic log with storage data
Failed to get reports count in SOCD container size: %d
Failed to allocate AEA decryption stream.
Failed to find a matching private key for the public key.
Failed to open file output stream.
Failed to enumerate the directory at '%@'
No boot fault data found in local device
Failed to get the number of agents: %d
NULL input for scanFilesInURL, skipping scanning in URL %@
getxattr %s returned error : %s
TapToRadarServiceSettings does not exist and thus we cannot start a radar
unable to write %@ back to NVRAM, it is not marked as reported!
Flush preoslog
invalid kcdata iter type in %s(): %d
Failed to unlink panic data -- DKIOCUNMAP failed with %d : %s
%llu bytes were read from the file or device, but at least %lu are required to fit the iBoot panic header.
Found matched panic pattern
Failed to create SOCD handle: %d
lseek() to file offset 0x%llx returned -1 (%{errno}d)
error zeroing corefile, attempted to write %zu bytes, wrote %zu bytes
Attempting to extract kernel core if it exists...
Machine configured to NOT reboot on a panic
Error getting a reference to IODeviceTree:/defaults
Skipping writing ResetCounter log as no unexpected resets detected
Failed to load the SOCD container: %d
Skipping non-file type '%@'
The input public key did not pass basic validation checks
OSADiagnosticsReporter does not exist and thus we cannot launch DR
ERROR: '%s' when opening '%@'
failed to write socd data to file: %@
Failed to create directory: %@ -> %@
Failed to query the size of kdp_corefile. Error: %d
Failed to query kdp_corefile. Error: %d
Successfully read %hu bytes for the public encryption key
failed to query sysct hw.memsize: %s
loaded %@ from NVRAM: %@
Skip writing ResetCounter log to disk for intentional panic
Waiting for SOCD data collection to complete
Failed to create matching dict
Failed to load SOCD container: %d
open_dprotected_np(%@, O_RDONLY): -1 (%{errno}d)
Failed to read the file contents for panic region file. Error: %@
Corefile corrupted. Public key (offset %llu, length %hu) extends past end of file (length %zu).
Mismatched key hash lengths
read out auxiliary PMU fault data: boot fault info: %@
Failed to remove directory: %@ -> %@
Failed to process the coredump through the byte streams. Error %lld
Corefile corrupted. Header (size %zu) and %llu file headers (each of size %zu) extend past end of file (length %zu).
Mismatched key hashes. Skipping
DR launched.
%.*s
Unexpected donate action count %ld
Failed to query disk block size -- DKIOCGETBLOCKSIZE failed with %d : %s
Device supported legacy panic path, file marker found
socd data found in local device
Skip handling kernel corefile which suggests 0 files present
Failed to enumerate the contents of the sandbox directory: %@
Failed to launch DR with error: %@.
Compressed stackshot metadata: type: %lld totalout: %lld totalin %lld
Device supported legacy panic path, no existing marker file found
Failed to process RTKit crashlog data
Failed to rename compressed %s from %s to %s
Failed to get response for tap to radar notification with error: %d
Discarding 'safe' log %@
Write a standalone socd panic report
open_dprotected_np(%s, O_RDONLY): -1 (%{errno}d)
Created legacy panic data marker file: %s
detected interesting reset, promoting to panic
gzopen(%s, wb) error: %s
Failed to read from kernelcore file.
Found %lu sets of cores under staged folder
failed to setup corefile stage directory due to error: %s
Launching DiagnosticsReporter with files to attach: %@, log_path: %@, and panic string: %@
Failed to write panic file
Failed to get SOCD v2 container agent ID: %d, num_agents: %zu
Moved staged '%{public}@ to panics folder
Failed to open %s to mark as purgeable. Error: %s
Failed to call the new public key callback
Unable to register for device lock state notification.
Magic for preoslog buffer doesn't match, expected %08X, given %08X
kcdata iterator was invalid while collecting compression metadata
Matched registered panic device: %s
The boot fault doesn't meet the promotion criterias, reportSingleUnexpectedReset: %d, reportiBootHang : %d, bootFaultsMatchCriteria: %d, ibootPanicSavePanic: %d, bailing out panic promotion
Failed to safely open file : %s
Failed to allocate section input stream data.
Failed to allocate gzip output stream data.
open_dprotected_np(%@, O_RDWR): -1 (%{errno}d)
failed to setup corefile output directory with error: %@
%s core already compressed, skipping collection
Failed to stat %s with error %s
no core file data found
Machine configured for intentional panic
failed to creat() DumpPanicDone cookie at path %s with error %s
Error getting a reference to IODeviceTree:/options
%s of unexpected type %lu
SOCD data collection is complete. Checking for data
invalid core file signature: %#llx (expected :%#llx)
Found corefile with signature %#llx
Reusing an existing key file
found hw.osenvironment: %s
preoslog buffer size is 0
Wrote log with storage data, discarding initial safe log
Failed to get matching socd ioservices: 0x%x
loaded socd data from: %@
Failed to get encoded report from SOCD buffer
Failed to parse breadcrumb with error : %s
Failed to read from lz4 decode stream source.
Misformatted key file. Key format not found
skipping launching TTR...
Found SOCD container with length 0x%llx
unable to serialize json: %@
Removing prior corefiles, found %lu sets (policy limit %u)
Corefile corrupted. File %zu's name is not a valid string.
failed to setup corefile stage directory with error: %s
Failed to open directory: %s (%{errno}d)
Invalid parameters for RTKit crashlog processing
Pattern matching failed: %s
Found %@: offset: 0x%llx, length: 0x%llx, flags: 0x%x. Writing to disk
AppleNVMeReadPanicLogData successfully extracted %llu bytes of data.
Warning: Failed to set AWL platform data from platformSocdBuffer in plane metadata
Failed to decode base64 SOCD report
Failed to unlink prior stashed panic log breadcrumb %s
Failed to write to gzip output file with error: %s.
Finished extracting core file data from file offset %llu\n
Failed to initialize Pattern Matching
Read %ld bytes from panic device
wrote boot fault data to: %@
IOService match returned an empty iterator for PMU services
open %s failed with error: %s
Current key does not match expected key format. Skipping
skipping launching TTR because of user defaults...
failed to write system watchdog reset panic log
Failed to locate primary PMU service
ready to submit %s
Failed to allocate lz4 decode stream data buffer.
Failed to read from AEA decrypt stream source.
getCoreDumpContentsWithOffset called with zero length
Failed to read the file contents for key file. Error: %@
Deleting unparseable file '%@'
skipping launching TTR because DumpPanic is currently rate limited...
Failed to allocate %zu bytes for report %d
On-disk zlib-compressed cores are not supported.
Cannot find matching private encryption key for encrypted core
boot fault data found in local device
unable to write socd data to file: %@
Failed to allocate lz4 decode stream.
File seems to be too large to be useful. Skipping
Unknown file version %d
Found embedded panic log of length 0x%llx
EmbeddedPanicDataDecoder initialization error: %@
Failed to parse the current private key. CoreCrypto error %d
Waiting for first unlock ...
no %@ in NVRAM
Failed to remove non-directory entry '%@'. Error: %s
No data was read from the file or device (buffer length was zero).
Failed to set the private key. Error %d
Device already after first unlock
No previous DumpPanic finish cookie
Failed to create directory: %s with error: %s
Failed to write boot fault report
No matched actions available from pattern matching
Neither can find %@
Failed to open %s core compressed output file with error %s
Misformatted key file. Full key not found
Detected stress rack device, skipping prompting user for panic
PanicMedic telemetry is nil, skipping parsing...
failed to write embedded panic data to file: %@
No reports in SOCD container for v2 fallback
AppleArchive is not supported.
Failed to query the size of the boot-args. Error: %d
Opening paniclog path '%@'\n
failed to write ResetCounter log to disk
IOService match returned an empty iterator
Failed to seek to offset %lld in kernelcore.
LZ4 decode stream is not supported.
Failed to allocate gzip output stream.
failed to read header from corefile (%zd bytes) with error: %{errno}d
Failed to gather the file attributes for key file at path: %@
Unable to open file: %@
This device does not support the AppleNVMeDevice API and no paniclog block device was found.
unable to write json to file: %@
Failed to get reports count: %d
Failed to flush the NVRAM store when setting '%@': Error 0x%04x
boot-args NVRAM variable is either not set or inaccessible
no safe log will be discarded
Failed to find matched panic pattern
Wrote log with SOCD data, discarding initial safe log
Found panic log breadcrumb with duplicated boot session uuid
Failed to allocate memory for kdp_corefile buffer
Not pruning because the policy limit is set to 0
failed to allocate staging directory string
saved core file %@
Corefile corrupted. File %zu's (name %s, offset %llu, length %llu) extends past end of file (length %zu).
panic stackshot is type %d
Failed to open AEA decryption stream.
Failed to parse the file contents as a dictionary
Error creating CFString %s
Populated launchOptions.options with matched actions: %@
Couldn't allocate a large enough (%zu bytes) buffer for inflating the compressed panic stackshot
failed to look up hw.osenvironment: %s(%d)
TapToRadarService reports the user has turned off DumpPanic prompts, skipping prompting user for panic
searching IORegistry again after %lds sleep
SOCD data collection still in progress
Keystore unlock has failed
Failed to allocate memory for the boot-args
Upper buffer is at va %p, size %zu bytes
failed to check whether PMU fault data has been processed using access(%s, O_RDONLY) returned: %s
0x%llx bytes of paniclog data found in local device
Corefile corrupted. File %zu's name was not terminated.
Current key does not match input key format. Skipping
Deleting dumppanic boot-arg...
%@
Found storage dump log of length 0x%llx
Failed to initialize lz4 decode stream data.
Failed to set %s xattr returned error : %s
Misformatted key file. Mismatched magic
TapToRadarService does not exist and thus we cannot start a radar
Failed to unlock a keystore. Encryption not vailable.
Prune kernel core files
Misformatted key file. Version not found
Failed to parse the value of the '%@' boot-arg as an integer. Remainder = '%s'
preoslog dump begin
failed to write fallback data to file: %@
bootFaults contained uncategorized PMU fault(s) : %@
SOCD report too small for AWLDataPlatform_v3: %zu < %zu
Couldn't obtain preoslog buffer, sysctl failed with result %s
Required metadata from compressed panic stackshot is unexpected: type: %lld totalout %lld totalin %lld
No panic data detected from '%@'
Failed to remove file %@ with error %@
Failed to open section input stream.
Public encryption key is empty. Corefile is not encrypted
Removing original %s core
Failed to create draft in Tap-to-Radar: %@
Machine configured to reboot on a panic
Successfully processed RTKit crashlog data (%zu bytes)
Unexpected pread result (%zd of %zu bytes) of panic data (%@): errno %d
Failed to write panic log with SOCD data
Failed to allocate lz4 decode stream data.
Found %lu sets of corefiles (policy limit %u, %lu set staged), not cleaning up
boot-args NVRAM variable does not have a '%@'=<value> arg
DumpPanic has already finished running for current boot
Pattern matching service crashed or hung
Stored %ld matched actions: %s
Failed to allocate section input stream.
Prune %@ userspace core files
Corefile corrupted. Log (offset %llu, length %llu) extends past end of file (length %zu).
Failed to parse the file contents as JSON. Error: %@
failed to creat() PMU fault data processed cookie at path %s with error %s
Invalid parameters for get_awl_platform_data
Successfully set AWL platform data in report
Successfully read %llu bytes for the corefile headers
Failed to close compressed %s core with error : %d
kern.preoslog is not supported by this kernel
preoslog dump end
Failed to remove inaccessible entry '%@'. Error: %s
%llu bytes were read from the file or device, but it did not contain any paniclog data (buffer was all zeros).
Failed to read report data for report %d: %d
Removing prior corefiles, found %lu sets (policy limit %u, %lu set staged)
stat(%@): -1 (%{errno}d)
Detected stress rack device, setting xattr on original %s core
implausible data type for %@, abandoning data
Failed to release socd ioservice (%s) iterator: 0x%x
failed to setup corefile output directory with error: %s
Failed to set the '%@' NVRAM variable. Error 0x%04x
Failed to query the boot-args. Error: %d
DumpPanic launched after boot to check for device panic data
Unsupported encryption key format in corefile flags: %llu
gzwrite failed to write %s core
Finished processing %@ core, available at %@
Failed to delete file '%@'. Error: %@
PanicMedic telemetry(valid:%d, reported:%d,panic count:%d) should be valid, hasn't been reported and has panic, skipping parsing...
Pattern Matching initialized with payload available: %s
Failed to create EmbeddedPanicDataDecoder instance
failed to write paniclog data to file: %@
Failed to construct panic log breadcrumb: %s
Failed to parse the input public key with the given format. CoreCrypto error %d
Failed to setup the key-store directory.Error: %@
Couldn't obtain preoslog buffer size, result %s
The platform data is not with expected version, version: %d, expected: %d
gzopen %s
Removing non-directory entry '%@'
Found %lu matched actions from pattern matching
Failed to inflate the compresssed panic stackshot buffer: rc = %d
Cannot find %@
Paniclog data size (%llu bytes) size greater than max buffer size. Truncating.
Failed to create an AEA context.
Failed to decode from lz4 stream source.
Prune core files in %@
Read of %lu bytes from dataOffset %llu (file offset from %llu)(total length %llu) failed with error %{errno}d
Failed to close compressed %s core with error : %s
Unsupported key format in key file: %d
Failed to allocate matching dictionary to match against PMU
Failed to get matching PMU ioservices: 0x%x
Failed to get the agent IDs: %d
Failed to read existing key file
Unable to get device lock state
Buffer size returned by sysctl doesn't match buffer size recorded in the header, preoslog buffer is corrupted
No valid storage dump data found
Failed to write out error panic log
Cannot move staged '%{public}@' to panics folder : %{public}@
Found a valid preoslog buffer at va %{private}p, size %zu bytes, write offset %d, source %s, wrapped %d
Error creating CFString for key %s
erased corefile contents
Read of %lu bytes from dataOffset %llu (file offset from %llu)(total length %llu) only read %lu bytes
Unknown key format %d
the feature flag is not enabled, skipping PanicMedic telemetry...
Expected to find donate action but none found in matched patterns
Falling back to corefile embedded panic log of length 0x%lx
Failed to write full panic log
No paniclog data found in local device
Failed to read %s in %s. This most probably means there's just no SOCD data
Failed to extract AWL platform data from SOCD buffer
Read from panic log breadcrumb failed due to %s
Failed to display tap to radar notification with error: %d
Warning: preoslog log timestamps are not original, they are assigned later when the buffer is being flushed
Found panic log of unknown type (%d) length 0x%llx
Failed to create file: %s with error: %s
Failed to open report record ID: %d, error: %d
write %@ to %s
error zeroing corefile: write(%zu): (%{errno}d)
Not a key file. Magic not found
Failed to generate JSON data for key file. Error: %@
```
