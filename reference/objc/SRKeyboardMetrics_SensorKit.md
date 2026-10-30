# `SRKeyboardMetrics`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `SRSampleExporting`, `SRSampling`, `NSCopying`
- 5 instance variables, 16 properties, 117 instance methods, 2 class methods

## Instance variables

```
@"NSDateInterval" _interval;
@"NSDictionary" _keyboardMetaInformation;
@"NSMutableDictionary" _mutableScalarMetrics;
@"NSMutableDictionary" _mutablePositionalMetrics;
@"NSMutableDictionary" _mutableProbabilityMetrics;
```

## Properties

```
@property (T@"NSDateInterval",&,V_interval) interval;
@property (T@"NSDictionary",C,V_keyboardMetaInformation) keyboardMetaInformation;
@property (T@"NSMutableDictionary",&,V_mutableScalarMetrics) mutableScalarMetrics;
@property (T@"NSMutableDictionary",&,V_mutablePositionalMetrics) mutablePositionalMetrics;
@property (T@"NSMutableDictionary",&,V_mutableProbabilityMetrics) mutableProbabilityMetrics;
@property (Td,R) duration;
@property (T@"NSString",R,C) keyboardIdentifier;
@property (T@"NSString",R,C) version;
@property (T@"NSMeasurement",R) width;
@property (T@"NSMeasurement",R) height;
@property (T@"NSArray",R,C) inputModes;
@property (T@"NSArray",R,C) sessionIdentifiers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRKeyboardMetrics supportsSecureCoding];
+[SRKeyboardMetrics initialize];
```

## Instance methods

```
-[SRKeyboardMetrics setInterval:];
-[SRKeyboardMetrics interval];
-[SRKeyboardMetrics dealloc];
-[SRKeyboardMetrics version];
-[SRKeyboardMetrics typingSpeed];
-[SRKeyboardMetrics duration];
-[SRKeyboardMetrics encodeWithCoder:];
-[SRKeyboardMetrics description];
-[SRKeyboardMetrics initWithCoder:];
-[SRKeyboardMetrics width];
-[SRKeyboardMetrics copyWithZone:];
-[SRKeyboardMetrics isEqual:];
-[SRKeyboardMetrics height];
-[SRKeyboardMetrics dictionaryRepresentation];
-[SRKeyboardMetrics inputModes];
-[SRKeyboardMetrics sessionIdentifiers];
-[SRKeyboardMetrics keyboardIdentifier];
-[SRKeyboardMetrics binarySampleRepresentation];
-[SRKeyboardMetrics initWithBinarySampleRepresentation:metadata:timestamp:];
-[SRKeyboardMetrics sr_dictionaryRepresentation];
-[SRKeyboardMetrics initWithInterval:metaInformation:];
-[SRKeyboardMetrics mutablePositionalMetrics];
-[SRKeyboardMetrics mutableProbabilityMetrics];
-[SRKeyboardMetrics mutableScalarMetrics];
-[SRKeyboardMetrics deleteToCharKey];
-[SRKeyboardMetrics shortWordCharKeyUpErrorDistance];
-[SRKeyboardMetrics spaceToShiftKey];
-[SRKeyboardMetrics totalDeathWords];
-[SRKeyboardMetrics totalPathPauses];
-[SRKeyboardMetrics anyTapToCharKey];
-[SRKeyboardMetrics charKeyToDelete];
-[SRKeyboardMetrics deleteToDeletes];
-[SRKeyboardMetrics emojiCountForSentimentCategory:];
-[SRKeyboardMetrics pathTypingSpeed];
-[SRKeyboardMetrics spaceToSpaceKey];
-[SRKeyboardMetrics totalAngerWords];
-[SRKeyboardMetrics totalPathLength];
-[SRKeyboardMetrics upErrorDistance];
-[SRKeyboardMetrics anyTapToPlaneChangeKey];
-[SRKeyboardMetrics charKeyToAnyTapKey];
-[SRKeyboardMetrics charKeyToPlaneChangeKey];
-[SRKeyboardMetrics charKeyToPrediction];
-[SRKeyboardMetrics charKeyToSpaceKey];
-[SRKeyboardMetrics deleteDownErrorDistance];
-[SRKeyboardMetrics deleteToDelete];
-[SRKeyboardMetrics deleteToPath];
-[SRKeyboardMetrics deleteToPlaneChangeKey];
-[SRKeyboardMetrics deleteToShiftKey];
-[SRKeyboardMetrics deleteToSpaceKey];
-[SRKeyboardMetrics deleteTouchDownUp];
-[SRKeyboardMetrics deleteUpErrorDistance];
-[SRKeyboardMetrics downErrorDistance];
-[SRKeyboardMetrics keyboardMetaInformation];
-[SRKeyboardMetrics longWordDownErrorDistance];
-[SRKeyboardMetrics longWordTouchDownDown];
-[SRKeyboardMetrics longWordTouchDownUp];
-[SRKeyboardMetrics longWordTouchUpDown];
-[SRKeyboardMetrics longWordUpErrorDistance];
-[SRKeyboardMetrics pathErrorDistanceRatio];
-[SRKeyboardMetrics pathToDelete];
-[SRKeyboardMetrics pathToPath];
-[SRKeyboardMetrics pathToSpace];
-[SRKeyboardMetrics planeChangeKeyToCharKey];
-[SRKeyboardMetrics planeChangeToAnyTap];
-[SRKeyboardMetrics positionalMetrics];
-[SRKeyboardMetrics probabilityMetrics];
-[SRKeyboardMetrics scalarMetrics];
-[SRKeyboardMetrics setKeyboardMetaInformation:];
-[SRKeyboardMetrics setMutablePositionalMetrics:];
-[SRKeyboardMetrics setMutableProbabilityMetrics:];
-[SRKeyboardMetrics setMutableScalarMetrics:];
-[SRKeyboardMetrics shortWordCharKeyDownErrorDistance];
-[SRKeyboardMetrics shortWordCharKeyToCharKey];
-[SRKeyboardMetrics shortWordCharKeyTouchDownUp];
-[SRKeyboardMetrics spaceDownErrorDistance];
-[SRKeyboardMetrics spaceToCharKey];
-[SRKeyboardMetrics spaceToDeleteKey];
-[SRKeyboardMetrics spaceToPath];
-[SRKeyboardMetrics spaceToPlaneChangeKey];
-[SRKeyboardMetrics spaceToPredictionKey];
-[SRKeyboardMetrics spaceTouchDownUp];
-[SRKeyboardMetrics spaceUpErrorDistance];
-[SRKeyboardMetrics totalAbsolutistWords];
-[SRKeyboardMetrics totalAlteredWords];
-[SRKeyboardMetrics totalAngerEmojis];
-[SRKeyboardMetrics totalAnxietyEmojis];
-[SRKeyboardMetrics totalAnxietyWords];
-[SRKeyboardMetrics totalAutoCorrections];
-[SRKeyboardMetrics totalConfusedEmojis];
-[SRKeyboardMetrics totalDeletes];
-[SRKeyboardMetrics totalDownWords];
-[SRKeyboardMetrics totalDrags];
-[SRKeyboardMetrics totalEmojis];
-[SRKeyboardMetrics totalHealthFeelingEmojis];
-[SRKeyboardMetrics totalHealthFeelingWords];
-[SRKeyboardMetrics totalHitTestCorrections];
-[SRKeyboardMetrics totalInsertKeyCorrections];
-[SRKeyboardMetrics totalLowEnergyEmojis];
-[SRKeyboardMetrics totalNearKeyCorrections];
-[SRKeyboardMetrics totalPathTime];
-[SRKeyboardMetrics totalPaths];
-[SRKeyboardMetrics totalPauses];
-[SRKeyboardMetrics totalPositiveEmojis];
-[SRKeyboardMetrics totalRetroCorrections];
-[SRKeyboardMetrics totalSadEmojis];
-[SRKeyboardMetrics totalSkipTouchCorrections];
-[SRKeyboardMetrics totalSpaceCorrections];
-[SRKeyboardMetrics totalSubstitutionCorrections];
-[SRKeyboardMetrics totalTaps];
-[SRKeyboardMetrics totalTranspositionCorrections];
-[SRKeyboardMetrics totalTypingDuration];
-[SRKeyboardMetrics totalTypingEpisodes];
-[SRKeyboardMetrics totalWords];
-[SRKeyboardMetrics touchDownDown];
-[SRKeyboardMetrics touchDownUp];
-[SRKeyboardMetrics touchUpDown];
-[SRKeyboardMetrics wordCountForSentimentCategory:];
```
