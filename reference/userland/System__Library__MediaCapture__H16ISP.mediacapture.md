# `/System/Library/MediaCapture/H16ISP.mediacapture`

iOS 27.2 dyld shared cache image. Version `6.104.0.0.0`. **[DSC]**

## Linked libraries (47)

- `/System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore`
- `/System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice`
- `/usr/lib/libIOAccessoryManager.dylib`
- `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`
- `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`
- `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`
- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth`
- `/System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore`
- `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`
- `/System/Library/PrivateFrameworks/AppleCVA.framework/AppleCVA`
- `/System/Library/Frameworks/CoreMotion.framework/CoreMotion`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/Frameworks/AVFoundation.framework/AVFoundation`
- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`
- `/usr/lib/libtailspin.dylib`
- `/System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer`
- `/System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics`
- `/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`
- `/usr/lib/libAccessibility.dylib`
- `/usr/lib/libamsupport.dylib`
- `/System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders`
- `/System/Library/Frameworks/Metal.framework/Metal`
- `/usr/lib/libFDR.dylib`
- `/usr/lib/libMobileGestalt.dylib`
- `/usr/lib/libcompression.dylib`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`
- `/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices`
- `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`
- `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/ImageIO.framework/ImageIO`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/CoreMedia.framework/CoreMedia`
- `/System/Library/Frameworks/CoreVideo.framework/CoreVideo`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer`
- `/System/Library/Frameworks/IOSurface.framework/IOSurface`
- `/System/Library/Frameworks/CoreGraphics.framework/CoreGraphics`
- `/usr/lib/libz.1.dylib`
- `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 3 classes, 3 protocols, 46 methods, 16 properties

### Class pages

Every class and protocol, with its methods: [`BasicMOVReader`](../objc/BasicMOVReader_H16ISP.mediacapture.md), [`FlickerResourceArbiterClientDelegate`](../objc/FlickerResourceArbiterClientDelegate_H16ISP.mediacapture.md), [`JasperDepthProvider`](../objc/JasperDepthProvider_H16ISP.mediacapture.md), [`NSObject`](../objc/NSObject_H16ISP.mediacapture.protocol.md), [`PDDepthProcessorDelegate`](../objc/PDDepthProcessorDelegate_H16ISP.mediacapture.protocol.md), [`ResourceArbiterClientDelegate`](../objc/ResourceArbiterClientDelegate_H16ISP.mediacapture.protocol.md)

### Classes

`BasicMOVReader`, `FlickerResourceArbiterClientDelegate`, `JasperDepthProvider`

### Protocols

`NSObject`, `PDDepthProcessorDelegate`, `ResourceArbiterClientDelegate`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,V_hasReachedEndOfStream) hasReachedEndOfStream;
@property (T@"ResourceArbiterClient",R,N,V_arbiterClient) arbiterClient;
@property (T^{H16ISPFlickerDetectorContext=^{H16ISPFlickerDetectorHWInfoStruct}B^{OpaqueAudioComponentInstance}{AudioStreamBasicDescription=dIIIIIIII}I{AudioBuffer=II^v}{AudioBuffer=II^v}Q{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}{AudioBuffer=II^v}^{CPastFlickerHistory}i^{OpaqueFFTSetup}{H16ISPFlickerDetectorDebugContext=^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{__sFILE}^{H16ISPMetrics}^{photometer_flicker_result}}f^?^vB{_opaque_pthread_mutex_t=q[56c]}@f^{?}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}CI^{AppleH16PhotonDetectorServicesAssistant}[132C][24C]},N,V_flickerContext) flickerContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,V_gmoFlowBitmask) gmoFlowBitmask;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (6,513)

First 3,000 of 6,513.
```
ReadPropertyValueExclave
AnfdSmudgeDetection
outStats->tests.isEnoughInPoints = %lf\n
gmcNumOfPoints
brgd
motionDataStatus=0x%08X sphereStatus=0x%08X 
currSnowSceneHistIndex
H16ISPBufferReceiverRealTimeThread
DAT
flashCaptureSequence=%d flashCaptureCount=%d flashCapture=%d captureType=%d
CISP_POOL_PDE_DY
hist_ch0: 
bayerYSumBandStdRef[16]
NTCTemperatureStandby
Unable to open file 
motionMetaVersion = %d\n
moduleWorkWeek
pflCorrectionUm
TestPatternColorBar1
JasperConfigId
JasperFramesSinceLastTransition
Shared FID DCN
Could not find SEP reference location. Will use ISP references
afWinStartX[16]
numConsecutiveDecreaseInMeasurement_rawR_7x1_hfir
FlareEstimate
ExclaveSetMinimumAutoExposureFrameRate
CacheTTL
validBufRectPreviewSecondary.width
earlyOut_rawGb_7x1_hfir
H16ISPGeneralProcessFrameReceiver: Did not get all pending requests back from kernel. remaining: %d.\n
UserStudyProbingPattern
resizeHiResRawPool
focusTriggerPDAFCorrMuteHintStatus
TestPatternSolidColor
com.apple.h16jaspernode.workloop
Jasper Bank Config: Config file size unexpected (%lu != %lu)
, calibration: 0x
DCSFPGASyncControl_channel_Private
ColorGMCDebug
drcAttenuationCoefPrevious
splitPDEnabled
/var/mobile/Library/ISP/Pearl/
CISP_POOL_SMV_SKY
lastFocusingMethod
bayerYSumBandAvgRef[16]
ISF: v%d.%d.%d. New calibration result: x=%.5f, y=%.5f, z=%.5f, confidence=%.5f from:%d (0:LMV,1:MI,2:GMC_GB,3:GMC_IR,4:RGBJ)
DepthResolution
0x%04x\n
afStatus=%d 
H16ISPServicesRemoteRGBIRPCEConfigKey
LoadFrontIRHPRFile
snfISPDGain
LinkFrequencyIndex
MutualInformation-RotationZ
triggeredScanStartTime
ALSControlMode_Private
maxGravityChange
focusBandLowNegativeOverrideTh
depthPerspectiveCorrected is false. Currently, only perspective corrected depth is supported
CopyStreamSensorRawOutputBufferPoolRequirements
com.apple.component-replacement.test
H16ISPCaptureStreamCopyProperty
sendInitialBuffersToFirmware
teleFOVUpperLeftY
outOfBandCount
Cost grid 
FusionMaxDepthThreshold
raw10
fdRect[3]
TestPatternFadeToGrayBar
laserIntensity
DCSAudioAccelTimeReference_ispTime_Private
BioCapBracketedCaptureParams
ShiftParams_RefOffsetY
/usr/local/share/firmware/isp/7425_01XX.dat
CopyProcessingSessionSupportedInputs
slowSyncFaceFlashOffLux
fdAWBDebug.skinColorSampleVariance
Peridot Near Event Compliance resolved, allowing all projectors
SecureAlgorithmSetTargetFrameRate
apsObjectDistance
lastFocusedScore_bayerY_viir_f0
DCSFPGAStatus_errorCode_Private
EnableAPSDebugMetadata
SetWSegThumbnailFeatureConfiguration
DCSIMUData_Private
com.apple.isp.frontfocusing
Adaptive Tone Curve
lastFocusedScore_rawGr_7x1_hfir
v8@?0
afWindowInRaw
gmcScoreBefore
SetLPDPEqualization
maxPixelValue
fdRect[1]
BadJasperCalibrationNotification
UARTErrorCount
SetSynchronizedStreamsSensorRawOutputRetainedBufferCounts
No
AllocateAndSendBuffers
Component Validation: At least one component replaced. Resetting stray
Expected size for decompressed firmware 0x%08x is larger than 0x%08x.  Failing. \n
sensorReadOutCropX
fdRect[0]
APS_zPosition_Private
H16ISPFlickerDetectorSetGain
lux.value
snfWBGain[1]
gravityIndex
xq.GetNumOfPoints() == yq.GetNumOfPoints()
shiftParamsUpscaleRef
ProjectorValid
StatsBlock
radiansFromXtoH[0]
vcmSensitivity
flags
SR+ 
Cam%dRawPoolRetainedCount
LPDPEqualization
OrigIrFromCVPixB.pb
Unexpected references size after compression (Expected %ld, Got %ld)\n
EnableDYWithSDOF
cscCoeffs row 1
choice
ProjectorBracketedCaptureParams
ISP_CopySetfile
H16ISPProcessingSessionCopyProperty
ConfigurePDEBufferPool
Pearl
Error: Couldn't send NVM\n
v32@?0@\"NSNumber\"8Q16^B24
preFlashMaxScoreIndex
bayerYSumBandDelayHistory[16][7]
gyroSamplesStd
CISP_POOL_SMV_PEOPLE
flashMainFlashLuxFull
afWindowEnabled
edgeGbValidPixPercent[16]
LSC_GET_BASE_U32_PT(chInfo2[ch]) % (chInfo2[ch]->gridCountX * chInfo2[ch]->gridCountY) == 0
GetProcNameAndAuditToken
fail to send command when trying to create frame sequence for closing projector banks, 0x%X
Computing signature for buffer %p whose size 0x%08zx is too large.  Failing. \n
DisableFrameReceiverTailspin
irSamplesAfterDownscale.pb
RGB-IR Calib: Dilute depth points from %d to %d
Jasper frame offset from array: failed to send command to firmware: 0x%08X
bodyWeight
DCSFPGASyncControl_enable_Private
ExclavesAnnounceSupport
earlyOut
The requested timeout is not allowed. The maximum allowed timeout is %d
Jasper Frame Config: using file %@ as config plist
False
SetStreamSensorRawOutputRetainedBufferCounts
stageLastFreshScoreFrameID
OneDimensionHorizontalFilterWithPadding
disabled
SetMetadataOutputFeatureEnabled
strobeNTCStatus
localHistBlockCntY
StereoGMC-ScoreAfter
set
IR samples after Median Filter (uint8)
DCSAudioAccelDevicePropertyStreamingEnabled_Private
nInliers after 3D constraints: %d\n
NormaDxToCanoncialDisparityOffset
Jasper Frame Config: failed to apply mode %d
SendStillImageBuffers
ProcessFrameMetadata
earlyOutMeasurementLimit_rawB_7x1_hfir
LsInterpMode
m_oldestIdx != m_nextIdx
No %s projector token found
LogCaptureDeviceEvent
ActivateWSegThumbnailOutputInFrameReceiver
v20@?0^{__CFArray=}8i16
primaryReadoutDoneTimeStamp: %llu\n
Color Samples After Equalization
\tCalibration UUID mismatch, removing contents of directory\n
pdpFocusPos
focusScanPeakPrediction
EnableCFOV
min_gyro: %f\n
Failed to read unique chip ID
ExclaveInitFlickerTimer
CISP_POOL_SMV_SKIN
flashCaptureSequence
multi-camera-cal-swide
Jasper sequence from array: tcm number not a number...
BufferPoolType_YUV
BA status: %d\n
weightLuminanceStable
continuousMode =\n
FocusPixel Data
pdafFocusPosition
WarmLEDPercentile
*ninliers != 0
/var/mobile/Library/ISP/Pearl/spotDB.bin
RotationYDiffFromPrev
MIConfidence
Timebase Conversion Info:\n
oisSampleCount: %d\n
n't
GMC Fail: Final Rotation out of tolerance
vDSPImgfir
H16ISPCaptureDeviceCreate: device creation time
device
stageAccumulatedDetect
snfSensorDGain
AEWindowsEnable
tempActDIE
ANSTFeatureAnnounceSupport
sensorConfigurationIndex
AttachSushiRaw
epochTime: %ld:%03d\n
m_records.size() == (size_t)m_nextIdx + 1
DCSLTCEnabled
DenseLowPowerProbeA
CISP_POOL_VIO
    Toolchain Name: %s\n
H16ISPExclaveGraphNode
xLen == v.GetNumOfPoints()
pIn3 != nullptr
%@.bin
HITHFeatureGetPoolRequirements
pdpImageHeight
ch0
pixelInRow != 0
Wide
ErodeOrDilateRect3x3
    Release Version: %s\n
sphereMeanY
Couldn't read vader compliance\n
ProjectorVersion
SetGroupNondisruptiveSwitchingFormatIndices
numSlaves
JasperOffset_AXY
H16ISPCaptureDeviceRelinquishStreams
packed
MultiCameraCalSwide
Inverse
/usr/local/share/firmware/isp/4723_01XX.dat
FrameDone
Process_x2
fdInfo[0].roll
lastFocusedScore_rawB_7x1_hfir
/usr/local/share/firmware/isp/6221_01XX.dat
ExclavePrepareDeviceModelsParameterCommand
besScaler0OutEffectWindowH
PDAFProcessX4Wrapper
public.jpeg
C 
IsfDifferenceXMaxMin
ltmGridOffsetX
MetalObjects.mm
PrePostLTMThumbnailFeatureAnnounceSupport
CaptureStreamStart
depthValue
TofSync_AggregationInterval
teleFOVUpperLeftX
lsModulationWeight
tnrMetaVersion
focusBandHighWin
isWindowDetected
h <= NROWSMAX
ExclaveSetTargetFrameRate
AD
matrixWindowCount
rosaline-serial-num
ltmGlobalCurve
autofocusDampingGel
projectorExtrinsicsRotation0
VIO
EnableLocalHist
af_3x3_filter_idx
SparseProbeAB
metadata->timeStamp: 0x%016llX\n
MetaDataProjectorPowerProbeB
GMC-RotationX
Depth frame after quantization
/usr/local/share/firmware/isp/4425_01XX.dat
/usr/local/share/firmware/isp/8825_01XX.dat
ModuleSerialNumber
GeomUtils.hpp
ManualCCM
apsMode: %d\n
splitPDOn
numTilesY
Yaw
!info
pos<m_size && m_helperNNZ<m_maxNNZ
GMC Fail: Spatial Coverage
ISF: Resetting history
SlafCmApi
Mode
detections error
thread_info() for THREAD_SCHED_RR_INFO failed\n
DeviceProximityDetectionResultCreateDictionaryRepresentation
ExclaveSendFrameRateToFirmware
CopyFrameRateRangeRational
%s: Invalid pixel format for shared buffer pool, compandingMode:%d, format:%d packType:%d 
fesOutWidth
apsStabilityFlags
GetSoCGeneration
ImageUtils.hpp
/var/mobile/Library/ISP
DCSFPGASyncOffsetControl_channel_Private
Cam%dApsInnerLoopClose
Cam%dLockAWBWithoutALS
SolveLTInPlace
FlowAccumulateRow2x1Scalar
FPD-Pass
inputCallbackForGrimaldi_iPad
x.GetNumOfPoints() == v.Cols()
rawDMASrcCropX
IR samples before Median Filter
reference-%s__T_%lf.bin
Found reference plist at %s. Will use SEP references
Reading rosaline power from FDR\n
GenericProjectorType
rhs.Cols() == m_cols && rhs.Rows() == m_rows
CISP_POOL_RAW
ltmLatency
earlyOutMeasurementLimit_bayerY_3x3_f0
updateEnabledObjects
H16ISPFullStats
ObjectDetectionSetCurrentOverrideMaxHumanFaceCount
com.apple.isp.backsuperwidetemperature
triggeredScanTotalTime
FlowAccumulateRow1x1Neon64
InvokeEKRunKit
ProjectorSpecCalibrationPw
CCM row 2
wb
IsfDifferenceZMaxMin
CISP_POOL_META_DEPTH
status == 0
sphereMode
ispPreflashOffTimeStamp
waitForFlashCapture
fdAWBDebug.prevSkinColorCenter[1]
topPadding
com.apple.isp.frontirprojector.ntctempactive
CISP_POOL_EXCLAVE_META
thumbnailWindowWidth
focusTriggerDeltaTime
LPDPRCParamC
H16ISPServicesRemoteRGBJColorCalibrationKey
TestPatternColorSquare
rc == 0
Algo_DistortRadialLiteInternal
IR Samples after Equalization
GenerateRGBObjectDictionary
%s%d
MyIOHIDEventCallback
prevGravity_y
weightOutOfBand
GMC Fail: Ambiguity
ErodeRect2x2
SupportedGroupChannelIndex
No Vmode found
H16ISPSetMachThreadPriority - thread_policy_set(...,THREAD_PRECEDENCE_POLICY,...) failed, err=%d\n
DeviceUsage
DCSAudioAccelTimeReference_absoluteTime_Private
SetMetadataOutputBufferPoolConfiguration
/private/var/mobile/tmp/com.apple.cameracaptured/
FaceY
maxWBGainDown
YMinIndex
ProjectorValidationFailed
RGBJDilutionRate
probeMode
farPos
/usr/local/share/firmware/isp/0019_02XX.dat
sensorBlkAvgInstantaneous[2]
numberOfFocusPixelLocationDescriptors
Jasper frame offset from array: config ID not a number...
com.apple.isp.PeridotCoexRetry
nfISPDGain
afScores_bayerY_15x3_bpf_f0
GMC-RotationZ
Firmware logging aborted\n
MyH16ISPFrameReceivedProc
EnablePCEStreamingInFrameReceiver
DynamicVoltageEnable
LPDPEqualizationDFEh5
GetAFEAddress
MamaBearState
Property_Private
tempActNTC
focusNowHintFW_ConcurrentTriggered
isValidDepthData
H16ISPMotionManager: setSidebandTimeSyncHandler delayed, execution time %llu ms\n
v20@?0^{sCIspCmdDeviceImpactEvent=BfiQ}8C16
DCS_NONVISION_DATA
ForceSingleChannelCommands
RotationY
PDE_DY
rawAverage[R]
FullImgConfidenceArea
absoluteXAngle
depthValueMm
Matrix.hpp
Cam%dHRLTM
ExclaveTestSuite
thumbnailTotal
/usr/local/share/firmware/isp/3623_01XX.dat
IOSurfaceAllocSize
\tDefault calibration from NVM: deice is not ready or no ToF channel found
SparseInterleaveLowPowerProbeA
StreamLockOrderValid
index < m_rows * m_cols
CISP_POOL_RAW_AUX
CISP_POOL_CAPTURE_PDC_RAW
TimeSincePrevConvergence
HiCCTrgBias
matrixParamsToSet_defaultLensPosition
/System/Library/PrivateFrameworks/AppleCVHWA.framework/Firmware/
JasperStateTransitionCount
ExclaveSendFrameRateToService
ProjectorHWVersion
metadata version (minor)
flashTargetMainFlashBrightness
localHistBlockCntX
slaveDataValid
com.apple.isp.frontirsensorpower
plugin
apsSample: ts=0x%016llX  Zt=%-10.4f  Ze=%-10.4f  aps_w=%-5d  aps_e=%-5d  apsTemperature=%-10.4f lensTemperature=%-10.4f dieTemperature=%-10.4f\n           aps_sp_pos_corr=%-10.4f  aps_sp_cur_corr=%-10.4f  Zcmd=%-10.4f  Zcmd_clamped=%-10.4f 
slowSyncFacePreFlashLux
fusedDx.%lux%lu.%s
AEMode
RedGreenGain
SendDataFileToFirmware
IR samples after scale
H16ISPCaptureStreamStopInternal
VisPipeRawBitDepth
CISP_POOL_STEN_COEFFICIENTS
faceBlockY0
setBufferConfig
colorIntrinsicsEFL
colorIntrinsicsPPY
CorrProfileSumRows2x1H
Bad Peridot online config received from PeridotDepth: Wrong size (got %zu, expected %zu)
\tCrypto hash method is %@. Only %s is supported
ConfigureFrameworkFaceKitSettings
/var/mobile/Library/ISP/Pearl/rgbpInterSession.plist
upscaleFactor
earlyOut_bayerY_3x3_f0
edgeRValidPixPercent[16]
%s: Unable to allocate CFDictionary for IOSurface properties\n
BufferPoolType_PDE_NORM_DX2
OperationsList
DumpRGBIRInput
historySumR
CameraEventLog
ProjectorRikerFaultStatus
PackedRawAttachmentsEnabled
ProjectorOverheatLimit
motionDataStatus
./
relativeEntropy
detectedSpoofing
currAFScore_rawGb_7x1_hfir
startNoBufferAvailableTimer
Metadata does not include synchronization information. Abort!
FigMotionGetISPHallData
currAFScore
ltmGridIntXStillYUV
irSamplesAfterMedianFilterF32.pb
Created for platforms:
min_accel: %f\n
Trying to load reference file %s (type: %d, index: %d, temperature: %lf)\n
frameCount=%d 
matrixWindow
manualAWBGainCommandTag
SetLocalHistogramsEnabled
/var/mobile/Documents/JasperL
SparseInterleaveProbeA
RotationXDiffFromPrev
afAvgScoreHistory_bayerY_15x3_bpf_f0
\tCouldn't validate directories\n
Randomize
totalCropX
panoBaseEit
gmcRotX
infinityPos
SWDC
GMC-RotationY
Testing if aFDR may be used
APS_sensorTemp_Private
SetUnsynchronizedSensorRawOutputBufferPool
CaptureStreamCopyProperty
TimeSincePrevRun
OutGMC R:\n%lf\t%lf\t%lf\n%lf\t%lf\t%lf\n%lf\t%lf\t%lf\n
sphereExternalOffsetY
Aborting (CalculateGrid)
Failed to read %s projector token file.
AttachDogBodiesDict
AFPeakTracking
roiType
ltmProcMode
onMessageProcessing
PVDD2
fwRepositories
afAvgScoreHistory_bayerY_hiir_f0
TestPatternPN28
BackSuperWideCameraSNUM
/var/mobile/Library/ISP/
UseRgbp
ParseLPDPNonVisionDataBuffer
timeMachineIdx
nbrOfSlice
af_viir_filter_idx
ISF: Error: Calibration result originated from unknown origin (%d).
OTHER
micronsToB[1]
LTCError
ManualLTMEnableSpatialCCM
Fail
Shared Stats
Shared AiCam Debug
shiftParamsRefOffsetY
EnableMetadataSection
TorchSegmentParameters
SegmentLEDBitmasks
nfSceneBrightness
AddFaceIDMetadata
SplitPDOverrideMode
AllocateAndSendOneShotBuffers
flashCapture
flickerWaveMatch[0]
thumbnailEnable row 0
JasperPreset_AutoFocusMacroNormal
NTCTemperatureActive
D 
ReplayRawFilePath
LMV
PPDPass
/usr/local/share/firmware/isp/9724_01XX.dat
ActivatePrimaryScalerOutputInFrameReceiver
CollapseMBSupplyToForceOpenCircuitFault
/var/mobile/Media/DCIM/%s-%05d-
row<(int)GetMatrixHeight() && col<(int)GetMatrixWidth()
kH16ISPFrameReceiverBufferPoolType_AF_ASSIST
validBufRectStill.height
BHistEndX
preFlashMaxScore
Entered
ImageCaptureWaitForAEEnabled
matrixPercentile
sideband
info
CISP_POOL_RAW_SIFR
snfTableSel
ManualLTC
SetGroupAEWindowParams
BufferPoolType_PDE_DX
earlyOut_bayerY_viir_f0
bayerYSumBandLowTh
GoodIdx.pb
JasperL
SetGroupROIForCameraControls
onActivate
GetModuleParams
mediaserverd
MetaDataProjectorPowerFlood
Error converting vader compliance value\n
stopProjectorWatchdogTimer
tileOffsetY
afAvgScoreHistory_rawGr_7x1_hfir
afAvgScoreHistory_rawB_7x1_hfir
SendSemanticBuffers
stereogmcValid
Could not retrieve face ROI information. Check detectedFaces argument.
PrepareXyzWorld
JasperGmoDebugMode
sensorTemperatureFraction
SecureMotionToWakeSetConfiguration
ze_avg: %f\n
fullyExposed
faceY0
tempStbDIE
focusDelayCountTh
SlafFwApi
Cam%dOisInnerLoopClose
PearlCalibrationDebugInfo
disparityParams.plist
FramesSinceEver
Placement
CorrProfileProcess
ISF: history.nextIdx is out of range: %d
rosaline-calibration-current
currAFScore_bayerY_hiir_f0
CorrProfile
GMC
DCSFPGASyncOffsetControl_offset_Private
BypassMotionManagerInit
BufferPoolType_PARAMS
dpcEnabled
ISP_IsSafeToStartConclave
isp-command-send
daemon
Cam%dSIFPixelFormat
slowSyncGainBackground
/usr/local/share/firmware/isp/CmPM-brgd
Markers.cpp
RikerState
SetSynchronizedStreamsSensorRawOutputRetainedBufferCountsInternal
EflPctDiffFromAssembly
MutualInformation-RotationY
RgbpLcd
frame
SMVH 
Front
StopChannels
temp3
Jasper frame offset from array: property not an array
H16ISPGraphInfoNode - Single-channel frame message (channel %d)\n
unpacked
slowSyncIsSlowSync
v16@?0@\"STMutableMediaStatusDomainData\"8
FLDProcessWrapper
SIFErrorCount
%s%s-metadata.plist
PowerOffExclaveKit
convertExpressionActivation
H16ISPUseAuxRawPool
compHist1Enabled
projectorExtrinsicsRotation2
SparseInterleaveProbeAB
JasperFrameModes.plist
x
focusBandHighTh
GMC Fail: Reprojection error median too large
.pb
flashDualProcessType
timeStampHRProcessStart
sensorBlkAvgInstantaneous[1]
totalGain
horizontalScanStartPosition
Fail in RANSAC: cannot find good model.
aeShutterTime
LPDPFilterEnable
snfSensorAGain
RGB-IR Calib: Final Result(ROI): x=%.1f, y=%.1f, z=%.1f, cost=%f
PreMapClientSurface
%02X
Could not read calibrated power from sysconfig\n
SetDefaultFormatIndexConfiguration
H16ISPFirmwareLoggingThreadPriority
JasperLockAfFrequency
RgbjReportIsfFailure
Source
EnableSidebandMetadata
Cam%dHR
vaMetaVersion: %d\n
x1_norm.GetNumOfPoints() == x2_norm.GetNumOfPoints()
Loading DAT file for unprovisioned Savage
[base=%p, width = %zd, height = %zd]\n
nRows2%2 == 1
maxColorCalGainDown
yshKnobLevel
DestroyH16ISPBufferReceiver_block_invoke
RGB-IR Calib: Local validation succeeded and face ROI result was selected: x=%.1f, y=%.1f, cost=%f
FaultState
SetISPDCSDataLtcEnabled
ColorGdcCoeffs
timeStamp
Jasper frame offset from array: DXY value not an array...
MD
stable
level
ManualSCCMLUTS
CaptureDevicePerformPearlCalibration
earlyOut_rawGr_7x1_hfir
\tSerial nubmers size mismatch
FrontSuperWide
RgbpLcd_Threshold
stageDetectStatus
params.shiftMax > 0
IrAfterQuantization.pb
True
ProjectorErrorCount
fpcEnabled
cropWindowPDEHeight
H16ISPProcessingSessionProcessBuffers
fwToolChain
RENDERED_RAW
irSamplesAfterEq.pb
Failed to send Romeo data file: 0x%08X\n
DCSFPGAStatus_version_Private
earlyOutMeasurementLimit_rawGr_7x1_hfir
ISP_GetGDCBesOutputValidRect
ExclaveSendFrameRateToServiceInternal
ActivateMetadataOutputInFrameReceiver
JasperPreset_MacroShortNormalHybrid
H16ISPCaptureStreamSetProperty
Histogram metadata
LSCAverageGreenApple
prirep
thumbnailStartY
tempIdleNTC
Process
RgbpLcd_MultiRunFrequency
setFileHeader project
sphereMeanX
FusionFixedDepthThreshold
Pearl FDR is %s, ToF FDR is %s
Failed to send rosaline data file: 0x%08X\n
Shared Auto Exposure
PowerSupplyVoltage1
Face ROI
com.apple.isp.backtofprojector.dietempidle
stereogmcRotX
TryToTopOffFirmwareBufferPools
ISF: element.prevInSorted[%d] points to an index out of range: %d
H16ISPServicesRemoteDataKey
  [%zu] = CBAF_ONESHOT\n
/var/mobile/Library/ISP/JasperL
CISP_POOL_STEN_PARAMETERS
GMC-ScoreBefore
DCSFPGAStatus_fpgaMinTollboothVer_Private
max_accel: %f\n
BodyDetector Debug
).\n
, 
Cam%dOISRecenterOffset
CaptureDeviceProcessingSessionCreate
data
DIETemperatureIdle
com.gmcRgbIr.CPU_GPU
visOverScanPercentageControl
could not find AppleDieTempController
hiCCTbgBias
ISF: New calculated rotation angle: x=%.5f, y=%.5f, z=%.5f
IsfDifferenceYQ31
BackIRCamera
/var/mobile/Library/ISP/JasperL/JasperLCalib.bin
VISPIPE
sensorValidRectWidth
SetActiveNondisruptiveSwitchingFormats
H16ISPSensorRawPoolConfigurationGetBufferWidthAndHeight
sensorBlkAvg[3]
fdInfo[0].y
afScanStopTime
%@/buffer-%@
alsTParameter
ltmGridIntX
temp2
input.Cols() == output.Cols() && input.Rows() == output.Rows()
focusLockDeltaTime
YonkersFabRevision
afTileWidth
zTargetDACFromDepth
InfLimit
RgbjConfigurationFeatureVectorSize
cropY
bFlickerDetected
~H16ISPGraphExclaveAutoExposureNode
No C string description.
CacheDeviceConfigs
AddSushiRawPoolToFrameReceiver
EnableTNRMetadata
DCNUInitInternal
teleFOVUpperRightX
CALm
Calibration result was out of allowed rotation spec (%f) after refinement stage
SecureRGBBaselineStreamingEnabled_Private
chromaOffsetV
synTagLTM
configID
BHistEnable
ReloadNVM
/Savage/SavagePatch.DAT
SparseMatrix.cpp
timeStampFrequency
totalCropHeightSecondary
flashLEDOffBrightness
motionSumB
postureCorrectionX
RGB-IR Calib: Regular grid minimum for ROI: x=%f, y=%f, cost=%f
LowCCTrgAbs
SetGroupMasterConfiguration
LSC_GET_BASE_U32_PT(chInfo1[ch]) % (chInfo1[ch]->gridCountX * chInfo1[ch]->gridCountY) == 0
v32@?0@\"ADStreamSyncTimestampedObject\"8Q16^B24
AttachHumanBodiesDict
Cam%dApsOffsetCorrectionScheme
Shared Attention Debug
fesCropX
DenseInterleaveLowPowerProbeA
secondGainBlockDisable
RGBEstimate[1]
LSC_GET_BASE_U32_PT(chInfo[ch]) % (chInfo[ch]->gridCountX * chInfo[ch]->gridCountY) == 0
H16ISPFrameReceiverBufferPool::%s - ISP_PreMapClientSurface failed: 0x%08X\n
FaultDT11ST
Shared Projector
HighFrameRateAF
BlueGreenGain
SetDeskViewEnabled
release
comboWBGain[0]
focusTriggerOutOfBandWinPercentile
JasperDepthNode::AFAssistance: failed to add buffer pool
Can't activate %s projector: no projector token found
SetVideoOutputHandlers
FD
focusNowCommandTag
CopyUnsynchronizedSensorRawOutputBufferPoolRequirements
configMode
triggeredScanFrameCount
SetMetadataOutputHandler
FigMotionComputeLensPositionScalingFactor
product
ExclaveHandleFlickerTimerEvent
renderedRawTotalSensorCropRectX
besScaler0OutEffectWindowW
/usr/local/share/firmware/isp/2921_02XX.dat
%lld
EnableFilterGraph
isIr
PrepareGridCalculation failed.
irSamplesBeforeMedianU8.pb
Bad configuration
Timestamp Wall Time: %llu (ms)\n
faceIRDepth
ProjectorQuarkFaultStatus
SparseInterleaveLowPower
distCxyY
currentTargetPosDac
level > 0
Reading rosaline serial number from sysconfig\n
sensorBlkOffset: [Gr]=%f [R]=%f [B]=%f [Gb]=%f [Mono]=%f 
%s.%lux%lu.%s
contextMode
thumbnailEnable[4]
colorExtrinsicsLocationZ
ApplyNoiseReductionConfiguration
startReceive
Process_x1
CorrPostProcess
HallSensor2
ResetGroupSynchronization
aeShutterTimeNext
w <= NCOLSMAX
ExclaveSetMaximumAutoExposureFrameRate
dx
pSpd != nullptr
frame: %d\n
GDCEnabled
afTileStartX
motionSampleCount = %d\n
BaneResistance
SetTestMode
rgWidth
PluginMetadata
readNoise_1x
statPreScalerRatioY
samplesStd
firmwareTimestamp=0x%08X ptsInNanoSeconds=0x%016llX
motionSampleCount: %d\n
ManualSCCM
validBufRectStill.x
Created on: 
ISPProcessingSessionProcessBuffer
lastFdAFWindow.x
drcBlack
afCurrentPosition
AFWinBrightnessNormalizationEnable[16]
LSCComputeSNFVerticalGains
ISF: history.oldestIdx is out of range: %d
DARTCacheParameters
SparseInterleave
DCSDataFileLoad_FilePath_Private
Roll
DCSFPGAStatus_Private
previewZoomFactorScaler0
/usr/local/share/firmware/isp/
UnitInfoNVMChannelMask
Initial Color Frame
\tReading from FDR\n
Saving %s\n
faceBlockX1
/usr/local/share/firmware/isp/3624_02XX.dat
afScoreHistory_bayerY_15x3_bpf_f1
level == 0
SetPearlControlMode
ShiftParams_S2DCoefC
Confidence level too low.
xLen > 1
ISP_SetFrontCameraOffsetFromDisplayCenter
Original Depth Frame
IMU
Cam%dLong2ShortSpeed
com.apple.H16ispcalibrationnode.algo
focusingMethod
comboWBGainNormalized[2]
thumbnailDownsampleY
leftPadding
stereogmcRotY
AddRawPlusPoolToFrameReceiver
ProjectorFaultStatus
ConstructExclaveFilterGraph
thread_info() for THREAD_SCHED_TIMESHARE_INFO failed\n
stereogmcRotZ
%02X%02X%02X%02X%02X%02X%02X%02X
H16ISPProcessingSessionPrepare
TestPatternBlueField
H16ISPGeneralProcessFrameReceiverRealTimeThread
AddMetadataOutputPixelBufferPoolToFrameReceiver
device invalidated
ColorCalibrationData
EnableV5LTMMetadata
GMC_Controller
DAT file for unprovisioned Yonkers - %@
bestScanPos
gmcScoreAfter
startPos
sensorSifrBayerBinFactor
DCSAudioAccelSampleCallback_Private
hdrRatio
teleFOVLowerRightX
laKnobStatus[CISP_KNOB_COLOR_SATURATION]
avgWindowEvalBrightnessValid
statWindowWidth
pdafDisparityOffset
drcEnabled
localHistWindow
BHistBinSize
infUp_fwdac
Jasper preload frame from array: 2 values expected in array (bankId, frame)
com.apple.isp.GmcAxisThreshold
RgbpBlockCinematic
temp1
ModuleIRFilterID
%s token doesn't match platform. Token will be removed.
Unexpected references size (Expected %ld, Got %d)\n
EXCLAVE_META
RgbpLcd_LookForSuccessFrequency
BlurMProcessWrapper
kGICMaxPerModuleY >= numYGIC
Pitch
File Version: %s\n
FlowOutputLevel
Sending rosaline configuration: SN: %s; Power: %d\n
Conversion Formula: elapsed time (seconds) = (elapsed time (mach ticks))/ %f \n
Couldn't create SavageChipID string ref
LowCCTbgAbs
hdrConfig
tensorAFMode
APS_oisZEst_Private
FaceHeight
com.apple.videoeng.basicmovreader
sifrRatio
ReplayFrame
flickerFrequency[1]
ValidateProjectorToken
No face ROI specified.
focusBandLowWin
PDE_NORM_DX2
Jasper frame from array: property not an array
FigMotionISPMotionDataFromCFData
focusOperation_currGx
JasperLCalib
\tValidting SN (registry vs cache)
DebugInfo
FigMotionComputeAverageSpherePositionForTimes
\t height: 
ProjectorType
ActiveNondisruptiveSwitchingFormatsTrackIncludedConfigs
stream not controlled
FrameReceived
com.apple.isp.backtelecamerapower
LsIdealPctCam%d
ISPDebugDumpSkipFrame
sensorConfigurationOriginal
curr0
DCSAudioAccelKeyMessageCallback_Private
SetDepthEngineConfiguration
depth
H16ISPServicesRemoteRGBIRReportKey
pdafConfidence
FrontCameraCalSwide
ISPPropertyValue_Private
WSegThumbnailFeatureGetPoolRequirements
B24@?0r*8^v16
snfEnabledInRaw
AWBComputedSecondGGain_Private
\tCouldn't get boot manifest hash
rvsyncTimeStamp: %llu\n
ZFProcessX1Wrapper
PCEPreset
APS meta-data section not found in frame meta-data.\n
sizeAEWindows
thumbnailStartX
overallScore
com.apple.vecamera
Offset
DestroyMotionMetadataDebugLogger: Invalid context \n
SavageUID
currAFScore_rawR_7x1_hfir
matrixParamsToSet_tensorAfBestPosSelectMode
Could not rotate the color buffer
AddMetadataOutputDataBufferPoolToFrameReceiver
MyH16ISPGeneralProcessFrameReceivedProc
EnableISPBringup
totalCropYSecondary
bStillCapture
scanSettled
com.apple.isp.backtofprojector.dietempstandby
CISP_POOL_META
Jasper frame offset from array: 3 values expected in array (bankId, configId, dictionary)
Couldn't read serial number\n
Cam%dOisActivePreviewLimit
UNSUPPORTED_PROPERTY_TYPE
xq.GetNumOfPoints() > 0
pdpFocusDistance
RequireExclaveAD
DCSMagnetometerReset_Private
aeAverage
awbWindowEnabled
/usr/local/share/firmware/isp/ISPUnitInfo.plist
APS_coilTemp_Private
afBayerGbSumPerWindow[16]
com.apple.isp.cameratorch
FIDEnabled
StillImageConfigUpdateAtomically
DenseLowPower
colorProcValidRectHeight
%5d%s
ISP_SetExclaveMinimumFrameRate
m_tail[angleIdx] != -1
DenseLowPowerProbeB
No DAT file for Yonkers found
GetChannelSensorID
/var/mobile/Library/ISP/Pearl/GmcThresholds.bin
fdAWBDebug.prevWhitePointCenter[0]
knobSNFLevel
sensorBlkOffset[0]
com.apple.isp.frontirprojector.dietempstandby
afTileStartY
/ispane.afpp
%@.calib.plist
Failed to load PDE files\n
totalCropWidthSecondary
Z
Cannot inflate to output buffer.  Output buffer size %zd does not match available bytes %d \n
max_ze: %f\n
vcmStartStepDACValid
FPC_DATA
H16ISPFirmwareLoggingInfoLoggerOut
comboWBGainNormalized[1]
lutsCountXPadded
currAFScore_bayerY_15x3_bpf_f0
earlyOutMeasurementLimit_bayerY_15x3_bpf_f1
Sending special debug function to firmware object returned error : 0x%08x\n
allocateBuffer
AppleProxHIDEventDriver
YUV2
 %llu 
Shared VIS
/var/mobile/Library/ISP/Pearl
visSphereControl
%s: [ch:%d] Setting built-in seqeuence %d
EyeOpenLeft
CmCl
CISP_POOL_CAPTURE_FULL_RES_YCC
afScoreHistory_bayerY_3x3_f1
OCCl
SavageSNUM
JasperSequence
PreCheck
SetMetadataOutputFeaturePixelBufferPool
ComplianceE
pflEstimatorLowError
ISPDebugTreatPropertyWriteKeysAsVolatile
H16ISPServicesRemoteRGBJBufferKey
afBayerRSumPerWindow[16]
afGravityXHistory[16]
accelSamplesStd
H16ISPDevice.cpp
SetupConclave
input.Cols() >= relevantWidth
DeactivateExclaveOutputFromFrameReceiver
StopStreaming
startProjectorWatchdogTimer_block_invoke
fesOutHeight
SR_T_bayerY_15x3_bpf_f1
H16ISPCaptureDeviceRequestStreams
isSensorAccessAllowed
OUTGMC angles: %lf\t%lf\t%lf\n
validBufRectPreviewSecondary.y
earlyOut_rawB_7x1_hfir
PCECalib and IR metadata do not match. PCECalib is probably not valid anymore
%s: Sending Peridot online config failed: 0x%08X
alsEnabled
apsMetaVersion
bgGain
ISF: New calibration result receives confidence %.5f
Jasper Bank Config: Failed to send to fw: %08X
SMVP 
RgbIrVerbose
VisPipeSupportedRawBitDepth
LaunchStillImageCapture
DAT file for unprovisioned Savage - %@
colorExtrinsicsLocationX
ChannelMaskForSharedRawPlusPool
ltmCCMEnabled
vcmStartStepDAC
Jasper sequence from array: sequence %ld doesn't have the expected 3 values (from, to, repeats)
H16ISPProcessingSessionSetProperty
tnrPreviousGlobalMotionAdjusted
focusOperation_FrameCount
setPeridotCalib
GMCDebug
CISP_POOL_ANST_INPUT_BUFFER
afScores_rawB_7x1_hfir
focusingMode            = LOCK_WHEN_DONE\n
ActivatePrePostLTMThumbnailOutputInFrameReceiver
ManualGTC
    mach_timebase_info = %u / %u \n
ActivateStillImageOutputInFrameReceiver
getNextFrame
slowSyncD2
faceFoundDuringLastScan
alsMethod
earlyOutMeasurementLimit_bayerY_15x3_bpf_f0
FaceIR-Rect
IR image preparation failed.
WSEG 
Cam%dApsModeSwitchEnable
ValidateCompliance
TestPatternNone
H16ISPServicesRemoteRGBIRBufferDepthKey
/private/var/tmp/usr/standalone/firmware/Savage/SavagePatch.DAT
/var/mobile/Library/ISP/CalData
/var/mobile/Media/DCIM/CaptureDevice_Event_%s.plist
vaSampleCount: %d\n
setFileHeader sensor
fdInfo[0].x
PrePostLTMThumbnailFeatureGetPoolRequirements
H16ISPDebugFrameFileWriter
Depth
grayworldWBGain[1]
r
SetSwitchingFormatIndex
RgbpDisableCalibUpdating
Mean
apsOffsetEstCorrection
focusBandStableTh
pLSCConfig->channelGR.gridCountY == pLSCConfig->channelGB.gridCountY
StereoGMC-ScoreBefore
Index
JasperPreset
mode
triggeredScanStopTime
GenerateAndAttachCoreMediaMetaDataDictionary
\tCan't create %s! (%d)\n
scale
sizeAFWindows
afBayerGrSumPerWindow[16]
%s%s.%s
/usr/local/share/firmware/isp/CmPM-DPCd
StereoGMC-RotationX
JasperBankId
flashPreflashBrightness
AFAssistVersion
Magic number of buffer does not match. File may not be a PortableBuffer or may be corrupted.\n
ColorResolution
Jasper Frame Config: plist %@ missing
v32@?0@8Q16^B24
flashCaptureCount
renderedRawTotalSensorCropRectHeight
ctfBeta
Failed to read %s projector token file. Token will be removed.
EnableLTMPadding
fpcEnabledInRaw
OIS Metadata Version
allowEarlyOutAtStart
GetFocusPixelTypeCount
ZFProcessX2Wrapper
matrixWeight
SR_T_rawGb_7x1_hfir
Error: oldest index record is out of range.
AELuxLevel
StrobeSerialNumber
    Metadata Version: %d.%d.%d\n
tempIdleDIE
TimeOfFlightAutoFocusAssistant::sendCloud: no points found
/usr/local/share/firmware/isp/1020_03XX.dat
ISPProcessingSessionPrepare
AutoFocusAssistanceMode
skipped by decimation
ransacComputeHomography
TestPatternSmearing
B
ManualControl
manualFocusCommandTag
AddSet
GetAnfdResultsFromBuffer
validBufRectPreviewPrimary.width
strobePattern
lastAfWindowUsedInRaw
lsModulationSuspended
focusOperation_MaxGravityVectorAngle
run
\tFailed to read UUID. Marking as invalid
THUMBRAW
H16ISPCaptureDeviceCopyProperty
ParseDCSNonVisionDataBufferLegacy
PDM Before: perc50:%lf, perc95:%lf, perc997:%lf, mean: %lf\n
JasperTotalFrameCount
confidenceLevel
sequences
Jasper frame offset from array: DXY: deltas out of bounds
sparse
Load: 0x%08x\n
Cam%dEnableSensorCrop
ManualSCCMBytesPerRow
hwErrors[1]
stereogmcScoreAfter
Cam%dFullLSC
pflCorrectionUm_Blob
AttachHeadsDict
OverrideJasperWideExtrinsics
CopyGeometricDistortionCorrectedRects
VA meta-data section not found in frame meta-data.\n
sensorID
sensorBlkAvgInstantaneous[3]
slaveCamera-comboWBGain.[3]
gyroMinSample
Found no IR sensor\n
AWBComputedSecondBGain_Private
Cam%dsHDRRatio
CoolLED1Level
Shared Calibration
faceAverage
sequence
sensorReadOutCropY
openStream
af_actuator_sensitivity_um_per_fwdac
gyroMaxSample
PCERegsUpdateTweak
LPDPEqualizationMode
nextExposureTimeStamp: %llu\n
drcAsymmetryFunctionLUT
StartCamera
DepthToPosition_Private
/usr/local/share/firmware/isp/7525_01XX.dat
PreStrobeBrightnessRatio
MetaDataProjectorSubMode
CaptureStreamSetProperty
focalLengthPinhole
im.Cols() > 1 && im.Rows() > 1
\tIgnoring unexpected cached version (%d != %d)\n
Jasper calibration\n
ChannelArray
RgbpLcd_LookForSuccessMaxAttempts
newRows * newCols == m_rows * m_cols
earlyOut_bayerY_3x3_f1
Dumping ToF AF buffers to path \"%@\"
SecureDeviceProximityDetectionSetConfiguration
afFocusMoving
H16ISPCaptureDeviceCreate
ispPreflashOnTimeStamp
aeTarget
PPDErrors
StartExclaveStreams
ISPDebug%sPropertyWrite
yshBrightnessAdj
Shared APS Stats
clutEnable
cnrKnobLevel
afScoreHistory_bayerY_viir_f0
JasperDepthNode: could not get calib data. Processing will not work
JasperPreset_Hybrid
currAFScore_bayerY_3x3_f0
afeGeom.cellStartY < afeGeom.cellCountY
cellWeight
AutoFocusAssistanceVerbose
m_head[i] == m_oldestIdx
!isnan(record.confidence)
RGB-IR Calib: Regular grid minimum for full image: x=%f, y=%f, cost=%f
ActiveSyncGroupStreamIndex
VSpad
FigMotionComputePrincipalPoint
Shared TNR
sensorBlkAvg[1]
ISP_SetExclaveMaximumFrameRate
BaselineStreaming
Shared BES Proc
motionLUTUpdated
DEV
VerboseBufferTracking
FaultDT1
lastFocusedPosition
apsSample
ForceEnableTestMetadata
row < m_rows && col < m_cols
SetSensorRawOutputRetainedBufferCount
Soft Brick to Armed
triggeredScanFrameRate
DisjointSet.hpp
AttachHumanFullBodiesDict
UniqueChipID
unified
Spmi0ErrorCount
IntermediateTapAndScalerConfigUpdateAtomically
cropX
statBinH
ReloadNVMBytes
Couldn't read unified Pearl FDR: %@
afStable=%d 
Jasper Frame Config: Failed to open file %@
BufferPoolType_STILLMETA
packType
conversionGain
bayerY2Bcoeff_Gr[16]
AttachHumanHandsDict
LPDPEqualizationCTLEr
SetMultiIlluminantWhiteBalanceEnabled
focusNowHintFW
Valid through: 
Jasper frame from array: failed to send command to firmware: 0x%08X
Cam%dCalCropOffsetX
ImageRegistrationInfoAttach
Unsupported CVPixelBuffer pixel format: 
Result out of range.
Expected file %s to be of size %ld. Actual size: %d\n
RAW_PLUS
tbcnum
DeactivateANSTSemanticOutputFromFrameReceiver
RgbjConfigurationDilutionRate
FigMotionCalculateAdjustedLensPosition
expBiasCommandTag
grayworldWBGain[0]
/usr/local/share/firmware/isp/CmCl-Override.DAT
faceRoiXAngleCorrection
sendSensorMetadata
GMC Fail: Final EFL out of tolerance
pAfe != nullptr
DenseInterleaveLowPower
PrimaryUsagePage
operator=
frameRate
sensorValidRectHeight
renderedRawValidRectWidth
validBufRectPreviewPrimary.height
Status
1.2.12
Secure RGB sensor not detected
Shared SIFR
No sync info in metadata.
setplscgDelay
CaptureDeviceEventLogging
motion to wake
tensorAfWindowID[16]
xyzWorld.pb
Jasper preload frame from array: frame data size mismatch: got %ld, expecting %ld
/var/mobile/Library/ISP/Pearl/PCECalib.bin
sensorSerialNum
rows > 0
initial_rgLogRatio
RGBJDilutionHighRate
FlashAuxManualAWBGains
inputCallbackForGrimaldi
rawPixelFormat
faceIRWidth
SensorVersion
sensorConfigurationIndex=%d 
TemperatureDiffSincePrevConvergence
/var/mobile/Media/DCIM/%s-RGBIR-
  [%zu] = PDAF\n
/usr/local/share/firmware/isp/4524_01XX.dat
RunForRGBP
FCDC
bank
Jasper Frame Config: requested mode %d is out of range [0..%lu]
Shared FD DCN
GICComputeFromNVMApple
/usr/local/share/firmware/isp/4523_01XX.dat
CaptureDeviceFinalize
ze_ss_error: %f\n
flashPreflashLux
lutsCountYPadded
SetKeypointDescriptorDataConfiguration
LPDPEqualizationVMMode
failure
CaptureStreamStop
afCurrentPosition: %d\n
rgGain
autofocus: afScores=
lastFocusedScore_rawR_7x1_hfir
isSifrOn
GetFocusRowInCell
IR original frame
TriggeringReason
ConcatCols
ProjectorFloodResistance
SPD 
offsetEstCalDone
TofSync_MaxNoColorInterval
AddDCSIMUDataPoolToFrameReceiver
ERROR: %.4s timestamp >= sensorRVSync! aaTimestamp=%llu ispTimestamp=%llu delta=%lld\n
H16ISPMotionManager::EnableMotionDataFeedToISPCPU - CMMotionManager doesn't support setSidebandTimeSyncHandler
AbsoluteColorCalFlags
Jasper Frame Config: Unsupported config type \"%@\"
Jasper frame from array: 3 values expected in array (bankId, configId, frame)
SetVideoOutputConfigurations
ManualLTMIIR
totGainDown
afScoreHistory_bayerY_hiir_f0
faceRoiYAngleCorrection
Failed to send PCE calibration to FW\n
APS_zTarget_Private
/usr/local/share/firmware/isp/cam%dsetfile.dat
chInfo1[ch]->gridCountX == chInfo1[0]->gridCountX
removeBufferPoolFromFrameReceiver
matrixEmptyWindowThreshold
RGBJDilutionLowRate
SparseInterleaveProbeB
pdeImageWidth
/usr/local/share/firmware/isp/2224_01XX.dat
BypassFrameDelivery
com.apple.isp.frontirprojector.dietempactive
v.Cols() >= 2
binningMode
MSTFCurrentEnabled
FaceRects
Cam%dApsDacClampEnable
ltmRectEndY
tempYogi
bayerY2Gcoeff_Gr[16]
BackCameraSNUM
MetaDataProjectorPowerHigh
colorSyncId
%s: Unable to create IOSurface for client logging buffer\n
LPDPRC
H16ISPGraphInfoNode - Synced-pair frame message (channels %d and %d). Timestamp delta: %6.3f mSec\n
setFileSubVersion SubMinor
sceneXm
Resets on boot: %s\n
warmupStrength
fdAFWinSize
emCoupling[0]
AttachFacesDict
ImageRegistrationInfoCreateDictionaryRepresentation
PPXOffset
exposureStableCount
STILLYCC
DiagnosticsLogDump
H16ISPLocationManager: countryCode=%s, flickerFreqHint=%dHz\n
Unknown mach thread policy\n
luxLevel
bayerYSumBandAvgPrev[16]
SetfileVersion
Interp1SortedWithExtrap
hist_ch2: 
ev0Ratio
ltmRectEndX
numConsecutiveDecreaseInMeasurement_bayerY_3x3_f0
bayerYSumBandHighWin[16]
sparseLP
H16ISPServicesRemoteRGBIRMetadataIRKey
gmcRotY
scanCount
Jasper Frame Config: Sending Config %d to firmware (%@)
Jasper sequence from array: a maximum of %d sequences is supported
nInliers: %d\n
lowCCTbgBias
aeShutterTime (us)
AFWindowsEnable
kH16ISPFrameReceiverBufferPoolType_DATA
%s%ld
binning disabled
fodProb
CISP_POOL_STREAM_DESCRIPTOR
singularityMeasure: %lf\n
flashPreFlashFaceCount
hrEnable
/var/mobile/Documents/Pearl/ProjectorValid.bin
GenericProjectorTypeModes
RetryCounter
Focal Length calculation failed! GravityZ: %f, lensPostionScalingFactor: %f
Reshape
warning: strobe coordinate not found in the registry
brightOutlierCount
pdpFocusDistanceModel
dx.%lux%lu.%s
%d--
SPLITPXL_DATA
TestPattern
SetTimeOfFlightConfiguration
succeeded
MutualInformation-RotationX
teleFOVLowerRightY
/var/mobile/Library/ISP/Pearl/NVM.bin
DCSMagData_Private
apsMetaVersion: %d\n
hToMicrons[0]
BHistStartX
BinningModeToFactor
MetalMgt
.raw
SetActiveNondisruptiveStreamingFormats
Shared Motion Stats
zoomFactorScaler1
Yes
/var/mobile/Documents/Tokens.log
cxyY
TestPatternColorBar4
/var/mobile/Library/ISP/Pearl/IsfHistory.bin
Cam%dSIFCompressed
sensorTemperature: %d\n
preSceneBrightness
floatAFWinID
ltmGridOffsetY
Could not convert color image to suitable format.
IsSIFROn: %s\n
rangeExpansionGain
RgbjConfigurationLowFrameInterval
ColorPixelSizeMm
IR
Mach Absolute Time: 0x%llX (%llu)\n
DAT file for provisioned Savage - %@
PDE Debug
/usr/local/share/firmware/isp/CmPM-dcnu
slaveCamera-CCTestimate
VIS Data
calibStatus
HiCCTrgAbs
QueryDeviceImpactsInternal
%@ %s\n
List
min_xy: %f\n
afScoreHistory_rawGr_7x1_hfir
Comment: %s\n
pdpGravity
Failed to read unique chip identifier
ComplianceD
CISP_POOL_CAPTURE_FULL_RES
LoadFDRFCClDataFile
tofColorInfieldCalibrationManagerVerbose
updateOnChange
LoadPDEFiles: isOverridden %d
com.apple.isp.IsfThreshold
sceneXh
slaveCamera-CCM row 2
DCSAudioAccelDevicePropertyStreamingSimplified_testMode_Private
DAT file for provisioned Yonkers - %@
Shared CBAF Debug
green-blue
historySumB
focusMappingKnee
sifrBinWidth
/usr/local/share/firmware/isp/0225_01XX.dat
SparseProbeA
ActivateProResRawOutputInFrameReceiver
CaptureDeviceInvalidate
lscSplittingEnabled
TimeOfFlightAutoFocusAssistant: Not sending the cloud buffer - frame receiver no longer available
deltaY
avgWindowEvalBrightness[32x16]
photon
awbStable=%d 
hrCounter
/usr/local/share/firmware/isp/CmPM-CALm
GenericProjectorTypeFrameRate
\tInvalid device\n
zTgtLogical_LFAF
absoluteYAngle
&im1 != res
HITH 
JasperFrameModeList
Armed
GetMaxResolutionSensorConfigIndex
doDimensionsMatchTo
tailspinDir
FilteredRotationX
validBufRectPreviewSecondary.height
status
BA iternumber1: %d,\titerNumber2: %d\n
raw14
IR.%lux%lu.%lu.%s.bin
/usr/local/share/firmware/isp/Savage/FrontIRHPR.DER
FigMotionAdjustPointForSphereMovement
MulticamSessionStatus
sensorReadOutCropHeight
\t pixel format: 0x
aeAGC=0x%04X 
startupCalStatus: %d\n
manualExposureGainCommandTag
lastFdAFWindow.width
afScores_rawR_7x1_hfir
fdrLogMessages
\t descr: 
Could not lock pixel buffer.
META
ERROR: %.4s timestamp >= sensorRVSync! magTimestamp=%llu ispTimestamp=%llu delta=%lld\n
AE stable
motionSampleCount
Jasper frame from array: bank ID not a number...
AttachDogHeadsDict
SendTelemetryData
not 
strobeCurrentMain
SR_T_bayerY_3x3_f0
/usr/local/share/firmware/isp/3624_01XX.dat
IsfDifferenceYMaxMin
LoadHPR
cnrEnabled
ProjectorFloodResistanceDelta
APSDistance
SetANSTFeatureConfiguration
flashLEDOffLux
volt3
maxAcceptableGravityVectorAngleTh
curSceneBrightnessEstimate=0x%08X 
Color
CISP_POOL_RENDERED_RAW
cscCoeffs row 2
ispDGain=0x%04X 
sphereMode: %d\n
bottomPadding
motionSample
RgbjConfigurationLowFrameIntervalThresholdY
EXCLAVE_EMPTY_QUEUE_ENABLE ch 0x%x tailspinCode 0x%x
AppleH16PhotonDetectorServicesThread
AllocateAndSendStillImageBuffers
fdInfo[0].pitch
count
TimeOfFlightAutoFocusAssistant::sendCloud: teared down - aborting
\tDidn't find calibration\n
WarmLED0Level
sphereDampingGel
focusTriggerActualStartTime
NTCTemperatureIdle
DistortionDynamicCorrectionParams
RGB-IR Calib: Confidence level = %f
\tDefault calibration from NVM: failed to create calibration from NVM
temp4
Depth image preparation failed.
EnableMasterSlaveAFMetadata
motionFromStatsX
cropWindowPDEX
withValidData
Depth image not valid.
StreamIndex
SetANSTThumbnailFeatureConfiguration
Warning: Serial number from calibration (0x%@) doesn't match actual ID (0x%@)
ForceJasperFPS
slowSyncWeightedAveFlashOffLux
totGain
focusNowHintFW_ConcurrentTrigger
CorrAccumulate
H16ISPServicesRemoteRGBJJasperCalibrationKey
log2
ambientLuxLevelLow
FigMotionGetSensorValidCropRect
CorrProfileAccumNeon64
ColorPracticalFocalLength
%s token has exceeded max allowed timeout. Token will be removed.
/var/mobile/Documents/Pearl
-sparseLP
DCSFPGAStatus_minVersion_Private
CheckOutputHeightAgainstPool
sifOutCropRectX
matrixUsedDefaultLensPos
ISF: ISF Step Detection result: isStepDetected:%d, stepIndex:%d
captureStreamBeginTimer
sendInitialDataBuffersToFirmware
strobeCurrentMax
initial_bgLogRatio
volt1
BHistEndY
exposureStabilityCountTh
absoluteZAngle
StopJasperForInternalStreaming
ProjectorRosalineFaultStatus
APSActuator
fodResult
YPosition
GeomUtils.cpp
pdpLensPosX
sensorBlkAvgInstantaneous[0]
ExclaveSetRGBDeviceModelsParameter
DCSAudioAccelDevicePropertyStreamingSimplified_enabled_Private
Algo.cpp
minSample
YES
Component Validation: component %d replacement detected (state %d)
SetMetadataSectionEnabled
ManualLTCLUTsCountY
H16ISPSensorSharedRawPoolConfigurationInitSharedHiResRawPool
IR frame after quantization
VerificationScore
RemoveOldestRecord
FigMotionGetGravityZ
sensorFirstPix
focusScanMode
nfTNRFilterStrength
oscarTimeStamp
slaveChannelId
earlyOutMeasurementLimit_bayerY_3x3_f1
Rotation was clipped. Will not mark Pearl as calibrated.
RgbjReportIsfSuccess
CISP_POOL_3D_DEPTH
CISP_POOL_STATS_FE_THUMBNAIL_MASK
PowerSupplyVoltage4
VdspSpecialization.hpp
FactoryFeaturesMode
EnableSynchronizedStreamsSensorRawOutputBufferPools
H16ISPFlickerDetectorStartDataCollection
Number of allowed activations has reached zero. %s token will be removed.
Face tracking AF window
  [%zu] = TOFAF_RESTRICTED\n
pData != nullptr
RGB-IR Calib: Could not open %s for writing.
GetAFEDelayV
-script
Cam%dALS
ConnectWithRemoteAssistant
currAFScore_bayerY_15x3_bpf_f1
com.apple.isp.backcamerasensorconfig
edgeBValidPixPercent[16]
H16ISPCaptureDevice: Time from stream start to first frame
PearlVersion
bracketingMode
earlyOutMeasurementLimit
brcl
Peridot Near Event Compliance detected, allowing half of the projectors (4-7)
colorProcValidRectY
save2File
AELocked
ispTimeStamp
currDepthScore
iCCl
SensorID
ScoreColumns
%s%d.bin
FramesSinceTransition
Shared LocalHist
frameSkippingInterval
flickerConfidence[0]
distCxyX
isp_lacc.bin
RG-Width
%s: Setting built-in sequence failed: 0x%08X
PCEDepthConfig
VTOutputFrameCallback
size
bayerYSumBandAvgCurr[16]
maxScanAngle
createTexture
afeGeom.initV == -1
ForceVideoRawBitDepth
.thread
MetaDataProjectorProbeMode
GetInitialWeightForRecord
FullImgIntermediateConfidenceScores
refSpX1
Reading rosaline power from IOReg\n
SMVSK 
APS_oisZGCOL_Private
afAvgScoreHistory_rawGb_7x1_hfir
TestPatternColorBar2
BHistData
currentTargetPosition
ActivateStillImageIntermediateTapOutputInFrameReceiver
H16ISPCaptureStreamInvalidate
NoDataTimeout
fesCropY
y
blcAdjustment
SR_T_bayerY_15x3_bpf_f0
StereoGMC-NumOfPoints
a
disable
BufferPoolType_RESIZED_RAW
Couldn't read SavageUID
Shared AF FocusMap
ccmDataCnt
frameCount
pixelInBuffer > 0
Error converting calibrated power value\n
DEPTH
sifOutCropRectWidth
preBracketing
fpnsWindow
No detected faces provided. Calibration will not be performed.
 %s:%s
com.apple.isp.flicker-update.queue
0
updatePCECalibWithGMCResults
nRoot <= i
inputFormat
laKnobStatus[CISP_KNOB_COLOR_SUPPRESSION]
ctfStrengthGainX
LTC
DCSFPGAStatus_relDate_Private
MasterSlaveContrastFocusEnable
BufferPoolType_FPC_DATA
Cannot initialize decompression.  Invalid input. \n
MutualInformation-TheFrame
TestPatternColorBwSquare
/usr/local/share/firmware/isp/9723_01XX.dat
Jasper sequence from array: sequence %ld not an array
SetRoot
com.apple.isp.dcnu
AWBLocked
fdAWBDebug.skinColorSampleNum
StopCamera
yyyy-MM-dd HH:mm:ss
m_nSize<m_nCapacity
slaveCamera-wbGain.[3]
af_bpf_f1_filter_idx
TestPatternColorBar
ISFConfidence
CISP_POOL_CAPTURE_FPC_DATA
PreStrobe
sceneLuxLevelLow
IgnoreUnitInfoPlist
apsModeInUse
drcBrightAmplLimit
focusBandWeightWin
afBayerYSumPerWindow[16]
pdafDisparityScale
Cam%dBinningCompensation
ManualLTCLUTS
fileAccessCheck
apsSampleCount: %d\n
syncTag
\tLooking for local override files\n
multi-camera-cal-wide
tofColorInfieldCalibrationFeatureVectorSize
fdInfo[0].z
prevGravity_z
ShiftParams_RefOffsetX
Jasper frame offset from array: AXY: expecting 2 numbers: dx, dy
stereogmcNumOfPoints
CopyFileToBuffer
Token created. Created on: %ld, Timeout: %d (Valid until: %ld), Activations: %d, Resets on boot: %d, Comment: %s
general
PropertyConfigurationValue
fpnsEnable
pdafTargetPosition
BootManifestHash
aeStable=%d aeLimitsReached=%d 
SetReplayFrame
pts.Rows() == 2
apsEFL
Debug parameters for fdAE metering
fdAWBDebug.prevWhitePointCenter[1]
focusMappingSlope0
\tLooking for FDR data\n
STR 
FIDState
thumbnailDownsampleX
pixsizeMM
RGB-IR Calib: Confidence level of result is too low (%f <= %f). Result not valid.
FocusBehaviorSDOF
MultAxBToC
wellCapacity
stageAverage
flashSequenceNum
focusNowHintFW_Latched
ComplianceB
adjustedTarget1
hToMicrons[1]
b2y_R_coeff
EventCompleted
ManualControlEnable
Shared YCC Proc
setfileSubVersion
Number of depth points is exceeded
params.plist
StrobeYetiStatus
sensorBlkAvg[4]
ISP_GetExclavePlatformStatus
RGB-IR Calib: Error. Minimum outside the tolerance range (x=%f, y=%f)
SetMultipleOutputSupportEnabled
ExclavePreferenceClearValuesOnFirstLaunchInternal
apsFieldCalOffset
knobBCFLevel
AfValidCountEnable
focusNowHintFW_Latched_FrameCount
com.apple.H16ispjaspercolorcalibration
Unable to read from 
OSStatus SetGroupMasterConfiguration(CFTypeRef, H16ISPCaptureStream *, H16ISPCaptureGroup *, H16ISPCaptureDevice *)
H16ISPFlickerDetectorDispose
reference
Error converting calibrated power value:  could not fit 32-bit value into 16-bit destination \n
AddSplitPixelDataToFrameReceiver
LPDPEqualizationCTLEc
PDM After: perc50:%lf, perc95:%lf, perc997:%lf, mean: %lf\n
fdInfo[0].height
SendSysConfigCalibrationDataByKey
DisableFrameDoneTimeoutRecovery
sensorTemperature
keypointEnabled
curr1
PPYOffset
systemTime=0x%016llX 
com.apple.isp.preference-notify
FID
GetSharedRawPlusBufferPoolInfo
drcWhite
RGB-IR Calib: Starting Mutual Information v%d.%d.%d. NormalizedDX: %d, perception corrected: %@, shift offset: %d
SetMetadataSectionRequired
com.apple.isp.backtofprojector.ntctempidle
addDataBufferPoolToFrameReceiver
CISP_POOL_AUDIO_ACCEL_DATA
faceWidth
fIDFlowType
JasperComplianceNoDepthPerc
/
Expand
cropWindowPDEY
EnableDCSIMUData_Private
H16ISPMetadataDictCreatorGraphNode
tempStbNTC
hasFinalScore
\tLooking for calibration in NVM\n
H16ISPProcessingSessionProcessBuffer
ispDGainNext
linearityWhite
JasperOffset_DXY
Failed to read PCE Calibration (FDR data)\n
 not
AUX (Vertical Edge Map)
CopyDefectivePixelTable
compHistEnabled
TestPattern10_2
MutualInformation-Confidence
Header
prevGravity_x
/var/mobile/Library/ISP/Pearl/IsfThresholds.bin
SmileAndBlinkFD
totalPositionScanned
ActivateSecondaryScalerOutputInFrameReceiver
Cam%dDebugMetadata
IsfDifferenceXQ31
OIS meta-data section not found in frame meta-data.\n
binning 1/2
fdAFWindowID
TofSync_InfieldMatchInterval
photon-detector-cal-data
EnableLTMLuts
/var/mobile/Library/ISP/CalData/DCNUMetadata_0
motionSample: Tisp=0x%016llX  Tmot=0x%016llX  type=%-5d  convergence=%-5d  Wq=%-10.7f  Xq=%-10.7f  Yq=%-10.7f  Zq=%-10.7f  Wp=%-10.7f  Xp=%-10.7f  Yp=%-10.7f  Zp=%-10.7f  Xg=%-10.7f  Yg=%-10.7f  Zg=%-10.7f AccelX=%-10.7f AccelY=%-10.7f Acce
PowerProfile
ObjectDetectionConfigurationUpdateIfStreaming
apsDDF
RGB-IR Calib: Calibration result was out of allowed rotation spec (%f)
FdrForTof
xq.GetNumOfPoints() > 1
Could not open OIS meta-data file for writing: %s\n
als2HistoryProfileID
irIntrinsicsPPY
SR_T_rawB_7x1_hfir
SamplingH == SamplingV
chInfo[ch]->gridCountY == chInfo[0]->gridCountY
ConfigureExclaveGraph
Shared System
renderedRawTotalSensorCropRectWidth
/var/mobile/Library/ISP/Pearl/IsfIRHistory.bin
MetaDataProjectorIndex
ConfigureFrameworkCameraSettings
RemoteAssistantGetFlickerResult
RawProcBlock
IOPlatformSerialNumber
ConfigureFrameworkPerceptionSettings
CamRequireAllSensors
iirStrength
MotionDataSamplingRate
ReplayEnable
JasperCalib
CISP_POOL_STAT_PIXELOUTPUT
ledID
Jasper Processing
ZFRPC.cpp
apsMode
currASscore
overrideDefaultPosition
localValidationYAngleCorrection
exclaves
StatsBuffer
SetMaximumFrameRateNow
shared memory mapping issue
\taFDR may be used
APSPosition
GMC_Controller.cpp
ltmLocked
binSize
fdInfo[0].yaw
BufferPoolType_RENDERED_RAW
infinityDown
snfNLMeanEn
%d
/var/mobile/Media/DCIM/oismetaCam
SetLightSourceMaskTunableConfiguration
tfEnabledInRaw
SavageDeviceRev
total number of descriptors
lscTableSource
aeLimitsReached
adjustedWeight1
BufferPoolType_STILL
SYNC_GROUP_NONE
manualPositionInProgress
ISP_SavageAuth
currentRecord->prevInSorted[angleIdx] != -1
sensorTemp=%d 
RGBJInitialMode
enable
SetStreamSensorRawOutputRetainedBufferCountsInternal
afScores_bayerY_15x3_bpf_f1
ispQuadraBinFactor
gmcRotZ
ReferenceIndexUsed
Timestamp
LightSourceMaskInfoAttach
Shared LTM
previewZoomFactorScaler1
laKnobStatus[CISP_KNOB_SHARPNESS]
linearityBlack
currIRScore
pflEstimatorConverged
/usr/local/share/firmware/isp/3524_01XX.dat
Shared LTC Data
PowerSupplyVoltage3
%s/%s.bin
SavePreBracketingFrame
MasterChannel
moduleIntegrator
PSB8DepthBin0LastACC
INF
rawHeight
\tCouldn't find AP ticket file at path %@
---------------------------------------------------------------------------\n
sphereStatus: %d\n
gravity[1]
curScanPosition=0x%04X afFocusMoving=0x%02X 
lastFdAFWindowID
FCCl
isNormalizedDx
dense
.log
SetGroupActiveStreams
timeStamp: 0x%016llX\n
earlyOut_rawR_7x1_hfir
ISF: Confidence is out of bounds (%.5f should be between %d..%d). This result will be ignored
ExclaveInitCaptureDevice
bodyAverage
focusOperation_currGy
focusBandStdRef[16]
SparseLowPowerProbeB
processRawSessionStarted
ADRCExposureRealizedGain
JasperCurrentState
H16ISPCaptureStreamAddAttachmentsToSampleBuffer
PrePostLTMThumbnailInfoAttach
binning 1/4
bayerYSumBandLowWin[16]
RgbjConfigurationLowFrameIntervalThresholdX
rawTapPoint
isDataPadded
focusBandAvgPrev[16]
focusRangeRestrictionFarValue
Image4CryptoHashMethod
visBaseCountControl
PearlISFStepDetectionMode
tileRegionWidth
dI_delta_infDnCal_to_hyperFocal_fwdac
com.apple.h16ispdevicecontroller.notifications.queue
Shared BodyDetector
setFileSubVersion Major
crcInfo
/var/mobile/Library/ISP/Pearl/IsfIRHistory.bin.bak
TimeOfFlightAutoFocusAssistant::activate: SetTofControlMode ch:%d owner:%d enable:%d mode:%d burst:%d
RawImageProcessStillFlowEnabled
EnableDCSNonVisionData_Private
H16ISPGraphInfoNode - No buffers in message (that is strange)
Sparse
focusRangeRestrictionNearValue
StereoGMC-RotationZ
thread_info() for THREAD_SCHED_FIFO_INFO failed
CISP_POOL_SMV_HAIR
%s/%@.bin
DCSAudioAccelConfig_isFilterBypass_Private
NumDoublets
ReplaySIFRRawFilePath
SegmentLEDLevels
outStats->tests.isEnoughNinliers = %lf\n
fwVersion
savePeridotCalib
inputCallbackForGrimaldiHighFreq
DotMult
min_ze: %f\n
YonkersMNS
rawDMASrcCropWidth
flickerConfidence[1]
%@/buffer-%@.raw
CISP_POOL_META_CAPTURE_FULL_RES
FirmwareToolchainName
sensor-type
MetaDataProjectorMode
TeleDensificationForceWide
sha2-384
Shared DMA Config
shiftParamsS2dCoefB
/usr/local/share/firmware/isp/OCCl-cmcd.DAT
Cam%dAWBScheme
CaptureStreamAddAttachmentsToSampleBuffer
Cannot initialize decompression.  Compressed buffer size %zd too large. \n
AddValueToHelper
slaveCamera-CCM row 0
com.apple.dietappleh16camerad.firmware_loading
ExclaveFIDVersion
colorImageBeforeEq.pb
GazeX
ForgetFirmwareDuringPluginTeardown
Cam%dCAFHintAction
ISPProcessingConfig
focusID
strobeLEDCalibData
bracketingCaptureCount
tfEnabled
CorrProfileAccumScalar
 :
refSpX0
Jasper frame offset from array: AXY value not an array...
queueing failed
    Platform Name: %s\n
%d\n
currAFScore_bayerY_3x3_f1
SparseLowPower
ISPExclaveFiltrationThreadMain
FaceRoi
trefmaxtof
%m%d%g_%H%M%S
CaptureGroupFinalize
error: brightness system client initialization failed.\n
fullResHeight
edgeGrValidPixPercent[16]
ISP_SendCommand
staticDistCxyX
Unload data file: channel: %d, type: %d, status: 0x%08X\n
colorRotationMatrix
vaSample: ts=0x%016llX  mode=%u Dt=%10.5f De=%10.5f adc=%d dac=%d ntc=%3.2f R=%3.3f coilTemp=%3.2f\n
StdFilter
lastFdAFWindow.y
JasperPreloadFrameConfig
FigMotionISPHallDataFromCFData
Current focus position
pixelFilterBlending
stride
H16ISPVerboseFlags
AddValue
faceX0
grayworldWBGain[2]
motionSumGr
intrinsicsEFL
Jasper Frame Config: applying mode %d
\tAP ticket digest doesn't match boot manifest hash
PDC_RAW
Chip ID: %s\n
ActivateANSTSemanticOutputInFrameReceiver
colorProcTotalSensorCropX
index
Component Validation
IMU 
RegType
windowSize > 0
H16ISPCaptureDevice: [ch%d] Time from stream start to first frame
RotationX
channel: %d\n
Load Savage DAT File: Size = %ld; SendStatus = %08x, FileStatus = 0x%08X
hwErrors[0]
com.apple.isp.backcamerapower
FIDResizedData
ISPProcessingSessionProcessBuffers
%s: ISP_TerminateClientLoggingSession returned 0x%08x\n
appleh16camerad
IsfDifferenceZQ31
CCM row 0
runAE
NotifySystemStatusForCIL
FrameReceiverMessage
channel
motionFromAEMatrix
H16ISPGraphExclaveAutoExposureNode
GetUnitInfoPropertyDict
Jasper Frame Config: Failed read file %@
teleFOVUpperRightY
output block
%d.%d.%d
ISPExclaveExfiltrationThread
ISFDuration
Y
com.apple.gmc.postprocess
Logging Buffer Corruption.  Aborting Logging\n
GMC_ToleranceTest, Relative angles: (%lf, %lf, %lf), tolerances: (%lf, %lf, %lf)\n
focusBandAvgRef[16]
ch1[%03d]
NO
%s: Unsupported companding mode: %d
sensorSifrQuadraBinFactor
SPDProcessWrapper
DIETemperatureStandby
ShiftParams_S2DCoefB
-%d
tailspinTimeout
softDGain
JasperPresetIndex
Could not find reference plist at %s (errno: %d). Will use ISP references
HandleSecureStreamOutputConfig
UserStudy
No face ROI available.
removeDataBufferPoolFromFrameReceiver
LPDPEqualizationDFEh2
Pass
secondWBGain[3]
focusStableCount
ColorExtrinsicsMatrix
minScanCoverage               = %u\n
NormDX2
ActivateStillImageRawOutputInFrameReceiver
SetSIFRCommonPool
bayerY2Gcoeff_Gb[16]
pContext->params.flow.levels[0] == 1
\tValidating Calibration UUID
H16ISPSetMachThreadPriority - proc_pidinfo() failed\n
output format
snfRadialGainEn
OISActuator
CISP_POOL_ID_FSCL
Prod
fdInfo[0].score
v24@?0Q8Q16
EnableTNR
ReadCalibrationData
CaptureDeviceSetProperty
AP
m_tail[angleIdx] == newRecord.prevInSorted[angleIdx]
doubleValue
linOutputBitDepth
numConsecutiveDecreaseInMeasurement_rawGr_7x1_hfir
H16ISPFirmwareLoggerThread
floodCalibrationCurrent
JasperComplianceNoDepthMaxValue
%@/%@
cropWidthScaler
thumbnailEnable[1]
StereoGMC-RotationY
TeleDensificationState
Illegal attempt to insert a record with no confidence.
MasterStream
ERROR: %.4s timestamp >= sensorRVSync! imuTimestamp=%llu ispTimestamp=%llu delta=%lld\n
YCCProcBlock
StopExclaveStreams
SecureDeviceProximityDetectionSetDeviceTypes
m_width == m_height
logicalOLPosFromCurrentDAC
version
localHistBinSize
cropWindowPDEWidth
PowerOnExclaveKit
Jasper frame offset from array: AXY: deltas out of bounds
DCSFPGASyncControl_frameRate_Private
Unexpected binning mode 0x%08x \n
BufferPoolType_DEPTH
island-notch-location
BackTeleCameraSNUM
ProResRaw
BufferPoolType_PDE_NORM_DX
MOVReplay
bSifDMACompress
sensorBlkAvgFiltered[2]
afScores_rawGb_7x1_hfir
lensMotionSpeedHint     = %u\n
CNTXSW_RAW
w_avg: %f\n
colorProcTotalSensorCropHeight
TorchManualParameters
SetLightSourceMaskConfiguration
CISP_POOL_RGB
moduleLensID
NormaDxToCanoncialDisparityMultiplier
pCmdAppleChLSCConfigure->tableSize == pCmdAppleChDSCConfigure->numEntries
EventType
CameraChannel
Flood
OIS/Motion Debug Log\n
curveUpdate
convertTrackingConfidenceLevel
ISPDebugFiltration
v12@?0B8
on
snfTNRFilterStrength
SPD.cpp
sphereCtrlErrX
SR_T_rawGr_7x1_hfir
pContext->geometry.roi.cellCountY == geometryCorr.profileSize
Depth pixel buffer format should be kCVPixelFormatType_FixedPointUnsigned13_3 if they are absolute values (not normalized dx)
focusNowHintFW_RangeRestrictedRemapSearchPos
accelMinSample
createPeridotCalib
Interp1
green-red
matrixUseWindow
thumbnailEnable row 1
\tLooking for local cache\n
ToneCurveLocked
GetLSCCoefficients
cmcd
shared.cpp
SetDeghostingFeatureConfiguration
moduleDayofWeek
height
dynamicBLCEnabled
Slave
faceIRValid
acceptableFocusBandsSet
flare.intensity <= Params::Flare::NINTENSITIES
slowSyncAveFlashOffLux
preFlashEmptyFocusBand
currAFScore_rawB_7x1_hfir
BayerArray::Dump -- empty array
TestPatternFlatField
Det
Cam%dSpikeDetection
PrepareGridCalculation
Prepare
Soft Brick to Hard Brick
com.apple.isp.JasperStateTransitions
startupCalStatus
Jasper Frame Config: Config file size unexpected (%lu != %lu)
EnableSDOF
XPosition
Couldn't combine frontIR chipIDStr and uidStr
postureCorrectionY
msafUpdate
focusLockCurrentTime
FDDCNFacesArray
ThresholdPassed
black
accelMaxSample
KPD 
Cam%dCalCropOffsetY
FlickerDetectorAlphaDenominator
Jasper Bank Config: Failed to open file %@
basic_string
SetSharedBufferPoolConfigurations
H16ISPServicesRemoteTypeKey
true
(filterSize % 2) == 1
ErodeOrDilateRect2x2
currGravity_x
camOrientationIndex
property
deltaX
AppleDieTempController
\t stride: 
resizeThumbnailRawPool
Resistance
%s%s.%lux%lu.%lu.%s.bin
/usr/local/share/firmware/isp/FCCl-Override.DAT
Unknown Status
SetSensorRawOutputBufferPool
GroupStillImageCaptureNow
BufferPoolType_YUV2
dpcEnabledInRaw
SetAFWindowParams
afGravityYHistory[16]
minOnTargetDurationToBeStable = %u\n
sphereMeanCurrent
lumaLUTUpdated
pContext != nullptr
PCERFCLockEnabled
FullImage
Shared LTM LUTs
Shared PDAFHW Debug
kCICMaxPerModuleX >= numXCIC
ConfigureFrameworkAutoExposure
IOServiceFirstPublish
H16ISPServicesRemoteRGBJMetadataKey
deltaRotationZ
PPD-Errors
fullImgXAngleCorrection
PO
CaptureDeviceCopyProperty
sensorReadOutCropWidth
AWBStatsUpdated
GMC Fail: Bundle adjustment did not converge
v12@?0i8
m_ownsData
cxyX
afScanStartTime
GMODropBeforeWakeup
acquire
SimulateYUVBufferStarvation
captureType
bHistSelSrcRGBY
MetaDataProjectorPowerProbeA
DCSAudioAccelKeySampleCallback_Private
Created: %s\n\n
None
StereoGmc
totalCropWidth
GetFrontCameraOffsetFromDisplayCenter
CISP_POOL_WSEG_MAP
bd[]
crop=%d/%d/%d/%d scale=%d/%d 
DumpGmcIrBuffer
ProximityMonitoringEnabled
PDE_NORM_DX
tnrAverageMode
LsAdjustEnableCam%d
focusingMode            = CONTINUOUS\n
Failed to create %s dir
Cam%dSIFRControlMode
FaultDT0
ExclaveGraphManagerInitTest
CaptureGroupCopyProperty
off
ConfigureFrameworkChannelSettings
FDOD
ISF: %s
dxcShiftOffset
afeGeom.initH == 0 || afeGeom.initH == 1
outputPaddingRows
pIn2 != nullptr
ISP_ColdBootPowerCycle
enrollStatus
colorExtrinsicsLocationY
/var/mobile/Media/DCIM/ISPCPU_LOG_
m_cols == B.Rows() && \"Input dimensions not legal\"
cropXScaler
/var/mobile/Library/ISP/CalData/DCNUPixbuf_0
H16ISPServicesRemoteCFTypeDataKey
throttle
goodForOnlineAdaptation
DCSAudioAccelConfig_range_Private
EnableIRProjector
AppleARMPE
Shared Motion Info
aeBlend
zTgtUm_LFAF
ComputeBinnedXtalk
H16ISPFlickerDetectorCreate
xqSorted.GetNumOfPoints() > 1
CISP_POOL_PDE_DEPTH
drcDarkAmplLimit
startPt.GetNumOfPoints()==1
Jasper frame v%d (expected:%d)
firstWBGain[3]
focusBandLowTh
SupportedLinkFrequencies
AWBTemporalStabilizationEnabled
APS_w_Private
LTMAEStableWaitTime
inputCallbackForPenrose
execute
x1.Cols()==4 && x1.Rows()==3
AC line flicker frequency
currentFocusScore=0x%016llX 
ProjectorRikerStatus
setfileMainVersion
imageOrientation
lsNormSelect
sensorBlkOffset[4]
thumbnailEnable[3]
sphereBoostMode
x2.Cols()==4 && x2.Rows()==3
FlickerDetectorIsGrimaldi
%@.jpeg
operator()
CopyVideoOutputConfigurations
FilteredRotationY
oisContactStopOffset
getCVPixelFormat
GMC Pass
/usr/local/share/firmware/isp/2820_01XX.dat
ExclaveSetDeviceModelsParameter
RgbjReportControllerReached
fdAWBDebug.firstValidFDFrame
comboWBGain[2]
derivedVector
cropWindow[]
SetCameraConfig
SetPrimaryFrameSkip
UpscaleFactor
TNRDebug
Depth perspective not corrected.
RAW
/var/mobile/Library/ISP/PFLEstimatorState
DotRepeatProductFromRight
Shared FD DCN Debug
CISP_POOL_RENDERED_SCL1
faceWeight
rawAverage[B]
af_bpf_f0_filter_idx
F
Temperature
Personalized firmware root path accessor not found
nfAGain
fdAFWinStartY
Chose full image calibration result
Reading rosaline power from sysconfig\n
FaultDT01ST
SetGroupAFWindowParams
kGICMaxPerModuleX >= numXGIC
tofColorSynchronizerVerbose
Full Image
Component Validation: Failed to query status for component %d: %@
GMC_FaceCoverageTest, coverage: %lf, num points: %d\n
localHistBlockSizeX
Failed to read boot time. errno %d
DCSFPGAStatus_fpgaBatStatus_Private
RgbjConfigurationLowFrameIntervalThresholdZ
drcVarianceSpace
EnableVIODebug
sensorBlackLevel
aeStable
TestPatternColorBar3
bCaptureNowStartTime
.\n
Loaded header of file 
Sending reference file %s, type: %d\n
Cam%dOisMetaFileMode
DenseLowPowerProbeAB
com.apple.isp.Gmc
com.apple.isp.backtelefocusing
gyro_std: %f\n
lastFocusedScore_bayerY_15x3_bpf_f1
Failed to create log message string with code: %d (0x%X)
Cam%dVIS
DenseInterleaveProbeAB
FilteredRotationZ
DnPerLuxSec
floatAFWinScore
tileRegionHeight
resizeStillMetaPool
FT
secondary
afWinStartY[16]
DynamicVoltage
B24@?0Q8^v16
xy_std: %f\n
/var/mobile/Media/DCIM/%s-%s-
ispTorchOnTimeStamp
drcVarianceIntensity
afBayerBSumPerWindow[16]
FrameModes
\tFailed to initialize Manifest from ticket
MasterSlaveAPSFocusEnable
raw8
afAvgScoreHistory_bayerY_viir_f0
LoadFDRDataFileCMPM
iOSBuildVersion
GetISPCounterFrequency
CopyGDCCoefficients
Cam%dEnableAPS
EnableIRFramesToPDE
H16ISPJasperDepthNode.mm
Couldn't create reference file %s to write\n
PrimaryAndSecondaryScalerConfigUpdateAtomically
DenseInterleaveLowPowerProbeB
RgbjReportFailedToSave
AEStatsUpdated
whiteWeight
gmcResult
currAFScore_bayerY_viir_f0
aeShutterTime=%d 
VisPipe
H16ISPServicesRemoteRGBIRBufferIRKey
lastFocusedScore_bayerY_15x3_bpf_f0
dcnu
GMC Fail: Inliers Spatial Coverage
GMC Fail: Face Coverage
CISP_POOL_YCC
Ngsk
updatePCECalibWithISF_block_invoke
InsertRecordInSortedList
H16ISPServicesRemoteRGBIRBufferColorKey
onlineUpdate
PrintInvalidANSTDetections
DistortRadialLiteInternal
snfEnabled
SavePFLFile
laKnobStatus[CISP_KNOB_CHROMA_NR]
nextV
EnrollmentState
earlyOutMeasurementLimit_bayerY_viir_f0
bayerYSumBandLowNegativeOverrideTh
Calibration data not consistent.
Jasper frame from array: frame data size mismatch: got %ld, expecting %ld
Pearl calibration\n
adjustedTarget0
MultiCameraCalWide
MSTFEnabled
Could not retrieve any element from detected faces array.
afeGeom.cellCountY >= delayV + 1
DeactivateDeghostingOutputFromFrameReceiver
Shared Depth to Position Debug
drcRoundModeCr
ProjectorWillFaultStatus
ProjectorRigelPulseCount
SetStreamingTuningProfile
MotionDetectionResultCreateDictionaryRepresentation
DEFAULT
comboWBGain[1]
sensorBlkOffset[3]
bayerY2Rcoeff_Gb[16]
PropertyKey
RemoteRgbIr
DCSMagnetometerOperationMode_Private
nfKnobLevel
SR_T_bayerY_3x3_f1
ISP_CILRequestPerChannel
colorImageAfterEq.pb
HITHInfoAttach
statBinV
wideCamZoomFactorScaler0
/usr/local/share/firmware/isp/1922_02XX.dat
ActivateIntermediateTapOutputInFrameReceiver
SetTemporalNoiseReductionConfiguration
RgbjConfigurationMinFrameNumAtLowInterval
SetExclusivelyForSecureProcessing
BufferPoolType_FACE
testSetSize == tsPtsIdx+1
CISP_POOL_FEP_THUMBNAIL_RAW
token was removed
AddHiResRawPoolToFrameReceiver
PARAMS (input)
FilteredRotationXDiffFromPrev
CameraStrobeMaxLoad
flickerWaveMatch[1]
com.apple.isp.frontcamerapower
DPCm
visLogDerivedStepControl
/var/mobile/Library/ISP/JasperL/session_persistency.plist
SetMetadataOutputConfiguration
fdAWBDebug.continuousFDTimes
ISF: history mismatch: %d != %u
Failed to open token log file.
AddSashimiRawPoolToFrameReceiver
EPipeDone
laKnobStatus[CISP_KNOB_DRC_STRENGTH]
validBufRectStill.width
adjustedAve2
flickerFrequency[0]
v16@?0^v8
%s token does not match device. Token will be removed.
ValidateComplianceWithDetails
BufferPoolType_PDC_RAW
delay
pdafDefocusDAC
CalibrateRgbIr.mm
FillExtrinsicCalibrationData
LPDPEqualizationDFEh4
LPDPRCParamR
Yonkers/YonkersPatch%s%s.DAT
zoomFactorColorProcTap
Failed to send references to FW\n
metadata version (major)
afScoreHistory_rawR_7x1_hfir
soc-generation
ReplaySIFDMAMode
GMC_ToleranceTest, angles: (%lf, %lf, %lf), tolerances: (%lf, %lf, %lf)\n
cropHeightScaler1
drcRoundModeCb
ch1
%s%s/%s
-dense
afScores_bayerY_hiir_f0
focusTriggerCBAFSceneChangeDeclaredTime
IrResolution
SIFR-Raw
CaptureStreamCreate
metadata->timeStamp (dec): %llu\n
/Yonkers/YonkersPatch.DAT
focusDelayCount
TofSync_AFMatchInterval
PropertyConfigurationKey
CISP_POOL_PDE_GMS
efl: %f\n
strobeCCTEstimate
sphereCtrlErrY
bodyBlockY1
F 
PCEOutputFormat
y.GetNumOfPoints() == v.Rows()
LoadFDRCalDataFile
%s-Ch%d.DAT
/usr/local/share/firmware/isp/7424_01XX.dat
banks
Unable to find prox service
SIFR_RAW
OISTemperature
lastFocusedScore_bayerY_3x3_f1
earlyOutMeasurementLimit_bayerY_hiir_f0
FusionMinDepthThreshold
Cached UUID: 0x
CamSave2File
AFTestScriptLoad
ScanModeStep
ambientLuxLevel
colorHistEnabled
HiCCTbgBias
Failed to update %s token file. Will return false so someone looks at that...
Jasper preload frame from array: failed to send command to firmware: 0x%08X
SetMultiCamConfiguration
TestModePopulateMockPerceptionResult
com.apple.isp.frontirprojector.dietempidle
/usr/local/share/firmware/isp/Savage/SavagePatchOverride.DAT
SplitPhotodiode_Private
 (see CVPixelBufferPrivate.h). Please contact PortableBuffer support.\n
BufferPoolType_YCC
outStats->isToleranceTestPass = %lf\n
Shared Distortion
rawDMASrcCropY
AttachCatHeadsDict
com.apple.pearlcalibration.algorithm
MetaDataProjectorPulseWidth
ANSTThumbnailInfoAttach
ImageRegistrationInfoCreateArray
inputCallbackForPenrose2
strobeID
PDPCleanedBuffer
goodIdxRoiMask
/usr/local/share/firmware/isp/6222_01XX.dat
O 
GenerateBufferTagsForOutput
Process_x4
XMinIndex
nCols2%2 == 1
\tCouldn't get crypto hash method
out
com.apple.h16ispgraphexclaveexit.callback.queue
com.apple.h16ispframereceiver.postprocess.queue
readOutTime
im.Cols() > 2 && im.Rows() > 2
FusionFixedDepthValue
BufferPoolType_SPARE
sizeHistSelBin
ccmDesatBlending
bCaptureNowDeltaLastFocusScanTime
ISP_UnregisterEPipeDoneCallback
IrUI16.pb
CurrentFrameRate: %f\n
luxLevelLow
InsertNewRecord
type
Jasper sequence from array: failed to send command to firmware: 0x%08X
m_rows == mat.Rows()
BackTeleCameraModuleSerialNumString
JasperBurstSize
CopyAutoFocusDriverShortStats
CISP_POOL_ID_JASPER_DEPTH
luxLevelHigh
fdAFWinID
ManualLTM
success
expBias
verifyStatus
removeBufferPoolFromBufferReceiver
H16ISPMotionManagerInitializationThread
IOService
DumpPCEFusion
Cam%dEnableDPMAssistedAE
ChipState
sessionID
afeGeom.initV == 2 || afeGeom.initV == 3
com.apple.isp.backtelesensortemperature
earlyOut_bayerY_15x3_bpf_f1
isLFAFDataValid
Jasper frame from array: frame not a data...
previewScaler
ActivateExclaveOutputInFrameReceiver
StartStreaming
com.apple.video.PhotometerManager.CommandQueue
RoiIntermediateConfidenceScores
ProjectorMamaBearStatus
AFAssist Debug meta-data section not found in frame meta-data.\n
Found FrontIR override (has highest precedence) HPR file - camChannel = %d
ltmRectStartX
RPCFileInfo
/usr/local/share/firmware/isp/Yonkers/YonkersPatchOverride.DAT
ISF: element.nextInSorted[%d] points to an index out of range: %d
\tCan't read serial number from cache
EnableFocusPixelMetadata
EnableMetadataSectionsHigh
LPDPEqualizationDFEh1
fodValidData
FlowAccumulateRow1x1Scalar
SetVideoOutputsEnabled
BufferPoolType_STILLYCC
captureStreamEndTimer
RawFaceDetectData
pos<m_size && m_nnz<m_maxNNZ
sceneLuxLevelHigh
SMVS 
DisjointSet.cpp
Sample buffer does not contain pixel data.
SetSynchronizedSensorRawOutputRetainedBufferCount
cropWidthScaler1
hwEvents
bHistEnabled
earlyOutMeasurementLimit_rawR_7x1_hfir
computePTS
Could not read calibrated power from IOReg\n
SyncGroup
DCSDataFileLoad_FileType_Private
matrixPeak
RGB-IR Calib: Local validation succeeded and full image result was selected: x=%.1f, y=%.1f, cost=%f
GetNumOfPoints() == rhs.GetNumOfPoints()
CamFWPoolPrimeCount
ChromaticAberrationReductionEnabled
lowCCTrgBias
stageWeight
statWindowHeight
SetPrimaryScalerCrop
StereoGmcStatus
0x
motionSumR
localHistEnable
gmcValid
FlowPostProcess
irImAfterGaussianFilter.pb
e_avg: %f\n
afScores_bayerY_3x3_f1
FirmwareReleaseVersion
ModuleLensID
STILLMETA
LPDPErrorCount
pIn1 != nullptr
apsPFLOffset
rawWidth
CreateStreamSession
com.apple.isp.frontirfloodtemperature
H16ISPServicesRemoteDeviceID
regType
luxLevel=%d 
Value_Private
BufferPoolType_IR
fdAWBDebug.minDistSkinToWhiteMapping
snfBinMode
sensorBlkAvg[2]
binning.all()
GMC Fail: RANSAC
Shared VisionProc
thumbnailWindow
Dumping ToF Raw buffers to path \"%@\"
TorchLevelOverride
en
sceneLuxLevel
overallASscore
PDAFProcessX3Wrapper
PortableBuffer version (v
RGB-IR Calib: Fine grid minimum for full image: x=%f, y=%f, cost=%f
ANSTThumbnailFeatureAnnounceSupport
RunScript
bodyConf
completeAllRequests
Local validation failed
Debug PCE Depth Writer
oisSampleCount
NVM
kH16ISPFrameReceiverBufferPoolType_SPLITPD
AppleH16PhotonDetector
intrinsicsPPCurrentConfig[0]
Unexpected Peridot DT1 v%d (expected:%d). Metadata might mis-behave
priper
synTagWBG
preFlashMinScoreIndex
GetCameraConfig
DCSFPGASyncControl_Private
DeghostingFeatureGetPoolRequirements
killall
matrixParamsToSet_percentile
AUX (Horizontal Edge Map)
ActiveNondisruptiveStreamingFormatsTrackIncludedConfigs
CISP_POOL_PDE_NORM_DX2
previewOutputHeightScaler1
darkOutlierCount
b2y_G_coeff
m_head[angleIdx] != -1
PDE_GMS
CISP_POOL_HI_RES_HITH_THUMBNAIL
Shared MasterSlave AF
BackEnd
motionSumGb
snfAttnEn
SendDeviceImpacts
Jasper preload frame from array: property not an array
@\"NSObject<OS_xpc_object>\"8@?0
apsPFL
TestPatternPN31
%@-%@
masterCam
curSceneBrightnessEstimate
slaveCamera-bgCalGain
cellInBuffer == 0
%s token activation count updated to %d
ToFCapturingPresetIndex
ActiveSyncGroupChannelIndex
H16ISPPhotometerManager_block_invoke
PDAFPixelEngine.cpp
GMC-NumOfPoints
YStartIndex
NoiseReductionLevel
SecureIRBaselineStreamingEnabled_Private
device proximity detection
sendMessageSync
Jasper frame offset from array: no offsets found
CopyFocusPixelMap
ispDGain
exposureMode
GetFocusPixelSamplingRateH
com.apple.isp.backtofprojector.ntctempstandby
ANSTFeatureGetPoolRequirements
EXCLAVE_SOURCE_AE_REQ_LATE ch 0x%x tailspinCode 0x%x
afScoreHistory
ReturnAllUnusedBuffers
\tFailed to digest AP ticket
ChannelMaskForSharedHiResRawPool
FullGrid
cropYScaler1
TestPatternGreenField
fault1
GetSensorNVMBytes
unavailable
InitSupportedFormatsForCaptureStream
EPD thresh: %lf, inlier rate: %lf, tested percentile: %lf, result: %lf\n
binSize1
MultiplePearlCalibration
com.apple.isp.backtofsensortemperature
binWidth
com.apple.isp.backsuperwidesensorconfig
AnfdModality
AF-Assist
fullImgYAngleCorrection
Depth pixel buffer format should be kCVPixelFormatType_FixedPointUnsigned11_5 if it is normalized dx
YogiFaultCSpecialFunctions
UseAuxRawPool
s1
RigelSerialNumber
SetMinimumFrameRateNow
LuxLevel: %d\n
lrsHeight
maxPt.GetNumOfPoints()==1
Failed to load Jasper files\n
AddDCSNonVisionDataPoolToFrameReceiver
af_hrz_filter_idx
LSCConfiguration
System performed boot since %s token creation (boot time: %ld). Token will be removed.
CopyProcessingSessionDefaultProcessingParameters
focusScanSearchPositionsToSet
CaptureDeviceRequestStreams
UnknownMode(%d)
vector
\tFound\n
Channel %u
SetContentAwareAWBEnabled
H16ISPCaptureGroupCopyProperty
SensorNVM
mbnrConfig[%d]
Failed to create JasperLCalib.bin
snfRecursiveMode
numResults
WSegThumbnailInfoAttach
Correspondences
tapToFocusMode
DumpGmc
com.apple.isp.cameratorchcoolcurrent
TorchColor
frame skipped
CISP_POOL_HIRES_RAW
focusTriggerConsecutiveOutOfBandFrameCountTh
TestPatternIncremental
R 
RigelFaultInterruptMask
DeactivatePrePostLTMThumbnailOutputFromFrameReceiver
H16ISPServicesRemoteReturnKey
blue
sphereStatus
m_tail[i] == m_oldestIdx
XStartIndex
UserStudyLowPower
GetSharedHiResRawBufferPoolInfo
FilteredRotationZDiffFromPrev
%s.root
afAvgScoreHistory
matrixParamsToSet_earlyOutDecrementAmount
GetNumCameraConfigs
Distance
AddProResRawPoolToFrameReceiver
CopyProcessingSessionSupportedOutputs
```
