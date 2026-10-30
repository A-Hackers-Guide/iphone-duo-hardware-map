# `SBPIPAnalyticsSessionSummaryAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPIPAnalyticsAssistant`
- 6 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
d _stashedDuration;
d _stashedTimestamp;
q _numberOfStashEvents;
B _restoredFullScreen;
B _startedAutomatically;
B _appStoppedSession;
```

## Instance methods

```
-[SBPIPAnalyticsSessionSummaryAssistant invalidate];
-[SBPIPAnalyticsSessionSummaryAssistant analyticsIdentifier];
-[SBPIPAnalyticsSessionSummaryAssistant _generateMutableAnalyticsPayload];
-[SBPIPAnalyticsSessionSummaryAssistant initWithBundleIdentifier:contentType:isAutoPIPEnabled:invalidationBlock:];
-[SBPIPAnalyticsSessionSummaryAssistant noteAppStoppedSession:];
-[SBPIPAnalyticsSessionSummaryAssistant noteBecameStashedAtTime:];
-[SBPIPAnalyticsSessionSummaryAssistant noteBecameUnstashedAtTime:];
-[SBPIPAnalyticsSessionSummaryAssistant noteRestoredFullScreen:];
-[SBPIPAnalyticsSessionSummaryAssistant noteStartedAutomatically:];
```
