# `CEKTextureStyle`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 15 instance methods, 10 class methods

## Instance variables

```
q _preset;
d _intensity;
d _grain;
```

## Properties

```
@property (Tq,R,N,V_preset) preset;
@property (Td,R,N,V_intensity) intensity;
@property (Td,R,N,V_grain) grain;
@property (TB,R,N,GisCustomizable) customizable;
@property (TB,R,N,GisCustomized) customized;
```

## Class methods

```
+[CEKTextureStyle defaultStyles];
+[CEKTextureStyle identityStyle];
+[CEKTextureStyle _indexForPresetString:];
+[CEKTextureStyle presetFromPersistenceString:success:];
+[CEKTextureStyle styleWithDictionary:referenceStyle:error:];
+[CEKTextureStyle canCustomizeIntensityForPreset:];
+[CEKTextureStyle _cmiPresetNameForPreset:];
+[CEKTextureStyle _defaultValuesForPreset:intensity:grain:];
+[CEKTextureStyle canCustomizeGrainForPreset:];
+[CEKTextureStyle persistenceStringForPreset:];
```

## Instance methods

```
-[CEKTextureStyle intensity];
-[CEKTextureStyle preset];
-[CEKTextureStyle initWithPreset:];
-[CEKTextureStyle analyticsDictionaryForPreferences];
-[CEKTextureStyle isCustomized];
-[CEKTextureStyle analyticsDictionaryForCapture];
-[CEKTextureStyle hash];
-[CEKTextureStyle isCustomizable];
-[CEKTextureStyle description];
-[CEKTextureStyle isEqual:];
-[CEKTextureStyle grain];
-[CEKTextureStyle initWithPreset:intensity:grain:];
-[CEKTextureStyle dictionaryRepresentationUsingReferenceStyle:];
-[CEKTextureStyle isEqualToTextureStyle:];
-[CEKTextureStyle _analyticsDictionary];
```
