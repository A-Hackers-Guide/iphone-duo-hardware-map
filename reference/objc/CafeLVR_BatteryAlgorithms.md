# `CafeLVR`

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BAProtocol`
- 16 instance variables, 20 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _freshInitNeeded;
B _dataOnDemand;
B _use_input_overwrite;
@"NSString" _name;
@"NSString" _version;
@"NSString" _algoDescription;
@"NSNumber" _runPeriod;
^Q _runType;
@"NSObject<OS_os_log>" _logger;
^v _model;
^v _state_retriever;
d _lvr_offset;
{Input="normalized_lvr"q"bmu_time"q} _previous_input;
{vector<std::vector<std::vector<double>>, std::allocator<std::vector<std::vector<double>>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _lvr_weights;
{SMCKeyData="bmu_time"d"normalized_lvr"d"t"d} _input_overwrite;
{PersistentState="lifetime"{Lifetime="controller"{Controller="error_integral"d"setpoint"d"output"d}"previous_lvr"q"previous_time"q}"weekly"{Weekly="controller"{Controller="error_integral"d"setpoint"d"output"d}"previous_lvr"q"previous_time"q"execution_counter"i"delta_lvr"q"weekly_lvr"q}"projected_lifetime"{ProjectedLifetime="controller"{Controller="error_integral"d"setpoint"d"output"d}"previous_lvr"q"previous_time"q"rate"d}"input"{Input="normalized_lvr"q"bmu_time"q}"shutdown_info"{ShutdownInfo="debounce_time"d"socv"d}"input_valid_flag"B"final_control_effort"d"config_version"i} _snapshot;
```

## Properties

```
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
```

## Class methods

```
+[CafeLVR algorithmWithData:];
```

## Instance methods

```
-[CafeLVR model];
-[CafeLVR logger];
-[CafeLVR setLogger:];
-[CafeLVR setModel:];
-[CafeLVR setSnapshot:];
-[CafeLVR snapshot];
-[CafeLVR version];
-[CafeLVR init:];
-[CafeLVR output];
-[CafeLVR name];
-[CafeLVR runWithData:];
-[CafeLVR input_overwrite];
-[CafeLVR runType];
-[CafeLVR setLvr_weights:];
-[CafeLVR state_retriever];
-[CafeLVR algoDescription];
-[CafeLVR freshInitNeeded];
-[CafeLVR preRun:];
-[CafeLVR dataOnDemand];
-[CafeLVR exportConfigJson];
-[CafeLVR freshInitWithData:];
-[CafeLVR getCafeLVRConfig];
-[CafeLVR getWithSpecifier:];
-[CafeLVR importConfigDictionary:];
-[CafeLVR importConfigJson:];
-[CafeLVR lvr_offset];
-[CafeLVR lvr_weights];
-[CafeLVR multiLog:];
-[CafeLVR previous_input];
-[CafeLVR runPeriod];
-[CafeLVR setInput_overwrite:];
-[CafeLVR setLvr_offset:];
-[CafeLVR setPrevious_input:];
-[CafeLVR setState_retriever:];
-[CafeLVR setUse_input_overwrite:];
-[CafeLVR updateWithSpecifier:];
-[CafeLVR use_input_overwrite];
```
