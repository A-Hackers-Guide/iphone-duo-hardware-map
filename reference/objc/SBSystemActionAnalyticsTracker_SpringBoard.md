# `SBSystemActionAnalyticsTracker`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBSystemActionSuppressionStatus" _suppressionStatus;
@"NSString" _lastQueriedActionIdentifier;
@"NSString" _lastQueriedParameterValueIdentifier;
@"NSDate" _lastQueryTimestamp;
d _buttonInteractionDownEventTime;
d _buttonInteractionDownEventDeliveryTime;
@"NSObject<OS_dispatch_queue>" _powerLogSendQueue;
```

## Instance methods

```
-[SBSystemActionAnalyticsTracker init];
-[SBSystemActionAnalyticsTracker _logSignificantTimeChanged];
-[SBSystemActionAnalyticsTracker _openCameraActionIdentifier];
-[SBSystemActionAnalyticsTracker _sendEventToPowerLog:payload:];
```
