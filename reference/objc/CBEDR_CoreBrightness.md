# `CBEDR`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 33 instance methods, 6 class methods

## Instance variables

```
Q _rampPolicy;
f _currentMaxBrightness;
f _panelMax;
f _brightnessCap;
f _sdrBrightness;
f _minHeadroom;
f _maxHeadroom;
f _secondsPerStop;
f _secondsPerStopExit;
f _referenceHeadroom;
f _requestedHeadroom;
f _currentHeadroom;
@"CBEDRModulator" _headroomModulator;
```

## Properties

```
@property (Tf,V_panelMax) panelMax;
@property (Tf,V_brightnessCap) brightnessCap;
@property (Tf,V_sdrBrightness) sdrBrightness;
@property (Tf,V_minHeadroom) minHeadroom;
@property (Tf,V_maxHeadroom) maxHeadroom;
@property (Tf,V_secondsPerStop) secondsPerStop;
@property (Tf,V_secondsPerStopExit) secondsPerStopExit;
@property (Tf,R,V_referenceHeadroom) referenceHeadroom;
@property (Tf,R,V_requestedHeadroom) requestedHeadroom;
@property (Tf,R,V_currentHeadroom) currentHeadroom;
@property (Tf,R) appliedHeadroom;
@property (Tf,R) availableHeadroom;
@property (T@"CBEDRModulator",&,V_headroomModulator) headroomModulator;
```

## Class methods

```
+[CBEDR animatedHeadroomForOrigin:target:andProgress:];
+[CBEDR headroomToScalingFactor:];
+[CBEDR headroomToStops:];
+[CBEDR overallRampDuration:target:durationPerStop:];
+[CBEDR scalingFactorToHeadroom:];
+[CBEDR stopsToHeadroom:];
```

## Instance methods

```
-[CBEDR copyStatusInfo];
-[CBEDR setHeadroomModulator:];
-[CBEDR secondsPerStop];
-[CBEDR clampHeadroom:];
-[CBEDR setMinHeadroom:];
-[CBEDR secondsPerStopExit];
-[CBEDR setSecondsPerStopExit:];
-[CBEDR dealloc];
-[CBEDR brightnessCap];
-[CBEDR setSdrBrightness:];
-[CBEDR headroomModulator];
-[CBEDR setPanelMax:];
-[CBEDR requestedHeadroom];
-[CBEDR setBrightnessCap:];
-[CBEDR setMaxHeadroom:];
-[CBEDR rampCallback:];
-[CBEDR maxHeadroom];
-[CBEDR appliedHeadroom];
-[CBEDR cappedHeadroomFromUncapped:];
-[CBEDR referenceHeadroom];
-[CBEDR availableHeadroom];
-[CBEDR description];
-[CBEDR shouldUpdateEDRForRequestedHeadroom:targetHeadroom:];
-[CBEDR resetRequestedHeadroom];
-[CBEDR currentHeadroom];
-[CBEDR shouldUpdateEDRForRequestedHeadroom:targetHeadroom:rampTime:];
-[CBEDR panelMax];
-[CBEDR minHeadroom];
-[CBEDR setSecondsPerStop:];
-[CBEDR initWithRampPolicy:potentialHeadroom:andReferenceHeadroom:];
-[CBEDR shouldUpdateEDRForRequestedHeadroom:targetHeadroom:rampTime:durationPerStop:];
-[CBEDR sdrBrightness];
-[CBEDR sanityCheck];
```
