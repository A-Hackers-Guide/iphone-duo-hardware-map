# `DisparityDiagnostics`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"NSMutableDictionary" _diagDict;
```

## Class methods

```
+[DisparityDiagnostics dictFromAdaptiveCorrectionStatus:];
+[DisparityDiagnostics dictFromCalModel:];
+[DisparityDiagnostics dictFromDistortionModel:];
```

## Instance methods

```
-[DisparityDiagnostics init];
-[DisparityDiagnostics addShiftmapRaw:];
-[DisparityDiagnostics addAdaptiveCorrectionStatus:];
-[DisparityDiagnostics addDisparityDebugStatus:];
-[DisparityDiagnostics addMinShift:maxShift:];
-[DisparityDiagnostics addShiftmapJPEG:];
-[DisparityDiagnostics clearDiagnostics];
-[DisparityDiagnostics createDiagnosticsDictionary];
```
