# `CUICommonAssetStorage`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 14 properties, 106 instance methods, 2 class methods

## Instance variables

```
^{_carheader=IIIII[128c][256c][16C]IIII} _header;
^{_carextendedMetadata=I[256c][256c][256c][256c]} _extendedMetadata;
^{_renditionkeyfmt=III[0I]} _keyfmt;
^v _imagedb;
^v _colordb;
^v _fontdb;
^v _fontsizedb;
^v _facetKeysdb;
^v _bitmapKeydb;
^v _appearancedb;
^v _localizationdb;
@"NSData" _globals;
I _thinnedWithCoreUIVersion;
b1 _swap;
b1 _isMemoryMapped;
b1 _hasAppearanceKey;
b1 _hasLocalizationKey;
b28 _reserved;
@"NSSet" _externalTags;
[20S] _renditionInfoCacheLookup;
[20@] _renditionInfoCache;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _renditionInfoCacheLock;
{_renditionkeyattributeindex="keymask"Q"keyindices"[65C]"nkeys"I"keylist"[29I]} _keyfmtindex;
@"NSDictionary" _appearances;
@"NSDictionary" _facetValueNameDict;
```

## Properties

```
@property (T^{_carheader=IIIII[128c][256c][16C]IIII},N,V_header) header;
@property (T^{_carextendedMetadata=I[256c][256c][256c][256c]},N,V_extendedMetadata) extendedMetadata;
@property (T^{_renditionkeyfmt=III[0I]},N,V_keyfmt) keyfmt;
@property (T^v,N,V_imagedb) imagedb;
@property (T^v,N,V_colordb) colordb;
@property (T^v,N,V_fontdb) fontdb;
@property (T^v,N,V_fontsizedb) fontsizedb;
@property (T^v,N,V_facetKeysdb) facetKeysdb;
@property (T^v,N,V_bitmapKeydb) bitmapKeydb;
@property (T^v,N,V_appearancedb) appearancedb;
@property (T^v,N,V_localizationdb) localizationdb;
@property (T@"NSData",&,N,V_globals) globals;
@property (T@"NSDictionary",R,N,V_appearances) appearances;
@property (T@"NSDictionary",N,V_facetValueNameDict) facetValueNameDict;
```

## Class methods

```
+[CUICommonAssetStorage isValidAssetStorageWithBytes:length:];
+[CUICommonAssetStorage isValidAssetStorageWithURL:];
```

## Instance methods

```
-[CUICommonAssetStorage setColordb:];
-[CUICommonAssetStorage _initDefaultHeaderVersion:versionString:];
-[CUICommonAssetStorage header];
-[CUICommonAssetStorage colorSpaceID];
-[CUICommonAssetStorage appearanceIdentifierForName:];
-[CUICommonAssetStorage keySemantics];
-[CUICommonAssetStorage hasColorForName:];
-[CUICommonAssetStorage getBaselineOffset:forFontType:];
-[CUICommonAssetStorage initWithBytes:length:];
-[CUICommonAssetStorage thinningArguments];
-[CUICommonAssetStorage facetKeysdb];
-[CUICommonAssetStorage validateFile];
-[CUICommonAssetStorage initWithPath:];
-[CUICommonAssetStorage keyFormatData];
-[CUICommonAssetStorage setHeader:];
-[CUICommonAssetStorage thinnedWithCoreUIVersion];
-[CUICommonAssetStorage colordb];
-[CUICommonAssetStorage deploymentPlatform];
-[CUICommonAssetStorage _swapRenditionKeyToken:];
-[CUICommonAssetStorage _addBitmapIndexForNameIdentifier:attribute:withValue:toDictionary:];
-[CUICommonAssetStorage uuid];
-[CUICommonAssetStorage maximumRenditionKeyTokenCount];
-[CUICommonAssetStorage validateBitmapInfo];
-[CUICommonAssetStorage _storagefileTimestamp];
-[CUICommonAssetStorage _renditionKeyForName:hotSpot:];
-[CUICommonAssetStorage enumerateRenditionInfosUsingBlock:];
-[CUICommonAssetStorage deploymentPlatformVersion];
-[CUICommonAssetStorage dealloc];
-[CUICommonAssetStorage mainVersionString];
-[CUICommonAssetStorage nameForLocalizationIdentifier:];
-[CUICommonAssetStorage keyFormat];
-[CUICommonAssetStorage allAssetKeys];
-[CUICommonAssetStorage renditionNameForKeyList:];
-[CUICommonAssetStorage validatekeyformat];
-[CUICommonAssetStorage setKeyfmt:];
-[CUICommonAssetStorage enumerateKeysAndObjectsWithoutIgnoringUsingBlock:];
-[CUICommonAssetStorage setFontsizedb:];
-[CUICommonAssetStorage _fontValueForFontType:];
-[CUICommonAssetStorage schemaVersion];
-[CUICommonAssetStorage writeToPath:withTreePageSize:];
-[CUICommonAssetStorage catalogGlobalData];
-[CUICommonAssetStorage setExtendedMetadata:];
-[CUICommonAssetStorage setGlobals:];
-[CUICommonAssetStorage appearancedb];
-[CUICommonAssetStorage authoringTool];
-[CUICommonAssetStorage versionString];
-[CUICommonAssetStorage localizationdb];
-[CUICommonAssetStorage getFontName:baselineOffset:forFontType:];
-[CUICommonAssetStorage appearances];
-[CUICommonAssetStorage initWithPath:forWriting:];
-[CUICommonAssetStorage storageVersion];
-[CUICommonAssetStorage globals];
-[CUICommonAssetStorage renditionCount];
-[CUICommonAssetStorage setAppearancedb:];
-[CUICommonAssetStorage keyAttributeIndex];
-[CUICommonAssetStorage setExternalTags:];
-[CUICommonAssetStorage assetExistsForKey:];
-[CUICommonAssetStorage _allRenditionNames];
-[CUICommonAssetStorage getColor:forName:];
-[CUICommonAssetStorage fontsizedb];
-[CUICommonAssetStorage assetKeysMatchingBlock:];
-[CUICommonAssetStorage localizationIdentifierForName:];
-[CUICommonAssetStorage associatedChecksum];
-[CUICommonAssetStorage _bringHeaderInfoUpToDate];
-[CUICommonAssetStorage _readAppearances];
-[CUICommonAssetStorage renditionKeyForName:hotSpot:];
-[CUICommonAssetStorage allRenditionNames];
-[CUICommonAssetStorage description];
-[CUICommonAssetStorage imagedb];
-[CUICommonAssetStorage renditionNameForKeyBaseList:];
-[CUICommonAssetStorage fontdb];
-[CUICommonAssetStorage _loadExtendedMetadata];
-[CUICommonAssetStorage enumerateColorsBlock:];
-[CUICommonAssetStorage setFacetValueNameDict:];
-[CUICommonAssetStorage lock];
-[CUICommonAssetStorage setFontdb:];
-[CUICommonAssetStorage enumerateBitmapIndexUsingBlock:];
-[CUICommonAssetStorage extendedMetadata];
-[CUICommonAssetStorage localizations];
-[CUICommonAssetStorage setLocalizationdb:];
-[CUICommonAssetStorage _buildBitmapInfoIntoDictionary:];
-[CUICommonAssetStorage renditionInfoForIdentifier:];
-[CUICommonAssetStorage bitmapKeydb];
-[CUICommonAssetStorage storageTimestamp];
-[CUICommonAssetStorage facetValueNameMap];
-[CUICommonAssetStorage externalTags];
-[CUICommonAssetStorage nameForAppearanceIdentifier:];
-[CUICommonAssetStorage distilledInCoreUIVersion];
-[CUICommonAssetStorage setImagedb:];
-[CUICommonAssetStorage usesCUISystemThemeRenditionKey];
-[CUICommonAssetStorage swapped];
-[CUICommonAssetStorage renditionNamesWithKeys];
-[CUICommonAssetStorage setFacetKeysdb:];
-[CUICommonAssetStorage _commonInitWithStorage:forWritting:];
-[CUICommonAssetStorage assetExistsForKeyData:length:];
-[CUICommonAssetStorage _swapRenditionKeyArray:];
-[CUICommonAssetStorage renditionInfoCacheLock];
-[CUICommonAssetStorage deploymentPlatformString];
-[CUICommonAssetStorage keyfmt];
-[CUICommonAssetStorage _bomStorage];
-[CUICommonAssetStorage fontSizeForFontSizeType:];
-[CUICommonAssetStorage assetForKey:];
-[CUICommonAssetStorage path];
-[CUICommonAssetStorage enumerateKeysAndObjectsUsingBlock:];
-[CUICommonAssetStorage setBitmapKeydb:];
-[CUICommonAssetStorage facetValueNameDict];
```
