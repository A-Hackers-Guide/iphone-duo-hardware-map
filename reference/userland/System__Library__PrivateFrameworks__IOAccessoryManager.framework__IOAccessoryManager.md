# `/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`

iOS 27.2 dyld shared cache image. Version `1068.40.6.0.0`. **[DSC]**

## Linked libraries (16)

- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Accelerate.framework/Accelerate`
- `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`
- `/System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/usr/lib/libIOAccessoryManager.dylib`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/UIKit.framework/UIKit`
- `/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`

## Objective-C: 17 classes, 5 protocols, 1051 methods, 502 properties

### Class pages

Every class and protocol, with its methods: [`HalogenAudio`](../objc/HalogenAudio_IOAccessoryManager.md), [`HalogenAudioDelegate`](../objc/HalogenAudioDelegate_IOAccessoryManager.protocol.md), [`HalogenCalcTypeC`](../objc/HalogenCalcTypeC_IOAccessoryManager.md), [`HalogenLdcmCalc`](../objc/HalogenLdcmCalc_IOAccessoryManager.md), [`HalogenMeasurement`](../objc/HalogenMeasurement_IOAccessoryManager.md), [`HalogenTypeC`](../objc/HalogenTypeC_IOAccessoryManager.md), [`HalogenWrapper`](../objc/HalogenWrapper_IOAccessoryManager.md), [`IOAccessoryLDCMPortManagerTypeC`](../objc/IOAccessoryLDCMPortManagerTypeC_IOAccessoryManager.md), [`IOAccessoryLdcmHealthClass`](../objc/IOAccessoryLdcmHealthClass_IOAccessoryManager.md), [`IOAccessorySystemStateEndpoint`](../objc/IOAccessorySystemStateEndpoint_IOAccessoryManager.md), [`IOAccessorySystemStateMonitor`](../objc/IOAccessorySystemStateMonitor_IOAccessoryManager.md), [`IOAccessoryUserLdcmParamClass`](../objc/IOAccessoryUserLdcmParamClass_IOAccessoryManager.md), [`IOPortLDCMManagerV4`](../objc/IOPortLDCMManagerV4_IOAccessoryManager.md), [`LDCMMeasurementV4`](../objc/LDCMMeasurementV4_IOAccessoryManager.md), [`LDCMMobileAssetDistributor`](../objc/LDCMMobileAssetDistributor_IOAccessoryManager.md), [`LDCMMobileAssetManager`](../objc/LDCMMobileAssetManager_IOAccessoryManager.md), [`LDCMMobileAssetManagerDelegate`](../objc/LDCMMobileAssetManagerDelegate_IOAccessoryManager.protocol.md), [`LDCMNotificationUIManagerV4`](../objc/LDCMNotificationUIManagerV4_IOAccessoryManager.md), [`NSCoding`](../objc/NSCoding_IOAccessoryManager.protocol.md), [`NSObject`](../objc/NSObject_IOAccessoryManager.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_IOAccessoryManager.protocol.md)

### Classes

`HalogenAudio`, `HalogenCalcTypeC`, `HalogenLdcmCalc`, `HalogenMeasurement`, `HalogenTypeC`, `HalogenWrapper`, `IOAccessoryLDCMPortManagerTypeC`, `IOAccessoryLdcmHealthClass`, `IOAccessorySystemStateEndpoint`, `IOAccessorySystemStateMonitor`, `IOAccessoryUserLdcmParamClass`, `IOPortLDCMManagerV4`, `LDCMMeasurementV4`, `LDCMMobileAssetDistributor`, `LDCMMobileAssetManager`, `LDCMNotificationUIManagerV4`, `NSValue`

### Protocols

`HalogenAudioDelegate`, `LDCMMobileAssetManagerDelegate`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T^{OpaqueAudioComponentInstance=},V_audioComponentInst) audioComponentInst;
@property (Ti,V_nInputChannels) nInputChannels;
@property (Ti,V_nOutputChannels) nOutputChannels;
@property (Ti,V_sampleRate) sampleRate;
@property (Ti,V_bitDepth) bitDepth;
@property (Ti,V_inputFrameSizeInBytes) inputFrameSizeInBytes;
@property (Ti,V_outputFrameSizeInBytes) outputFrameSizeInBytes;
@property (T@"<HalogenAudioDelegate>",&,N,V_halogenUnitDelegate) halogenUnitDelegate;
@property (Ti,V_nSamples) nSamples;
@property (Ti,V_sizeofSample) sizeofSample;
@property (Td,V_sampleRate) sampleRate;
@property (Td,V_signalFrequency) signalFrequency;
@property (Td,V_tiaGain) tiaGain;
@property (Td,V_adcGain) adcGain;
@property (Td,V_parasiticCap) parasiticCap;
@property (Td,V_pinParasitics) pinParasitics;
@property (Td,V_seriesResistance) seriesResistance;
@property (Td,V_seriesRCResistance) seriesRCResistance;
@property (Td,V_LDCMACCapacitance) LDCMACCapacitance;
@property (Tjd,V_seriesTotalImpedance) seriesTotalImpedance;
@property (T@"NSMutableData",V_tmp1DataBuff) tmp1DataBuff;
@property (Ti,V_tmp1DataBuffSize) tmp1DataBuffSize;
@property (T@"NSMutableData",V_tmp2DataBuff) tmp2DataBuff;
@property (Ti,V_tmp2DataBuffSize) tmp2DataBuffSize;
@property (T@"NSMutableData",V_tmp3DataBuff) tmp3DataBuff;
@property (Ti,V_tmp3DataBuffSize) tmp3DataBuffSize;
@property (T^{OpaqueFFTSetupD=},V_fftContext) fftContext;
@property (Td,R,V_voltageGainCorrection) voltageGainCorrection;
@property (Td,R,V_currentGainCorrection) currentGainCorrection;
@property (Td,R,V_currentPhaseCompensation) currentPhaseCompensation;
@property (Td,R,V_calVoltageSignalLevel) calVoltageSignalLevel;
@property (Td,R,V_calVoltageNoiseLevel) calVoltageNoiseLevel;
@property (Td,R,V_calCurrentSignalLevel) calCurrentSignalLevel;
@property (Td,R,V_calCurrentNoiseLevel) calCurrentNoiseLevel;
@property (Td,R,V_calVoltageSNR) calVoltageSNR;
@property (Td,R,V_calCurrentSNR) calCurrentSNR;
@property (Td,R,V_calVoltageAmplitude) calVoltageAmplitude;
@property (Td,R,V_calCurrentAmplitude) calCurrentAmplitude;
@property (Td,R,V_measurementVoltageSignalLevel) measurementVoltageSignalLevel;
@property (Td,R,V_measurementVoltageNoiseLevel) measurementVoltageNoiseLevel;
@property (Td,R,V_measurementVoltageSNR) measurementVoltageSNR;
@property (Td,R,V_measurementCurrentSignalLevel) measurementCurrentSignalLevel;
@property (Td,R,V_measurementCurrentNoiseLevel) measurementCurrentNoiseLevel;
@property (Td,R,V_measurementCurrentSNR) measurementCurrentSNR;
@property (Td,R,V_measurementVoltageAmplitude) measurementVoltageAmplitude;
@property (Td,R,V_measurementCurrentAmplitude) measurementCurrentAmplitude;
@property (Td,R,V_measurementVoltagePhase) measurementVoltagePhase;
@property (Td,R,V_measurementCurrentPhase) measurementCurrentPhase;
@property (Td,R,V_goertzelImpedance) goertzelImpedance;
@property (Td,R,V_goertzelPhase) goertzelPhase;
@property (Td,R,V_compensatedImpedance) compensatedImpedance;
@property (Td,R,V_compensatedPhase) compensatedPhase;
@property (Td,R,V_loadImpedanceInOhms) loadImpedanceInOhms;
@property (Td,R,V_loadPhase) loadPhase;
@property (Td,R,V_resistanceInOhms) resistanceInOhms;
@property (Td,R,V_capacitanceInNanoF) capacitanceInNanoF;
@property (TB,R,V_wetTooLong) wetTooLong;
@property (Ti,V_nSamples) nSamples;
@property (Ti,V_diffWindowSize) diffWindowSize;
@property (Ti,V_clipDetectWindowSize) clipDetectWindowSize;
@property (Ti,V_sizeofSample) sizeofSample;
@property (Td,V_sampleRate) sampleRate;
@property (Td,V_signalFrequency) signalFrequency;
@property (Td,V_adcGain) adcGain;
@property (Td,V_tiaGain) tiaGain;
@property (Td,V_hydraImpedance) hydraImpedance;
@property (Td,V_movesumClipThreshold) movesumClipThreshold;
@property (Td,V_hydraR) hydraR;
@property (Td,V_ldcmAcCap) ldcmAcCap;
@property (Td,V_sanitycheckImpedanceLowerbound) sanitycheckImpedanceLowerbound;
@property (Td,V_sanitycheckImpedanceUpperbound) sanitycheckImpedanceUpperbound;
@property (Td,V_sanitycheckPhaseLowerbound) sanitycheckPhaseLowerbound;
@property (Td,V_sanitycheckPhaseUperbound) sanitycheckPhaseUperbound;
@property (Td,V_sanitycheckVoltageGainCorrectionLowerbound) sanitycheckVoltageGainCorrectionLowerbound;
@property (Td,V_sanitycheckVoltageGainCorrectionUpperbound) sanitycheckVoltageGainCorrectionUpperbound;
@property (Td,V_sanitycheckCurrentGainCorrectionLowerbound) sanitycheckCurrentGainCorrectionLowerbound;
@property (Td,V_sanitycheckCurrentGainCorrectionUpperbound) sanitycheckCurrentGainCorrectionUpperbound;
@property (Td,V_sanitycheckCurrentPhaseCompensationLowerbound) sanitycheckCurrentPhaseCompensationLowerbound;
@property (Td,V_sanitycheckCurrentPhaseCompensationUpperbound) sanitycheckCurrentPhaseCompensationUpperbound;
@property (TB,V_isDigitalFilterTrigger) isDigitalFilterTrigger;
@property (T@"NSMutableData",V_tmp1DataBuff) tmp1DataBuff;
@property (Ti,V_tmp1DataBuffSize) tmp1DataBuffSize;
@property (T@"NSMutableData",V_tmp2DataBuff) tmp2DataBuff;
@property (Ti,V_tmp2DataBuffSize) tmp2DataBuffSize;
@property (T@"NSMutableData",V_tmp3DataBuff) tmp3DataBuff;
@property (Ti,V_tmp3DataBuffSize) tmp3DataBuffSize;
@property (T^{OpaqueFFTSetupD=},V_fftContext) fftContext;
@property (Td,R,V_precalVoltageSignalLevel) precalVoltageSignalLevel;
@property (Td,R,V_precalVoltageNoiseLevel) precalVoltageNoiseLevel;
@property (Td,R,V_precalVoltageSNR) precalVoltageSNR;
@property (Td,R,V_precalCurrentSignalLevel) precalCurrentSignalLevel;
@property (Td,R,V_precalCurrentNoiseLevel) precalCurrentNoiseLevel;
@property (Td,R,V_precalCurrentSNR) precalCurrentSNR;
@property (Td,R,V_voltageGainCorrection) voltageGainCorrection;
@property (Td,R,V_currentGainCorrection) currentGainCorrection;
@property (Td,R,V_currentPhaseCompensation) currentPhaseCompensation;
@property (Td,R,V_calVoltageSignalLevel) calVoltageSignalLevel;
@property (Td,R,V_calVoltageNoiseLevel) calVoltageNoiseLevel;
@property (Td,R,V_calVoltageSNR) calVoltageSNR;
@property (Td,R,V_calCurrentSignalLevel) calCurrentSignalLevel;
@property (Td,R,V_calCurrentNoiseLevel) calCurrentNoiseLevel;
@property (Td,R,V_calCurrentSNR) calCurrentSNR;
@property (Td,R,V_goertzelImpedance) goertzelImpedance;
@property (Td,R,V_goertzelPhase) goertzelPhase;
@property (Td,R,V_compensatedImpedance) compensatedImpedance;
@property (Td,R,V_compensatedPhase) compensatedPhase;
@property (Td,R,V_clippingScore) clippingScore;
@property (Td,R,V_resistanceInOhms) resistanceInOhms;
@property (Td,R,V_capacitanceInNanoF) capacitanceInNanoF;
@property (Td,R,V_measurementVoltageSignalLevel) measurementVoltageSignalLevel;
@property (Td,R,V_measurementVoltageNoiseLevel) measurementVoltageNoiseLevel;
@property (Td,R,V_measurementVoltageSNR) measurementVoltageSNR;
@property (Td,R,V_measurementCurrentSignalLevel) measurementCurrentSignalLevel;
@property (Td,R,V_measurementCurrentNoiseLevel) measurementCurrentNoiseLevel;
@property (Td,R,V_measurementCurrentSNR) measurementCurrentSNR;
@property (Td,R,V_measurementCondetSNR) measurementCondetSNR;
@property (T@"HalogenLdcmCalc",V_halogenLdcmCalc) halogenLdcmCalc;
@property (Ti,V_nInputChannels) nInputChannels;
@property (Ti,V_nOutputChannels) nOutputChannels;
@property (Ti,V_sampleRate) sampleRate;
@property (Ti,V_bitDepth) bitDepth;
@property (Ti,V_inputFrameSizeInBytes) inputFrameSizeInBytes;
@property (Ti,V_outputFrameSizeInBytes) outputFrameSizeInBytes;
@property (T^{OpaqueAudioComponentInstance=},V_audioComponentInst) audioComponentInst;
@property (Ti,V_warmupTimeInMs) warmupTimeInMs;
@property (Ti,V_hydraSettlingTimeInMs) hydraSettlingTimeInMs;
@property (Ti,V_nMeasurementSamples) nMeasurementSamples;
@property (Ti,V_nWarmupSamples) nWarmupSamples;
@property (Ti,V_nHydraSettlingSamples) nHydraSettlingSamples;
@property (Ti,V_nTotalSamples) nTotalSamples;
@property (Ti,V_nPaddingSamples) nPaddingSamples;
@property (Td,V_signalFreq) signalFreq;
@property (Ti,V_initalPhaseInDegrees) initalPhaseInDegrees;
@property (TS,R,N,V_maxOutputAmplitude) maxOutputAmplitude;
@property (TS,R,N,V_signalOffset) signalOffset;
@property (T@"NSMutableData",V_pcmInputData) pcmInputData;
@property (Ti,V_pcmInputDataMaxSzInBytes) pcmInputDataMaxSzInBytes;
@property (Ti,V_pcmInputDataIndexInBytes) pcmInputDataIndexInBytes;
@property (Ti,V_pcmInputDataSampleCnt) pcmInputDataSampleCnt;
@property (TB,V_isCalibrationDone) isCalibrationDone;
@property (TB,V_isMeasurementDone) isMeasurementDone;
@property (T@"NSMutableData",V_pcmOutputData) pcmOutputData;
@property (Ti,V_pcmOutputDataMaxSzInBytes) pcmOutputDataMaxSzInBytes;
@property (Ti,V_pcmOutputDataIndexInBytes) pcmOutputDataIndexInBytes;
@property (T@"NSMutableData",V_currentData) currentData;
@property (T@"NSMutableData",V_voltageData) voltageData;
@property (TB,R,N,V_shouldInvertData) shouldInvertData;
@property (Ti,V_audioTimeoutInSec) audioTimeoutInSec;
@property (T@"NSCondition",V_audioTimeoutCond) audioTimeoutCond;
@property (Ti,V_measurementSampleOffsetInFrames) measurementSampleOffsetInFrames;
@property (TI,V_service) service;
@property (TI,V_connect) connect;
@property (Ti,V_pinToMeasure) pinToMeasure;
@property (TQ,V_eisPinToken1) eisPinToken1;
@property (TQ,V_eisPinToken2) eisPinToken2;
@property (T@"NSObject<OS_dispatch_queue>",N,V_systemPowerQueue) systemPowerQueue;
@property (TI,N,V_systemPowerPort) systemPowerPort;
@property (T^{IONotificationPort=},N,V_systemPowerNotifyPortRef) systemPowerNotifyPortRef;
@property (TI,N,V_systemPowerIterator) systemPowerIterator;
@property (Ti,N,V_powerState) powerState;
@property (T@"NSCondition",V_powerStateCond) powerStateCond;
@property (T@"BaseResourceArbiterClient",R,N,V_arbiterClient) arbiterClient;
@property (TB,R,N,V_arbiterLocked) arbiterLocked;
@property (TB,R,N,V_arbitrationRequired) arbitrationRequired;
@property (Ti,R,V_precalibrationSampleOffsetInFrames) precalibrationSampleOffsetInFrames;
@property (Td,R,V_precalVoltageSignalLevel) precalVoltageSignalLevel;
@property (Td,R,V_precalVoltageNoiseLevel) precalVoltageNoiseLevel;
@property (Td,R,V_precalVoltageSNR) precalVoltageSNR;
@property (Td,R,V_precalCurrentSignalLevel) precalCurrentSignalLevel;
@property (Td,R,V_precalCurrentNoiseLevel) precalCurrentNoiseLevel;
@property (Td,R,V_precalCurrentSNR) precalCurrentSNR;
@property (Ti,R,V_calibrationSampleOffsetInFrames) calibrationSampleOffsetInFrames;
@property (Td,R,V_voltageGainCorrection) voltageGainCorrection;
@property (Td,R,V_currentGainCorrection) currentGainCorrection;
@property (Td,R,V_currentPhaseCompensation) currentPhaseCompensation;
@property (Td,R,V_calVoltageSignalLevel) calVoltageSignalLevel;
@property (Td,R,V_calVoltageNoiseLevel) calVoltageNoiseLevel;
@property (Td,R,V_calVoltageSNR) calVoltageSNR;
@property (Td,R,V_calCurrentSignalLevel) calCurrentSignalLevel;
@property (Td,R,V_calCurrentNoiseLevel) calCurrentNoiseLevel;
@property (Td,R,V_calCurrentSNR) calCurrentSNR;
@property (Td,R,V_goertzelImpedance) goertzelImpedance;
@property (Td,R,V_goertzelPhase) goertzelPhase;
@property (Td,R,V_compensatedImpedance) compensatedImpedance;
@property (Td,R,V_compensatedPhase) compensatedPhase;
@property (Td,R,V_resistanceInOhms) resistanceInOhms;
@property (Td,R,V_capacitanceInNanoF) capacitanceInNanoF;
@property (Td,R,V_clippingScore) clippingScore;
@property (Td,R,V_measurementVoltageSignalLevel) measurementVoltageSignalLevel;
@property (Td,R,V_measurementVoltageNoiseLevel) measurementVoltageNoiseLevel;
@property (Td,R,V_measurementVoltageSNR) measurementVoltageSNR;
@property (Td,R,V_measurementCurrentSignalLevel) measurementCurrentSignalLevel;
@property (Td,R,V_measurementCurrentNoiseLevel) measurementCurrentNoiseLevel;
@property (Td,R,V_measurementCurrentSNR) measurementCurrentSNR;
@property (Td,R,V_measurementCondetSNR) measurementCondetSNR;
@property (Ti,R,V_halogenResult) halogenResult;
@property (Ti,V_nInputChannels) nInputChannels;
@property (Ti,V_nOutputChannels) nOutputChannels;
@property (Ti,V_sampleRate) sampleRate;
@property (Ti,V_bitDepth) bitDepth;
@property (Ti,V_inputFrameSizeInBytes) inputFrameSizeInBytes;
@property (Ti,V_outputFrameSizeInBytes) outputFrameSizeInBytes;
@property (T^{OpaqueAudioComponentInstance=},V_audioComponentInst) audioComponentInst;
@property (T@"HalogenAudio",V_halogenAudioUnit) halogenAudioUnit;
@property (Ti,V_warmupTimeInMs) warmupTimeInMs;
@property (Ti,V_AceSettlingTimeInMs) AceSettlingTimeInMs;
@property (Ti,V_nMeasurementSamples) nMeasurementSamples;
@property (Ti,V_nWarmupSamples) nWarmupSamples;
@property (Ti,V_nAceSettlingSamples) nAceSettlingSamples;
@property (Ti,V_nTotalSamples) nTotalSamples;
@property (Ti,V_nPaddingSamples) nPaddingSamples;
@property (Td,V_signalFreq) signalFreq;
@property (Ti,V_initalPhaseInDegrees) initalPhaseInDegrees;
@property (TS,R,N,V_maxOutputAmplitude) maxOutputAmplitude;
@property (TS,R,N,V_signalOffset) signalOffset;
@property (T@"NSMutableData",V_pcmInputData) pcmInputData;
@property (Ti,V_pcmInputDataMaxSzInBytes) pcmInputDataMaxSzInBytes;
@property (Ti,V_pcmInputDataIndexInBytes) pcmInputDataIndexInBytes;
@property (Ti,V_pcmInputDataSampleCnt) pcmInputDataSampleCnt;
@property (TB,V_isCalibrationDone) isCalibrationDone;
@property (TB,V_isMeasurementDone) isMeasurementDone;
@property (TB,V_selfTestCapable) selfTestCapable;
@property (T@"NSMutableData",V_pcmOutputData) pcmOutputData;
@property (Ti,V_pcmOutputDataMaxSzInBytes) pcmOutputDataMaxSzInBytes;
@property (Ti,V_pcmOutputDataIndexInBytes) pcmOutputDataIndexInBytes;
@property (T@"NSMutableData",V_currentData) currentData;
@property (T@"NSMutableData",V_voltageData) voltageData;
@property (Ti,V_audioTimeoutInSec) audioTimeoutInSec;
@property (T@"NSCondition",V_audioTimeoutCond) audioTimeoutCond;
@property (Ti,V_measurementSampleOffsetInFrames) measurementSampleOffsetInFrames;
@property (T@"HalogenCalcTypeC",V_halogenCalcTypeC) halogenCalcTypeC;
@property (T{?=iiiddddddddddddddddddddd},N,V_measurementInfoDefault) measurementInfoDefault;
@property (TI,V_service) service;
@property (TI,V_connect) connect;
@property (TB,V_measureSBU) measureSBU;
@property (Ti,V_pinToMeasure) pinToMeasure;
@property (Ti,V_ldcmState) ldcmState;
@property (TB,V_isInternalBuild) isInternalBuild;
@property (T@"NSMutableString",V_measurementInfoOutputString) measurementInfoOutputString;
@property (T@"NSMutableString",V_measurementInfoAcchalogenOutputString) measurementInfoAcchalogenOutputString;
@property (T@"NSObject<OS_dispatch_queue>",N,V_systemPowerQueue) systemPowerQueue;
@property (TI,N,V_systemPowerPort) systemPowerPort;
@property (T^{IONotificationPort=},N,V_systemPowerNotifyPortRef) systemPowerNotifyPortRef;
@property (TI,N,V_systemPowerIterator) systemPowerIterator;
@property (Ti,N,V_powerState) powerState;
@property (T@"NSCondition",V_powerStateCond) powerStateCond;
@property (Ti,R,V_precalibrationSampleOffsetInFrames) precalibrationSampleOffsetInFrames;
@property (Td,R,V_precalVoltageSignalLevel) precalVoltageSignalLevel;
@property (Td,R,V_precalVoltageNoiseLevel) precalVoltageNoiseLevel;
@property (Td,R,V_precalVoltageSNR) precalVoltageSNR;
@property (Td,R,V_precalCurrentSignalLevel) precalCurrentSignalLevel;
@property (Td,R,V_precalCurrentNoiseLevel) precalCurrentNoiseLevel;
@property (Td,R,V_precalCurrentSNR) precalCurrentSNR;
@property (Ti,R,V_calibrationSampleOffsetInFrames) calibrationSampleOffsetInFrames;
@property (Td,R,V_voltageGainCorrection) voltageGainCorrection;
@property (Td,R,V_currentGainCorrection) currentGainCorrection;
@property (Td,R,V_currentPhaseCompensation) currentPhaseCompensation;
@property (Td,R,V_calVoltageSignalLevel) calVoltageSignalLevel;
@property (Td,R,V_calVoltageNoiseLevel) calVoltageNoiseLevel;
@property (Td,R,V_calVoltageSNR) calVoltageSNR;
@property (Td,R,V_calCurrentSignalLevel) calCurrentSignalLevel;
@property (Td,R,V_calCurrentNoiseLevel) calCurrentNoiseLevel;
@property (Td,R,V_calCurrentSNR) calCurrentSNR;
@property (Td,R,V_calVoltageAmplitude) calVoltageAmplitude;
@property (Td,R,V_calCurrentAmplitude) calCurrentAmplitude;
@property (Td,R,V_goertzelImpedance) goertzelImpedance;
@property (Td,R,V_goertzelPhase) goertzelPhase;
@property (Td,R,V_compensatedImpedance) compensatedImpedance;
@property (Td,R,V_compensatedPhase) compensatedPhase;
@property (Td,R,V_resistanceInOhms) resistanceInOhms;
@property (Td,R,V_capacitanceInNanoF) capacitanceInNanoF;
@property (Td,R,V_clippingScore) clippingScore;
@property (Td,R,V_measurementVoltageSignalLevel) measurementVoltageSignalLevel;
@property (Td,R,V_measurementVoltageNoiseLevel) measurementVoltageNoiseLevel;
@property (Td,R,V_measurementVoltageSNR) measurementVoltageSNR;
@property (Td,R,V_measurementCurrentSignalLevel) measurementCurrentSignalLevel;
@property (Td,R,V_measurementCurrentNoiseLevel) measurementCurrentNoiseLevel;
@property (Td,R,V_measurementCurrentSNR) measurementCurrentSNR;
@property (Td,R,V_measurementCondetSNR) measurementCondetSNR;
@property (Td,R,V_measurementVoltageAmplitude) measurementVoltageAmplitude;
@property (Td,R,V_measurementCurrentAmplitude) measurementCurrentAmplitude;
@property (Td,R,V_measurementVoltagePhase) measurementVoltagePhase;
@property (Td,R,V_measurementCurrentPhase) measurementCurrentPhase;
@property (Td,R,V_measurementLoadImpedanceMagnitude) measurementLoadImpedanceMagnitude;
@property (Td,R,V_measurementLoadImpedancePhase) measurementLoadImpedancePhase;
@property (TB,R,V_wetTooLong) wetTooLong;
@property (Ti,R,V_halogenResult) halogenResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenMeasurementDispatchQueue) halogenMeasurementDispatchQueue;
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenTtrDispatchQueue) halogenTtrDispatchQueue;
@property (T@"NSObject<OS_dispatch_source>",N,V_timer) timer;
@property (TB,N,V_attachDelayTimerRunning) attachDelayTimerRunning;
@property (TQ,N,V_wetPollingIntervalNs) wetPollingIntervalNs;
@property (TQ,N,V_dryPollingIntervalNs) dryPollingIntervalNs;
@property (TQ,N,V_ldcmArbiterRetryNs) ldcmArbiterRetryNs;
@property (TQ,N,V_ldcmStartMeasurementsDelayNs) ldcmStartMeasurementsDelayNs;
@property (TQ,N,V_ldcmStartMeasurementsRetryNs) ldcmStartMeasurementsRetryNs;
@property (TQ,N,V_minDryReadings) minDryReadings;
@property (TQ,N,V_dryCnt) dryCnt;
@property (TQ,N,V_firstDryTimestamp) firstDryTimestamp;
@property (TB,N,V_isWet) isWet;
@property (TB,N,V_wasTapToRadarShown) wasTapToRadarShown;
@property (TB,N,V_isTapToRadarPending) isTapToRadarPending;
@property (TB,N,V_isReceptacleEmpty) isReceptacleEmpty;
@property (TQ,N,V_wetDryTransitionTimestamp) wetDryTransitionTimestamp;
@property (TB,N,V_isTimestampValid) isTimestampValid;
@property (T@"NSCondition",N,V_cond) cond;
@property (TB,N,V_isMeasurementEnabled) isMeasurementEnabled;
@property (TB,N,V_isMeasurementActive) isMeasurementActive;
@property (T@"HalogenMeasurement",N,V_halogenMeasurement) halogenMeasurement;
@property (TI,N,V_service) service;
@property (Ti,N,V_portID) portID;
@property (T@"NSData",N,V_eventBasedPDigitalID) eventBasedPDigitalID;
@property (TQ,N,V_eventBasedDigitalID) eventBasedDigitalID;
@property (Ti,N,V_eventBasedOrientation) eventBasedOrientation;
@property (T@"NSData",N,V_connectedAccessoryPDigitalID) connectedAccessoryPDigitalID;
@property (TQ,N,V_connectedAccessoryDigitalID) connectedAccessoryDigitalID;
@property (Ti,N,V_connectedAccessoryOrientation) connectedAccessoryOrientation;
@property (Ti,N,V_pinID) pinID;
@property (TB,N,V_didNotify) didNotify;
@property (TB,N,V_didConfidentNotify) didConfidentNotify;
@property (TB,N,V_didHighConfidentNotify) didHighConfidentNotify;
@property (TB,N,V_didWetDuration) didWetDuration;
@property (TB,N,V_accessoryConnectedWhileWet) accessoryConnectedWhileWet;
@property (TQ,N,V_wetAccessoryAttachTimestamp) wetAccessoryAttachTimestamp;
@property (TB,N,V_didWetTooLong) didWetTooLong;
@property (TB,N,V_isHeadsetConnected) isHeadsetConnected;
@property (TB,N,V_isDebugAccessoryConnected) isDebugAccessoryConnected;
@property (TB,N,V_isBlacklistedAccessoryConnected) isBlacklistedAccessoryConnected;
@property (TB,N,V_justDetached) justDetached;
@property (TB,N,V_justAttachedCase) justAttachedCase;
@property (TB,N,V_isPowerAssertionHeld) isPowerAssertionHeld;
@property (TI,N,V_sleepAssertionID) sleepAssertionID;
@property (TB,N,V_isPowerAssertionHeld) isPowerAssertionHeld;
@property (TB,N,V_isMeasurementActive) isMeasurementActive;
@property (TB,N,V_isWet) isWet;
@property (TB,N,V_isInternalBuild) isInternalBuild;
@property (TB,N,V_isReceptacleEmpty) isReceptacleEmpty;
@property (TB,N,V_newAccArrived) newAccArrived;
@property (TB,N,V_userNotified) userNotified;
@property (TB,N,V_measureSBU) measureSBU;
@property (TB,N,V_wetTooLongRecorded) wetTooLongRecorded;
@property (TB,N,V_mitigationsEnabled) mitigationsEnabled;
@property (TB,N,V_mitigationsOverrideEnabled) mitigationsOverrideEnabled;
@property (TB,N,V_fakeWetMeasurements) fakeWetMeasurements;
@property (TB,N,V_measurementsEnabled) measurementsEnabled;
@property (TB,N,V_selfTestFailed) selfTestFailed;
@property (TB,N,V_refMeasurementFailed) refMeasurementFailed;
@property (TB,N,V_sbuBootArgSet) sbuBootArgSet;
@property (TB,N,V_enableMitigationsBootArgSet) enableMitigationsBootArgSet;
@property (TB,N,V_skipTTRBootArgSet) skipTTRBootArgSet;
@property (TB,N,V_didReportDisabledAnalytic) didReportDisabledAnalytic;
@property (TB,N,V_initialAlertShown) initialAlertShown;
@property (TB,N,V_followupAlertShown) followupAlertShown;
@property (TI,N,V_drySinceWetCount) drySinceWetCount;
@property (TI,N,V_selfTestFailureCount) selfTestFailureCount;
@property (TI,N,V_selfTestPassCount) selfTestPassCount;
@property (TI,N,V_referenceMeasurementFailureCount) referenceMeasurementFailureCount;
@property (TI,N,V_referenceMeasurementPassCount) referenceMeasurementPassCount;
@property (TQ,N,V_lastUserNotificationTimeNS) lastUserNotificationTimeNS;
@property (T^v,N,V_FBSOpenApplicationOptionKeyPromptUnlockDevice) FBSOpenApplicationOptionKeyPromptUnlockDevice;
@property (T@"NSObject<OS_dispatch_source>",N,V_timerSelfTest) timerSelfTest;
@property (T@"NSObject<OS_dispatch_source>",N,V_timerReferenceMeasurement) timerReferenceMeasurement;
@property (T@"NSObject<OS_dispatch_source>",N,V_timerPortStateCheck) timerPortStateCheck;
@property (T@"NSMutableDictionary",N,V_ldcmErrorCountDict) ldcmErrorCountDict;
@property (T@"NSLock",V_defaultsRWLock) defaultsRWLock;
@property (TI,N,V_sleepAssertionID) sleepAssertionID;
@property (T@"NSCondition",N,V_condition) condition;
@property (T^{__CFUserNotification=},N,V_notification) notification;
@property (T{?=dddd},N,V_wetMeasurementInfo) wetMeasurementInfo;
@property (Ti,N,V_analyticsDebugEvent) analyticsDebugEvent;
@property (T{mach_timebase_info=II},N,V_timeBase) timeBase;
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenTypeCUserPromptDispatchQueue) halogenTypeCUserPromptDispatchQueue;
@property (Ti,N,V_lastMeasurementResult) lastMeasurementResult;
@property (Ti,N,V_lastMeasurementStatus) lastMeasurementStatus;
@property (T@"HalogenTypeC",N,V_typeC) typeC;
@property (T@"NSObject<OS_dispatch_queue>",N,V_halogenTypeCDispatchQueue) halogenTypeCDispatchQueue;
@property (T@"NSObject<OS_dispatch_source>",N,V_timer) timer;
@property (TQ,N,V_wetPollingIntervalNs) wetPollingIntervalNs;
@property (TQ,N,V_dryPollingIntervalNs) dryPollingIntervalNs;
@property (TI,V_version) version;
@property (TB,V_isHealthy) isHealthy;
@property (TQ,V_leakagePassedCount) leakagePassedCount;
@property (TQ,V_dryCount) dryCount;
@property (TQ,V_wetCount) wetCount;
@property (TQ,V_overVoltageCount) overVoltageCount;
@property (TQ,V_outOfProfileCount) outOfProfileCount;
@property (TQ,V_lastSeenTimestamp) lastSeenTimestamp;
@property (TQ,V_rsvd0) rsvd0;
@property (TQ,V_rsvd1) rsvd1;
@property (TQ,V_rsvd2) rsvd2;
@property (TQ,V_rsvd3) rsvd3;
@property (TQ,V_overVoltageTimestamp) overVoltageTimestamp;
@property (TI,R,N,V_service) service;
@property (TI,R,N,V_connection) connection;
@property (T@"NSMutableDictionary",&,N,V_endpointMap) endpointMap;
@property (TQ,N,V_pmNotificationHandle) pmNotificationHandle;
@property (T^{IONotificationPort=},N,V_notificationPort) notificationPort;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_notificationQueue) notificationQueue;
@property (TI,N,V_discoveryIterator) discoveryIterator;
@property (TI,N,V_terminationIterator) terminationIterator;
@property (Ti,N,V_bootToken) bootToken;
@property (Ti,N,V_displayNotifyToken) displayNotifyToken;
@property (TB,N,V_bootComplete) bootComplete;
@property (TB,N,V_displayEnabled) displayEnabled;
@property (TB,N,V_pmUserActive) pmUserActive;
@property (TB,N,V_userActive) userActive;
@property (TB,N,V_userPresent) userPresent;
@property (TQ,V_minVhiDurationSec) minVhiDurationSec;
@property (TQ,V_maxVhiDurationSec) maxVhiDurationSec;
@property (TQ,V_maxUpFluctuationMv) maxUpFluctuationMv;
@property (Ti,V_userBehaviorMask) userBehaviorMask;
@property (Ti,V_fdpBehaviorMask) fdpBehaviorMask;
@property (TQ,V_numEisHalogenSamples) numEisHalogenSamples;
@property (TQ,V_wetPollingIntervalSec) wetPollingIntervalSec;
@property (TQ,V_dryPollingIntervalSec) dryPollingIntervalSec;
@property (TQ,V_ldcmArbiterRetrySec) ldcmArbiterRetrySec;
@property (TQ,V_ldcmStartMeasurementsDelayMs) ldcmStartMeasurementsDelayMs;
@property (TQ,V_ldcmStartMeasurementsRetryMs) ldcmStartMeasurementsRetryMs;
@property (TQ,V_minDryReadings) minDryReadings;
@property (TQ,V_enableHalogenSnrTtr) enableHalogenSnrTtr;
@property (TQ,V_enableHalogenMitigationsAndUI) enableHalogenMitigationsAndUI;
@property (Td,V_wetTransitionCapacitanceThreshold) wetTransitionCapacitanceThreshold;
@property (Td,V_dryTransitionCapacitanceThreshold) dryTransitionCapacitanceThreshold;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_ldcmV4DispatchQueue) ldcmV4DispatchQueue;
@property (T@"LDCMNotificationUIManagerV4",&,N,V_notificationUIManager) notificationUIManager;
@property (TI,N,V_notification) notification;
@property (TI,N,V_ldcmFeatureConnect) ldcmFeatureConnect;
@property (TQ,N,V_measurementQueueMappedAddress) measurementQueueMappedAddress;
@property (TQ,N,V_measurementQueueMappedSize) measurementQueueMappedSize;
@property (TI,N,V_measurementQueueNotificationPort) measurementQueueNotificationPort;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_measurementQueueDispatchSource) measurementQueueDispatchSource;
@property (Ti,N,V_buildType) buildType;
@property (Ti,N,V_deviceClass) deviceClass;
@property (TC,N,V_previousLDCMPortStatus) previousLDCMPortStatus;
@property (TB,N,V_isReceptacleEmpty) isReceptacleEmpty;
@property (TB,N,V_mitigationsEnabled) mitigationsEnabled;
@property (TB,N,V_overrideEnabled) overrideEnabled;
@property (T@"NSString",N,V_measurementInfoOutputString) measurementInfoOutputString;
@property (TB,N,V_uiActive) uiActive;
@property (TB,N,V_waveformExtractionDisabled) waveformExtractionDisabled;
@property (TB,N,V_behaviorOverrideDisableMitigations) behaviorOverrideDisableMitigations;
@property (TB,N,V_behaviorOverrideDisableUI) behaviorOverrideDisableUI;
@property (TB,N,V_behaviorOverrideDisableIntrusiveUI) behaviorOverrideDisableIntrusiveUI;
@property (TB,N,V_behaviorOverrideForcePortWet) behaviorOverrideForcePortWet;
@property (Ti,N,V_currentMitigationsStatus) currentMitigationsStatus;
@property (T@"NSDate",N,V_portAttachedTime) portAttachedTime;
@property (TC,N,V_ovpErrorCount) ovpErrorCount;
@property (TB,N,V_ovpInterruptsDisabled) ovpInterruptsDisabled;
@property (Td,R,N,VldcmLoadImpMag) ldcmLoadImpMag;
@property (Td,R,N,VldcmLoadImpPhase) ldcmLoadImpPhase;
@property (Td,R,N,VldcmCalculatedRes) ldcmCalculatedRes;
@property (Td,R,N,VldcmCalculatedCap) ldcmCalculatedCap;
@property (Td,R,N,VldcmTIACurrentAmp) ldcmTIACurrentAmp;
@property (Td,R,N,VldcmVoltageAmp) ldcmVoltageAmp;
@property (Td,R,N,VldcmLeakageCurrentAmp) ldcmLeakageCurrentAmp;
@property (Td,R,N,VldcmMeasureTIASNR) ldcmMeasureTIASNR;
@property (Td,R,N,VldcmMeasureVoltageSNR) ldcmMeasureVoltageSNR;
@property (Td,R,N,VldcmCalTIAAmp) ldcmCalTIAAmp;
@property (Td,R,N,VldcmCalVoltageAmp) ldcmCalVoltageAmp;
@property (Td,R,N,VldcmCalTIASNR) ldcmCalTIASNR;
@property (Td,R,N,VldcmCalVoltageSNR) ldcmCalVoltageSNR;
@property (Td,R,N,VldcmTIAGainCorrection) ldcmTIAGainCorrection;
@property (Td,R,N,VldcmVoltageGainCorrection) ldcmVoltageGainCorrection;
@property (Td,R,N,VldcmPhaseComp) ldcmPhaseComp;
@property (TC,R,N,VldcmRREFGated) ldcmRREFGated;
@property (TC,R,N,VldcmPortStatus) ldcmPortStatus;
@property (TC,R,N,VldcmMitigationsStatus) ldcmMitigationsStatus;
@property (TC,R,N,VldcmFeatureStatus) ldcmFeatureStatus;
@property (TC,R,N,VldcmLowImp) ldcmLowImp;
@property (TC,R,N,VldcmCompletion) ldcmCompletion;
@property (TC,R,N,VldcmWet) ldcmWet;
@property (TC,R,N,VldcmMeasurePin) ldcmMeasurePin;
@property (TI,R,N,VldcmWetStateDuration) ldcmWetStateDuration;
@property (TC,R,N,VldcmWetStateTooLong) ldcmWetStateTooLong;
@property (TC,R,N,V_ldcmWetTooLongLDCMDisabled) ldcmWetTooLongLDCMDisabled;
@property (TC,R,N,VldcmIncompSNRAmpCnt) ldcmIncompSNRAmpCnt;
@property (TC,R,N,VldcmIncompOVPCnt) ldcmIncompOVPCnt;
@property (TC,R,N,VldcmIncompTimeoutCnt) ldcmIncompTimeoutCnt;
@property (TS,R,N,VldcmSuccessfulCnt) ldcmSuccessfulCnt;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_assetManagerQueue) assetManagerQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_timer) timer;
@property (Ti,N,V_lastProcessedAssetVersion) lastProcessedAssetVersion;
@property (TI,N,V_queryFrequencySec) queryFrequencySec;
@property (TI,N,V_queryFrequencyToleranceSec) queryFrequencyToleranceSec;
@property (TI,N,V_retryQueryFrequencySec) retryQueryFrequencySec;
@property (TI,N,V_retryQueryFrequencyToleranceSec) retryQueryFrequencyToleranceSec;
@property (T@"<LDCMMobileAssetManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"IOPortLDCMManagerV4",W,N,V_ldcmManager) ldcmManager;
@property (T{?=BdB^{__CFUserNotification}^{__CFRunLoopSource}^{__CFRunLoop}@},N,V_liquidNotificationContext) liquidNotificationContext;
```

## Strings (915)

```
%s skipping measurement just after detach.\n
%s Measurement Halogen Status: %d. \n
%s Measurement Result: %@ \n
HalogenMeasurement:IOAccessoryManagerSelectEisPin failed to set the pin ret = 0x%x
HalogenTypeC:Could not start Halogen AudioUnit! Exiting ...
HalogenTypeC:ERROR: Could not set LiquidDetected. %d
LDCM - Invalid queue entry size: %u (expected %zu)
%s Invalid AggD key\n
(%d) EIS measurement #%d triggered abort due to sleep / failed arbitration / audio failure
HalogenMeasurement:Failed to alloc _pcmOutputData
%s unable to open service (%s)
HalogenCalcTypeC:Failed to alloc _tmp1DataBuff
LDCM - dryToWetTransition - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
LDCM - Measurement queue mapped at 0x%llx, size: %llu bytes
  dryPollingIntervalSec = %lld \n
HalogenMeasurement:dispatch_queue_create() failed
%s unable to read registry entry id (%s)
%s Failed to download catalog (%ld)
HalogenCalcTypeC:Invalid signalFrequency provided. (signalFrequency: %f)
LDCM - Mitigations no longer active.
  ldcmStartMeasurementsRetryMs = %lld \n
  minDryReadings = %lld \n
(%d) Event: Vlo, VoltageState: %d -> %d, gPlug: %d
HalogenLdcmCalc:Failed to alloc _tmp1DataBuff
%s boot completed notifying %lu endpoints
handle battery state update: isExtChg=%u, (delay) timer not running, don't perform measurement, key %@, halogenWrapper %@
LDCM - selfTestFailure - TIACurrentAmp: %f, VoltageAmp: %f, LeakageCurrentAmp: %f
Too many alerts shown, skipping
HalogenTypeC:Could not initialize HalogenAudio.
HalogenTypeC:HalogenTypeC Started!
HalogenTypeC:Mitigations Enabled: Turning off Type-C Port.
%s IOAccessoryHandleDetach entry\n
SelfTest passed, _selfTestPassCount:%d
%s SelfTest failed. Consecutive Failures Count: %d Next SelfTest in:%llu seconds.\n
LDCM - dryToWetTransition!!!
LDCM - dryToWetTransitionPortNotEmpty!!!
handle battery state update: isExtChg=%u, stop (delay) timer and perform measurement, key %@, halogenWrapper %@
%s Receptacle empty, skip checking port state
HalogenAudio:AudioUnitInitialize() failed (status = 0x%x)
LDCM UI Emergency Override!!!\n
LDCM - WARNING: Waveform data size mismatch! Size returned: %zu
LDCM - ovpError!!!
Reference measurement passed, _referenceMeasurementPassCount:%d isRefMeasurmentInFailedState:%d:\n
LDCM - LDCM Discovery disabled? default setting: %d
HalogenTypeC:_connectToAccessoryManager() failed for port %d
LDCM - Measurement Data - wetStateDuration: %d, wetStateTooLong: %d, wetTooLongLDCMDisabled: %d
%s handleEisMeasurement entry\n
HalogenMeasurement:CFURLCreateFromFileSystemRepresentation() returned NULL.
%s service has unexpected type
HalogenAudio:AudioUnitStop() failed (status = 0x%x)
LDCM UI Dismiss!!!\n
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_EnableIO/1 (status = 0x%x)
HalogenTypeC:_allocBuffers() failed
HalogenTypeC:Exiting function with HalogenReturnStatus: %u
LDCM - Failed to setup measurement data queue: 0x%x
[eval] <%{public}@> : emptyFail %d, accyFail %d
Mitagations overridden. Enabling port.
%d No analytics event generated.\n
%s default response
%s LDCM Asset timer fired, querying metadata
LDCM - wetToDryTransition - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
%s LDCM - Error in seeking to end of file. %@\n
(%d) halogen measurement = [%.13f, %.13f, %.13f, %.13f, %.13f, %.13f, %.13f, %.13f, %.13f, %.13f]
%s Could not disable mitigations.\n
%s user active changed %d->%d notifying %lu endpoints
%s Initializing LDCM Asset Manager
%s Query had no results
LDCM - Dry empty port with active override in measurement - clearing override
Nothing to write to csv file.\n
%s Unable to create file at '%@'
%s LDCM measurements currently disabled.\n
Dismissing wet prompt
HalogenMeasurement:render failed osstatus=0x%x
LDCM - Not showing UI (buildtype: %d override: %d userOverride: %d)
LDCM - Error retrieving cached waveform: 0x%x
%s Failed to create HalogenMeasurementDispatchQueue\n
(%d) IOAccessoryHandleAttach() Stop empty receptacle measurements for previous attachment
%s:\n%@
(%d) EIS measurement wet interval = %lld seconds, dryTime = %lld seconds
%s Receptacle not empty, will try again in 10 minutes.\n
HalogenMeasurement:Failed to alloc _voltageData
HalogenTypeC:%s pin:%d _pinToMeasure:%d measurementType:%d
LDCM - referenceMeasurementFailure - WetStateDuration: %d, WetStateTooLong: %d
LDCM - Override already enabled, no action taken
(%d) halogen SNR = [precal: %.13f, %.13f cal: %.13f, %.13f measurement: %.13f, %.13f condet: %.13f]
%s Failed to create HalogenTypeCUserPromptDispatchQueue\n
%s Reference measurement failed. halogenStatus: %d\n
HalogenTypeC:CFURLCreateFromFileSystemRepresentation() returned NULL.
HalogenAudio:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_EnableIO/1 (status = 0x%x)
HalogenAudio:AudioUnitSetProperty() failed to set kAudioUnitProperty_StreamFormat/kAudioUnitScope_Output (status = 0x%x)
%s Failed to set up LDCM attach/detach interest notification\n
LDCM - WARNING: Mitigations failed!!!
LDCM - Setting waveform extraction: %d...
%s kIOPortFeatureLDCMMessageTypeMeasurementStatusChange (queued for analytics)\n
(!) Event: AggD key %{public}@ with value %llu
LDCM - TIACurrentSNR: %f, VoltageSNR: %f, CalTIASNR: %f, CalVoltageSNR: %f
LDCM - IncompOVPCnt: %d
LDCM - Skipping mitigations due to behavior override!
%s start measurement timer: %llu ms\n
%s failed to release power assertion. Error 0x%x\n
%s alternate response
HalogenLdcmCalc:doLiquidDetection capacitanceThreshholdNanoF = %f, isReceptacleWet: %d
HalogenMeasurement:Skipping arbitration.
LDCM - Setting Override in Port Manager: %d!!!
HalogenMeasurement:Arbiter failed to grant access to Halogen
HalogenMeasurement:AudioUnitStart() failed (status = 0x%x)
%s unable to initialize endpoint
HalogenCalcTypeC:Invalid sampleRate provided. (sampleRate: %llu)
HalogenCalcTypeC:_allocBuffers() failed
HalogenCalcTypeC:Failed to alloc _tmp2DataBuff
HalogenCalcTypeC:Failed to alloc _tmp3DataBuff
HalogenTypeC:_doLDCMMeasurement failed (HalogenMeasurementStatus = 0x%x)
LDCM - Skipping waveform storage due to data size mismatch!!! Size returned: %zu
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioUnitProperty_ShouldAllocateBuffer (status = 0x%x)
%s user present changed %d->%d notifying %lu endpoints
%s Failed to query metadata (%ld)
%s failed to create behavior dictionary from plist (%@)
LDCM Discovery is enabled.
%s IOServiceAddInterestNotification failed: %08x
%s Failed to create HalogenTypeC NSCondition\n
%s Skipping mitigations enableMitigations:%d
HalogenAudio:initAudioPath did not receive a valid halogenUnit.
LDCM UI Cancel!!!\n
LDCM - Waveform extraction default setting: %d
LDCM - wetToDryTransitionPortNotEmpty!!!
(%d) Suppress TapToRadar as it was already shown on this insertion
%s Port not wet, skipping alert
HalogenMeasurement:_createSleepWakeNotifier() failed for port %d
HalogenTypeC:abort measurement... system going to sleep
LDCM - referenceMeasurementFailure!!!
LDCM - Notification message too large: need %u bytes, have %zu
Logging aggd key: %{public}@ value: %f
HalogenAudio:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_EnableIO/0 (status = 0x%x)
LDCM - Mitigations triggered... Waiting for attach and/or mitigations success.
LDCM - wetToDryTransition - WetStateDuration: %d, WetStateTooLong: %d
HalogenMeasurement:Waiting for kHalogenPowerStateAwake
HalogenTypeC:ERROR: Could not set EnableMitigations. %d
LDCM - selfTestFailure - CalTIAAmp: %f, CalVoltageAmp: %f, CalTIASNR: %f, CalVoltageSNR: %f
%s kIOPort_Message_ConnectionStateChange attach\n
HalogenLdcmCalc:vDSP_create_fftsetupD() failed
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_SetRenderCallback (status = 0x%x)
HalogenMeasurement:Measurement did not complete... cannot save WAV file
HalogenMeasurement:AudioFileCreateWithURL() returned ostatus=0x%x
%s error %s
HalogenTypeC:_createSleepWakeNotifier() failed for port %d
HalogenTypeC:Failed to alloc _voltageData
HalogenTypeC:Timeout!
%s Failed to create ldcmV4DispatchQueue\n
%s LDCM - Error in closing file. %@\n
%s failed to allocate HalogenMeasurement\n
UI Emergency Override!!!\n
Failed to instantiate HalogenTypeC. Exiting... \n
HalogenTypeC:dispatch_queue_create() failed
HalogenTypeC:Invalid pin to measure: %d. Exiting measurement...
%s err: %s
LDCM - selfTestFailure!!!
LDCM - Skipping waveform storage due to waveform extraction default setting.
LDCM - Measurement data queue setup complete
%s kIOPortFeatureLDCMMessageTypeLiquidDetectedChange (handled in kernel)\n
  wetPollingIntervalSec = %lld \n
%s Failed to get IOPort kernel service\n
(%d) dryCnt = %llu
HalogenLdcmCalc:Failed to alloc _tmp2DataBuff
HalogenMeasurement:_eisPinToken2 != _eisPinToken1+1 due to change on lightning port. isTimeout=%d
%s asset version %d not compatible, skipping
HalogenTypeC:Failed to create NSCondition: powerStateCond
LDCM - Failed to create measurement from queued data
Showing wet prompt
HalogenMeasurement:Failed to alloc _currentData
HalogenMeasurement:IOAccessoryManagerSelectEisPin() failed (ret = 0x%x)
%s Attempting to process plist found in %@
HalogenTypeC:This device does not support self-test. Exiting...
HalogenTypeC:IOAccessoryManagerSetLDCM() failed (ret = 0x%x)
LDCM - referenceMeasurementFailure - MeasureTIASNR: %f, MeasureVoltageSNR: %f, LeakageCurrentAmp: %f
(%d) ~~~ [%012llx] LDCM consecutiveVoltageNotDetected %d / rearm %d
%s halogen power assertion already in the correct state: %d.\n
%s Failed to create HalogenTypeC Timer\n
%s unexpected response
  ldcmArbiterRetrySec = %lld \n
[fluctuation] diffAdcMv %d
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioUnitProperty_StreamFormat/kAudioUnitScope_Output (status = 0x%x)
%s Failed to initialize IOPortLDCMManagerV4 super\n
LDCM - Dry port with Active mitigations in measurement - clearing mitigations
LDCM - Request to disable OVP interrupts
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioUnitProperty_StreamFormat/kAudioUnitScope_Input (status = 0x%x)
%s requesting purge of asset version %d
HalogenTypeC:IORegisterForSystemPower() failed
LDCM - Failed to map measurement queue memory: 0x%x
[trim] <%{public}s> : %llu
(%d) Event: Attach, CurrentVoltageState = %d, gPlug = %d
(%d) dryCnt=%llu didn't reach the minimum threshold of %llu before reading wet again
LDCM - Failed to read LDCM architecture version!!!
LDCM - Mitigations successful. Showing UI
LDCM - Feature Status: %x, Mitigations Status: %d [%s], Mitigations Framework State: %d, Override Framework State: %d, Wet Declared %d, Wet Measured: %d, Wet State Duration: %d, Receptacle Empty: %d, RREF Gated: %d
(%d) IOAccessoryHandleAttach() Pause empty receptacle measurements, attached accessory has no free pins
HalogenMeasurement:Timeout!
LDCM - wetToDryTransition - TIACurrentAmp: %f, VoltageAmp: %f, LeakageCurrentAmp: %f
LDCM - selfTestFailure - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
LDCM - Setting up measurement data queue...
LDCM - Processed %u queued measurement(s)
%s Could not enable mitigations.\n
HalogenMeasurement:AudioComponentFindNext() failed to find kAudioUnitSubType_LDCMIO
HalogenTypeC:Failed to alloc _pcmOutputData
HalogenTypeC:%d:Measurement status:%llu
LDCM - IncompSNRAmpCnt: %d, TIACurrentAmp: %f, VoltageAmp: %f, CalTIAAmp: %f, CalVoltageAmp: %f
LDCM - selfTestFailure - TIAGainCorrection: %f, VoltageGainCorrection: %f, PhaseComp: %f
%s behavior overrides - mitigations: %d ui: %d
LDCM - Processed measurement: %@ (reason: %s, timestamp: %llu, waveform: %s)
(%d) ~~~ [%012llx] LDCM consecutiveVoltageDetected %d / rearm %d
%s Reference Measurement failed. Consecutive Failures Count: %d Next Reference Measurement in:%llu seconds.\n
%s Failed to create HalogenTtrDispatchQueue\n
%s HalogenResult: %d\n
%s Measurement type is neither SelfTest or Reference. Type:%d\n
HalogenLdcmCalc:Failed to alloc _tmp3DataBuff
HalogenMeasurement:abort measurement... system going to sleep
%s removing endpoint
%s found asset state:%ld version:%d
HalogenTypeC:IOAccessoryManagerSetLDCM failed with: 0x%x
LDCM - Measurement Data - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
LDCM - ldcmDisabled!!!
%s Starting measurement of occupied port\n
%s LDCM - Duration of port attached: %ld\n
%d Analytics event for %@:%@\n
HalogenLdcmCalc:_allocBuffers() failed
HalogenCalcTypeC:vDSP_create_fftsetupD() failed
HalogenTypeC:Failed to alloc _pcmInputData
HalogenTypeC:Not an internal build, desired measurement pin SBU. Abort measurement.
%s Failed to create NSCondition\n
[health %d] <%{public}s> : %llu, isHealthy %d, leakagePassedCount %llu, dryCount %llu, wetCount %llu
HalogenMeasurement:IORegisterForSystemPower() failed
HalogenMeasurement:abort measurement... system is not yet awake
HalogenMeasurement:recordCallback() insufficient space in pcmInputData buffer to render %d frames.  bufsize = %d idx=%d
HalogenTypeC:Could not find a valid HalogenAudio instance.
LDCM - ldcmDisabled - FeatureStatus: %d
LDCM - Failed to set notification port: 0x%x
(%d) Event: Vhi, VoltageState: %d -> %d, gPlug: %d, VhiCount: %d, DigitalID: %02x %02x %02x %02x %02x %02x, CumulativeLifetimeExceeded: %d
(%d) Detach: Empty Receptacle State. Keep measuring.
%s Failed to download asset (%ld)
HalogenTypeC:Product Type string is NULL - No support for SelfTest
LDCM - Periodic measurements now handled in kernel space
LDCM - dryToWetTransition - TIACurrentAmp: %f, VoltageAmp: %f, LeakageCurrentAmp: %f
LDCM - referenceMeasurementFailure - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
LDCM - Setting ForcePortWet in kernel: %d
%s SelfTest failed. halogenStatus: %d\n
HalogenAudio:AudioComponentFindNext() failed to find kAudioUnitSubType_LDCMIO
HalogenAudio:AudioUnitSetProperty() failed to set kAudioUnitProperty_ShouldAllocateBuffer (status = 0x%x)
LDCM - wetToDryTransition!!!
HalogenTypeC:abort measurement... system is not yet awake
%@
(!) Event: AggD key %{public}@ increment
HalogenMeasurement:Could not find IOAccessoryManager service for port=%d
HalogenMeasurement:Failed to open IOAccessoryManager manager (ret = 0x%x)
LDCM - Successfully enabled waveform extraction.
LDCM - Failed to consume mach message: 0x%x
HalogenTypeC:Failed to alloc _currentData
LDCM - Analytics bitfields - _previousLDCMPortStatus %d, ldcmPortStatus %d, ldcmMeasurePin %d, ldcmCompletion %d, ldcmLowImp %d
LDCM - Setting Mitigations in Port Manager: %d!!!
%s Could not locate boot-args.\n
%s Bad Measurement recorded. HalogenResult: %d\n
LDCM - dryToWetTransition - CalTIAAmp: %f, CalVoltageAmp: %f, CalTIASNR: %f, CalVoltageSNR: %f
LDCM - Cleaning up measurement data queue...
(%d) Event: GoldbondDisabledMbHeadset, CurrentVoltageState = %d, gPlug = %d
HalogenMeasurement:Failed to alloc _pcmInputData
HalogenMeasurement:IOAccessoryManagerSelectEisPin() device busy (ret = 0x%x)
%s: Setting asset path for LDCM wet icon:%@
LDCM - referenceMeasurementFailure - TIACurrentAmp: %f, VoltageAmp: %f, LeakageCurrentAmp: %f
  ldcmStartMeasurementsDelayMs = %lld \n
%s stop measurement timer.\n
%s Performing SelfTest.\n
%smReference measurement failed. measurementInfo.resistanceInOhms:%f, measurementInfo.capacitanceInNanoF: %f
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_SetInputCallback (status = 0x%x)
%s purge of asset version %d failed (%ld)
%s Error while filing radar. %@\n
LDCM - Clearing stale override on new mitigation trigger
LDCM - badMeasurement!!!
%s Failed to create halogenWrapper\n
%s: digitalID(0x%08llx) indicates no charging or Not DisableStartDelay behavior, perform measurement now.\n
Failed to override mitigations.
HalogenMeasurement:HalogenMeasurement Started!
HalogenMeasurement:failed to allocate halogen ResourceArbiterClient
%s Failed to set up LDCM interrupts interest notification\n
LDCM - wetOnConnect!!!
LDCM - UI already active, not showing UI
LDCM - Measurement data queue cleanup complete
%s IOAccessoryHandleAttach entry\n
%s: digitalID(0x%08llx), start measurement after %llums.\n
%s failed to acquire power assertion. Error 0x%x\n
%s Port has been wet for a while, reminding user
(%d) Restarting Measurements
LDCM - Failed to copy data!!! Error: %d
(%d) wet duration interval = %lld seconds
%s Failed to create HalogenTypeCDispatchQueue\n
HalogenMeasurement:_allocBuffers() failed
HalogenMeasurement:AudioComponentInstanceNew() failed (status = 0x%x) 
%s bestInstalledAssetVersion:%d bestNotInstalledAssetVersion:%d _lastProcessedAssetVersion:%d
HalogenAudio:AudioUnitStart() failed (status = 0x%x)
LDCM - Waveform extraction not enabled due to build type.
LDCM - wetToDryTransition - MeasureTIASNR: %f, MeasureVoltageSNR: %f, LeakageCurrentAmp: %f
LDCM - impedanceTooLow!!!
LDCM - WetReplug
Halogen Parameters: \n
HalogenMeasurement:AudioUnitInitialize() failed (status = 0x%x)
%s adding endpoint
HalogenTypeC:Liquid Detected Set:%d.
HalogenAudio:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_SetInputCallback (status = 0x%x)
LDCM UI Notification Duration: %ld\n
(%d) Attach: Start Measurements
%s IOAccessoryManagerCopyDeviceInfo returned %x\n
HalogenCalcTypeC:Invalid sample value provided. (samples: %d)
HalogenTypeC:AudioFileCreateWithURL() returned ostatus=0x%x
LDCM - wetOnDisconnect!!!
LDCM - IncompTimeoutCnt: %d
LDCM - referenceMeasurementFailure - CalTIAAmp: %f, CalVoltageAmp: %f, CalTIASNR: %f, CalVoltageSNR: %f
Incrementing aggd key: %{public}@
(%d) Dynamic free pins have been consumed. Cannot take Halogen LDCM measurment freePinMask = 0x%llx
(%d) IOAccessoryManagerGetFreePinMask() failed so abort measurement
%s service already added
HalogenAudio:Uninitializing AudioUnit instance.
LDCM - dryToWetTransition - MeasureTIASNR: %f, MeasureVoltageSNR: %f, LeakageCurrentAmp: %f
%s kIOPort_Message_ConnectionStateChange detach \n
handle battery state update: isExtChg=%u->%u, enableHalogenMitigationsAndUI %llu
LDCM - Measurement Data - TIAGainCorrection: %f, VoltageGainCorrection: %f, PhaseComp: %f
%s Failed to create Halogen Timer\n
(%d) EIS measurement #%d on %d (%{public}s) returned %d (%{public}@)
HalogenMeasurement:Failed to create NSCondition: powerStateCond
LDCM - No kernel connection for queue setup
LDCM - Data size mismatch!!! Size returned: %zu
LDCM - wetToDryTransition - CalTIAAmp: %f, CalVoltageAmp: %f, CalTIASNR: %f, CalVoltageSNR: %f
HalogenAudio:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_SetRenderCallback (status = 0x%x)
LDCM - Popping up a wet notification!!!
HalogenTypeC:Measurement did not complete... cannot save WAV file
(%d) Empty Receptacle Dry State. Disable measurements
HalogenMeasurement:AudioUnitSetProperty() failed to set kAudioOutputUnitProperty_EnableIO/0 (status = 0x%x)
LDCM - WARNING: Failed to copy waveform! Error: %d
LDCM - Measurement Data - MeasureTIASNR: %f, MeasureVoltageSNR: %f, CalTIASNR: %f, CalVoltageSNR: %f
LDCM - dryToWetTransition - TIAGainCorrection: %f, VoltageGainCorrection: %f, PhaseComp: %f
LDCM - referenceMeasurementFailure - TIAGainCorrection: %f, VoltageGainCorrection: %f, PhaseComp: %f
UI Dismiss!!!\n
HalogenMeasurement:_connectToAccessoryManager() failed for port %d
HalogenMeasurement:_eisPinToken2 != eisPinTokenFinal due to change on lightning port. isTimeout=%d
%s purge of asset version %d succeeded
HalogenTypeC:Failed to open IOAccessoryManager manager (ret = 0x%x)
HalogenTypeC:recordCallback() insufficient space in pcmInputData buffer to render %d frames.  bufsize = %d idx=%d
%s performEisMeasurement entry wrapper = %p\n
%s skipping measurement just after attach of case.\n
HalogenTypeC:Waiting for kHalogenPowerStateAwake
HalogenTypeC:Measurement Status Error:%llu Skipping LDCM calculations.
LDCM - Showing UI, if applicable
LDCM - Failed to get measurement queue memory type: 0x%x
(%d) EIS measurement dry interval = %lld seconds
%s Audio issue detected. HalogenMeasurementStatus: %d\n
LDCM - ldcmPreempted!!!
LDCM - selfTestFailure - WetStateDuration: %d, WetStateTooLong: %d
LDCM - Mapped address is NULL
%s kIOPortFeatureLDCMMessageTypeMitigationsStatusChange: %d\n
(%d) Event: PH update, failed = %d, success = %d
%s Performing Reference Measurement.\n
HalogenMeasurement:AudioUnit is not initialized
HalogenTypeC:Could not find IOAccessoryManager service for port=%d
HalogenTypeC:render failed osstatus=0x%x
HalogenTypeC:Setting LDCM back to Idle with HalogenReturnStatus: %u
%s Error in creating directory. %@\n
LDCM - Failed to allocate notification port
(%d) Event: Detach, CurrentVoltageState = %d, gPlug = %d
LDCM - impedanceTooLow - loadImpMag: %f, loadImpPhase: %f, calculatedRes: %f, calculatedCap: %f
>>> showing initial accy health dictionary
halogenMeasurementCleanup() TIMEOUT... cleanup anyway
%s _measurementEnabled:%d, _selfTestFailed:%d, _refMeasurementFailed:%d\n
%s Failed to initialize analytcs event string.\n
LDCM - Data size mismatch!
HalogenAudio:AudioUnitSetProperty() failed to set kAudioUnitProperty_StreamFormat/kAudioUnitScope_Input (status = 0x%x)
%s Failed to open LDCM kernel service\n
(%d) ~~~ setDriverMitigationEnabled [%d] returned %d
%s No valid instance of HalogenTypeC\n
%s NULL service
%s downloaded asset version %d successfully
Starting LDCM Now
LDCM - Failed to enable waveform extraction!
LDCM - Beginning LDCM measurement. Reason: %d
LDCM - wetToDryTransition - TIAGainCorrection: %f, VoltageGainCorrection: %f, PhaseComp: %f
LDCM - selfTestFailure - MeasureTIASNR: %f, MeasureVoltageSNR: %f, LeakageCurrentAmp: %f
(%d) EIS measurement #%d on %d (%{public}s) returned %#x
LDCM - Failed to instantiate IOPortLDCMManagerV4!!!
HalogenAudio:AudioComponentInstanceNew() failed (status = 0x%x) 
LDCM - Hiding UI, if applicable
LDCM - Failed to create dispatch source for queue
LDCM - Unknown queue entry reason: %u, treating as periodic
(%d) wet too long = %lld seconds
%s IOServiceAddMatchingNotification falied: %08x
%s IOAccessoryLDCMPortManagerTypeC initialized.\n
%s Performing a measurement. \n
LDCM - IOPortLDCMManagerV4 successfully initialized!
[eval] <%012llx_%1d_%012llx> : emptyFail %d, accyFail %d
(%d) Event: Terminated
q24@?0@8@16
ADClientClearScalarKey
vlow
WETMSG_DIALOG_HEADER_LOCKSCREEN_LEGACY
Loopback
WETMSG_BUTTON_EMERGENCY_OVERRIDE
initialImpedance
calVoltageSNR -> %.13f\n
--distributionsWithPrefix
IOAccessoryIDBusSystemStates
LDCMForcePortWet
Triggered
ADClientPushValueForDistributionKey
NoIdleSleepAssertion
-[LDCMMobileAssetManager updateMetadata]
WETMSG_BUTTON_DISMISS
com.apple.ioaccessorymanager.ldcm.notification.wettoolong
precalCurrentNoiseLevel -> %.13f\n
measurementVoltageSignalLevel -> %.13f\n
badCalVoltageSNR
 DigitalID = [%02x %02x %02x %02x %02x %02x], ORIENT = %s, PH = %s, ACC_PWR = %s
IOAccessoryAggDCollectData
referenceMeasurementsFailureTimestamp
LDCMDisableIntrusiveUI
com.apple.ioaccessorymanager.ldcm.eis.capacitance.histogram
NONE
--data=0x110B0402
MitigationsStatus
Liquid detected in Lightning port.\n File a Radar?
reportEisMeasurementStateChange
chargerConnected
/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
clippingScore -> %.13f\n
com.apple.ioaccessorymanager.ldcm.eis.currentgaincorrection.outofrange
- If the exposure was limited to a certain part of the device, where was it?\n\n
commitPersistentAccyHealthDictionary
q
- What kind of liquid? (e.g. tap water, rain, sweat, soda, beer, etc.)\n\n
iPhone
R!
bm3
/tmp/halogen_ttr.wav
precalibrationSampleOffsetInFrames -> %d\n
connected accessory orientation -> %d\n
com.apple.ioaccessorymanager.ldcm.eis.phase.high
com.apple.ioaccessorymanager.ldcm.usbc.selfTestFailToPassDuration
com.apple.ioaccessorymanager.ldcm.usbc.dryToWetTransitionPortNotEmpty
badMeasurementCurrentSNR
com.apple.ioaccessorymanager.ldcm.usbc.ldcmDisabled
LIQUID DETECTION REPORT (detected via Halogen)\n\n
CurrentPhaseCompensation
typeC
LDCMWaveformExtractionDisabled
badCalCurrentAmp
.%02x%02x%02x%02x%02x%02x%d
WETMSG_DIALOG_HEADER_LOCKSCREEN
AssertType
IOAccessoryNotifyWet
/usr/local/bin/hpmtool
NonUI
-[IOAccessoryLDCMPortManagerTypeC _readLDCMBootArgs]
PreCalibrationBadSNR
1!
notificationUserAction
DeviceClass
accessoryUnplug
%@
,%@
com.apple.MobileAsset.IOAccessoryManager
HalogenTtrDispatchQueue
halogenMeasurementCleanupSafe
IOAccessoryOrientation
Liquid has been detected in the USB-C connector. Disconnect to allow the connector to dry.
LDCMAssetQueryFrequencyTolerance
LDCMBehavior.plist
LDCMAssetManagerQueue
1
v24@?0@\"NSDictionary\"8@\"NSError\"16
Time To Dry\n %02llu:%02llu:%02llu
ExternalConnected
com.apple.CoreAccessories.LDCMMitigationsOverrideNotification
-[IOAccessoryLDCMPortManagerTypeC _showWetPrompt]_block_invoke
com.apple.ioaccessorymanager.ldcm.usbc.WetReplug
%02x %02x %02x %02x %02x %02x
measurementCurrentSignalLevel -> %.13f\n
com.apple.ioaccessorymanager.halogen
com.apple.ioaccessorymanager.ldcm.usbc.ovpErrorPortNotEmpty
Voltage No longer Detected
- Time since exposure\n
tap-to-radar://new?ComponentName=LDCM&ComponentVersion=AutofilledBugs&ComponentID=750390&Classification=Other Bug&Reproducibility=Not Applicable&
ldcmMeasurementsDisabled
-[IOAccessorySystemStateEndpoint notifyUserPresent:]
reinsertion
com.apple.ioaccessorymanager.ldcm.usbc.badMeasurement
Voltage Detected
precalVoltageNoiseLevel -> %.13f\n
com.apple.ioaccessorymanager.ldcm.usbc.dryMeasurementPortNotEmpty
MitigationsEnabled
BRICK
histogramVoltage
DisablePeriodicMeasurements
-[LDCMMobileAssetManager init]
Interrupt
com.apple.ioaccessorymanager.ldcm.notification.suppress.phone
/var/logs/ldcm/halogenTypeC_ttr_temp.wav
-[LDCMMobileAssetManager downloadCatalog]_block_invoke_2
\n\nIf no:\n\n
com.apple.ioaccessorymanager.ldcm.usbc.wetTooLong
badMeasurementNegativeCap
com.apple.ioaccessorymanager.voltage.histogram.dp1
selfTestMeasurementsFailed
com.apple.ioaccessorymanager.voltage.cumulativetime
selfTestFailureTimestamp
Error fetching fileA attributes. File ordering could be out of order. Error:%@ File:%@
, %s(%s) = %.3fV
WETMSG_DIALOG_BODY_LOCKSCREEN_TYPEC_PASSIVE
iPad13,9
Inactive
badCalVoltageAmp
lastSeenTimestamp
measurementVoltageSNR -> %.13f\n
RequiresEisAfeArbiter
IOAccessoryInterestNotificationCallbackTypeC
WETMSG_DIALOG_BODY_LOCKSCREEN
com.apple.CoreAccessories.TestLDCMAnalytics
com.apple.ioaccessorymanager.ldcm.usbc.wetToDryTransition
currentGainCorrection -> %.13f\n
--scalarsWithPrefix
AssertName
iPhone11
If yes:\n\n
- What kind of exposure? (e.g. submersion, splash, droplet, sitting in puddle, using device with wet/sweaty hands, etc)\n\n
ACC1
Not Now
 
com.apple.ioaccessorymanager.ldcm.eis.error.suppress.accessory
retrievePersistentAccyHealthDictionary
Unkown measurement state\n\n
com.apple.ioaccessorymanager.ldcm.notification.badaccessorycount
com.apple.ioaccessorymanager.ldcm.notification.highconfidentcount
-[IOAccessorySystemStateEndpoint initWithService:]
-[LDCMMobileAssetManager processAsset:]
low
MeasurementBadSNR
-[IOAccessorySystemStateEndpoint notifyBootComplete]
BadAmplitudeMeasurement
com.apple.ioaccessorymanager.halogenTypeC
B
TimeStamp,%@\nMeasurementType,%@\nMeasurementPin,%@\nMeasurementResult,%@\nVolGainCorrection,%.12f\nCurGainCorrection,%.12f\nCurPhaseCompensation,%.12f\nVolSNR,%.12f\nCurSNR,%.12f\nVolAmplitude,%.12f\nCurAmplitudeMicroA,%.12f\nVolPhase,%.12
notificationDuration
com.apple.ioaccessorymanager.ldcm.usbc.DidNotifyUser
-[IOPortLDCMManagerV4 initWithParams:withNotificationPort:withServerRunloop:]
__powerBatteryMatch
Error fetching fileB attributes. File ordering could be out of order. Error:%@ File:%@
precalVoltageSignalLevel -> %.13f\n
LDCMDiscoveryDisabled
Has your iPad or charging cable been near liquid in the past 5 hours? \n\n
iPad13,10
Yes
ADClientSetValueForScalarKey
ConnectionActive
calVoltageNoiseLevel -> %.13f\n
com.apple.ioaccessorymanager.ldcm.eis.impedance.low
IOPort
(Undefined)
initialResistance
ADClientAddValueForScalarKey
ReleaseType
badMeasurementCurrentAmp
/System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
SBU
HalogenMeasurementDispatchQueue
voltageGainCorrection -> %.13f\n
HalogenTypeCDispatchQueue
-[HalogenTypeC _doLDCMMeasurement:isReceptacleEmpty:isReceptacleWet:withWetTransitionThreshold:withDryTransitionThreshold:measurementType:]
/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
IOService
Halogen Measurements:\n\n
Capacitance in nF -> %.13f\n
SNR failure while doing Liquid Detection.\n File a Radar?
com.apple.ioaccessorymanager.ldcm.usbc.selfTest
ProcessPublishedEndpoints
com.apple.IOAccessoryManagerFramework.WetNotification
Detach
-[IOPortLDCMManagerV4 generateLDCMCSVData]
ArchitectureVersion
 (%d) Event: %s, Vhi = %d, CumulativeTimeVhi = %d sec,
lightningDry
com.apple.ioaccessorymanager.ldcm.notification.confidentcount
com.apple.ioaccessorymanager.ldcm.eis.measurement.bad.snr
com.apple.accessoryd.plugin
rsvd2
-[HalogenWrapper init]
com.apple.CoreAccessories.LDCMSettingsDidChangeNotification
-[IOAccessorySystemStateMonitor notifyEndpointsBootComplete:]
off
accyHealthDict
com.apple.ioaccessorymanager.ldcm.eis.currentphasecompensation.outofrange
-[IOAccessoryLDCMPortManagerTypeC initWithParams:dryPollingIntervalNs:]
impedancePhase
At your own risk, you may override this now or later from Settings > Accessories > Re-Enable Port.
v24@?0Q8Q16
date,measurementReason,measurementEvent,ldcmPortStatus,ldcmMitigationsStatus,ldcmFeatureStatus,ldcmMeasurePin,ldcmCompletion,ldcmWet,ldcmLowImp,ldcmLoadImpMag,ldcmLoadImpPhase,ldcmCalculatedRes,ldcmCalculatedCap,ldcmTIACurrentAmp,ldcmVoltag
IOAccessoryHandleDetach
IOServiceFirstMatch
Unknown
Description=%@
com.apple.ioaccessorymanager.ldcm.eis.drytimeV2.histogram
connected accessory DigitalID -> 0x%012llx\n
com.apple.ioaccessorymanager.ldcm.eis.phase.histogram
com.apple.CoreAccessories.LDCMActiveMeasurementsDidChangeNotification
skipLDCMTTR
com.apple.ioaccessorymanager.ldcm.usbc.badMeasurementPortNotEmpty
Attachments=%@
hpmtool returned:\n%@
DN2
Ok
com.apple.ioaccessorymanager.ldcm.usbc.ovpError
ldcmMitigations
lockScreenLiquidDetection
internalMeasurementData
Liquid has been detected in the Lightning connector. Disconnect to allow the connector to dry. Charging now may damage your iPhone.
WETMSG_DIALOG_BODY_LOCKSCREEN_LEGACY
calibrationSampleOffsetInFrames -> %d\n
MeasureSBU
BadSNRMeasurement
event based orientation -> %d\n
-[IOAccessoryLDCMPortManagerTypeC _checkPortState]
iPad13,8
Error fetching fileA attritbutes. File ordering could be out of order. Error:%@ File:%@
Wet
LDCMV4DisableUI
wetDuration
com.apple.ioaccessorymanager.ldcm.usbc.PortAttachedDuration
%@,%@,%@,%.12d,%.12d,%.12d,%.12d,%.12d,%.12d,%.12d,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12f,%.12d,%.12d,%.12d,%.12d,%.12d\n
com.apple.ioaccessorymanager.ldcm.notification.suppress.accessory
precalCurrentSNR -> %.13f\n
com.apple.CoreAccessories.MitigationsDidChange
ERROR: Could not write calibration results to disc.
_holdPowerAssertion
-[IOAccessoryLDCMPortManagerTypeC _generateAlternateMeasurementAnalytics:measurementInfo:intervalSinceLastPass:]
com.apple.ioaccessorymanager.ldcm.usbc.referenceMeasurement
ProcessTerminatedEndpoints
Negative measurement capacitance recorded. capacitanceInNanoF:%.12f
Internal
BadSNRCalibration
Voltage Measurement
_retrieveDeviceInterfaceSerialNumber
SNR Failure\n\n
AssertLevel
com.apple.CoreAccessories.LDCMPreferences
v12@?0i8
resistance
PortType
IOPortLDCMFeatureInterestCallback
isHealthy
com.apple.ioaccessorymanager.ldcm.notification.count
com.apple.ioaccessorymanager.ldcm.eis.accessory.connection
com.apple.ioaccessorymanager.ldcm.eis.suppress.accessory
goertzelPhase -> %.13f\n
Goldbond Disable MB Headset
com.apple.ioaccessorymanager.voltage.count
-[LDCMMobileAssetManager updateMetadata]_block_invoke
-[IOPortLDCMManagerV4 processBehaviorDictionary:]
HalogenTypeCUserPromptDispatchQueue
NO
ADClientClearDistributionKey
/tmp/ioam_aggregatectl.log
badMeasurementVoltageAmp
com.apple.ioaccessorymanager.voltage.averagetime
calCurrentNoiseLevel -> %.13f\n
NegativeCapacitanceMeasurement
%012llx_%1d_%012llx
compensatedImpedance -> %.13f\n
hpmDebugFlags
ldcmV4DispatchQueue
com.apple.ioaccessorymanager.ldcm.usbc.mitigationsOverridden
leakagePassedCount
dryCount
rsvd0
com.apple.ioaccessorymanager.voltage.histogram.dp2
Close
Charging is not available because liquid has been detected in the Lightning connector. Disconnect to allow the connector to dry.
.%02x%02x%02x%02x%02x%02x
-[IOAccessorySystemStateMonitor notifyEndpointsUserActive:]
measurementCurrentSNR -> %.13f\n
mobile
iPad13,1
impedance
%@%@%@.csv
0x%x
com.apple.ioaccessorymanager.ldcm.usbc.audioUnitFailure
i
Has your device or charging cable been near liquid in the past 5 hours? \n\n
,
Active
disable_reason
WETMSG_BUTTON_CLOSE
Emergency Override
self BEGINSWITH[cd] 'internalWaveformData'
com.apple.ioaccessorymanager.ldcm.usbc.selfTestFailure
DisableMitigations
IOPortLDCMPortInterestCallback
CalibrationOutOfRange
-[LDCMMobileAssetManager queryMetadata]
Disconnect cable from charger and device. Unplug charger and allow all connectors to dry. This may take several hours.
IOGeneralInterest
IOPortFeatureLDCM
Unexpected measurement current or voltage SNR. measurementCurrentSNR: %f, measurementVoltageSNR: %f
com.apple.ioaccessorymanager.ldcm.usbc.ldcmPreempted
DP1
com.apple.ioaccessorymanager.ldcm.eis.mitigation.override.seen
com.apple.ioaccessorymanager.ldcm.eis.initial.wet.impedance.histogram
Dry
com.apple.ioaccessorymanager.ldcm.notification.wetduration
-[IOAccessoryLDCMPortManagerTypeC _controlLDCMMeasurements]
- How long was the exposure?\n\n
LDCMV4DisableMitigations
com.apple.ioaccessorymanager.ldcm.eis.mitigation.override
com.apple.CoreAccessories.LDCMFileRadarNotification
-[IOAccessoryLDCMPortManagerTypeC performTypeCReferenceMeasurement]
IOServiceTerminate
Unexpected calibration current or voltage amplitude. calibrationCurrentAmplitude: %f, calibrationVoltageAmplitude: %f
capacitance
.%012llx.%1d
calCurrentSNR -> %.13f\n
/var/logs/ldcm/halogenTypeC_ttr.wav
Clipped
-[LDCMMobileAssetManager init]_block_invoke_2
com.apple.ioaccessorymanager.ldcm.notification.voltagefluctuation
com.apple.ioaccessorymanager.ldcm.usbc.dryToWetTransition
com.apple.ioaccessorymanager.ldcm.notification.drytooshort
com.apple.ioaccessorymanager.ldcm.eis.calibration.bad.snr
-[LDCMMobileAssetManager downloadAsset:]_block_invoke
ERROR: calibration not successful. Result: x%x
WETMSG_BUTTON_RADAR
Radar
-[IOAccessoryLDCMPortManagerTypeC _setMitigations:]
-[IOAccessorySystemStateMonitor addEndpointForService:]
acc-mb-ld-lifetime
Failed
%@\n%@\n%@\n%@\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n%.12f\n
LIQUID DETECTION REPORT (detected via HalogenTypeC)\n\n
initialCapacitance
voltageMeasurement
-[IOAccessoryLDCMPortManagerTypeC _holdPowerAssertionTypeC:]
DefaultDry
com.apple.ioaccessorymanager.ldcm.eis.impedance.histogram
com.apple.ioaccessorymanager.ldcm.usbc.referenceMeasurementFailToPassDuration
IOAccessoryFileRadarLDCMV4_block_invoke
PlugIns/WetNotification.appex/Assets.car
com.apple.ioaccessorymanager.ldcm.usbc.wetOnConnect
com.apple.ioaccessorymanager.ldcm.usbc.impedanceTooLow
IOAccessoryPowerHandshake
IOAccessoryGenerateAggregatectlLog
iPhone12,8
com.apple.ioaccessorymanager.ldcm.usbc.WouldNotifyUser
com.apple.ioaccessorymanager
duration
yyyy-MM-dd HH:mm:ss
Trace
performEisMeasurement
iPad13,11
%@%@
DP2
com.apple.ioaccessorymanager.powerhandshakefail
com.apple.CoreAccessories.TestLDCMAnalyticsNotification
referenceMeasurementsFailed
CalibrationBadSNR
com.apple.IOAccessoryManagerFramework
WETMSG_DIALOG_HEADER_LOCKSCREEN_TYPEC
/var/logs/calibrationData.plist
Could not find Current Gain Correction Value. Falling back to default value of 1.0.
com.apple.ioaccessorymanager.ldcm.usbc.referenceMeasurementFailure
internalWaveformData
outOfProfileCount
uhpm
iPad
.log
lightningWet
EnableAnalyticsTest
com.apple.ioaccessorymanager.ldcm.usbc.audioUnitTimeout
LDCMAssetRetryQueryFrequency
LDCMAssetRetryQueryFrequencyTolerance
rsvd1
LDCMAssetQueryFrequency
Could not find Voltage Gain Correction Value. Falling back to default value of 1.0.
Resistance in Ohms -> %.13f\n
-[IOAccessoryLDCMPortManagerTypeC _generateLDCMCSVData]
Liquid Detected
&
{DockState=i{UnsignedWide=II}{UnsignedWide=II}Q[6C]QCQQBBddBB@{?=BII}IIB}
com.apple.ioaccessorymanager.ldcm.notification.overvoltage
event based DigitalID -> 0x%012llx\n
, %s(%s) = .3%fV
OK
Incomplete
FeaturesSupported
on
com.apple.ioaccessorymanager.voltage.histogram.dn1
Has your phone or charging cable been near liquid in the past 5 hours? \n\n
- Cable or iPad?\n\n
com.apple.ioaccessorymanager.ldcm.usbc.dryMeasurement
v16@?0q8
-[IOPortLDCMManagerV4 measureOccupiedWetPortDuration]
ACC2
IODeviceTree:/options
-[IOAccessoryLDCMPortManagerTypeC _fileRadarHalogenTypeC:TTRCategory:]_block_invoke
-[IOAccessorySystemStateEndpoint notifyUserActive:]
com.apple.ioaccessorymanager.ldcm.usbc.wetToDryTransitionPortNotEmpty
overVoltageCount
AUX
calVoltageSignalLevel -> %.13f\n
=
Default
measurementCurrentSNR
version
goertzelImpedance -> %.13f\n
measurementCurrentNoiseLevel -> %.13f\n
FBSOpenApplicationOptionKeyPromptUnlockDevice
N/A
pin -> %s\n
com.apple.ioaccessorymanager.ldcm.eis.digitalnoise.fault
com.apple.CoreAccessories.LDCMPreferencesNotification
Unexpected measurement current or voltage amplitude. beforeTIACurrentAmplitude: %f, beforeTIAVoltageAmplitude: %f
No
legacy
FakeWetMeasurements
AnalyticsTestEvent
Override
com.apple.iokit.hid.displayStatus
AppleTriStarBuiltIn
SelfTest
com.apple.ioaccessorymanager.ldcm.usbc.mitigationsFailure
com.apple.ioaccessorymanager.ldcm.usbc.wetOnDisconnect
com.apple.ioaccessorymanager.ldcm.eis.clipping
/var/logs/ldcm/
measurementSampleOffsetInFrames -> %d\n
calCurrentSignalLevel -> %.13f\n
-[IOAccessorySystemStateMonitor notifyEndpointsUserPresent:]
%02d%02d%02d-%02d%02d
Periodic
_%012llx_%1d
Reference
- Cable or device?\n\n
precalCurrentSignalLevel -> %.13f\n
com.apple.ioaccessorymanager.ldcm.eis.phase.low
WETMSG_DIALOG_BODY_LOCKSCREEN_TYPEC
%@%@%@.bin
com.apple.ioaccessorymanager.voltage.histogram.dn2
compensatedPhase -> %.13f\n
measurementCondetSNR -> %.13f\n
iPad13,2
logEventForAppleCare
IOServiceFirstPublish
/usr/local/bin/aggregatectl
BadAmplitudeCalibration
measurementVoltageSNR
-[IOPortLDCMManagerV4 storeWaveform:withWaveformDataLen:]
Attach
rsvd3
YES
com.apple.IOAccessoryManager.SystemStateMonitor
--command=DVEn
MdyHms
/tmp/halogen.wav
currentPhaseCompensation -> %.13f\n
boot-args
com.apple.RealitySimulation.DisplayRevealFirstBoot
com.apple.ioaccessorymanager.halogenTypeC.systemPower.queue
Undefined
DisableUI
Measurement Result -> %@\n\n
com.apple.ioaccessorymanager.ldcm.eis.initial.wet.capacitance.histogram
-[IOAccessoryLDCMPortManagerTypeC performTypeCSelfTest]
self BEGINSWITH[cd] 'internalMeasurementData'
wetCount
%s
com.apple.ioaccessorymanager.ldcm.eis.accessory.nofreepins
precalVoltageSNR -> %.13f\n
count
mitigationStatus
v8@?0
Could not find Current Phase Compensation Value. Falling back to default value of 0.0.
IOPMPowerSource
 (%d) Event: %s, TimeStamp = %llu, Vhi = %d, CumulativeTimeVhi = %d sec,
IOAccessoryHandleAttach
setupBatteryNotification
Error fetching fileB attritbutes. File ordering could be out of order. Error:%@ File:%@
--data=0x110B0400
SupportsEisAfe
/tmp/halogenTypeC_ttr.wav
LDCM
ProductType
VoltageGainCorrection
badCalCurrentSNR
- Cable or Phone?\n\n
AllowsDeviceRestart
com.apple.ioaccessorymanager.halogenMeasurement.systemPower.queue
attachDuration
/private/var/mobile/Library/Logs/com.apple.ioam/ioam_logs/
com.apple.ioaccessorymanager.ldcm.eis.impedance.high
DN1
measurementVoltageNoiseLevel -> %.13f\n
Manual HalogenTypeC radar request.\n
handleWetPromptResponse_block_invoke
LDCMBehaviorV4
Dismiss
badMeasurementVoltageSNR
com.apple.ioaccessorymanager.voltage.headset
Liquid Detected. Turning off Type-C Port. The port will be re-enabled automatically once dry.
-[IOAccessoryLDCMPortManagerTypeC performTypeCMeasurement]
Unexpected calibration current or voltage SNR. calibrationCurrentSNR: %f, calibrationVoltageSNR: %f
Invalid
com.apple.ioaccessorymanager.ldcm.eis.drytime.histogram
CurrentGainCorrection
None
IOAccessoryServiceMatchingCallback
accessoryPlug
LIQUID DETECTED
MANUAL RADAR REQUESTED\n\n
```
