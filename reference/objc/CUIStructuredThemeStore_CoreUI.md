# `CUIStructuredThemeStore`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUIStructuredThemeStorage`, `CUIStructuredThemeStorage2`
- 12 instance variables, 5 properties, 66 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _cache;
@"CUICommonAssetStorage" _store;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _cacheLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _storeLock;
Q _themeIndex;
@"NSString" _bundleID;
@"NSCache" _namedRenditionKeyCache;
^? _attributePresent;
b1 _mainBundle;
@"NSDictionary" _aliasDictionary;
@"NSSet" _legacyFlippableSet;
@"NSCache" _nameCache;
```

## Properties

```
@property (TB) mainBundle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CUIStructuredThemeStore _commonInit];
-[CUIStructuredThemeStore mainBundle];
-[CUIStructuredThemeStore localizationWorkaroundForKeyList:withLocale:];
-[CUIStructuredThemeStore colorSpaceID];
-[CUIStructuredThemeStore appearanceIdentifierForName:];
-[CUIStructuredThemeStore imagesWithName:];
-[CUIStructuredThemeStore initWithBytes:length:];
-[CUIStructuredThemeStore initWithPath:];
-[CUIStructuredThemeStore thinnedWithCoreUIVersion];
-[CUIStructuredThemeStore store];
-[CUIStructuredThemeStore deploymentPlatform];
-[CUIStructuredThemeStore getPhysicalColor:withName:];
-[CUIStructuredThemeStore debugDescription];
-[CUIStructuredThemeStore authoredWithSchemaVersion];
-[CUIStructuredThemeStore maximumRenditionKeyTokenCount];
-[CUIStructuredThemeStore renditionKeyForName:];
-[CUIStructuredThemeStore setBundleID:];
-[CUIStructuredThemeStore _subImageTexturingShouldBeSupported];
-[CUIStructuredThemeStore dealloc];
-[CUIStructuredThemeStore baseGradationKeySignatureForKey:];
-[CUIStructuredThemeStore keySignatureForKey:];
-[CUIStructuredThemeStore imageNamedShouldFlip:];
-[CUIStructuredThemeStore nameForLocalizationIdentifier:];
-[CUIStructuredThemeStore keyFormat];
-[CUIStructuredThemeStore themeStore];
-[CUIStructuredThemeStore renditionNameForKeyList:];
-[CUIStructuredThemeStore clearRenditionCache];
-[CUIStructuredThemeStore renditionWithKey:usingKeySignature:];
-[CUIStructuredThemeStore allImageNames];
-[CUIStructuredThemeStore getFontName:baselineOffset:forFontType:];
-[CUIStructuredThemeStore appearances];
-[CUIStructuredThemeStore containsLookupForName:];
-[CUIStructuredThemeStore _formatStorageKeyArrayBytes:length:fromKey:];
-[CUIStructuredThemeStore _newRenditionKeyDataFromKey:];
-[CUIStructuredThemeStore keyAttributeIndex];
-[CUIStructuredThemeStore assetExistsForKey:];
-[CUIStructuredThemeStore hasPhysicalColorWithName:];
-[CUIStructuredThemeStore copyKeySignatureForKey:withBytesNoCopy:length:];
-[CUIStructuredThemeStore localizationIdentifierForName:];
-[CUIStructuredThemeStore themeIndex];
-[CUIStructuredThemeStore mappedAliases];
-[CUIStructuredThemeStore setThemeIndex:];
-[CUIStructuredThemeStore copyLookupKeySignatureForKey:];
-[CUIStructuredThemeStore convertRenditionKeyToKeyData:];
-[CUIStructuredThemeStore bundleID];
-[CUIStructuredThemeStore catalogGlobals];
-[CUIStructuredThemeStore aliasForName:];
-[CUIStructuredThemeStore renditionKeyFormat];
-[CUIStructuredThemeStore localizations];
-[CUIStructuredThemeStore renditionInfoForIdentifier:];
-[CUIStructuredThemeStore setMainBundle:];
-[CUIStructuredThemeStore debugDescriptionForKeyList:];
-[CUIStructuredThemeStore defaultAppearanceName];
-[CUIStructuredThemeStore documentFormatVersion];
-[CUIStructuredThemeStore nameForAppearanceIdentifier:];
-[CUIStructuredThemeStore distilledInCoreUIVersion];
-[CUIStructuredThemeStore initWithURL:];
-[CUIStructuredThemeStore usesCUISystemThemeRenditionKey];
-[CUIStructuredThemeStore renditionWithKey:];
-[CUIStructuredThemeStore lookupAssetForKey:];
-[CUIStructuredThemeStore deploymentPlatformString];
-[CUIStructuredThemeStore _updateKeyWithCompatibilityMapping:];
-[CUIStructuredThemeStore canGetRenditionWithKey:];
-[CUIStructuredThemeStore fontSizeForFontSizeType:];
-[CUIStructuredThemeStore caAllowSubimageOfImage:];
-[CUIStructuredThemeStore renditionKeyForName:cursorHotSpot:];
```
