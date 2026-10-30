# `CFXAnalyticsManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXAnalyticsManager`
- 3 instance variables, 2 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queryDataQueue;
@"NSMutableArray" _analyticsDurationData_queryDataQueue;
@"CFXPickerSession" _currentPickerSession;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_analyticsDurationData_queryDataQueue) analyticsDurationData_queryDataQueue;
@property (T@"CFXPickerSession",&,N,V_currentPickerSession) currentPickerSession;
```

## Class methods

```
+[CFXAnalyticsManager sharedInstance];
```

## Instance methods

```
-[CFXAnalyticsManager init];
-[CFXAnalyticsManager isDistribution:];
-[CFXAnalyticsManager pickerDidScroll];
-[CFXAnalyticsManager CFX_allowedPickerIdentifier:];
-[CFXAnalyticsManager CFX_composedAnalyticsKeyWithAnimoji:video:frontCamera:effectType:];
-[CFXAnalyticsManager pickerDidChangePresentationMode];
-[CFXAnalyticsManager addAnalyticsDurationData:];
-[CFXAnalyticsManager analyticsDurationData];
-[CFXAnalyticsManager analyticsDurationData_queryDataQueue];
-[CFXAnalyticsManager checkIfEventExistsWithName:];
-[CFXAnalyticsManager currentPickerSession];
-[CFXAnalyticsManager dictionaryWithEventName:value:];
-[CFXAnalyticsManager didSelectEffectOfType:effectIsNone:];
-[CFXAnalyticsManager isIncrementScalar:];
-[CFXAnalyticsManager persistAnalyticsDataWithEventName:value:];
-[CFXAnalyticsManager removeAnalyticsDurationDataItems:];
-[CFXAnalyticsManager roundWithNumber:];
-[CFXAnalyticsManager setAnalyticsDurationData_queryDataQueue:];
-[CFXAnalyticsManager setCurrentPickerSession:];
-[CFXAnalyticsManager startTrackingPickerWithIdentifier:];
-[CFXAnalyticsManager startTrackingTimeIntervalEventWithName:];
-[CFXAnalyticsManager stopTrackingPickerWithIdentifier:];
-[CFXAnalyticsManager stopTrackingTimeIntervalEventWithName:];
-[CFXAnalyticsManager trackAnimojiWithEffectId:];
-[CFXAnalyticsManager trackEffect:];
-[CFXAnalyticsManager trackEmojiStickerWithEffectId:];
-[CFXAnalyticsManager trackEventWithName:];
-[CFXAnalyticsManager trackEventWithName:count:];
-[CFXAnalyticsManager trackEventWithName:duration:];
-[CFXAnalyticsManager trackEventWithName:supportsHDR:isHDR:];
-[CFXAnalyticsManager trackFilterWithEffectId:];
-[CFXAnalyticsManager trackKey:supportsHDR:isHDR:];
-[CFXAnalyticsManager trackKey:withDuration:];
-[CFXAnalyticsManager trackKey:withEffectId:];
-[CFXAnalyticsManager trackLabelWithEffectId:];
-[CFXAnalyticsManager trackMediaSentWithAnimoji:video:frontCamera:filterCount:labelCount:messagesStickerCount:shapeCount:emojiStickerCount:supportsHDR:isHDR:];
-[CFXAnalyticsManager trackMessagesStickerWithEffectId:];
-[CFXAnalyticsManager trackShapeWithEffectId:];
```
