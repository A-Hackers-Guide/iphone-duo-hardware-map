# `TMDisplayModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBDisplayModule`
- 5 instance variables, 1 properties, 32 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _updateQueue;
@"<CBBrightnessProxy>" _brightnessControlProxy;
d _rampStart;
@"BrightnessSequenceQueue" _updateSequence;
```

## Properties

```
@property (TQ,R,D) displayID;
```

## Class methods

```
+[TMDisplayModule newBrightnessUpdateWithDefaultValues];
```

## Instance methods

```
-[TMDisplayModule setContrastPreservation:];
-[TMDisplayModule setPotentialHeadroom:];
-[TMDisplayModule setIndicatorBrightness:];
-[TMDisplayModule setIndicatorBrightnessLimit:];
-[TMDisplayModule copyPropertyForKey:];
-[TMDisplayModule setBrightnessLimit:];
-[TMDisplayModule setHeadroom:];
-[TMDisplayModule setSDRBrightness:];
-[TMDisplayModule setProperty:forKey:];
-[TMDisplayModule setAmbient:];
-[TMDisplayModule setContrastEnhancer:];
-[TMDisplayModule setLowAmbientAdaptation:];
-[TMDisplayModule setFilteredAmbient:];
-[TMDisplayModule setHighAmbientAdaptation:];
-[TMDisplayModule stop];
-[TMDisplayModule setAdaptationScale:];
-[TMDisplayModule dealloc];
-[TMDisplayModule start];
-[TMDisplayModule setReferenceHeadroom:];
-[TMDisplayModule displayID];
-[TMDisplayModule setWhitePoint:];
-[TMDisplayModule setupNextUpdate];
-[TMDisplayModule brightnessControlProxySendSelector:value:];
-[TMDisplayModule commitBrightness];
-[TMDisplayModule commitBrightnessUpdate:];
-[TMDisplayModule configureSkyLightTimeouts];
-[TMDisplayModule finishRamp];
-[TMDisplayModule handleBrightnessControlProperty:forKey:];
-[TMDisplayModule handleDisplayStateChange];
-[TMDisplayModule initWithBrightnessControl:andQueue:];
-[TMDisplayModule rampRoutine:];
-[TMDisplayModule startRamp:];
```
