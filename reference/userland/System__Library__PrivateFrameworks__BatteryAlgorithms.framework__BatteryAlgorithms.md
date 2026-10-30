# `/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`

iOS 27.2 dyld shared cache image. Version `156.0.0.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 6 classes, 2 protocols, 210 methods, 114 properties

### Class pages

Every class and protocol, with its methods: [`AdaptiveOCV`](../objc/AdaptiveOCV_BatteryAlgorithms.md), [`AugmentedBatteryHealth`](../objc/AugmentedBatteryHealth_BatteryAlgorithms.md), [`BAProtocol`](../objc/BAProtocol_BatteryAlgorithms.protocol.md), [`CafeLVR`](../objc/CafeLVR_BatteryAlgorithms.md), [`CafeSwell`](../objc/CafeSwell_BatteryAlgorithms.md), [`NSObject`](../objc/NSObject_BatteryAlgorithms.protocol.md), [`OnDeviceACAM`](../objc/OnDeviceACAM_BatteryAlgorithms.md), [`SampleAlgorithm`](../objc/SampleAlgorithm_BatteryAlgorithms.md)

### Classes

`AdaptiveOCV`, `AugmentedBatteryHealth`, `CafeLVR`, `CafeSwell`, `OnDeviceACAM`, `SampleAlgorithm`

### Protocols

`BAProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) version;
@property (T@"NSString",R,N) algoDescription;
@property (T@"NSNumber",R,N) runPeriod;
@property (T^Q,R,N) runType;
@property (TB,R,N) dataOnDemand;
@property (TB,R,N) freshInitNeeded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (T{PersistentState={State=[100i][50i][15i][100i][5[500d]]dddid[6d][3d]iiii}{ConfigurationOCV=[103d][103d][103d][103d][103d]dB}},N,V_persistentStateCache) persistentStateCache;
@property (T{BDCOutput={vector<double, std::allocator<double>>=^d^d{?=^d}}{vector<double, std::allocator<double>>=^d^d{?=^d}}{vector<double, std::allocator<double>>=^d^d{?=^d}}{vector<double, std::allocator<double>>=^d^d{?=^d}}{vector<double, std::allocator<double>>=^d^d{?=^d}}ii},N,V_bdcOutputCache) bdcOutputCache;
@property (T{MLOCVModel=[1{ConfigurationMLOCV=[91d]}]},N,V_mlOcvModelCache) mlOcvModelCache;
@property (TB,N,V_outputReady) outputReady;
@property (T{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}},N,V_programName) programName;
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
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (T{ABHWeekly=d{vector<double, std::allocator<double>>=^d^d{?=^d}}dd{vector<double, std::allocator<double>>=^d^d{?=^d}}d},N,V_bdc_output_cache) bdc_output_cache;
@property (TB,N,V_bdc_output_ready) bdc_output_ready;
@property (TI,N,V_errorBit) errorBit;
@property (T{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}},N,V_program_code) program_code;
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
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (T^v,N,V_state_retriever) state_retriever;
@property (T{vector<std::vector<std::vector<double>>, std::allocator<std::vector<std::vector<double>>>>=^v^v{?=^v}},N,V_lvr_weights) lvr_weights;
@property (Td,N,V_lvr_offset) lvr_offset;
@property (T{Input=qq},N,V_previous_input) previous_input;
@property (TB,N,V_use_input_overwrite) use_input_overwrite;
@property (T{SMCKeyData=ddd},N,V_input_overwrite) input_overwrite;
@property (T{PersistentState={Lifetime={Controller=ddd}qq}{Weekly={Controller=ddd}qqiqq}{ProjectedLifetime={Controller=ddd}qqd}{Input=qq}{ShutdownInfo=dd}Bdi},N,V_snapshot) snapshot;
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
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T^v,N,V_model) model;
@property (Td,N,V_previousACAMInitializationTime) previousACAMInitializationTime;
@property (Td,N,V_previousFreshInitializationTime) previousFreshInitializationTime;
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
@property (T@"NSObject<OS_os_log>",&,N,V_logger) logger;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_version) version;
@property (T@"NSString",R,N,V_algoDescription) algoDescription;
@property (T@"NSNumber",R,N,V_runPeriod) runPeriod;
@property (T^Q,R,N,V_runType) runType;
@property (TB,R,N,V_freshInitNeeded) freshInitNeeded;
@property (TB,R,N,VdataOnDemand) dataOnDemand;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (643)

```
[Heron runtime error]Unexpected mode
 Must be opened by 
deltaResistancePos
control_effort
currentDataError
D83COS
table_pntr
<
V64eATL
streamCurrentDate
std::string_view TypeErasedConfig::utility::get_type_name() [T = std::string]
Thp_last
D83
D83ATL
use_input_overwrite
Persistent state is generated
persistentState.Derivative.dAvgRcdt
persistentState.History
ChgOCV_temp_co
timePassedOnset
OnDeviceACAMWeekly
readonly_states
SOC
but destination has 
V59ATL
Writing currentRunningInfo
persistentState.ElectrodeStateCurrent.potentialAnode
persistentState.AgingState.Qn
t_last
N240ATL
input_bmu_time
persistentState.AgingState.expGammaHardSwell
persistentState.AgingState.QpAcidLoss
matmul
][Warning] 
Editing an entry after setup complete is not allowed. Consider use `viewEntry`
V159
V64pATL
I
N237sFDB
%lu valid OBC data received.
OCVdrift
potentialCathode
D48ATL
Attempting to convert unsupported value to double
PreviousACAMInitializationTime
Fallback initialization complete.
persistentState.Status.mPreviousAlgoStatus
V63
previousACAMInitializationTime
%lu 1Hz data received 
x100
 and closed by 
sbcInterval
streamDateEnd
fastAlgoInterval
InstantAmperage
BatteryStateCurrent
accelerateRateFactorPhase
kUsePreviousInput
Fallback init inputs
SBC
weekly_lvr
validDataCount
numSubChunks
persistentState.UpdatorState.integralYShrinkdt
persistentState.Derivative.dHardSwelldt
persistentState.Derivative.dQpAciddt
Policy activation
xLastExtreme
kBDCOutputData
streamRequest
final_control_effort
previous_time
Editing entries after setup complete is not allowed. Consider use `viewEntriesByRegex`
 # 
D47ATL
TimeAtHighSoc
augmentedRdc
RunningInfo
kSavedAlgoStateAdaptiveOCVInterface
persistentState.BatteryStateCurrent.V
metric1
f_mid_h
integralJWRadt
dGasSwelldt
Config module: 
deltaQmax
Non-1D std library array-like object cannot use flat assigner.
%lu valid SBC data received.
YYYY-MM-dd HH:m:s.SSS
persistentState.Status.mCurrentAlgoStatus
sbcStreamData
DateOfFirstUse
value3
pps3
\n{\n    \"Lifetime\": {\n        \"controller\": {\n            \"Ki\": 8e-10,\n            \"Kp\": 0.0005,\n            \"u_max\": 1,\n            \"u_min\": 0\n        },\n        \"settings\": {\n            \"shape\": {\n              
Adding an entry after setup complete is not allowed
wRcFreshAtCurrentTemp
Statistics
normalized_lvr
cover_scores
[Heron runtime error]trend changes in control effort column
: 
previousFreshInitializationTime
persistentState.AgingState.Qp
metric3
control_effort_slew_rate_down
integralJAvgRadt
com.apple.batteryalgorithms
Enhance the gauging output with physics-based model like ACAM
Running OnDeviceACAM
persistentState.ElectrodeStateCurrent.resistanceNeg
persistentState.UpdatorState.x100
AdaptiveOCVTrackingMatrix.cpp
dYShrinkdt
V68TBATL
ChargeAccum_last
V63eATL
V68MDCOS
ChargeAccum
%@,%@
persistentState.AgingState.integralJYShrinkdt
persistentState.DynamicConfiguration.SOCBiasCorrection
└──
or 
ElectrodeStateCurrent
controller_state
persistentState.ElectrodeStateCurrent.xLastExtreme
error_integral
D47COS
V64
kSavedAlgoStateCafeSwellCoreAlgo
gasSwell
yShrink
{
D38
V57COS
policy_ProjectedLifetime_controller_integral_error
std::string_view TypeErasedConfig::utility::get_type_name() [T = std::vector<std::vector<std::vector<double>>>]
\n{\n    \"Lifetime\": {\n        \"controller\": {\n            \"Ki\": 8e-10,\n            \"Kp\": 0.0005,\n            \"u_max\": 1,\n            \"u_min\": 0\n        },\n        \"settings\": {\n            \"shape\": {\n              
Attempting to get an instance that does not exist
Only one delimiter is allowed between groups
value
rawSmcKey
SMC Key for Running OnDeviceACAM
OCV
Unable to identify a key for submodule!
persistentState.AgingState.protectiveBuffer
persistentState.AgingState.integralJWRcdt
persistentState.UpdatorState.resistanceNegChgRatio
control_effort_table
N237bATL
preInit result
persistentState.AgingState.timePassedOnset
parent
CtC3x3
Not yet initialized
streamLastRunDate
persistentState.Statistics.sleepStatistics[4]
policy_ProjectedLifetime
QLi
N240
dailyStreamData
persistentState.Status.mSystemSignal.time
dProtectiveBufferdt
?
Inbalanced array open/close characters detected.
#
D94ATL
Qmax
augmentedQmax
BDC_SBC
Failed to update with: 
postFreshInitSnapshot
persistentState.Derivative.dQndt
persistentState.Derivative.accelerateRateFactorPhase
V57
%lu valid ACAMDaily data received.
obcStreamData
kSavedAlgoStateOnDeviceACAMDebugLog
persistentState.ElectrodeStatePrevious.deltaResistanceNeg
persistentState.UpdatorState.x0
[BaseLogger] flush is called before setup
submodules
D93ATL
BDC_Weekly
 
bdcDailyData
string_view::substr
AlgorithmInitialized
D93
D23ATL
amaStreamData
table_dist_day
control_effort_slew_rate_up
[BaseLogger] log is called before setup
 already exists.
resistancePos
OnDeviceACAMSBC
persistentState.Derivative.dYShrinkdt
config_version
: {
persistentState.AgingState.QLi
OCV_temp_co
][Error] 
D38LGC
V68MDATL
model_prediction
persistentState.ElectrodeStatePrevious.resistanceNeg
metric2
config_selected
level: 
integralJSEIdt
streamDateStart
policy_Lifetime_control_effort
x0
persistentState.ElectrodeStatePrevious.resistancePos
persistentState.Derivative.dQpCrackdt
persistentState.DynamicConfiguration.voltageChargeLimit
Not yet implemented
UpdatorState
Adaptive algorithm that optimizes battery longevity by controlling the low voltage residency through Vmax
shutdown voltage [V]
input_overwrite
WriteStdOut
NCCp
%04x
persistentState.ParameterVersion
policy_Lifetime
D94LGC
expGammaHardSwell
 [typeid: 
AlgoTemperature
Do you mean 
DynamicConfiguration
qual_flag
%lu
QpAcidLoss
shutdown debounce time [s]
previous_lvr
integralJAvgRcdt
OCV_selected
swell_target
description
 entires. Specifier must have no more tokens than destination entries.
streamPaginate
persistentState.UpdatorState.resistancePosDcgRatio
debounce_time
yLastExtreme
integralYShrinkdt
errorBits
mCafe
idx_min_rmse
persistentState.ElectrodeStatePrevious.x
 not found.
kPowerLogData
T
persistentState.Status.mBuffer
D84
programCode
std::string_view TypeErasedConfig::utility::get_type_name() [T = unsigned int]
Soft initialization result
Editing entries after setup complete is not allowed. Consider use `viewEntriesByRegex` (not yet supported)
potentialAnode
 entries.
[%@] %@
persistentState.BatteryStatePrevious.T
Controller output max saturation
Unknown option to convert module to string
Invalid specifier: 
DeviceType
vector
VacVoltageLimit
timeSinceLastDaily
lastCafeFast
%lu valid 1Hz data found out of %lu.\n- %lu are invalid records\n- %lu have overlapping timestamp with SBC\n- %lu chunks identified\n
persistentState.AgingState.wRaChangeRatio
dExpGammaHardSwelldt
V64pCOS
PresentDOD
persistentState.Status.mCurrentDataError
persistentState.Status.mFreshInitReason
policy_Weekly
unordered_map::at: key not found
persistentState.AgingState.integralJAvgRadt
persistentState.Derivative.dGasSwelldt
1.0
rows == B.size() && cols == B[0].size()
Entry: 
Fallback initialization result
apparentWRa
persistentState.Derivative.dAvgRadt
persistentState.Status.mSystemSignal.batteryReplacementDate
Error reading file: %@
, enable: 
OnDeviceACAM: %@
avgRcGrowthRatio
table_dist
integralJWRcdt
deltaResistanceNeg
basic_string
D47
CycleCount
NominalChargeCapacity
VCafe
data_number
BDC-based initialization result: After daily data-based fallback initialization
y100
timeSinceLastWeekly
persistentState.UpdatorState.resistanceNegDcgRatio
persistentState.Status.mSystemSignal.batteryInfo
final_budget_target
\" is not a valid bool specifier
D37LGC
persistentState.BatteryStatePrevious.I
value1
aged_target
Symptom-based OCV algorithm to enhance the accuracy of Machine-Learning OCV.
}
preInit done.
grace_period
\n{\n  \"Lifetime\": {\n    \"controller\": {\n      \"Ki\": 8e-10,\n      \"Kp\": 0.0005,\n      \"u_max\": 1,\n      \"u_min\": 0\n    },\n    \"settings\": {\n      \"shape\": {\n        \"a\": 0,\n        \"b\": 5.7519e-05,\n        \"c
, 
Non-white space char that's not delimiter is not allowed between groups
V54eATL
mlOcvModelCache
persistentState.AgingState.hardSwell
D84LGC
V53pCOS
lastUpdateTime
totalDataCount
persistentState.ElectrodeStatePrevious.potentialCathode
D84ATL
Daily
Error converting NSArray to JSON: %@
ready
subtract
dQpCrackdt
OnDeviceACAM
ProjectedLifetime
streamSkipRun
persistentState.ElectrodeStatePrevious.deltaResistancePos
persistentState.ElectrodeStateCurrent.yLastExtreme
Amperage
SOCBiasCorrection
sleepStatistics
D38ATL
BDC_OBC
persistentState.Derivative.JSEI
] 
freshInitReason
V59
persistentState.BatteryStatePrevious.V
persistentState.BatteryStateCurrent.t
persistentState.UpdatorState.Qn
SafeHarbor
protectiveBuffer
resistanceNegDcgRatio
V53
persistentState.ElectrodeStateCurrent.potentialCathode
input_normalized_lvr
AlgoCycleCountDbgData
persistentState.Statistics.sleepStatistics[2]
persistentState.Status.mSystemSignal.batteryAuthentication
[BaseLogger] Trying to clone another setup after init completed
>
String group format wrong.
resistanceNeg
QpPhaseLoss
AugmentedBatteryHealth
deferralDuration
numObcDataUsed
persistentState.Derivative.dQpPhasedt
 already exists!
 tokens 
policy_Weekly_controller_integral_error
kSavedAlgoStateCafeSwellInterface
postRunningSnapshot
V
persistentState.AgingState.integralJAvgRcdt
AgingState
Proportional controller gain
N237b
deltaRdc
\n
persistentState.UpdatorState.Qmax
<Empty Module>
resistancePosDcgRatio
std::string_view TypeErasedConfig::utility::get_type_name() [T = long long]
currentAlgoStatus
Soft initiliazation done. Persistent state is loaded. 
Controller
D23
N237sATL
Finished currentRunningInfo
Error parsing JSON: %@
BDC Data is not present. Performing fallback initialization
Submodule: 
total_budget
wRaFreshAtCurrentTemp
V53eATL
N228b
message
colsA == rowsB
final_time
},
resistanceNegChgRatio
V54
last_input_bmu_time
policy_ProjectedLifetime_control_effort
persistentState.UpdatorState.y0
persistentState.AlgorithmInitialized
V57ATL
persistentState.ElectrodeStatePrevious.wRcFreshAtCurrentTemp
resistancePosChgRatio
deltaNCC
 does not exist.
amaInterval
persistentState.UpdatorState.resistancePosChgRatio
state
ParameterVersion
std::string_view TypeErasedConfig::utility::get_type_name() [T = ACAMStatus]
\"
The bool specifier must be one of the following (case-insentivie): 
RaTableRaw0
Timestamp
V_captured
persistentState.ElectrodeStatePrevious.xLastExtreme
%lu valid ACAMSBC data received.
t
persistentState.AgingState.integralJWRadt
Just to show that this works
Execution interval [s]
Provided parent does not contain this module
AlgoChemID
disable_dynamic_shutdown
persistentState.AgingState.gasSwell
persistentState.Derivative.dExpGammaHardSwelldt
table_dist_temp
V68
policy_Lifetime_controller_integral_error
datacheckOverride
BDC-based initialization result: intermediate state #%lu
ShutdownInfo
max_interval
ElectrodeStatePrevious
D48LGC
agedRa
final_socv
configuration
lastCafeSlow
kSavedAlgoStateAdaptiveOCVCoreAlgo
Finished
dQpPhasedt
BatteryStatePrevious
_fieldOffset does not match
std::string_view TypeErasedConfig::utility::get_type_name() [T = unsigned long]
D48
avgRaGrowthRatio
RefTemp
[
^
dQpAciddt
Config entry: 
Weekly
Performing BDC-based initialization.
persistentState.Derivative.dWRcdt
[Heron runtime error]unexpected parameter size: 0
Derivative
persistentState.ElectrodeStateCurrent.wRaFreshAtCurrentTemp
wRaChangeRatio
timeSinceLastSBC
.
%@
persistentState.AgingState.wRcChangeRatio
kSavedAlgoStateOnDeviceACAMFreshInitInfo
table_data
V54eLGC
V63pATL
N237s
CycleCountLastQmax
Model-based algorithm to provide adaptively insight to charging controller and optimize user-experience
Physics-based battery aging model for on-device battery chemistry state.
persistentState.ElectrodeStatePrevious.wRaFreshAtCurrentTemp
OCVcurvehysteresis_now
wRcChangeRatio
N237bFDB
bdcInitInfo
persistentState.ElectrodeStateCurrent.deltaResistanceNeg
No prior group is detected
PreviousFreshInitializationTime
TotalOperatingTime
readonly_state
parsedTeq
persistentState.Statistics.sleepStatistics[1]
N227b
persistentState.AgingState.QpCrackLoss
smcData
D37
V64eCOS
Qp
apparentQmax
persistentState.Status.mSystemSignal.batteryReplacement
Perturbation to avoid forced activation [1]
slowAlgoInterval
persistentState.BatteryStateCurrent.T
persistentState.Status.mSystemSignal.version
pps1
Controller output min saturation
\" 
augmentedNCC
input_valid_flag
fallbackInitInfo
y0
persistentState.BatteryStatePrevious.t
]
V68TBCOS
CafeSwell
kSavedAlgoStateOnDeviceACAMCoreAlgo
numBdcTriggers
[BaseLogger] setup is called before initialization
dataTable<T>::dataTable requires at least two elements[pointer constructor]
dataTable<T>::interpolate: Division by zero
dHardSwelldt
systemState
V54pATL
CafeLVR
persistentState.ElectrodeStatePrevious.potentialAnode
persistentState.ElectrodeStateCurrent.resistancePos
[Heron runtime error]parameter size mismatch
controller_integral_error
statusBuffer
RMSE_ocv_candidates
persistentState.ElectrodeStateCurrent.deltaResistancePos
persistentState.Statistics.sleepStatistics[0]
persistentState.Status.mInitType
Forgetting factor [1]
N227bATL
persistentState.ElectrodeStateCurrent.wRcFreshAtCurrentTemp
Integral controller gain
V53pATL
kCoreAnalyticsData
persistentState.ElectrodeStatePrevious.yLastExtreme
persistentState.UpdatorState.y100
std::string_view AbstractTree::get_type_name() [T = AbstractTree::Tree<LogEntry<std::variant<float, double, std::unordered_map<std::string, double>>, Properties>>]
savedAlgoState
hardSwell
voltageChargeLimit
V54pLGC
V64S
snapshot
VirtualTemperature
[Heron runtime error]non-unique entry encountered in control effort column
i
V53eCOS
print_detail
BatteryAuthPass
controller_setpoint
std::string_view AbstractTree::get_type_name() [T = LoggerModule]
persistentState.AgingState.integralJSEIdt
Non-invertible. Giving up.\n
LowVoltageResidencyCounters
policy_Weekly_control_effort
persistentState.ElectrodeStateCurrent.y
OCVDrift
,
value2
persistentState.UpdatorState.Qp
i3
├──
batteryState
OnDeviceACAMDaily
std::string_view TypeErasedConfig::utility::get_type_name() [T = std::vector<double>]
lastBVVL
Vprev_mV
numSbcDataUsed
persistentState.BatteryStateCurrent.SOC
persistentState.ElectrodeStatePrevious.y
idx_selected_OCV
kVerboseOutput
longevityPredict
SaveDebugInfo
persistentState.Statistics.sleepStatistics[3]
ChgOCV
Specifier contains 
Qmax0
final_debounce_time
smcKeyInputs
persistentState.Derivative.dWRadt
Serial
PresentDOD0
ccdrift_model_parameter
persistentState.AgingState.QpLoss
N227bMUR
BDC_Daily
AdaptiveOCV
BDC_AMA
persistentState.AgingState.QpPhaseLoss
Cy3x1
execution_counter
D94
Unrecognized Program. Using default parameters.\n
kSavedAlgoStateOnDeviceACAMRunningInfo
initType
grace_period_budget_target
History[
persistentState.BatteryStateCurrent.I
 does not exist!
integralJYShrinkdt
previousAlgoStatus
V59LGC
 entries, but destination has 
\": 
Must have at least 2 specifiers
QpCrackLoss
Voltage
BDC-based initialization complete.
obcInterval
persistentState.Derivative.dQpdt
SampleAlgorithm
controller
:
std::string_view TypeErasedConfig::utility::get_type_name() [T = unsigned long[6]]
safe_harbor_status
Qn
persistentState.Derivative.dProtectiveBufferdt
D37ATL
Running result: intermediate state #%lu
persistentState.ElectrodeStateCurrent.x
delta_lvr
kSavedAlgoStateOnDeviceACAMInterface
persistentState.BatteryStatePrevious.SOC
persistentState.Derivative.dQLidt
persistentState.Statistics.sleepStatistics[5]
pps2
[CafeLVR] Persistent state found but loading failed
[CafeLVR] %@ is not a recognized key from CafeLVR output
%@
%s\n
I was passed in these keys: %@
Output Dictionary looks like : %@
Update with: %@
```
