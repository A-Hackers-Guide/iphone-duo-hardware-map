# `AdaptiveOCV`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 14 instance variables, 18 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _freshInitNeeded;
B _dataOnDemand;
B _outputReady;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
^v _model;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} _programName;
{BDCOutput="OCV_selected"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"V_captured"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"cover_scores"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"RMSE_ocv_candidates"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"ccdrift_model_parameter"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"idx_min_rmse"i"data_number"i} _bdcOutputCache;
{MLOCVModel="configPool"[1{ConfigurationMLOCV="OCV"[91d]}]} _mlOcvModelCache;
{PersistentState="state"{State="table_dist"[100i]"table_dist_temp"[50i]"table_dist_day"[15i]"table_pntr"[100i]"table_data"[5[500d]]"f_mid_h"d"OCVcurvehysteresis_now"d"Vprev_mV"d"data_number"i"i3"d"CtC3x3"[6d]"Cy3x1"[3d]"t_last"i"ChargeAccum_last"i"Thp_last"i"idx_selected_OCV"i}"config_selected"{ConfigurationOCV="OCV"[103d]"OCV_temp_co"[103d]"ChgOCV"[103d]"ChgOCV_temp_co"[103d]"SOC"[103d]"RefTemp"d"ready"B}} _persistentStateCache;
```

## Properties

```
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
```

## Class methods

```
+[AdaptiveOCV algorithmWithData:];
```

## Instance methods

```
-[AdaptiveOCV model];
-[AdaptiveOCV logger];
-[AdaptiveOCV setLogger:];
-[AdaptiveOCV setModel:];
-[AdaptiveOCV version];
-[AdaptiveOCV init:];
-[AdaptiveOCV output];
-[AdaptiveOCV name];
-[AdaptiveOCV setProgramName:];
-[AdaptiveOCV programName];
-[AdaptiveOCV setOutputReady:];
-[AdaptiveOCV outputReady];
-[AdaptiveOCV runWithData:];
-[AdaptiveOCV mlOcvModelCache];
-[AdaptiveOCV runType];
-[AdaptiveOCV algoDescription];
-[AdaptiveOCV freshInitNeeded];
-[AdaptiveOCV preRun:];
-[AdaptiveOCV bdcOutputCache];
-[AdaptiveOCV dataOnDemand];
-[AdaptiveOCV freshInitWithData:];
-[AdaptiveOCV getAdaptiveOCVConfig];
-[AdaptiveOCV getWithSpecifier:];
-[AdaptiveOCV persistentStateCache];
-[AdaptiveOCV runPeriod];
-[AdaptiveOCV setBdcOutputCache:];
-[AdaptiveOCV setMlOcvModelCache:];
-[AdaptiveOCV setPersistentStateCache:];
-[AdaptiveOCV updateWithSpecifier:];
```
