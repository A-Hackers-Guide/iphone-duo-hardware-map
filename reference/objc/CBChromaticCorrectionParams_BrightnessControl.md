# `CBChromaticCorrectionParams`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBChromaticCorectionParamsProtocol`, `CBSerializable`
- 23 instance variables, 18 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _log;
Q _luxTableSizeOG;
^f _luxTableOG;
Q _nitsTableSizeOG;
^f _nitsTableOG;
Q _strengthTableSizeOG;
^f _strengthTableOG;
f _rampUpdateRateOG;
^f _rampBezierAnchorsOG;
f _rampUpDuration;
f _rampDownDuration;
f _rampUpLuxDeltaThreshold;
f _rampDownLuxDeltaThreshold;
f _aodRampDuration;
f _rampUpdateRate;
f _luxActivationThreshold;
f _nitsActivationThreshold;
I _supported;
@"NSDictionary" _codingKeys;
@"NSArray" _luxTable;
@"NSArray" _nitsTable;
@"NSArray" _strengthTable;
@"NSArray" _rampBezierAnchors;
```

## Properties

```
@property (T@"NSArray",R,V_luxTable) luxTable;
@property (T@"NSArray",R,V_nitsTable) nitsTable;
@property (T@"NSArray",R,V_strengthTable) strengthTable;
@property (T@"NSArray",R,V_rampBezierAnchors) rampBezierAnchors;
@property (Tf,R,V_luxActivationThreshold) luxActivationThreshold;
@property (Tf,R,V_nitsActivationThreshold) nitsActivationThreshold;
@property (Tf,R,V_rampUpdateRate) rampUpdateRate;
@property (Tf,R,V_rampUpDuration) rampUpDuration;
@property (Tf,R,V_rampUpLuxDeltaThreshold) rampUpLuxDeltaThreshold;
@property (Tf,R,V_rampDownDuration) rampDownDuration;
@property (Tf,R,V_rampDownLuxDeltaThreshold) rampDownLuxDeltaThreshold;
@property (Tf,R,V_aodRampDuration) aodRampDuration;
@property (TI,R,V_supported) supported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,V_codingKeys) codingKeys;
```

## Instance methods

```
-[CBChromaticCorrectionParams supported];
-[CBChromaticCorrectionParams dealloc];
-[CBChromaticCorrectionParams luxActivationThreshold];
-[CBChromaticCorrectionParams nitsTable];
-[CBChromaticCorrectionParams rampUpDuration];
-[CBChromaticCorrectionParams aodRampDuration];
-[CBChromaticCorrectionParams codingKeys];
-[CBChromaticCorrectionParams getStrengthForRow:andColumn:];
-[CBChromaticCorrectionParams initBezierWithPrefix:fromParser:];
-[CBChromaticCorrectionParams initCommonWithPrefix:fromParser:];
-[CBChromaticCorrectionParams initFromParserOG:withName:andPrefix:];
-[CBChromaticCorrectionParams initTablesWithPrefix:fromParser:];
-[CBChromaticCorrectionParams initWithProvider:withName:andPrefix:];
-[CBChromaticCorrectionParams luxTable];
-[CBChromaticCorrectionParams nitsActivationThreshold];
-[CBChromaticCorrectionParams rampBezierAnchors];
-[CBChromaticCorrectionParams rampDownDuration];
-[CBChromaticCorrectionParams rampDownLuxDeltaThreshold];
-[CBChromaticCorrectionParams rampUpLuxDeltaThreshold];
-[CBChromaticCorrectionParams rampUpdateRate];
-[CBChromaticCorrectionParams strengthTable];
```
