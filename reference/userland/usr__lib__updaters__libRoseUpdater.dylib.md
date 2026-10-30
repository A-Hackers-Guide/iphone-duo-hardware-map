# `/usr/lib/updaters/libRoseUpdater.dylib`

iOS 27.2 dyld shared cache image. Version `133.0.0.0.0`. **[DSC]**

## Linked libraries (10)

- `/usr/lib/libamsupport.dylib`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/AppleConvergedFirmwareUpdater.framework/AppleConvergedFirmwareUpdater`
- `/usr/lib/libIOReport.dylib`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Strings (843)

```
%s::%s: rkos bundle data unavailable\n
%s::%s: could not initialize firmware object\n
%s::%s: personalization attempt %u of %u...\n
%s::%s: failed to get event data\n
%s::%s: Unable to get the current Rose chip power state\n
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: Collecting coredump for core: %d\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: failed to create command\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: could not create output data\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: firmware does not have bootNonce available\n
%s::%s: NeRD OS preflight attempt...\n
%s::%s: failed to power on rose\n
%s::%s: failed to create ftab file object\n
%s::%s: no rose ticket found in response\n
%s::%s: %s\n
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: response size %zu doesn't match additional info size %u\n
%s::%s: failed to create request dict\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
%s::%s: IOReportCopyAllChannels failed\n
%s::%s: rooted override data unavailable\n
%s::%s: bad BootNonce size %zu\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: error retrieving descriptor: 0x%08x\n
%s::%s: Crash log is fatal\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: failed to reset rose\n
%s::%s: failed to push rose fw\n
%s::%s: Sent %lu %s file(s):%s\n
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: failed to retain reference to personalized firmware\n
%s::%s: Command %d not supported by restore step\n
%s::%s: Updater object created successfully\n
%s::%s: rrko bundle data unavailable\n
%s::%s: failed to set boot nonce\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: response size %zu too small for HSI1\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: invalid payload length %zu\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%s::%s: failed to allocate buffer for coredump\n
%s::%s: ping attempt #%d...\n
%s::%s: Ping success!\n
%s::%s: failed to create restore object\n
%s::%s: failed to copy firmware container\n
%s::%s: failed to query rose plugin interface\n
%s::%s: failed to parse HSI1 ping info\n
%s::%s: failed to initialize base class\n
%s::%s: failed to get target\n
%s::%s: failed to create path\n
%s::%s: icnf firmware is missing\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: failed to init ftab file object\n
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
%s::%s: No firmware logs available to pull\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
%s::%s: Invalid cal data size\n
%s::%s: could not create device info dictionary\n
%s::%s: failed to get device info list\n
%s::%s: unexpected device info parameters\n
%s::%s: failed to init bundle firmware\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: BootNonce size: %zu\n
%s::%s: invalid coredump size: %u\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: Bad chip ID size\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: savePath: %s\n
%s::%s: error converting host chipID\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: attempt %u of %u...\n
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: Could not create RTKitFirmware\n
%s::%s: Unable to power on Rose chip\n
%s::%s: Firmware to push is missing!\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: current firmware state: %d\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: failed to set bootNonce\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: successfully collected preflight information\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: failed to push healed rose fw\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: invalid event format\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: failed to create ioReport array\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: failed to create output request dictionary\n
%s::%s: failed to convert chip rev\n
%s::%s: failed to get chip parameters post boot\n
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
%s::%s: no coredump available for core: %u\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
%s::%s: Pulling firmware logs...\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
%s::%s: No updater object passed, this is fatal\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: failed to create firmware\n
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: failed to find rose service\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: no data available to send\n
%s::%s: Local sign enabled? %s\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: could not create path to unsigned firmware\n
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: failed to validate ping response\n
%s::%s: error converting host ECID\n
%s::%s: Rose target string: %s\n
%s::%s: Rose Update is complete!\n
%s::%s: Exception: %s\n
%s::%s: no firmware override specified\n
%s::%s: failed to initialize object\n
%s::%s: Booted OS preflight attempt...\n
%s::%s: failed to ping after second boot\n
%s::%s: unknown HSI version\n
%s::%s: failed to get chip rev\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: failed to create Rose CFType object\n
%s::%s: unrecognized event oid 0x%03x\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: failed to get ecid (ret: 0x%08x)\n
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: message is not an event\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
%s::%s: %s\n%@
%s::%s: boot nonce hash size: %zu\n
%s::%s: hardware not supported\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: resetting chip\n
%s::%s: additional info size %u too small for HSI1\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: failed to compute host identifier\n
%s::%s: failed to query chip\n
%s::%s: could not create save path url\n
%s::%s: group pruning failed\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: could not open healed rose firmware\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: There is a crash log available!\n
%s::%s: error getting host ECID\n
%s::%s: failed to allocate override options\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: Applied reset glitch workaround successfully\n
%s::%s: failed to init framework operation\n
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: failed to open unsigned rose firmware\n
%s::%s: failed to get power state\n
%s::%s: invalid or no firmware file present in restore options\n
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: Failed to collect preflight info\n
%s::%s: Restore boot nonce present!\n
%s::%s: failed to get chip parameters pre boot\n
%s::%s: skipping firmware save action!\n
%s::%s: bad input event\n
%s::%s: successfully triggered fatal crashlog\n
%s::%s: Calibration file transfer success: %s!\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: Failed to initialize base object\n
%s::%s: failed to get boot-nonce\n
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: unexpected debug log path type\n
%s::%s: Logging files under %s\n
%s::%s: invalid event size: %zu\n
%s::%s: failed while waiting for chip to initialize\n
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: unhandled product %lld\n
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: bad event message\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
%s::%s: Invalid response (size: %zu)\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: getDebugInfo failed\n
%s::%s: bad device info parameters\n
%s::%s: failed to create capabilities object\n
%s::%s: Identified chip as R1\n
%s::%s: bad parameter\n
%s::%s: could not get reference to data\n
%s::%s: Enabling Rose certification step\n
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
%s::%s: MGProductTypeUnknown\n
%s::%s: No device info\n
%s::%s: failed to save rose fw\n
%s::%s: bad input parameter\n
%s::%s: failed to create dispatch queue\n
%s::%s: error getting debug info: 0x%x\n
%s::%s: failed to get the Rose restore instance\n
%s::%s: failed to ping after first boot\n
%s::%s: failed to create event\n
%s::%s: bad transport object provided\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: failed to create crash long name string\n
%s::%s: failed to ping chip\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Invalid cal data reference\n
%s::%s: Unexpected subscribed channel count: %d\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
%s::%s: No chip ID\n
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: Performing Rose preflight...\n
%s::%s: Could not create RoseTransport\n
%s::%s: failed to set dispatch queue: 0x%x\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: Error sending FDR blob identification\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: Cleaning up restore object\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: failed to create capabilities\n
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: no AP ticket in updater options\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: failed to create host object\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: failed to create crash syncher\n
%s::%s: %d IOReport Channels found\n
%s::%s: Finished sending %s, waiting for result\n
%s::%s: dropping event\n
%s::%s: Failed to perform certification step (ret: %d)\n
%s::%s: failed to create healed firwmare URL\n
%s::%s: Identified chip as R2\n
%s::%s: Invalid cal data parameter\n
%s::%s: nonce is of unexpected size\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
%s::%s: failed to create rose tss request dictionary\n
%s::%s: failed to init base\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
%s::%s: No Channels found\n
%s::%s: failed to allocate dict\n
%s::%s: chip reset successful\n
%s::%s: failed to get chipId (ret: 0x%08x)\n
%s::%s: %u bytes of firmware logs pulled\n
%s::%s: setPowerState (%d) successful\n
%s::%s: Error setting cal payload length to %lu\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: IOReportCreateSamples failed\n
%s::%s: Timed out on cal file transfer\n
%s::%s: failed to send calibration\n
%s::%s: error getting host chipID\n
%s::%s: failed to copy unsigned firmware path\n
%s::%s: Bad options\n
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: failed to create Rose CFRuntimeClass\n
%s::%s: could not create libauthinstall object\n
%s::%s: failed to allocate event\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: drained %zu bytes of firmware logs\n
%s::%s: Invalid refcon crash callback\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: failed to collect preflight information\n
%s::%s: failed to create event syncher\n
%s::%s: no diagnostics object provided\n
%s::%s: failed to open framework\n
%s::%s: failed to initialize update operations\n
%s::%s: failed to init certification firmware\n
%s::%s: could not create rose transport\n
%s::%s: could not create restore dictionary\n
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: %d crash logs pulled for core: %d\n
%s::%s: failed to reset chip: 0x%08x\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: Command:\n
%s::%s: Response:\n
%s::%s: failed to init logging\n
%s::%s: Failed to execute command %d\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: failed to set log sink: 0x%x\n
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
%s::%s: descriptor is null\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
%s::%s: Initializing RoseRestore for preflight\n
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: could create coredump filename string\n
%s::%s: crash event timeout\n
%s::%s: invalid debugInfoDict\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: RoseRestore object doesn't exist\n
%s::%s: Error in event: status 0x%x\n
%s::%s: failed to allocate buffer for firmware logs\n
%s::%s: failed to create a dictionary\n
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: bad input parameters\n
%s::%s: AP ticket has wrong type\n
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: crashLogSize is too small\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
BuildIdentity
%s::%s: bad input event\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x)\n
%s::%s: setPowerState (%d) failed: 0x%08x\n
%s::%s: Invalid cal data reference\n
%s::%s: error converting host chipID\n
%s::%s: crashLogSize is too small\n
collectIOReport_block_invoke
%s::%s: Initializing RoseRestore for preflight\n
r1hp2
failed to create Rose CFType object
%s::%s: Rose Update is complete!\n
%s::%s: firmware log collection isn't supported for this chip\n
%s::%s: Parsing error while extracting the crash string reason. crashlog size: %zu offset and section size: %lu\n
%s::%s: failed to create data payload (ret: 0x%08x)\n
Rose
copyFirmware: rrko bundle data unavailable
rose
%s::%s: Failed to execute command %d\n
%s::%s: failed to get boot nonce hash 2nd time (ret: 0x%08x)\n
%s::%s: error while trying to read the coredump 0x%x\n
%s::%s: Crash log is fatal\n
failed to init logging
copyFirmware: could not create output data
getBoardParameters
%s::%s: error while trying to dequeue firmware logs (ret: 0x%08x)\n
copyUnsignedFirmwarePath
%s::%s: Failed to send FDR files (ret: %d)\n
%s::%s: Performing Rose preflight...\n
%s::%s: could not create save path url\n
%@.log
RoseRestore
copyFirmwareUpdater
%s::%s: failed to create path\n
%s::%s: could not create restore dictionary\n
%s::%s: Manifest for firmware is missing!\n
%s::%s: flushed a crash log of size: %zu for core: %d\n
%s::%s: failed to get debug info  (ret: 0x%08x)\n
%s::%s: failed to query chip\n
RoseRestore object doesn't exist
copyFirmware: could not get 'rrko' object from ftab
%s::%s: Identified chip as R2\n
Rap,SecurityDomain
%s::%s: failed to get target\n
%s::%s: failed to register event callback: 0x%x\n
%s::%s: IOReportSampleCopyDescription() failed\n
%s::%s: failed to allocate dict\n
%s::%s: Invalid cal data size\n
%s::%s: failed to initialize base class\n
copyFirmwareUpdater: bad device info parameters
%s::%s: invalid payload length %zu\n
%s::%s: RoseRestore object doesn't exist, this is fatal\n
RoseUpdater
create
%s::%s: failed to get boot-nonce\n
%s::%s: could not open healed rose firmware\n
Trusted
copyCalDataToSend
%s::%s: AP ticket has wrong type\n
%s::%s: unexpected device info parameters\n
%s::%s: failed to set boot nonce\n
eventCallback
roseControllerLogSink
%s::%s: failed to init framework operation\n
%s::%s: error getting host chipID\n
RoseCapabilities
%s::%s: Error flushing the debug logs: (%d)\n
%s::%s: unhandled product %lld\n
%s::%s: Checking for crash logs for core: %d\n
%s::%s: %d crash logs pulled for core: %d\n
Rap,SecurityMode
%s::%s: bad device info parameters\n
%s::%s: failed to initialize LAI lib create function\n
%s::%s: Status 0x%x, Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
combined
%s::%s: bad transport object provided\n
%s::%s: No firmware logs available to pull\n
%s::%s: failed to read RosePowerState value from the dictionary\n
%s::%s: No certification URL found for certification step (ret: %d)\n
%s::%s: failed to copy unsigned firmware path\n
%s::%s: failed to copy firmware container\n
%s::%s: bad parameter\n
%s::%s: failed to allocate buffer for crash log\n
%s::%s: failed to ping chip\n
%s::%s: failed to push rose fw\n
%s::%s: failed to dequeue crash logs (ret: 0x%08x) for core: %d\n
%s::%s: failed to apply reset glitch workaround, proceeding with reset anyway\n
%s::%s: setPowerState (%d) successful\n
rMC2
%s::%s: Sent %lu %s file(s):%s\n
Rap,MinEpoch
Failed to collect preflight info
%s::%s: failed to ping after first boot\n
/usr/standalone/firmware/Rose
%s::%s: failed to open unsigned rose firmware\n
%s::%s: failed to allocate buffer for firmware logs\n
 
%s::%s: failed to create event syncher\n
RoseService
queryCmd
%s::%s: failed to create Rose CFRuntimeClass\n
rMNB
%s::%s: failed to resume the firmware logs (ret: 0x%08x)\n
%s::%s: unrecognized event oid 0x%03x\n
getRoseDebugInfoDict
%s::%s: Ping success!\n
%s::%s: chip query attempt %u of %u...\n
%s::%s: failed to create dispatch queue\n
%s::%s: failed to resume firmware logging (ret: 0x%08x)\n
%s::%s: unsupported sikblobtype: %u\n
%s::%s: unexpected debug log path type\n
r1p1
%s::%s: failed to create Rose CFType object\n
%s::%s: failed to power on rose\n
%s::%s: failed to open healed firmware file (status: %d)\n
%s::%s: Unrecognized chipID 0x%x\n
%s::%s: failed to parse HSI1 ping info\n
%s::%s: Incomplete parameter set for certification (ret: %d)\n
%s::%s: failed to init logging\n
%s::%s: subscribed channel count: %d less than desired channel count: %d\n
%s::%s: Error sending cal data: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
createRestoreDictionary
%s::%s: bad boot nonce hash size 1st time: %zu\n
%s::%s: RoseUpdater Version: %s\n
%s::%s: invalid event size: %zu\n
%s::%s: Calibration file transfer success: %s!\n
performCmd
%s::%s: Could not create RTKitFirmware\n
copyFirmware: failed to init bundle firmware
RoseRestoreHost
%s::%s: failed to create healed firwmare URL\n
rSCl
%s::%s: SetHostBootNonce failed with error (ret: 0x%08x)\n
%s::%s: Timed out on cal file transfer\n
%s::%s: failed to get device info list\n
rcrt
%s::%s: failed to create restore object\n
%s::%s: failed to initialize update operations\n
%s::%s: failed to create request dict\n
getBootNonceHash
%s::%s: IOReportCreateSamples failed\n
%s::%s: failed to save rose fw\n
%s::%s: skipping firmware save action!\n
%s::%s: failed to reset chip: 0x%08x\n
RoseRestoreObjDestroy
%s::%s: failed to init ftab file object\n
%s::%s: failed to push healed rose fw\n
%s::%s: Pulling firmware logs...\n
RoseBootstrappedPreflight
%s::%s: failed to get production mode (ret: 0x%08x) prodMode: 0x%x\n
ChipID
%s::%s: rrko bundle data unavailable\n
%s::%s: Contents: status: 0x%02x\n
%s::%s: invalid coredump size: %u\n
reset
failed to get the Rose restore instance
Rap,RTKitOS
Rap,ProductionMode
AMAuthInstallCreate
%s::%s: failed to create firmware\n
NULL
%s::%s: failed to set log sink: 0x%x\n
%s::%s: Unexpected subscribed channel count: %d\n
combinedFDRObjects
Rap,BoardID
%s::%s: There is a crash log available!\n
%s::%s: Reserved (%lu bytes):\n
%s::%s: boot nonce hash is all zero (%zu bytes) after successful nonce generation\n
%s::%s: Firmware to push is missing!\n
%s::%s: failed to create ioReport array\n
%s::%s: no AP ticket in updater options\n
%s::%s: failed to retain reference to personalized firmware\n
%s::%s: invalid or no firmware file present in restore options\n
flushDebugInfo
%s::%s: getDebugInfo failed\n
RoseUpdaterCreate
Rap,Nonce
/usr/standalone/firmware/Rose/%@/ftab.bin
Rap,ChipID
%s::%s: failed to get chip parameters pre boot\n
%s::%s: could not initialize firmware object\n
%s::%s: Skipping %s because its parent %s has already been sent\n
%s::%s: MGProductTypeUnknown\n
%s::%s: Restore boot nonce present!\n
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
copyFirmware: rooted override data unavailable
%s::%s: could not get 'rrko' object from ftab\n
%s::%s: failed to get minimum epoch (ret: 0x%08x)\n
triggerCrashLog
%s::%s: invalid debugInfoDict\n
runCertification
outData
%s::%s: crash event timeout\n
-
%s::%s: RoseRestore object doesn't exist\n
operator()
%s::%s: failed to satisfy prerequisites to flush debug info (ret: 0x%08x)\n
%s::%s: chip reset successful\n
%s::%s: failed to get boardId (ret: 0x%08x)\n
%s::%s: Could not create RoseTransport\n
Rap,FDRAllowUnsealed
%s::%s: no rose ticket found in response\n
%s::%s: Boot mode failed to update: expected 0x%x, found 0x%x\n
%s::%s: Crash string section version mismatch. Expected: 0x%x Version in Crashlog: 0x%x\n
failed to create Rose CFRuntimeClass
%s::%s: failed to get ticket for rose (laiStatus: %d)\n
crashHandler
%s::%s: failed to create a dictionary\n
%s::%s: Bad options\n
%s::%s: could not create device info dictionary\n
%s::%s: IOReportCopyAllChannels failed\n
%s::%s: failed to parse HSI2 ping info\n
%s::%s: Failed to initialize restore object (%d)\n
%s::%s: bundle cert firmware doesn't have 'rrko'\n
%s::%s: could not create ACFU diagnostics\n
%s::%s: Exception: %s\n
raw
%s::%s: failed to find rose service\n
%s::%s: icnf firmware is missing\n
r2p1
getRoseTarget
%s::%s: failed to generate a boot nonce (ret: 0x%08x)\n
%s::%s: %zu bytes of crash logs to be pulled...\n
%@-raw.bin
%s::%s: Invalid refcon crash callback\n
r1p2
@Rap,Ticket
vector
R1
RosePowerState
RoseTransport
%s::%s: overriding combined FDR objects to %s due to debug-arg: %u\n
%s::%s: rkos bundle data unavailable\n
%s::%s: failed to open libauthinstall dylib\n
%s::%s: failed to allocate event\n
sendCalibration
%s::%s: descriptor is null\n
%s::%s: failed to convert chip rev\n
%s::%s: Error status (0x%04x) in response\n
%s::%s: failed to add firmware logs to diagnostics\n
%s::%s: Attempting to apply reset glitch workaround\n
%s::%s: No chip ID\n
Rap,RestoreBootNonce
%s::%s: failed to reset rose\n
%s::%s: failed to get chipID (ret: 0x%08x)\n
%s::%s: drained %zu bytes of firmware logs\n
FirmwareLogs
%s::%s: rooted override data unavailable\n
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x, board ID 0x%x\n
%s::%s: failed to open framework\n
setNonce
%s::%s: Firmware Version '%s', host interface version 0x%x (%u.%u), hardware version 0x%x\n
collectCoreDump
%s::%s: failed to allocate buffer for coredump\n
%s::%s: IOReportCreateSubscription failed\n
%s::%s: current firmware state: %d\n
v8@?0
%s::%s: error converting host ECID\n
AP-CrashLog
%s::%s: No device info\n
%s::%s: error while trying to trigger a crashlog: 0x%x\n
%s::%s: Updater object created successfully\n
RoseCommand
%s::%s: failed to get ecid (ret: 0x%08x)\n
collectIOReport
DSP-CoreDump
%s::%s: personalization attempt %u of %u...\n
%s::%s: bad input parameter\n
%s::%s: failed to get secure mode (ret: 0x%08x) secMode: 0x%x\n
%s::%s: Invalid command length (%lu) for hello packet\n
%s::%s: Failed to apply reset glitch workaround\n
%s::%s: invalid event format\n
%s::%s: group pruning failed\n
copyFirmware: bundle firmware specified is invalid
copyFirmware: could not add 'rrko' object to final ftab
bootstrappedPreflight
collectFirmwareLogs
%s::%s: response size %zu too small for HSI1\n
%s::%s: Finished sending %s, waiting for result\n
map::at:  key not found
parsePingResponse
%s::%s: Failed to get a restore mount point to create FW object with\n
%s::%s: Enabling Rose certification step\n
r1p0
%s::%s: No updater object passed, this is fatal\n
Rap,ECID
%s::%s: failed to get power state\n
%s::%s: dropping event\n
Rap,RTKitIOConfig
FirmwareData
createRoseController
%s::%s: failed to create output request dictionary\n
%s::%s: failed to get security domain (ret: 0x%08x)\n
%s::%s: Crashlog Reason: \"%s\"\n
%s::%s: coredump size mismatch, receivedSize %zu, expected size %u\n
/usr/standalone/firmware/Rose/
Firmware File Dictionary: 
%s::%s: UWB_AP version 0x%x, UWB_DSP version 0x%x, target '%s', cal data version 0x%x, module ID 0x%x, modem init version 0x%x\n
%s::%s: Rose chip is powered off. Powering it back on.\n
%s::%s: Unable to power on Rose chip\n
%s::%s: no diagnostics object provided\n
%s::%s: Command:\n
%s::%s: Bad chip ID size\n
init
%s::%s: Invalid response (size: %zu)\n
%s::%s: failed to collect preflight information\n
RoseRestoreObj
%s::%s: failed to create rose tss request dictionary\n
logDirectoryContents
AMAuthInstallRequestSendSync
%s::%s: failed to get bootMode (ret: 0x%08x) (bootMode: 0x%x)\n
%s::%s: firmware does not have bootNonce available\n
%s::%s: Cleaning up restore object\n
%s::%s: failed to init bundle firmware\n
%s::%s: copyfirmware: ICNF missing in bundle firmware\n
%s::%s: failed to get chip rev\n
%s::%s: %s\n
%s::%s: failed to get event data\n
DeviceInfo
%s::%s: could not create path to unsigned firmware\n
%s::%s: Unable to get the current Rose chip power state\n
collectCrashLogs
%s::%s: failed to allocate override options\n
copyFirmware: bundle cert firmware doesn't have rrko
%s::%s: could not get reference to data\n
No
copyFirmware: rkos bundle data unavailable
%s::%s: Logging files under %s\n
RoseCalibration
%s::%s: failed to get chip revision (ret: 0x%08x)\n
%s::%s: failed to init restore option dictionaries\n
%s::%s: failed to create crash syncher\n
pushFirmware
%s::%s: error getting debug info: 0x%x\n
%s::%s: response size %zu too small for HSI2\n
%s::%s: Local sign enabled? %s\n
%s::%s: failed to initialize object\n
%s::%s: Identified chip as R1\n
%s::%s: Response:\n
%s::%s: response size %zu doesn't match additional info size %u\n
%s::%s: security mode demotion disallowed for Rose\n
%s::%s: pausing firmware logs failed (ret: 0x%08x)\n
r2p0
%s::%s: failed to create capabilities\n
%s::%s: dequeued more logs than we have room for (%zu > %zu)\n
isCrashLogAvailable
%s::%s: Coredump Descriptor: log_id (%llu), size (%u), core_type (%u), log_type (%u), is_corrupted (%u)\n
copyFirmwareUpdater: failed to get device info list
UNDEF
%s::%s: Content: status: 0x%04x, trustEvaluationError: 0x%016llx\n
%s::%s: failed to get rose driver: 0x%x\n
%s::%s: DownloadCustomFirmware failed with error (ret: 0x%08x)\n
%s::%s: error retrieving descriptor: 0x%08x\n
%s::%s: failed to apply reset glitch workaround, proceeding with power off anyway\n
AP-CoreDump
%s::%s: failed to create ftab file object\n
%s::%s: failed to query rose plugin interface\n
optionsOverride: 
%s::%s: failed to send calibration\n
r1hp1
/usr/lib/libauthinstall.dylib
%s::%s: no data available to send\n
DebugLogPath
%s::%s: %d IOReport Channels found\n
r2w2
%s::%s: could not create output data\n
parsePingInfo
%s::%s: Invalid header: received gid 0x%02x oid 0x%03x msg type 0x%02x; expected gid 0x%02x oid 0x%03x msg type 0x%02x\n
%s::%s: RosePowerState isn't present in the dictionary\n
%s::%s: Invalid cal data parameter\n
%s::%s: %s segment #%u of %u: segmentLength %u bytesRemaining %u\n
%s::%s: failed to collect the SiK CSR (ret: 0x%08x)\n
UwbB
%s::%s: Error in event: expectedCompleteEvent 0x%02x status 0x%x\n
%s::%s: Content: status: 0x%02x, completedCmdOid: 0x%03x, debugData: 0x%02x\n
%s::%s: Booted OS preflight attempt...\n
Rap,SoftwareBinaryDsp1
%s::%s: failed to get chip parameters post boot\n
Incomplete parameter set for certification
RoseControllerState
%s::%s: attempt %u of %u...\n
%s::%s: bundle firmware specified is invalid\n
%s::%s: no firmware nonce present to boot with\n
%s::%s: failed to create host object\n
%s::%s: Error in event: status 0x%x\n
%s::%s: failed while waiting for chip to initialize\n
i16@?0^{__CFDictionary=}8
waitForFatalCrashCB
RoseTransport-v1
%s::%s: unknown HSI version\n
%s::%s: failed to validate ping response\n
%s::%s: failed to get the Rose restore instance\n
copyFirmware: failed to init ftab file object
%s::%s: successfully collected preflight information\n
r2w0
%s::%s: Unrecognized event/size: gid: 0x%02x oid: 0x%03x msg type: 0x%02x size: %zu\n
DSP-CrashLog
Rap,ChipRev
%s::%s: failed to set bootNonce\n
%s::%s: Failed to initialize base object\n
copyFirmwareUpdater: nonce is of unexpected size
%s::%s: could not create libauthinstall object\n
RoseQueue
isCoreDumpAvailable
%s::%s: failed to ping after second boot\n
%s::%s: No Channels found\n
%s::%s: Error setting cal payload length to %lu\n
::
PRGetPreflightInfo
%s::%s: message is not an event\n
pingCheck
%s::%s: nonce is of unexpected size\n
%s::%s: failed to set dispatch queue: 0x%x\n
getPowerState
%s::%s: failed to compute host identifier\n
Rap,FdrRootCaDigest
copyFirmwareUpdater: unexpected device info parameters
%s::%s: IOReportIterate retVal: 0x%x\n
%s::%s: bad event message\n
IOService
%s::%s: bad boot nonce hash size 2nd time: %zu\n
%s::%s: %u bytes of firmware logs pulled\n
applyResetGlitchWorkaround
APTicket
/System/Library/PrivateFrameworks/Proximity.framework/Proximity
rMUB
%s::%s: error while trying to dequeue FirwmareCrashLogs (ret: 0x%8x)\n
%s::%s: Failed to collect preflight info\n
Failed to perform certification step
getRoseTarget_block_invoke
%s::%s: failed to dequeue firmware logs (ret: 0x%08x)\n
%s::%s: invalid refcon in rose event callback\n
%s::%s: error getting host ECID\n
RoseTargetMap
%s::%s: boot nonce hash size: %zu\n
%s::%s: failed to perform command: 0x%08x\n
%s::%s: bad input parameters\n
UniqueChipID
rMCl
%s::%s: creating rose plugin interface failed: 0x%x\n
%s::%s: resetting chip\n
setPowerState
%s::%s: Applied reset glitch workaround successfully\n
RoseUpdaterIsDone
%s::%s: failed to get chipId (ret: 0x%08x)\n
%@-%d.bin
basic_string
copyFirmware: failed to init certification firmware
%s::%s: could not create rose transport\n
%s::%s: invalid crashlog of size: %zu\n
%s::%s: Error sending FDR blob identification\n
r1p3
%s::%s: savePath: %s\n
%s::%s: could create coredump filename string\n
%s::%s: Command %d not supported by restore step\n
RoseUpdaterExecCommand
%s::%s: BootNonce size: %zu\n
%s::%s: failed to get firmware state (ret: 0x%08x)\n
%s::%s: NeRD OS preflight attempt...\n
ftab.bin
%s::%s: Error in event: status 0x%04x, trustEvaluationError 0x%016llx\n
%s::%s: additional info size %u too small for HSI1\n
validateResponse
%s::%s: failed to create crash long name string\n
%s::%s: Collecting coredump for core: %d\n
sendRoseCommand
Yes
%s::%s: Rose target string: %s\n
validate
%@.bin
crashCallback
%s::%s: failed to get boot nonce hash 1st time (ret: 0x%08x)\n
%s::%s: could not add 'rrko' object to final ftab\n
%s::%s: failed to intialialize LAI lib server sync function\n
%s::%s: failed to create capabilities object\n
%s::%s: failed to create event\n
%s::%s: failed to init base\n
log
%s::%s: Header: gid: 0x%02x, oid: 0x%03x, msgType: 0x%02x\n
Rap,Ticket
createRequest
RoseEvent
%s::%s: Extra additional info we don't know how to parse (%lu bytes):\n
%s::%s: bad BootNonce size %zu\n
RoseIOReport
%s::%s: failed to perform command with timeout: 0x%08x\n
%s::%s: failed to create command\n
%s::%s: crashLog size mismatch, expected: %zu, received: %zu\n
gatherPreflightParameters
%s::%s: Dequeued crashLog: log_id (%llu), core_type (%u), log_type (%u), is_corrupted (%u)\n
getDebugInfo
%s::%s: booted chip query attempt %u of %u...\n
%s::%s: DownloadCustomFirmwareExt failed with error (ret: 0x%08x)\n
logCrashLogReason
%s::%s: successfully triggered fatal crashlog\n
sendCalibration_block_invoke
No certification URL found for certification step
%s::%s: Failed to perform certification step (ret: %d)\n
createRoseRequest
R2
%s::%s: no coredump available for core: %u\n
r1hp0
Rap,RestoreRTKitOS
%s::%s: failed to register crash callback: 0x%x\n
%s::%s: failed to get boot nonce (ret: 0x%08x)\n
%s::%s: hardware not supported\n
%s::%s: failed to set bootMode (ret: 0x%08x)\n
%s::%s: ping attempt #%d...\n
%s::%s: no firmware override specified\n
%s::%s: crashlog section is too small. Section signature: 0x%x version: 0x%x size: %d\n
<RoseRestoreObj %p [%p]>{}
LocalSigningID
%s::%s: failed to init certification firmware\n
```
