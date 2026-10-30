# `BLSHFlipbookPowerSavingProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHFlipbookPowerSavingProviding`
- 5 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<BLSDisplay>" _display;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHFlipbook>" _lock_flipbook;
Q _lock_count;
[8Q] _lock_reasonsCount;
```

## Properties

```
@property (T@"<BLSHFlipbook>",W,N) flipbook;
@property (TB,R,N,GisFlipbookPowerSavingEnabled) flipbookPowerSavingEnabled;
@property (T@"<BLSDisplay>",R,N) display;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHFlipbookPowerSavingProvider display];
-[BLSHFlipbookPowerSavingProvider incrementDisablePowerSavingUsageCountForReason:];
-[BLSHFlipbookPowerSavingProvider initForDisplay:];
-[BLSHFlipbookPowerSavingProvider isFlipbookPowerSavingEnabled];
-[BLSHFlipbookPowerSavingProvider flipbook];
-[BLSHFlipbookPowerSavingProvider description];
-[BLSHFlipbookPowerSavingProvider decrementDisablePowerSavingUsageCountForReason:];
-[BLSHFlipbookPowerSavingProvider lock_description];
-[BLSHFlipbookPowerSavingProvider setFlipbook:];
```
