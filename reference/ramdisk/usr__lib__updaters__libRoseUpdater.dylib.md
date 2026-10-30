# `/usr/lib/updaters/libRoseUpdater.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 351,760 bytes.

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
%s::%s: Exception: %s\n
%s::%s: failed to init base\n
%s::%s: Bad options\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: group pruning failed\n
%s::%s: Ping success!\n
%s::%s: failed to push healed rose fw\n
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: failed to create a dictionary\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: crash event timeout\n
%s::%s: no data available to send\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: getDebugInfo failed\n
%s::%s: error getting host chipID\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: Bad chip ID size\n
%s::%s: message is not an event\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: Collecting coredump for core: %d\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
%s::%s: Applied reset glitch workaround successfully\n
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: could not create path to unsigned firmware\n
%s::%s: Identified chip as R2\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: failed to allocate buffer for coredump\n
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: failed to get device info list\n
%s::%s: could not create output data\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: bad transport object provided\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: failed to query chip\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: failed to create Rose CFType object\n
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: chip reset successful\n
%s::%s: ping attempt #%d...\n
%s::%s: Failed to collect preflight info\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: Cleaning up restore object\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: failed to create restore object\n
%s::%s: invalid event size: %zu\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: invalid coredump size: %u\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: Finished sending %s, waiting for result\n
%s::%s: Updater object created successfully\n
%s::%s: failed to set boot nonce\n
%s::%s: bad input event\n
%s::%s: crashLogSize is too small\n
%s::%s: IOReportCopyAllChannels failed\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
%s::%s: failed to push rose fw\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: descriptor is null\n
%s::%s: No firmware logs available to pull\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: could not initialize firmware object\n
%s::%s: bad event message\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: unexpected debug log path type\n
%s::%s: Failed to execute command %d\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: failed to create output request dictionary\n
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: Error in event: status 0x%x\n
%s::%s: Firmware to push is missing!\n
%s::%s: failed to create ftab file object\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: Unable to power on Rose chip\n
%s::%s: failed to create dispatch queue\n
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: resetting chip\n
%s::%s: Error sending FDR blob identification\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: failed to create event syncher\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: failed to create ioReport array\n
%s::%s: failed to validate ping response\n
%s::%s: error converting host chipID\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: Response:\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: unhandled product %lld\n
%s::%s: failed to get chip rev\n
%s::%s: dropping event\n
%s::%s: failed to init framework operation\n
%s::%s: RoseRestore object doesn't exist\n
%s::%s: BootNonce size: %zu\n
%s::%s: bad input parameters\n
%s::%s: failed to retain reference to personalized firmware\n
%s::%s: failed to open framework\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: No updater object passed, this is fatal\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: unexpected device info parameters\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: Enabling Rose certification step\n
%s::%s: failed to init logging\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: failed to allocate event\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: AP ticket has wrong type\n
%s::%s: failed to init bundle firmware\n
%s::%s: failed to compute host identifier\n
%s::%s: Could not create RTKitFirmware\n
%s::%s: bad input parameter\n
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: Command %d not supported by restore step\n
%s::%s: icnf firmware is missing\n
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: %s\n%@
%s::%s: failed to get target\n
%s::%s: could not create rose transport\n
%s::%s: invalid or no firmware file present in restore options\n
%s::%s: failed to set log sink: 0x%x\n
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: failed to allocate dict\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: rooted override data unavailable\n
%s::%s: no AP ticket in updater options\n
%s::%s: Failed to initialize base object\n
%s::%s: MGProductTypeUnknown\n
%s::%s: Rose Update is complete!\n
%s::%s: additional info size %u too small for HSI1\n
%s::%s: Restore boot nonce present!\n
%s::%s: failed to ping after first boot\n
%s::%s: could not open healed rose firmware\n
%s::%s: %s\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: invalid debugInfoDict\n
%s::%s: failed to create path\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: invalid event format\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: There is a crash log available!\n
%s::%s: Invalid refcon crash callback\n
%s::%s: Command:\n
%s::%s: Invalid cal data reference\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: failed to ping chip\n
%s::%s: failed to initialize object\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: failed to send calibration\n
%s::%s: failed to initialize update operations\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: No Channels found\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: bad parameter\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: successfully triggered fatal crashlog\n
%s::%s: failed to create command\n
%s::%s: error converting host ECID\n
%s::%s: failed to init ftab file object\n
%s::%s: failed to get boot-nonce\n
%s::%s: failed to create host object\n
%s::%s: unknown HSI version\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: hardware not supported\n
%s::%s: Invalid cal data size\n
%s::%s: rrko bundle data unavailable\n
%s::%s: Booted OS preflight attempt...\n
%s::%s: failed to copy firmware container\n
%s::%s: Identified chip as R1\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: Sent %lu %s file(s):%s\n
%s::%s: %d IOReport Channels found\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: Timed out on cal file transfer\n
%s::%s: failed to initialize base class\n
%s::%s: no firmware override specified\n
%s::%s: could not create save path url\n
%s::%s: invalid payload length %zu\n
%s::%s: bad BootNonce size %zu\n
%s::%s: Initializing RoseRestore for preflight\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: attempt %u of %u...\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: no rose ticket found in response\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: NeRD OS preflight attempt...\n
%s::%s: bad device info parameters\n
%s::%s: failed to copy unsigned firmware path\n
%s::%s: failed to convert chip rev\n
%s::%s: failed to create capabilities object\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: Invalid cal data parameter\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: savePath: %s\n
%s::%s: failed to create firmware\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: firmware does not have bootNonce available\n
%s::%s: failed to set bootNonce\n
%s::%s: failed to get the Rose restore instance\n
%s::%s: failed to create capabilities\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: skipping firmware save action!\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: rkos bundle data unavailable\n
%s::%s: failed to get power state\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: current firmware state: %d\n
%s::%s: response size %zu doesn't match additional info size %u\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: failed to create event\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: Rose target string: %s\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: Local sign enabled? %s\n
%s::%s: Could not create RoseTransport\n
%s::%s: No chip ID\n
%s::%s: failed to create healed firwmare URL\n
%s::%s: failed to create request dict\n
%s::%s: failed to get event data\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: no coredump available for core: %u\n
%s::%s: no diagnostics object provided\n
%s::%s: Crash log is fatal\n
%s::%s: nonce is of unexpected size\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: failed to power on rose\n
%s::%s: failed to get chip parameters pre boot\n
%s::%s: could not create device info dictionary\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: Pulling firmware logs...\n
%s::%s: could create coredump filename string\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: Logging files under %s\n
%s::%s: failed to save rose fw\n
%s::%s: failed to ping after second boot\n
%s::%s: error getting debug info: 0x%x\n
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
%s::%s: failed to reset rose\n
%s::%s: failed to allocate override options\n
%s::%s: Performing Rose preflight...\n
%s::%s: No device info\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: failed to find rose service\n
%s::%s: failed to create crash syncher\n
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: Error setting cal payload length to %lu\n
%s::%s: failed to collect preflight information\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: Invalid response (size: %zu)\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
%s::%s: setPowerState (%d) successful\n
%s::%s: could not create restore dictionary\n
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: error retrieving descriptor: 0x%08x\n
%s::%s: Unexpected subscribed channel count: %d\n
%s::%s: could not get reference to data\n
%s::%s: failed to parse HSI1 ping info\n
%s::%s: successfully collected preflight information\n
%s::%s: failed to init certification firmware\n
%s::%s: could not create libauthinstall object\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: error getting host ECID\n
%s::%s: failed to create Rose CFRuntimeClass\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: failed to create crash long name string\n
%s::%s: IOReportCreateSamples failed\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: no AP ticket in updater options\n
%s::%s: failed to open libauthinstall dylib\n
R1
%s::%s: invalid event size: %zu\n
RoseCommand
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: Could not create RoseTransport\n
r2p1
createRequest
%s::%s: additional info size %u too small for HSI1\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: failed to validate ping response\n
r1p1
%s::%s: personalization attempt %u of %u...\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: failed to create dispatch queue\n
%s::%s: icnf firmware is missing\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: failed to retain reference to personalized firmware\n
Rap,SecurityMode
Rap,ChipRev
%s::%s: failed to init base\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: Enabling Rose certification step\n
RoseRestore
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: error getting host chipID\n
%s::%s: failed to send calibration\n
combinedFDRObjects
%s::%s: failed to initialize object\n
RoseCalibration
%s::%s: failed while waiting for chip to initialize\n
%s::%s: no data available to send\n
%s::%s: failed to set bootNonce\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: could not create libauthinstall object\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
crashCallback
Rap,SoftwareBinaryDsp1
Rap,MinEpoch
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
copyFirmwareUpdater: unexpected device info parameters
RoseQueue
%s::%s: Collecting coredump for core: %d\n
%s::%s: Ping success!\n
%s::%s: successfully collected preflight information\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
collectCrashLogs
%s::%s: Invalid command length (%lu) for hello packet\n
getRoseTarget
basic_string
isCrashLogAvailable
%s::%s: successfully triggered fatal crashlog\n
isCoreDumpAvailable
%s::%s: Performing Rose preflight...\n
%s::%s: failed to copy firmware container\n
%s::%s: could not create save path url\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
collectFirmwareLogs
%s::%s: Bad chip ID size\n
%s::%s: failed to create ftab file object\n
%s::%s: Unrecognized chipID 0x%x\n
getBoardParameters
%s::%s: no coredump available for core: %u\n
setPowerState
LocalSigningID
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
collectCoreDump
%s::%s: Could not create RTKitFirmware\n
rcrt
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
roseControllerLogSink
%s::%s: failed to create Rose CFType object\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: could not create rose transport\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
queryCmd
Firmware File Dictionary: 
%s::%s: no firmware nonce present to boot with\n
%s::%s: failed to allocate event\n
parsePingInfo
%s::%s: unexpected debug log path type\n
copyUnsignedFirmwarePath
%s::%s: failed to push rose fw\n
%s::%s: error retrieving descriptor: 0x%08x\n
UniqueChipID
RoseRestoreHost
DSP-CoreDump
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: failed to add firmware logs to diagnostics\n
i16@?0^{__CFDictionary=}8
getRoseDebugInfoDict
%s::%s: Error setting cal payload length to %lu\n
%s::%s: failed to allocate override options\n
%s::%s: rrko bundle data unavailable\n
outData
%s::%s: failed to save rose fw\n
%s::%s: Crash log is fatal\n
optionsOverride: 
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
APTicket
%s::%s: rooted override data unavailable\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%@.bin
eventCallback
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: failed to create capabilities\n
%s::%s: nonce is of unexpected size\n
AMAuthInstallCreate
%s::%s: failed to initialize LAI lib create function\n
%s::%s: No firmware logs available to pull\n
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: failed to open framework\n
%s::%s: failed to get power state\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: Invalid cal data reference\n
Rap,BoardID
copyFirmware: could not add 'rrko' object to final ftab
%s::%s: Identified chip as R1\n
%s::%s: failed to create crash syncher\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: failed to get device info list\n
copyFirmware: could not create output data
createRestoreDictionary
%s::%s: No updater object passed, this is fatal\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: failed to initialize update operations\n
Rap,Ticket
copyFirmware: failed to init ftab file object
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%@.log
copyFirmware: bundle cert firmware doesn't have rrko
AMAuthInstallRequestSendSync
%s::%s: BootNonce size: %zu\n
%s::%s: getDebugInfo failed\n
v8@?0
%s::%s: Local sign enabled? %s\n
%s::%s: savePath: %s\n
ftab.bin
%s::%s: bad input parameter\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: Updater object created successfully\n
UNDEF
combined
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
performCmd
NULL
RoseUpdaterCreate
copyFirmware: rrko bundle data unavailable
waitForFatalCrashCB
Rap,RestoreRTKitOS
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: firmware does not have bootNonce available\n
Rap,ECID
IOService
%s::%s: IOReportCreateSubscription failed\n
%s::%s: IOReportSampleCopyDescription() failed\n
applyResetGlitchWorkaround
r1p3
%s::%s: failed to power on rose\n
%s::%s: AP ticket has wrong type\n
R2
%s::%s: NeRD OS preflight attempt...\n
No
Rap,RTKitIOConfig
%s::%s: Applied reset glitch workaround successfully\n
<RoseRestoreObj %p [%p]>{}
%s::%s: RoseUpdater Version: %s\n
createRoseRequest
%s::%s: invalid payload length %zu\n
%s::%s: No device info\n
%s::%s: failed to create ioReport array\n
%s::%s: could not get reference to data\n
failed to get the Rose restore instance
RoseUpdater
DeviceInfo
%s::%s: failed to init ftab file object\n
%s::%s: Sent %lu %s file(s):%s\n
r1hp1
RoseControllerState
DSP-CrashLog
Incomplete parameter set for certification
%s::%s: Identified chip as R2\n
%s::%s: bad event message\n
%s::%s: bad parameter\n
%s::%s: There is a crash log available!\n
%s::%s: Failed to initialize restore object (%d)\n
Rap,FdrRootCaDigest
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
copyFirmware: rkos bundle data unavailable
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
copyCalDataToSend
gatherPreflightParameters
RoseRestoreObjDestroy
%s::%s: failed to ping after second boot\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: Failed to apply reset glitch workaround\n
PRGetPreflightInfo
copyFirmwareUpdater: bad device info parameters
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: hardware not supported\n
%s::%s: group pruning failed\n
%s::%s: ping attempt #%d...\n
%s::%s: Failed to initialize base object\n
%s::%s: MGProductTypeUnknown\n
%s::%s: failed to push healed rose fw\n
parsePingResponse
%s::%s: failed to create Rose CFRuntimeClass\n
%s::%s: Failed to execute command %d\n
%s::%s: failed to create event syncher\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: could not create restore dictionary\n
%s::%s: failed to get boot-nonce\n
%s::%s: bad input event\n
%s::%s: invalid coredump size: %u\n
%s::%s: failed to ping chip\n
%s::%s: attempt %u of %u...\n
failed to create Rose CFType object
RoseUpdaterExecCommand
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
sendRoseCommand
%s::%s: response size %zu too small for HSI1\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: Attempting to apply reset glitch workaround\n
Failed to perform certification step
%s::%s: failed to init framework operation\n
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: Booted OS preflight attempt...\n
RoseRestore object doesn't exist
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: invalid or no firmware file present in restore options\n
getBootNonceHash
RosePowerState
%s::%s: failed to set boot nonce\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
rSCl
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: Crashlog Reason: \"%s\"\n
getDebugInfo
%s::%s: failed to allocate dict\n
%s::%s: failed to query chip\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: failed to find rose service\n
%s::%s: Failed to get a restore mount point to create FW object with\n
copyFirmwareUpdater
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: Firmware to push is missing!\n
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: failed to init logging\n
%s::%s: Bad options\n
%s::%s: unexpected device info parameters\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
setNonce
No certification URL found for certification step
%s::%s: Initializing RoseRestore for preflight\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: no rose ticket found in response\n
%s::%s: could not open healed rose firmware\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
collectIOReport_block_invoke
%s::%s: Calibration file transfer success: %s!\n
copyFirmwareUpdater: failed to get device info list
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
RoseBootstrappedPreflight
%s::%s: message is not an event\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: Invalid cal data parameter\n
%s::%s: Logging files under %s\n
BuildIdentity
%s::%s: failed to create request dict\n
RoseRestoreObj
%s::%s: failed to get chip parameters pre boot\n
createRoseController
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: failed to reset rose\n
copyFirmware: bundle firmware specified is invalid
%s::%s: booted chip query attempt %u of %u...\n
logDirectoryContents
%s::%s: descriptor is null\n
%s::%s: RoseRestore object doesn't exist\n
pushFirmware
%s::%s: failed to compute host identifier\n
%s::%s: no firmware override specified\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
copyFirmware: rooted override data unavailable
copyFirmware: failed to init certification firmware
%s::%s: Manifest for firmware is missing!\n
rMNB
%s::%s: bad transport object provided\n
%s::%s: bad input parameters\n
%s::%s: failed to create restore object\n
Rap,RTKitOS
%s::%s: could not create path to unsigned firmware\n
%s::%s: crash event timeout\n
%s::%s: Invalid cal data size\n
sendCalibration_block_invoke
%s::%s: bad boot nonce hash size 1st time: %zu\n
rMCl
flushDebugInfo
%s::%s: crashLogSize is too small\n
%@-%d.bin
%s::%s: error getting debug info: 0x%x\n
copyFirmware: failed to init bundle firmware
map::at:  key not found
%s::%s: failed to init restore option dictionaries\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: invalid debugInfoDict\n
%s::%s: failed to get chip revision (ret: 0x%08x)\n
@Rap,Ticket
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: could not create output data\n
%s::%s: skipping firmware save action!\n
%s::%s: failed to get event data\n
%s::%s: Failed to collect preflight info\n
FirmwareData
crashHandler
%s::%s: Response:\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
DebugLogPath
Rap,ChipID
/usr/standalone/firmware/Rose/%@/ftab.bin
/usr/lib/libauthinstall.dylib
%s::%s: failed to create capabilities object\n
AP-CrashLog
r2w0
%s::%s: failed to create firmware\n
%s::%s: Timed out on cal file transfer\n
vector
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: No Channels found\n
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
%s::%s: failed to create event\n
raw
%s::%s: Restore boot nonce present!\n
copyFirmwareUpdater: nonce is of unexpected size
%s::%s: failed to copy unsigned firmware path\n
sendCalibration
%s::%s: failed to allocate buffer for crash log\n
%s::%s: Invalid refcon crash callback\n
%s::%s: failed to create a dictionary\n
RoseTransport-v1
create
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: error converting host chipID\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
%s::%s: failed to parse HSI2 ping info\n
Failed to collect preflight info
%s::%s: Rose Update is complete!\n
Rap,RestoreBootNonce
bootstrappedPreflight
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: %s\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: rkos bundle data unavailable\n
%s::%s: IOReportCopyAllChannels failed\n
triggerCrashLog
init
%s::%s: failed to init certification firmware\n
%s::%s: could not initialize firmware object\n
%s::%s: Invalid response (size: %zu)\n
rose
RoseIOReport
/usr/standalone/firmware/Rose/
r1p0
Rose
%s::%s: could not create device info dictionary\n
logCrashLogReason
%s::%s: Command:\n
/System/Library/PrivateFrameworks/Proximity.framework/Proximity
%s::%s: failed to create output request dictionary\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: error getting host ECID\n
%s::%s: failed to get target\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: no diagnostics object provided\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
reset
%s::%s: No chip ID\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: Unable to power on Rose chip\n
RoseTargetMap
runCertification
RoseCapabilities
log
RoseEvent
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: %d IOReport Channels found\n
%s::%s: failed to create command\n
Rap,ProductionMode
Trusted
%s::%s: failed to allocate buffer for coredump\n
%@-raw.bin
%s::%s: RosePowerState isn't present in the dictionary\n
Yes
r2p0
%s::%s: failed to create path\n
%s::%s: failed to get chip rev\n
rMC2
%s::%s: Error in event: status 0x%x\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
ChipID
%s::%s: unknown HSI version\n
 
operator()
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: failed to parse HSI1 ping info\n
::
RoseService
%s::%s: failed to read RosePowerState value from the dictionary\n
failed to create Rose CFRuntimeClass
%s::%s: failed to convert chip rev\n
%s::%s: bad BootNonce size %zu\n
collectIOReport
%s::%s: failed to create crash long name string\n
%s::%s: Finished sending %s, waiting for result\n
%s::%s: bad device info parameters\n
validate
%s::%s: Unexpected subscribed channel count: %d\n
r2w2
%s::%s: Exception: %s\n
FirmwareLogs
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: error converting host ECID\n
RoseTransport
r1p2
failed to init logging
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: failed to ping after first boot\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: response size %zu doesn't match additional info size %u\n
-
%s::%s: unhandled product %lld\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: current firmware state: %d\n
r1hp2
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: setPowerState (%d) successful\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
r1hp0
Rap,SecurityDomain
copyFirmware: could not get 'rrko' object from ftab
%s::%s: could create coredump filename string\n
UwbB
%s::%s: Error sending FDR blob identification\n
AP-CoreDump
%s::%s: bundle firmware specified is invalid\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: failed to create healed firwmare URL\n
rMUB
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
Rap,Nonce
%s::%s: failed to init bundle firmware\n
%s::%s: failed to create host object\n
%s::%s: boot nonce hash size: %zu\n
%s::%s: dropping event\n
%s::%s: Pulling firmware logs...\n
%s::%s: chip reset successful\n
getPowerState
%s::%s: unsupported sikblobtype: %u\n
%s::%s: failed to get the Rose restore instance\n
%s::%s: Cleaning up restore object\n
Rap,FDRAllowUnsealed
%s::%s: failed to initialize base class\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: invalid event format\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: Command %d not supported by restore step\n
RoseUpdaterIsDone
/usr/standalone/firmware/Rose
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: IOReportCreateSamples failed\n
pingCheck
getRoseTarget_block_invoke
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: resetting chip\n
%s::%s: Rose target string: %s\n
validateResponse
%s::%s: failed to set log sink: 0x%x\n
%s::%s: failed to collect preflight information\n
UTF8String
```
