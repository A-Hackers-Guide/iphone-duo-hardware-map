# `CBBacklightNode`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPrimitiveConfigurationProvider`, `CBBacklightConfigurationProvider`
- 4 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"<CBPrimitiveConfigurationProvider>" _parser;
@"NSDictionary" _capabilities;
@"<CBPrimitiveConfigurationProvider>" _combinedProvider;
@"NSObject<OS_os_log>" _logHandle;
```

## Properties

```
@property (T@"NSObject<OS_os_log>",&,V_logHandle) logHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBBacklightNode logHandle];
-[CBBacklightNode dealloc];
-[CBBacklightNode forwardingTargetForSelector:];
-[CBBacklightNode setLogHandle:];
-[CBBacklightNode initWithService:];
-[CBBacklightNode initWithParser:];
-[CBBacklightNode initWithParser:andCapabilities:];
-[CBBacklightNode copyAABCapDictionary];
-[CBBacklightNode copyAABConstraintDictionary];
-[CBBacklightNode copyMarketingTable];
-[CBBacklightNode copyRestrictionDictionary];
-[CBBacklightNode copyRestrictionDictionaryMultiPoint];
-[CBBacklightNode copyRestrictionDictionarySinglePoint];
-[CBBacklightNode copyTrueToneStrength];
-[CBBacklightNode createMultipointArrayCommon:unitSize:outputCount:];
-[CBBacklightNode createMultipointRestrictionArrayForThresholdsName:andFactorsName:andThresholds:andFactors:];
-[CBBacklightNode getBacklightCalibration:];
-[CBBacklightNode getBacklightCalibrationParser:];
-[CBBacklightNode getCPMSUseModernOverride:];
-[CBBacklightNode getGlobalScalarDisplayI:andB:];
-[CBBacklightNode getGlobalScalarTo:];
-[CBBacklightNode getRingLightSupport:forDisplayPreferences:];
-[CBBacklightNode initWithService:andCapabilities:];
-[CBBacklightNode newMultiPointFactorsArray:];
-[CBBacklightNode newMultiPointThresholdsArray:];
```
