# `CMSwimTracker`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"CMSwimTrackerInternal" _internal;
```

## Properties

```
@property (T@"CMSwimTrackerInternal",R,N,V_internal) _internal;
```

## Class methods

```
+[CMSwimTracker isAvailable];
+[CMSwimTracker maxSwimDataEntries];
```

## Instance methods

```
-[CMSwimTracker _internal];
-[CMSwimTracker init];
-[CMSwimTracker dealloc];
-[CMSwimTracker stopUpdates];
-[CMSwimTracker startUpdatesFromRecord:handler:];
-[CMSwimTracker querySWOLFSummaryWithSessionID:handler:];
-[CMSwimTracker querySwimUpdatesFromRecord:handler:];
```
