# `CEKSmartStyle`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKCaptureStyle`
- 5 instance variables, 17 properties, 21 instance methods, 15 class methods

## Instance variables

```
q _presetType;
q _castType;
d _castIntensity;
d _toneBias;
d _colorBias;
```

## Properties

```
@property (Tq,R,N,V_presetType) presetType;
@property (Tq,R,N,V_castType) castType;
@property (Td,R,N,V_castIntensity) castIntensity;
@property (Td,R,N,V_toneBias) toneBias;
@property (Td,R,N,V_colorBias) colorBias;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
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
+[CEKSmartStyle systemStyle];
+[CEKSmartStyle identityStyle];
+[CEKSmartStyle styleWithDictionary:error:];
+[CEKSmartStyle persistenceStringForPresetType:];
+[CEKSmartStyle _indexForPresetString:];
+[CEKSmartStyle canCustomizeCastIntensityForCastType:];
+[CEKSmartStyle castTypeForPresetType:];
+[CEKSmartStyle defaultStylesIncludingSystemStyles:systemStylePlaceholder:creativeStyles:];
+[CEKSmartStyle displayNameForPresetType:];
+[CEKSmartStyle isCustomizablePresetType:];
+[CEKSmartStyle presetTypeFromPersistenceString:success:];
+[CEKSmartStyle thumbnailFilterForCastType:];
+[CEKSmartStyle _getPresetValuesForPresetType:castIntensity:toneBias:colorBias:];
+[CEKSmartStyle thumbnailFilterNameForCastType:];
+[CEKSmartStyle isSystemStyleCastType:];
```

## Instance methods

```
-[CEKSmartStyle castType];
-[CEKSmartStyle colorBias];
-[CEKSmartStyle analyticsDictionaryForPreferences];
-[CEKSmartStyle displayName];
-[CEKSmartStyle presetType];
-[CEKSmartStyle thumbnailFilter];
-[CEKSmartStyle presetDisplayName];
-[CEKSmartStyle isCustomized];
-[CEKSmartStyle isEqualToSmartStyle:];
-[CEKSmartStyle isNeutral];
-[CEKSmartStyle analyticsDictionaryForCapture];
-[CEKSmartStyle hash];
-[CEKSmartStyle isCustomizable];
-[CEKSmartStyle description];
-[CEKSmartStyle castIntensity];
-[CEKSmartStyle initWithPresetType:];
-[CEKSmartStyle initWithPresetType:castIntensity:toneBias:colorBias:];
-[CEKSmartStyle toneBias];
-[CEKSmartStyle isEqual:];
-[CEKSmartStyle _analyticsDictionaryForCapture:];
-[CEKSmartStyle dictionaryRepresentation];
```
