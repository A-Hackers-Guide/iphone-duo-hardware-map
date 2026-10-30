# `AUHeadTrackingBinauralRenderer`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AUAudioUnit`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _headTracking;
B _disabled;
@"NSString" _deviceUID;
```

## Properties

```
@property (TB,R,N,GisHeadTracking,V_headTracking) headTracking;
@property (TB,R,N,GisDisabled,V_disabled) disabled;
@property (T@"NSString",R,N,V_deviceUID) deviceUID;
```

## Instance methods

```
-[AUHeadTrackingBinauralRenderer deviceUID];
-[AUHeadTrackingBinauralRenderer initWithComponentDescription:options:error:];
-[AUHeadTrackingBinauralRenderer isDisabled];
-[AUHeadTrackingBinauralRenderer setDeviceUID:];
-[AUHeadTrackingBinauralRenderer setDisabled:];
-[AUHeadTrackingBinauralRenderer isHeadTracking];
-[AUHeadTrackingBinauralRenderer setHeadTracking:];
```
