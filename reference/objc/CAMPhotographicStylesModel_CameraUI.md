# `CAMPhotographicStylesModel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
Q _selectedIndex;
Q _systemStyleIndex;
@"CEKSmartStyle" _systemSmartStyle;
@"CEKTextureStyle" _systemTextureStyle;
@"NSMutableArray" __smartStyles;
@"NSMutableArray" __textureStyles;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V__smartStyles) _smartStyles;
@property (T@"NSMutableArray",&,N,V__textureStyles) _textureStyles;
@property (Tq,N) selectedPreset;
@property (Tq,N) systemStylePreset;
@property (TQ,N,V_selectedIndex) selectedIndex;
@property (TQ,N,V_systemStyleIndex) systemStyleIndex;
@property (T@"CEKSmartStyle",R,N,V_systemSmartStyle) systemSmartStyle;
@property (T@"NSArray",R,C,N) smartStylesSnapshot;
@property (T@"CEKTextureStyle",R,N,V_systemTextureStyle) systemTextureStyle;
@property (T@"NSArray",R,C,N) textureStylesSnapshot;
```

## Instance methods

```
-[CAMPhotographicStylesModel currentPhotographicStyleForSupport:];
-[CAMPhotographicStylesModel setSystemStyleIndex:];
-[CAMPhotographicStylesModel currentTextureStyleReferenceForSupport:];
-[CAMPhotographicStylesModel _smartStyles];
-[CAMPhotographicStylesModel selectedIndex];
-[CAMPhotographicStylesModel updateCurrentTextureStyle:forSupport:];
-[CAMPhotographicStylesModel systemTextureStyle];
-[CAMPhotographicStylesModel set_smartStyles:];
-[CAMPhotographicStylesModel availableStylePresetsForSupport:];
-[CAMPhotographicStylesModel updateCurrentSmartStyle:forSupport:];
-[CAMPhotographicStylesModel _textureStyles];
-[CAMPhotographicStylesModel systemStylePreset];
-[CAMPhotographicStylesModel _resolvedTypeForCurrentStyleWithSupport:];
-[CAMPhotographicStylesModel _textureStyleForResolvedType:];
-[CAMPhotographicStylesModel currentTextureStyleReferenceForSupport:texturePreset:];
-[CAMPhotographicStylesModel systemSmartStyle];
-[CAMPhotographicStylesModel setSystemStylePreset:];
-[CAMPhotographicStylesModel systemStyleIndex];
-[CAMPhotographicStylesModel currentSmartStyleReferenceForSupport:];
-[CAMPhotographicStylesModel initWithSmartStyles:textureStyles:selectedIndex:systemStyleIndex:systemSmartStyle:systemTextureStyle:];
-[CAMPhotographicStylesModel _smartStyleForResolvedType:];
-[CAMPhotographicStylesModel smartStylesSnapshot];
-[CAMPhotographicStylesModel setSelectedPreset:];
-[CAMPhotographicStylesModel setSelectedIndex:];
-[CAMPhotographicStylesModel currentSmartStyleForSupport:];
-[CAMPhotographicStylesModel copyWithZone:];
-[CAMPhotographicStylesModel set_textureStyles:];
-[CAMPhotographicStylesModel textureStylesSnapshot];
-[CAMPhotographicStylesModel selectedPreset];
-[CAMPhotographicStylesModel currentTextureStyleForSupport:];
```
