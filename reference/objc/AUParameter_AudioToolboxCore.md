# `AUParameter`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUParameterNode`
- Protocols: `NSSecureCoding`
- 7 instance variables, 10 properties, 35 instance methods, 1 class methods

## Instance variables

```
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _localValueStale;
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _numUIObservers;
{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}} _numRecordingObservers;
f _value;
Q _address;
@"NSArray" _dependentParameters;
@"_AUStaticParameterInfo" _info;
```

## Properties

```
@property (TQ,N,V_address) address;
@property (T@"_AUStaticParameterInfo",&,N,V_info) info;
@property (Tf,R,N) minValue;
@property (Tf,R,N) maxValue;
@property (TI,R,N) unit;
@property (T@"NSString",R,C,N) unitName;
@property (TI,R,N) flags;
@property (T@"NSArray",R,C,N) valueStrings;
@property (T@"NSArray",R,C,N,V_dependentParameters) dependentParameters;
@property (Tf,N,V_value) value;
```

## Class methods

```
+[AUParameter supportsSecureCoding];
```

## Instance methods

```
-[AUParameter stringFromValue:];
-[AUParameter address];
-[AUParameter minValue];
-[AUParameter maxValue];
-[AUParameter set_originalOrder:];
-[AUParameter set_defaultValue:];
-[AUParameter unit];
-[AUParameter _clumpID];
-[AUParameter setAddress:];
-[AUParameter info];
-[AUParameter flags];
-[AUParameter setInfo:];
-[AUParameter _defaultValue];
-[AUParameter initWithID:name:address:min:max:unit:unitName:flags:valueStrings:dependentParameters:];
-[AUParameter dealloc];
-[AUParameter value];
-[AUParameter unitName];
-[AUParameter valueFromString:];
-[AUParameter _originalOrder];
-[AUParameter copyNodeWithOffset:];
-[AUParameter set_clumpID:];
-[AUParameter _observersChanged:deltaCount:];
-[AUParameter valueStrings];
-[AUParameter setValue:originator:atHostTime:eventType:];
-[AUParameter setValue:originator:];
-[AUParameter setValue:];
-[AUParameter setLocalValueStale:];
-[AUParameter encodeWithCoder:];
-[AUParameter localValueStale];
-[AUParameter description];
-[AUParameter _internalValue];
-[AUParameter initWithCoder:];
-[AUParameter setValue:originator:atHostTime:];
-[AUParameter setValue:extOriginator:atHostTime:eventType:];
-[AUParameter dependentParameters];
```
