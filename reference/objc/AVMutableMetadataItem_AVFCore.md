# `AVMutableMetadataItem`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataItem`
- 1 instance variables, 8 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"AVMutableMetadataItemInternal" _mutablePriv;
```

## Properties

```
@property (T@"NSString",C,N) identifier;
@property (T@"NSString",C,N) extendedLanguageTag;
@property (T@"NSLocale",C,N) locale;
@property (T{?=qiIq},N) time;
@property (T{?=qiIq},N) duration;
@property (T@"NSString",C,N) dataType;
@property (T@"<NSObject><NSCopying>",C,N) value;
@property (T@"NSDictionary",C,N) extraAttributes;
```

## Class methods

```
+[AVMutableMetadataItem keyPathsForValuesAffectingIdentifier];
+[AVMutableMetadataItem metadataItem];
```

## Instance methods

```
-[AVMutableMetadataItem startDate];
-[AVMutableMetadataItem setExtendedLanguageTag:];
-[AVMutableMetadataItem setStartDate:];
-[AVMutableMetadataItem setDataType:];
-[AVMutableMetadataItem identifier];
-[AVMutableMetadataItem setLocale:];
-[AVMutableMetadataItem value];
-[AVMutableMetadataItem setKey:];
-[AVMutableMetadataItem duration];
-[AVMutableMetadataItem languageCode];
-[AVMutableMetadataItem setIdentifier:];
-[AVMutableMetadataItem setValue:];
-[AVMutableMetadataItem locale];
-[AVMutableMetadataItem setExtraAttributes:];
-[AVMutableMetadataItem keySpace];
-[AVMutableMetadataItem dataType];
-[AVMutableMetadataItem setKeySpace:];
-[AVMutableMetadataItem setTime:];
-[AVMutableMetadataItem setDuration:];
-[AVMutableMetadataItem extendedLanguageTag];
-[AVMutableMetadataItem copyWithZone:];
-[AVMutableMetadataItem extraAttributes];
-[AVMutableMetadataItem setPreferredStorageLocation:];
-[AVMutableMetadataItem key];
-[AVMutableMetadataItem time];
```
