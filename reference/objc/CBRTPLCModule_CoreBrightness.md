# `CBRTPLCModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
rtplc;
```

## Properties

```
@property (TQ,N,R) state;
@property (T@"NSString",N,R) stateString;
@property (TB,N,R) capApplied;
@property (Tf,N,R) cap;
```

## Instance methods

```
-[CBRTPLCModule init];
-[CBRTPLCModule rampCallback:];
-[CBRTPLCModule exitEDR];
-[CBRTPLCModule enterEDR];
-[CBRTPLCModule stateString];
-[CBRTPLCModule cap];
-[CBRTPLCModule state];
-[CBRTPLCModule capApplied];
-[CBRTPLCModule handleBrightnessUpdateWithSDRNits:andAppliedHeadroom:];
-[CBRTPLCModule initWithQueue:rampRunner:frameStats:displayID:brightnessCap:];
```
