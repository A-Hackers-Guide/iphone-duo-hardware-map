# `SSRAssetManager`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSLanguageCodeUpdateMonitorDelegate`
- 8 instance variables, 12 properties, 34 instance methods, 2 class methods

## Instance variables

```
@"<SSRAssetManagerDelegate>" _delegate;
@"NSArray" _assetProviders;
@"NSString" _currentLanguageCode;
@"CSOnDeviceCompilationHandler" _onDeviceCompilationHandler;
@"NSMutableSet" _compiledAssets;
@"<SSRAssetProviding>" _mobileAssetProvider;
@"<SSRAssetProviding>" _uafAssetProvider;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSArray",&,N,V_assetProviders) assetProviders;
@property (T@"NSString",&,N,V_currentLanguageCode) currentLanguageCode;
@property (T@"CSOnDeviceCompilationHandler",&,N,V_onDeviceCompilationHandler) onDeviceCompilationHandler;
@property (T@"NSMutableSet",&,N,V_compiledAssets) compiledAssets;
@property (T@"<SSRAssetProviding>",&,N,V_mobileAssetProvider) mobileAssetProvider;
@property (T@"<SSRAssetProviding>",&,N,V_uafAssetProvider) uafAssetProvider;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<SSRAssetManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SSRAssetManager sharedManager];
+[SSRAssetManager sharedManagerOnDeviceCompilationDisable];
```

## Instance methods

```
-[SSRAssetManager CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:];
-[SSRAssetManager init];
-[SSRAssetManager dealloc];
-[SSRAssetManager start];
-[SSRAssetManager queue];
-[SSRAssetManager setDelegate:];
-[SSRAssetManager onDeviceCompilationHandler];
-[SSRAssetManager delegate];
-[SSRAssetManager setOnDeviceCompilationHandler:];
-[SSRAssetManager setQueue:];
-[SSRAssetManager currentLanguageCode];
-[SSRAssetManager setCurrentLanguageCode:];
-[SSRAssetManager allInstalledSpeakerRecognitionAssetsForLanguage:];
-[SSRAssetManager getSpeakerRecognitionAssetWithLanguage:completion:];
-[SSRAssetManager installedSpeakerRecognitionAssetForLanguage:];
-[SSRAssetManager _compileAssets:];
-[SSRAssetManager _compileCurrentInstalledAssets:];
-[SSRAssetManager _allInstalledSpeakerRecognitionAssetsForLanguage:];
-[SSRAssetManager _convertVersionStringToFloat:];
-[SSRAssetManager _getSSRAssetFromMAProviderWithLanguage:];
-[SSRAssetManager _getSpeakerRecognitionOverrideAsset];
-[SSRAssetManager _loadUAFAssetsIfNecessary];
-[SSRAssetManager allInstalledAssetsOfType:forLanguage:];
-[SSRAssetManager assetProviders];
-[SSRAssetManager compiledAssets];
-[SSRAssetManager initWithOnDeviceCompilationDisable:];
-[SSRAssetManager installedAssetOfType:forLanguage:];
-[SSRAssetManager mobileAssetProvider];
-[SSRAssetManager releaseAssetsLocksIfNecessary];
-[SSRAssetManager setAssetProviders:];
-[SSRAssetManager setCompiledAssets:];
-[SSRAssetManager setMobileAssetProvider:];
-[SSRAssetManager setUafAssetProvider:];
-[SSRAssetManager uafAssetProvider];
```
