# `BLSHInternalTapToRadarDialog`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"BLSHTapToRadarDescriptor" _descriptor;
@"NSObject<OS_os_log>" _log;
@? _completion;
```

## Properties

```
@property (T@"BLSHTapToRadarDescriptor",R,N,V_descriptor) descriptor;
```

## Instance methods

```
-[BLSHInternalTapToRadarDialog descriptor];
-[BLSHInternalTapToRadarDialog _cancel];
-[BLSHInternalTapToRadarDialog presentWithCompletion:];
-[BLSHInternalTapToRadarDialog _ignore];
-[BLSHInternalTapToRadarDialog _alertDidDismiss:];
-[BLSHInternalTapToRadarDialog _file];
-[BLSHInternalTapToRadarDialog _gotError];
-[BLSHInternalTapToRadarDialog _shouldIgnore];
-[BLSHInternalTapToRadarDialog callCompletion:shouldTryAgain:];
-[BLSHInternalTapToRadarDialog initWithDescriptor:log:];
```
