# `EspressoProfilingLayerInfo`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
i _selected_runtime_engine;
@"NSString" _name;
@"NSString" _debug_name;
@"EspressoProfilingLayerSupportInfo" _main_engine_support;
@"NSDictionary" _per_platform_support;
@"NSArray" _runtimes;
d _average_runtime;
```

## Properties

```
@property (T@"NSString",&,V_name) name;
@property (T@"NSString",&,V_debug_name) debug_name;
@property (Ti,V_selected_runtime_engine) selected_runtime_engine;
@property (T@"EspressoProfilingLayerSupportInfo",&,V_main_engine_support) main_engine_support;
@property (T@"NSDictionary",&,V_per_platform_support) per_platform_support;
@property (T@"NSArray",&,V_runtimes) runtimes;
@property (Td,V_average_runtime) average_runtime;
```

## Instance methods

```
-[EspressoProfilingLayerInfo setName:];
-[EspressoProfilingLayerInfo name];
-[EspressoProfilingLayerInfo average_runtime];
-[EspressoProfilingLayerInfo debug_name];
-[EspressoProfilingLayerInfo main_engine_support];
-[EspressoProfilingLayerInfo per_platform_support];
-[EspressoProfilingLayerInfo runtimes];
-[EspressoProfilingLayerInfo selected_runtime_engine];
-[EspressoProfilingLayerInfo setAverage_runtime:];
-[EspressoProfilingLayerInfo setDebug_name:];
-[EspressoProfilingLayerInfo setMain_engine_support:];
-[EspressoProfilingLayerInfo setPer_platform_support:];
-[EspressoProfilingLayerInfo setRuntimes:];
-[EspressoProfilingLayerInfo setSelected_runtime_engine:];
```
