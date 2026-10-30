# `BKMatchPearlOperation`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKMatchOperation`
- 7 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _longTimeout;
B _shouldAutoRetry;
B _preAugmentationCheck;
B _fullFaceOnly;
B _nonDelayedIndicator;
@"BKIdentity" _preAugmentationCheckIdentity;
Q _trigger;
```

## Properties

```
@property (T@"<BKMatchPearlOperationDelegate>",W,D,N) delegate;
@property (TB,N,V_longTimeout) longTimeout;
@property (TB,N,V_shouldAutoRetry) shouldAutoRetry;
@property (TB,N,V_preAugmentationCheck) preAugmentationCheck;
@property (T@"BKIdentity",&,N,V_preAugmentationCheckIdentity) preAugmentationCheckIdentity;
@property (TB,N,V_fullFaceOnly) fullFaceOnly;
@property (TQ,N,V_trigger) trigger;
@property (TB,N,V_nonDelayedIndicator) nonDelayedIndicator;
```

## Instance methods

```
-[BKMatchPearlOperation trigger];
-[BKMatchPearlOperation statusMessage:client:];
-[BKMatchPearlOperation statusMessage:details:client:];
-[BKMatchPearlOperation setTrigger:];
-[BKMatchPearlOperation setLongTimeout:];
-[BKMatchPearlOperation shouldAutoRetry];
-[BKMatchPearlOperation enableAutoRetry:error:];
-[BKMatchPearlOperation setShouldAutoRetry:];
-[BKMatchPearlOperation startNewMatchAttemptWithError:];
-[BKMatchPearlOperation fullFaceOnly];
-[BKMatchPearlOperation longTimeout];
-[BKMatchPearlOperation matchResultInfoWithServerIdentity:details:];
-[BKMatchPearlOperation nonDelayedIndicator];
-[BKMatchPearlOperation optionsDictionaryWithError:];
-[BKMatchPearlOperation pauseFaceDetectTimer:error:];
-[BKMatchPearlOperation preAugmentationCheck];
-[BKMatchPearlOperation preAugmentationCheckIdentity];
-[BKMatchPearlOperation setFullFaceOnly:];
-[BKMatchPearlOperation setNonDelayedIndicator:];
-[BKMatchPearlOperation setPreAugmentationCheck:];
-[BKMatchPearlOperation setPreAugmentationCheckIdentity:];
```
