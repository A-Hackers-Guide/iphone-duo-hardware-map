# `EspressoProfilingLayerSupportInfo`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _supported;
B _exists;
B _has_perf_warning;
B _internal_layer;
@"NSArray" _error_public;
@"NSArray" _error_private;
@"NSString" _type;
```

## Properties

```
@property (T@"NSArray",&,V_error_public) error_public;
@property (T@"NSArray",&,V_error_private) error_private;
@property (TB,V_supported) supported;
@property (TB,V_exists) exists;
@property (TB,V_has_perf_warning) has_perf_warning;
@property (TB,V_internal_layer) internal_layer;
@property (T@"NSString",&,V_type) type;
```

## Instance methods

```
-[EspressoProfilingLayerSupportInfo supported];
-[EspressoProfilingLayerSupportInfo exists];
-[EspressoProfilingLayerSupportInfo setSupported:];
-[EspressoProfilingLayerSupportInfo setExists:];
-[EspressoProfilingLayerSupportInfo setType:];
-[EspressoProfilingLayerSupportInfo type];
-[EspressoProfilingLayerSupportInfo error_private];
-[EspressoProfilingLayerSupportInfo error_public];
-[EspressoProfilingLayerSupportInfo has_perf_warning];
-[EspressoProfilingLayerSupportInfo internal_layer];
-[EspressoProfilingLayerSupportInfo setError_private:];
-[EspressoProfilingLayerSupportInfo setError_public:];
-[EspressoProfilingLayerSupportInfo setHas_perf_warning:];
-[EspressoProfilingLayerSupportInfo setInternal_layer:];
```
