# `_UIDefinitionDictionary`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
^{__DCSDictionary=} _dictionary;
B _activated;
@"MAAsset" _rawAsset;
@"NSString" _definitionLanguage;
@"MAAsset" _assetToUpgrade;
```

## Properties

```
@property (T@"MAAsset",R,V_rawAsset) rawAsset;
@property (T@"NSString",R) localizedLanguageName;
@property (T@"NSString",R) localizedDictionaryName;
@property (T@"NSString",R,V_definitionLanguage) definitionLanguage;
@property (TB,V_activated) activated;
@property (T@"MAAsset",&,V_assetToUpgrade) assetToUpgrade;
```

## Class methods

```
+[_UIDefinitionDictionary _normalizedLanguageStringForLanguageCode:];
```

## Instance methods

```
-[_UIDefinitionDictionary setActivated:];
-[_UIDefinitionDictionary dealloc];
-[_UIDefinitionDictionary initWithAsset:];
-[_UIDefinitionDictionary description];
-[_UIDefinitionDictionary _HTMLDefinitionForTerm:type:];
-[_UIDefinitionDictionary _attributedDefinitionForTerm:];
-[_UIDefinitionDictionary _definitionValueForTerm:];
-[_UIDefinitionDictionary _fullHTMLDefinitionForTerm:];
-[_UIDefinitionDictionary _hasDefinitionForTerm:];
-[_UIDefinitionDictionary _isTTYDictionary];
-[_UIDefinitionDictionary _shortHTMLDefinitionForTerm:];
-[_UIDefinitionDictionary activated];
-[_UIDefinitionDictionary assetIsDeletable];
-[_UIDefinitionDictionary assetIsLocal];
-[_UIDefinitionDictionary assetToUpgrade];
-[_UIDefinitionDictionary definitionLanguage];
-[_UIDefinitionDictionary localizedDictionaryName];
-[_UIDefinitionDictionary localizedLanguageName];
-[_UIDefinitionDictionary rawAsset];
-[_UIDefinitionDictionary setAssetToUpgrade:];
-[_UIDefinitionDictionary updateAsset];
```
