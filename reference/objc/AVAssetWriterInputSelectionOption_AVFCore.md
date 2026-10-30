# `AVAssetWriterInputSelectionOption`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMediaSelectionOption`
- 10 instance variables, 9 properties, 27 instance methods, 2 class methods

## Instance variables

```
@"AVAssetWriterInput" _input;
@"NSString" _mediaType;
@"NSDictionary" _outputSettings;
^{opaqueCMFormatDescription=} _sourceFormatHint;
@"NSString" _languageCode;
@"NSString" _extendedLanguageTag;
@"NSArray" _metadata;
@"NSDictionary" _trackReferences;
B _displaysNonForcedSubtitles;
B _enabled;
```

## Properties

```
@property (T@"NSString",R,N,V_mediaType) mediaType;
@property (T@"NSDictionary",R,N,V_outputSettings) outputSettings;
@property (T^{opaqueCMFormatDescription=},R,N,V_sourceFormatHint) sourceFormatHint;
@property (T@"NSString",R,N,V_languageCode) languageCode;
@property (T@"NSString",R,N,V_extendedLanguageTag) extendedLanguageTag;
@property (T@"NSArray",R,N,V_metadata) metadata;
@property (T@"NSDictionary",R,N,V_trackReferences) trackReferences;
@property (TB,R,N,V_displaysNonForcedSubtitles) displaysNonForcedSubtitles;
@property (T@"AVAssetWriterInput",R,N,V_input) input;
```

## Class methods

```
+[AVAssetWriterInputSelectionOption assetWriterInputSelectionOptionWithAssetWriterInput:];
+[AVAssetWriterInputSelectionOption assetWriterInputSelectionOptionWithAssetWriterInput:displaysNonForcedSubtitles:];
```

## Instance methods

```
-[AVAssetWriterInputSelectionOption isPlayable];
-[AVAssetWriterInputSelectionOption trackReferences];
-[AVAssetWriterInputSelectionOption commonMetadata];
-[AVAssetWriterInputSelectionOption outputSettings];
-[AVAssetWriterInputSelectionOption input];
-[AVAssetWriterInputSelectionOption propertyList];
-[AVAssetWriterInputSelectionOption metadataForFormat:];
-[AVAssetWriterInputSelectionOption dealloc];
-[AVAssetWriterInputSelectionOption metadata];
-[AVAssetWriterInputSelectionOption languageCode];
-[AVAssetWriterInputSelectionOption availableMetadataFormats];
-[AVAssetWriterInputSelectionOption locale];
-[AVAssetWriterInputSelectionOption hash];
-[AVAssetWriterInputSelectionOption extendedLanguageTag];
-[AVAssetWriterInputSelectionOption mediaType];
-[AVAssetWriterInputSelectionOption isEqual:];
-[AVAssetWriterInputSelectionOption _ancillaryDescription];
-[AVAssetWriterInputSelectionOption _hasEqualValueForKey:asObject:];
-[AVAssetWriterInputSelectionOption _isAuxiliaryContent];
-[AVAssetWriterInputSelectionOption _isDesignatedDefault];
-[AVAssetWriterInputSelectionOption _taggedCharacteristics];
-[AVAssetWriterInputSelectionOption associatedMediaSelectionOptionInMediaSelectionGroup:];
-[AVAssetWriterInputSelectionOption displaysNonForcedSubtitles];
-[AVAssetWriterInputSelectionOption initWithAssetWriterInput:];
-[AVAssetWriterInputSelectionOption initWithAssetWriterInput:displaysNonForcedSubtitles:];
-[AVAssetWriterInputSelectionOption mediaSubTypes];
-[AVAssetWriterInputSelectionOption sourceFormatHint];
```
