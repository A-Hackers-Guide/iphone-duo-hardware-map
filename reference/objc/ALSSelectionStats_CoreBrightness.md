# `ALSSelectionStats`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
i currentALSOrientation;
i currentALSPlacement;
[12d] deltas;
[18d] time;
[18@"CBHistogramBuilder"] luxTimeHistograms;
f startTime;
f lastEvalTime;
I nSwaps;
@"NSMutableDictionary" samples;
f currentLux;
```

## Instance methods

```
-[ALSSelectionStats init];
-[ALSSelectionStats submit];
-[ALSSelectionStats dealloc];
-[ALSSelectionStats resetStats];
-[ALSSelectionStats calculateIndexForOrientation:placement:];
-[ALSSelectionStats recordALSSwapWithOrientation:andPlacement:andLux:];
-[ALSSelectionStats recordTime];
-[ALSSelectionStats recordTimeForCurrentALS];
-[ALSSelectionStats updateStatsDisplayOff];
-[ALSSelectionStats updateStatsWithOrientation:andLux:andPlacement:];
-[ALSSelectionStats updateTimeWithOrientation:andPlacement:andLux:];
-[ALSSelectionStats validateOrientation:];
-[ALSSelectionStats validatePlacement:];
```
