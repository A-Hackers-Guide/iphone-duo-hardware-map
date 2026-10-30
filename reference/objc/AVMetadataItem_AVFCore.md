# `AVMetadataItem`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAsynchronousKeyValueLoading`, `NSCopying`, `NSMutableCopying`
- 1 instance variables, 12 properties, 54 instance methods, 21 class methods

## Instance variables

```
@"AVMetadataItemInternal" _priv;
```

## Properties

```
@property (T@"NSString",R,N) stringValue;
@property (T@"NSNumber",R,N) numberValue;
@property (T@"NSDate",R,N) dateValue;
@property (T@"NSData",R,N) dataValue;
@property (T@"NSString",R,C,N) identifier;
@property (T@"NSString",R,C,N) extendedLanguageTag;
@property (T@"NSLocale",R,C,N) locale;
@property (T{?=qiIq},R,N) time;
@property (T{?=qiIq},R,N) duration;
@property (T@"NSString",R,C,N) dataType;
@property (T@"<NSObject><NSCopying>",R,C,N) value;
@property (T@"NSDictionary",R,C,N) extraAttributes;
```

## Class methods

```
+[AVMetadataItem initialize];
+[AVMetadataItem _clientExpectsISOUserDataKeysInQuickTimeUserDataKeySpace];
+[AVMetadataItem _figMetadataPropertyFromMetadataItems:];
+[AVMetadataItem _isoUserDataKeysRequiringKeySpaceConversion];
+[AVMetadataItem _metadataArrayWithSmartDeferredLoadingForMetadataArray:error:];
+[AVMetadataItem _metadataItemWithFigMetadataDictionary:];
+[AVMetadataItem _metadataItemWithFigMetadataDictionary:containerURL:securityOptions:];
+[AVMetadataItem _replaceQuickTimeUserDataKeySpaceWithISOUserDataKeySpaceIfRequired:];
+[AVMetadataItem dataTypeForValue:];
+[AVMetadataItem figMetadataPropertyFromMetadataItems:];
+[AVMetadataItem identifierForKey:keySpace:];
+[AVMetadataItem keyForIdentifier:];
+[AVMetadataItem keySpaceForIdentifier:];
+[AVMetadataItem metadataItemWithPropertiesOfMetadataItem:valueLoadingHandler:];
+[AVMetadataItem metadataItemsFromArray:filteredAndSortedAccordingToPreferredLanguages:];
+[AVMetadataItem metadataItemsFromArray:filteredByIdentifier:];
+[AVMetadataItem metadataItemsFromArray:filteredByIdentifiers:];
+[AVMetadataItem metadataItemsFromArray:filteredByMetadataItemFilter:];
+[AVMetadataItem metadataItemsFromArray:withKey:keySpace:];
+[AVMetadataItem metadataItemsFromArray:withLocale:];
+[AVMetadataItem metadataItemsFromArray:withStringValue:];
```

## Instance methods

```
-[AVMetadataItem startDate];
-[AVMetadataItem stringValue];
-[AVMetadataItem dataValue];
-[AVMetadataItem dateValue];
-[AVMetadataItem mutableCopyWithZone:];
-[AVMetadataItem identifier];
-[AVMetadataItem statusOfValueForKey:error:];
-[AVMetadataItem init];
-[AVMetadataItem numberValue];
-[AVMetadataItem dealloc];
-[AVMetadataItem value];
-[AVMetadataItem duration];
-[AVMetadataItem languageCode];
-[AVMetadataItem locale];
-[AVMetadataItem keySpace];
-[AVMetadataItem hash];
-[AVMetadataItem dataType];
-[AVMetadataItem description];
-[AVMetadataItem extendedLanguageTag];
-[AVMetadataItem copyWithZone:];
-[AVMetadataItem isEqual:];
-[AVMetadataItem extraAttributes];
-[AVMetadataItem cancelLoading];
-[AVMetadataItem key];
-[AVMetadataItem loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVMetadataItem time];
-[AVMetadataItem imageValue];
-[AVMetadataItem _initWithFigMetadataDictionary:];
-[AVMetadataItem _makeValueReady];
-[AVMetadataItem _preferredStorageLocationWasSet];
-[AVMetadataItem _areExtraAttributesOf:comparableToExtraAttributesOf:];
-[AVMetadataItem _conformingDataTypes];
-[AVMetadataItem _copyValueAsCFTypeWithFormatDescription:error:];
-[AVMetadataItem _createJSONEncodedDataFromValue:error:];
-[AVMetadataItem _extractPropertiesFromDictionary:];
-[AVMetadataItem _figMetadataDictionary];
-[AVMetadataItem _figMetadataDictionaryWithValue:diviningValueDataType:];
-[AVMetadataItem _figMetadataFormat];
-[AVMetadataItem _figMetadataSpecificationReturningError:];
-[AVMetadataItem _initWithReader:itemIndex:];
-[AVMetadataItem _keyAsString];
-[AVMetadataItem _makePropertiesReady];
-[AVMetadataItem _serializationDataType];
-[AVMetadataItem _updateCommonKey];
-[AVMetadataItem _updateIdentifier];
-[AVMetadataItem _updateLanguageInformationFromExtendedLanguageTag:];
-[AVMetadataItem _updateLanguageInformationFromLocale:];
-[AVMetadataItem _valueFromCFType:];
-[AVMetadataItem commonKey];
-[AVMetadataItem discoveryTimestamp];
-[AVMetadataItem intrinsicAttributesOfExtraAttributes:];
-[AVMetadataItem preferredStorageLocation];
-[AVMetadataItem unicodeLanguageCode];
-[AVMetadataItem unicodeLanguageIdentifier];
```
