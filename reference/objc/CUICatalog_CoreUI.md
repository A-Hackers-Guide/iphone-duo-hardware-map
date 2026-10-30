# `CUICatalog`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 1 properties, 167 instance methods, 10 class methods

## Instance variables

```
Q _storageRef;
@"NSMapTable" _storageMapTable;
@"NSBundle" _bundle;
@"NSString" _assetStoreName;
@"NSCache" _lookupCache;
@"NSCache" _negativeCache;
@"NSCache" _localObjectCache;
@"NSDictionary" _vibrantColorMatrixTints;
@"NSArray" _assetCatalogLocalizations;
S _preferredLocalization;
b1 _purgeWhenFinished;
b2 _fileHasDisplayGamutInKeySpace;
b1 _skipLocalCaches;
b27 _reserved;
```

## Properties

```
@property (TQ,N,V_storageRef) storageRef;
```

## Class methods

```
+[CUICatalog bestMatchUsingImages:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:];
+[CUICatalog defaultUICatalogForBundle:];
+[CUICatalog bestMatchUsingImages:scaleFactor:deviceIdiom:deviceSubtype:];
+[CUICatalog bestMatchUsingImages:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
+[CUICatalog bestMatchUsingImages:scaleFactor:deviceIdiom:displayGamut:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
+[CUICatalog bestMatchUsingObjects:getAttributeValueUsing:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:deploymentTarget:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsFeatureSetClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
+[CUICatalog bestMatchUsingObjects:getAttributeValueUsing:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:deploymentTarget:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsFeatureSetClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:platform:];
+[CUICatalog isValidAssetStorageWithURL:];
+[CUICatalog isValidLCRWithBytes:length:];
+[CUICatalog newColorByAdjustingLightnessOfColor:darker:];
```

## Instance methods

```
-[CUICatalog imagesWithName:];
-[CUICatalog debugDescription];
-[CUICatalog init];
-[CUICatalog platform];
-[CUICatalog dealloc];
-[CUICatalog allImageNames];
-[CUICatalog containsLookupForName:];
-[CUICatalog initWithName:fromBundle:error:];
-[CUICatalog initWithURL:error:];
-[CUICatalog _storageRefForRendition:representsODRContent:];
-[CUICatalog _baseImageKeyForName:];
-[CUICatalog _baseKeyForName:];
-[CUICatalog appearanceNames];
-[CUICatalog clearCachedImageResources];
-[CUICatalog colorWithName:displayGamut:deviceIdiom:];
-[CUICatalog colorWithName:displayGamut:deviceIdiom:appearanceName:];
-[CUICatalog dataForVectorGlyphsWithNames:];
-[CUICatalog dataWithName:];
-[CUICatalog defaultLayerStackWithScaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog hasStylePresetWithName:];
-[CUICatalog imageByStylingImage:stylePresetName:styleConfiguration:foregroundColor:scale:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:];
-[CUICatalog initWithBytes:length:error:];
-[CUICatalog namedLookupWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:locale:];
-[CUICatalog namedVectorGlyphWithName:scaleFactor:deviceIdiom:layoutDirection:glyphSize:glyphWeight:glyphPointSize:appearanceName:locale:];
-[CUICatalog namedVectorImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:locale:];
-[CUICatalog styledInsetsForStylePresetName:styleConfiguration:foregroundColor:scale:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:locale:];
-[CUICatalog namedVectorGlyphWithName:scaleFactor:deviceIdiom:layoutDirection:glyphContinuousSize:glyphContinuousWeight:glyphPointSize:appearanceName:locale:];
-[CUICatalog namedVectorImageWithName:scaleFactor:displayGamut:layoutDirection:appearanceName:locale:];
-[CUICatalog drawGlyphs:atPositions:inContext:withFont:count:stylePresetName:styleConfiguration:foregroundColor:];
-[CUICatalog namedVectorGlyphWithName:scaleFactor:deviceIdiom:layoutDirection:glyphSize:glyphWeight:glyphPointSize:appearanceName:];
-[CUICatalog _sharedSetup];
-[CUICatalog namedTextureWithName:scaleFactor:];
-[CUICatalog _modelWithName:];
-[CUICatalog layerStackWithName:scaleFactor:];
-[CUICatalog _nameForLocalizationIdentifier:];
-[CUICatalog textStyleWithName:displayGamut:];
-[CUICatalog _appearancefallback_colorWithName:displayGamut:deviceIdiom:appearanceName:];
-[CUICatalog _appearancefallback_gradientWithName:displayGamut:deviceIdiom:appearanceName:];
-[CUICatalog _baseAtlasContentsKeyForName:];
-[CUICatalog _baseAtlasKeyForName:];
-[CUICatalog _baseColorKeyForName:];
-[CUICatalog _baseGradientKeyForName:];
-[CUICatalog _baseLayeredIconKeyForName:];
-[CUICatalog _baseModelForKeyForName:];
-[CUICatalog _baseMultisizeImageSetKeyForName:];
-[CUICatalog _baseRecognitionGroupImageSetKeyForName:];
-[CUICatalog _baseRecognitionObjectKeyForName:];
-[CUICatalog _baseStackKeyForName:];
-[CUICatalog _baseTextureKeyForName:];
-[CUICatalog _baseVectorGlyphForName:];
-[CUICatalog _baseVectorRenditionKey:];
-[CUICatalog _dataWithName:deviceIdiom:deviceSubtype:memoryClass:graphicsClass:appearanceIdentifier:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog _defaultAssetRenditionKey:];
-[CUICatalog _defaultBaseLayeredIconKeyForName:];
-[CUICatalog _defaultLayerStackWithScaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog _defaultNamedAssetWithScaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog _doStyledQuartzDrawingInContext:inBounds:stylePresetName:styleConfiguration:drawingHandler:];
-[CUICatalog _effectStyle:state:presentationState:value:resolution:dimension1:appearance:fromStyleConfiguration:];
-[CUICatalog _imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:appearanceIdentifier:graphicsFallBackOrder:deviceSubtypeFallBackOrder:locale:];
-[CUICatalog _layerStackWithName:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog _nameForAppearanceIdentifier:];
-[CUICatalog _namedImageAtlasWithName:scaleFactor:deviceIdiom:displayGamut:deviceSubtype:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog _namedLookupWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:locale:];
-[CUICatalog _namedTextureWithName:scaleFactor:appearanceName:];
-[CUICatalog _namedTextureWithName:scaleFactor:displayGamut:appearanceName:];
-[CUICatalog _namedVectorImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceIdentifier:locale:];
-[CUICatalog _recognitionImageWithName:];
-[CUICatalog _recognitionObjectWithName:];
-[CUICatalog _resolveInterpolationSourceRenditionKeysUltralight:regular:black:forName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:appearanceIdentifier:locale:];
-[CUICatalog _resolvedRenditionKeyForName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:locale:withBaseKeySelector:adjustRenditionKeyWithBlock:];
-[CUICatalog _resolvedRenditionKeyFromThemeRef:withBaseKey:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:locale:adjustRenditionKeyWithBlock:];
-[CUICatalog _resourceUnPinnedNotification:];
-[CUICatalog _setPreferredLocalization:];
-[CUICatalog _themeRef];
-[CUICatalog _themeStore];
-[CUICatalog _vibrantColorMatrixBrightnessSaturationForColor:saturation:brightness:];
-[CUICatalog blendModeForStylePresetWithName:styleConfiguration:];
-[CUICatalog canGetShapeEffectRenditionWithKey:];
-[CUICatalog colorWithName:displayGamut:];
-[CUICatalog colorWithName:displayGamut:appearanceName:];
-[CUICatalog compositingFilterForStylePresetWithName:styleConfiguration:];
-[CUICatalog compositingFilterForStylePresetWithName:styleConfiguration:foregroundColor:];
-[CUICatalog copiedVectorGlyphsWithNames:outputFile:];
-[CUICatalog copyVectorGlyphsWithNames:toFile:];
-[CUICatalog dataWithName:appearanceName:];
-[CUICatalog dataWithName:deviceIdiom:deviceSubtype:memoryClass:graphicsClass:appearanceIdentifier:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog dataWithName:deviceIdiom:deviceSubtype:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog defaultIconLayerStack];
-[CUICatalog defaultNamedAssetWithScaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog enumerateNamedLookupsUsingBlock:];
-[CUICatalog equivalentForegroundColorForStylePresetWithName:styleConfiguration:];
-[CUICatalog equivalentForegroundColorForStylePresetWithName:styleConfiguration:baseForegroundColor:];
-[CUICatalog fillStyledPath:inContext:stylePresetName:styleConfiguration:];
-[CUICatalog fillStyledRect:inContext:stylePresetName:styleConfiguration:];
-[CUICatalog finalizeNamedVectorGlyphLookupWithResult:name:glyphContinuousSize:glyphContinuousWeight:pointSize:];
-[CUICatalog gradientWithName:displayGamut:deviceIdiom:appearanceName:];
-[CUICatalog hasStylePresetWithName:styleConfiguration:];
-[CUICatalog iconImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:desiredSize:];
-[CUICatalog iconImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:desiredSize:appearanceName:];
-[CUICatalog iconImageWithName:scaleFactor:displayGamut:layoutDirection:desiredSize:];
-[CUICatalog iconImageWithName:scaleFactor:displayGamut:layoutDirection:desiredSize:appearanceName:];
-[CUICatalog iconLayerStackWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:appearanceName:locale:];
-[CUICatalog imageExistsWithName:];
-[CUICatalog imageExistsWithName:scaleFactor:];
-[CUICatalog imageWithName:scaleFactor:];
-[CUICatalog imageWithName:scaleFactor:appearanceName:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:appearanceName:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:appearanceName:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:appearanceIdentifier:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:appearanceIdentifier:graphicsFallBackOrder:deviceSubtypeFallBackOrder:locale:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:appearanceName:];
-[CUICatalog imageWithName:scaleFactor:deviceIdiom:layoutDirection:locale:adjustRenditionKeyWithBlock:];
-[CUICatalog imageWithName:scaleFactor:displayGamut:layoutDirection:];
-[CUICatalog imageWithName:scaleFactor:displayGamut:layoutDirection:appearanceName:];
-[CUICatalog imageWithName:scaleFactor:displayGamut:layoutDirection:appearanceName:locale:];
-[CUICatalog imageWithName:scaleFactor:locale:];
-[CUICatalog initWithName:fromBundle:];
-[CUICatalog layerStackWithName:];
-[CUICatalog layerStackWithName:scaleFactor:deviceIdiom:];
-[CUICatalog layerStackWithName:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog localObjectCache];
-[CUICatalog lookupCache];
-[CUICatalog modelWithName:];
-[CUICatalog namedImageAtlasWithName:scaleFactor:];
-[CUICatalog namedImageAtlasWithName:scaleFactor:deviceIdiom:];
-[CUICatalog namedImageAtlasWithName:scaleFactor:deviceIdiom:displayGamut:deviceSubtype:memoryClass:graphicsClass:graphicsFallBackOrder:deviceSubtypeFallBackOrder:];
-[CUICatalog namedImageAtlasWithName:scaleFactor:displayGamut:];
-[CUICatalog namedLookupWithName:scaleFactor:];
-[CUICatalog namedLookupWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog namedLookupWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:];
-[CUICatalog namedLookupWithName:scaleFactor:deviceIdiom:deviceSubtype:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog namedRecognitionGroupWithName:];
-[CUICatalog namedTextureWithName:scaleFactor:appearanceName:];
-[CUICatalog namedTextureWithName:scaleFactor:displayGamut:];
-[CUICatalog namedTextureWithName:scaleFactor:displayGamut:appearanceName:];
-[CUICatalog namedVectorGlyphWithName:scaleFactor:deviceIdiom:glyphSize:glyphWeight:glyphPointSize:appearanceName:];
-[CUICatalog namedVectorImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog namedVectorImageWithName:scaleFactor:deviceIdiom:deviceSubtype:displayGamut:layoutDirection:sizeClassHorizontal:sizeClassVertical:appearanceName:];
-[CUICatalog namedVectorImageWithName:scaleFactor:displayGamut:layoutDirection:];
-[CUICatalog namedVectorImageWithName:scaleFactor:displayGamut:layoutDirection:appearanceName:];
-[CUICatalog negativeCache];
-[CUICatalog newShapeEffectPresetForStylePresetName:styleConfiguration:];
-[CUICatalog newShapeEffectPresetWithRenditionKey:];
-[CUICatalog newShapeEffectStackForStylePresetName:styleConfiguration:foregroundColor:];
-[CUICatalog newTextEffectStackForStylePresetName:styleConfiguration:foregroundColor:];
-[CUICatalog parentNamedImageAtlasForImageNamed:scaleFactor:displayGamut:];
-[CUICatalog parentNamedImageAtlastForImageNamed:scaleFactor:];
-[CUICatalog pdfDocumentWithName:];
-[CUICatalog pdfDocumentWithName:appearanceName:];
-[CUICatalog preloadNamedAtlasWithScaleFactor:andNames:completionHandler:];
-[CUICatalog renditionKeyForShapeEffectPresetForStylePresetName:styleConfiguration:];
-[CUICatalog renditionKeyForShapeEffectPresetWithStyleID:state:presentationState:value:resolution:dimension1:];
-[CUICatalog renditionKeyForShapeEffectPresetWithStylePresetName:state:presentationState:value:resolution:dimension1:appearance:];
-[CUICatalog setStorageRef:];
-[CUICatalog storageRef];
-[CUICatalog strokeStyledPath:inContext:stylePresetName:styleConfiguration:];
-[CUICatalog textStyleWithName:deviceIdiom:deviceSubtype:displayGamut:sizeClassHorizontal:sizeClassVertical:];
-[CUICatalog textStyleWithName:deviceIdiom:deviceSubtype:displayGamut:sizeClassHorizontal:sizeClassVertical:appearanceName:];
-[CUICatalog textStyleWithName:displayGamut:appearanceName:];
```
