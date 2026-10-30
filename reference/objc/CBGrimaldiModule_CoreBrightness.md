# `CBGrimaldiModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 17 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _currentRLuxOutputDict;
@"NSDictionary" _lastRLuxOutputDict;
@"NSMutableDictionary" _overriddenInput;
B _overriding;
@"NSSet" _validKeys;
@"NSNumber" _lastLux;
d _correctionFactor;
Q _samplingTime;
c _currentNumSamples;
B _sampleOnce;
B _sampleMultiple;
B _started;
B _coexStrobe;
B _coexJasper;
@"<CBGrimaldiEventSource>" _eventSource;
@"<CBGrimaldiSamplingStrategy>" _samplingStrategy;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (TB,R) strobeCoex;
@property (TB,R) jasperCoex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBGrimaldiModule copyPropertyForKey:];
-[CBGrimaldiModule setProperty:forKey:];
-[CBGrimaldiModule stop];
-[CBGrimaldiModule dealloc];
-[CBGrimaldiModule start];
-[CBGrimaldiModule sendNotificationForKey:withValue:];
-[CBGrimaldiModule handleNotificationForKey:withProperty:];
-[CBGrimaldiModule copyPropertyForKey:withParameter:];
-[CBGrimaldiModule timerCallback];
-[CBGrimaldiModule copyGainChanged];
-[CBGrimaldiModule copyReliableLux];
-[CBGrimaldiModule clearOutput];
-[CBGrimaldiModule copyJasperCoex];
-[CBGrimaldiModule copyParam:];
-[CBGrimaldiModule copyRearLux];
-[CBGrimaldiModule copyStrobeCoex];
-[CBGrimaldiModule grimaldiLuxReceived:];
-[CBGrimaldiModule initWithQueue:andEventSource:andSamplingStrategy:];
-[CBGrimaldiModule jasperCoex];
-[CBGrimaldiModule setGrimaldiLux];
-[CBGrimaldiModule startSingleSample];
-[CBGrimaldiModule startWithFrequency:];
-[CBGrimaldiModule startWithFrequency:singleSample:];
-[CBGrimaldiModule strobeCoex];
```
