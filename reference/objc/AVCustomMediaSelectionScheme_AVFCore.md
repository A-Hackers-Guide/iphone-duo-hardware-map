# `AVCustomMediaSelectionScheme`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 7 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _weakReferenceToGroup;
@"NSArray" _options;
@"NSArray" _mediaPresentationSelectors;
@"NSArray" _availableLanguageTags;
@"NSDictionary" _decorationCharacteristicsForLanguages;
@"NSDictionary" _languageDecorationDisplayNames;
B _shouldOfferLanguageSelection;
```

## Properties

```
@property (T@"NSDictionary",R,N) decorationCharacteristicsForLanguages;
@property (T@"NSDictionary",R,N) languageDecorationDisplayNames;
@property (TB,R) shouldOfferLanguageSelection;
@property (T@"NSArray",R) availableLanguages;
@property (T@"NSArray",R) selectors;
```

## Instance methods

```
-[AVCustomMediaSelectionScheme dealloc];
-[AVCustomMediaSelectionScheme group];
-[AVCustomMediaSelectionScheme hash];
-[AVCustomMediaSelectionScheme description];
-[AVCustomMediaSelectionScheme availableLanguages];
-[AVCustomMediaSelectionScheme copyWithZone:];
-[AVCustomMediaSelectionScheme isEqual:];
-[AVCustomMediaSelectionScheme _selectorForSetting:];
-[AVCustomMediaSelectionScheme decorationCharacteristicsForLanguages];
-[AVCustomMediaSelectionScheme displayNameForLanguage:localeIdentifier:];
-[AVCustomMediaSelectionScheme initWithGroup:figAssetMediaSelectionGroupCustomMediaSelectionScheme:];
-[AVCustomMediaSelectionScheme languageDecorationDisplayNames];
-[AVCustomMediaSelectionScheme mediaPresentationSettingsForSelector:complementaryToLanguage:settings:];
-[AVCustomMediaSelectionScheme selectors];
-[AVCustomMediaSelectionScheme shouldOfferLanguageSelection];
```
