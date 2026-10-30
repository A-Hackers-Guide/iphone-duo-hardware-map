# `/usr/lib/libKTLDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 417,232 bytes.

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
_
(%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
Read failed. success = %u, read %u of %u\n
KTLInitOptions
sFetchMessageRemainder
KTLBspGetCalibrationStatus
Failed to send raw data.\n
Failed FactoryGetNvItemsSettingRspCb\n
KTLGetFactGetTestReadyStateParseAndRelease
GetEuuidRequest
KTLGetRxDiversity
Error: ICE_FILER_write. Failed ARI_EXTRACT (Remaining=%d/%d)\n
Receive Data failed.\n
Have %u bytes, expect %u more...
Failed to send the message of CsiMsCpsReadImeiReq.\n
KTLPingParseAndRelease
VinylCommandDriver StreamFW perform failure
GSMA
KTLNVMSendDeregister
Failed CsiSecGetRandomNumReq\n
Flushing trace
[ind] IQ trace stop complete indication has fill level %u
KTLGetIPCLogBuffer_block_invoke
00499901064000
Version: %u\n
Failed to setup CsiIceRFFilerWriteReq\n
Reading response from PSI, maxLength = %u\n
System Information Parameter is missing.\n
KTLGetIPCLogBuffer
GetNcCfgRequest
Failed CsiSecReadSikPKeyReq\n
KTLPSISendMrcTrainingCommand
Invalid transport option selected.  See previous error.  Abort!\n
KTLBspIceAtString
Failed CsiGetCurrentBootStateRspCb\n
Failed to send PSI\n
AT string size (%u) larger than max size (%u).\n
Failed sending %d bytes - amount written %u\n
ICE_FILER_transport_write
[ind] IQ trace stop complete indication has region id %d
blockRet=%d\n
simSlot parameter: %d is >= KTL max number of supported SIMs: %d\n
Failed to send the message of CsiIceGetTxAntennaReq.\n
Success\n
cfg
Trace flush indication received successfully
com.apple.telephony.bb
Skipping potentially dangerous filename \"%s\"\n
ret=%d\n
VinylCommandDriver AuthPerso perform failure
Failed after checking of core dump lists:\n
Error: given filename size (%lu) is too small to copy. We need %d size.\n
Skipping unexpected message (groupId=%d, msgId=0x%x) with unexpected direction (%d) and retrying receive.\n
Received IQ trace stop complete indication
error while trying to get response from device \n
VinylCommandDriver LPASigning Request failure
deregisterIndication
Failed to send request (this message does not expect a response)\n
Read Buffer as CoreDump Header List:
KTLParsePSIRunning
KTLGetMEIDInfo
[%s:%u] %s\n%s\n
GetHwIdSimConfig
Apple SIM
KTLRFFilePushReq_block_invoke
Sending PSI enhanced command: command %d, param %d, length = %u\n
Read response from PSI: code = %u\n
ICE_FILER_transport_read
Failed to copy received data.\n
KTLCDSendStartCoredumpCommand
Received:
Linked additional ARI message (%u-0x%x) %u bytes i=%u\n
KTLTriggerDelayedResponse
Failed IBIBbPowerSocSleepStatsRspCb\n
pkt(%p) or opt(%p) or bootState(%p) is NULL\n
ReadFileFromBB
WriteFileToBB
KTLGetIPCLogBufferList_block_invoke
VinylCommandDriver GetData perform failure
Command driver with ariId=%d successfully deregistered for indication: %s (%u, 0x%x)
Getting Baseband wake reason
simSlotMapping->slot_instance_id[%lu] = %d\n
PSI is running in %s mode\n
KTLEBLSendPacket
IceFilerReadRspCb
NVMSnapshot
KTLOpenChannel
KTLBspStateGet
GetCurrentBootState
kdm
Failed IBIFilerHSStartWriteBBSessionReq\n
Failed to flush trace
VinylCommandDriver SwitchCardMode perform failure
AuthPerso
KTLPSIReadMrcResponse
KTLGetFactGetTestReadyState
Failed CsiSysGetInfoRspCbV2\n
KTLCpsPriWrite
KTLCpsPriWriteParseAndRelease
%s\n
SwTrap
KTLNVMSendUpdateAck
Failed to send request.\n
Error: packet malformed, payload too small for Done.\n
KTLEFISendData
KTLUTACopyReceiveData
KTLBspStateSet
[ind] Got unexpected message 0x%0x, expected trace flush complete indication (0x%0x)
Perform trace flush
v8@?0
VinylCommandDriver Euuid Request failure
registerIndication_block_invoke
Command driver with ariId=%d failed to deregister indication: %s (%u, 0x%x)
00000000000000
KTLIsSIMSlotReady
KTLNVMReadUpdateHeader
Response in error. response->instance_t1: %d ( expecting nInstance: %d ), response->result_t2: %d ( expecting %d ), \n
\r\nOK\r\n
ICE_FILER_read_block_invoke
Failed to send the message of CsiBmmProvideBootTimeInfoReq.\n
KTLGetCurrentBootState
.
i20@?0*8I16
ResetSimCard
StartAck
Sending %u bytes to device timeout=%u\n
Partial message discarded.  Failed to receive remaining %u bytes\n
opt(%p) or allReady(%p) or moduleStatus(%p) is NULL\n
Returned Instance is %d while expecting instance is %d\n
GetBBIPCLogs
VinylCommandDriver ValidatePerso perform failure
Successful Read response from PSI,bytesRead = %u\n
Error: one of given parameter got null. ( pkt: %p, fname: %p, offset: %p, length: %p )\n
Rx:
fetchARIMsgFromTransport
TraceFlush_block_invoke
listenForIQStopCompleteInd_block_invoke
ICE_FILER_read: %s (return code=%d)\n
InitPerso
VinylCommandDriver Reset Sim Card failure
KTLNVMReadGroupBlock
driver timeout
KTLBmmProvideBootTimeInfo
KTLGetManifestStatus
Number of entries: %u\n
These parameters cannot be NULL: opt: %p\n
These parameters cannot be NULL: opt: %p, rxDiversity: %p\n
KTLGetPersonalizationInfo
Packet read < Minimum size (%d < %ld)\n
Readfile
Done
SwitchCardMode
ManagePairing
%s is not an indication, not registering it
success
driver IF not available
Failed to send PSI command\n
Failed GetRandomNum ARI command\n
Error: Failed ARI_EXTRACT on copyReceiveData (Remaining=%d/%d)\n
VinylCommandDriver InstallVad perform failure
param count mismatch
cmd format invalid
KTLSecGetFusingState
Malformed/Incomplete Packet.  Bytes read does not match expected length from Packet header (read=%d, expected=%ld).\n
KTLBspSetApWakeInterval
KTLGetSimStackMapping
KTLGetIMEIInfoParseAndRelease
Failed to send the message of CsiIceSetTxAntennaReq.\n
GetRandomNum
KTLEBLParseDone
Could not find ARI magic (bufSize = %u)\n
KTLBspShutdown
Failed IBIFilerHSReadBBReq\n
PriRefresh
PriWrite
Timeout waiting for response.\n
GetVinylType
error sending\n
unknown SIM type
Error: CsiFpUpdateAckRsp Failure (%s)\n
Packet read failed.\n
sKTLPacketCopyReceiveData
Failed IBIPriWriteReq_V3\n
Treating BB as single-SIM. Using default SIM stack mapping in KTL.\n
Error: CsiFpSnapshotRsp Failure (%s)\n
Unknown
Failed to get response!\n
Missing required transaction ID: context_id=%x\n
KTLMonMemoryStatus
KTLGetCurrentBootStateParseAndRelease
[ind] Error while unpacking trace flush complete indication
Error: packet malformed, payload too large for Readfile.\n
Error: ICE_FILER_write. Invalid Parameter.\n
Error: IceFilerReadRspCb. Uta Failure from Baseband.\n
Failed to send message IBIMSimGetSimStackMappingReq.\n
Received NACK\n
Error on the result: %d\n
KTLStartProvision
driver not supported
KTLSetAntennaPort
KTLSecGetFactoryDebugEnabled
Error: packet malformed, payload too large for StartInfo.\n
Error: IceFilerReadRspCb. ARI Context ID %x not on Lookup Table.\n
misc
GetEid
KTLAudioEnableHWLoopback
ari
Parameters are not correct: opt: %p, filerID: %p\n
CsiSecReadSikPKey
KTLSysGetInfo
opt(%p) or respParam(%p) is NULL\n
Sending command of length %u, type %u\n
EFI receive expected AT response (%u) but found (%u)\n
Tx:
KTLGetSimTrayStatus
KTLBmmProvideBootTimeInfoParseAndRelease
KTLIsBBSimStackMappingEnabledParseAndRelease
Carrier bundle name length (%u) larger than max allowed (%d)
Failed to run TraceSetConfigReq\n
Received trace flush indication callback
sendRet=%d\n
Error: %s. Invalid Parameter.\n
Received additional bytes %u, expected %u, additional %u\n
pkt(%p) or opt(%p) or allReady(%p) or moduleStatus(%p) is NULL\n
send
These parameters cannot be NULL: opt: %p, antennaPort: %p\n
ICE_FILER_read
Error: TelephonyUtilTransportRead (ret=%d, available=%d, read=%d).\n
Embedded null found in AT response at buffer offset %u\n
Failed to send command\n
KTLCpsSetSvn
Successfully flushed trace
FinalizePerso
Failed to parse response.\n
etb
registerIndication
KTLGetAntennaPort
Invalid buffer size(s) returned from baseband:\nnonce(%u)\tnonce_max(%u)\nsnum(%u)\tsnum_max(%u)\npkhash(%u)\tpkhash_max(%u)\n
KTLPSISendEnhancedCommand
Unknown-type
KTLEBLParseStartInfo
Provide either transport or ARI id, not both\n
Received AT string size %u, but caller provided buffer size %u\n
Error: CsiFpRegisterRsp Failure (%s)\n
Failed GetPersonalizationParametersReq\n
Error: IceFilerReadRspCb. Buffer Overflow.\n
Pulling next message from backlog\n
An error occured sending the message. (%d)\n
VinylCommandDriver DeleteProfile perform failure
Command driver with ariId=%d registering for indication: %s (%u, 0x%x)
KTLAudioDisableHWLoopback
KTLPSIReadResponse
Failed reading response from PSI: bytesRead = %u\n
Error: ICE_FILER_read. Invalid Parameter.\n
GetData
%s: Failed to send (Remaining=%d/%d).  Aborting...\n
KTLPing
%s%s%s.%s
Failed IBIFilerHSWriteBBReq\n
Error: IceFilerWriteRspCb. ARI Context ID %x not on Lookup Table.\n
KTLGetSimSlotInstance
Error: CsiFpGetStatusRsp Failure (%s)\n
driver error
KTLSecGetSNUM
Error: ICE_FILER_read. Context Already Exists.\n
Error: ICE_FILER_read. Failed copyReceiveData (Remaining=%d/%d)\n
GetNvItemsSetting
Malformed response\n
Rcvd Packet of type %u (%s), length %u\n
Error: packet malformed, payload too large for Done.\n
Unrecognized message type.\n
opt(%p) or bootState(%p) is NULL\n
Delayed response received\n
PRI/GRI Command Result: %d\n
recv
InstallVad
KTLNVMReadGroupStart
function not supported
NACK Received\n
KTLEBLReceivePacket
KTLGetIPCLogBufferList
GetIMEIInfo
Normal
Coredump
Packet read too large (%d > %d) - Internal Error.\n
KTLEFIReceiveData
Receved message of size %u, but caller provided buffer size %u\n
Error: ICE_FILER_write. Failed copyReceiveData\n
Unexpected status while waiting for trace flush indication
LpaSigningRequest
operator=
KTLGetSimSlotMapping
Reading response from PSI\n
Secure
Timeout waiting for transfer to complete\n
Failed receive of remaining packet bytes (expected=%u, actual=%u)\n
[ind] Error while unpacking IQ trace stop complete indication
Error: TelephonyUtilTransportWrite (ret=%d, available=%d, written=%d).\n
Failed to send the message of IBISimTrayStatusReq.\n
basic_string
%s/%s.bin
Success
VinylCommandDriver FinalizePerso perform failure
KTLNVMReadGroupEnumList
KTLNVMSendSnapshot
CsiSecCollectScrtBlob
%c%d%c
TraceFlush
Timeout while waiting for trace flush indication
[ind] IQ trace stop complete indication success
%s.bin
File Open: %s (name=\"%s\" descriptor=%d)\n
VinylCommandDriver GetVinylType perform failure
KTLSetRxDiversity
IceFilerWriteRspCb
KTLGetIPCLogBufferList returned false\n
blockRet=%d blockCtxId=%d\n
KTLSecGetRandomNum
BadEEPROM
Failed IBIFilerHSEndBBSessionReq\n
TelephonyUtilTransportCreateWithFD: %s (filedesc=%d)\n
Failed to retrieve SIM stack mapping from BB.\n
Failed IBINvmSnapshotReq\n
Failed to read coredump list table\n
Failed CsiSecCollectScrtBlobReq\n
Failed initial receive\n
Not supported\n
KTLGetSimTrayStatusParseAndRelease
VinylCommandDriver GetEid perform failure
Error: CsiBspNvmGroupEnumListRespCb Failure\n
internal error
KTLSetAntennaPortParseAndRelease
ICE_FILER_write
Error: ICE_FILER_write. Context Already Exists.\n
KTLSahGetCrashReport
KTLIsBBSimStackMappingEnabled
TraceConfig
perform
..
DeleteProfile
ValidatePerso
BB internal SIM slot -> stack instance mapping disabled. Retrieveing SIM stack mapping from BB.\n.
cmd called in wrong state
KTLSecGetChipId
VinylCommandDriver GetHwIdSimConfig perform failure
Failed to allocate memory for core dump lists\n
Error: packet id mismatch (expected=%d (%s), got=%d (%s))\n
KTLEBLParseReadfileExt
\r\nERROR\r\n
KTLRawSendData
KTLCddGetDebugLog
KTLBspDebugJtagMode
/AppleInternal/Library/BuildRoots/4~CatVugAVHlPmCykG3u5RYNuSUaO3iPS0fZcrWSs/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/local/include/ARI/ari_sdk_msg.h
GetPersonalizationParams
Could not find ARI magic in additional bytes.  Discarding...\n
KTLTriggerDelayedResponseParseAndRelease
Failed IBIFilerHSReadBBGetSizeReq\n
Failed to send the message of IBIPriWriteReq_V2.\n
Command driver with ariId=%d successfully registered for indication: %s (%u, 0x%x)
[ind] Trace flush complete indication success
Start
Error: packet malformed, payload too small for Readfile.\n
GetPowerSleepStats
ktl
GetBBWakeReason
vector
Error: packet malformed, payload too small for StartInfo.\n
ICE_FILER_write_block_invoke
Failed IBIFilerHSStartReadBBSessionReq\n
listenForIQStopCompleteInd
ret=%d list size=%lu\n
KTLNVMSendGetStatus
maxLen( %u ) is less than sizeof command ( %lu )\n
Failed to unpack response.\n
SysGetInfoV2
Command driver with ariId=%d failed to register indication: %s (%u, 0x%x)
KTLFinishProvision
Unknown sim state 0x%x\n
Baseband NVM sync group not enabled. Check PR settings. (UTA error = dev grep not supported)\n
KTLCddGetParamDump
KTLBspSetNvItemsToState
Failed IBIPriRefreshReq\n
Registering for trace flush complete indication
KTLGetIPCLogBuffer: %s\n
%s \n
VinylCommandDriver Manage pairing failure
KTLSecGetPkHash
Error: IceFilerWriteRspCb. Failure from Baseband.\n
Failed to send message CsiMSimGetSimStackMappingStatusReq.\n
StartWriteSession
Fetching log buffer entry: filename=\"%s\" size=%d level=%d next=%d buf_p=%d\n
StreamFW
Failed request\n
Failed to read response\n
Not enough space left to append \\r\\n to AT string.\n
GetReadSize
EndSession
PRI signature size (%u) larger than max allowed (%d)
%s indication received; calling indication handler
Command driver with ariId=%d deregistering for indication: %s (%u, 0x%x)
Chunk size cannot be zero\n
DoneAck
%s indication received but no indication handler exists
%s is not an indication, not deregistering it
param out of range
read byte (%u) is less than the dump list size (%lu) or more than maxlen(%u)\n
KTLCDSendEndCoredumpCommand
KTLGetIMEIInfo
StartReadSession
opt(%p) or filerId(%p) is NULL\n
Indication %s is not currently registered, no need to deregister it
KTLBspIceAtString_block_invoke
KTLGetSimCardPresence
Error while receiving trace flush indication
[ind] Got unexpected message 0x%0x, expected IQ trace stop complete indication (0x%0x)
expected gmid %d, doesn't match response gmid %d \n
VinylCommandDriver InitPerso perform failure
Error: CsiBspNvmReadGroupBlockRespCb Failure\n
KTLNVMSendRegister
KTLCDProcessCoredumpEntry
Filer ID: %d (0x%x)\n
VinylCommandDriver configId Request failure
Normal SIM
Error: CsiBspNvmReadGroupRespCb Failure\n
Error: CsiFpUpdateHeaderData Failure (%s)\n
Failed to allocate packet memory\n
KTLGetAntennaPortParseAndRelease
Sending PSI enhanced command: command %d, param %d\n
Enhanced
Registering for IQ trace stop complete indication
Failure
BB internal SIM slot -> stack instance mapping enabled. Using default SIM stack mapping in KTL.\n
KTLRFFilePushReq
KTLBspSwTrap
KTLGetSimStackMappingParseAndRelease
%s
%s: (%s:%d) Array assignment too large(%p), got(%zu) max(%zu)
```
