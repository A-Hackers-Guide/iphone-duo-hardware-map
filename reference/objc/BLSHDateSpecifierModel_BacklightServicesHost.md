# `BLSHDateSpecifierModel`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<BLSHInactiveBudgetPolicing_Private>" _inactiveBudgetPolicy;
@"NSMapTable" _environmentModels;
@"NSHashTable" _observers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[BLSHDateSpecifierModel removeObserver:];
-[BLSHDateSpecifierModel addObserver:];
-[BLSHDateSpecifierModel isEmpty];
-[BLSHDateSpecifierModel clearSpecifiersForEnvironment:];
-[BLSHDateSpecifierModel initWithInactiveBudgetPolicy:];
-[BLSHDateSpecifierModel missingAnySpecifiersInDateInterval:forPresentation:];
-[BLSHDateSpecifierModel missingIntervalsForMinimumInterval:requestInterval:ofPresentation:];
-[BLSHDateSpecifierModel purgeSpecifiersBefore:];
-[BLSHDateSpecifierModel registerSpecifiers:forDateInterval:environment:];
-[BLSHDateSpecifierModel updatesAfterSpecifier:coalesceFirstUpdateToNowDate:plusRenderEarlyEpsilon:untilGapOverDuration:coaelscingEpsilon:maximumUpdates:lastValidDate:forPresentation:environmentFilter:];
```
