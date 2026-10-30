# `AugmentedBatteryHealth`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 13 instance variables, 17 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _freshInitNeeded;
B _dataOnDemand;
B _bdc_output_ready;
I _errorBit;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
^v _model;
{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}} _program_code;
{ABHWeekly="deltaQmax"d"deltaRdc"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"deltaNCC"d"augmentedQmax"d"augmentedRdc"{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}}"augmentedNCC"d} _bdc_output_cache;
```

## Properties

```
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
```

## Class methods

```
+[AugmentedBatteryHealth algorithmWithData:];
```

## Instance methods

```
-[AugmentedBatteryHealth model];
-[AugmentedBatteryHealth logger];
-[AugmentedBatteryHealth setLogger:];
-[AugmentedBatteryHealth setModel:];
-[AugmentedBatteryHealth version];
-[AugmentedBatteryHealth init:];
-[AugmentedBatteryHealth output];
-[AugmentedBatteryHealth name];
-[AugmentedBatteryHealth runWithData:];
-[AugmentedBatteryHealth getAugmentedBatteryHealthConfig];
-[AugmentedBatteryHealth runType];
-[AugmentedBatteryHealth algoDescription];
-[AugmentedBatteryHealth freshInitNeeded];
-[AugmentedBatteryHealth preRun:];
-[AugmentedBatteryHealth bdc_output_cache];
-[AugmentedBatteryHealth bdc_output_ready];
-[AugmentedBatteryHealth dataOnDemand];
-[AugmentedBatteryHealth errorBit];
-[AugmentedBatteryHealth freshInitWithData:];
-[AugmentedBatteryHealth getWithSpecifier:];
-[AugmentedBatteryHealth program_code];
-[AugmentedBatteryHealth runPeriod];
-[AugmentedBatteryHealth setBdc_output_cache:];
-[AugmentedBatteryHealth setBdc_output_ready:];
-[AugmentedBatteryHealth setErrorBit:];
-[AugmentedBatteryHealth setProgram_code:];
-[AugmentedBatteryHealth updateWithSpecifier:];
```
