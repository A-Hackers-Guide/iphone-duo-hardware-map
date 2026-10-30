# `/usr/lib/libRoseBooter.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 368,416 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 3168)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/libRoseBooter.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libIOReport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Strings (858)

```
%s::%s: invalid debugInfoDict\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: failed to create capabilities object\n
%s::%s: bad BootNonce size %zu\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: hardware not supported\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: chip reset successful\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: Could not allocate preflight dictionary\n
%s::%s: failed to copy unsigned firmware path\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: Collecting coredump for core: %d\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: invalid rose diagnostics\n
%s::%s: rooted override data unavailable\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: could create coredump filename string\n
%s::%s: %s: %s\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: failed to reset rose\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: error retrieving descriptor: 0x%08x\n
%s::%s: IOReportCreateSamples failed\n
%s::%s: successfully triggered fatal crashlog\n
%s::%s: error getting debug info: 0x%x\n
%s::%s: failed to create firmware object\n
%s::%s: invalid event size: %zu\n
%s::%s: could not initialize firmware object\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: failed to create rose firmware path\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: no rose ticket found in response\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
%s::%s: current firmware state: %d\n
%s::%s: setPowerState (%d) successful\n
%s::%s: Error setting cal payload length to %lu\n
%s::%s: RoseBooter FF Status: %d (MSU Status: %d)\n
%s::%s: Unknown value type: %lu for Key: %s\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: could not open healed rose firmware\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: Crash log is fatal\n
%s::%s: bad transport object provided\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: Firmware to push is missing!\n
%s::%s: Invalid cal data size\n
%s::%s: successfully created symlink for symbol harvest (tmp directory)\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: firmware does %sexist\n
%s::%s: invalid calibration type %d\n
%s::%s: failed to determine if FW exists due to bad input parameter\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: failed to allocate buffer for coredump\n
%s::%s: failed to set bootNonce\n
%s::%s: crash event timeout\n
%s::%s: failed to gather personalization parameters\n
%s::%s: rkos bundle data unavailable\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: failed to create crash syncher\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: failed to create a dictionary\n
%s::%s: failed to create host object\n
%s::%s: failed to get device info list\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: failed to create crash long name string\n
%s::%s: group pruning failed\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: failed to ping device\n
%s::%s: bad input parameter\n
%s::%s: failed to get chip parameters pre boot\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: icnf firmware is missing\n
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: no coredump available for core: %u\n
%s::%s: failed to verify FDR data\n
%s::%s: The key is not a CFString type. The type is: %lu\n
%s::%s: bad input event\n
%s::%s: invalid payload length %zu\n
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: could not get reference to data\n
%s::%s: failed to create firmware\n
%s::%s: ping attempt #%d...\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: failed to create symlink for symbol harvest (tmp directory)\n
%s::%s: nonce is of unexpected size\n
%s::%s: message is not an event\n
%s::%s: ACFU Version: %s\n
%s::%s: unexpected device info parameters\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: Error in event: status 0x%x\n
%s::%s: firmware does not have bootNonce available\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: MGProductTypeUnknown\n
%s::%s: could not create rose transport\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: Pulling firmware logs...\n
%s::%s: failed to create ioReport array\n
%s::%s: no data available to send\n
%s::%s: failed to create firmware path\n
%s::%s: failed to power on rose\n
%s::%s: failed to push healed rose fw\n
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: invalid coredump size: %u\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
%s::%s: Response:\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: persistent path: %s\n
%s::%s: could not create output data\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: error getting host ECID\n
%s::%s: invalid handle\n
%s::%s: Restore boot nonce present!\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: Starting dump of debug info:\n
%s::%s: %s: %lld\n
%s::%s: Identified chip as R1\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: No firmware logs available to pull\n
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: no data classes supported for requested calibration type\n
%s::%s: failed to find rose service\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: There is a crash log available!\n
%s::%s: Bad options\n
%s::%s: No chip ID\n
%s::%s: failed to get event data\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: booter init failed\n
%s::%s: bad device info parameters\n
%s::%s: failed to create dispatch queue\n
%s::%s: Unexpected subscribed channel count: %d\n
%s::%s: failed to parse HSI1 ping info\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: failed to create request dict\n
%s::%s: failed to create event syncher\n
%s::%s: getDebugInfo failed\n
%s::%s: failed to create event\n
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: failed to get chip rev\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: error converting host chipID\n
%s::%s: failed to get firmware path\n
%s::%s: %s\n%@
%s::%s: Logging files under %s\n
%s::%s: response size %zu doesn't match additional info size %u\n
%s::%s: failed to intialialize MSU framework function\n
%s::%s: failed to get firmware path for symbol harvest (tmp directory), skipping symlinking\n
%s::%s: could not create save path url\n
%s::%s: failed to get boot-nonce\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to create command\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: Unable to power on Rose chip\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: error converting host ECID\n
%s::%s: Error sending FDR blob identification\n
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: bad event message\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: invalid parameters\n
%s::%s: invalid rtkitROM handle\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: descriptor is null\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: invalid event format\n
%s::%s: failed to copy firmware container\n
%s::%s: failed to set boot nonce\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: failed to boot rose: %d\n
%s::%s: failed to init certification firmware\n
%s::%s: failed to allocate dict\n
%s::%s: Finished dumping of debug info\n
%s::%s: %s\n
%s::%s: Invalid response (size: %zu)\n
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: failed to open MSU framework\n
%s::%s: could not create libauthinstall object\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: failed to ping after first boot\n
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: failed to create rtkitROM object\n
%s::%s: failed to initialize object\n
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: failed to convert chip rev\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: Invalid refcon crash callback\n
%s::%s: Finished sending %s, waiting for result\n
%s::%s: rrko bundle data unavailable\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
%s::%s: crashLogSize is too small\n
%s::%s: IOReportCopyAllChannels failed\n
%s::%s: bad input parameters\n
%s::%s: failed to create ftab file object\n
%s::%s: failed to get rose firmware path\n
%s::%s: invalid transport handle\n
%s::%s: Requested calibration files 0x%x\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Invalid cal data reference\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: Unable to print the number value for for Key: %s\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: Applied reset glitch workaround successfully\n
%s::%s: attempting to heal firmware...\n
%s::%s: Sent %lu %s file(s):%s\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: failed to get power state\n
%s::%s: failed to save rose fw\n
%s::%s: failed to set log sink: 0x%x\n
%s::%s: failed to create diagnostics object\n
%s::%s: No device info\n
%s::%s: failed to initialize base class\n
%s::%s: failed to create output request dictionary\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: Command:\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: failed to allocate event\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: failed to push rose fw\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: Unable to get RoseServiceState as a number\n
%s::%s: could not create restore dictionary\n
%s::%s: Exception: %s\n
%s::%s: failed to compute host identifier\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: Ping success!\n
%s::%s: Invalid cal data parameter\n
%s::%s: was able to heal firmware from fail forward state? %s\n
%s::%s: Rose target string: %s\n
%s::%s: failed to init base\n
%s::%s: savePath: %s\n
%s::%s: resetting chip\n
%s::%s: failed to ping chip\n
%s::%s: error getting host chipID\n
%s::%s: was able to heal from no firmware state? %s\n
%s::%s: invalid rose transport\n
%s::%s: failed to create healed firwmare URL\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: %d IOReport Channels found\n
%s::%s: dropping event\n
%s::%s: Unable to get SecureROMStatus as a number\n
%s::%s: unknown HSI version\n
%s::%s: skipping firmware save action!\n
%s::%s: BootNonce size: %zu\n
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: platform does not support rose\n
%s::%s: failed to create transport object\n
%s::%s: failed to create capabilities\n
%s::%s: failed to init ftab file object\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: bad parameter\n
%s::%s: no diagnostics object provided\n
%s::%s: failed to validate ping response\n
%s::%s: Bad chip ID size\n
%s::%s: could not create path to unsigned firmware\n
%s::%s: all required personalization parameters are not available\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: failed to gather personalization parameters: %d\n
%s::%s: failed to get debug info: %d\n
%s::%s: failed to get chip parameters for FDR data instance\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: No Channels found\n
%s::%s: unhandled product %lld\n
%s::%s: failed to get target\n
%s::%s: failed to create path\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: Identified chip as R2\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: could not create device info dictionary\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: failed to ping after second boot\n
%s::%s: invalid or no firmware file present in restore options\n
%s::%s: additional info size %u too small for HSI1\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: Timed out on cal file transfer\n
%s::%s: no firmware override specified\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: failed to init bundle firmware\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: no data classes supported for requested calibration type\n
rMC2
%s::%s: unhandled product %lld\n
%s::%s: failed to allocate event\n
bootstrappedPreflight
DSP-CoreDump
copyFirmwareUpdater: nonce is of unexpected size
%s::%s: Sent %lu %s file(s):%s\n
FirmwareData
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: Starting dump of debug info:\n
log
%s::%s: failed to get ecid (ret: 0x%08x)\n
getRoseTarget_block_invoke
operator()
%s::%s: bad transport object provided\n
r1hp0
Rap,FdrRootCaDigest
RoseBootstrappedPreflight
%s::%s: invalid payload length %zu\n
eventCallback
%s::%s: failed to get chip parameters pre boot\n
%s::%s: Bad options\n
%s::%s: failed to initialize base class\n
%s::%s: icnf firmware is missing\n
%s::%s: no diagnostics object provided\n
MSUCopyToleratedStatusForStep
RoseCalibration
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
sendRoseCommand
%s::%s: error converting host chipID\n
rSCl
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: Invalid cal data parameter\n
-
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: invalid rtkitROM handle\n
createRequest
%s::%s: Error in event: status 0x%x\n
%s::%s: failed to convert chip rev\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: could not create save path url\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: invalid coredump size: %u\n
applyResetGlitchWorkaround
%s::%s: could not create device info dictionary\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: failed to get boot-nonce\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: response size %zu doesn't match additional info size %u\n
rMUB
r1hp2
%s::%s: additional info size %u too small for HSI1\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
copyFirmware: could not create output data
r2w0
logDirectoryContents
%s::%s: Firmware to push is missing!\n
%s::%s: group pruning failed\n
%s::%s: descriptor is null\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: failed to create ftab file object\n
%s::%s: drained %zu bytes of firmware logs\n
i16@?0^{__CFDictionary=}8
parsePingResponse
%s::%s: Skipping %s because its parent %s has already been sent\n
RoseTargetMap
%s::%s: failed to create request dict\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: Checking for crash logs for core: %d\n
getDebugInfo
%s::%s: invalid refcon in rose event callback\n
Rap,ChipID
%s::%s: invalid event format\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
AP-CoreDump
%s::%s: invalid handle\n
%s::%s: Invalid response (size: %zu)\n
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: Error setting cal payload length to %lu\n
v8@?0
%s::%s: invalid crashlog of size: %zu\n
crashHandler
%s::%s: Error sending FDR blob identification\n
r2w2
%s::%s: Unable to power on Rose chip\n
%s::%s: invalid debugInfoDict\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
RoseBooterPreflight
FirmwareLogs
%@-%d.bin
%s::%s: unsupported sikblobtype: %u\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: failed to ping after second boot\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: dropping event\n
%s::%s: invalid rose transport\n
ECID
UwbB
%s::%s: failed to get firmware path\n
%s::%s: failed to boot rose: %d\n
AMAuthInstallRequestSendSync
%s::%s: savePath: %s\n
%s::%s: failed to parse HSI1 ping info\n
ACFUBootInterface
%s::%s: failed to get target\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: error retrieving descriptor: 0x%08x\n
pingCheck
%s::%s: platform does not support rose\n
%s::%s: Bad chip ID size\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: failed to create crash long name string\n
%s::%s: persistent path: %s\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
RoseCapabilities
Rap,BoardID
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: failed to create rose firmware path\n
RoseBooterSendCalWithOptions
raw
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: unknown HSI version\n
pushFirmware
%s::%s: failed to get debug info: %d\n
copyFirmwareUpdater
%s::%s: Restore boot nonce present!\n
%s::%s: failed to power on rose\n
AMAuthInstallCreate
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: Collecting coredump for core: %d\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: could not create output data\n
%s::%s: failed to create firmware\n
%s::%s: Timed out on cal file transfer\n
DSP-CrashLog
rose-symlink-ftab.bin
RoseBooterDestroy
RoseRestoreHost
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
not 
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: failed to create command\n
Rap,Nonce
Rap,SecurityMode
copyFirmware: failed to init ftab file object
RoseService
%s::%s: setPowerState (%d) failed: 0x%08x\n
getRoseDebugInfoDict
Rap,ECID
%s::%s: could not create path to unsigned firmware\n
%s::%s: failed to allocate buffer for coredump\n
update_rose
%s::%s: %s: %s\n
rMCl
%s::%s: firmware does %sexist\n
%s::%s: Unable to get SecureROMStatus as a number\n
getDaemonDataStore_block_invoke
%s::%s: No device info\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: Response:\n
%s::%s: invalid rose diagnostics\n
%s::%s: Finished dumping of debug info\n
%s::%s: failed to create firmware path\n
 
%s::%s: %d crash logs pulled for core: %d\n
RoseTransport
%s::%s: The key is not a CFString type. The type is: %lu\n
vector
Rose
%s::%s: nonce is of unexpected size\n
%s::%s: failed to push rose fw\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
isCoreDumpAvailable
copyFirmware: could not add 'rrko' object to final ftab
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: BootNonce size: %zu\n
RoseControllerState
%s::%s: failed to set bootNonce\n
create
%s::%s: Identified chip as R2\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
init
%s::%s: failed to create output request dictionary\n
roseControllerLogSink
%s::%s: failed to find rose service\n
copyFirmware: bundle cert firmware doesn't have rrko
DeviceInfo
getBootNonceHash
%s::%s: error getting debug info: 0x%x\n
copyFirmware: rkos bundle data unavailable
AP-CrashLog
%s::%s: invalid calibration type %d\n
%s::%s: failed to set boot nonce\n
r1p2
%s::%s: failed to init ftab file object\n
RoseCommand
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
waitForFatalCrashCB
Rap,RTKitIOConfig
%s::%s: message is not an event\n
%@.log
runCertification
combined
Rap,SoftwareBinaryDsp1
::
%s::%s: failed to create capabilities object\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: failed to create path\n
/usr/lib/libauthinstall.dylib
%s::%s: IOReportCreateSamples failed\n
%s::%s: invalid transport handle\n
%@/ftab.bin
%s::%s: rkos bundle data unavailable\n
%s::%s: rooted override data unavailable\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: could not open healed rose firmware\n
collectIOReport
%s::%s: current firmware state: %d\n
%s::%s: successfully triggered fatal crashlog\n
Rap,FDRAllowUnsealed
%s::%s: could not create libauthinstall object\n
parsePingInfo
%s::%s: crash event timeout\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: getDebugInfo failed\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
MSUParsedToleratedFailureForStep
%s::%s: was able to heal firmware from fail forward state? %s\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: failed to allocate buffer for firmware logs\n
Rap,SecurityDomain
%s::%s: bad input parameter\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
collectFirmwareLogs
No
RoseBooterGetCal
%s::%s: chip reset successful\n
%s::%s: MGProductTypeUnknown\n
%@-raw.bin
%s::%s: failed to get firmware path for symbol harvest (tmp directory), skipping symlinking\n
@Rap,Ticket
%s::%s: failed to get rose firmware path\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: failed to create firmware object\n
%s::%s: failed to initialize object\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: failed to get chip rev\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: bad input event\n
copyUnsignedFirmwarePath
/usr/standalone/firmware/Rose
%s::%s: Pulling firmware logs...\n
%s::%s: error getting host chipID\n
%s::%s: Requested calibration files 0x%x\n
%s::%s: no firmware override specified\n
%s::%s: invalid event size: %zu\n
%s::%s: %s\n
%s::%s: failed to set log sink: 0x%x\n
r1hp1
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: failed to init bundle firmware\n
%s::%s: failed to allocate dict\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: failed to get device info list\n
Rap,ChipRev
Rap,MinEpoch
%s::%s: failed to gather personalization parameters\n
rMNB
Rap,RTKitOS
%s::%s: failed to push healed rose fw\n
isCrashLogAvailable
%s::%s: failed to ping device\n
%s::%s: Unable to print the number value for for Key: %s\n
%s::%s: failed to get power state\n
setNonce
%s::%s: Unexpected subscribed channel count: %d\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
basic_string
%s::%s: IOReportCopyAllChannels failed\n
RoseBooterAllocate
/var/db/nearbyd/
copyFirmwareUpdater: failed to get device info list
%s::%s: could create coredump filename string\n
triggerCrashLog
%s::%s: failed to get chip parameters for FDR data instance\n
%s::%s: Rose target string: %s\n
Firmware File Dictionary: 
%s::%s: No Channels found\n
RoseIOReport
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: bad input parameters\n
%s::%s: failed to open unsigned rose firmware\n
IOService
%s::%s: Invalid command length (%lu) for hello packet\n
copyFirmware: rooted override data unavailable
%s::%s: rrko bundle data unavailable\n
copyFirmware: failed to init certification firmware
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
copyFirmware: bundle firmware specified is invalid
rose
RoseQueue
%s::%s: failed to create ioReport array\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
Yes
%s::%s: failed to init certification firmware\n
Trusted
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to query rose plugin interface\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: failed to intialialize MSU framework function\n
%s::%s: failed to create rtkitROM object\n
%s::%s: bad event message\n
%s::%s: could not create rose transport\n
%s::%s: Ping success!\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: unexpected device info parameters\n
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: Invalid cal data reference\n
%s::%s: error converting host ECID\n
RoseServiceState
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
UniqueChipID
%s::%s: invalid parameters\n
%s::%s: Crash log is fatal\n
%s::%s: failed to compute host identifier\n
copyFirmwareUpdater: bad device info parameters
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: RoseBooter FF Status: %d (MSU Status: %d)\n
r1p0
r2p0
%s::%s: failed to reset rose\n
flushDebugInfo
collectIOReport_block_invoke
%s::%s: Unknown value type: %lu for Key: %s\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: Logging files under %s\n
collectCoreDump
ChipID
%s::%s: Applied reset glitch workaround successfully\n
copyFWPath
NULL
/usr/standalone/firmware/Rose/%@/ftab.bin
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: failed to copy firmware container\n
%s::%s: No firmware logs available to pull\n
setPowerState
ftab.bin
reset
r2p1
copyFirmware: failed to init bundle firmware
%s::%s: skipping firmware save action!\n
%s::%s: booter init failed\n
getRoseTarget
%s::%s: failed to open libauthinstall dylib\n
RoseBooterHasFailedForward
%s::%s: failed to create capabilities\n
%s::%s: failed to init base\n
%s::%s: failed to get event data\n
%s::%s: %d IOReport Channels found\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: Could not allocate preflight dictionary\n
%s::%s: failed to create diagnostics object\n
%s::%s: failed to create healed firwmare URL\n
createRoseRequest
logCrashLogReason
%s::%s: error while trying to read the coredump 0x%x\n
copyCalDataToSend
%s::%s: Exception: %s\n
%s::%s: no coredump available for core: %u\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: all required personalization parameters are not available\n
%s::%s: successfully created symlink for symbol harvest (tmp directory)\n
%s::%s: failed to register event callback: 0x%x\n
getBoardParameters
%s::%s: failed to create event\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
R2
%s::%s: Contents: status: 0x%02x\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: could not initialize firmware object\n
%s::%s: failed to create crash syncher\n
%s::%s: error getting host ECID\n
RoseBooterInit
validate
Rap,Ticket
RoseEvent
%s::%s: failed to copy unsigned firmware path\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
crashCallback
%s::%s: failed to perform command: 0x%08x\n
%s::%s: could not get reference to data\n
%s::%s: could not add 'rrko' object to final ftab\n
r1p1
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: Command:\n
sendCalibration_block_invoke
%s::%s: invalid or no firmware file present in restore options\n
validateResponse
copyFirmware: could not get 'rrko' object from ftab
UNDEF
createRestoreDictionary
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: firmware does not have bootNonce available\n
RoseBooterBootChip
/tmp/FTABHarvest/
r1p3
map::at:  key not found
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: Invalid refcon crash callback\n
outData
%s::%s: failed to create host object\n
%s::%s: failed to create event syncher\n
%s::%s: %s: %lld\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: failed to gather personalization parameters: %d\n
%s::%s: failed to create symlink for symbol harvest (tmp directory)\n
%s::%s: no rose ticket found in response\n
%@.bin
%s::%s: failed to create transport object\n
%s::%s: was able to heal from no firmware state? %s\n
%s::%s: ACFU Version: %s\n
%s::%s: No chip ID\n
%s::%s: no data available to send\n
%s::%s: failed to save rose fw\n
%s::%s: bad BootNonce size %zu\n
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: setPowerState (%d) successful\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: failed to create a dictionary\n
Rap,ProductionMode
RoseTransport-v1
%s::%s: Identified chip as R1\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: resetting chip\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: failed to validate ping response\n
R1
copyFirmwareUpdater: unexpected device info parameters
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: failed to verify FDR data\n
%@/%@
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: bad parameter\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: failed to add firmware logs to diagnostics\n
getPowerState
%s::%s: bad device info parameters\n
%s::%s: bundle firmware specified is invalid\n
BuildIdentity
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: Finished sending %s, waiting for result\n
sendCalibration
copyFirmware: rrko bundle data unavailable
%s::%s: failed to open MSU framework\n
%s::%s: failed to determine if FW exists due to bad input parameter\n
Rap,RestoreRTKitOS
%s::%s: could not create restore dictionary\n
createRoseController
RoseBooterPerformHealing
%s::%s: attempting to heal firmware...\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: failed to ping chip\n
%s::%s: hardware not supported\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
RosePowerState
%s::%s: Invalid cal data size\n
%s::%s: Unable to get RoseServiceState as a number\n
collectCrashLogs
%s::%s: ping attempt #%d...\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: failed to ping after first boot\n
%s::%s: RoseUpdater Version: %s\n
Rap,RestoreBootNonce
%s::%s: failed to create dispatch queue\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
SecureROMStatus
%s::%s: crashLogSize is too small\n
%s::%s: There is a crash log available!\n
/System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
UTF8String
stringWithFormat:
URLWithString:
```
