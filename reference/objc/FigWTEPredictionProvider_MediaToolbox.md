# `FigWTEPredictionProvider`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WISServicePredictionProviderDelegate`
- 6 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"WISServicePredictionProvider" predictionProvider;
^{OpaqueFigReentrantMutex=} predictionProviderMutex;
@"<WISServicePrediction>" prediction;
q predictionTimeToStartTime;
i numberOfPredictions;
[5{?="numberOfPredictions"i"servicePredictionType"Q"servicePredictionSource"Q"predictionTime"q"predictedStartTime"q"predictedDuration"i"predictionConfidence"i"startTimeConfidence"i"durationConfidence"i"numPrevPredictions"i"windowStart"q"windowEnd"q}] previousPredictions;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigWTEPredictionProvider dealloc];
-[FigWTEPredictionProvider initWithError:];
-[FigWTEPredictionProvider updateClientStateForSession:to:];
-[FigWTEPredictionProvider copyAllWTEPredictionStats];
-[FigWTEPredictionProvider copyWTEPredictionStatsFromPredictionRecord:];
-[FigWTEPredictionProvider getPredictionRecordSlot];
-[FigWTEPredictionProvider purgeExpiredPredictionRecords:];
-[FigWTEPredictionProvider servicePredictionProvider:didUpdateServicePredictions:];
-[FigWTEPredictionProvider withPredictionProviderMutex:];
```
