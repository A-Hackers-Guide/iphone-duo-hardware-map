# `CAMPhotographicStyle`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 6 properties, 14 instance methods, 8 class methods

## Instance variables

```
@"CEKSmartStyle" _smartStyle;
@"CEKTextureStyle" _textureStyle;
```

## Properties

```
@property (Tq,R,N) presetType;
@property (T@"NSString",R,C,N) displayName;
@property (TB,R,N,GisCustomized) customized;
@property (T@"CEKSmartStyle",R,N,V_smartStyle) smartStyle;
@property (T@"CEKTextureStyle",R,N,V_textureStyle) textureStyle;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
```

## Class methods

```
+[CAMPhotographicStyle identityStyle];
+[CAMPhotographicStyle styleWithDictionary:error:];
+[CAMPhotographicStyle _cekTextureStylePresetForCMIPresetName:];
+[CAMPhotographicStyle _cmiCastTypeForPresetType:];
+[CAMPhotographicStyle defaultPhotographicStyleForPresetType:];
+[CAMPhotographicStyle defaultStylesIncludingSystemStyles:systemStylePlaceholder:creativeStyles:];
+[CAMPhotographicStyle defaultTextureStyleForPresetType:];
+[CAMPhotographicStyle defaultTextureStyleForPresetType:texturePreset:];
```

## Instance methods

```
-[CAMPhotographicStyle textureStyle];
-[CAMPhotographicStyle smartStyle];
-[CAMPhotographicStyle displayName];
-[CAMPhotographicStyle presetType];
-[CAMPhotographicStyle isCustomized];
-[CAMPhotographicStyle hash];
-[CAMPhotographicStyle description];
-[CAMPhotographicStyle isEqual:];
-[CAMPhotographicStyle dictionaryRepresentation];
-[CAMPhotographicStyle _isDefaultTextureStyle];
-[CAMPhotographicStyle initWithSmartStyle:textureStyle:];
-[CAMPhotographicStyle isEqualToPhotographicStyle:];
-[CAMPhotographicStyle photographicStyleByUpdatingSmartStyle:];
-[CAMPhotographicStyle photographicStyleByUpdatingTextureStyle:];
```
