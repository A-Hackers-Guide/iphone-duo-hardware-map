# `BLSHFlipbookFramesHistogram`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 26 properties, 27 instance methods, 2 class methods

## Instance variables

```
f _lowestAPL;
f _averageAPL;
f _medianAPL;
f _highestAPL;
f _lowestAPLDimming;
f _averageAPLDimming;
f _medianAPLDimming;
f _highestAPLDimming;
Q _totalCount;
d _averagePresentationTimeFromNow;
d _medianPresentationTimeFromNow;
@"NSArray" _presentationTimeHistogram;
d _intervalUntilFirstFrame;
d _presentationDuration;
Q _memoryUsage;
Q _averageMemoryUsage;
Q _medianMemoryUsage;
@"NSArray" _memoryUsageHistogram;
```

## Properties

```
@property (T@"NSDictionary",R,N) blsh_analyticsPayload;
@property (TQ,R,N,V_totalCount) totalCount;
@property (Td,R,N,V_averagePresentationTimeFromNow) averagePresentationTimeFromNow;
@property (Td,R,N,V_medianPresentationTimeFromNow) medianPresentationTimeFromNow;
@property (T@"NSArray",R,N,V_presentationTimeHistogram) presentationTimeHistogram;
@property (TI,R,N) countLessThan1Min;
@property (TI,R,N) count1to2Min;
@property (TI,R,N) count2to3Min;
@property (TI,R,N) count3to4Min;
@property (TI,R,N) count4to5Min;
@property (TI,R,N) count5to6Min;
@property (TI,R,N) countMoreThan6Min;
@property (Td,R,N,V_intervalUntilFirstFrame) intervalUntilFirstFrame;
@property (Td,R,N,V_presentationDuration) presentationDuration;
@property (TQ,R,N,V_memoryUsage) memoryUsage;
@property (TQ,R,N,V_averageMemoryUsage) averageMemoryUsage;
@property (TQ,R,N,V_medianMemoryUsage) medianMemoryUsage;
@property (T@"NSArray",R,N,V_memoryUsageHistogram) memoryUsageHistogram;
@property (Tf,R,N,V_lowestAPL) lowestAPL;
@property (Tf,R,N,V_averageAPL) averageAPL;
@property (Tf,R,N,V_medianAPL) medianAPL;
@property (Tf,R,N,V_highestAPL) highestAPL;
@property (Tf,R,N,V_lowestAPLDimming) lowestAPLDimming;
@property (Tf,R,N,V_averageAPLDimming) averageAPLDimming;
@property (Tf,R,N,V_medianAPLDimming) medianAPLDimming;
@property (Tf,R,N,V_highestAPLDimming) highestAPLDimming;
```

## Class methods

```
+[BLSHFlipbookFramesHistogram histogramWithReferenceDate:flipbookFrames:];
+[BLSHFlipbookFramesHistogram histogramWithReferenceDate:iteratePresentationDatesBlock:];
```

## Instance methods

```
-[BLSHFlipbookFramesHistogram totalCount];
-[BLSHFlipbookFramesHistogram presentationDuration];
-[BLSHFlipbookFramesHistogram description];
-[BLSHFlipbookFramesHistogram memoryUsage];
-[BLSHFlipbookFramesHistogram averageAPL];
-[BLSHFlipbookFramesHistogram averageAPLDimming];
-[BLSHFlipbookFramesHistogram count1to2Min];
-[BLSHFlipbookFramesHistogram count2to3Min];
-[BLSHFlipbookFramesHistogram count3to4Min];
-[BLSHFlipbookFramesHistogram count4to5Min];
-[BLSHFlipbookFramesHistogram count5to6Min];
-[BLSHFlipbookFramesHistogram countLessThan1Min];
-[BLSHFlipbookFramesHistogram countMoreThan6Min];
-[BLSHFlipbookFramesHistogram highestAPL];
-[BLSHFlipbookFramesHistogram highestAPLDimming];
-[BLSHFlipbookFramesHistogram intervalUntilFirstFrame];
-[BLSHFlipbookFramesHistogram lowestAPL];
-[BLSHFlipbookFramesHistogram lowestAPLDimming];
-[BLSHFlipbookFramesHistogram presentationTimeHistogram];
-[BLSHFlipbookFramesHistogram averageMemoryUsage];
-[BLSHFlipbookFramesHistogram averagePresentationTimeFromNow];
-[BLSHFlipbookFramesHistogram blsh_analyticsPayload];
-[BLSHFlipbookFramesHistogram medianAPL];
-[BLSHFlipbookFramesHistogram medianAPLDimming];
-[BLSHFlipbookFramesHistogram medianMemoryUsage];
-[BLSHFlipbookFramesHistogram medianPresentationTimeFromNow];
-[BLSHFlipbookFramesHistogram memoryUsageHistogram];
```
