# `SBPIPAnalyticsSourceSummaryAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPIPAnalyticsAssistant`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _PIPBecameActive;
d _possibleDuration;
d _possibleTimestamp;
```

## Instance methods

```
-[SBPIPAnalyticsSourceSummaryAssistant invalidate];
-[SBPIPAnalyticsSourceSummaryAssistant analyticsIdentifier];
-[SBPIPAnalyticsSourceSummaryAssistant _generateMutableAnalyticsPayload];
-[SBPIPAnalyticsSourceSummaryAssistant initWithBundleIdentifier:contentType:isAutoPIPEnabled:invalidationBlock:];
-[SBPIPAnalyticsSourceSummaryAssistant noteBecameActiveAtTime:];
-[SBPIPAnalyticsSourceSummaryAssistant notePIPBecamePossibleAtTime:];
-[SBPIPAnalyticsSourceSummaryAssistant notePIPBecameProhibitedAtTime:];
```
