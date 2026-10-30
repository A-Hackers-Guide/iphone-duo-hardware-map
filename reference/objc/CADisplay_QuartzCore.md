# `CADisplay`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 55 properties, 93 instance methods, 5 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSArray",R,N) availableModes;
@property (T@"CADisplayMode",&,N) currentMode;
@property (T@"CADisplayMode",R,N) preferredMode;
@property (T@"NSString",C,N) colorMode;
@property (TB) allowsVirtualModes;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) safeBounds;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) deviceName;
@property (TI,R,N) displayId;
@property (Tq,R,N) displayType;
@property (TI,R,N) seed;
@property (TI,R,N) connectionSeed;
@property (T@"NSString",R,N) uniqueId;
@property (T@"NSUUID",R,N) UUID;
@property (T@"NSString",R,N) containerId;
@property (TB,R,N,GisSupported) supported;
@property (Tq,R,N) tag;
@property (Ti,R,N) processId;
@property (TB,R,N,GisExternal) external;
@property (Td,R,N) refreshRate;
@property (Td,R,N) heartbeatRate;
@property (Tq,R,N) minimumFrameDuration;
@property (TB,R,N) hasNativeFrameRateRequest;
@property (TB,R,N) supportsVariableFrameDuration;
@property (TB,R,N,GisOverscanned) overscanned;
@property (T@"NSString",C,N) overscanAdjustment;
@property (Td,R,N) overscanAmount;
@property (T{CGSize=dd},R,N) overscanAmounts;
@property (T{CGSize=dd},R,N) logicalScale;
@property (TQ,R,N) pointScale;
@property (Td,R,N) minimumLogicalScale;
@property (Td,R,N) maximumLogicalScale;
@property (TB,R,N,GisCloned) cloned;
@property (TB,R,N,GisCloning) cloning;
@property (TB,R,N,GisCloningSupported) cloningSupported;
@property (T@"NSString",R,N) nativeOrientation;
@property (T@"NSString",R,N) currentOrientation;
@property (TI,R,N) odLUTVersion;
@property (TB,R,N) supportsExtendedColors;
@property (T@"CADisplayAttributes",R,N) externalDisplayAttributes;
@property (Ti,R,N) linkQuality;
@property (Td,N) latency;
@property (T@"CADisplayPreferences",C,N) preferences;
@property (T@"NSString",R,N) productName;
@property (T{CGSize=dd},R,N) physicalSize;
@property (T{CGSize=dd},R,N) nativeSize;
@property (T{CGSize=dd},R,N) pixelsPerInch;
@property (T@"NSString",R,N) transportType;
@property (T@"CADisplayPreset",&,N) currentPreset;
@property (TB,R,N) isReference;
@property (TB,R,N) isReferenceLimited;
@property (Tf,R,N) autoLuminanceBoost;
@property (TB,N,GisForceFixedRateLinksEnabled) forceFixedRateLinksEnabled;
```

## Class methods

```
+[CADisplay displays];
+[CADisplay automaticallyNotifiesObserversForKey:];
+[CADisplay TVOutDisplay];
+[CADisplay mainDisplay];
+[CADisplay updateDisplays];
```

## Instance methods

```
-[CADisplay overrideDisplayTimings:];
-[CADisplay allowsVirtualModes];
-[CADisplay allowedHDRModes];
-[CADisplay setLatency:];
-[CADisplay _getSecureIndicatorSteadyDeadlineForType:kind:deadline:];
-[CADisplay safeBounds];
-[CADisplay currentOrientation];
-[CADisplay _initWithDisplay:];
-[CADisplay supportedHDRModes];
-[CADisplay isOverscanned];
-[CADisplay stateControl];
-[CADisplay seed];
-[CADisplay flipBookWithOptions:];
-[CADisplay isCloned];
-[CADisplay heartbeatRate];
-[CADisplay latency];
-[CADisplay connectionSeed];
-[CADisplay setAllowsVirtualModes:];
-[CADisplay isExternal];
-[CADisplay highestLocalPreferredFrameRateRequest];
-[CADisplay colorMode];
-[CADisplay _postNotification:];
-[CADisplay _notifyDisallowedLayersChange:];
-[CADisplay currentMode];
-[CADisplay _copyDebugProperties];
-[CADisplay preferredMode];
-[CADisplay externalDisplayAttributes];
-[CADisplay nativeOrientation];
-[CADisplay overscanAmount];
-[CADisplay refreshRate];
-[CADisplay displayType];
-[CADisplay minimumLogicalScale];
-[CADisplay setOverscanAdjustment:];
-[CADisplay preferredFrameRateRangeForVelocity:];
-[CADisplay hasNativeFrameRateRequest];
-[CADisplay supportedHDRModesWithCriteria:];
-[CADisplay odLUTVersion];
-[CADisplay availableModes];
-[CADisplay overscanAmounts];
-[CADisplay setForceFixedRateLinksEnabled:];
-[CADisplay _availableModesInternal];
-[CADisplay isCloning];
-[CADisplay immutableCopy];
-[CADisplay isForceFixedRateLinksEnabled];
-[CADisplay timingsControl];
-[CADisplay isReference];
-[CADisplay preferredFrameRateRangeForMaximumVelocity:];
-[CADisplay setPreferences:];
-[CADisplay _finalize];
-[CADisplay processId];
-[CADisplay isCloningSupported];
-[CADisplay physicalSize];
-[CADisplay overscanAdjustment];
-[CADisplay update];
-[CADisplay isReferenceLimited];
-[CADisplay preferredHDRModes];
-[CADisplay pixelsPerInch];
-[CADisplay productName];
-[CADisplay supportsExtendedColors];
-[CADisplay setDisallowedLayersCallback:];
-[CADisplay preferredModeWithCriteria:];
-[CADisplay displayId];
-[CADisplay autoLuminanceBoost];
-[CADisplay availablePresets];
-[CADisplay _invalidate];
-[CADisplay currentPreset];
-[CADisplay setDisplayProperties:];
-[CADisplay supportsVariableFrameDuration];
-[CADisplay hardwareRefreshRate];
-[CADisplay pointScale];
-[CADisplay isSupported];
-[CADisplay UUID];
-[CADisplay logicalScale];
-[CADisplay preferences];
-[CADisplay nativeSize];
-[CADisplay setColorMode:];
-[CADisplay setCurrentPreset:];
-[CADisplay maximumLogicalScale];
-[CADisplay minimumFrameDuration];
-[CADisplay dealloc];
-[CADisplay setCurrentMode:];
-[CADisplay overrideMinimumFrameDuration:];
-[CADisplay _silmgrId];
-[CADisplay containerId];
-[CADisplay transportType];
-[CADisplay linkQuality];
-[CADisplay uniqueId];
-[CADisplay tag];
-[CADisplay bounds];
-[CADisplay description];
-[CADisplay deviceName];
-[CADisplay name];
-[CADisplay frame];
```
