# `AVAssetReader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`
- 1 instance variables, 12 properties, 30 instance methods, 3 class methods

## Instance variables

```
@"AVAssetReaderInternal" _priv;
```

## Properties

```
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{OpaqueFigAssetReader=},R,N,G_figAssetReader) figAssetReader;
@property (TB,N,G_readSingleSample,S_setReadSingleSample:) readSingleSample;
@property (T@"AVAsset",R,&,N) asset;
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (T{?={?=qiIq}{?=qiIq}},N) timeRange;
@property (T@"NSArray",R,N) outputs;
```

## Class methods

```
+[AVAssetReader initialize];
+[AVAssetReader assetReaderWithAsset:error:];
+[AVAssetReader _errorForOSStatus:];
```

## Instance methods

```
-[AVAssetReader outputs];
-[AVAssetReader setTimeRange:];
-[AVAssetReader asset];
-[AVAssetReader timeRange];
-[AVAssetReader _tearDownFigAssetReader];
-[AVAssetReader init];
-[AVAssetReader _outputDidFinish:];
-[AVAssetReader _transitionToStatus:failureError:];
-[AVAssetReader dealloc];
-[AVAssetReader _failWithError:];
-[AVAssetReader _handleServerDiedNotification];
-[AVAssetReader setWindowExtendedTimeRange:];
-[AVAssetReader status];
-[AVAssetReader error];
-[AVAssetReader startReading];
-[AVAssetReader isDefunct];
-[AVAssetReader setPreparesMediaDataForRealTimeConsumption:];
-[AVAssetReader _commonInitWithAsset:options:error:];
-[AVAssetReader initWithAsset:error:];
-[AVAssetReader _canAddOutput:exceptionReason:];
-[AVAssetReader _readSingleSample];
-[AVAssetReader cancelReading];
-[AVAssetReader _setReadSingleSample:];
-[AVAssetReader preparesMediaDataForRealTimeConsumption];
-[AVAssetReader canAddOutput:];
-[AVAssetReader description];
-[AVAssetReader windowExtendedTimeRange];
-[AVAssetReader addOutput:];
-[AVAssetReader _figAssetReader];
-[AVAssetReader initWithAsset:options:error:];
```
