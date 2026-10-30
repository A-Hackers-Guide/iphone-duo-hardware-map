# `TCTerminationEstimator`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _language;
^{CoreLanguageModelWithState=} _coreLM;
@"NSObject<OS_os_transaction>" _coreLMTransaction;
@"NSMutableDictionary" _cachedTerminationEstimateDictionary;
@"NSMutableArray" _cachedSentenceArray;
@"NSTimer" _idleTimer;
d _coreLMLastTime;
Q _coreLMCount;
f _threshold;
```

## Instance methods

```
-[TCTerminationEstimator dealloc];
-[TCTerminationEstimator idleTimerFired:];
-[TCTerminationEstimator resetIdleTimer];
-[TCTerminationEstimator initWithLanguage:];
-[TCTerminationEstimator loadModel];
-[TCTerminationEstimator terminationEstimateForSentence:];
-[TCTerminationEstimator analyzeSentenceAsPotentiallyTerminated:];
-[TCTerminationEstimator computedTerminationEstimateForSentence:];
-[TCTerminationEstimator resetModel];
```
