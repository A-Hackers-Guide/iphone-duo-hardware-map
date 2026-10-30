# `PLTimeReferenceKernel`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLTimeReference`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _rebootOccurred;
@"NSDate" _lastSystemTimeRecalibrated;
@"NSDate" _lastKernelTimeRecalibrated;
```

## Properties

```
@property (T@"NSDate",&,V_lastSystemTimeRecalibrated) lastSystemTimeRecalibrated;
@property (T@"NSDate",&,V_lastKernelTimeRecalibrated) lastKernelTimeRecalibrated;
@property (TB,V_rebootOccurred) rebootOccurred;
```

## Instance methods

```
-[PLTimeReferenceKernel resolution];
-[PLTimeReferenceKernel currentTime];
-[PLTimeReferenceKernel getTimebaseInfo];
-[PLTimeReferenceKernel continuousTimeToAbsoluteNs:];
-[PLTimeReferenceKernel initializeOffsetWithEntries:];
-[PLTimeReferenceKernel lastKernelTimeRecalibrated];
-[PLTimeReferenceKernel lastSystemTimeRecalibrated];
-[PLTimeReferenceKernel quarantineWithExitReason:];
-[PLTimeReferenceKernel rebootOccurred];
-[PLTimeReferenceKernel setLastKernelTimeRecalibrated:];
-[PLTimeReferenceKernel setLastSystemTimeRecalibrated:];
-[PLTimeReferenceKernel setRebootOccurred:];
-[PLTimeReferenceKernel setSystemReboot:];
```
