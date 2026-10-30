# `FudProgressWeights`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
f prepareWeight;
f applyWeight;
f finishWeight;
```

## Properties

```
@property (Tf,VprepareWeight) prepareWeight;
@property (Tf,VapplyWeight) applyWeight;
@property (Tf,VfinishWeight) finishWeight;
```

## Instance methods

```
-[FudProgressWeights description];
-[FudProgressWeights setApplyWeight:];
-[FudProgressWeights applyWeight];
-[FudProgressWeights calculateOverallProgressWithStepProgress:step:];
-[FudProgressWeights finishWeight];
-[FudProgressWeights initWithPrepareWeight:applyWeight:finishWeight:];
-[FudProgressWeights prepareWeight];
-[FudProgressWeights setFinishWeight:];
-[FudProgressWeights setPrepareWeight:];
```
