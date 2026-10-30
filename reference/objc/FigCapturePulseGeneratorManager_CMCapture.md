# `FigCapturePulseGeneratorManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCapturePulseGeneratorManagerDelegate`
- 5 instance variables, 5 properties, 7 instance methods, 4 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSObject<OS_dispatch_queue>" _operationQueue;
I _lastPulseGeneratorID;
@"NSMutableArray" _pulseGenerators;
@"FigCapturePulseGenerator" _activePulseGenerator;
```

## Properties

```
@property (T@"FigCapturePulseGenerator",N) activePulseGenerator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FigCapturePulseGeneratorManager initialize];
+[FigCapturePulseGeneratorManager _isSupported];
+[FigCapturePulseGeneratorManager _anyCaptureSourceSupportsMSG];
+[FigCapturePulseGeneratorManager sharedPulseGeneratorManager];
```

## Instance methods

```
-[FigCapturePulseGeneratorManager init];
-[FigCapturePulseGeneratorManager dealloc];
-[FigCapturePulseGeneratorManager activePulseGenerator];
-[FigCapturePulseGeneratorManager invalidatePulseGenerator:];
-[FigCapturePulseGeneratorManager newPulseGenerator];
-[FigCapturePulseGeneratorManager performOperationForPulseGenerator:block:];
-[FigCapturePulseGeneratorManager setActivePulseGenerator:];
```
