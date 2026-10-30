# `AVAssetDownloadConfiguration`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 10 properties, 23 instance methods, 2 class methods

## Instance variables

```
@"AVURLAsset" _asset;
@"NSString" _title;
@"NSData" _artworkData;
@"AVAssetDownloadContentConfiguration" _primaryContentConfiguration;
@"NSArray" _auxiliaryContentConfigurations;
{?="start"{?="value"q"timescale"i"flags"I"epoch"q}"duration"{?="value"q"timescale"i"flags"I"epoch"q}} _timeRange;
@"NSURL" _destinationURL;
B optimizesAuxiliaryContentConfigurations;
B downloadsInterstitialAssets;
B liveActivityEnabled;
@"NSMutableDictionary" _interstitialMediaSelectionCriteria;
B _optimizesAuxiliaryContentConfigurations;
B _downloadsInterstitialAssets;
```

## Properties

```
@property (T@"AVURLAsset",R,N,G_asset) asset;
@property (T@"NSString",R,N,G_assetTitle) assetTitle;
@property (T{?={?=qiIq}{?=qiIq}},N) timeRange;
@property (T@"NSURL",C,N,G_destinationURL,S_setDestinationURL:) destinationURL;
@property (TB,N,GisLiveActivityEnabled) liveActivityEnabled;
@property (T@"NSData",C,N,V_artworkData) artworkData;
@property (T@"AVAssetDownloadContentConfiguration",R,N,V_primaryContentConfiguration) primaryContentConfiguration;
@property (T@"NSArray",C,N,V_auxiliaryContentConfigurations) auxiliaryContentConfigurations;
@property (TB,N,V_optimizesAuxiliaryContentConfigurations) optimizesAuxiliaryContentConfigurations;
@property (TB,N,V_downloadsInterstitialAssets) downloadsInterstitialAssets;
```

## Class methods

```
+[AVAssetDownloadConfiguration supportsSecureCoding];
+[AVAssetDownloadConfiguration downloadConfigurationWithAsset:title:];
```

## Instance methods

```
-[AVAssetDownloadConfiguration setTimeRange:];
-[AVAssetDownloadConfiguration timeRange];
-[AVAssetDownloadConfiguration setArtworkData:];
-[AVAssetDownloadConfiguration artworkData];
-[AVAssetDownloadConfiguration dealloc];
-[AVAssetDownloadConfiguration encodeWithCoder:];
-[AVAssetDownloadConfiguration initWithCoder:];
-[AVAssetDownloadConfiguration _asset];
-[AVAssetDownloadConfiguration _destinationURL];
-[AVAssetDownloadConfiguration _assetTitle];
-[AVAssetDownloadConfiguration setDownloadsInterstitialAssets:];
-[AVAssetDownloadConfiguration _copyFigDownloadConfig];
-[AVAssetDownloadConfiguration _setDestinationURL:];
-[AVAssetDownloadConfiguration auxiliaryContentConfigurations];
-[AVAssetDownloadConfiguration downloadsInterstitialAssets];
-[AVAssetDownloadConfiguration initWithAsset:title:];
-[AVAssetDownloadConfiguration isLiveActivityEnabled];
-[AVAssetDownloadConfiguration optimizesAuxiliaryContentConfigurations];
-[AVAssetDownloadConfiguration primaryContentConfiguration];
-[AVAssetDownloadConfiguration setAuxiliaryContentConfigurations:];
-[AVAssetDownloadConfiguration setInterstitialMediaSelectionCriteria:forMediaCharacteristic:];
-[AVAssetDownloadConfiguration setLiveActivityEnabled:];
-[AVAssetDownloadConfiguration setOptimizesAuxiliaryContentConfigurations:];
```
