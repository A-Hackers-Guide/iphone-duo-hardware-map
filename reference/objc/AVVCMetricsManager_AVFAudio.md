# `AVVCMetricsManager`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 4 properties, 32 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" mWorkQueue;
@"CAReporter" mMetricsReporter;
q mAudioIssueDetector;
Q mAudioDataAnalysisSiriSession;
@"NSObject<OS_os_transaction>" mADAMTransaction;
B mProfileAVVC;
Q _voiceTriggerStartHostTime;
Q _callToStartRecordHostTime;
@"NSMutableDictionary" _publicMetrics;
@"NSMutableDictionary" _avvcProfilingInfoDictionary;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_publicMetrics) publicMetrics;
@property (T@"NSMutableDictionary",&,V_avvcProfilingInfoDictionary) avvcProfilingInfoDictionary;
@property (TQ,N,V_voiceTriggerStartHostTime) voiceTriggerStartHostTime;
@property (TQ,N,V_callToStartRecordHostTime) callToStartRecordHostTime;
```

## Class methods

```
+[AVVCMetricsManager sharedManager];
+[AVVCMetricsManager getLock];
+[AVVCMetricsManager createSharedManager];
+[AVVCMetricsManager destroySharedManager];
```

## Instance methods

```
-[AVVCMetricsManager init];
-[AVVCMetricsManager dealloc];
-[AVVCMetricsManager reporterID];
-[AVVCMetricsManager retrieveMetrics];
-[AVVCMetricsManager setAvvcProfilingInfoDictionary:];
-[AVVCMetricsManager _disposeADAM];
-[AVVCMetricsManager adamAnalyzeBuffer:numFrames:timeStamp:shouldAnalyze:];
-[AVVCMetricsManager audioIssueDetectorAnalyzeBuffer:numFrames:timeStamp:shouldAnalyze:];
-[AVVCMetricsManager avvcProfilingInfoDictionary];
-[AVVCMetricsManager callToStartRecordHostTime];
-[AVVCMetricsManager checkAndUpdateReporterID:];
-[AVVCMetricsManager disposeADAM];
-[AVVCMetricsManager getStringDate:];
-[AVVCMetricsManager logABCMetric:category:type:reporterID:];
-[AVVCMetricsManager logProfileMetrics:];
-[AVVCMetricsManager logRecordAudioFormat:reporterID:];
-[AVVCMetricsManager logRecordRoute:andPlaybackRoute:reporterID:];
-[AVVCMetricsManager logSessionMetric:value:category:type:context:reporterID:];
-[AVVCMetricsManager logSessionMetric:value:category:type:reporterID:];
-[AVVCMetricsManager logSingleMetric:value:category:type:reporterID:];
-[AVVCMetricsManager measureElapseTimeForMetric:block:];
-[AVVCMetricsManager publicMetrics];
-[AVVCMetricsManager resetAudioIssueDetector];
-[AVVCMetricsManager resetProfileMetrics];
-[AVVCMetricsManager retrieveProfileMetrics];
-[AVVCMetricsManager setADAMFormat:numFrames:];
-[AVVCMetricsManager setAudioIssueDetectorFormat:numFrames:];
-[AVVCMetricsManager setCallToStartRecordHostTime:];
-[AVVCMetricsManager setPublicMetrics:];
-[AVVCMetricsManager setVoiceTriggerStartHostTime:];
-[AVVCMetricsManager updateWithReporterID:];
-[AVVCMetricsManager voiceTriggerStartHostTime];
```
