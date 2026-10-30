# `CBClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"BrightnessSystemClient" bsc;
B _activated;
@"CBBlueLightClient" _blueLightClient;
@"CBAdaptationClient" _adaptationClient;
@? _stateObserver;
```

## Properties

```
@property (T@"CBBlueLightClient",R,V_blueLightClient) blueLightClient;
@property (T@"CBAdaptationClient",R,V_adaptationClient) adaptationClient;
@property (T@?,C,V_stateObserver) stateObserver;
```

## Class methods

```
+[CBClient supportsAdaptation];
+[CBClient supportsBlueLightReduction];
```

## Instance methods

```
-[CBClient init];
-[CBClient dealloc];
-[CBClient activateWithError:];
-[CBClient initWithClientID:];
-[CBClient cancel];
-[CBClient newDisplayClientForID:withError:];
-[CBClient blueLightClient];
-[CBClient adaptationClient];
-[CBClient setStateObserver:];
-[CBClient stateObserver];
-[CBClient newDisplayClientForUniqueID:withError:];
-[CBClient newDisplayClientForUUID:withError:];
```
