# `BWPortraitAutoSuggest`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _shallowDepthOfFieldRenderingEnabled;
B _portTypeIsFFC;
B _doSuggest;
B _lastDoSuggest;
I _validityCounter;
I _validObjectCounterOld;
I _invalidityCounter;
f _validObjectIntervalThSec;
I _validObjectIntervalTh;
f _fadeValidThInvalidityActiveSec;
I _fadeValidThInvalidityActive;
f _fadeValidThInvalidityBuildSec;
I _fadeValidThInvalidityBuild;
f _fadeInvalidThCst;
f _fadeValidThCst;
f _objectFrameRatio;
I _objectBoxFrameAreaValidityRatio;
I _objectBoxFrameAreaValidityRatioWhenOn;
I _marginInRatioWidth;
I _marginInRatioHeight;
I _marginOutRatioWidth;
I _marginOutRatioHeight;
I _temporalValidityTh;
I _fadeValidTh;
I _fadeInvalidTh;
f _objectCentersLookbackIntervalSec;
I _objectCentersLookbackInterval;
I _maxMotionThreshold;
I _minMotionThreshold;
f _xObjectCenterStdTh;
f _yObjectCenterStdTh;
@"NSMutableArray" _trackers;
```

## Properties

```
@property (TB,N,V_shallowDepthOfFieldRenderingEnabled) shallowDepthOfFieldRenderingEnabled;
@property (TB,N,V_portTypeIsFFC) portTypeIsFFC;
```

## Class methods

```
+[BWPortraitAutoSuggest initialize];
```

## Instance methods

```
-[BWPortraitAutoSuggest dealloc];
-[BWPortraitAutoSuggest initWithTuningParameters:];
-[BWPortraitAutoSuggest portTypeIsFFC];
-[BWPortraitAutoSuggest runAutoSuggestionWithSampleBuffer:portraitSceneMonitorStatus:];
-[BWPortraitAutoSuggest setPortTypeIsFFC:];
-[BWPortraitAutoSuggest setShallowDepthOfFieldRenderingEnabled:];
-[BWPortraitAutoSuggest shallowDepthOfFieldRenderingEnabled];
```
