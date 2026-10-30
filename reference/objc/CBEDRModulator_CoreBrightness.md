# `CBEDRModulator`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
B _enabled;
@"NSArray" _headroomDataPointsConfig;
@"NSArray" _nitsDataPointsConfig;
```

## Properties

```
@property (TB,N,V_enabled) enabled;
@property (T@"NSArray",&,V_nitsDataPointsConfig) nitsDataPointsConfig;
@property (T@"NSArray",&,V_headroomDataPointsConfig) headroomDataPointsConfig;
```

## Instance methods

```
-[CBEDRModulator enabled];
-[CBEDRModulator init];
-[CBEDRModulator dealloc];
-[CBEDRModulator setEnabled:];
-[CBEDRModulator description];
-[CBEDRModulator isConfigured];
-[CBEDRModulator headroomDataPointsConfig];
-[CBEDRModulator modulatedHeadroom:forHeadroom:forSDRNits:];
-[CBEDRModulator nitsDataPointsConfig];
-[CBEDRModulator setHeadroomDataPointsConfig:];
-[CBEDRModulator setNitsDataPointsConfig:];
```
