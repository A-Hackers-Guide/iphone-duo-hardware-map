# `PKInk`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 17 instance variables, 23 properties, 95 instance methods, 28 class methods

## Instance variables

```
{shared_ptr<PKProtobufUnknownFields>="__ptr_"^{PKProtobufUnknownFields}"__cntrl_"^{__shared_weak_count}} _unknownFields;
@"PKInk" _cachedInkWithOriginalRequiredContentVersion;
B __weightIsUndefined;
@"NSString" _identifier;
@"UIColor" _sdrColor;
Q _version;
@"NSString" _variant;
d _weight;
d _azimuth;
@"PKInkBehavior" _behavior;
@"UIColor" _hdrColor;
d _hdrHeadroom;
q __requiredContentVersionOverride;
_sixChannelAddColor;
_sixChannelMultiplyColor;
_hdrAddColor;
_hdrMultiplyColor;
```

## Properties

```
@property (T@"NSData",R,N) rawValue;
@property (TQ,R,N) particleRotation;
@property (T@"UIColor",R,N,V_hdrColor) hdrColor;
@property (Td,R,N,V_hdrHeadroom) hdrHeadroom;
@property (T@"UIColor",R,N,V_sdrColor) sdrColor;
@property (T,N,V_sixChannelAddColor) _sixChannelAddColor;
@property (T,N,V_sixChannelMultiplyColor) _sixChannelMultiplyColor;
@property (T,N,V_hdrAddColor) _hdrAddColor;
@property (T,N,V_hdrMultiplyColor) _hdrMultiplyColor;
@property (Tq,N,V__requiredContentVersionOverride) _requiredContentVersionOverride;
@property (TB,N,V__weightIsUndefined) _weightIsUndefined;
@property (T@"PKInkBehavior",&,N,V_behavior) behavior;
@property (TQ,R,N,V_version) version;
@property (Tq,R,N) inkFormatVersion;
@property (T@"NSString",R,N,V_variant) variant;
@property (Td,R,N) _weight;
@property (Td,R,N,V_azimuth) _azimuth;
@property (TB,R,N) _isStrokeGeneratingInk;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (Td,R,N,V_weight) weight;
@property (T@"NSString",R,N) inkType;
@property (T@"UIColor",R,N) color;
@property (Tq,R,N) requiredContentVersion;
```

## Class methods

```
+[PKInk supportsSecureCoding];
+[PKInk inkWithIdentifier:color:weight:];
+[PKInk _clearCachedInks];
+[PKInk colorForLassoStroke];
+[PKInk currentInkVersionForInkIdentifier:];
+[PKInk decodeColorFrom:propertyKey:inkOpacity:];
+[PKInk defaultAzimuthForIdentifier:];
+[PKInk defaultOpacityForIdentifier:];
+[PKInk defaultWeightForIdentifier:];
+[PKInk headroomForCGColor:];
+[PKInk identifierForCommandType:wantsObjectErase:];
+[PKInk identifierForInkType:];
+[PKInk inkFromDictionary:color:identifier:];
+[PKInk inkFromInk:azimuth:];
+[PKInk inkFromInk:color:];
+[PKInk inkFromInk:color:hdrColor:hdrHeadroom:];
+[PKInk inkFromInk:weight:];
+[PKInk inkFromInk:withBehavior:];
+[PKInk inkWithIdentifier:color:];
+[PKInk inkWithIdentifier:color:variant:];
+[PKInk inkWithIdentifier:color:version:variant:];
+[PKInk inkWithIdentifier:color:weight:azimuth:];
+[PKInk inkWithIdentifier:properties:];
+[PKInk inkWithIdentifier:properties:inkVersion:];
+[PKInk inkWithType:color:weight:];
+[PKInk inkWithType:color:weight:azimuth:];
+[PKInk sdrColorFromCGColor:];
+[PKInk sdrInkFromInk:];
```

## Instance methods

```
-[PKInk _shouldSaveHDRMultiplyColor];
-[PKInk _addTestDataToUnknownFields];
-[PKInk _isLassoInk];
-[PKInk initWithInkType:color:];
-[PKInk properties];
-[PKInk _isFountainPenInk];
-[PKInk _copyWithVariant:];
-[PKInk isEqualUnweightedInk:];
-[PKInk _requiredContentVersionOverride];
-[PKInk _isPencilInk];
-[PKInk initWithUncheckedIdentifier:color:hdrColor:hdrHeadroom:version:variant:weight:azimuth:];
-[PKInk identifier];
-[PKInk _setupDefaultSixChannelAddAndMultiplyColors];
-[PKInk _shouldSaveHDRAddColor];
-[PKInk init];
-[PKInk _defaultSixChannelAddColor];
-[PKInk rawValue];
-[PKInk _shouldSaveSixChannelMultiplyColor];
-[PKInk set_weightIsUndefined:];
-[PKInk _supportsCombiningStrokes];
-[PKInk _sixChannelMultiplyColor];
-[PKInk weight];
-[PKInk initWithUncheckedIdentifier:color:version:variant:weight:];
-[PKInk initWithBehavior:color:version:variant:weight:azimuth:];
-[PKInk _requiredContentVersion];
-[PKInk _weightIsUndefined];
-[PKInk initWithIdentifier:color:version:variant:];
-[PKInk _copyWithOriginalRequiredContentVersion];
-[PKInk _weight];
-[PKInk version];
-[PKInk _isCrayonInk];
-[PKInk hdrHeadroom];
-[PKInk requiredContentVersion];
-[PKInk inkFormatVersion];
-[PKInk set_hdrAddColor:];
-[PKInk setWeight:];
-[PKInk set_sixChannelMultiplyColor:];
-[PKInk variantForArchiving];
-[PKInk color];
-[PKInk _defaultHDRMultiplyColor];
-[PKInk _hdrMultiplyColor];
-[PKInk initWithIdentifier:color:version:variant:weight:azimuth:];
-[PKInk inkType];
-[PKInk initWithIdentifier:color:version:variant:weight:];
-[PKInk _azimuth];
-[PKInk setBehavior:];
-[PKInk behavior];
-[PKInk colorForUIAllowHDR:];
-[PKInk initWithArchive:];
-[PKInk _defaultSixChannelMultiplyColor];
-[PKInk _shouldSaveSixChannelAddColor];
-[PKInk set_hdrMultiplyColor:];
-[PKInk _initColor:hdrColor:hdrHeadroom:];
-[PKInk _hdrAddColor];
-[PKInk sdrColor];
-[PKInk _isGenerationTool];
-[PKInk encodeWithCoder:];
-[PKInk _isEraserInk];
-[PKInk _setupCustomizedSixChannelColors];
-[PKInk _isFountainPenInkV2];
-[PKInk _isStrokeGeneratingInk];
-[PKInk hash];
-[PKInk saveToV1Archive:];
-[PKInk _isReedCalligraphyInk];
-[PKInk saveToArchive:];
-[PKInk description];
-[PKInk _isWatercolorInk];
-[PKInk _isPenInk];
-[PKInk isEqualInk:];
-[PKInk _shouldSaveRequiredContentVersionOverride];
-[PKInk initWithCoder:];
-[PKInk set_sixChannelAddColor:];
-[PKInk set_requiredContentVersionOverride:];
-[PKInk hashValueForFloat:];
-[PKInk _isHandwritingInk];
-[PKInk identifierForArchiving];
-[PKInk particleRotation];
-[PKInk hdrColor];
-[PKInk _defaultHDRAddColor];
-[PKInk _isMarkerInk];
-[PKInk _sixChannelVersion];
-[PKInk _sixChannelAddColor];
-[PKInk _isCustomInk];
-[PKInk initWithRawValue:];
-[PKInk copyWithZone:];
-[PKInk _isMonolineInk];
-[PKInk isEqual:];
-[PKInk _shadowModel];
-[PKInk initWithV1Archive:serializationVersion:];
-[PKInk _dataInUnknownFields];
-[PKInk variant];
-[PKInk initWithIdentifier:color:hdrColor:hdrHeadroom:version:variant:weight:azimuth:behavior:];
-[PKInk _setupRequiredContentVersion];
-[PKInk _numPaintFramebuffers];
-[PKInk dictionaryRepresentation];
```
