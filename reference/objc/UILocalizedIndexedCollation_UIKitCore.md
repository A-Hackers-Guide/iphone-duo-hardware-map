# `UILocalizedIndexedCollation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSLocale" _locale;
@"NSArray" _sectionTitles;
@"NSArray" _sectionStartStrings;
@"NSArray" _sectionIndexTitles;
@"NSArray" _sectionIndexMapping;
@"NSString" _transform;
@"NSString" _firstSectionStartString;
@"NSString" _lastSectionStartString;
^{__CFStringTokenizer=} _tokenizer;
B _primaryLanguageIsJapanese;
B _preferJapaneseRomajiTranscriptions;
```

## Properties

```
@property (T@"NSArray",R,N) sectionTitles;
@property (T@"NSArray",R,N) sectionIndexTitles;
```

## Class methods

```
+[UILocalizedIndexedCollation collationWithDictionary:];
+[UILocalizedIndexedCollation currentCollation];
```

## Instance methods

```
-[UILocalizedIndexedCollation tokenizer];
-[UILocalizedIndexedCollation initWithDictionary:];
-[UILocalizedIndexedCollation dealloc];
-[UILocalizedIndexedCollation sectionIndexTitles];
-[UILocalizedIndexedCollation _kanaTranscriptionForString:];
-[UILocalizedIndexedCollation sectionForObject:collationStringSelector:];
-[UILocalizedIndexedCollation sectionForSectionIndexTitleAtIndex:];
-[UILocalizedIndexedCollation sectionTitles];
-[UILocalizedIndexedCollation sortedArrayFromArray:collationStringSelector:];
-[UILocalizedIndexedCollation transformedCollationStringForString:];
```
