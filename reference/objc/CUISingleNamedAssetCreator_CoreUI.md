# `CUISingleNamedAssetCreator`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 12 properties, 77 instance methods, 0 class methods

## Instance variables

```
@"NSString" _primaryName;
Q _primaryIndex;
@"NSMutableArray" _names;
@"NSMutableArray" _generators;
@"CUIMutableCommonAssetStorage" _store;
d _radiosityCompressionQuaility;
d _flattenedCompressionQuality;
d _layersCompressionQuality;
q _compressionType;
@"NSMutableDictionary" _mappings;
B _allowsWideGamutImages;
B _allowsPaletteImageCompression;
B _generateFlattenedImages;
B _checkForMonochrome;
q _targetPlatform;
```

## Properties

```
@property (T@"CUIMutableCommonAssetStorage",&,V_store) store;
@property (T@"NSString",&,V_primaryName) primaryName;
@property (TQ,V_primaryIndex) primaryIndex;
@property (T@"NSMutableArray",&,V_names) names;
@property (T@"NSMutableArray",&,V_generators) generators;
@property (Td,N) compressionQuality;
@property (Tq,N) compressionType;
@property (TB,N,V_allowsWideGamutImages) allowsWideGamutImages;
@property (TB,N,V_allowsPaletteImageCompression) allowsPaletteImageCompression;
@property (TB,N,V_generateFlattenedImages) generateFlattenedImages;
@property (Tq,N,V_targetPlatform) targetPlatform;
@property (TB,N,V_checkForMonochrome) checkForMonochrome;
```

## Instance methods

```
-[CUISingleNamedAssetCreator compressionQuality];
-[CUISingleNamedAssetCreator setNames:];
-[CUISingleNamedAssetCreator targetPlatform];
-[CUISingleNamedAssetCreator compressionType];
-[CUISingleNamedAssetCreator names];
-[CUISingleNamedAssetCreator setAllowsPaletteImageCompression:];
-[CUISingleNamedAssetCreator setAllowsWideGamutImages:];
-[CUISingleNamedAssetCreator setCompressionQuality:];
-[CUISingleNamedAssetCreator addIconLayerGroupWithName:atScale:];
-[CUISingleNamedAssetCreator setCompressionType:];
-[CUISingleNamedAssetCreator setTargetPlatform:];
-[CUISingleNamedAssetCreator primaryIndex];
-[CUISingleNamedAssetCreator _flattenedImageBaseKeyWithScale:];
-[CUISingleNamedAssetCreator store];
-[CUISingleNamedAssetCreator addGradient:withStops:ofType:startPoint:endPoint:withName:atScale:];
-[CUISingleNamedAssetCreator setCheckForMonochrome:];
-[CUISingleNamedAssetCreator generateFlattenedImages];
-[CUISingleNamedAssetCreator generators];
-[CUISingleNamedAssetCreator _iconGroupBaseKeyWithScale:];
-[CUISingleNamedAssetCreator addSVGDocument:withName:atScale:];
-[CUISingleNamedAssetCreator addImageAsJPEG:withName:atScale:];
-[CUISingleNamedAssetCreator _addImage:withBaseKey:name:atScale:];
-[CUISingleNamedAssetCreator allowsWideGamutImages];
-[CUISingleNamedAssetCreator addTexture:withName:atScale:];
-[CUISingleNamedAssetCreator dealloc];
-[CUISingleNamedAssetCreator addLayerReference:forGroupToLayerStackWithName:atScale:];
-[CUISingleNamedAssetCreator addLayerReference:forColorToLayerStackWithName:atScale:];
-[CUISingleNamedAssetCreator setPrimaryIndex:];
-[CUISingleNamedAssetCreator addLayerReference:forImage:toLayerStackWithName:atScale:];
-[CUISingleNamedAssetCreator _addLayerStackWithSize:type:stackData:name:atScale:withRenderingProperties:];
-[CUISingleNamedAssetCreator flattenedLossyCompressionQuality];
-[CUISingleNamedAssetCreator setGenerators:];
-[CUISingleNamedAssetCreator _defaultBaseKeyWithScale:];
-[CUISingleNamedAssetCreator _distillNameEntries:];
-[CUISingleNamedAssetCreator _addImageAsJPEG:withBaseKey:withName:atScale:];
-[CUISingleNamedAssetCreator addLayerReference:forGradientToLayerStackWithName:atScale:];
-[CUISingleNamedAssetCreator _textureImageBaseKeyWithScale:];
-[CUISingleNamedAssetCreator _iconStackBaseKeyWithScale:];
-[CUISingleNamedAssetCreator primaryName];
-[CUISingleNamedAssetCreator addIconLayerStackWithSize:stackData:name:atScale:withRenderingProperties:];
-[CUISingleNamedAssetCreator _radiosityImageBaseKeyWithScale:];
-[CUISingleNamedAssetCreator layersLossyCompressionQuality];
-[CUISingleNamedAssetCreator _generatorForName:];
-[CUISingleNamedAssetCreator allowsPaletteImageCompression];
-[CUISingleNamedAssetCreator _configureDefaultStorageParameters];
-[CUISingleNamedAssetCreator addImage:withName:atScale:];
-[CUISingleNamedAssetCreator _textureBaseKeyWithScale:];
-[CUISingleNamedAssetCreator updateBitmapIndex];
-[CUISingleNamedAssetCreator distillAndSave:];
-[CUISingleNamedAssetCreator writeFlattenedImageToOutput:error:];
-[CUISingleNamedAssetCreator _vectorImageBaseKeyWithScale:];
-[CUISingleNamedAssetCreator setUpdateBitmapIndex:];
-[CUISingleNamedAssetCreator setPrimaryName:];
-[CUISingleNamedAssetCreator _allowsWideGamutImages];
-[CUISingleNamedAssetCreator _finalizeNameIdentifiers];
-[CUISingleNamedAssetCreator setRadiosityLossyCompressionQuality:];
-[CUISingleNamedAssetCreator setFlattenedLossyCompressionQuality:];
-[CUISingleNamedAssetCreator initWithOutputURL:versionString:];
-[CUISingleNamedAssetCreator _extractFlattenedImages:];
-[CUISingleNamedAssetCreator setGenerateFlattenedImages:];
-[CUISingleNamedAssetCreator _generatorWithName:];
-[CUISingleNamedAssetCreator setThinningArguments:];
-[CUISingleNamedAssetCreator setLayersLossyCompressionQuality:];
-[CUISingleNamedAssetCreator setStore:];
-[CUISingleNamedAssetCreator _colorBaseKeyWithScale:];
-[CUISingleNamedAssetCreator addColor:withName:atScale:];
-[CUISingleNamedAssetCreator addIconLayerStackWithSize:stackData:name:atScale:];
-[CUISingleNamedAssetCreator _gradientBaseKeyWithScale:];
-[CUISingleNamedAssetCreator _keyDataFromKey:];
-[CUISingleNamedAssetCreator checkForMonochrome];
-[CUISingleNamedAssetCreator _distillRenditions:];
-[CUISingleNamedAssetCreator addLayerStackWithSize:stackData:name:atScale:];
-[CUISingleNamedAssetCreator _keyFormat];
-[CUISingleNamedAssetCreator radiosityLossyCompressionQuality];
-[CUISingleNamedAssetCreator addFlattenedImage:forLayerStackWithName:atScale:];
-[CUISingleNamedAssetCreator path];
-[CUISingleNamedAssetCreator addLayerReference:forSVGDocumentToLayerStackWithName:atScale:];
```
