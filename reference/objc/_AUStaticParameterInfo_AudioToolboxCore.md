# `_AUStaticParameterInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
f _minValue;
f _maxValue;
I _unit;
I _flags;
I _clumpID;
f _defaultValue;
I _originalOrder;
@"NSString" _unitName;
@"NSArray" _valueStrings;
```

## Properties

```
@property (Tf,N,V_minValue) minValue;
@property (Tf,N,V_maxValue) maxValue;
@property (TI,N,V_unit) unit;
@property (T@"NSString",&,N,V_unitName) unitName;
@property (TI,N,V_flags) flags;
@property (T@"NSArray",&,N,V_valueStrings) valueStrings;
@property (TI,N,V_clumpID) clumpID;
@property (Tf,N,V_defaultValue) defaultValue;
@property (TI,N,V_originalOrder) originalOrder;
```

## Class methods

```
+[_AUStaticParameterInfo supportsSecureCoding];
```

## Instance methods

```
-[_AUStaticParameterInfo setDefaultValue:];
-[_AUStaticParameterInfo setUnit:];
-[_AUStaticParameterInfo setOriginalOrder:];
-[_AUStaticParameterInfo minValue];
-[_AUStaticParameterInfo maxValue];
-[_AUStaticParameterInfo unit];
-[_AUStaticParameterInfo originalOrder];
-[_AUStaticParameterInfo setFlags:];
-[_AUStaticParameterInfo flags];
-[_AUStaticParameterInfo defaultValue];
-[_AUStaticParameterInfo dealloc];
-[_AUStaticParameterInfo unitName];
-[_AUStaticParameterInfo setUnitName:];
-[_AUStaticParameterInfo setClumpID:];
-[_AUStaticParameterInfo valueStrings];
-[_AUStaticParameterInfo setValueStrings:];
-[_AUStaticParameterInfo encodeWithCoder:];
-[_AUStaticParameterInfo setMaxValue:];
-[_AUStaticParameterInfo initWithCoder:];
-[_AUStaticParameterInfo clumpID];
-[_AUStaticParameterInfo setMinValue:];
```
