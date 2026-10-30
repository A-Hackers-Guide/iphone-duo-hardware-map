# `CBSoftWakeDisplayDelegate`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
q _state;
{__DisplayFactorFade="period"d"startTime"d"Ftarget"f"Fcurrent"f"Fstart"f"coeff"[3f]"rampDoneCallback"^?"refcon"^v} _fade;
```

## Properties

```
@property (T^{__DisplayFactorFade=ddfff[3f]^?^v},R,N) fade;
```

## Class methods

```
+[CBSoftWakeDisplayDelegate isSupported];
```

## Instance methods

```
-[CBSoftWakeDisplayDelegate init];
-[CBSoftWakeDisplayDelegate dealloc];
-[CBSoftWakeDisplayDelegate isActive];
-[CBSoftWakeDisplayDelegate fade];
-[CBSoftWakeDisplayDelegate action:];
-[CBSoftWakeDisplayDelegate setFactor:withFade:];
```
