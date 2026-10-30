# `/usr/lib/libNFC_Comet.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,419,232 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 21 (Size: 2304)
Flags         = NoUndefs, DyldLink, TwoLevel, AppExtensionSafe
```

## Linked libraries (3)

- `/usr/lib/libNFC_Comet.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libNFC_HAL.dylib (compatibility version 1.0.0, current version 1.0.0, reexport)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (6,284)

First 2,500 of 6,284.
```
phNciNfc_CompleteNfceeDiscoverSequence:Registering for Nfcee Discover Notification Failed
NFCEE Notification Type: phLibNfc_eSE_EvtSwitchedOff
bModeCeB 
phLibNfc_GetRtngTableProc
Set Rf signed config sequence failed to Set remaining configurations, return failed
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_Rejected
phNciNfc_GetNciContext:Failed to allocate memory, insufficient resources
phNciNfc_CommonSwpRsp
Ioctl_SetRfCalData: Invalid input parameters
LibNfc:TrigEvent=
phLibNfc_SM_SE_eModeSetOffToOffTrans
Target is no more in the Rf field
phFriNfc_MifStd_H_ChkTLVs
phLibNfc_549ProcSysL1LogNtf: L1-eDebMgmtL1DataRxFailure
Rxd Routing Entries Validation Failed!
phDnldNfc_FwVerAfterVenReset:Invoked with failure status
No NCI Discovery Configuration Details:
phLibNfc_CoreInitCmd
phLibNfc_SM_IoctlGetRfPropRegsTrans
phLibNfc_SM_eAntennaSelfTest:Invoking callback, wStatus = 
 Mf XchgData Request Failed RF Time out..
phLibNfc_MifareMap
phLibNfc_TagRemovalDetectComplete
phNciNfc_ReceiveDataBufferCb
phLibNfc_Ioctl_Mgmt_CB - Ioctl Prop Get Transition register complete
phDnldNfc_RetrieveSn450vEcIntegrityStatus
bNciReTransLimit:
eSE Re-initialization Sequence
phLibNfc_ModeSetHciNwkProc: Set Mode success
phLibNfc_ConfigTestModeComplete
phFriNfc_Tpz_H_UpdateLenFieldZeroAfterRead
phDnldNfc_DnldGeteSEHash2DataCmd: Request submitted successfully
phDnldNfc_GetFwInfoRspBeforeDnldWrite - Request Successful
phLibNfc_RetrieveDnldTable
phDnldNfc_SecureUpdateRsp:Received Status byte=
phDnldEseNfc_HciDeleteList
phDnldNfc_DnldGetSessnStateCb - Request Failed!!
phLibNfc_Ioctl_PropSetPwrTrackConfig: Feature Not supported!
phLibNfc_SM_SetSuicaEntrySysCodeTrans
phLibNfc_SM_SE_eModeSetVirtualToVirtualTrans
phLibNfc_GetTagTypeMoreInfoResp
beSERemovedNtf:
phLibNfc_DeInitializeComplete: Invalid LIBNFC Context
phLibNfc_SM_CustFactoryCfgTrans: Invalid context
phFriNfc_MfUL_H_findNDEFTLV:Current Ndef Message size
phLibNfc_RFParaUpdateComplete
phNciNfc_UpdateCrcErrNtfRecoveryFlag
phNciNfc_SetVasCodeRsp:Set VAS Code response received with failure status
phFriNfc_Desfire_SelectSmartTag
Invalid input parameter (Nci Context)!
phNciNfc_UpdateNtfList
bNewVer[0]
phLibNfc_DnldLogReadReq
phLibNfc_SM_AntennaTestTrans
phNciNfc_CoreRxDelayReqNciPkt
phNciNfc_ClearDiscContext
IDm 
Deactivate Ntf to IdleMode..
phNciNfc_GetTagTypeInfo
 Mf Sector select Request is Successful!! ..
phLibNfc_ISO_14443_3B_PresChkConnComplete:ISO_14443_3B Connect callback and Presence Check callback unavailable!!
phLibNfc_AntennaTestCmd
phLibNfc_RawCtrlMsgTrnscvComplete
phLibNfc_GetMemoryDumpRsp - Request Failed!!
phLibNfc_SpmiClientResetTimerStart: Client reset Nack Timer Start failed
phFriNfc_T5T_H_ProcessCheckNdef:Current Ndef Message size
Continue... 
phNciNfc_GetConnInfo
phNciNfc_GetSmbLogInfo: Stack not initialized
Response opcode not matching to opcode of command sent 
phDnldNfc_BuildDnldEsePkt : pDnldEseCoreCtx->dwCrdtTimeOutMs:
phDnldNfc_DnldGetSecureFwInfoCmd: Request submitted successfully
NCI Remote device Details:
phLibNfc_CustFactoryCfgComplete: Failed status received from NFCC
Flush Data command rejected by NFCC
phNciNfc_GetLstnNtfTimeoutHandler
phNciNfc_GetAteTrimVersion
Log Request submitted successfully
phLibNfc_EseCfgDelayTimerStart: Dnld Ese config Timer failed to start
  ISO15693 listen  Rf tech and mode sent 
Read SWIO voltage Info Successful
phLibNfc_SeqHandler
CheckIntegrity Request submitted successfully
SensB Response:
phNciNfc_eSeSvddOnCtrl, Memory allocation failed!
Discovery select command failed!
phLibNfc_RemoteDev_ChkPresenceTimer_Cb
phFriNfc_MfStd_H_WrRdAuth
phNciNfc_GetGenDbgLogRsp: phNciNfc_GetGenDbgLogRsp: failed with
phDnldNfc_DnldPrevSessnStateCb - Valid Session State Resp Buff!!...
phDnldNfc_SecureBootEnterCommitModeRsp
Sequence operations not set!
phLibNfc_SM_SetCWRFCfgTrans
phLibNfc_SM_Main_PollActiveTransComplete:Invoking callback function, wStatus = 
NCI Core Initialization success!
TML Read req during boot retry failed
phLibNfc_Mgt_VenResetStatus
phHciNfc_ProcessEventsOnApduPipe: Independent SE OS Reset, PipeID
Failed to Reset!
phNciNfc_ProcessModeSetRsp
phLibNfc_HCESendComplete
procSplitTlv
Inc/Dec Command Header failed!
phLibNfc_InvokeDiscDisconnCb: Upper layer call back function (pDiscNtfCb) not found
PipeStatusCeA 
aDataRateMaxCeB[1] 
phNciNfc_ChkPresExtnCmd
pNciCtx->dwNtfTimerId
phLibNfc_DnldGetFwVersionApiCb - Incorrect Response!!/Unknown Platform
phLibNfc_ConfigNciMode - client ID update failed
Get Pwr Track Data command Semantic error received
phNciNfc_GetLpcdCountRsp:Get LPCD false positive counter response received with failure status
bCurrVer[1]
phLibNfc_InitializeAfterVenReset:Init Failed
phFriNfc_Felica_CB_Transceive
phLibNfc_DeselectCmdMfpSL1Resp : Invalid Libnfc Context
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyECmdParUnknown received
phNciNfc_GetGenDbgLogRsp: allocate memory failed
phNciNfc_GetSwitchRFCfgCmd: Invalid input parameter
phNciNfc_ProcessResetRsp
phLibNfc_SetPowerMode
phLibNfc_SM_Main_ListenReceiveTransComplete:Invoking callback function, wStatus = 
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_DiscTearDown
phNciNfc_FreeSendPayloadBuff
Invalid RfInterface!
phLibNfc_InternalSequence: RID/RALL Response dropped due to Ongoing Discovery Sequence
Fw Already Upto Date!!
phLibNfc_RemoteDev_Receive
RSAKEY Area Crc is NOT OK!!
phNciNfc_TlvUtilsAddTlv
LPCD Assistance Exit Notification is not applicable for this platform
phLibNfc_PrintSendData: phHal_eMifareSectorSel
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_Failed
phLibNfc_GenericErrorHandler: Independent SMB TX Blocked Received
phNciNfc_BuildNxpRfDiscConfigParams
phFriNfc_MfStd_H_ProCon
phNciNfc_ProcessGetPwrTrackDataNtf
phNciNfc_CreditsUpdateCB
Rf Protocol:
 Couldn't Get ConnId..
phHciNfc_ProcessClearAllPipeNotifyCmd:unkown NFCEE ID
phLibNfc_GetMfUlcReadPage
 Credits updated for ConnId
phNciNfc_GetSwitchRFCfgRsp: Invalid switch RF config received
phLibNfc_GetFaultCounterProc: Invalid Response received!
 3B_PICC XchgData,PH_NCINFC_STATUS_RF_FRAME_CORRUPTED Detected by NFCC during Data Exchange 
 Mf XchgData,PH_NCINFC_STATUS_RF_PROTOCOL_ERROR Detected by NFCC during Data Exchange 
Validation of  NCI RemoteDev handle Failed
phLibNfc_GetSuicaSysCodeCmd
Enabling extension command accepted by NFCC
phNciNfc_StoreListenIsoNfcDepParams
Max Control packet payload size:
TmlReadCommonCb: Invoking proc function
phLibNfc_EraseCounterNtfHandler: Dropping Ntf as there is no registration
Target Lost!!
Invalid LibNfc Context passed by lower layer
phLibNfc_SM_GetTransEvent
phLibNfc_RetrieveNvmDumpStartAddrProc: pReadBuff allocation failed
phDnldNfc_DnldEseVldtCrcRcvd:Invalid frame payload length received
Max Routing Table size:
phLibNfc_SM_Dnld_eSE_GetSmbTrans
Starting timer for phLibNfc_RemoteDev_ConnectTimer_Cb
phLibNfc_PrepareConnect_Felica
phLibNfc_HLMCfgComplete
phDnldNfc_BuildSecureHdllPkt
phNciNfc_GetGenDbgLogCmd
eRfDeactvType -> phNciNfc_e_SleepMode/phNciNfc_e_SleepAfMode
phLibNfc_InitSetConfigProcess
phNciNfc_CoreValidateNciCoreCmd
phLibNfc_TagRemovalDetectResp
phLibNfc_UpdateSeInfo:Initialization in Progress for:
phNciNfc_UpdateDtaStatusFlag
phLibNfc_ParseHrdFltDumpInfo: dwControl_s
Manufacturer specific info - Byte0:
phLibNfc_SM_InitTrans:MultiTag Detection MW initialization Failed
phNciNfc_StoreTlvInfo
phLibNfc_LongVasCwDetNtfHandler :pGenericNtfCb[Prop Vas Long CW Ntf]
Valid Actv Rf Tech and mode received (2)...
phDnldNfc_DnldChkIntegrityCb - Valid Resp Buff!!...\n
phLibNfc_NfceeDisableUICC: Failed to Disable UICC,error
#######Set Mode notification TIMEOUT########\n
Completing T3t Connect sequence
phLibNfc_ConfigHsuBrCmd: Check succeeded with baudrate
phNciNfc_RegisterNotification
phNciNfc_TriggerNfccAssert: Sequence failed!
Response/Data call back not registered
phLibNfc_Mgt_ConfigureAssertionLogging: LIBNFC Not Initialized
phLibNfc_SearchSETable
Ioctl_PropSetConfigSigned: Invalid Input Parameter!
bLibSeqNxt:
ATR_REQ - Length Reduction is applicable 
phHciNfc_GetPipeIndex
phHciNfc_ProcessEventsOnPipe: phLibNfc_eSE_EvtEndOfOperation, Ins
phLibNfc_SM_ConfigReDiscoveryTrans
Releasing NCI context has already been done
State machine status is NFCSTATUS_REJECTED
Nci context null (phNciNfc_GetPwrTrackDataTimeOutHandler)\n
Get Secure Fw Info SUCCESS!
 Felica XchgData,PH_NCINFC_STATUS_RF_TIMEOUT_ERROR Detected by NFCC during Data Exchange 
phLibNfc_LibNfcRecovery: HSU baud rate different, changing it to the default baud rate (115200)
phNciNfc_CompleteNfceeDiscoverSequence
phFriNfc_MifareStd_iConnect
phLibNfc_GetEepromSettingsProc-Retry Failed to Configure Entries
NFCC Re-Init failed, return failed
phFriNfc_Desfire_NdefFileSize
Registering for notification message...
phNciNfc_CoreInvokeCb:Registered Ntf call back function invoked failed-Invalid function pointer
phNciNfc_DeAssertWakeUpTimerCb
phNciNfc_CoreSendCb
phHciNfc_RegisterForResponses:APDU Pipe
phNciNfc_PrintRfTechModeDescription
 Mf XchgData,Unknown RF related error Detected by NFCC during Data Exchange 
phLibNfc_Mgt_eSeCfgDnldMode: Invalid IOCTL context!!
Set Rf Settings sequence failed to Set remaining configurations, failed with status=
phLibNfc_GetSuicaSysCodeCmd : Libnfc Context is Invalid
phLibNfc_GetDbgLogCmd : Invalid parameter, Libnfc Context is Invalid
Generic DEBUG Notification timer start FAILED
phHciNfc_HciCmdRspCb : HCI Command Response timer deleted successfully
phLibNfc_SM_MwResetTrans NFCC is ON
phFriNfc_Felica_HUpdateAttrInfo:Current Ndef Message size
phFriNfc_Tpz_H_ActualCardSize:Current Ndef Message size
phDnldNfc_DnldVldtCrcRcvd:RESET NTF- NO UART message Received
phNciCoreMuxNfc_DnldEseTx:Invalid Parameter
phNciNfc_GetPwrTrackDataSeqComplete
 Mifare Plus tag detected..
phNciNfc_GetUsrAreaAddrSeqComplete
phLibNfc_RFParaUpdateComplete: Invalid LibNfc Ctx
phDnldNfc_SecureUpdateRsp: Flushing pending notifications 
phDnldEseNfc_ProcessApduPipeEvts:Could not copy entire received data
Can not process Generic Error Ntf - Invalid input parameters
Suica express transaction ongoing
phHciNfc_CoreSend:HCI Resend Packet Timer Create failed
phLibNfc_ConvertToRemDevType
phLibNfc_ParseAssertionData:Failed Status Received From Lower Layer
phLibNfc_RawCtrlMsgTrnscvCmd: Sending command failed
bCurrVer[0]
phLibNfc_InvokePendingDnldCb
phLibNfc_PrintgDebugInfo
phHciNfc_AnyGetParameter:Memory Allocation failed
phNciNfc_RdrIso15693Init
phLibNfc_InitializeComplete :pGenericNtfCb[PLLUnlock]
Stack not initialized (phNciNfc_Nfcee_StopDiscovery)\n
PH_NCINFC_STATUS_RF_TIMEOUT_ERROR Detected by NFCC during Data Exchange 
phDnldNfc_DnldPrevSessnStateCb - Invalid IOCTL context!!
phLibNfc_DnldGetFwVersionApiCb - Invalid Chip Version!!
phDnldNfc_eSESmbCfgVenResetTimeoutCb:Invalid LIBNFC Context
phHciNfc_RegisterCmdRspEvt:Failed, Invalid HCI bMsgType or Input params
phLibNfc_ProcessDevInfo
phLibNfc_HciSetAllowList: Invalid LibNfc context received!
phLibNfc_IoctlSetPropRfCfgCmd
Rx HCP:PipeID
phLibNfc_SM_GetNfccEseHashDumpTrans Invalid parameter
Unable to delete resend timer
phLibNfc_PrintSendData: phHal_eMifareRaw
phLibNfc_PropRdrNtfHandler :pGenericNtfCb[Prop Reader Ntf]
phNciNfc_ChkDataRetransmission: Re-transmitting Data pkt Attempt..
phLibNfc_GetAvailableSlotIndex: Registration not found
HCE Activation in Express mode failed
phDnldNfc_MemDmpVenResetTimeoutCb:Invalid or NULL download core context
phNciMuxNfc_MuxHandler : Write Request Failed(eMuxEvtDnldTx)
Switched Off state: Supported
phLibNfc_SM_Dnld_eSE_CfgTransCmplt
 Mf WriteN Request is Successful!! ..
phHciNfc_Transceive:Invalid HCI Context
phDnldEseNfc_ProcessApduPipeEvts:EVENT_WTX_REQ received
phDnldNfc_RetrieveSn450vBootStatus - Invalid value received
phUtilNfc_GetdnldEseCoreContext
phLibNfc_SetRtngTableCfgs
phLibNfc_SM_SE_eModeSetApduToApduTrans
phLibNfc_SendWrt16CmdResp:SendWrt16 Command payload Header failed!
phLibNfc_GetMultiTagInfoCmd
Kovio poll Techn and mode received
phNciNfc_CoreRegister:No free slots available, registration failed!
phDnldNfc_DnldEseTranscvCmd : Response Timer Start failed!!!
phNciNfc_UpdateClosedLogConnInfo
phHciNfc_ReceiveAdminNotifyCmd:Failed Invalid Params Received
 SE restricted mode Unknown Event\n
Failed to Register phLibNfc_RssiStatsHandler
Nci Set routing table failed!
Invalid input parameter (phNciNfc_ProcessActvNtf)\n
phDnldNfc_DnldChkIntegrityCb: Invalid IOCTL context!!
phLibNfc_Ioctl_PropSetCrcChkConfig: Feature Not supported!
Listen F bitrate:424kbps
Failed to Register phLibNfc_EmvcoRfCollisionDetNtfHandler
phNciNfc_CoreReSend Failed to Stop Timer
phLibNfc_PrintSendData: phHal_eMifareWriteSector
phLibNfc_CustFactoryCfgCmd: Libnfc Context is Invalid
phDnldNfc_GetFwInfoRspBeforeDnldWrite
phLibNfc_IoctlSetRfCfgProc : Libnfc Context is Invalid
Frame waiting time len:
phLibNfc_SM_IoctlSetSysConfigTrans: Failed
phLibNfc_Mgt_GeneralNtfRegister
LPCD Trace mode is wrongly enabled
phLibNfc_GetAvailableSlotIndex: No Free slot available
phLibNfc_SM_IoctlFwDnldTrans: Firmware Library Load Failed!!
phNciNfc_PrintTechNfcASpcfcParamsDescription
NFC F LISTEN Techn Specific Params - END
phLibNfc_Mgt_Initialize - Protected Page Status received in Get Secure FW info response is NOK
phLibNfc_ChkDiscoveryTypeAndMode
phNciNfc_CoreIfSetInitialCredit
phNciNfc_GetConfigRawRsp
phDnldEseNfc_HciRecvManager:Memory Allocation Failed
phNciNfc_GetGenDbgLogRsp
phLibNfc_IoctlSetRfCalDataCmd : Libnfc Context is Invalid
 Invalid Params supplied!!
aPupiRegCeB[1] 
 Unknown tag detected..
phNciNfc_RFParaUpdateCmd
phNciNfc_DeActivateRemDev
phLibNfc_SM_GetNfccEseHashDumpTrans
Battery off pow state requested but not supported
phDnldEseNfc_GenErrNtfHandler: Error code 0x0C,Invalid Pipe
Sync Handler resending in progress
phLibNfc_DnldGetFwVersion
phHciNfc_CoreDeleteList:NULL HCI Core context!
Deactivation to discovery success
Set Rtng table Sequence failed!
Invalid Baud rate
phNciNfc_CustFactorySetGetCfg
phNciNfc_ValidateSuppDeActvType
phLibNfc_GetPlatformInfo
phDnldNfc_InitImgInfo
phFriNfc_MfUL_GetLockBytesInfo
phLibNfc_GetSmbLogProcComplete
Flush Data response Invalid parameter received
phNciNfc_ValidateSysConfigParams
phNciNfc_SeEUiccSelectCfg: pNciCtx->bSeEUiccCfg
phNciNfc_ProcessGenericErrNtfMFC: Can not process Generic Error Ntf - Invalid input parameters
phDnldNfc_DnldEseTranscvCmd
phLibNfc_SM_GetPowerTrackTrans
phLibNfc_Ndef_DeInit
Presence check extension response received with failure status
phDnldNfc_UpdateRsp:First Success READ Address
Ioctl_PropGetRfConfig Failed!!!
Listen NFC-DEP waiting time len:
phLibNfc_SM_IoctlConfigDebugModeTrans: Invalid timeout value
phLibNfc_Mgt_SetRfSettings
phLibNfc_Actv2Discovery
Version Not Updated After Previous Download!!\n
Invalid parameter, Libnfc Context is Invalid
phLibNfc_ChkMFCAuthWrtCmd
pLibCtx->tDiscCtx.bRetryCfgCount
phLibNfc_HciInitComplete: Invalid Hci context received!
Get Listen Mode Ntf Handler timer start FAILED\n\n
phDnldNfc_BuildHdllPkt wRemBytes
bNciSeqId:
Timeout:wEofTimeout
phLibNfc_InitializeAfterVenReset:Invalid Context
phDnldEseNfc_GenErrNtfHandler
phNciNfc_GetNciSeqId
phDnldNfc_DnldChkIntegrityCb - Request Failed!!
phLibNfc_LogConnCloseCb
phNciMuxNfc_DnldClearInvokeUpperLayer
Rf LinkLoss in DiscMode..
phNciNfc_CoreUtilsUpdatePktInfo
phLibNfc_SM_IoctlIoctlSetRfConfigSignedTrans:                                    Buffer is not adhering to semantics of RF_SIGNED_CONFIG_CMD!
phLibNfc_Mgt_DeInitialize
Stopping Credit await timer..
phLibNfc_NfceeDisableESE:Invalid Context
phLibNfc_PreparePresenceCheck
NFCEE Notification Type: ACTIVATED
phLibNfc_ConfigLoggingCmd
phLibNfc_GetDbgLogCmd
phLibNfc_GetNvmMemoryDumpRsp
Invalid RF procotol
phNciNfc_ReadSwioPadVoltageRsp
phNciNfc_RawCtrlMsgTrnscvSeqComplete
phNciNfc_ProcessCommonNciRsp1 - Response Successful
phLibNfc_EsePwrCfgDelayCb:Invalid Timer ID!!
phNciNfc_SwpSelfTest
phDnldNfc_RecvDnldEsePkt: Read Request Failure
Number of Rf intf's supported:
phNciNfc_GetFwInterfaceVersionCmd
phNciNfc_ClearSetModeNtfWaitTimer
phLibNfc_Mgt_GetNfccParams: Invalid input parameters
Set Config se reader Failed!
phNciNfc_SetRtngConfig
phNciNfc_CoreInit:Stack not initialized
SEL INFO - ISO-DEP protocol is supported 
Registering for Generic Debug Logging Notification
phLibNfc_SpmiRstCrcConfig
phLibNfc_SM_IoctlLoopbackTrans: Failed
phNciNfc_eSeSvddOnCtrl
phLibNfc_MultiTagCompleteInit
SetRfCalSignedData: Invalid parameters
phFriNfc_Desfire_ReadBinary
phLibNfc_SM_Dnld_TransComplete
phNciNfc_ReleaseMemory
phLibNfc_ReqInfoComplete
Set Config failed
phNciNfc_SendMfReq
NCI Get Config Response partially received 
phHciNfc_CoreRecvCB: SE Transceive Timer Already deleted
In phLibNfc_ListenModeDeactvNtfHandler
Failed to Register phLibNfc_LongVasCwDetNtfHandler
phFriNfc_Felica_HAfterRead_CopyDataToBuff
phLibNfc_GetTagInfo: Invalid param
phLibNfc_GpadcDebugHandler
phDnldNfc_DnldEseGetRemainingSmbLog:Invalid Download Ese Response Timer ID
phLibNfc_SM_GetMultiTagInfoTrans: Feature not supported on this platform
 Request Payload Header Creation Failed ..
phNciNfc_CoreRecvChkPktType:NFCC Sends Command Packet Type, dropping...
phNciNfc_ValidateRfTechMode
phNciNfc_GetSmbLogCmd
phHciNfc_AnySetParameterCb
phHciNfc_AddRegistration
phLibNfc_ShutdownCb: Lower layer Reset Failed
phNciNfc_StateDummy2Idle
phFriNfc_MfUL_H_NxtOp
phNciNfc_FlushDataRsp:Flush Data response received with failure status
NCI Discovery Configuration Details:
Set Config Response:
phHciNfc_OpenPipeCb
phHciNfc_OpenPipeCb: Releasing memory
ShutdownCb:Invoking callback function, wStatus = 
phNciNfc_VerifySupportedRfIntfs
Invalid routing type
Framing failed!
phNciNfc_ProcessIntfErrNtf:pRfIntfErrNtfCb call back is not registered so dropped at NCI
phHciNfc_CoreSend:Invalid HCI Context or Send params
phHciNfc_AnyOkCb:
phLibNfc_SM_IoctlExpModeSWaitTimerOffTrans
phLibNfc_ConfigTestModeOffComplete
phNciNfc_ParseSysClkParams
phNciNfc_PrbsTest: Stack not initialized
phLibNfc_ParseHrdFltDumpInfo: dwS_cfsr
phHciNfc_GetPipeId: ADM_NOTIFY_ALL_PIPE_CLEARED cleared the pipes!!!
Vas Inversion Timer Stopped
####NCI CORE Context
Flush data command failed!
Invalid Nfc-A UID length
phLibNfc_SwpTest_CB: Prbs test passed
phDnldNfc_RetrieveSn450vEcIntegrityStatus - Un-known value received
phNciNfc_InitGenErrorNtfCB:Invalid Context Param..
Rf Deactivate Ntf to IdleMode..
State machine has returned NFCSTATUS_FAILED 
phLibNfc_InitializeComplete : Initial Download TML read request failed!!
phFriNfc_MfUL_H_RdCardfindNdefTLV
Anti-tearing protected Area Crc is NOT OK!!
Registering for RSSI statistics Notification
phLibNfc_HciDataSend: Invalid LibNfc context received!
Timeout:dwVasNtfTimer
phLibNfc_SetRfSignedSeqComplete: TML HSU Baud rate Set to default baud rate
phLibNfc_GetSwioPadVoltageSeqComplete: Failed
FMM NTF for eSE HASH1 RECEIVED 
RF Tech and Mode:NFC_A_SILENT_NTAG_PASSIVE_POLL_MODE
phLibNfc_NfceeDisableProc wStatus
phLibNfc_ChkRfListnerforNFCBPoll
phNciNfc_GetPwrTrackData: Invalid parameters
phLibNfc_SM_TrigRfOnNtfTrans: Failed
Invalid parameter passed (phNciNfc_ChkPresExtnNtfCb)!
Timeout:dwResendPktTimerId
LibNFC Null Context -Timers Delete failed
phLibNfc_SM_GetSwitchRFConfigTrans: Feature not supported on this platform
TmlReadCommonCb: Full read length received
phLibNfc_GetTagTypeResp
phLibNfc_DiscDeactivateComplete: Retry set mapping Failed
phLibNfc_HciDataSend: SE TxRx Timer Start Failed
phFriNfc_MfUL_UpdateAndWriteLockBits
phFriNfc_T5T_ChkNdef
phLibNfc_SetPowerModeComplete
phNciNfc_CoreRecvCb
\n\nphLibNfc_549ProcSysL1LogNtf: L1-RSSI wRssiInterpolatedinfo
phLibNfc_PropMultiTagStatNtfHandler- Length Error or Null buffer received
phNciNfc_ValidateCommonParams failed
Stack not initialized (phNciNfc_GetConfigRfParameters)\n
phNciNfc_PrintGetRtngTableRespDescription
phLibNfc_SM_SetChipScopeCfgTrans: Invalid Params
phLibNfc_SM_SetCWRFCfgTrans: Invalid Params
phFriNfc_OvrHal_Reconnect
pLibContext->tPlatformInfo.bBrRetryCnt
phFriNfc_MfStd_H_ChkAcsBit
Get VAS Code response Failed with Status
phNciNfc_RawCtrlMsgTrnscvRsp
phDnldNfc_GetFwInfoRspBeforeDnldWrite: Previous Fw Upgrade Session still Open..
phNciNfc_GetMultiTagInfoCmd
phHciNfc_UnRegisterCmdRspEvt
phLibNfc_SetHostCEConfigComplete
phFriNfc_MifareUL_iSelSectorChk1
bNciRspTimer:
State machine has returned NFCSTATUS_SUCCESS 
phLibNfc_PrintSendData: phHal_eMifareProxCheck
phLibNfc_MapBitRate
NFCC Configure HSU baud rate Failed after bBrRetryCnt
phLibNfc_SetSwitchRFCfgCmd : Libnfc Context is Invalid
phNciNfc_InitContext
phNciNfc_GetPwrTrackData
eSE Conn Pipe Updated Status- Open
GetClrAssertRegs:Invoking callback function, wStatus = 
phNciNfc_SetConfigRaw:Failed to allocate memory, insufficient resources
Get Power Track data Notification timer started\n
phNciNfc_SendEofDataPacket: Invalid or NULL pNciContext
phLibNfc_DummyDisc
phLibNfc_LaunchChildDeviceSequence:Started for SE Type
Critical failure in Download!!
phDnldEseNfc_ProcessApduPipeEvts: OS Reset Event received
phLibNfc_Verify_3_0_CrcStatus
phNciNfc_RecvMfResp
phLibNfc_GetAssertLogConfigCmd
De-register pres chk extension ntf call back success
phLibNfc_WaitLibSeqHdlrTimerCb
phLibNfc_Ioctl_PropGetRfRegs Failed!!!
phDnldNfc_DnldChkIntegrity: Invalid IOCTL/DNLD context!!
phDnldNfc_RetrievePn800vBootStatus - Invalid value received
Routing Table Area Crc is NOT OK!!
pLibCtx->tPlatformInfo.bBrRetryCnt
phLibNfc_SeGetRfCfg
phLibNfc_SetEepromStngsProc
phFriNfc_Desfire_ChkNdef
phLibNfc_ConnChkDevType
phDnldNfc_DnldGeteSEHash1DataRsp - Successful
phNciNfc_PrintTechNfcFLstnSpcfcParams
phNciNfc_InitReset
phLibNfc_HciDataSendProc:eSE Transceive received data after Timeout
phLibNfc_GetSwitchRFCfgCmd
phNciNfc_BuildSmbConfigParams
phDnldNfc_DnldChkIntegrityRecoverCb - Request Successful
phDnldNfc_DnldEseGetSmbCb
phNciNfc_Send4BData
phLibNfc_SM_MwResetTrans: Failed to reset the Rx Delay
phNfcNfc_NfceeGetDevIndex
phLibNfc_Mgt_GetstackCapabilities
phLibNfc_RemoteDev_ChkPresenceTimer_Cb: Invalid  or NULL pLibContext 
aATQACeA[1] 
Uid length:
phHciNfc_ProcessPipeCreateNotifyCmd:Failed Invalid Params Received
phLibNfc_SM_IoctlSetSysConfigTrans- Set Default Baud Rate FAILED, Status
phLibNfc_Mgt_SetNfccParams: LIBNFC Not Initialized
phLibNfc_GpadcDebugHandler: Dropping Ntf as there is no registration
Get Listen Mode Ntf Handler timer started\n
phDnldNfc_BuildHdllPkt : Invalid Input Parameter(s)!!
Start of Degraded FW Update, Offset
AFI
phLibNfc_ParseInputBuffer
Route                    :
phLibNfc_SM_GetGenericDebugLogTrans
Received ATRInfo length exceeded max ATR length
phLibNfc_LoggingNtfHandler:Failed to allocate memory for Dynamic BBA Info events
phLibNfc_ExtTempNormalNtfHandler :pGenericNtfCb[GPADC Temperature back To Normal Notification]
phNciNfc_BuildSwpConfigParams
phNciMuxNfc_BuildDataPktHci2-Failed to retrieve bIgnoreWkUpRet
phLibNfc_SM_MwResetTrans: Handle already released/ not initialised!!
phNciNfc_ProcessNfceeDiscoverRsp
Failed to created resend timer
phLibNfc_VerifyRxdRtngTable
phLibNfc_GetMultiTagInfoProc
phLibNfc_GetGenericDbgLogProc: operation failed
phNciNfc_ValidateLstnIsoDepParams
phDnldNfc_DnldGetSessnStateCb:Previous Fw Upgrade Session still Open..
RF Protocol:PROTOCOL_NFC_KOVIO
phHciNfc_CoreInit
 Jewel XchgData,PH_NCINFC_STATUS_RF_TRANSMISSION_ERROR Detected by NFCC during Data Exchange 
phLibNfc_SM_IoctlFwDnldTrans: Failed
phLibNfc_SM_IoctlGetSpmiGpioTrans: Invalid IOCTL Context
phFriNfc_Felica_HGetMaximumBlksToRead
phLibNfc_ModeSetHciNwkProc
phNciNfc_SwpTestCompleteSequence
phLibNfc_Ioctl_SetSpmiGpio: Invalid IOCTL context
phDnldNfc_DnldGeteSEHash1DataRsp - Invalid response 
IoctlGetRfCfgComplete,Libnfc Context is Invalid
phLibNfc_GetMemoryDumpSeqComplete: failed!
phLibNfc_CreateLogConnCmd
phLibNfc_CreateLogConnCb
Frame waiting time Value:
phHciNfc_AnyGetParameterCb:Uppler Layer Callback not defined
pres chk failed
phLibNfc_SendAuthCmd
phLibNfc_GenericErrorHandler
Only one notification is received to read listen mode routing table
phNciNfc_GetUsrAreaAddrRsp:Semantic error received
phNciNfc_MapBitRate
phLibNfc_ParseHrdFltDumpInfo: dwBasepri_s
phNciNfc_GetFwInterfaceVersionRsp
phLibNfc_UpdateNfceeDiscTechnType: poll Nfc-B tech supported
phLibNfc_SpmiStsRegInfoNtfHandler: Read Spmi Status Failed - pInfo set to NULL
phDnldNfc_DnldGetNfccHashDataRsp
No Techn specific params available
phNciNfc_ResetNtfCb
HCI Resend Info,bIns =
Tml Write error!!
Aid based routing request but not supported by NFCC
phDnldNfc_DnldLogCb - Request Successful
Listen A Bitframe SDD Value:
phLibNfc_ProcessNfceeStopDisc
phNciNfc_Nfcee_Connect
Response timer re-started
phLibNfc_GetEraseCounterSeqComplete
Padding
phNciNfc_CoreReSendCb:Resend command send callback received
phFriNfc_Felica_HUpdateData
phLibNfc_DummyDisc: Failed to create Timer!
SE is not active in VAS Express+HCE mode
phNciNfc_GetActiveHeadCount
phLibNfc_DelayDiscTimerCb
phLibNfc_RFParaUpdateComplete: Failed
phDnldNfc_eSEPwrCfgAfterVenReset:Failed to invoke Dnld Ese power Config Sequence
phLibNfc_Mgt_GeneralNtfRegister: Invalid input parameters
phNciNfc_ChkPresExtnRsp
Timeout:pNciCtx->dwNtfTimerId
phNciNfc_PrbsTest
Registering for RF Data packets
phNciNfc_ProcessDeActvState
phLibNfc_Validate_IoctlParam: NULL call back
Connector - Check Expected Packet Type
bModeCeA 
RF Tech and Mode:NFC_KOVIO_PASSIVE_POLL_MODE
phHciNfc_RegisterCmdRspEvt:Registering for Pipe ID
Init Comp- Static feature config
phLibNfc_RemoteDev_FormatNdef
Resetting Logical conn
SMB Get Logging response received with invalid payload length
phDnldNfc_SpmiClientResetDelayCb: SPMI Reset Client Retry Status =
SENSB Response:
Lower layer has returned status NFCSTATUS_MULTIPLE_TAGS
Ioctl_SetRfConfig: Invalid input parameters
phDnldNfc_SecureSEDisableComplete: Invalid LIBNFC context!!
phLibNfc_FwVerDelayTimerStart: Dnld Ese Get Fw Version Timer failed to start
RF Tech and Mode:NFC_F_ACTIVE_LISTEN_MODE
phLibNfc_SM_Dnld_eSE_TrnscvTransCmplt
phLibNfc_SM_SetSETransStatus
phLibNfc_ModeSetHciNwk
phLibNfc_SetNfceeModeSeqEnd
phFriNfc_Felica_HRdAttrInfo
phLibNfc_PropMultiTagStatNtfHandler-Corrutped MultiTag NTF received, Reset/Boot MW
GetRfCalSignedData: Sequence failed!
phNciNfc_TagRemNtfClearRemDevInfo
Failed,(phNciNfc_ProcessActvNtf)Wrong ntf payload length\n
phLibNfc_DebugLogInfoNtfHandler: Dropping - Generic Debug Log Ntf Info
phLibNfc_ReApplyHsuBrCmd
phLibNfc_ConfigHsuBrResp: Nci Read request failed
phLibNfc_GetMultiTagInfoCmd : Libnfc Context is Invalid
Proc Iso-Dep pres chk ntf: Invalid length of payload
phHciNfc_CoreInitRxData
IoctlSwp2TestTrans: Failed
phLibNfc_RetrieveSETable
phLibNfc_SetVasCodeCfgComplete: Failed
phLibNfc_Validate_IoctlParam: Invalid Driver handle
phLibNfc_SM_TrigNfccAssertionTrans: Invalid input parameters
phLibNfc_CalSectorAddress
NFCEE Notification Type: eNciNfc_NciExpressModeStartedNtf
phNciNfc_ValidatePropConfigParams failed
phNciNfc_CoreRecvManager-Failed to Delete De-Assert Wake Up Line Timer
phDnldNfc_ProcessExtendedGetInfoPn800A1
bHciRxdErr:
phLibNfc_ConfigRoutingTableProc: Routing Table configuration failed
phLibNfc_SetRtidConfigSeq
phDnldNfc_TmlReadCommonCb
phNciNfc_CoreRecvManager4-Failed to retrieve bIgnoreWkUpRet
State Transition failed
phLibNfc_Process_Disconnect
phDnldNfc_BuildDnldEsePkt: Frame created successfully
Response/Data call back de-registration failed
TimerStartEvent:dwDnldMuxTmlBusyTimerId
phNciMuxNfc_BuildDataPktHci
phLibNfc_L2EventProc: L2-eDebMgmtL2Tech
phLibNfc_ParseWupIotReconfigStage
 Invalid Device Handle Param..
phNciNfc_GetGenDbgLogRsp: Response received with failure status
phDnldNfc_MapBinToDnldFrame: pDnldCtx->nxp_nfc_fw_len - 
phLibNfc_Verify_5_0_CrcStatus_NewLayout
phNciNfc_PollMgmt
Invalid input parameters!
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyEPipeNotOpened received
phNciNfc_TurnRfOnOffPropCmdRsp
Received next Rtng ntf with more set to '1'
phFriNfc_Desfire_WrNdef
SensF Resp Length
phLibNfc_GetEepromParamsProc
phLibNfc_SM_GetSpmiCfgRegsTrans
phLibNfc_UIDNotMatchingCb
aHighLayerRspCeB 
TmlReadCommonCb: Received either invalid 'pInfo' or TML Read                                    call back with status failed
Invalid input Parameter
phDnldNfc_BuildDnldEsePkt : Failed to create start timer
 Invalid Notification!!
phLibNfc_UpdateStaticPipeInfo
phNciNfc_NfceeConnCb:Retrieving logical connection id for secure element failed
aDataRateMaxCeB[0] 
Invalid parameters (phNciNfc_DeActivateRsp)\n
phDnldNfc_GetSecureFwInfoAfterVenReset
phNciCoreMuxNfc_HciBuildHcpFragment
Power State - Switch OFF :
phNciNfc_CoreRequestTmlRead
phNciNfc_CoreBuildCmdPkt:Build Command packet failed!
phNciNfc_ProcessModeSetDisableNtf
phNciNfc_SwpTestNtfCb:Swp1 power mode: PMUVCC = 1.8V
phLibNfc_SM_DeactivateTrans
phNciNfc_GetSwioPadVoltage
phNciNfc_CoreUtilsValidateGID
Set Routing Table Config sequence could not start!
phHciNfc_CreateSETranseiveTimer
Received VasUpPayload size exceeded Max vas code length. Hence resetting length
phLibNfc_GetFwTypeProc: operation success
phNciNfc_ChkPresExtnNtfCb
phNciNfc_GetSetCustFactCfgRsp - Response Successful
Listen A Platform config Value:
phDnldNfc_DnldEsePwrCfgCmd:Get FW ver Response Failed!!
phNciCoreMuxNfc_DnldEseTx:Failed to create start timer
phLibNfc_SM_Main_PollDiscoveredTransComplete:Invoking callback, wStatus = 
phLibNfc_HciDeInit:Invalid HCI Context
phLibNfc_HciDataSendProc:SE Get Atr Timer Deleted
phDnldEseNfc_GetPipeIndx
phDnldNfc_DnldPrevSessnStateCb: Session State Rsp Buff Invalid...
phTmlNfc_WriteAbort Status
phHciNfc_CoreGetNewNode:Memory allocation failed while creating new node!
\n\nTimer expired: Failed to restarting timer
phNciNfc_DetTagRemCmd
phLibNfc_DeInitializeProcess
phLibNfc_SM_ResetNtfTrans: Received reset notification triggered by Hardfault
phLibNfc_SM_GetSuicaSysCodeTrans: Failed
phLibNfc_PrintSendData: phHal_eMifareInvalidCmd
phLibNfc_TrimmingErrorNtfHandler: Dropping - Trimming Failure Info Ntf
phLibNfc_UartCommnErrorHandler: Dropping as no Registrations Exist
phLibNfc_GenericErrorHandler: Generic error received: MULTI_TAG ERROR
phHciNfc_ProcessClearAllPipeNotifyCmd:UICC
phHciNfc_ProcessEventsOnPipe: Unknown HCI Event, Dropped Ins
phLibNfc_SM_GetEraseCounterTrans
phDnldNfc_InitImgInfo: Invalid input buffer !!\n
phLibNfc_ReActivateMFCComplete
phLibNfc_GetCoreDumpLogCmd
phDnldNfc_GetNfccEseHashDumpVenResetTimeoutCb:Invalid Context
 Cannot Extract Rf Device Handle!!
phNciNfc_CoreUtilsValidateNtfPktOID
phNciNfc_SetNfccParams: Invalid eNfccParam
phDnldNfc_DnldEseSmbCfgCb:Unsuccessful status/invalid response  received!!
phLibNfc_SM_SetHceParamsTrans
NCI Receive Current State
phLibNfc_RFParaUpdateCmd : Libnfc Context is Invalid
phLibNfc_SetSuicaEntrySysCodeCmd
phNciNfc_StoreListenAParams
phNciNfc_GetFwType: Invalid parameters
Listen NFC-DEP ATR-RES Gen bytes:
Rf interfaces: NFCEE DEP RF interface
phUtilNfc_RetrieveDnldCoreCtx
phLibNfc_SM_IoctlVenResetTrans
phLibNfc_Mgt_ConfigRoutingTable: Feature not supported
PIPE ID
phLibNfc_GetPowerTrackDataSeqComplete: Failed
phLibNfc_RawCtrlMsgTrnscvCmd: Libnfc Context is Invalid
Registering for response message...
Invalid Nfc-A SEL_RES length
phLibNfc_SpmiClientResetTimerStart: Invalid Download core context
phLibNfc_ParseHrdFltDumpInfo: dwSfar
phNciNfc_RfFieldInfoNtfHandler
phNciNfc_ChkPresExtnNtfCb:Target is still in the field
phNciNfc_SetVasCodeRsp
Memory allocation for Remotedevice information failed
phLibNfc_ConfigHsuBrResp: Failed to configure NFCC HSU baud rate
phDnldNfc_SecureBootEnterDnldModeSeq:Get Secure FW Info Response Failed!!
phNciMuxNfc_BuildDataPktHci1-Failed to Assert Wake Up Line
NFC F LISTEN Techn Specific Params - START
phFriNfc_MifStd_H_CallConnect
phLibNfc_H_GetFSC
NFCEE Notification Type: eNciNfc_NciRfRapduSentNtf
phNciNfc_GetRtngConfigNtfCb
phNciNfc_ValidateAidBasedParams
Deactivate ntf timer restarted for extended time\n
Forcing FW update even if the version is same !!\n
phLibNfc_ParseHrdFltDumpInfo: dwMSplim_s
phLibNfc_LoggingNtfHandler:Failed to allocate memory for Reader Mode MultiTag events
phNciNfc_TriggerNfccAssert
Version Not Updated After Download!!\n
Get Hash Dump FAILED!
phLibNfc_Verify_5_1_CrcStatus
phLibNfc_ParseHrdFltDumpInfo: dwBfar
UICC Conn Pipe Updated Status- Open
phNciNfc_ResendTimerCb:Resend Failed, Unknown Message Type
phFriNfc_MifStd_H_AuthSector
phLibNfc_GetLpcdConfig
Length and Value is:
Invalid ISO15693 UID length
Patch Table Crc is NOT OK!!
phNciCoreMuxNfc_eMuxEvtDnldRspTo: Dnld Response timeout, re-transmit the frame!!
phHciNfc_CoreRecvCB:Invalid Information received from lower layer 
phLibNfc_SM_SE_eSERawTransceiveTrans
Invalid Core context!
phLibNfc_ISO_14443_3B_AttribResp
phNciNfc_SetVasCodeCmd
Uid Length is greater than 10(0x0A) byte so only 10 bytes will be printed
phLibNfc_InitializeComplete :pGenericNtfCb[XTAL Start Error]
phLibNfc_SM_WriteNdefTrans
phLibNfc_ChkT2Ttag
phLibNfc_SearchDnldTable
phLibNfc_HciSetAllowList: Setting SE2 Se Allow list
phLibNfc_TrimmingErrorNtfHandler
phNciNfc_ProcessGenericErrNtf
phLibNfc_GetMemoryDumpSeqComplete
phDnldNfc_MemDmpVenResetTimeoutCb:Invalid LIBNFC Context
phLibNfc_PrintLibNfcCritInfo: Invalid Controller Type 
ATR_REQ - DID shall not be used 
phFriNfc_Desf_HWrCCBytes
phNciNfc_GetLpcdCount: Stack not initialized
phNciNfc_GetGenericDbgLogInfo: Invalid parameters
phNciNfc_RfExtTempNormalNtfHandler
phLibNfc_NfceeInitializeComplete:Could not start!
phLibNfc_CalcFieldStrength
phLibNfc_RfXtalErrNtfHandler
phLibNfc_GetGenericDbgLogProc: Failed to allocate memory
phNciNfc_GetRfErrorStatus
M1 Fallback NEXT ADDRESS
Nci context null (phNciNfc_SwptestNtfTimeOutHandler)\n
FAILURE, IOCTL/DNLD Context is Invalid
phLibNfc_GetEraseCounterCmd
phNciNfc_ValidateSmbCfgParams failed
Transceive timeout is greater then default, value 
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_RF_FRAME_CORRUPTED
phDnldNfc_DnldGetVersionCb : DnldGenNtfCb
phLibNfc_GetSEPipeStatus
 Mf Auth Pass ..
phNciNfc_SendRfOnOffCmd:Failed to allocate memory, insufficient resources
phDnldNfc_DnldEseSmbCfgCmd:Couldn't get the FW version
phLibNfc_SM_Dnld_eSE_PwrSmbCfgTrans
LPCD Assistance mode is not applicable for this platform
phLibNfc_PrintSendData: phHal_eMifareRead16/phHal_eMifareRead
NFCEE Notification Type: eNciNfc_NciSuicaTxNtf
phNciNfc_Notify
phNciNfc_GetTxValue
phNciNfc_ConfigDeactvDelay
phDnldNfc_DnldEseEnableCB
phLibNfc_Mgt_ConfigCustFactoryPage: LIBNFC Not Initialized
phLibNfc_GetSwio2VoltageCmd: Invalid parameter, Libnfc Context is Invalid
phDnldNfc_CoreInit : Dnld Mux Tml Timer Create failed!!
phDnldNfc_BuildHdllPkt:DNLD Read Address
phFriNfc_Desfire_ConvertToReadOnly
Response call back de-registration success
phLibNfc_GetSecureFwInfoComplete
phNciNfc_LogConnGetMaxPld:Connection Maximum Data payload size Found!!
phLibNfc_Process_ConfigDisc
phLibNfc_NtfRegRespCb: Ignoring HCE Activation in Express + HCE mode 
phDnldNfc_DnldVldtCrcRcvd
Get erase counter Info failed!
phNciNfc_GetRfCalDataCompleteSequence
Log Request Failed!!
Expected Payload Mismatch
phNciNfc_GetConnMaxPldSz
phLibNfc_FlushSramDataProcess
Invalid Request Mode 
ProcessEventsOnApduPipe:pSeListenerNtfCb[OS Reset Ntf during Warm reset]
Read SWIO voltage Info failed!
phFriNfc_MfStd_H_NdefComplSect
phNciNfc_InvokeMfwCommonNtfCb
phNciNfc_ProcessCommonNciRsp1
phHciNfc_HciCoreLowerLayerSendCb:Invalid HCI Context received from Lower Layer 
phLibNfc_SM_Main_PollDiscoveredTransComplete
phLibNfc_AntennaTestResp
phLibNfc_ClearMultiTagInfoCmd
phLibNfc_Ioctl_GetSpmiConfigRegs: Invalid IOCTL context
Calculated CRC: 
phLibNfc_HCERemoteDev_ReceiveCb
phLibNfc_RelaydetectionNtfHandler
Chk Pres ntf timer start FAILED\n\n
phNciNfc_CompleteGetConfigRaw
phDnldEseNfc_UpdateRsp: SMB logging received payload size more than expected
phNciNfc_GenDbgLogNtf: Received More than expected length
phDnldNfc_GetSecureFwInfoAfterVenReset:Invalid Context
Invalid send payload buffer or length!
Invalid Rf Techn and mode
phLibNfc_T3tChkPresComplete
phFriNfc_MifStd_H_CallWrNdefLen
phLibNfc_GenericErrorHandler: phLibNfc_PropMultiTagStatNtfHandler- Independent Prop Tag Detect NTF Rxd
Get Listen mode routing notification registered
phDnldNfc_DnldLogCb: Invalid IOCTL context!!
phLibNfc_NfceeDisableSE2: Busy stats returned from NCI
phLibNfc_SM_GetStackCapTrans
Connect Sequence failed!
End Marker Area Crc is NOT OK!!
**** LibNfc Major version **** 
phLibNfc_eSE_Transceive: Send or Receive data invalid
phLibNfc_ReDiscoveryComplete: All retries for set config Failed
phLibNfc_L2EventProc: L2-bExtraInfo
Set Config parameter validation failed!
phNciNfc_GetConfigRaw
phNciNfc_SetChipScopeRsp : Chip scope response received with failure status
phLibNfc_ParseWdgDumpInfo: dwHostProcessWaitObject
phNciNfc_TlvUtilsParseTLV
SPMI
phLibNfc_GetSwioPadVoltageSeqComplete
phDnldEseNfc_MultiOSGetPipeId
phLibNfc_IoctlClearAbortDnldCtx: Invalid IOCTL context!!
phLibNfc_UpdateNfceeDiscTechnType: poll Nfc-A tech supported
UICC init sequence could not start!
Rf Signed Config response signature error
phHciNfc_CoreSend:HCP Packet Sent to NCI 
phNciNfc_CoreInitialise
TML Write Failed
HCE send failed!
phLibNfc_ClearMultiTagInfoCmd : Libnfc Context is Invalid
phNciNfc_GetSwioPadVoltage: Stack not initialized
phNciCoreMuxNfc_eMuxEvtDnldTxCb
Registering for SMB Logging Notification
phLibNfc_GetNfceeSessionId: No need to poll for Session ID
phNciNfc_RecvStateHandler
Timeout:dwInitWdTimerId
FWT timeout is less than default, hence using default timeout: 
phLibNfc_IoctlSetRfCfgCmd, Libnfc Context is Invalid
Registering for Suica Mode Started Notification
phLibNfc_SM_SetHceParamsTrans:Set Host Card Emulation Config sequence could not start!
phLibNfc_SM_SetSmbNfccParamsTrans: Feature not supported on this platform
No NDEF TLV found, complete card has been read
bAfiCeB 
phFriNfc_MfUL_H_ProWrOTPBytes
phNciNfc_StorePropParams
Invalid context received from RecvMgrHdlr!
phLibNfc_Ioctl_Mgmt_CB - Nfcc & eSE power track Config complete
phHciNfc_AnyGetParameter
Buffer passed by lower layer is NULL
Response Timer Create failed
phLibNfc_ConvertToReadOnlyNdef
phFriNfc_MfUL_H_ProWrittenBytes
phLibNfc_Ndef_ReadOnly_Cb
phNciNfc_CompleteDataSequence
phLibNfc_ParseWdgDumpInfo: dwSwpProcessPc
phHciNfc_AnyGetParameterCb:Sucessfull
phLibNfc_DisableStandbyMode
phNciNfc_TmlReadCommonCb
phLibNfc_ConnectExtensionFelica_Cb: Lower layer has returned invalid LibNfc context
phLibNfc_GetNvmMemDumpProcComplete
phNciNfc_CoreRecvManager:Invoke notification call back function if registered
phLibNfc_SM_AntennaTestTrans failed
phNciNfc_CoreReSend-Fialed to De-Assert Wake Up Line
phNciNfc_SendConnCloseCmd:Setting up command Info to be sent to lower layer ..
phLibNfc_ModeSetHciNwk: NCI returned Busy status
phNciNfc_UpdateReqParamIDs
Received Erroneous Notification(phNciNfc_ProcessDiscNtf)\n
phDnldNfc_DnldCfgHsuBaudRateCb: Dnld Config HSU baud rate failed
phLibNfc_SM_Main_InitTransComplete
phLibNfc_HandleInternalEvent
Chk Pres ntf timer failed to start for extended time\n\n
phDnldNfc_DnldLog: Invalid IOCTL/DNLD context!!
phDnldNfc_DnldGetNfccHashDataRsp - Successful
 Invalid Param..
beSEStatus:
[Timeout] hMultiTagNtfWaitTimerId
phLibNfc_JewelMap
phDnldNfc_UpdateRsp:First Success READ, Midpoint0 read NEXT ADDRESS
dwSwpNtfTimerId
Svdd On Control Sequence failed!
phLibNfc_DummyDisc: Failed to start Timer!
phLibNfc_StartRtidDiscSeq
phLibNfc_HciDeInit
phLibNfc_VerifyRxdRtngTable: Routing Table configuration Success
End of list reached
phNciNfc_PollMgmt: Invalid input parameters
NCI Send busy[DNLD]
phLibNfc_eSePowerCycleSetModeSeqEnd
phLibNfc_GetEraseCounterProc: received failed status or invalid response length
Presence check (extension command) failed!
phHciNfc_CoreDeInit:phHciNfc_ReceiveAdminNotifyCmd unregistered for ADM Cmds
phHciNfc_VerifyIfRegistered
Invalid parameters (phNciNfc_Transceive)\n
phNciNfc_IncrConnCredits:Credit Limit exceeded for this Conn,Rounding to max value ..
LibNfc:tSeList[phLibNfc_SE_Index_UICC].eSE_Type=
phLibNfc_SM_GetFwVersionTrans: Update Client-ID to Secondary Client ID(0x0B)
phFriNfc_Desf_HSendTransCmd
phLibNfc_UpdateSeInfo- Virtual Mode = Recovery Started
phLibNfc_GetClrAssertComplete: Invalid LibNfc Ctx
RAM AO Only Area Crc is NOT OK!!
phNciNfc_PrintNfceeDiscreqNtfDescription
phLibNfc_Mgt_ConfigureLogging: Feature not supported
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyENok received
phLibNfc_ProcSysL1LogStandbyNtf: L1-phNfc_SysL1LogEntry.StandbyEvent
Stack not initialized (phNciNfc_Connect)\n
Interface err received, initiating RecvStateHandler with 'NFCSTATUS_RF_ERROR' status
phNciNfc_DecrConnCredit:Connection Credit Info Found!!
phLibNfc_SM_GetTrimVerTrans: Get Trim Version not supported on this platform
phLibNfc_SpmiStsRegInfoNtfHandler :pGenericNtfCb[Spmi Status RegInfo ntf]
phNciNfc_ValidatePropConfigParams
phNciNfc_SetChipScopeCmd
phLibNfc_IsShutDownInProgress
phLibNfc_CommonSeqProc
phNciNfc_CoreExtractData
phNciNfc_GetSwitchRFCfgRsp
phNciNfc_WaitCreditTimerCb - Credits-
phHciNfc_CoreInitialiseContext
Discover Frequency:
phLibNfc_GetMemoryDump
phLibNfc_MultiTagGetFwTypeProc
phNciNfc_GetGenericDbgLogInfo: Insufficient Memory 
phDnldNfc_UpdateRsp:EDL_CERT_ERROR:Error during Certificate frame processing
Invalid RfProtocol!
phLibNfc_SM_IoctlConfigDebugModeTrans: Invalid configuration 
phLibNfc_SM_SetMultiTagCfgTrans: Feature not supported on this platform
Invoking pClientTranscvCb...
phLibNfc_SetRfSignedSeqComplete: Invalid input parameter
phDnldNfc_DnldWriteCb [Degraded Fw Update] - NFCC Reset Successful
phNciNfc_WaitCreditTimerCb - NFCSTATUS_RF_TIMEOUT
phLibNfc_SetStandbyModeProcess
Authentication command success
Nci context null (phNciNfc_GetLstnNtfTimeoutHandler)\n
phFriNfc_Desfire_RdNdef
Rf interfaces supported: HID Rf interface
phLibNfc_GetRtngTable
Ioctl_EnableDtaMode: LIBNFC Not Initialized
phDnldNfc_ProcessExtendedGetInfoSn450Bx
Insufficient resources!
phFriNfc_Felica_HInitInternalBuf
Received System End of operation notification from NFCC
phLibNfc_Ioctl_Mgmt_CB - Ioctl Generic-A Express Set wait time after Rf Off complete
phDnldNfc_DnldGetSessnStateCb - Request Successful
phLibNfc_IoctlSetPropRfCfgComplete: NFCC Re-Init failed, return failed
phLibNfc_ParseWdgDumpInfo: dwKernelProcessSp
State machine has returned NFCSTATUS_BUSY 
phUtilNfc_SetdnldEseCoreContext
Unexpected MW Log Area Value still forcing MW config =
phNciNfc_CheckFor14443_3BPICC
Fw Download Failed!!
phLibNfc_ParseWdgTickInfo: dwWatchdog_Process_Swp
phLibNfc_UpdateRtngCfg:Update routing config failed!
phLibNfc_SM_SetHLMParamsTrans: Feature not supported on this platform
MergeSak detected, update remote device detected to P2P Target
 FelicaCmdEvent NULL!!!
phLibNfc_GetEepromSettings
phDnldNfc_DnldEseGetRemainingSmbLog:Download mode Get Smb logging Failed!!
phDnldNfc_FwVerVenResetTimeoutCb
phDnldNfc_GetSecureFwInfoAfterVenReset:Failed to start GetSecureFwInfo Sequence
Listen F T3T Flag len:
phNciNfc_PrintRfRfProtocolDescription: RFU or proprietary
phNciNfc_CoreRecvChkExptdPktType
phLibNfc_HciRawDataSend
phLibNfc_VerifyRxdRtngTable: Routing Table configuration failed
phFriNfc_MfStd_H_BlkNoToWrTLV
phFriNfc_T5T_RdNdef
EEPROM User param - wCurrMwVer
phLibNfc_staticFeatureCfgComplete
phLibNfc_ConfigRoutingTableMoreProc: Routing Table configuration success
phLibNfc_SpmiStsRegInfoNtfHandler: Dropping - Spmi Status Register Info Ntf
phLibNfc_ConfigHsuBrResp
phLibNfc_MultiTagGetFwTypeProc: Libnfc Context is Invalid
phDnldNfc_SecureBootEnterCommitModeCmd: Invalid LIBNFC context!!
 Vpp Calculation Failed!!!
phLibNfc_StopRfFieldOn
phNciNfc_ProtoIfMapRsp
Invalid call back function pointer to register
phNciNfc_SeSendCb
Release Sender State Machine failed!
phLibNfc_DummyInit
Size Of DNLD PKT
 phDnldEseNfc_HciRecvManager:Failed To Allocate Memory for Node
phDnldNfc_GetFwInfoRspDuringInit: Session State Rsp Buff Invalid...
Length of Send buffer
Memory Read Error!!,status
phDnldNfc_RecvDnldEsePkt:corrupted packet rxd and dropped
phNciNfc_ProcessCommonNciRsp1 - Response received with invalid status/payload
phLibNfc_IoctlSetRfCalDataComplete
EEPROM User param - bConfig
phLibNfc_RetrieveNvmDumpStartAddr
phLibNfc_MultiTagGetFwInfoComplete: Libnfc Context is Invalid
phLibNfc_Ioctl_Mgmt_CB - Ioctl VAS Express Set wait time after Rf Off complete
phLibNfc_Ioctl_Mgmt_CB - Nfcc CRC Config complete
phFriNfc_T5T_CB_Transceive
phNciNfc_UpdateRemDevInf
phLibNfc_Initialize: SPMI Reset Client Status =
phLibNfc_ChkRfListnerforNFCFListen
phNciNfc_CorePktSendToTml- Wakeup failed
Interface err limit reached, initiating RecvStateHandler with error status
phLibNfc_IoctlGetRfCalDataCmd
phLibNfc_CommonSeqProc:Libnfc Context is Invalid
phLibNfc_RemoteDev_ReActivate
phLibNfc_SetDiscPayload
phLibNfc_GetEraseCounterProc: Invalid data received from NFCC
phNciNfc_GetPwrTrackData: Stack not initialized
phHciNfc_ProcessPipeCreateNotifyCmd:UICC Conn Pipe Info Updated
phLibNfc_MfcChkPresAuthComplete
phLibNfc_DummyInitTimerCb: Timer stopped and deleted
phFriNfc_MfUL_ParseTLVs
phNciNfc_GetUserAreaAddress: Sequence failed!
phDnldNfc_UpdateRsp:M1 Success Address
phDnldEseNfc_GenErrNtfHandler: Error code 0x0B,SE is not enabled
Ioctl_PropGetRfRegs: Invalid IOCTL context
Failed to Register phLibNfc_PropTagRemDetNtfHandler
phNciNfc_ResendTimerCb1-Failed to retrieve bIgnoreWkUpRet
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyECmdNotSupported received
ROM Area Crc is NOT OK!!
phDnldNfc_DnldProcessDisable_EdlWMDisableSE: gphDnldNfc_EseEnabledEnterCmtModeGetSecureFwInfo sequence successful
phLibNfc_SM_ConfigDriverTrans:TML initialization failed
Reached end of user buffer
phLibNfc_SwioPadNtfHandler
phFriNfc_Tpz_H_RemainingReadDataCopy
phDnldEseNfc_GetNewNode
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_FAILED
phNciNfc_CoreInvokeCb:Registered Data call back function invoke failed-Invalid function pointer!
phLibNfc_ParseWdgTickInfo: dwCurrentSysTick
Registering for Prop Vas CW Ntf message notification
phHciNfc_ProcessPipeCreateNotifyCmd
phUtilNfc_SetDnldNfcContext
phNciNfc_SendConnCloseCmd
phLibNfc_EnDisMultiTagSeq Fail : invalid config
phNciNfc_ValidateIfActParams:type A silent TAG1 poll phase Tech and mode received
phLibNfc_EnableExtnProcess : Invalid Context or pInfo Received
phLibNfc_AntennaSelfTest: Stack Not Initialized
phLibNfc_StartDiscSeq:Discovery 'tADDCfg' empty, passing SUCCESS to caller
phNciNfc_GetAteTrimVersion: Invalid parameters
Valid DataXchg Actv Rf Tech and mode received (2)...
phDnldNfc_SecureBootEnterDnldModeRsp - FAILED 
phNciMuxNfc_MuxHandler
phHciNfc_OpenPipe:Invalid HCI Context
phLibNfc_SM_Dnld_eSE_PwrSmbCfgTrans: Failed to initialize DNLD eSE core context 
Failed to start resend timer
Valid remoteDev Handle!!
 phLibNfc_LoggingNtfHandler : Unknown L2 Message!!!
phNciNfc_NotifySpmiRegInfo: Dropped at NCI
phNciNfc_WtxNtfHandler
phLibNfc_Ioctl_Mgmt_CB - Fw Download test
phFriNfc_NdefSmtCrd_Reset
phNciNfc_GetSecureMemoryDump: Insufficient Memory 
phDnldNfc_BuildDnldEsePkt
phNciNfc_TotalPollDurationNtfHandler
phDnldNfc_GetSecureFwInfoVenResetTimeoutCb
phNciNfc_CoreRxDelayReqNciPkt: Set Rx delay failed!
phLibNfc_HciInitComplete: Static feature config sequence started
phNciNfc_ValidateSetRtngParams
Send RF On or Off command failed!
phDnldEseNfc_CoreInit : Dnld Ese Rsp Timer Create failed!!
phNciNfc_GetGenDbgLogRsp: failed!
Ioctl_LoopbackTransceive: LIBNFC Not Initialized
phLibNfc_UpdateFirmware
No routing entries
MultiTag Detection NTF Timer Restarted for extended time
phLibNfc_SetRfSettingsProc : Invalid Param
phDnldNfc_RecvDnldEsePkt:Critical failure in Download Ese mode!!
 Mifare Mini tag detected..
Get Power Track data Notification timer start FAILED\n\n
phHciNfc_ProcessPipeCreateNotifyCmd: Failed to register phHciNfc_ReceiveOpenPipeNotifyCmd
phLibNfc_GenericTransceiveResp:transceive failed!
phLibNfc_SM_ResetNtfTrans
phLibNfc_CustFactoryCfgCmd: Sending command failed
GetTransition reg resp failed
phDnldEseNfc_CrdtTimeOutCb:Invalid or NULL pDnldEseCoreCtx 
 MifareUL tag detected..
phLibNfc_Ioctl_PropSetPwrTrackConfig
RF Tech and Mode:NFC_HID_PASSIVE_POLL_MODE
phLibNfc_SM_SeGetRfParamsTrans :Failed
phLibNfc_Mgt_ValidateEepromSettings: Invalid call back function passed
OsResetRcvd_AdminPipe:pGenericNtfCb[OS Reset Ntf During Init]
phLibNfc_GetTrimVerProc: Get Trim version operation failed
Get Rtng Config Sequence failed!
Received VAS CW notification from NFCC
phNciNfc_SetSwitchRFCfgCmd: Invalid input parameter
phFriNfc_Desfire_Update_SmartTagCapContainer
phNciNfc_ListenMgmt_DeActivate
phLibNfc_ParseHrdFltDumpInfo: dwR2
RF Tech and Mode:NFC_B_PASSIVE_POLL_MODE
phLibNfc_NfceeDisableUICC: Secure Element removed 
phLibNfc_SM_Dnld_eUserFwDnldTrans: NFCSTATUS_SPMI_NACK1
phDnldNfc_RetrieveSn450vBootStatus - Invalid context
phNciMuxNfc_MuxHandler : Write Request Failed(phNciCoreMuxNfc_eMuxEvtDnldTx)
phNciNfc_PrintRfTechModeDescription:RF Tech and Mode: RFU or Proprietary
phFriNfc_T5T_H_ProcessDynamicRdNdef
phLibNfc_ListenModeDeactvNtfHandler
phLibNfc_SM_GetPowerTrackTrans: Failed
phFriNfc_OvrHal_CB_ConnectDisconnect
dwVasNtfTimer
phNciNfc_GenDbgLogNtf: Received Generic debug Logs notification from NFCC
Libnfc sync handler Timer Create failed!!
phDnldNfc_DnldGeteSEHash1DataCmd
phLibNfc_ParseHrdFltDumpInfo: dwS_mmfar
RF NFCEE Action len:
phLibNfc_SM_Dnld_eUserGetDieIdTrans: TML Config Baudrate failed status
phLibNfc_ConnIsRfListnerRegisterd
phLibNfc_ConfigAssertLoggingSeqComp: Failed
phNciNfc_TriggerNfccAssertCmd
phNciNfc_SwpTestNtfCb:Swp1 power mode: PMUVCC = 3.3V
Failed to start credit ntf wait timer with extended time!
phHciNfc_ReceiveAdminNotifyEvt:Failed, Invalid Context or Info received
phUtilNfc_SetIoctlContext
phLibNfc_ConfigLoggingSeqComp: Failed
phLibNfc_GetSuicaSysCodeComplete: Invalid LibNfc context
 phNciNfc_ChkDataRetransmission: Invalid Nci Context or status param
Listen F T3T Flag Value lower byte:
phLibNfc_SM_CofigRtngTrans
phLibNfc_GetLpcdConfigProc- SUCCESS
\n\nTimer Count
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_NotInitiatlized
phLibNfc_GetPageCountProc: received failed status or invalid response length
Input parameter validation failed
phFriNfc_Tpz_H_ActualCardSize:Maximum Ndef Message size
Listen ISO-DEP INFO RESP:
RF NFCEE Action Value:
phFriNfc_MifStd_H_RdTLV
phFriNfc_Desfire_Reset
Session Id is not retrieved in 10 tries 
Stack not initialized (phNciNfc_PropConfigClrMultiTag)\n
RF Interface: Tag-Cmd RF Interface
Command packet:
phNciNfc_CorePktSendToTml
phLibNfc_eSE_Transceive:Hci Transceive sequence could not start!
phLibNfc_HciDataSendProc:Invalid HCI Context
phLibNfc_ProcSysL1LogDpcEventNtf
phNciMuxNfc_InitiateNextPkt
phDnldNfc_BuildSecureDnldEseHciPkt
RawFrame Request Failed!!
phLibNfc_ProcessDevInfo: status returned is other than success wStatus
phDnldEseNfc_UpdateRsp:Secure Platform Unsuccessful Status received!!
phFriNfc_Desfire_ReadBinary_NdefLen
phLibNfc_Ioctl_Mgmt_CB - Swp2 test complete
Credit wait timer started with extended time..
phHciNfc_AddRegistration:Failed, Invalid List or Callback
phLibNfc_SM_DisConnectReStartTrans
Card is Read-Writable
FindResBytePosition
phLibNfc_DiscDeactivateComplete
phDnldNfc_DnldChkIntegrity: Invalid LIBNFC context!!
phDnldNfc_GetSecureFwInfoAfterVenReset: Enable download mode failed
phNciNfc_Recv4BResp
phLibNfc_SM_IoctlSetSpmiGpioTrans
SeModeSet/DelayForSE Ntf timer is still active, stopping and deleting the same
Failed to Open logical connection in loopback mode
Notifications instead of response for download mode EDL group commands indicate failure 
phDnldEseNfc_GenErrNtfHandler: Error code 0x11,SE Identity Management Pipe deleted
phNciNfc_SendPrbsTestCmd
phLibNfc_PropMfwRawCtrlMsgNtfHandler
ISO DEP interface mapped to wrong protocol!
Trim Data Crc is NOT OK!!
phHciNfc_CoreInit:Invalid Context
phLibNfc_SE_SetMode
Notifying upper layer...
phNciNfc_DetectTagRemoval: Invalid parameters
phDnldNfc_ChkIntVenResetTimeoutCb:Invalid or NULL download core context
phHciNfc_HciCmdRspCb : HCI Command Response Packet Timer Expired
eRfDeactvType -> phNciNfc_e_DiscMode
phLibNfc_SM_SetChipScopeCfgTrans: Failed
NCI Core Receiver State Machine Init Failed
Invalid IOCTL context
LPCD Assistance mode cannot be enabled without CE/express/RF Detect enabled
Found pClientTranscvCb as valid
SMB Get Logging command Semantic error received
phDnldNfc_DnldEseGetRemainingSmbLog:Response Timer Start failed!!!
phLibNfc_HciSetAllowListProc: Successful
phLibNfc_HciRawDataSend: SE TxRx Timer Started with Timeout
phLibNfc_AntennaTestResp: no of configs none
phNciNfc_MfCreateAuthCmdHdr
phNciNfc_StateIdle2Dummy
phLibNfc_MapDesfireTagType
phFriNfc_MfUL_H_Wr4bytes
aATQBCeB[2] 
NFCC Configure HSU baud rate success
ChkPresence Extn: invalid ntf
RF Tech and Mode:NFC_F_PASSIVE_POLL_MODE
phFriNfc_MifStd_H_RdtoWrNdefLen
phFriNfc_Desf_HWrNDEFData
phLibNfc_GetSwio1VoltageCmd: Invalid parameter, Libnfc Context is Invalid
Presence check extension command accepted by NFCC
phNciNfc_ValidateProtoBasedParams
phNciNfc_RegUnRegSeEvent: Failed to register with Nci core
phDnldNfc_UpdateRsp:CHUNK READ ERROR ADDRESS
phFriNfc_MfStd_Format
phDnldNfc_DnldGetVersion - Invalid libnfc context!!
eRfDeactvType Other
phLibNfc_Mgt_SetCE_ConfigParams
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_ErrorNotDefined -Unknown error code
phDnldNfc_BuildHdllPkt : Inserting FrameId ..
phDnldEseNfc_ProcessConnPipeEvts:Failed,BER TLV parsing, Length Mismatch
phDnldEseNfc_HciRecvManager: Recvd HCP Pkt > PHDNLDNFC_ESE_HDLL_HCP_MAX_PACKET_SIZE
 Kovio tag detected..
phDnldNfc_SecureBootEnterDnldModeCmd: Invalid LIBNFC context!!
phFriNfc_T5T_WrNdef
phLibNfc_SetHostCECfgs: Invalid status -CE Host configuration failed to send
phNciNfc_SpmiRetryWakeup
phLibNfc_ReActivateMFCComplete1
phDnldNfc_GetFwInfoRspAfterEseDisable: Session State Rsp Buff Invalid...
phLibNfc_GetMemoryDumpCmd: Invalid IOCTL context!!
 Unexpected Mf Write Response Received ..
phLibNfc_Ndef_Write
eSE reader mode Invalid Input Parameter
phLibNfc_RelaydetectionNtfHandler: Received Length is zero
Failed to create Timer!
phDnldNfc_DnldGetNfccHashDataCmd
phLibNfc_MapRemoteDevHandle: Failed to map handle
phLibNfc_ReInitDisableNfceeDisc: Stopping NFCEE Discovery
phNciNfc_CoreSendCb:Send success
HciEvtEndofOptRcvd: Evt End Of Operation received
Invalid input parameter (phNciNfc_ProcessDiscNtf)\n
phDnldNfc_DnldGetSessnStateCb
phLibNfc_IoctlSetRfCalDataCmd
phDnldNfc_MemDmpAfterVenReset:Invalid Context
RF Protocol:PROTOCOL_NFC_EPCGEN2
phLibNfc_SpmiClientResetDelayCb: SPMI Reset Client Retry Status =
phLibNfc_SM_IoctlEnableDtaModeTrans
phLibNfc_Mgt_FMM_GetHashDump: None of the hash data requested
Invalid message type
phHciNfc_CoreDeleteList
 FelicaSysCode NULL!!!
phLibNfc_SetEepromStngsProc :Invalid LibNfc Ctx
phLibNfc_PropRdrNtfHandler:RF_ON followed by VAS (Exp Non Entry) received hence propagate VAS NTF to upper
phDnldNfc_BuildDnldEsePkt:Invalid Input Parameter!!
phLibNfc_Ioctl_Mgmt_CB - Ioctl Config Swio Sens periodic timer complete
phNciCoreMuxNfc_TmlBusyCb
Invalid Protocol from Upper Layer
phLibNfc_HciResponseTimerRestartRequestNtfHandler: SE TxRx Timer Re-Start Failed
phLibNfc_GetNvmMemDumpProcComplete: SUCCESS!
Lifecycle Validity Error Status received!!
phDnldNfc_GetFwInfoRspAfterEseDisable - Protected Page Status is 
bNciRxdNtf:
Discovery Configuration Mode: DH is the only entity that configures the NFCC
phLibNfc_SM_Dnld_eSE_GetSmbTransCmplt:host Callback Invoked
phLibNfc_SM_IoctlSwp2TestTrans
phFriNfc_OvrHal_CB_Transceive
phLibNfc_FindTagTypeFromSak
phLibNfc_SetSuicaEntrySysCodeCmd : Libnfc Context is Invalid
phNciNfc_InvokeMfwCommonNtfCb : Invalid Context
phLibNfc_ProcessNfceeDiscRsp
phLibNfc_SM_GetNfccEseHashDumpTrans: Failed
phLibNfc_SM_EMVCoTagRemDetTrans
phLibNfc_SM_CheckNdefTrans: Unable to Retrieve NDEF context
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_RfFrameCorrupted
phNciNfc_CoreInit
phDnldEseNfc_UpdateRsp:Invalid Context!!
phNciNfc_SetSwitchRFCfgRsp: Set switch RF config response received with failure status
phFriNfc_MifareUL_H_Complete
 Zero credit Ntf Received
Aborting Format NDEF
Sending through admin pipe, os_reset_Acknowledgement for OS @
phLibNfc_SetHLMCfgCmd
phDnldNfc_SecureBootEnterDnldModeCmd: Request Failed!!
Ioctl_SetRfCalData: Feature Not supported
phNciCoreMuxNfc_TmlBusyCb:Mux TML busy timer expired
RF Tech and Mode:NFC_A_PASSIVE_POLL_MODE
phHciNfc_ReceiveAdminNotifyEvt:Rxd phHciNfc_e_EvtHotPlug
phLibNfc_staticFeatureCfgComplete :pGenericNtfCb[PLLLostlock]
phLibNfc_GetMfUlcReadPageResp
 Invalid Oid received..
phLibNfc_Ioctl_NfccTimerCfg: Invalid IOCTL code!
Listen A Select info len:
 Invalid SENSB_RES Length received..
 Failed to get Conn details for index..
phLibNfc_HciDataSendProc:SE TxRx Timer Deleted
phLibNfc_VldtEepromCheckComDiscParams
phDnldEseNfc_CoreInit : Timer Create dwCrdtTimerId!
phDnldEseNfc_RspTimeOutCb
phLibNfc_IoctlGetSpmiGpioProc
phLibNfc_ProcessCoreInitRsp:Core init response failed
phLibNfc_SE_NtfRegister
phLibNfc_IoctlSetRfCfgCmd
phLibNfc_MapRemDevType
phLibNfc_SM_GetRandomDieIdTrans
phNciNfc_NfceeDiscNtfHandler
phFriNfc_MifStd_H_ChkRdWr
phLibNfc_RssiStatsHandler :pGenericNtfCb[RSSI STATS ntf]
phLibNfc_GetSwioPadVoltageProc: received failed status
phLibNfc_RfLpcdAssistExitNtfHandler :pGenericNtfCb[Lpcd Assistance Exit Ntf]
phNciNfc_InitGenErrorNtfCB:Notification invalid..
phLibNfc_SM_Dnld_eUserFwDnldTrans: Update Client-ID to Secondary Client                                ID(0x0B)
phDnldNfc_DnldRecover: Invalid IOCTL/DNLD context!!
LibNfc:tSeList[phLibNfc_SE_Index_eSE].eSE_ActivationMode=
 T3T Poll Req Failed ..
phLibNfc_PrintSendData: phHal_eMifareReadSector
phNciNfc_GetConfigRsp: Request Number of Parameters not matching with received Parameters
phNciNfc_GetMultiTagInfo
phNciNfc_RawCtrlMsgTransceive: Stack not initialized
phNciNfc_ProcessActvNtf
phLibNfc_Ioctl_ConfigDebugMode
phDnldNfc_GetDieId : Invalid IOCTL/DNLD Context!!
phLibNfc_IoctlGetSpmiGpioComplete: Failed
phLibNfc_SM_SE_eModeSetVirtualToPwrOffTrans
phLibNfc_SE_RawTranseive: Invalid input parameters
phLibNfc_SetRfSettingsSeqComplete: Invalid input parameter
phLibNfc_AntennaTestSeqComplete
phNciNfc_DeactNtfTimeoutHandler
phLibNfc_DnldGetFwVersion: Request Failed!!
phLibNfc_UpdateRtngCfg
phNciNfc_SetRfCalSignedData
phFriNfc_Desfire_Process: Current NDEF message exceeds the Maximum Tag NDEF size
phHciNfc_ProcessPipeCreateNotifyCmd:Unkown Source Host ID
phLibNfc_ConfigRoutingTableProc: Routing Table configuration success
phLibNfc_SM_GetTagTypeTrans
phLibNfc_Mgt_Initialize
RALL response received
phLibNfc_RfXtalErrNtfHandler :pGenericNtfCb[XTAL Start Error]
phLibNfc_GetVasCodeCfgComplete
phDnldNfc_DnldGeteSEHash1DataCmd: Request Failed!!
Reset status: SUCCESS
Incorrect Memory control TLV values
NFCEE Notification Type: ACTION
phLibNfc_SetRfSignedSeqComplete:NFCC hard reset happened, performing Re-Init
phLibNfc_ConfigTestModeOffRspCb: Failed
phDnldEseNfc_ProcessApduPipeEvts
phDnldEseNfc_ProcessConnPipeEvts:Se notification callback is NULL
phNciNfc_RdrAInit
phLibNfc_ReleaseMemory
phNciNfc_CoreWakeupMgmt
phNciNfc_RfPlllostlockNtfHandler
phLibNfc_Ioctl_SpmiVgpioDbgLogCfg
phDnldNfc_DnldGetSecureFwInfoRsp - Invalid Hardware Version!!
phDnldNfc_DnldGeteSEHash2DataRsp
phLibNfc_SM_PiccActivatedTrans :Received ACTIVATED NTF
phDnldNfc_InitImgInfo: FW Image Length - 
phLibNfc_ConfigSeReaderEmvCoSeq
phLibNfc_SetRfSettingsCmd
Get Power Track data Notification timer failed to restart for extended time\n\n
phNciNfc_CoreSend2-Failed to retrieve bIgnoreWkUpRet
No target is connected
phLibNfc_SetEepromStngs
phNciNfc_GetConfigRsp
Transceive timeout value  
phDnldEseNfc_GenErrNtfHandler: Error code 0x10,SE loopback Pipe deleted
phNciNfc_GetSmbLogSeqComplete
phLibNfc_Ioctl_ClearSpmiErrorRegs
phLibNfc_RemoteDev_ClearInfo
phDnldNfc_SecureUpdateRsp: Unexpected Notification received 
Read Internal Register failed!
Get Rf calibration data signed passed
phLibNfc_SpmiClientResetTimerStart: Client reset Nack Timer Started
No Dbg Info added for this Remote Device Type
phNciNfc_PrintTechNfcBSpcfcParamsDescription
phLibNfc_InvokeNciTranscvComplete
phLibNfc_SM_Init
phLibNfc_ProcessReDiscReq
phDnldNfc_DnldCfgHsuBaudRateCb : Config Hsu Baud Rate failed Status 
phLibNfc_Ioctl_GetRfCalData: Feature Not supported
phHciNfc_CoreRecvCB:Buffered Received Chained HCI packets
phLibNfc_SM_ConfigPowerModeTrans
phLibNfc_DelayForSeNtfProc
phLibNfc_GetSwitchRFCfgComplete
phDnldNfc_GetFwInfoRspAfterDnldWrite - Failure status returned from lower layer or Invalid libnfc context or invalid info received!!
phLibNfc_ParseHrdFltDumpInfo: dwLR
phLibNfc_ReInitializeComplete
phLibNfc_SM_Dnld_NfccResetTransCmplt: Download mode Generic Notification not registered
phLibNfc_FelicaReqResCmd
phDnldNfc_CoreInit : Timer Create dwDnldRspTimerId!
phDnldNfc_SecureBootEnterCommitModeCmd: Invalid IOCTL/Dnld context!!
dwUsrAreaEndAddr:
Invalid or Proprietary TLV Type! It is
phLibNfc_SetVasCodeCfgCmd
phNciNfc_RegRfDataPkt
phNciNfc_CoreRecvNciHeaderCb
phNciNfc_CoreBuildCmdPkt:Max Control Payload Length is not available !!!!!
phFriNfc_Desf_HReadOnlyWriteCCFile
phLibNfc_L2EventProc
phLibNfc_GetHlmDbgLogProcComplete
phNciNfc_CoreDeRegNciRes
phDnldNfc_eSESmbCfgVenResetTimeoutCb:Invalid or NULL Context
Timer Create Failed for pLibContext->tConnectCtx.dwConnectTimerId
phLibNfc_SM_TrigNfccAssertionTrans:Invalid Assertion type
Waiting for Test Swp notification...
Failed to perform phDnldNfc_CoreDeInit!!
phFriNfc_T5T_ReadRemainingInMultiple
phLibNfc_SM_GetClrAssertRegsTrans: Invalid input parameters
phLibNfc_SM_IoctlGenAWaitTimerOffTrans
phNciNfc_ProcessCustFactPageNtf: Failed to allocate memory
Perform Degraded Fw update\n
Download Image Primitives extraction failed!!
pLibNfcHandle->dev_cnt == 
phLibNfc_DelayForSeNtf: Delay Timer(ms) 
phDnldNfc_DnldEseValidateRxdPkt
Building Header bytes for Deactivate Command
Function Table Area Crc is NOT OK!!
Resend Count Reached
phNciNfc_ProcessSysL2DbgMsgNtf
Ioctl_PropGetRfRegs: Feature not supported
phLibNfc_Ioctl_GetSpmiErrorRegs: Invalid IOCTL context
phLibNfc_Ioctl_Mgmt_CB - Ioctl DTA mode Complete
phLibNfc_SM_Main_ShutdownTransComplete
phLibNfc_Mgt_ConfigCustFactoryPage: Invalid input parameters
phFriNfc_MifareUL_iRoNdefWriteCC
phLibNfc_SetconfEntryCheck
phNciNfc_WtxNtfHandler: Received WTX_NTF
phLibNfc_SM_IoctlSwioPadVolNtfTimerTrans: Failed
phLibNfc_HciRawDataSendProc
phLibNfc_GetNvmMemDumpProcComplete : Status Failed or Invalid pIoctlCtx
Received Express Mode started notification from NFCC
####phLibNfc_VerifyCtxt: DriverHandle
phLibNfc_DnldEsePwrCfgSeq
phLibNfc_SM_IoctlIoctlSetRfConfigSignedTrans
phLibNfc_Mgt_TriggerNfccAssertion
HCE detected as remote device type, try priority discovery
phLibNfc_GetClrAssertComplete
Clear Multi tag List Sequence failed!
phDnldNfc_DnldLog: Invalid LIBNFC context!!
Ioctl_PropSetConfigSigned: Feature Not supported!
phLibNfc_GetTagTypeSeqComplete : Failed with Status code
LPCD Trace mode is not applicable for this platform
phLibNfc_ChkRfListnerforNFCAListen
phLibNfc_GetEraseCounterSeqComplete:  Invalid LibNfc Ctx received from NCI
phHciNfc_HciCoreLowerLayerSendCb
phLibNfc_SM_Main_IdleTransComplete: phLibNfc_SM_eIoctlSetSysConfig:Invalid IOCTL context!!
Resend timer started
Generic-A Express is wrongly enabled
Version Already UpToDate!!\n
phNciNfc_GetFwIntVerCompleteSequence
Registering for Discover Notification
Invalid input Se Handle
phLibNfc_RemoteDev_ChkPresence_Cb:Lower layer has returned Invalid Buffer Length!!
Found pClientNfcIpRxCb as valid, invoking the same
phLibNfc_Compute7816ClifTech
 Invalid Send Buff Params. (phNciNfc_Transceive)\n
phNciNfc_SetSwitchRFCfgCmd
phDnldNfc_DnldEsePwrCfgCmd:Unsupported Secure Boot Platform
Registering for Get power track data Notification
phLibNfc_PrepareConnect_Iso15693
phFriNfc_MifareUL_iFndNdefCompReadOp
Discovery started...
RF_NFCEE_DISCOVERY_REQ_NTF Payload Contents:
phNciNfc_PrintTechNfcFSpcfcParamsDescription:NFC F POLL Tech Specific Params - Start
eSE Conn Pipe Updated Status- Deleted
phLibNfc_UpdateSeInfo:Rxd eSE Removed Ntf, eSE Transceive CB Invoked
Invalid Core context passed from LogConn Module!
phDnldNfc_ProcessExtendedGetInfoPn800A1 - Invalid context
phDnldNfc_DnldGetNfccHashDataRsp - Un-successful Status received, Status byte
Invalid Libnfc context passed by lower layer
Invalid 'pInfo' from TML!
phLibNfc_ParseDiscActivatedRemDevInfo
HCI pHciContext->bResendPacket =
Hci init sequence could not start!
phNciCoreMuxNfc_Tx :Unknown Mux Index
phHciNfc_CoreSend
phLibNfc_ParseRfConfigSignedInputBuffer
phNciNfc_SetChipScopeCmd: Invalid input parameter
phLibNfc_Ioctl_SetSpmiConfigRegs: Invalid IOCTL context
phLibNfc_IoctlRfConfig
phHciNfc_CoreRecvCB : HCI Cmd Rsp Timer deleted successfully
phLibNfc_SM_IoctlGenAWaitTimerOffTrans: Failed
 Invalid driver handle or libctx
Invalid Read/Write state
P2P Target detected as remote device type, try priority discovery
phNciNfc_DetTagRemRsp
Launching Download Recovery Sequence..
IoctlGetRfCfgComplete,output buffer is Invalid
phDnldNfc_DnldEseEnableCB:Hardcoding Initial No. of Credits to
LibNfc:aConnectionStatus[phLibNfc_SE_Index_HciNwk]=
phLibNfc_LogEepromUserData
phLibNfc_MFCIncDecRestorePayload
Stop Discovery priority raised
phNciNfc_RawCtrlMsgTrnscvCmd: Invalid input parameter
phDnldNfc_SecureBootEnterDnldModeRsp - Request Successful
Anti-tearing Mirrored User Area Protected Crc is NOT OK!!
phHciNfc_UnRegAllRspEvts: Clearing all response call back function registrations
phLibNfc_Mgt_ConfigRoutingTable
phHciNfc_ProcessRspsOnApduPipe:Unknown Response INS received
phNciNfc_ReadIntRegRsp
phDnldNfc_GetFwInfoRspAfterDnldWrite - Request Successful
RF Tech and Mode:NFC_F_ACTIVE_POLL_MODE
phHciNfc_AnyGetParameterCb
phNciNfc_RecvStateHandler:CurrState = 
Invalid parameter!
phLibNfc_GetMeasuredFsRssiCfgProc: Status Failed!
phLibNfc_GetSmbLogCmd
phNciNfc_SmbLogNtf: Received SMB Logging notification from NFCC
phNciNfc_StoreNfcFTechParams
phLibNfc_ForceNextSeq
----------Technology based routing----------
424 kbps
phDnldNfc_RecvDnldPkt: Read Request Failure
phDnldNfc_DnldWriteCb - Request Failed!!
phNciNfc_InitGenErrorNtfCB
phLibNfc_ClearEseSessionIdProc: Set Session ID Failed
phNciNfc_UpdateCrcAppendFlag
phFriNfc_Tpz_H_UpdateNdefTypeField
phDnldNfc_eSESmbCfgAfterVenReset:Failed to invoke Dnld Ese Smb Config Sequence
phLibNfc_SM_SE_eSEGetAtrTrans:Failed, Pipe Info not Available
phFriNfc_MifareUL_iSelSectorChk2
phFriNfc_MifStd_H_ChkIntLen
phHciNfc_ProcessEventsOnApduPipe:                                        eSe Transceive Timer restarted with WTX timeout value
phLibNfc_eSE_GetAtrProc: Received FAILED status or pInfo Invalid
Trigger RF On command failed!
Invalid Error Status received!!
ADC-FO, ADC value is
phLibNfc_SM_Main_InitTransComplete: phLibNfc_SM_eTrigNfccAssertion invoking callback function, wStatus = 
phLibNfc_HciRawDataSendProc:Could not copy entire received data
phLibNfc_SeSvddCtrlCmd
phFriNfc_MfUL_H_Transceive
dwSetModeNtfTimerId
phNciNfc_GetGenDbgLogRsp: Semantic error received
bNciCmd:
 Mf WriteN Request Failed ..
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_SEMANTIC_ERROR
phDnldNfc_DnldEsePwrCfgCmd: Invalid LIBNFC context!!
bHciRspTimer:
phLibNfc_GenericTransceiveResp
Tml write error!
phDnldNfc_DnldCfgHsuBaudRateCb: Invalid LIBNFC context!!
Get DieId Request Failed!!
Mirrored User Area Crc is NOT OK!!
Set Rf calibration data signed passed
Failed to Register phLibNfc_PropLpcdDebugNtfHandler
phNciNfc_ValidateIntfActvdNtf
phLibNfc_SM_DisConnectSleepTrans
phFriNfc_MifStd_H_GetActCardLen
phLibNfc_DummyInitTimerCb: Invalid 'pLibCtx', cannot invoke upper layer call back
phFriNfc_Tpz_H_ProWrResp
phNciNfc_ProcessGenericErrNtf: Can not process Generic Error Ntf - Invalid input parameters
Generic Debug Log ntf timer started for extended time 
phLibNfc_ConfigLoggingSeqComp
phNciNfc_GetVasCodeRsp:Get VAS Code response received with failure status
phLibNfc_PrintSendData: phHal_eMifareAuthentB
phLibNfc_SetCWRFCfgComplete: Failed status received from NFCC
Antenna Self Test command failed!
phNciNfc_GetUserAreaAddress: Invalid parameters
phNciNfc_CompleteDiscSequence
phLibNfc_SM_IoctlGetSpmiGpioTrans: Failed
phLibNfc_HciInitComplete
phHciNfc_ProcessRspsOnApduPipe
phNciNfc_EnterNciRecoveryMode
pADDSetup is NULL 
Received AppData length exceeded max ATR length
phLibNfc_SetRfSignedSeqComplete
phNciNfc_RegDebugLogNtf
Download Completed (Degraded FW)
Received SensFResp Length exceeded max SensF length
phNciCoreMuxNfc_Tx
phLibNfc_SM_RawCtrlMsgTrnscvTrans: Failed
phLibNfc_GetVasCodeCfgComplete: Failed
phNciNfc_ValidateMode
 Mf XchgData,PH_NCINFC_STATUS_RF_TIMEOUT_ERROR Detected by NFCC during Data Exchange 
Waiting for Get listen mode routing notification...
phLibNfc_DnldGetFwVersionApiCb - Request Successful
phNciNfc_LogConnGetConnId
phLibNfc_ParseHrdFltDumpInfo: dwPsp
phNciNfc_ProcessInitRsp
phHciNfc_ReceiveAdminNotifyCmd:Unknown Instruction
phLibNfc_SM_GetSmbLogTrans: SMB Logging feature not supported on this platform
Dropping as there is NO upper layer call back function
Chip Version Error Status received!!
Max number of logical conn's supported:
Invoking pClientNtfRegRespCB with Tag Removed status
phLibNfc_GetNfceeSessionId
phLibNfc_Sn100AndAboveProcSysL2LogNtf
phNciNfc_RfPropReaderInfoNtfHandler:Invalid Length
phLibNfc_Validate_IoctlParam
phLibNfc_SM_ReadOnlyTrans
phLibNfc_Mgt_SetRfSettings: Invalid input parameter
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyERegParUnknown received
phLibNfc_L2EventProc: L2-eDebMgmtL2State
phLibNfc_ParseAssertionData:INvalid Length Received from Lower Layer
phFriNfc_Tpz_H_RdForWrite
 Response dropped due to force stop Discovery Sequence
phDnldNfc_DnldGetVersion - Invalid IOCTL context!!
phLibNfc_SM_SetVasCodeTrans: Failed
chkReservedBytes
phFriNfc_MifStd_H_Get4kStTrail
phLibNfc_HciDeInit:dwHciResendPacketTimerId Deleted
phLibNfc_SetEepromStngs :Invalid LibNfc Ctx 
Get Listen mode routing notification registration failed!
phNciNfc_CoreRecvManager-Failed to Stop De-Assert Wake Up Line Timer
phNciNfc_ProcessDataRsp
phFriNfc_Tpz_H_ParseNdefTLVType
phDnldNfc_RecvDnldEsePkt
Nfcee REMOVED
phLibNfc_SM_DeInitTrans: Failed to reset the Rx Delay
phLibNfc_Ndef_format_Cb
phDnldNfc_InitImgInfo: Invalid input parameters or Invalid IOCTL context!!
phLibNfc_CustFactoryCfgCmd: Invalid TLV Parameters
Max Rtng table size is '0', can not read Rtng table!
phLibNfc_IoctlGetSpmiGpioCmd
 Creating Request Payload (Header + Data)..
phNciNfc_CompleteModeSetSequence
Mapping on NCI RemoteDev Handle to LibNfc RemoteDev Handle Failed
phFriNfc_MifareStd_iWrNdefLen
phLibNfc_SwpIntfControl
phLibNfc_CustFactoryCfgCmd
phNciNfc_GetT3tTagId
phNciNfc_GetVasCodeSeqComplete
phDnldNfc_DnldPrevSessnStateCb: Session still Open after previous Fw Upgrade attempt!!
Registering for MFW Raw API RF validation test Notification
phDnldNfc_InitImgInfo: MW Major Version Number - 
####Primary NFCC, DOWNLOAD-ESE-CORE context
phDnldEseNfc_GetNewNode:Memory allocation failed while creating new node!
phLibNfc_SM_Main_ListenSendTransComplete
phLibNfc_Mgt_DnldGeneralNtfRegister: Invalid input parameters
Do not invoke upper layer as Deinit is in progress
phDnldNfc_BuildDnldEseHciPkt:Invalid PipeId
phLibNfc_SM_RemDevUnNtfRegTrans:Un Registering Notification Handler
phLibNfc_SM_GetTrimVerTrans: Failed
phLibNfc_SM_SetSmbNfccParamsTrans
Registering for Conn Credits Notification
Rf Technology Specific Details:
phLibNfc_eSE_GetAtrProc: App layer Callback Invoked
Timeout:dwConnectTimerId
phLibNfc_GetTagTypeInit
phFriNfc_MfUL_H_WrTermTLV
phLibNfc_SendEMVCoTagDetection
phLibNfc_GetSwioPadVoltageProc: Invalid parameter, Libnfc Context is Invalid
Notification call back de-registration success
Write Request submitted successfully
phUtilNfc_SetHciNfcContext
 ISO15693 XchgData,PH_NCINFC_STATUS_RF_FRAME_CORRUPTED Detected by NFCC during Data Exchange 
phFriNfc_MifareStdMap_WrNdef
No Log conn in loop back mode exists
phNciNfc_CustFactorySetGetCfg: Memory not available\n
phDnldNfc_DnldWriteCb: Invalid IOCTL context!!
Re-Initialize the sequence to perform set config
phLibNfc_SM_IoctlGetSpmiGpioTrans
phLibNfc_T3tCmdResp
Add Delay Wait for EoOP of SE2
phLibNfc_SetRfSettingsSeqComplete : Config Hsu Baud Rate failed Status 
DNLD Waiting on Send CB
phLibNfc_SM_GetFwVersionTrans
phDnldNfc_SetHwDevHandle
phNciNfc_BuildLstnIsoDepParams
phLibNfc_Ioctl_Mgmt_CB - Ioctl Get Prop Config complete
phDnldNfc_DnldProcessDisable_EdlWMDisableSE: gphDnldNfc_EseEnabledEnterCmtModeGetSecureFwInfo sequence Failed!!
phLibNfc_ProcessTmlError :pGenericNtfCb[COMM ERR]
phNciCoreMuxNfc_eMuxEvtDnldTxCb : Write Request Failed
phFriNfc_MfUL_H_ProRd16Bytes
phLibNfc_L2EventProc: L2-wTimeStampMillisec
phDnldEseNfc_HciRecvManager : Response Timer Start failed!!!
phLibNfc_SwpTest_CB: Prbs test failed
phDnldNfc_DnldCfgHsuBaudRate: ePlatformType = 
phLibNfc_CommonSeqProc: Status success
Registering for Rf Nfcee Discovery Request Notification
phLibNfc_RegisterForHceActivation
Get Config Raw Sequence failed!
phNciNfc_VerifyRtngTableConfig
phLibNfc_WaitLibSeqHdlrTimerCb: Sync Handler timer call back invoked
bUICCStatus:
Status received is...
Failed to allocate temporary buffer for                     storing the received data message
phDnldNfc_DnldLog
phHciNfc_AnyGetParameter:Failed Status from lower layer
phLibNfc_Ndef_Init
phLibNfc_RetrieveNvmDumpStartAddrProc : Invalid pIoctlCtx or Failed Status
phLibNfc_GetLpcdFalseDetCntComplete
phLibNfc_Ioctl_Mgmt_CB - Get Dnld Integrity Info complete
phDnldNfc_DnldGetSecureFwInfoRsp - Response Failed!!
phDnldNfc_EseStoreSmbList:Memory allocation failed while creating new node!
phDnldNfc_SpmiClientResetDelayCb : DnldGenNtfCb
phLibNfc_ParseHrdFltDumpInfo: dwR0
Listen A NFCID1 len:
phLibNfc_InitializeComplete
phLibNfc_SM_Dnld_eUserFwDnldTrans
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_NOT_INITIALIZED
phNciNfc_GenericSequence
phNciNfc_ProcessDeActvNtf
phDnldNfc_MemDmpAfterVenReset:Invoked with failure status
phLibNfc_SpmiRetryClientReset
phLibNfc_SM_SE_eSEGetAtrTrans
phLibNfc_SetAntennaTestParams
phNciNfc_StoreRemDevInfo
phDnldNfc_DnldComplete:Switching to Normal Mode Failed!!
phLibNfc_ParseHrdFltDumpInfo: dwXPsr
phLibNfc_ParseWdgTickInfo: dwWatchdog_Process_MailBox
Common params Total duration len:
(uint64_t)pInDriverHandle
Upon Zero credit reception, Not Restarting HCI command response timer (Upper layer CB not registered )
Invalid LibNfc context
phNciNfc_ProcessGpadcDebugNtf - Can not process Gpadc Debug Ntf - Invalid input parameters
Syntax error received in response packet
phFriNfc_Felica_HSetTrxLen
This API will be handled only in Libnfc uninitialized state
phLibNfc_Mgt_RawCtrlMsgTransceive: Invalid input parameters
phFriNfc_Desfire_Format
State machine has returned NFCSTATUS_UNKNOWN_TAG_PROTOCOL 
Unknown routing type
Tag with ISODEP protocol and Unknown SAK detected..
phDnldNfc_SecureBootEnterTransientDebugCmd: Invalid IOCTL/Dnld context!!
GetMemDumpTrans:Set Default Baud Rate FAILED, Status
phLibNfc_HciRawDataSendProc:Failed Status received from lower layer
phDnldNfc_DnldGeteSEHash2DataRsp - Un-successful Status received or Incomplete Hash Info Received, Status Byte
LibNfc:pActiveSeInfo->eSE_ActivationMode=
phFriNfc_T5T_H_CheckCCBytes
phHciNfc_AnySetParameterCb:Sucessfull
phLibNfc_SM_SetChipScopeCfgTrans
Current Ndef Message size
phLibNfc_HciOpenAdmPipe
Flush Data command Semantic error received
phFriNfc_Desfire_SelectFile
phDnldNfc_GetFwInfoRspAfterEseDisable
LibNfc:tSeList[phLibNfc_SE_Index_HciNwk].eSE_Type=
Registering for Interface Error Notification
NFCEE Discovery successfully started
phNciNfc_CoreWakeupMgmt SPMI wakeup Retry Status =
phLibNfc_Mgt_ConfigureAssertionLogging
phLibNfc_GetSpmiDbgProcComplete
bLibCurrState:
Invalid length of value! length and value is:
phLibNfc_ReInitDisableNfceeDisc
phLibNfc_SM_SetSmbNfccParamsTrans: Failed
phLibNfc_SM_IoctlPrbsTestTrans
phLibNfc_Mgt_ConfigurePowerMode: Wired mode/SetMode API in progress
Invalid Upper layer inputs..
phNciNfc_CoreIfUnRegRspNtf
NFC DEP interface mapped to wrong protocol!
SENSB INFO - ISO-DEP protocol is supported 
RF Protocol:PROTOCOL_T3T
phHciNfc_ProcessClearAllPipeNotifyCmd
phLibNfc_MapRemoteDevB
phNciNfc_SetConfigSignedRaw
phNciNfc_GetSecureMemoryDump: Sequence failed!
phNciNfc_DetectTagRemoval
4A tag detected..
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_COLD_TEMPERATURE_THRESHOLD_REACHED
phDnldNfc_FwVerAfterVenReset:Failed to start Get Fw Version Sequence
phLogNfc_ConfigureMwLogging
phNciNfc_CoreReqNciPkt: Requesting Nci Pkt Header
phLibNfc_SendTranscvCmd
phHciNfc_eSEGetAtrTimeOutCb:Invalid Context
 phLibNfc_Sn100AndAboveProcSysL2LogNtf : Invalid tag ID !!!
Get Pwr Track Data failed!
phDnldNfc_DnldEseSmbCfgCmd:Download mode eSE config Failed!!
Common params Total duration Value byte 1:
phHciNfc_ReceiveOpenPipeNotifyCmd:Failed Invalid Params Received
UICC Conn Pipe Updated Status- Deleted
phLibNfc_SM_IoctlSetSysConfigTrans- Inconsistent Input buffer 
phHciNfc_CalcWtxTimeout
M2 Fallback NEXT ADDRESS
phLibNfc_DnldGetFwVersionApiCb
phLibNfc_SM_Main_PollDiscoveredTransComplete:Invoking callback function, wStatus = 
Invalid Parameter
phNciNfc_SendConnOpenCmd
phFriNfc_MifareStd_iAuth
ProcessEventsOnApduPipe:pSeListenerNtfCb[OS Reset Ntf]
phLibNfc_SeSendCb: Call back received with status != success
Timer STOPPED phLibNfc_eSEExpNtfTimeOutCb
Received invalid Max data packet payload size. Applying work around
phNciNfc_ProcessCommonNciRsp2
phDnldNfc_DnldGetNfccHashDataCmd: Invalid IOCTL context!!
pClientNfcIpRxCb is valid, invoking...
phLibNfc_SM_IoctlGetRfPropConfigTrans
NCI Core Sender State Machine Init Failed
phFriNfc_MifareStd_iAuthFail
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_CorruptedTrim
phNciNfc_GetSwitchRFCfgRsp: Get switch RF config response Failed with Status
phLibNfc_Ioctl_PrbsTest
phDnldNfc_RetrievePn800vBootStatus
bLibTransFlag:
Invalid remote device or Remote device not found
phLibNfc_SM_SE_eModeSetPwrOffToPwrOffTrans
phLibNfc_DelayDiscTimerCb:Timeout
phLibNfc_GetTrimVerSeqComplete
Get Download Integrity Info Request success.. 
phLibNfc_Mgt_GetDebugInfo: Invalid parameter
phLibNfc_PrepareConnect_ISO14443_4A
phFriNfc_MifareStd_iRdTlv
phNciNfc_TurnRfOnOffPropCmdRsp:Turn RF ON or OFF response received with failure status
Init Sequence failed!
Invalid parameters (phNciNfc_GetConfigRfParameters)\n
phNciNfc_CoreInitRecverStateMachine: SUCCESS
phNciCoreMuxNfc_DnldCmdTx : Failed to create start timer
phDnldNfc_DnldChkIntegrity
Nfcee ENABLED
 . Starting LibNfc recovery . 
LPCD is wrongly enabled
phLibNfc_DummyInit: Failed start timer
phHciNfc_ProcessEventsOnApduPipe
phLibNfc_ParseWdgTickInfo
Listen B ADC-FO len:
ISO15693 XchgData Request is Successful!
phLibNfc_SM_AntennaTestTrans Failed
phLibNfc_SM_GetVasCodeTrans: Feature not supported on this platform
eSE Power Cycle Sequence Success !!
phLibNfc_LongVasCwDetNtfHandler
phLibNfc_EraseCounterNtfHandler
phNciNfc_GenDbgLogNtf: Received partial debug Logs than expected total length
phLibNfc_Ioctl_GetSpmiErrorRegs: Invalid input parameters
phDnldNfc_DnldCfgHsuBaudRateCb: Invalid IOCTL context!!
phNciNfc_ResetLogConn
phLibNfc_NfceeNtfDelayCb: Timer stopped due to eSE removed Notification
phDnldEseNfc_CrdtTimeOutCb
phDnldNfc_SecureBootEnterDnldModeSeq:Response Timer Start failed!!!
phDnldNfc_DnldCfgHsuBaudRate: phTmlNfc_GetHsuMaxBaudRate Failed = 
phDnldNfc_eSEPwrCfgAfterVenReset:Invoked with failure status
phHciNfc_CoreInit:Failed to register Callback for Admin pipe events!
phNciNfc_StopTimer
phFriNfc_Desf_Process
phLibNfc_NtfRegRespCb
phLibNfc_ModeSetHciNwk: Failed to set mode, error
Interface not active for this connection
phLibNfc_EnableExtnProcess: Nci Read request failed
chkDynLockBytes
phLibNfc_MFCIncDecTrRestoreComplete
phLibNfc_ClrRetAssertDataCb:Context is Null
phLibNfc_GetAssertDbgLogApiProc: operation failed
SwpSelfTest: Swp self test sequence failed!
phDnldNfc_SecureSEDisableComplete
phHciNfc_ProcessEventsOnPipe :pGenericNtfCb[RestrictedMode]
phLibNfc_Mgt_ConfigurePowerMode: Invalid call back function passed
phFriNfc_MifareUL_CB_Transceive
Invalid libnfc context received from lower layer!
phHciNfc_ReceiveHandler:Failed, Invalid Context or Rxd Params
bSakCeA 
Certificate Version Error Status received!!
phNciNfc_CoreReSendCb: Send status
phNciMuxNfc_BuildDataPktHci2-Failed to Assert Wake Up Line
phNciNfc_RawCtrlMsgTrnscvRsp: Invalid context
phDnldNfc_SpmiClientResetDelayCb
bNciIntErrRxd:
Re- Init Comp- Static feature config
Invalid LibNfc context passed by lower layer
phLibNfc_GetAssertDbgLogApiProc: Failed to allocate memory
Response Timer Start failed!!!
phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_CORRUPTED_TRIM
phFriNfc_T5T_H_Complete
phHciNfc_AnySetParameterCb:Uppler Layer Callback not defined
phLibNfc_SM_GetSwioVoltageTrans
phNciNfc_SvddOnCtrlRsp
phLibNfc_GetNvmMemDumpProcComplete:MEMORY DUMP LENGTH
phLibNfc_SetVasCodeCfgComplete
phFriNfc_Desfire_HProcReadData
phNciNfc_CoreRecvMgrDeRegisterCb
phLibNfc_SM_IsVirtual
phLibNfc_GetGenericDbgLogProc: Mismatch in Log type Received, pDbgInfo->bGenericDbgInfoType
Pres chk extension ntf call back not registered!
Flush Data response received with invalid payload length
phFriNfc_Tpz_H_CheckCCBytesForWrite
phFriNfc_TopazDynamic_CB_Transceive
phFriNfc_MfStd_H_ProErrAuth
phNciNfc_CoreRecvManager1-Failed to De-Assert Wake Up Line
phDnldNfc_SecureBootEnterDnldModeSeq:Unsupported Platform
phDnldNfc_GetNfccEseHashDumpAfterVenReset: Enable download mode failed
phHciNfc_CoreInit:Adm pipe Callback for Rx Events registered!
phNciNfc_TrigRfOnPropCmd
phNciNfc_AntennaSelfTestPropSeqComplete
phDnldNfc_Validate_DnldHeaderRcvd
phLibNfc_Mgt_GetDebugInfo
Target is still in the Rf field
phNciNfc_EnableExtnCmd
phNciNfc_CompleteEnableExtnSeq
Flush Data failed!
phDnldEseNfc_GenErrNtfHandler: Error code 0x0F,SE connectivity Pipe deleted
ID Check Error Status received!!
phLibNfc_ParseInputBuffer: Invalid input parameter
Listen mode routing: Not supported
Get FW interface version Rejected/Syntax error, Hence this is OLD FW
phNciNfc_CompleteT3TPollSequence
phLibNfc_GetEepromParams
phLibNfc_SM_Main_IdleTransComplete
phLibNfc_PrepareConnect_Jewel
phLibNfc_GetMwApi
phLibNfc_InternalSequence
phLibNfc_SM_ConfigHsuTrans
Re-configure failed!
phLibNfc_ConfigTestModeRspCb
phNciNfc_UpdateAidRtngParams
####DriverHandle
Chunked Write Frame Success Status received!!
phDnldEseNfc_ProcessConnPipeEvts:Failed Parsing BER TLV One BYTE
phLibNfc_EseCfgDelayTimerStart: Dnld Ese Cfg Timer started
phLibNfc_MultiTagNtfWaitTimeOutCb:Init Failed
RF Field ON
Response timer start failed
phDnldEseNfc_GenErrNtfHandler: Error code 0x0A,Message size exceeded maximum size
phDnldEseNfc_UpdateRsp:Invalid TML buffer received!!
phLibNfc_GetDumpDnldGetFwVersionCb: Invalid IOCTL context!!
phFriNfc_MifStd_H_ChkTLVs: Current NDEF message exceeds the Maximum Tag NDEF size
phFriNfc_MifStd_H_BlkChk_1
Driver handle is not mapped with NFCC type: Critical Failure
Invalid Input Parameter!!
phDnldEseNfc_UpdateCredits
Get session state received locked during Degraded FW update!!
phLibNfc_RfConnect_Twice
cpReservedBytes
phLibNfc_SM_SetTransStatus
phLibNfc_GetPageCountProc: Total page count is zero or exceeded maximum number of flash page count 
phNciNfc_ParseSysConfigParams
phLibNfc_Ioctl_DnldGetDieID: Invalid parameter
phNciNfc_CoreSendCb:Nci context cleared, received send callback!
phNciNfc_UpdateDataToNode:Memory allocation failed while creating new node!
phNciNfc_SetConfigSequence
phNciNfc_RegUnRegSeEvent: No registration found!
phLibNfc_SM_Main_ListenReceiveTransComplete
####Primary NFCC, DriverHandle
phHciNfc_ReceiveHandler:Failed, Invalid HCI bMsgType received
phLibNfc_DnldLogReadReq: Invalid LIBNFC context!!
phLibNfc_CrcConfigProcess
phLibNfc_EnableExtnProcess:Enable proprietary extension successful after no of retry
phNciNfc_SvddOnCtrlCmd
Card is Read-Only
RF Technology B parameters
phLibNfc_GetEraseCounterProc
phDnldNfc_DnldComplete: Switching to Normal Mode Failed!!
phDnldNfc_FwDnldAfterVenReset:Invoked with failure status
phLibNfc_SM_FormatNdefTrans
Discovery API is already ongoing
phLibNfc_MfcAuthInfo_Clear
phLibNfc_UpdateSeInfo: Check Trans On Apdu Pipe status :
phLibNfc_ConvertToRemDevType- RF tech Not supported
phNciNfc_GetNciParams: Invalid parameters
phNciCoreMuxNfc_TxCallback
phLibNfc_MifareULTagTypeSeqComplete ; Success
phNciNfc_LogConnNotifCB
phFriNfc_MifStd_H_GetSect
Invalid LibNfc context passed
phDnldNfc_UpdateRsp:Received DNLD Error, Status:
Invalid input parameter
bNewVer[1]
phLibNfc_SM_SetSwitchRFConfigTrans: Invalid Params
phLibNfc_GetTagTypeSeqComplete
phNciNfc_CoreGetData
eSE Power Cycle Sequence Failed !!
Failed to allocate trans info buffer!
phDnldNfc_DieIDAfterVenReset
phHciNfc_UnRegAllRspCb
phLibNfc_SM_ResetNtfTrans: RESET NTF - NO Uart Message Received
Receive State Machine: Result
phLibNfc_PrintSendData
RID response received
phLibNfc_SM_SetSECurrState
phDnldNfc_RspTimeOutCb
phLibNfc_Ioctl_NfccTimerCfg: Invalid IOCTL/LIBNFC context !
phUtilNfc_InitIoctlDnldCoreCtx
phLibNfc_eSE_Transceive: Invalid input parameters
phFriNfc_MfUL_H_Rd16Bytes
 4A Payload created successfully..
phDnldNfc_DnldEseValidateRxdPkt:Dnld eSE Cmd Request Failed!!
phFriNfc_MifStd4k_H_CheckNdef
dwGetPwrTrackDataNtfTimerId
phDnldNfc_DnldEseGetRemainingSmbLog:Invalid Context received!!
phLibNfc_SM_GetClrAssertRegsTrans:Invalid Assertion Config type
phLibNfc_GetLpcdFalseDetCntProc: operation failed
phLibNfc_ClrRetAssertDataCb:Parsing Assertion Data Failed
phNciNfc_FlushDataRsp
phDnldNfc_ChkIntAfterVenReset:Invalid Context
phLibNfc_SetRtngTableCfgsMore
phLibNfc_SM_GetFwVersionTrans: NFCSTATUS_SPMI_NACK1
Set Mode ntf timer start FAILED\n\n
phLibNfc_PrintSendData: phHal_eMifareAuthentA
phNciNfc_DetTagRemNtfHandler: Received Tag Removal Detect Notification
phNciNfc_ProcessCommonNciRsp2  - failed status received in response!
phNciNfc_RdrFInit
phLibNfc_NfceeNtfDelayCb
phLibNfc_SM_GetMultiTagInfoTrans: Failed
phLibNfc_SM_ConfigInitDiscoveryStopTrans: Invalid Input Parameter passed
phLibNfc_SetSmbCfgCmd : Libnfc Context is Invalid
 Invalid Param(s)..
phDnldNfc_DnldGetSessnState: Invalid LIBNFC context!!
Data Max Payload Length is not available !!!!!
EOF need to be sent after sending the data packet
phLibNfc_SM_SetHLMParamsTrans: Failed
Svdd On Control Successful
phNciNfc_DeAssertWakeUpTimerCb-Fialed to De-Assert Wake Up Line
phLibNfc_RemoteDev_Transceive: State machine status is NFCSTATUS_REJECTED
Get Power Track data Notification Timer Created Successfully
phLibNfc_CoreResetCmd
phHciNfc_CoreGetNewNode
Transfer/Restore Command Header failed!
phLibNfc_HciSetAllowListProc: Invalid Hci context received!
phHciNfc_CheckTransOnApduPipe:eSE Transceive or Get ATR API in progress
phLibNfc_GetFwTypeProc: Libnfc Context is Invalid
Chk Pres ntf timer restarted for extended time\n
phNciNfc_RfPlllostlockNtfHandler:Dropped at NCI
phNciNfc_DiscoverSequence
phLibNfc_HciOpenAdmPipe: Invalid Hci context passed!
phLibNfc_GetSpmiDbgProcComplete: Failed
Invalid Nci handle passed!
*************************Activation Notification*************************
Failed to Register phLibNfc_PropMultiTagStatNtfHandler
phFriNfc_MfUL_H_findNDEFTLV
phNciNfc_TrigRfOnPropCmdRsp:Trigger RF Field On Ntf Invalid Parameter
phNciNfc_StoreConfParams
phDnldNfc_DnldLogCb: Invalid LIBNFC context!!
phNciCoreMuxNfc_DnldCmdTx
Dropping Deactivate to sleep Ntf as Call back is not registered
phLibNfc_NfceeNtfDelayCb: Timer expired
phLibNfc_InitializeComplete :pGenericNtfCb[PLLLostlock]
phDnldNfc_NtfTimeOutCb: Invalid or NULL pContext
phNciNfc_GetPwrTrackDataCmd
phLibNfc_EsePwrCfgDelayCb
phLibNfc_DeActvNtfRegister_Resp_Cb
phLibNfc_SM_Dnld_eSE_TrnscvTrans
phFriNfc_MfUL_H_findReservedBytes
phLibNfc_GetSwio2VoltageCmd
Presence check extension response received with invalid payload length
RF parameter update response received with invalid payload length
phDnldNfc_DnldChkIntegrityRecoverCb - Request Failed!!
NCI Get Config Response Completely received 
phNciNfc_CompleteInitSequence
phLibNfc_SM_IoctlDisableDtaModeTrans: Failed to update NCI DTA flag
phLibNfc_SM_RemDevSendTrans
phLibNfc_SM_IoctlIoctlSetRfConfigSignedTrans Failed!!!
Rf Signed Config error, Tag ID (All):
phHciNfc_ProcessEventsOnPipe:Failed Parsing BER TLV One BYTE
NFCSTATUS_PENDING
Get Logical Conn ID failed!
phNciNfc_GenDbgLogNtf: Received debug Logs notification from NFCC
NCI Send busy
phLibNfc_SM_ConfigAssertionLogTrans: Failed
phLibNfc_SetChipScopeLogCfgComplete: Failed
phDnldNfc_DnldEseEnableCB: Received bNumCredits
phLibNfc_StaticListenModeRouting
phLibNfc_ChkForListnModeConfig
SMB ntf timer restarted for extended time
phDnldNfc_DnldEsePwrCfgCmd:Download mode eSE config Failed!!
====================================================
Battery Off state: Supported
Manufacturer ID:
phLibNfc_GetSessionAfterVenReset:Invalid Context
Failed to Register phLibNfc_TotalPollDurationNtfHandler
\n\nphLibNfc_549ProcSysL1LogNtf: L1- Calculated Field Strength
phNciNfc_UpdateLstnMgmtRemDevInfo
Rf Cal data response failed!
phLibNfc_Verify_5_1_CrcStatus_NewLayout
MuxEvtDnldRxFail Write Abort failed
Failed to start NFCEE Discovery (phLibNfc_ProcessNfceeStopDisc)
Invalid Input Parameters!!
phLibNfc_SysEoOpNtfHandler: Received EoOP
phLibNfc_GetNvmMemDumpProcComplete:MEMORY DUMP End Address
Repair Request submitted successfully
phNciNfc_InvokeUartCommnErrNtf: UNKNOWN UART ERROR
phNciNfc_SwptestNtfTimeOutHandler:SWP ntf timer started for extended time 
phLibNfc_SwpTest_CB
No Dbg Info for this Remote Device Type
 Invalid Device..
Enabling extension command failed by NFCC
phDnldNfc_SecureUpdateRsp : Notification Timer Start failed!!!
phLibNfc_SM_SE_eModeSetVirtualToApduTrans
phLibNfc_SM_GetDnldTransEvent
phDnldNfc_UpdateRsp:FOUND START ADDRESS
phNciNfc_RfPllUnlockedNtfHandler
phLibNfc_ParseHrdFltDumpInfo: dwMsp
phNciNfc_EofSendCb
 Mf ReadN Request Failed ..
 Invalid Caller Param(s)..
 4A tag detected..
Sel Resp:
phLibNfc_SM_IoctlExpModeSWaitTimerOffTrans: Failed
phHciNfc_CreateSEGetAtrTimer
Generic DEBUG ntf timer started
phHciNfc_CmdSendCb
phFriNfc_MfUL_H_CpDataToUserBuf
phLibNfc_SetCWRFCfgComplete: Invalid LibNfc Ctx received from NCI
phDnldNfc_DnldGeteSEHash1DataCmd: Request submitted successfully
HLM debug logging Area Crc is NOT OK!!
phFriNfc_MifareUL_iSelSectorWrite2
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyERegAccessDenied received
Listen B App Data len:
Payload MemAlloc for Send request Failed!
Invalid core context!
phLibNfc_StartDiscSeqEnd
phLibNfc_LoggingNtfHandler:Failed to allocate memory for Felica Miscellaneous events
phLibNfc_GetLpcdFalseDetCntComplete: Invalid LibNfc Ctx
phNciNfc_CoreRecvMgrRegisterCb
phLibNfc_Ioctl_GetRfCalData: Invalid input parameters
Using timer with 10mSec to send EOF data packet\n
phLibNfc_EmvcoRfCollisionDetNtfHandler :pGenericNtfCb[EMVCO RF Collision Detected]
phLibNfc_TriggerRfOnNtf:Invalid Context
Deactivate ntf timer started\n
User Area Crc is NOT OK!!
phLibNfc_IoctlSetRfCfgComplete: Failed
Discover start Failed!
Memory not available(phNciNfc_Nfcee_StopDiscovery)\n
phNciNfc_GenDbgLogNtf
Registered Ntf call back function invoked
phLibNfc_SpmiRstCrcConfig: Invalid NCI context
State Machine is ready for shutdown
phNciNfc_UpdateCrcChkFlag
phDnldNfc_DnldGetSessnStateCb: Session State Rsp Buff Invalid...
phDnldNfc_GetDieId
phLibNfc_ValidateRtidConfig
phLibNfc_GetMultiTagInfoProc: received failed status
phNciNfc_VerifySupportedRouting
Received Successful LPCD Assistance Exit from NFCC
phNciNfc_PrintTechNfcFSpcfcParamsDescription
Registering for RF interface error Notification..
phLibNfc_Mgt_DeInitialize : HCI Command Response timer deleted successfully
phLibNfc_SM_Dnld_RecoveryTrans
phDnldNfc_RecvDnldPkt: dnld packet Read Request Failure
phDnldEseNfc_ProcessConnPipeEvts:SE restricted mode Unknown Event\n
phDnldNfc_DnldEseSmbCfgCmd:Response Timer Start failed!!!
phNciNfc_PrintResetRespDescription
Rf interfaces supported: ISO-DEP Rf interface
phNciNfc_RecvJewelResp
phLibNfc_GetNfceeIntfCfgProc
phDnldNfc_ClearFwBuffRef: Invalid DNLD context!!
phLibNfc_MultiTagGetFwInfoComplete
phNciNfc_ProcessCommonNciCompleteSeq
Ioctl_PropGetRfRegs: LIBNFC Not Initialized
Fw Download success.. 
phLibNfc_ReleaseLibNfcContext
phLibNfc_NfceeDisableUICC:Secure Element Handle not available
phLibNfc_DeInitialize
phLibNfc_SM_IoctlGetRfCalDataSignedTrans: Failed
Set Mode Notification Timer Created Successfully
phNciNfc_GetRfDevType
phLibNfc_ValidateDevHandle
Target not connected
phLibNfc_SM_SetVasCodeTrans: Invalid Params
Invalid input parameters received
phHciNfc_ProcessRspsOnApduPipe:phHciNfc_e_RspAnyEPipesFull received
phLibNfc_eSEExpNtfTimeOutCb
phFriNfc_MfStd_MemCompare
phNciNfc_ValidateIfActParams:type A silent NTAG poll phase Tech and mode received
phNciNfc_GetGenDbgLogSeqComplete
phDnldNfc_DnldGetVersionCb: Version Check Failed - Major Version Number Mismatch\n
phLibNfc_Ioctl_PropSetCrcChkConfig
Stopping Credit await timer as zero credit recvd..
phLibNfc_SeSendCb
phLibNfc_PropMultiTagStatNtfHandler :pGenericNtfCb[Multi-tag Status]
Response call back de-registered as auto de-register is enabled
RF Interface: NFC-DEP RF Interface
phLibNfc_InitializeComplete: Static feature config sequence failed
phLibNfc_SM_ClearSpmiErrorRegsTrans
Libnfc Stack busy - Init callback pending
bPipeStatusCeB 
phDnldNfc_FwVerAfterVenReset:Invalid Context
phLibNfc_SM_DisConnectStopTrans
phLibNfc_SM_Main_ListenSendTransComplete:Invoking callback function, wStatus = 
StoreTlvInfo: Received NFCEE removed Ntf with eSE Not present Reason Code
phLibNfc_SetCWRFCfgCmd
phLibNfc_ClrRetAssertDataCb:User Buffer is Null
phNciNfc_Nfcee_StartDiscovery
phNciNfc_DeActivateRsp
NFCEE Mode Set process Success
State machine has returned NFCSTATUS_PENDING
phLibNfc_GetNvmMemoryDumpRsp: Failed
phLibNfc_GetSwitchRFCfgComplete: Invalid LibNfc context
phFriNfc_MifareStdMap_RdNdef
phLibNfc_HciDataSendProc:Could not copy entire received data
phLibNfc_GetVasCodeCfgCmd
phNciNfc_ClearConfigParams
Failed,(phNciNfc_ProcessDeActvNtf)Wrong ntf length\n
phLibNfc_Ioctl_Mgmt_CB - Get SPMI GPIO test
phLibNfc_UpdateSeInfo:Unkown Nfcee Id
Invalid parameter passed(phNciNfc_SetPowerMode)\n
Valid Actv Rf Tech and mode received (1)...
phLibNfc_eSE_Transceive: Stack BUSY
phLibNfc_TempReceiveCb
Turn RF ON or OFF command rejected by NFCC
Conn Credentials update failed!!..
Repair Request Failed!!
phUtilNfc_SetMuxState
phFriNfc_MifStd_H_RemainTLV
phLibNfc_SENtfHandler :NFCEE Removed Ntf
Send Success
phLibNfc_SkipSequenceSeq
phDnldNfc_DnldWrite
phLibNfc_ComputeMemDumpAddr : Invalid memory Type
phLibNfc_CreateLogConnCb: Failed
phLibNfc_Mgt_GetSecureFwInfo: API will be handled only in Libnfc uninitialized state
phFriNfc_MifStd_H_ProAcsBits
phNciNfc_TrigRfOnPropCmdRsp:Trigger RF Field On Ntf command rejected by NFCC
phNciNfc_ValidateLstnNfcBParams failed
phLibNfc_FwVerDelayTimerStart
Max Packet Size
\nMode set requested for UICC, no change in power state\n
phFriNfc_MifareUL_iTermTlv
Set Config disable se reader success
Dropping eNciNfc_NfceeDiscReqNtf:                                                            phNfc_e_RfProtocolsUnknownProtocol
Received AID length exceeded Max AID Length
phNciNfc_GetRtngTableConfig
phLibNfc_Ioctl_Mgmt_CB - Prbs test complete
SENSF Response:
phLibNfc_ReleaseTimers
phLibNfc_SM_CfgTestModeTrans: TML HSU Baud rate Set to
phLibNfc_SM_SetCWRFCfgTrans: Feature not supported on this platform
phFriNfc_Felica_HChkApduBuff_Size
phLibNfc_GetMultiTagInfoProc: Tag of Not interest detected but partial info received
phNciNfc_SeDataPktDelayCfg: pNciCtx->bSeTxDelay
phDnldNfc_SecureBootEnterDnldModeSeq: Enter Download mode cmd submitted successfully
phLibNfc_GetMemoryDumpCmd : Config Hsu Baud Rate failed Status 
phLibNfc_DeInitializeComplete:De-Init is successful
Get Memory Dump:Invoking callback function, wStatus = 
phFriNfc_MifareUL_iWrLenTlv
phLibNfc_549ProcSysL1LogNtf: L1-eDebMgmtL1State
phNciNfc_BuildPropConfigParams
phLibNfc_GetAvailableSlotIndex
phDnldNfc_DnldFlashIntegrityCb - Request Failed!!
phLibNfc_IoctlClearAbortDnldCtx: Invalid Driver Handle!!
Return Partial Log length
phDnldNfc_RetrieveProtectedPageStatus
phDnldNfc_SecureBootDnldComplete
bLibTarState:
RF Tech and Mode:NFC_A_PASSIVE_LISTEN_MODE
 Felica XchgData,PH_NCINFC_STATUS_RF_PROTOCOL_ERROR Detected by NFCC during Data Exchange 
 SensFResResp.not present in T3T Poll Ntf recvd.
phLibNfc_SM_SE_eModeSetVirtualToOffTrans
phNciNfc_RawCtrlMsgTrnscvRsp: Raw control message transceive Successful
Platform Not Supported
phLibNfc_Verify_5_0_CrcStatus
 Extension Payload Packet creation Failed..
phFriNfc_Felica_ChkNdef
phLibNfc_ProcessRallResp
phLibNfc_ParseLogNtfDatRxFailure
phLibNfc_ConfigNciMode: Update client-ID to Secondary client ID(0x0B)
phNciNfc_WtxNtfHandler: Timer started for Transceive timeout value  
phNciMuxNfc_FindMuxNextPktIndex
Registering for LPCD Debug Notification
phLibNfc_MapRemoteDevCeHost
phNciNfc_StateDummy2Recv
Pkt Header<-<-
phLibNfc_SeSvddCtrlSeqComplete: Se SVDDD Success
phLibNfc_BuildSetCfgSignedCmdPayload
phLibNfc_StaticListenModeRouting: Listen Mode Routing sequence could not start!
phLibNfc_NfceeDisableSE2: Secure Element Already disabled
phLibNfc_GetAssertRegRsp
phNciNfc_RdrMgmtXchgData:Invalid Receive Buff Params..
De-register Rtng ntf call back success
phNciNfc_BuildLstnNfcBParams
Received Packet:
phLibNfc_FelicaReqResResp
phLibNfc_UpdateNfceeDiscTechnType: Listen Nfc-F tech supported
phLibNfc_Mgt_FMM_GetHashDump: Not in Idle state or eSE in download mode is enabled
phLibNfc_Mgt_Initialize:NFCC Power On Failed!!,phTmlNfc_IoCtl Return Status =
phLibNfc_SearchTable
phLibNfc_SendSelectCmd1
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_SyntaxErr
phNciNfc_RdrMgmtInit
phLibNfc_Ioctl_GetSpmiConfigRegs: Invalid input parameters
phHciNfc_RemoveRegistration
phLibNfc_NfceeDisableSE2
TML Write failed
phNciNfc_ProcessRtngEntry
phNciNfc_ReceiveCb
phLibNfc_IoctlSetRfCfgComplete
phLibNfc_SM_ISO15693_HdrConfigTrans
phFriNfc_MifareStd_iRdACSBit
NFCEE Notification Type: eNciNfc_NciSuicaModeStartedNtf
phLibNfc_CheckMfpEVxSlResp
phFriNfc_MifareStdMap_ConvertToReadOnly
phFriNfc_TopazDynamicMap_ChkNdef
phDnldNfc_SecureBootEnterDnldModeSeq - Protected Page Status is 
phDnldNfc_Read Request Failed!!
SENSB Response length:
phNciNfc_CoreReSendCb:Invalid 'pInfo' from TML!
phDnldNfc_InitImgInfo: FW Image Info Pointer - 
phNciNfc_LogicalConnClose_CB
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_MsgSizeExceeded
phLibNfc_SM_GetSecureFwInfoTrans: Failed
Invalid input parameter sent!
phFriNfc_Tpz_H_UpdateLenFieldValuesAfterRead
phLibNfc_FlashIntg_Verify_3_0_CrcStatus_NewLayout
phNciNfc_MfCreateXchgDataHdr
phNciNfc_ReleaseNciHandle
phLibNfc_GetSwioPadVoltageProc
phNciNfc_SetNfccParams: Stack not initialized
phLibNfc_VerifyRoutedTech
phLibNfc_ParseWdgDumpInfo: dwHostProcessPc
phDnldNfc_InitImgInfo: Image details extraction Failed!!
phLibNfc_SetSeReaderEnableEmvCoSeqEnd
phLibNfc_RfTxLdoErrorNtfHandler
Tag with MFC protocol and Unknown SAK detected..
phLibNfc_GetFwVersionComplete
phLibNfc_NfceeDisableESE: Secure Element Handle not available
phLibNfc_SetCfgSignedCmd
phDnldNfc_DnldValidateRxdPkt
phNciNfc_SetChipScopeRsp
phLibNfc_Validate_IoctlParam: NULL Output buffer
phDnldNfc_DnldEseEnableCB:Invalid response buffer!!
NFC A POLL Techn Specific Params - START
Get Tag Type:Invoking callback function, wStatus = 
phFriNfc_MifareUL_iRoNdefComp
phHciNfc_HciCoreExtractData:HCI Core Receive- Mismatch in Number of Payload Bytes Processed and Stored
eSE APDU Pipe Updated Status- Open
phNciNfc_StateRecv2Recv
phFriNfc_MifStd_H_ProAuth
phLibNfc_SetChipScopeLogCfgComplete
phDnldEseNfc_ProcessApduPipeEvts:WTX Call Back not defined by App
Libnfc sync handler wait timer started..
 Freeing T3TPollReq Buff..
phHciNfc_RemoveRegistration:Failed, Invalid Callback or List Empty
phLibNfc_HciResponseTimerRestartRequestNtfHandler
phHciNfc_eSEGetAtrTimeOutCb :Invalid or NULL pHciContext
phLibNfc_SetRfSignedCmd: Number of configurations to be set is 0
Notification registration entry already exists, skip registration
phDnldNfc_GetFwInfoRspBeforeDnldWrite: Version Check Failed - Major Version Number Mismatch\n
UnSupported BitRate!!
phLibNfc_SM_ConfigMwLoggingTrans
Invoking pClientNtfRegRespCB with rf deactivated status
phLibNfc_ParseRfConfigSignedInputBuffer: Payload Len issue
phNciNfc_CreateLogicalConn
phDnldEseNfc_ExtractHciData: HCI Core Receive- Zero Payload Len
Invalid Max Data packet Payload!
phNciNfc_GetSetCustFactCfgCmd
phDnldNfc_DnldEseTranscvCmd: Download mode eSE transceive submitted successfully
phLibNfc_SetEepromParams
Resend - Stopping Credit await timer..
phFriNfc_MifStd1k_H_BlkChk
phLibNfc_SetRfSettingsSeqComplete:NFCC hard reset happened, performing Re-Init
phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_InvalidParam
NFC A LISTEN Techn Specific Params - END
phLibNfc_SM_IoctlLoopbackTrans
phFriNfc_TopazDynamicMap_Process
phLibNfc_IoctlGetRfRegCmd: failed!
phHciNfc_HciCmdRspCb
####### LibNfc Stack Shutdown in progress #######
phLibNfc_EseSmbCfgDelayCb
phNciNfc_SendReset
phLibNfc_SM_EnableDisableMultiTagTrans
phNciNfc_GetRfCalDataRsp
phLibNfc_IsoDepFelicaPresChk_Cb
phFriNfc_MifStd_H_ProWrABlock
Set Se Mode Failed!
phLibNfc_GetMultiTagInfoComp: Failed
phNciNfc_GetRfParams
Can not process Crc Error Ntf - Invalid input parameters
phDnldNfc_ProcessExtendedGetInfoSn450Bx - Invalid pBuff
phLibNfc_VerifyCtxt
phDnldNfc_InvokeNfccResetNtfCb
phLibNfc_GetLibNfcSeqId
phLibNfc_ResumeDeinit
phLibNfc_SM_ConfigHsuTrans failed
pNciContext->dwNtfTimerId
 ISO15693 XchgData,PH_NCINFC_STATUS_RF_PROTOCOL_ERROR Detected by NFCC during Data Exchange 
phLibNfc_Retrive_TagId
phLibNfc_SM_Dnld_eUserFwDnldTrans: Assert Wakeup Status=
Invalid parameters passed by upper layer
EOF timer start failed\n
phLibNfc_MapRemoteDevKovio
******HCI SE Get Atr Timer Expired********
phHciNfc_HciResendPacketCb:Invalid Context
phLibNfc_DeActvNtfRegister_Resp_Cb: State transition target state is 
pClientNfcIpTxCb is valid, invoking...
phLibNfc_Mgt_GeneralNtfRegister: LIBNFC Not Initialized
phLibNfc_ProcessDeactToDiscResp
phLibNfc_GetPowerTrackDataSeqComplete: Invalid LibNfc Ctx received from NCI
phLibNfc_GetAssertDbgLogApiProc
phNciNfc_NciCtxInitialize
Data message call back registration failed!
Patch Code Crc is NOT OK!!
phLibNfc_FlashIntg_Verify_3_0_CrcStatus
phDnldNfc_EseCfg_GetFwVer
LibNfc:tSeList[phLibNfc_SE_Index_eSE].eSE_Type=
phNciNfc_RecvFelicaResp
phHciNfc_CmdSendCb: Send Failed
phHciNfc_OpenPipe:Failed to send to lower layer
Failed to create NCI Handle
phFriNfc_Desf_HSelectApp
phNciNfc_SetConfigRsp
phNciNfc_ClearUpperLayerCb
phFriNfc_Tpz_H_ProReadResp
phFriNfc_Tpz_H_ActualCardSize
Invalid frame payload length received
phDnldNfc_BuildDnldEseHciPkt
Get Pwr Track Data response received with invalid payload length
Read SWIO voltage Info: Invalid context
phDnldNfc_DnldWrite - Invalid libnfc context!!
Force No RF boot in case of SE300S
phNciNfc_GetUsrAreaAddrRsp
Listen ISO-DEP Hist bytes :
Notification Timer Created Successfully
phHciNfc_GetAllocatedPipeIndex
phLibNfc_SM_IoctlSetSysConfigTrans
phNciNfc_LogConnResp
phLibNfc_RawCtrlMsgTrnscvCmd
phLibNfc_RfDiscMapping : skip RF_DISCOVER_MAP_CMD 
Listen F T3T MAX Value:
phNciNfc_SendEofDataPacket: Failed to send EOF data packet
phLibNfc_SM_IoctlGetDnldIntgInfoTrans
phLibNfc_SendWrt16Cmd
phLibNfc_CustFactoryCfgComplete: Invalid TLV buffer received 
phLibNfc_RemoteDev_InternalConnect
Getting LibNfc RemoteDev Info by using LibNfc RemoteDev Handle Failed
phLibNfc_DummyDisc:Timer started
phFriNfc_Tpz_H_GetNDEFValueFieldAddrForWrite
Invalid session state received!!
phLibNfc_SendWrt16CmdPayload
Memory not available(phNciNfc_Nfcee_StartDiscovery)\n
phDnldEseNfc_ExtractHciData:HCI Core Receive- Mismatch in Number of Payload Bytes                Processed and Stored
phNciNfc_GetSmbLogRsp:SMB Get Logging response received with failure status
phFriNfc_Desfire_ProcReadCapCont
phLibNfc_InitializeAfterVenReset invoked with failure status
phLibNfc_HciSetAllowListProc: Invalid LibNfc context received!
NFCEE DISC NTF(UICC,Connected)Received and Dropped
phLibNfc_DelayForSeNtf: Timer Count
Enabling extension command Semantic error received
phNciNfc_ClearUpperLayerCb: Clear callback and context
phDnldNfc_DnldGetVersion
phLibNfc_GetDumpDnldGetFwVersionCb: Platform NOT supported
**********************NFCEE Discovery Notification*************************
ConfigureDriver:Invalid Parameter
FMM NTF fro NFCC Hash RECEIVED 
End of list reached2
phLibNfc_UpdateStackCapabilities
phLibNfc_SM_ProcessDeInit
 Conn Notification invalid..
phFriNfc_MfUL_ReadWriteLockBytes
Flags
phDnldNfc_SpmiClientResetDelayCb: SPMI Reset Client Status =
Unknown Event
phFriNfc_Felica_HUpdateAttrBlkForRdOnlyOp
phNciNfc_CoreInit:gphNciNfc_CoreResetSequence failed
phLibNfc_OpenLogConn
phLibNfc_SetSeReaderDisableEmvCoSeqEnd
phLibNfc_OsResetRcvd_AdminPipe:Invoke Get Atr Response callback
phFriNfc_MfStd_H_CallCon
phNciNfc_ProcessRfMgtRelaydetectionNtf:Dropped at NCI
phNciNfc_LogConnUpdateDestInfo
phLibNfc_SM_ConfigDriverTrans:OSAL initialization failed
phNciNfc_CoreRelease
Feature not supported
phLibNfc_Send_ISO_14443_3B_AttribCmd
Invalid length : Received size greater than maximum download frame size!!
phNciNfc_NfceeMgmtSetModeTimeOutHandler
phLibNfc_CustFactoryCfgComplete: Invalid LibNfc Ctx
phLibNfc_Ioctl_GetSpmiGpio: LIBNFC Not Initialized
phDnldNfc_DnldWriteCb: Invalid LIBNFC context!!
DNLD Ese Waiting on Send CB
SENS_RES Byte 2
phLibNfc_SM_GetSwioVoltageTrans: Failed
Add Delay Wait for EoOP of UICC
LibNfc Timer_Stop failed,Stat=
phDnldNfc_GetFwInfoRspBeforeDnldWrite - Protected Page Status is 
phNciMuxNfc_SendDnldEsePkt
phHciNfc_HciCmdRspCb :Invalid Context
phLibNfc_SE_NtfUnregister
Stack not initialized (phNciNfc_SetPowerMode)\n
Input Routing config size exceeds Max routing table size                                     supported by NFCC
phNciNfc_CoreDeRegister
Select ntf timer restarted for extended time\n
phNciCoreMuxNfc_CmdTx
phFriNfc_NDEF_Deinit
phFriNfc_MifareUL_iFndNdefComp
phLibNfc_SM_GetTargetState
OsResetRcvd_AdminPipe:pSeListenerNtfCb[OS Reset Ntf]
phLibNfc_SetSuicaEntrySysCodeComplete: Failed
phNciNfc_ProcessCommonNciRsp2 - Discovery rejected due to high temperature
phDnldNfc_DnldGetSecureFwInfoRsp - Invalid pSecureFwInfo!!
phLibNfc_SM_GetPowerTrackTrans: System Power trace feature not supported on this platform
Discovery select command success
phLibNfc_MFCSendAuthCmdComplete
phNciNfc_CompleteChkPresExtnSeq
phNciNfc_SetChipScopeCmd: Invalid Config
```
