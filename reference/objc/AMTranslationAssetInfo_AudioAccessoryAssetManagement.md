# `AMTranslationAssetInfo`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`](../userland/System__Library__PrivateFrameworks__AudioAccessoryAssetManagement.framework__AudioAccessoryAssetManagement.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
C _assetStatus;
B _isSuggested;
@"NSLocale" _locale;
@"NSString" _displayName;
```

## Properties

```
@property (T@"NSLocale",&,N,V_locale) locale;
@property (T@"NSString",&,N,V_displayName) displayName;
@property (TC,N,V_assetStatus) assetStatus;
@property (TB,N,V_isSuggested) isSuggested;
```

## Class methods

```
+[AMTranslationAssetInfo supportsSecureCoding];
```

## Instance methods

```
-[AMTranslationAssetInfo isSuggested];
-[AMTranslationAssetInfo displayName];
-[AMTranslationAssetInfo setLocale:];
-[AMTranslationAssetInfo setDisplayName:];
-[AMTranslationAssetInfo locale];
-[AMTranslationAssetInfo encodeWithCoder:];
-[AMTranslationAssetInfo description];
-[AMTranslationAssetInfo initWithCoder:];
-[AMTranslationAssetInfo setIsSuggested:];
-[AMTranslationAssetInfo assetStatus];
-[AMTranslationAssetInfo setAssetStatus:];
```
