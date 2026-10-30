# `OnDeviceACAM`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 16 instance variables, 20 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _freshInitNeeded;
B _dataOnDemand;
{RuntimeOptions="SaveDebugInfo"B"WriteStdOut"B} _runTimeOptions;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
^v _model;
@"NSMutableDictionary" _lastBDCOutputTimestamp;
@"NSDictionary" _bdcOutputBuffer;
@"NSMutableArray" _debugLogBuffer;
@"NSDictionary" _freshInitInfo;
@"NSMutableArray" _runningInfo;
{ACAMPersistentStates="BatteryStatePrevious"{ACAMBatteryState="V"d"I"d"T"d"SOC"d"t"d}"BatteryStateCurrent"{ACAMBatteryState="V"d"I"d"T"d"SOC"d"t"d}"ElectrodeStatePrevious"{ACAMElectrodeState="x"d"y"d"xLastExtreme"d"yLastExtreme"d"potentialAnode"d"potentialCathode"d"wRcFreshAtCurrentTemp"d"wRaFreshAtCurrentTemp"d"deltaResistancePos"d"deltaResistanceNeg"d"resistancePos"d"resistanceNeg"d}"ElectrodeStateCurrent"{ACAMElectrodeState="x"d"y"d"xLastExtreme"d"yLastExtreme"d"potentialAnode"d"potentialCathode"d"wRcFreshAtCurrentTemp"d"wRaFreshAtCurrentTemp"d"deltaResistancePos"d"deltaResistanceNeg"d"resistancePos"d"resistanceNeg"d}"AgingState"{ACAMAgingState="gasSwell"d"protectiveBuffer"d"timePassedOnset"d"hardSwell"d"expGammaHardSwell"d"wRaChangeRatio"d"wRcChangeRatio"d"Qp"d"QpLoss"d"QpPhaseLoss"d"QpAcidLoss"d"QpCrackLoss"d"Qn"d"QLi"d"integralJSEIdt"d"integralJWRadt"d"integralJWRcdt"d"integralJYShrinkdt"d"integralJAvgRadt"d"integralJAvgRcdt"d}"UpdatorState"{ACAMUpdatorState="x0"d"x100"d"y0"d"y100"d"Qmax"d"Qn"d"Qp"d"resistancePosChgRatio"d"resistanceNegChgRatio"d"resistancePosDcgRatio"d"resistanceNegDcgRatio"d"integralYShrinkdt"d}"Derivative"{ACAMDerivative="dProtectiveBufferdt"d"dGasSwelldt"d"dExpGammaHardSwelldt"d"dHardSwelldt"d"dQpdt"d"dQpPhasedt"d"dQpAciddt"d"dQpCrackdt"d"dQndt"d"dQLidt"d"JSEI"d"dWRadt"d"dWRcdt"d"dYShrinkdt"d"dAvgRadt"d"dAvgRcdt"d"accelerateRateFactorPhase"d}"DynamicConfiguration"{ACAMDynamicConfiguration="SOCBiasCorrection"d"voltageChargeLimit"d}"Statistics"{ACAMStatistics="sleepStatistics"[6Q]}"Status"{ACAMStatus="mPreviousAlgoStatus"i"mCurrentAlgoStatus"i"mCurrentDataError"i"mBuffer"i"mInitType"i"mFreshInitReason"i"mSystemSignal"{SystemSignals="batteryAuthentication"B"batteryReplacement"B"batteryReplacementDate"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"time"Q"version"Q"batteryInfo"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}}}"History"{simpleList<ACAMHistory>="m_head"^v"m_tail"^v"m_size"Q}"AlgorithmInitialized"B"ParameterVersion"Q} _snapshotCache;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (T@"NSMutableDictionary",&,V_lastBDCOutputTimestamp) lastBDCOutputTimestamp;
@property (T@"NSDictionary",&,V_bdcOutputBuffer) bdcOutputBuffer;
@property (T@"NSMutableArray",&,N,V_debugLogBuffer) debugLogBuffer;
@property (T{RuntimeOptions=BB},N,V_runTimeOptions) runTimeOptions;
@property (T{ACAMPersistentStates={ACAMBatteryState=ddddd}{ACAMBatteryState=ddddd}{ACAMElectrodeState=dddddddddddd}{ACAMElectrodeState=dddddddddddd}{ACAMAgingState=dddddddddddddddddddd}{ACAMUpdatorState=dddddddddddd}{ACAMDerivative=ddddddddddddddddd}{ACAMDynamicConfiguration=dd}{ACAMStatistics=[6Q]}{ACAMStatus=iiiiii{SystemSignals=BB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}QQ{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}}{simpleList<ACAMHistory>=^v^vQ}BQ},N,V_snapshotCache) snapshotCache;
@property (T@"NSDictionary",&,V_freshInitInfo) freshInitInfo;
@property (T@"NSMutableArray",&,V_runningInfo) runningInfo;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_version) version;
@property (T@"NSString",R,N,V_algoDescription) algoDescription;
@property (T@"NSNumber",R,N,V_runPeriod) runPeriod;
@property (T^Q,R,N,V_runType) runType;
@property (TB,R,N,V_freshInitNeeded) freshInitNeeded;
@property (TB,R,N,V_dataOnDemand) dataOnDemand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[OnDeviceACAM algorithmWithData:];
```

## Instance methods

```
-[OnDeviceACAM model];
-[OnDeviceACAM logger];
-[OnDeviceACAM setLogger:];
-[OnDeviceACAM setModel:];
-[OnDeviceACAM snapshotCache];
-[OnDeviceACAM setSnapshotCache:];
-[OnDeviceACAM version];
-[OnDeviceACAM init:];
-[OnDeviceACAM output];
-[OnDeviceACAM name];
-[OnDeviceACAM runWithData:];
-[OnDeviceACAM runType];
-[OnDeviceACAM algoDescription];
-[OnDeviceACAM bdcOutputBuffer];
-[OnDeviceACAM freshInitNeeded];
-[OnDeviceACAM setRunningInfo:];
-[OnDeviceACAM addToBdcOutputBuffer::];
-[OnDeviceACAM dataOnDemand];
-[OnDeviceACAM debugLogBuffer];
-[OnDeviceACAM freshInitInfo];
-[OnDeviceACAM freshInitWithData:];
-[OnDeviceACAM getOnDeviceACAMConfig];
-[OnDeviceACAM getWithSpecifier:];
-[OnDeviceACAM lastBDCOutputTimestamp];
-[OnDeviceACAM multiLog:];
-[OnDeviceACAM runPeriod];
-[OnDeviceACAM runTimeOptions];
-[OnDeviceACAM runningInfo];
-[OnDeviceACAM setBdcOutputBuffer:];
-[OnDeviceACAM setDebugLogBuffer:];
-[OnDeviceACAM setFreshInitInfo:];
-[OnDeviceACAM setLastBDCOutputTimestamp:];
-[OnDeviceACAM setRunTimeOptions:];
-[OnDeviceACAM updateWithSpecifier:];
```
