# `CMHealthTracker`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 4 class methods

## Instance variables

```
@"CMHealthTrackerInternal" _internal;
```

## Properties

```
@property (T@"CMHealthTrackerInternal",R,N,V_internal) _internal;
```

## Class methods

```
+[CMHealthTracker isAuthorizedForMetMinutes];
+[CMHealthTracker isAuthorizedForVO2MaxData];
+[CMHealthTracker isMetMinutesAvailable];
+[CMHealthTracker isVO2MaxDataAvailable];
```

## Instance methods

```
-[CMHealthTracker _internal];
-[CMHealthTracker init];
-[CMHealthTracker dealloc];
-[CMHealthTracker queryMetMinutesFromDate:toDate:handler:];
-[CMHealthTracker queryVO2MaxInputsFromRecord:handler:];
```
