# `WiFiUsageLQMWindowAnalysis`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 21 properties, 59 instance methods, 8 class methods

## Instance variables

```
@"NSMutableDictionary" dimensions;
Q _osStateHandle;
B _isDone;
B _inCall;
B _hasKernel;
B _inA2dp;
B _inEsco;
@"NSString" _reason;
@"NSDate" _timestamp;
@? _completionHandler;
@"NSDictionary" _summary;
@"NSMutableArray" _subsequentTriggers;
@"NSString" _firstSubsequentLinkDownReason;
@"NSArray" _preceedingTriggers;
@"NSString" _fgApp;
@"NSString" _metricNameCDF;
@"NSString" _metricNameSankey;
@"NSMutableDictionary" _lqmWindowsFeatures;
Q _diceRoll;
@"NSObject<OS_dispatch_source>" _analysisTimer;
@"NSObject<OS_dispatch_queue>" _analysisQueue;
@"WiFiUsageLQMRollingWindow" _windowBeforeTrigger;
@"WiFiUsageLQMRollingWindow" _windowAfterTrigger;
```

## Properties

```
@property (T@"NSString",C,N,V_reason) reason;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (TB,N,V_isDone) isDone;
@property (T@"NSDictionary",&,N,V_summary) summary;
@property (T@"NSMutableArray",&,N,V_subsequentTriggers) subsequentTriggers;
@property (T@"NSString",N,V_firstSubsequentLinkDownReason) firstSubsequentLinkDownReason;
@property (T@"NSArray",&,N,V_preceedingTriggers) preceedingTriggers;
@property (T@"NSString",&,N,V_fgApp) fgApp;
@property (TB,N,V_inCall) inCall;
@property (TQ,N,V_diceRoll) diceRoll;
@property (TB,N,V_hasKernel) hasKernel;
@property (TB,N,V_inA2dp) inA2dp;
@property (TB,N,V_inEsco) inEsco;
@property (T@"NSString",&,N,V_metricNameCDF) metricNameCDF;
@property (T@"NSString",&,N,V_metricNameSankey) metricNameSankey;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_analysisTimer) analysisTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_analysisQueue) analysisQueue;
@property (T@"WiFiUsageLQMRollingWindow",&,N,V_windowBeforeTrigger) windowBeforeTrigger;
@property (T@"WiFiUsageLQMRollingWindow",&,N,V_windowAfterTrigger) windowAfterTrigger;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSMutableDictionary",&,N,V_lqmWindowsFeatures) lqmWindowsFeatures;
```

## Class methods

```
+[WiFiUsageLQMWindowAnalysis config];
+[WiFiUsageLQMWindowAnalysis initialize];
+[WiFiUsageLQMWindowAnalysis updateConfig];
+[WiFiUsageLQMWindowAnalysis canCreateAnalysisFor:];
+[WiFiUsageLQMWindowAnalysis computeFeatures:For:WithLogLabel:];
+[WiFiUsageLQMWindowAnalysis isInCallAnalysisDue:];
+[WiFiUsageLQMWindowAnalysis isKernerlParsingEnabled];
+[WiFiUsageLQMWindowAnalysis maxConcurrentAnalysis];
```

## Instance methods

```
-[WiFiUsageLQMWindowAnalysis fgApp];
-[WiFiUsageLQMWindowAnalysis setFgApp:];
-[WiFiUsageLQMWindowAnalysis setTimestamp:];
-[WiFiUsageLQMWindowAnalysis setCompletionHandler:];
-[WiFiUsageLQMWindowAnalysis addDimensionsTo:];
-[WiFiUsageLQMWindowAnalysis completionHandler];
-[WiFiUsageLQMWindowAnalysis dealloc];
-[WiFiUsageLQMWindowAnalysis timestamp];
-[WiFiUsageLQMWindowAnalysis canSubmitToCA];
-[WiFiUsageLQMWindowAnalysis setSummary:];
-[WiFiUsageLQMWindowAnalysis setReason:];
-[WiFiUsageLQMWindowAnalysis inCall];
-[WiFiUsageLQMWindowAnalysis description];
-[WiFiUsageLQMWindowAnalysis reason];
-[WiFiUsageLQMWindowAnalysis preceedingTriggers];
-[WiFiUsageLQMWindowAnalysis isDone];
-[WiFiUsageLQMWindowAnalysis summary];
-[WiFiUsageLQMWindowAnalysis _generateState];
-[WiFiUsageLQMWindowAnalysis setIsDone:];
-[WiFiUsageLQMWindowAnalysis performAnalysis];
-[WiFiUsageLQMWindowAnalysis dumpDimensions:];
-[WiFiUsageLQMWindowAnalysis analysisQueue];
-[WiFiUsageLQMWindowAnalysis analysisTimer];
-[WiFiUsageLQMWindowAnalysis computeBins:WithSampleKind:];
-[WiFiUsageLQMWindowAnalysis computeFeaturesFor:WithLogLabel:];
-[WiFiUsageLQMWindowAnalysis diceRoll];
-[WiFiUsageLQMWindowAnalysis dumpAnalysis:];
-[WiFiUsageLQMWindowAnalysis fetchKernelLQMRollingWindowForInterface:into:];
-[WiFiUsageLQMWindowAnalysis firstSubsequentLinkDownReason];
-[WiFiUsageLQMWindowAnalysis getBeforeKernelWindowWithLikelyhood];
-[WiFiUsageLQMWindowAnalysis hasKernel];
-[WiFiUsageLQMWindowAnalysis inA2dp];
-[WiFiUsageLQMWindowAnalysis inEsco];
-[WiFiUsageLQMWindowAnalysis initWithRollingWindow:andReason:andContext:andTimestamp:onQueue:];
-[WiFiUsageLQMWindowAnalysis isAnalysisTodo];
-[WiFiUsageLQMWindowAnalysis lqmWindowsFeatures];
-[WiFiUsageLQMWindowAnalysis metricCallbackForMetric:AndField:];
-[WiFiUsageLQMWindowAnalysis metricNameCDF];
-[WiFiUsageLQMWindowAnalysis metricNameSankey];
-[WiFiUsageLQMWindowAnalysis setAnalysisQueue:];
-[WiFiUsageLQMWindowAnalysis setAnalysisTimer:];
-[WiFiUsageLQMWindowAnalysis setDiceRoll:];
-[WiFiUsageLQMWindowAnalysis setFirstSubsequentLinkDownReason:];
-[WiFiUsageLQMWindowAnalysis setHasKernel:];
-[WiFiUsageLQMWindowAnalysis setInA2dp:];
-[WiFiUsageLQMWindowAnalysis setInCall:];
-[WiFiUsageLQMWindowAnalysis setInEsco:];
-[WiFiUsageLQMWindowAnalysis setLqmWindowsFeatures:];
-[WiFiUsageLQMWindowAnalysis setMetricNameCDF:];
-[WiFiUsageLQMWindowAnalysis setMetricNameSankey:];
-[WiFiUsageLQMWindowAnalysis setPreceedingTriggers:];
-[WiFiUsageLQMWindowAnalysis setSubsequentTriggers:];
-[WiFiUsageLQMWindowAnalysis setWindowAfterTrigger:];
-[WiFiUsageLQMWindowAnalysis setWindowBeforeTrigger:];
-[WiFiUsageLQMWindowAnalysis subsequentTriggers];
-[WiFiUsageLQMWindowAnalysis updateWithLQMSample:];
-[WiFiUsageLQMWindowAnalysis updateWithSubsequentTrigger:];
-[WiFiUsageLQMWindowAnalysis windowAfterTrigger];
-[WiFiUsageLQMWindowAnalysis windowBeforeTrigger];
```
