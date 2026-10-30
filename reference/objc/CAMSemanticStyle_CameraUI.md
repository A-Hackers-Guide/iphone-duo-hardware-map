# `CAMSemanticStyle`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKCaptureStyle`
- 3 instance variables, 17 properties, 20 instance methods, 7 class methods

## Instance variables

```
d _sceneBias;
d _warmthBias;
q _presetType;
```

## Properties

```
@property (Td,R,N,V_sceneBias) sceneBias;
@property (Td,R,N,V_warmthBias) warmthBias;
@property (Tq,R,N,V_presetType) presetType;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
@property (Tq,R,N) makerPreset;
@property (T@"AVSemanticStyle",R,N) avSemanticStyle;
@property (TB,R,N,GisNeutral) neutral;
@property (TB,R,N,GisCustomizable) customizable;
@property (TB,R,N,GisCustomized) customized;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) presetDisplayName;
@property (T@"NSDictionary",R,N) analyticsDictionaryForCapture;
@property (T@"NSDictionary",R,N) analyticsDictionaryForPreferences;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMSemanticStyle standardStyle];
+[CAMSemanticStyle defaultStyles];
+[CAMSemanticStyle styleWithDictionary:error:];
+[CAMSemanticStyle persistenceStringForPresetType:];
+[CAMSemanticStyle _indexForPresetString:];
+[CAMSemanticStyle getSceneBias:warmthBias:forPresetType:];
+[CAMSemanticStyle isCustomizablePresetType:];
```

## Instance methods

```
-[CAMSemanticStyle analyticsDictionaryForPreferences];
-[CAMSemanticStyle displayName];
-[CAMSemanticStyle presetType];
-[CAMSemanticStyle presetDisplayName];
-[CAMSemanticStyle isCustomized];
-[CAMSemanticStyle isNeutral];
-[CAMSemanticStyle analyticsDictionaryForCapture];
-[CAMSemanticStyle isCustomizable];
-[CAMSemanticStyle description];
-[CAMSemanticStyle initWithPresetType:];
-[CAMSemanticStyle isEqual:];
-[CAMSemanticStyle _analyticsDictionaryForCapture:];
-[CAMSemanticStyle dictionaryRepresentation];
-[CAMSemanticStyle sceneBias];
-[CAMSemanticStyle warmthBias];
-[CAMSemanticStyle avSemanticStyle];
-[CAMSemanticStyle _makerPresetWithSceneBias:warmthBias:];
-[CAMSemanticStyle initWithPresetType:sceneBias:warmthBias:];
-[CAMSemanticStyle isEqualToSemanticStyle:];
-[CAMSemanticStyle makerPreset];
```
