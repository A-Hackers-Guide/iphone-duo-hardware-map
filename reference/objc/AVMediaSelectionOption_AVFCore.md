# `AVMediaSelectionOption`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 13 properties, 57 instance methods, 3 class methods

## Instance variables

```
@"AVMediaSelectionOptionInternal" _mediaSelectionOption;
```

## Properties

```
@property (Ti,R,N) trackID;
@property (T@"NSString",R,N) unicodeLanguageIdentifier;
@property (T@"NSString",R,N) unicodeLanguageCode;
@property (T@"NSNumber",R,N,G_audioCompositionPresetIndex) audioCompositionPresetIndex;
@property (T@"NSArray",R,N,G_audioCompositionPresetIndexesForFallbackIDs) audioCompositionPresetIndexesForFallbackIDs;
@property (T@"NSString",R,N) mediaType;
@property (T@"NSArray",R,N) mediaSubTypes;
@property (TB,R,N,GisPlayable) playable;
@property (T@"NSString",R,N) extendedLanguageTag;
@property (T@"NSLocale",R,N) locale;
@property (T@"NSArray",R,N) commonMetadata;
@property (T@"NSArray",R,N) availableMetadataFormats;
@property (T@"NSString",R,N) displayName;
```

## Class methods

```
+[AVMediaSelectionOption _plistHasOptionIdentifier:];
+[AVMediaSelectionOption mediaSelectionNilOptionForGroup:];
+[AVMediaSelectionOption mediaSelectionOptionForAsset:group:dictionary:requiresKeyValueOption:];
```

## Instance methods

```
-[AVMediaSelectionOption isPlayable];
-[AVMediaSelectionOption commonMetadata];
-[AVMediaSelectionOption _groupID];
-[AVMediaSelectionOption propertyList];
-[AVMediaSelectionOption metadataForFormat:];
-[AVMediaSelectionOption init];
-[AVMediaSelectionOption trackID];
-[AVMediaSelectionOption displayName];
-[AVMediaSelectionOption dealloc];
-[AVMediaSelectionOption group];
-[AVMediaSelectionOption dictionary];
-[AVMediaSelectionOption languageCode];
-[AVMediaSelectionOption availableMetadataFormats];
-[AVMediaSelectionOption locale];
-[AVMediaSelectionOption track];
-[AVMediaSelectionOption _groupMediaCharacteristics];
-[AVMediaSelectionOption description];
-[AVMediaSelectionOption extendedLanguageTag];
-[AVMediaSelectionOption _groupMediaType];
-[AVMediaSelectionOption copyWithZone:];
-[AVMediaSelectionOption mediaType];
-[AVMediaSelectionOption _title];
-[AVMediaSelectionOption initWithGroup:];
-[AVMediaSelectionOption outOfBandSource];
-[AVMediaSelectionOption _ancillaryDescription];
-[AVMediaSelectionOption _audioCompositionPresetIndex];
-[AVMediaSelectionOption _audioCompositionPresetIndexesForFallbackIDs];
-[AVMediaSelectionOption _baseLanguageDisplayNameWithLocale:context:fallingBackToMatchingUndeterminedAndMultilingual:];
-[AVMediaSelectionOption _displayNameWithLocale:fallingBackToMatchingUndeterminedAndMultilingual:];
-[AVMediaSelectionOption _displayNameWithLocale:omittingDecorationsForMediaCharacteristics:fallingBackToMatchingUndeterminedAndMultilingual:sparkleAllowed:context:redoBecauseLanguageInMiddleOfSentence:];
-[AVMediaSelectionOption _hasTranslationCharacteristicOrSourcingDependency];
-[AVMediaSelectionOption _isAuxiliaryContent];
-[AVMediaSelectionOption _isDesignatedDefault];
-[AVMediaSelectionOption _isMainProgramContent];
-[AVMediaSelectionOption _languageDisplayNameFromMetadataAccordingToPreferredLanguages:fallingBackToMatchingEmptyLocale:];
-[AVMediaSelectionOption _matchingOptionWithEnhancedSpeechIntelligibility];
-[AVMediaSelectionOption _preferredMetadataTitleAccordingToPreferredLanguages:fallingBackToMatchingEmptyLocale:excludeM3U8Metadata:];
-[AVMediaSelectionOption _representsNilSelection];
-[AVMediaSelectionOption _taggedMediaCharacteristics];
-[AVMediaSelectionOption _track];
-[AVMediaSelectionOption _updateDisplayNameCacheWithLocale:omittingDecorationsForMediaCharacteristics:fallingBackToMatchingUndeterminedAndMultilingual:sparkleAllowed:];
-[AVMediaSelectionOption associatedExtendedLanguageTag];
-[AVMediaSelectionOption associatedMediaSelectionOptionInMediaSelectionGroup:];
-[AVMediaSelectionOption associatedPersistentIDs];
-[AVMediaSelectionOption associatedUnicodeLanguageIdentifier];
-[AVMediaSelectionOption displayNameOmittingDecorationsForMediaCharacteristics:locale:];
-[AVMediaSelectionOption displayNameWithLocale:];
-[AVMediaSelectionOption displayNameWithOptionalSparkleWithLocale:];
-[AVMediaSelectionOption displaysNonForcedSubtitles];
-[AVMediaSelectionOption fallbackIDs];
-[AVMediaSelectionOption hasMediaCharacteristic:];
-[AVMediaSelectionOption mediaCharacteristics];
-[AVMediaSelectionOption mediaSubTypes];
-[AVMediaSelectionOption optionID];
-[AVMediaSelectionOption outOfBandIdentifier];
-[AVMediaSelectionOption unicodeLanguageCode];
-[AVMediaSelectionOption unicodeLanguageIdentifier];
```
