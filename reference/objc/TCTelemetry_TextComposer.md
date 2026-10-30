# `TCTelemetry`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _analyticsQueue;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSObject<OS_dispatch_queue>" _dailyBudgetQueue;
@"NSDate" _overriddenCurrentDate;
@"NSMutableArray" _cachedSentenceHashArray;
Q _capacity;
```

## Class methods

```
+[TCTelemetry sharedInstance];
```

## Instance methods

```
-[TCTelemetry init];
-[TCTelemetry _currentDate];
-[TCTelemetry _cacheHitForSentence:];
-[TCTelemetry _consumeProofreadingReviewDailyBudget];
-[TCTelemetry _currentDayIndex];
-[TCTelemetry _errorReasonForError:];
-[TCTelemetry _overrideCurrentDateForDailyBudgetTesting:];
-[TCTelemetry _registerPayload:forEvent:];
-[TCTelemetry _resetProofreadingReviewDailyBudget];
-[TCTelemetry countWords:];
-[TCTelemetry trackPostEditingRequest:inString:offset:tagger:appIdentifier:];
-[TCTelemetry trackProofreadingReviewResults:forString:language:latency:appIdentifier:error:];
-[TCTelemetry trackResponse:toGrammarDetail:language:appIdentifier:];
```
