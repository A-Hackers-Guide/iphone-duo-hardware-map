# `TPSSubscriptionLabeler`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 18 instance methods, 21 class methods

## Instance variables

```
@"NSMutableDictionary" _labelDictionary;
@"NSObject<OS_dispatch_queue>" _accessQueue;
@"NSURL" _url;
@"NSArray" _applicableUnlocalizedLabels;
@"NSString" _applicableLanguage;
@"NSLocale" _updatingLocale;
@"NSArray" _cachedResult;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_labelDictionary) labelDictionary;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessQueue) accessQueue;
@property (T@"NSURL",&,N,V_url) url;
@property (T@"NSArray",&,N,V_applicableUnlocalizedLabels) applicableUnlocalizedLabels;
@property (T@"NSString",&,N,V_applicableLanguage) applicableLanguage;
@property (T@"NSLocale",&,N,V_updatingLocale) updatingLocale;
@property (T@"NSArray",&,N,V_cachedResult) cachedResult;
```

## Class methods

```
+[TPSSubscriptionLabeler localizedLabelForLabel:];
+[TPSSubscriptionLabeler _dictionary:containsCollationEquivalentKey:];
+[TPSSubscriptionLabeler _groupStringsByCollationEquivalency:];
+[TPSSubscriptionLabeler _resultWithAllCharacters:string:];
+[TPSSubscriptionLabeler displayShortLabelStringsForLongFormShortLabels:];
+[TPSSubscriptionLabeler fontAttributeDictionary];
+[TPSSubscriptionLabeler isExclusivelyCJKString:characterSets:];
+[TPSSubscriptionLabeler isString:exclusivelyInCharacterSet:];
+[TPSSubscriptionLabeler localizedBadgeLabelsForUnlocalizedLabels:];
+[TPSSubscriptionLabeler localizedBadgeLabelsForUnlocalizedLabels:languageIdentifiers:];
+[TPSSubscriptionLabeler localizedBadgeLabelsForUnlocalizedLabels:languageStringOverrides:];
+[TPSSubscriptionLabeler localizedLabelForLabel:longForm:languageStringOverrides:];
+[TPSSubscriptionLabeler localizedLabelsForLabels:languageIdentifiers:];
+[TPSSubscriptionLabeler localizedLabelsForLabels:languageStringOverrides:];
+[TPSSubscriptionLabeler localizedStringDictionaryForLanguageIdentifiers:selectedLanguage:];
+[TPSSubscriptionLabeler standardLabelIdentifiers];
+[TPSSubscriptionLabeler stringByShorteningString:maximumWidth:attributes:];
+[TPSSubscriptionLabeler stringsByAbbreviatingToPrefixesOfStrings:];
+[TPSSubscriptionLabeler stringsByClippingStrings:toWidthOfString:];
+[TPSSubscriptionLabeler stringsByNumericallyDisambiguatingStrings:];
+[TPSSubscriptionLabeler widthOfString:attributes:];
```

## Instance methods

```
-[TPSSubscriptionLabeler accessQueue];
-[TPSSubscriptionLabeler cachedResult];
-[TPSSubscriptionLabeler setAccessQueue:];
-[TPSSubscriptionLabeler setUrl:];
-[TPSSubscriptionLabeler url];
-[TPSSubscriptionLabeler setCachedResult:];
-[TPSSubscriptionLabeler labelDictionary];
-[TPSSubscriptionLabeler setApplicableUnlocalizedLabels:];
-[TPSSubscriptionLabeler _validateLabelsForInstalledUnlocalizedLabels:languageIdentifiers:];
-[TPSSubscriptionLabeler applicableLanguage];
-[TPSSubscriptionLabeler applicableUnlocalizedLabels];
-[TPSSubscriptionLabeler cachedLocalizedLabelsForUnlocalizedLabels:];
-[TPSSubscriptionLabeler cachedLocalizedLabelsForUnlocalizedLabels:languageIdentifiers:];
-[TPSSubscriptionLabeler initWithLabelStorage:];
-[TPSSubscriptionLabeler setApplicableLanguage:];
-[TPSSubscriptionLabeler setLabelDictionary:];
-[TPSSubscriptionLabeler setUpdatingLocale:];
-[TPSSubscriptionLabeler updatingLocale];
```
