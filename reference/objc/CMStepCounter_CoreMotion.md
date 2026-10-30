# `CMStepCounter`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"CMStepCounterProxy" _stepcounterProxy;
```

## Properties

```
@property (T@"CMStepCounterProxy",R,N,V_stepcounterProxy) stepcounterProxy;
@property (TB) enabled;
```

## Class methods

```
+[CMStepCounter isStepCountingAvailable];
```

## Instance methods

```
-[CMStepCounter enabled];
-[CMStepCounter init];
-[CMStepCounter dealloc];
-[CMStepCounter setEnabled:];
-[CMStepCounter deleteHistory];
-[CMStepCounter getTotalCountToQueue:withHandler:];
-[CMStepCounter queryStepCountStartingFrom:to:toQueue:withHandler:];
-[CMStepCounter startStepCountingUpdatesToQueue:updateOn:withHandler:];
-[CMStepCounter stepcounterProxy];
-[CMStepCounter stopStepCountingUpdates];
```
