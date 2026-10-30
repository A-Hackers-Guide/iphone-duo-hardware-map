# `WiFiUsageLQMWindowAnalysisLinkDown`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMWindowAnalysis`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _isInvoluntary;
@"NSString" _linkDownReason;
q _linkDownSubreason;
Q _linkUpDuration;
```

## Properties

```
@property (TB,N,V_isInvoluntary) isInvoluntary;
@property (T@"NSString",&,N,V_linkDownReason) linkDownReason;
@property (Tq,N,V_linkDownSubreason) linkDownSubreason;
@property (TQ,N,V_linkUpDuration) linkUpDuration;
```

## Instance methods

```
-[WiFiUsageLQMWindowAnalysisLinkDown addDimensionsTo:];
-[WiFiUsageLQMWindowAnalysisLinkDown initWithRollingWindow:WithIsInvoluntary:AndLinkChangeReason:AndLinkChangeSubreason:AndDuration:andContext:AndTimestamp:onQueue:];
-[WiFiUsageLQMWindowAnalysisLinkDown isInvoluntary];
-[WiFiUsageLQMWindowAnalysisLinkDown linkDownReason];
-[WiFiUsageLQMWindowAnalysisLinkDown linkDownSubreason];
-[WiFiUsageLQMWindowAnalysisLinkDown linkUpDuration];
-[WiFiUsageLQMWindowAnalysisLinkDown setIsInvoluntary:];
-[WiFiUsageLQMWindowAnalysisLinkDown setLinkDownReason:];
-[WiFiUsageLQMWindowAnalysisLinkDown setLinkDownSubreason:];
-[WiFiUsageLQMWindowAnalysisLinkDown setLinkUpDuration:];
```
