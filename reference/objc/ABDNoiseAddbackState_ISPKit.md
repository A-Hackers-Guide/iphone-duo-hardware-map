# `ABDNoiseAddbackState`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
f _luxFactor;
f _gainFactor;
f _bias;
@"ABDLookupTable" _luxTable;
@"ABDLookupTable" _gainTable;
```

## Properties

```
@property (T@"ABDLookupTable",&,V_luxTable) luxTable;
@property (T@"ABDLookupTable",&,V_gainTable) gainTable;
@property (Tf,V_luxFactor) luxFactor;
@property (Tf,V_gainFactor) gainFactor;
@property (Tf,V_bias) bias;
```

## Class methods

```
+[ABDNoiseAddbackState createLookupTableFrom:];
+[ABDNoiseAddbackState getFloatValueFrom:at:];
```

## Instance methods

```
-[ABDNoiseAddbackState bias];
-[ABDNoiseAddbackState initFromDictionary:];
-[ABDNoiseAddbackState setBias:];
-[ABDNoiseAddbackState luxTable];
-[ABDNoiseAddbackState gainFactor];
-[ABDNoiseAddbackState gainTable];
-[ABDNoiseAddbackState getValueForLux:andGain:];
-[ABDNoiseAddbackState initFromOther:];
-[ABDNoiseAddbackState luxFactor];
-[ABDNoiseAddbackState setGainFactor:];
-[ABDNoiseAddbackState setGainTable:];
-[ABDNoiseAddbackState setLuxFactor:];
-[ABDNoiseAddbackState setLuxTable:];
```
