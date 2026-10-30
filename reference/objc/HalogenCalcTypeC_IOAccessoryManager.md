# `HalogenCalcTypeC`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 49 instance variables, 49 properties, 84 instance methods, 0 class methods

## Instance variables

```
B _wetTooLong;
i _nSamples;
i _sizeofSample;
i _tmp1DataBuffSize;
i _tmp2DataBuffSize;
i _tmp3DataBuffSize;
d _voltageGainCorrection;
d _currentGainCorrection;
d _currentPhaseCompensation;
d _calVoltageSignalLevel;
d _calVoltageNoiseLevel;
d _calCurrentSignalLevel;
d _calCurrentNoiseLevel;
d _calVoltageSNR;
d _calCurrentSNR;
d _calVoltageAmplitude;
d _calCurrentAmplitude;
d _measurementVoltageSignalLevel;
d _measurementVoltageNoiseLevel;
d _measurementVoltageSNR;
d _measurementCurrentSignalLevel;
d _measurementCurrentNoiseLevel;
d _measurementCurrentSNR;
d _measurementVoltageAmplitude;
d _measurementCurrentAmplitude;
d _measurementVoltagePhase;
d _measurementCurrentPhase;
d _goertzelImpedance;
d _goertzelPhase;
d _compensatedImpedance;
d _compensatedPhase;
d _loadImpedanceInOhms;
d _loadPhase;
d _resistanceInOhms;
d _capacitanceInNanoF;
d _sampleRate;
d _signalFrequency;
d _tiaGain;
d _adcGain;
d _parasiticCap;
d _pinParasitics;
d _seriesResistance;
d _seriesRCResistance;
d _LDCMACCapacitance;
@"NSMutableData" _tmp1DataBuff;
@"NSMutableData" _tmp2DataBuff;
@"NSMutableData" _tmp3DataBuff;
^{OpaqueFFTSetupD=} _fftContext;
jd _seriesTotalImpedance;
```

## Properties

```
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
```

## Instance methods

```
-[HalogenCalcTypeC sampleRate];
-[HalogenCalcTypeC dealloc];
-[HalogenCalcTypeC setSampleRate:];
-[HalogenCalcTypeC _freeBuffers];
-[HalogenCalcTypeC LDCMACCapacitance];
-[HalogenCalcTypeC adcGain];
-[HalogenCalcTypeC signalFrequency];
-[HalogenCalcTypeC tiaGain];
-[HalogenCalcTypeC _allocBuffers];
-[HalogenCalcTypeC _applyFractionalPhaseShift:withPhaseDelay:];
-[HalogenCalcTypeC _applyGain:toData:];
-[HalogenCalcTypeC _applyHanningWindow:withSize:];
-[HalogenCalcTypeC _applyTiaGain:toCurrentData:];
-[HalogenCalcTypeC _doMuxComp:withPhase:];
-[HalogenCalcTypeC _goertzelSecondOrder:hasFftValue:hasPhase:withHanning:amplitudeCorrectionFactor:];
-[HalogenCalcTypeC _isResistiveOnly:resistanceInOhms:loadPhase:];
-[HalogenCalcTypeC _rcSolver];
-[HalogenCalcTypeC _snr:withGain:hasSignalLevel:hasNoiseLevel:];
-[HalogenCalcTypeC calCurrentAmplitude];
-[HalogenCalcTypeC calCurrentNoiseLevel];
-[HalogenCalcTypeC calCurrentSNR];
-[HalogenCalcTypeC calCurrentSignalLevel];
-[HalogenCalcTypeC calVoltageAmplitude];
-[HalogenCalcTypeC calVoltageNoiseLevel];
-[HalogenCalcTypeC calVoltageSNR];
-[HalogenCalcTypeC calVoltageSignalLevel];
-[HalogenCalcTypeC capacitanceInNanoF];
-[HalogenCalcTypeC compensatedImpedance];
-[HalogenCalcTypeC compensatedPhase];
-[HalogenCalcTypeC currentGainCorrection];
-[HalogenCalcTypeC currentPhaseCompensation];
-[HalogenCalcTypeC doCalibration:withCurrentData:];
-[HalogenCalcTypeC doLiquidDetection:withCurrentData:isReceptacleEmpty:isReceptacleWet:withWetTransitionThreshold:withDryTransitionThreshold:pinParasitics:measurementType:];
-[HalogenCalcTypeC fftContext];
-[HalogenCalcTypeC goertzelImpedance];
-[HalogenCalcTypeC goertzelPhase];
-[HalogenCalcTypeC initWithParams:signalFrequency:sampleRate:tiaGain:adcGain:parasiticCap:];
-[HalogenCalcTypeC loadImpedanceInOhms];
-[HalogenCalcTypeC loadPhase];
-[HalogenCalcTypeC measurementCurrentAmplitude];
-[HalogenCalcTypeC measurementCurrentNoiseLevel];
-[HalogenCalcTypeC measurementCurrentPhase];
-[HalogenCalcTypeC measurementCurrentSNR];
-[HalogenCalcTypeC measurementCurrentSignalLevel];
-[HalogenCalcTypeC measurementVoltageAmplitude];
-[HalogenCalcTypeC measurementVoltageNoiseLevel];
-[HalogenCalcTypeC measurementVoltagePhase];
-[HalogenCalcTypeC measurementVoltageSNR];
-[HalogenCalcTypeC measurementVoltageSignalLevel];
-[HalogenCalcTypeC nSamples];
-[HalogenCalcTypeC parasiticCap];
-[HalogenCalcTypeC pinParasitics];
-[HalogenCalcTypeC resistanceInOhms];
-[HalogenCalcTypeC seriesRCResistance];
-[HalogenCalcTypeC seriesResistance];
-[HalogenCalcTypeC seriesTotalImpedance];
-[HalogenCalcTypeC setAdcGain:];
-[HalogenCalcTypeC setFftContext:];
-[HalogenCalcTypeC setLDCMACCapacitance:];
-[HalogenCalcTypeC setNSamples:];
-[HalogenCalcTypeC setParasiticCap:];
-[HalogenCalcTypeC setPinParasitics:];
-[HalogenCalcTypeC setSeriesRCResistance:];
-[HalogenCalcTypeC setSeriesResistance:];
-[HalogenCalcTypeC setSeriesTotalImpedance:];
-[HalogenCalcTypeC setSignalFrequency:];
-[HalogenCalcTypeC setSizeofSample:];
-[HalogenCalcTypeC setTiaGain:];
-[HalogenCalcTypeC setTmp1DataBuff:];
-[HalogenCalcTypeC setTmp1DataBuffSize:];
-[HalogenCalcTypeC setTmp2DataBuff:];
-[HalogenCalcTypeC setTmp2DataBuffSize:];
-[HalogenCalcTypeC setTmp3DataBuff:];
-[HalogenCalcTypeC setTmp3DataBuffSize:];
-[HalogenCalcTypeC setWetTooLong:];
-[HalogenCalcTypeC sizeofSample];
-[HalogenCalcTypeC tmp1DataBuff];
-[HalogenCalcTypeC tmp1DataBuffSize];
-[HalogenCalcTypeC tmp2DataBuff];
-[HalogenCalcTypeC tmp2DataBuffSize];
-[HalogenCalcTypeC tmp3DataBuff];
-[HalogenCalcTypeC tmp3DataBuffSize];
-[HalogenCalcTypeC voltageGainCorrection];
-[HalogenCalcTypeC wetTooLong];
```
