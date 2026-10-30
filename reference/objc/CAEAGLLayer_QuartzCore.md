# `CAEAGLLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `EAGLDrawable`
- 1 instance variables, 8 properties, 25 instance methods, 2 class methods

## Instance variables

```
^{_CAEAGLNativeWindow={_EAGLNativeWindowObject=iI^?^?^?^?^?^?^?}^v^?^?^?^?^{x_list_struct}IQ{Atomic={?=i}}{Atomic={?=i}}{SpinLock={?=i}}^{_CAImageQueue}@dd^{x_list_struct}I^{CAEAGLBuffer}^{CAEAGLBuffer}III^{CAEAGLBuffer}@{Atomic={?=i}}Qb1b1b1b1} _win;
```

## Properties

```
@property (T^{_EAGLNativeWindowObject=iI^?^?^?^?^?^?^?},R) nativeWindow;
@property (TB,GisAsynchronous) asynchronous;
@property (TQ) maximumDrawableCount;
@property (TB) lowLatency;
@property (Td) inputTime;
@property (Td) drawableTimeoutSeconds;
@property (TB) presentsWithTransaction;
@property (T@"NSDictionary",C) drawableProperties;
```

## Class methods

```
+[CAEAGLLayer defaultValueForKey:];
+[CAEAGLLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAEAGLLayer isDrawableAvailable];
-[CAEAGLLayer didChangeValueForKey:];
-[CAEAGLLayer isAsynchronous];
-[CAEAGLLayer dealloc];
-[CAEAGLLayer setLowLatency:];
-[CAEAGLLayer lowLatency];
-[CAEAGLLayer layerDidBecomeVisible:];
-[CAEAGLLayer shouldArchiveValueForKey:];
-[CAEAGLLayer discardContents];
-[CAEAGLLayer _defersDidBecomeVisiblePostCommit];
-[CAEAGLLayer _didCommitLayer:];
-[CAEAGLLayer _display];
-[CAEAGLLayer drawableProperties];
-[CAEAGLLayer drawableTimeoutSeconds];
-[CAEAGLLayer inputTime];
-[CAEAGLLayer isDrawableAvailableInternal];
-[CAEAGLLayer maximumDrawableCount];
-[CAEAGLLayer nativeWindow];
-[CAEAGLLayer presentsWithTransaction];
-[CAEAGLLayer setAsynchronous:];
-[CAEAGLLayer setDrawableProperties:];
-[CAEAGLLayer setDrawableTimeoutSeconds:];
-[CAEAGLLayer setInputTime:];
-[CAEAGLLayer setMaximumDrawableCount:];
-[CAEAGLLayer setPresentsWithTransaction:];
```
