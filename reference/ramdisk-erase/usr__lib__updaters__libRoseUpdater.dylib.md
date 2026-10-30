# `/usr/lib/updaters/libRoseUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 351,760 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 3024)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/updaters/libRoseUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libIOReport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Strings (844)

```
%s::%s: %d IOReport Channels found\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: could not open healed rose firmware\n
%s::%s: %s\n
%s::%s: Exception: %s\n
%s::%s: Invalid response (size: %zu)\n
%s::%s: failed to send calibration\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: failed to create path\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: failed to initialize update operations\n
%s::%s: Restore boot nonce present!\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: savePath: %s\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
%s::%s: rrko bundle data unavailable\n
%s::%s: failed to init certification firmware\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: could not create restore dictionary\n
%s::%s: failed to create request dict\n
%s::%s: failed to create dispatch queue\n
%s::%s: ping attempt #%d...\n
%s::%s: Failed to collect preflight info\n
%s::%s: Logging files under %s\n
%s::%s: failed to push rose fw\n
%s::%s: failed to init framework operation\n
%s::%s: failed to create healed firwmare URL\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: hardware not supported\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: failed to find rose service\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: no coredump available for core: %u\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: invalid payload length %zu\n
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: failed to compute host identifier\n
%s::%s: Finished sending %s, waiting for result\n
%s::%s: Rose Update is complete!\n
%s::%s: invalid event format\n
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: Failed to execute command %d\n
%s::%s: failed to create output request dictionary\n
%s::%s: failed to copy firmware container\n
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: Crash log is fatal\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: failed to validate ping response\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: Firmware to push is missing!\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: Response:\n
%s::%s: Updater object created successfully\n
%s::%s: failed to create host object\n
%s::%s: failed to init base\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: failed to allocate dict\n
%s::%s: attempt %u of %u...\n
%s::%s: failed to create event syncher\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: getDebugInfo failed\n
%s::%s: failed to query chip\n
%s::%s: unknown HSI version\n
%s::%s: failed to init ftab file object\n
%s::%s: failed to create ftab file object\n
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: IOReportCopyAllChannels failed\n
%s::%s: RoseRestore object doesn't exist\n
%s::%s: failed to initialize base class\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: bad input parameter\n
%s::%s: additional info size %u too small for HSI1\n
%s::%s: failed to collect preflight information\n
%s::%s: failed to get target\n
%s::%s: failed to get chip parameters pre boot\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: failed to ping after second boot\n
%s::%s: bad BootNonce size %zu\n
%s::%s: failed to create a dictionary\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: current firmware state: %d\n
%s::%s: could not get reference to data\n
%s::%s: failed to create Rose CFType object\n
%s::%s: No device info\n
%s::%s: nonce is of unexpected size\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: Pulling firmware logs...\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: failed to create crash long name string\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: Command %d not supported by restore step\n
%s::%s: Bad options\n
%s::%s: failed to get device info list\n
%s::%s: bad device info parameters\n
%s::%s: could not create save path url\n
%s::%s: failed to push healed rose fw\n
%s::%s: Sent %lu %s file(s):%s\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: failed to save rose fw\n
%s::%s: failed to initialize object\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: failed to ping chip\n
%s::%s: Error sending FDR blob identification\n
%s::%s: failed to reset rose\n
%s::%s: failed to get event data\n
%s::%s: failed to set log sink: 0x%x\n
%s::%s: bad parameter\n
%s::%s: successfully triggered fatal crashlog\n
%s::%s: There is a crash log available!\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: error converting host chipID\n
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: crashLogSize is too small\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: AP ticket has wrong type\n
%s::%s: failed to copy unsigned firmware path\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: BootNonce size: %zu\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: No firmware logs available to pull\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: Could not create RTKitFirmware\n
%s::%s: failed to create Rose CFRuntimeClass\n
%s::%s: failed to create crash syncher\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: Enabling Rose certification step\n
%s::%s: No updater object passed, this is fatal\n
%s::%s: rooted override data unavailable\n
%s::%s: unexpected device info parameters\n
%s::%s: bad event message\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: error retrieving descriptor: 0x%08x\n
%s::%s: Failed to initialize base object\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: bad input event\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: Ping success!\n
%s::%s: error converting host ECID\n
%s::%s: rkos bundle data unavailable\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: failed to convert chip rev\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: No Channels found\n
%s::%s: failed to create capabilities\n
%s::%s: %s\n%@
%s::%s: could not create path to unsigned firmware\n
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: Identified chip as R2\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: failed to parse HSI1 ping info\n
%s::%s: Rose target string: %s\n
%s::%s: failed to get chip rev\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: Invalid cal data reference\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: crash event timeout\n
%s::%s: chip reset successful\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: failed to retain reference to personalized firmware\n
%s::%s: Performing Rose preflight...\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: failed to create command\n
%s::%s: firmware does not have bootNonce available\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: could not initialize firmware object\n
%s::%s: bad transport object provided\n
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: unhandled product %lld\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: could not create rose transport\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: Initializing RoseRestore for preflight\n
%s::%s: failed to create restore object\n
%s::%s: failed to create capabilities object\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: Collecting coredump for core: %d\n
%s::%s: Applied reset glitch workaround successfully\n
%s::%s: Local sign enabled? %s\n
%s::%s: failed to create firmware\n
%s::%s: invalid debugInfoDict\n
%s::%s: Invalid cal data parameter\n
%s::%s: successfully collected preflight information\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: icnf firmware is missing\n
%s::%s: Command:\n
%s::%s: failed to create ioReport array\n
%s::%s: skipping firmware save action!\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: MGProductTypeUnknown\n
%s::%s: failed to power on rose\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: failed to set bootNonce\n
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: Could not create RoseTransport\n
%s::%s: Bad chip ID size\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: no data available to send\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: error getting host ECID\n
%s::%s: No chip ID\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: failed to ping after first boot\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: IOReportCreateSamples failed\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: failed to open framework\n
%s::%s: could not create output data\n
%s::%s: no rose ticket found in response\n
%s::%s: invalid or no firmware file present in restore options\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: failed to allocate buffer for coredump\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: Booted OS preflight attempt...\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: resetting chip\n
%s::%s: Invalid cal data size\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: failed to init bundle firmware\n
%s::%s: Unable to power on Rose chip\n
%s::%s: unexpected debug log path type\n
%s::%s: Cleaning up restore object\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: failed to allocate event\n
%s::%s: Error setting cal payload length to %lu\n
%s::%s: dropping event\n
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: Invalid refcon crash callback\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: setPowerState (%d) successful\n
%s::%s: bad input parameters\n
%s::%s: response size %zu doesn't match additional info size %u\n
%s::%s: failed to get the Rose restore instance\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: could not create device info dictionary\n
%s::%s: failed to get boot-nonce\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: no AP ticket in updater options\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: error getting debug info: 0x%x\n
%s::%s: could not create libauthinstall object\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: descriptor is null\n
%s::%s: error getting host chipID\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
%s::%s: failed to init logging\n
%s::%s: no firmware override specified\n
%s::%s: failed to create event\n
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: no diagnostics object provided\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
%s::%s: invalid coredump size: %u\n
%s::%s: Timed out on cal file transfer\n
%s::%s: failed to allocate override options\n
%s::%s: failed to set boot nonce\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: Unexpected subscribed channel count: %d\n
%s::%s: NeRD OS preflight attempt...\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: message is not an event\n
%s::%s: could create coredump filename string\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: invalid event size: %zu\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: failed to get power state\n
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: group pruning failed\n
%s::%s: Identified chip as R1\n
%s::%s: Error in event: status 0x%x\n
init
Firmware File Dictionary: 
%s::%s: chip reset successful\n
%s::%s: failed to create firmware\n
rMCl
rSCl
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: failed to create request dict\n
RoseQueue
%s::%s: no coredump available for core: %u\n
reset
%s::%s: Enabling Rose certification step\n
%s::%s: No chip ID\n
DSP-CrashLog
%s::%s: Initializing RoseRestore for preflight\n
%s::%s: Failed to execute command %d\n
%s::%s: could not initialize firmware object\n
%s::%s: failed to push healed rose fw\n
combined
%s::%s: setPowerState (%d) successful\n
%s::%s: Local sign enabled? %s\n
%s::%s: failed to initialize update operations\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
performCmd
@Rap,Ticket
%s::%s: could not create ACFU diagnostics\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: IOReportIterate retVal: 0x%x\n
/System/Library/PrivateFrameworks/Proximity.framework/Proximity
DeviceInfo
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: failed to ping after second boot\n
R2
RoseCommand
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: No Channels found\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: skipping firmware save action!\n
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: Pulling firmware logs...\n
%s::%s: failed to allocate buffer for coredump\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
Failed to collect preflight info
copyFirmware: rkos bundle data unavailable
outData
%s::%s: Reserved (%lu bytes):\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: no rose ticket found in response\n
%s::%s: message is not an event\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: ping attempt #%d...\n
No certification URL found for certification step
copyFirmware: rrko bundle data unavailable
%s::%s: failed to create capabilities object\n
%s::%s: invalid coredump size: %u\n
r1hp0
pingCheck
Rap,ChipRev
RoseCapabilities
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: failed to reset chip: 0x%08x\n
eventCallback
%s::%s: could not get reference to data\n
%s::%s: error converting host ECID\n
Rap,FDRAllowUnsealed
%s::%s: nonce is of unexpected size\n
collectCoreDump
%s::%s: failed to compute host identifier\n
%s::%s: Command %d not supported by restore step\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: BootNonce size: %zu\n
pushFirmware
%s::%s: Finished sending %s, waiting for result\n
%s::%s: failed to create output request dictionary\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: unexpected debug log path type\n
%s::%s: bad device info parameters\n
Rap,Nonce
Rap,ProductionMode
roseControllerLogSink
%s::%s: failed to init framework operation\n
RoseUpdaterIsDone
copyFirmware: could not add 'rrko' object to final ftab
%s::%s: bad parameter\n
%s::%s: crash event timeout\n
%s::%s: no AP ticket in updater options\n
%s::%s: NeRD OS preflight attempt...\n
RoseTargetMap
%s::%s: failed to get the Rose restore instance\n
%s::%s: creating rose plugin interface failed: 0x%x\n
RoseService
crashCallback
ChipID
%s::%s: Could not create RTKitFirmware\n
%s::%s: failed to create Rose CFType object\n
%s::%s: group pruning failed\n
%s::%s: no diagnostics object provided\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: failed to create a dictionary\n
%s::%s: failed to init restore option dictionaries\n
%@.log
RoseRestoreObj
%s::%s: Identified chip as R2\n
%s::%s: bad input parameter\n
v8@?0
%s::%s: firmware does not have bootNonce available\n
%s::%s: No device info\n
%s::%s: failed to get chip parameters pre boot\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: error getting host chipID\n
r1hp1
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: Rose target string: %s\n
%s::%s: no firmware override specified\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: failed to send calibration\n
Rap,RTKitIOConfig
%s::%s: failed to open libauthinstall dylib\n
Trusted
%s::%s: failed to get chipID (ret: 0x%08x)\n
LocalSigningID
%s::%s: invalid or no firmware file present in restore options\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: Command:\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: could not open healed rose firmware\n
%s::%s: bad BootNonce size %zu\n
%s::%s: failed to get device info list\n
copyFirmware: could not get 'rrko' object from ftab
parsePingInfo
collectIOReport
%s::%s: IOReportCreateSamples failed\n
%s::%s: invalid debugInfoDict\n
%s::%s: invalid refcon in rose event callback\n
RoseRestore object doesn't exist
%s::%s: failed to reset rose\n
%s::%s: Exception: %s\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
RoseIOReport
%s::%s: failed to init logging\n
%s::%s: unexpected device info parameters\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
r1p0
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
RoseTransport-v1
%s::%s: failed to create capabilities\n
RoseUpdaterExecCommand
/usr/standalone/firmware/Rose
logCrashLogReason
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: failed to create Rose CFRuntimeClass\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
collectFirmwareLogs
%s::%s: failed to set bootNonce\n
%s::%s: Contents: status: 0x%02x\n
Rap,ECID
%s::%s: failed to create path\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: error retrieving descriptor: 0x%08x\n
Incomplete parameter set for certification
%s::%s: Invalid response (size: %zu)\n
%s::%s: Error flushing the debug logs: (%d)\n
waitForFatalCrashCB
%s::%s: could not create libauthinstall object\n
FirmwareLogs
%s::%s: resetting chip\n
Rap,SoftwareBinaryDsp1
copyFirmware: failed to init certification firmware
FirmwareData
%s::%s: Invalid cal data size\n
%s::%s: failed to retain reference to personalized firmware\n
Rose
IOService
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: firmware log collection isn't supported for this chip\n
-
%s::%s: failed to create restore object\n
%s::%s: Bad options\n
%s::%s: failed to get event data\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: failed to initialize object\n
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
copyFirmwareUpdater: failed to get device info list
%s::%s: failed to ping after first boot\n
%s::%s: savePath: %s\n
rMC2
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: invalid crashlog of size: %zu\n
AMAuthInstallRequestSendSync
rose
%s::%s: failed to ping chip\n
%s::%s: Ping success!\n
Rap,SecurityMode
%s::%s: error while trying to trigger a crashlog: 0x%x\n
copyFirmwareUpdater
%s::%s: failed to set log sink: 0x%x\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
queryCmd
R1
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
crashHandler
%s::%s: Failed to initialize base object\n
%s::%s: unhandled product %lld\n
RoseUpdaterCreate
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: failed to create crash long name string\n
%s::%s: current firmware state: %d\n
DebugLogPath
r1p2
map::at:  key not found
%s::%s: invalid payload length %zu\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: no data available to send\n
BuildIdentity
%s::%s: Response:\n
APTicket
%s::%s: AP ticket has wrong type\n
%s::%s: successfully collected preflight information\n
%s::%s: invalid event size: %zu\n
raw
gatherPreflightParameters
%s::%s: Booted OS preflight attempt...\n
setNonce
%s::%s: Applied reset glitch workaround successfully\n
%s::%s: Unable to get the current Rose chip power state\n
Failed to perform certification step
Rap,RTKitOS
%s::%s: failed to get chip rev\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
getBoardParameters
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
r1p3
%s::%s: failed to initialize base class\n
%@-raw.bin
copyCalDataToSend
RoseRestore
%s::%s: rooted override data unavailable\n
Rap,SecurityDomain
Rap,FdrRootCaDigest
%s::%s: failed to init certification firmware\n
UNDEF
%s::%s: could not create save path url\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
%s::%s: Unexpected subscribed channel count: %d\n
copyFirmware: failed to init ftab file object
bootstrappedPreflight
%s::%s: could not create rose transport\n
RoseBootstrappedPreflight
log
%s::%s: error getting host ECID\n
%s::%s: failed to validate ping response\n
failed to create Rose CFRuntimeClass
RoseEvent
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: failed to create command\n
UniqueChipID
%s::%s: Could not create RoseTransport\n
%s::%s: failed to get target\n
%s::%s: failed to get power state\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: failed to init ftab file object\n
/usr/lib/libauthinstall.dylib
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%@-%d.bin
%s::%s: Invalid refcon crash callback\n
parsePingResponse
%s::%s: failed to collect preflight information\n
optionsOverride: 
%s::%s: failed to copy unsigned firmware path\n
%s::%s: unknown HSI version\n
createRoseController
%s::%s: icnf firmware is missing\n
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: failed to parse HSI2 ping info\n
logDirectoryContents
%s::%s: bad event message\n
getPowerState
%s::%s: failed to parse HSI1 ping info\n
copyFirmware: failed to init bundle firmware
create
%s::%s: No firmware logs available to pull\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: error converting host chipID\n
DSP-CoreDump
%s::%s: no firmware nonce present to boot with\n
%s::%s: Collecting coredump for core: %d\n
RosePowerState
%s::%s: Error setting cal payload length to %lu\n
%s::%s: failed to create ftab file object\n
%s::%s: failed to init base\n
copyUnsignedFirmwarePath
%s::%s: additional info size %u too small for HSI1\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: IOReportCopyAllChannels failed\n
collectIOReport_block_invoke
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: failed to create crash syncher\n
%s::%s: error getting debug info: 0x%x\n
%s::%s: failed to copy firmware container\n
%s::%s: failed to create healed firwmare URL\n
%s::%s: Crash log is fatal\n
sendCalibration_block_invoke
combinedFDRObjects
r1hp2
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: failed to create dispatch queue\n
%s::%s: Manifest for firmware is missing!\n
collectCrashLogs
%s::%s: Failed to collect preflight info\n
%s::%s: Updater object created successfully\n
Rap,RestoreBootNonce
copyFirmware: could not create output data
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: IOReportCreateSubscription failed\n
applyResetGlitchWorkaround
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: dropping event\n
ftab.bin
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: Rose Update is complete!\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: failed to allocate event\n
getDebugInfo
%s::%s: response size %zu doesn't match additional info size %u\n
runCertification
Yes
%s::%s: Firmware to push is missing!\n
%s::%s: Error sending FDR blob identification\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
RoseRestoreHost
%s::%s: Identified chip as R1\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: crashLogSize is too small\n
%s::%s: failed to power on rose\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
getRoseDebugInfoDict
PRGetPreflightInfo
%s::%s: Sent %lu %s file(s):%s\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: bad input parameters\n
%s::%s: Attempting to apply reset glitch workaround\n
r2w0
%s::%s: bundle firmware specified is invalid\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: %s\n
%s::%s: bad input event\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
r1p1
%s::%s: rrko bundle data unavailable\n
%s::%s: failed to find rose service\n
createRequest
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: rkos bundle data unavailable\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: Checking for crash logs for core: %d\n
isCoreDumpAvailable
triggerCrashLog
RoseTransport
failed to create Rose CFType object
%s::%s: failed to init bundle firmware\n
%s::%s: failed to push rose fw\n
rMNB
validateResponse
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: getDebugInfo failed\n
No
RoseUpdater
getBootNonceHash
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: failed to allocate dict\n
r2p1
NULL
RoseRestoreObjDestroy
Rap,BoardID
AMAuthInstallCreate
%s::%s: failed to get chip parameters post boot\n
%s::%s: hardware not supported\n
sendRoseCommand
AP-CrashLog
copyFirmwareUpdater: bad device info parameters
/usr/standalone/firmware/Rose/%@/ftab.bin
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: Logging files under %s\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: could not create output data\n
%s::%s: failed to convert chip rev\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
vector
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
r2p0
getRoseTarget_block_invoke
<RoseRestoreObj %p [%p]>{}
%s::%s: Error status (0x%04x) in response\n
Rap,MinEpoch
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: There is a crash log available!\n
copyFirmwareUpdater: unexpected device info parameters
UwbB
%@.bin
%s::%s: failed to get chip revision (ret: 0x%08x)\n
i16@?0^{__CFDictionary=}8
%s::%s: failed to perform command with timeout: 0x%08x\n
createRestoreDictionary
 
setPowerState
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: failed to allocate override options\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
RoseCalibration
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: %d IOReport Channels found\n
%s::%s: Failed to apply reset glitch workaround\n
AP-CoreDump
failed to get the Rose restore instance
%s::%s: Restore boot nonce present!\n
%s::%s: could not create restore dictionary\n
operator()
%s::%s: failed to open framework\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: failed to create ioReport array\n
/usr/standalone/firmware/Rose/
failed to init logging
%s::%s: Cleaning up restore object\n
%s::%s: could not create path to unsigned firmware\n
%s::%s: could not create device info dictionary\n
%s::%s: bad transport object provided\n
%s::%s: failed to create event syncher\n
%s::%s: RoseRestore object doesn't exist\n
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
copyFirmware: rooted override data unavailable
copyFirmware: bundle cert firmware doesn't have rrko
rMUB
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: Unable to power on Rose chip\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
isCrashLogAvailable
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: Invalid cal data reference\n
%s::%s: Performing Rose preflight...\n
getRoseTarget
Rap,ChipID
%s::%s: Bad chip ID size\n
basic_string
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
%s::%s: successfully triggered fatal crashlog\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: Timed out on cal file transfer\n
%s::%s: MGProductTypeUnknown\n
::
Rap,Ticket
%s::%s: failed to get boot-nonce\n
%s::%s: failed to set boot nonce\n
%s::%s: No updater object passed, this is fatal\n
copyFirmwareUpdater: nonce is of unexpected size
copyFirmware: bundle firmware specified is invalid
%s::%s: failed to save rose fw\n
createRoseRequest
%s::%s: Error in event: status 0x%x\n
flushDebugInfo
%s::%s: failed to create host object\n
%s::%s: failed to create event\n
%s::%s: could create coredump filename string\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: failed to query chip\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: Invalid cal data parameter\n
rcrt
%s::%s: Unrecognized chipID 0x%x\n
sendCalibration
%s::%s: invalid event format\n
%s::%s: error while trying to read the coredump 0x%x\n
RoseControllerState
Rap,RestoreRTKitOS
%s::%s: attempt %u of %u...\n
r2w2
validate
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: descriptor is null\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
UTF8String
```
