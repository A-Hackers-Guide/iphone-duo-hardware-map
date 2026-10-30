# `/usr/lib/libKTLDynamic.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 417,232 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 2656)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libKTLDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libARI.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (437)

```
KTLCddGetDebugLog
%s%s%s.%s
Failed IBIFilerHSStartReadBBSessionReq\n
TraceFlush
KTLGetSimSlotInstance
KTLGetPersonalizationInfo
Failed CsiSecCollectScrtBlobReq\n
KTLMonMemoryStatus
KTLBspIceAtString_block_invoke
KTLGetSimTrayStatusParseAndRelease
Returned Instance is %d while expecting instance is %d\n
KTLGetIPCLogBufferList_block_invoke
VinylCommandDriver FinalizePerso perform failure
ResetSimCard
Failed IBINvmSnapshotReq\n
Failed after checking of core dump lists:\n
KTLSetAntennaPort
GetRandomNum
Read response from PSI: code = %u\n
Command driver with ariId=%d failed to deregister indication: %s (%u, 0x%x)
00499901064000
KTLPSIReadMrcResponse
Rcvd Packet of type %u (%s), length %u\n
Failed CsiGetCurrentBootStateRspCb\n
GetReadSize
Failed to send PSI command\n
KTLPSISendMrcTrainingCommand
Invalid transport option selected.  See previous error.  Abort!\n
sKTLPacketCopyReceiveData
Failed receive of remaining packet bytes (expected=%u, actual=%u)\n
KTLTriggerDelayedResponse
KTLCpsPriWrite
ret=%d list size=%lu\n
Error on the result: %d\n
KTLGetIMEIInfo
GetNvItemsSetting
KTLCpsPriWriteParseAndRelease
TelephonyUtilTransportCreateWithFD: %s (filedesc=%d)\n
KTLNVMSendUpdateAck
KTLCDSendEndCoredumpCommand
KTLPSIReadResponse
Partial message discarded.  Failed to receive remaining %u bytes\n
sFetchMessageRemainder
KTLGetIPCLogBuffer
KTLNVMSendDeregister
These parameters cannot be NULL: opt: %p, antennaPort: %p\n
Error: one of given parameter got null. ( pkt: %p, fname: %p, offset: %p, length: %p )\n
Failed to send the message of IBIPriWriteReq_V2.\n
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
KTLNVMReadGroupStart
Parameters are not correct: opt: %p, filerID: %p\n
Failed reading response from PSI: bytesRead = %u\n
Error: ICE_FILER_write. Failed ARI_EXTRACT (Remaining=%d/%d)\n
Failed IBIFilerHSWriteBBReq\n
[ind] IQ trace stop complete indication has fill level %u
Treating BB as single-SIM. Using default SIM stack mapping in KTL.\n
KTLSecGetRandomNum
Enhanced
Error: Failed ARI_EXTRACT on copyReceiveData (Remaining=%d/%d)\n
Failed to send the message of CsiBmmProvideBootTimeInfoReq.\n
PRI signature size (%u) larger than max allowed (%d)
error while trying to get response from device \n
GetBBIPCLogs
StreamFW
VinylCommandDriver GetHwIdSimConfig perform failure
simSlot parameter: %d is >= KTL max number of supported SIMs: %d\n
Error: CsiFpUpdateAckRsp Failure (%s)\n
driver IF not available
driver timeout
VinylCommandDriver Reset Sim Card failure
KTLSecGetSNUM
Packet read < Minimum size (%d < %ld)\n
KTLEFISendData
misc
registerIndication_block_invoke
Failed to send the message of CsiIceGetTxAntennaReq.\n
These parameters cannot be NULL: opt: %p, rxDiversity: %p\n
NACK Received\n
BadEEPROM
Received additional bytes %u, expected %u, additional %u\n
KTLBspSetNvItemsToState
ktl
%s/%s.bin
GetVinylType
VinylCommandDriver StreamFW perform failure
FinalizePerso
%s is not an indication, not registering it
KTLBspSetApWakeInterval
Failed to send message IBIMSimGetSimStackMappingReq.\n
VinylCommandDriver SwitchCardMode perform failure
Command driver with ariId=%d deregistering for indication: %s (%u, 0x%x)
Error: packet malformed, payload too large for StartInfo.\n
Error: ICE_FILER_write. Context Already Exists.\n
Success\n
Embedded null found in AT response at buffer offset %u\n
Failed IBIFilerHSStartWriteBBSessionReq\n
WriteFileToBB
GetBBWakeReason
ari
param out of range
Failed to allocate packet memory\n
Error: TelephonyUtilTransportRead (ret=%d, available=%d, read=%d).\n
Failed initial receive\n
KTLBmmProvideBootTimeInfo
basic_string
com.apple.telephony.bb
Success
expected gmid %d, doesn't match response gmid %d \n
GetIMEIInfo
KTLNVMSendRegister
KTLNVMSendGetStatus
Sending %u bytes to device timeout=%u\n
ICE_FILER_read
i20@?0*8I16
Perform trace flush
Received IQ trace stop complete indication
NVMSnapshot
Failed to get response!\n
Secure
Error: ICE_FILER_write. Invalid Parameter.\n
Error: IceFilerWriteRspCb. Failure from Baseband.\n
blockRet=%d blockCtxId=%d\n
GetEid
/AppleInternal/Library/BuildRoots/4~CatVugAVHlPmCykG3u5RYNuSUaO3iPS0fZcrWSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
KTLCDSendStartCoredumpCommand
Failed to send the message of CsiIceSetTxAntennaReq.\n
Response in error. response->instance_t1: %d ( expecting nInstance: %d ), response->result_t2: %d ( expecting %d ), \n
KTLSecGetPkHash
Packet read too large (%d > %d) - Internal Error.\n
KTLGetIPCLogBuffer: %s\n
VinylCommandDriver GetVinylType perform failure
ValidatePerso
GetEuuidRequest
KTLNVMReadGroupBlock
cmd called in wrong state
KTLParsePSIRunning
KTLBmmProvideBootTimeInfoParseAndRelease
[ind] IQ trace stop complete indication success
VinylCommandDriver LPASigning Request failure
Command driver with ariId=%d failed to register indication: %s (%u, 0x%x)
KTLGetRxDiversity
Failed CsiSysGetInfoRspCbV2\n
Failed IBIBbPowerSocSleepStatsRspCb\n
InstallVad
KTLStartProvision
maxLen( %u ) is less than sizeof command ( %lu )\n
Sending PSI enhanced command: command %d, param %d, length = %u\n
\r\nOK\r\n
Error: IceFilerReadRspCb. Uta Failure from Baseband.\n
Failed to send the message of IBISimTrayStatusReq.\n
%c%d%c
[ind] Trace flush complete indication success
Successfully flushed trace
listenForIQStopCompleteInd
Fetching log buffer entry: filename=\"%s\" size=%d level=%d next=%d buf_p=%d\n
Failed to send request.\n
Normal
Receved message of size %u, but caller provided buffer size %u\n
Error: TelephonyUtilTransportWrite (ret=%d, available=%d, written=%d).\n
[%s:%u] %s\n%s\n
..
TraceConfig
GetHwIdSimConfig
VinylCommandDriver InitPerso perform failure
Error: CsiBspNvmReadGroupRespCb Failure\n
These parameters cannot be NULL: opt: %p\n
Failed to setup CsiIceRFFilerWriteReq\n
Timeout while waiting for trace flush indication
cmd format invalid
internal error
Failed CsiSecGetRandomNumReq\n
Error: packet id mismatch (expected=%d (%s), got=%d (%s))\n
KTLInitOptions
Error: ICE_FILER_read. Failed copyReceiveData (Remaining=%d/%d)\n
KTLCddGetParamDump
CsiSecCollectScrtBlob
Error: ICE_FILER_read. Invalid Parameter.\n
KTLPing
KTLBspGetCalibrationStatus
KTLGetSimCardPresence
Failed IBIPriWriteReq_V3\n
Skipping potentially dangerous filename \"%s\"\n
Filer ID: %d (0x%x)\n
Invalid buffer size(s) returned from baseband:\nnonce(%u)\tnonce_max(%u)\nsnum(%u)\tsnum_max(%u)\npkhash(%u)\tpkhash_max(%u)\n
KTLBspDebugJtagMode
KTLPingParseAndRelease
KTLGetCurrentBootStateParseAndRelease
KTLGetFactGetTestReadyStateParseAndRelease
_
KTLGetIPCLogBufferList
ManagePairing
registerIndication
driver error
Error: packet malformed, payload too small for Done.\n
EFI receive expected AT response (%u) but found (%u)\n
KTLSahGetCrashReport
kdm
PriWrite
KTLGetIPCLogBuffer_block_invoke
Successful Read response from PSI,bytesRead = %u\n
DoneAck
Unknown-type
Sending command of length %u, type %u\n
Provide either transport or ARI id, not both\n
KTLBspIceAtString
KTLIsBBSimStackMappingEnabledParseAndRelease
[ind] Got unexpected message 0x%0x, expected trace flush complete indication (0x%0x)
send
KTLGetSimSlotMapping
BB internal SIM slot -> stack instance mapping disabled. Retrieveing SIM stack mapping from BB.\n.
Could not find ARI magic in additional bytes.  Discarding...\n
Receive Data failed.\n
ReadFileFromBB
v8@?0
VinylCommandDriver DeleteProfile perform failure
Failed request\n
Error: CsiFpRegisterRsp Failure (%s)\n
PSI is running in %s mode\n
System Information Parameter is missing.\n
Failed to send the message of CsiMsCpsReadImeiReq.\n
Failed to copy received data.\n
GetData
error sending\n
KTLCDProcessCoredumpEntry
Failed to send command\n
Failed FactoryGetNvItemsSettingRspCb\n
StartReadSession
opt(%p) or filerId(%p) is NULL\n
PRI/GRI Command Result: %d\n
CsiSecReadSikPKey
ICE_FILER_transport_read
fetchARIMsgFromTransport
Failed to send message CsiMSimGetSimStackMappingStatusReq.\n
GetCurrentBootState
Failed IBIFilerHSReadBBGetSizeReq\n
VinylCommandDriver ValidatePerso perform failure
SwTrap
GSMA
Failed to read coredump list table\n
StartAck
KTLEBLSendPacket
ICE_FILER_write
Linked additional ARI message (%u-0x%x) %u bytes i=%u\n
VinylCommandDriver AuthPerso perform failure
KTLGetAntennaPortParseAndRelease
KTLGetSimStackMappingParseAndRelease
Command driver with ariId=%d registering for indication: %s (%u, 0x%x)
%s is not an indication, not deregistering it
00000000000000
KTLNVMSendSnapshot
KTLSecGetFactoryDebugEnabled
Error: IceFilerReadRspCb. ARI Context ID %x not on Lookup Table.\n
SysGetInfoV2
recv
LpaSigningRequest
VinylCommandDriver Euuid Request failure
%s indication received but no indication handler exists
Read failed. success = %u, read %u of %u\n
KTLSecGetChipId
Failed CsiSecReadSikPKeyReq\n
Error: packet malformed, payload too small for Readfile.\n
ICE_FILER_read: %s (return code=%d)\n
Flushing trace
DeleteProfile
KTLEBLParseReadfileExt
Error: packet malformed, payload too large for Done.\n
Unrecognized message type.\n
\r\nERROR\r\n
Error: %s. Invalid Parameter.\n
Failed to run TraceSetConfigReq\n
read byte (%u) is less than the dump list size (%lu) or more than maxlen(%u)\n
Not enough space left to append \\r\\n to AT string.\n
Error: ICE_FILER_write. Failed copyReceiveData\n
ICE_FILER_transport_write
KTLBspShutdown
Unexpected status while waiting for trace flush indication
success
Pulling next message from backlog\n
Have %u bytes, expect %u more...
listenForIQStopCompleteInd_block_invoke
Command driver with ariId=%d successfully registered for indication: %s (%u, 0x%x)
driver not supported
Packet read failed.\n
KTLEBLParseStartInfo
KTLOpenChannel
File Open: %s (name=\"%s\" descriptor=%d)\n
KTLAudioEnableHWLoopback
Failed to read response\n
Start
opt(%p) or respParam(%p) is NULL\n
opt(%p) or allReady(%p) or moduleStatus(%p) is NULL\n
Failed IBIPriRefreshReq\n
Received NACK\n
Failed sending %d bytes - amount written %u\n
Failed to parse response.\n
Not supported\n
Failed IBIFilerHSReadBBReq\n
VinylCommandDriver Manage pairing failure
KTLAudioDisableHWLoopback
Read Buffer as CoreDump Header List:
KTLSecGetFusingState
Delayed response received\n
cfg
%s\n
Failed to send PSI\n
Sending PSI enhanced command: command %d, param %d\n
Coredump
KTLGetMEIDInfo
KTLGetSimTrayStatus
EndSession
KTLFinishProvision
Failed to retrieve SIM stack mapping from BB.\n
Baseband NVM sync group not enabled. Check PR settings. (UTA error = dev grep not supported)\n
Error: given filename size (%lu) is too small to copy. We need %d size.\n
KTLEBLParseDone
KTLGetSimStackMapping
TraceFlush_block_invoke
[ind] Error while unpacking trace flush complete indication
KTLSetAntennaPortParseAndRelease
GetPersonalizationParams
Skipping unexpected message (groupId=%d, msgId=0x%x) with unexpected direction (%d) and retrying receive.\n
Timeout waiting for transfer to complete\n
IceFilerWriteRspCb
KTLBspSwTrap
KTLGetIPCLogBufferList returned false\n
Trace flush indication received successfully
An error occured sending the message. (%d)\n
GetNcCfgRequest
BB internal SIM slot -> stack instance mapping enabled. Using default SIM stack mapping in KTL.\n
Apple SIM
Number of entries: %u\n
IceFilerReadRspCb
perform
KTLGetAntennaPort
%s: Failed to send (Remaining=%d/%d).  Aborting...\n
KTLTriggerDelayedResponseParseAndRelease
ret=%d\n
Error: CsiBspNvmGroupEnumListRespCb Failure\n
etb
Failed IBIFilerHSEndBBSessionReq\n
KTLCpsSetSvn
SwitchCardMode
operator=
param count mismatch
KTLSetRxDiversity
KTLEBLReceivePacket
Received trace flush indication callback
VinylCommandDriver GetData perform failure
Failed to send request (this message does not expect a response)\n
Error: CsiFpUpdateHeaderData Failure (%s)\n
Received:
ICE_FILER_write_block_invoke
PriRefresh
Failed to allocate memory for core dump lists\n
KTLRFFilePushReq_block_invoke
Readfile
Error: ICE_FILER_read. Context Already Exists.\n
KTLIsBBSimStackMappingEnabled
KTLGetCurrentBootState
GetPowerSleepStats
pkt(%p) or opt(%p) or bootState(%p) is NULL\n
Indication %s is not currently registered, no need to deregister it
KTLIsSIMSlotReady
Failed to unpack response.\n
Error: packet malformed, payload too large for Readfile.\n
KTLBspStateSet
Failed to send raw data.\n
%s.bin
Failed to flush trace
[ind] IQ trace stop complete indication has region id %d
sendRet=%d\n
Getting Baseband wake reason
KTLNVMReadGroupEnumList
Error: CsiFpGetStatusRsp Failure (%s)\n
AT string size (%u) larger than max size (%u).\n
Failure
[ind] Got unexpected message 0x%0x, expected IQ trace stop complete indication (0x%0x)
[ind] Error while unpacking IQ trace stop complete indication
Unknown sim state 0x%x\n
Version: %u\n
Missing required transaction ID: context_id=%x\n
Error: IceFilerWriteRspCb. ARI Context ID %x not on Lookup Table.\n
Malformed response\n
blockRet=%d\n
Timeout waiting for response.\n
AuthPerso
deregisterIndication
Normal SIM
function not supported
Failed GetPersonalizationParametersReq\n
KTLUTACopyReceiveData
InitPerso
VinylCommandDriver configId Request failure
vector
simSlotMapping->slot_instance_id[%lu] = %d\n
Error: CsiFpSnapshotRsp Failure (%s)\n
Chunk size cannot be zero\n
Tx:
KTLGetFactGetTestReadyState
Registering for IQ trace stop complete indication
Command driver with ariId=%d successfully deregistered for indication: %s (%u, 0x%x)
Reading response from PSI\n
opt(%p) or bootState(%p) is NULL\n
KTLGetIMEIInfoParseAndRelease
pkt(%p) or opt(%p) or allReady(%p) or moduleStatus(%p) is NULL\n
.
KTLRawSendData
StartWriteSession
Carrier bundle name length (%u) larger than max allowed (%d)
KTLGetManifestStatus
Received AT string size %u, but caller provided buffer size %u\n
Rx:
ICE_FILER_read_block_invoke
KTLBspStateGet
%s \n
%s indication received; calling indication handler
unknown SIM type
Error: CsiBspNvmReadGroupBlockRespCb Failure\n
Unknown
KTLPSISendEnhancedCommand
Reading response from PSI, maxLength = %u\n
Malformed/Incomplete Packet.  Bytes read does not match expected length from Packet header (read=%d, expected=%ld).\n
Registering for trace flush complete indication
VinylCommandDriver InstallVad perform failure
VinylCommandDriver GetEid perform failure
Failed GetRandomNum ARI command\n
Done
KTLEFIReceiveData
Error: IceFilerReadRspCb. Buffer Overflow.\n
KTLSysGetInfo
Error while receiving trace flush indication
KTLNVMReadUpdateHeader
KTLRFFilePushReq
Error: packet malformed, payload too small for StartInfo.\n
Could not find ARI magic (bufSize = %u)\n
%s
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
```
