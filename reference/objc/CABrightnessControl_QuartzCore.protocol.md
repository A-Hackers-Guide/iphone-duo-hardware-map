# `CABrightnessControl` (protocol)

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `CABrightnessTransaction`
- 0 instance variables, 14 properties, 26 instance methods, 0 class methods

## Properties

```
@property (TI,R) displayId;
@property (Tq,R) displayType;
@property (TQ,R,N) productId;
@property (TQ,R,N) vendorId;
@property (T@"NSUUID",R,N) uuid;
@property (TB,R,N) brightnessAvailable;
@property (TB,R,N) whitePointAvailable;
@property (TB,R,N) whitePointD50XYZ;
@property (T@"NSDictionary",R,N) brightnessCapabilities;
@property (TI,R,N) serviceObject;
@property (Td,N) maximumHDRLuminance;
@property (Td,N) maximumSDRLuminance;
@property (Td,N) minimumLuminance;
@property (Td,N) maximumReferenceLuminance;
```

## Instance methods

```
-[CABrightnessControl setMaximumSDRLuminance:];
-[CABrightnessControl setSyncNotificationQueue:];
-[CABrightnessControl serviceObject];
-[CABrightnessControl registerForNotifications:withBlock:];
-[CABrightnessControl whitePointD50XYZ];
-[CABrightnessControl minimumLuminance];
-[CABrightnessControl setNotificationQueue:];
-[CABrightnessControl brightnessAvailable];
-[CABrightnessControl unregisterNotificationBlocks];
-[CABrightnessControl productId];
-[CABrightnessControl setMinimumLuminance:];
-[CABrightnessControl maximumSDRLuminance];
-[CABrightnessControl brightnessCapabilities];
-[CABrightnessControl maximumHDRLuminance];
-[CABrightnessControl setWhitePoint:rampDuration:error:];
-[CABrightnessControl whitePointAvailable];
-[CABrightnessControl vendorId];
-[CABrightnessControl abortWhitePointRamp:error:];
-[CABrightnessControl setMaximumHDRLuminance:];
-[CABrightnessControl registerForSyncNotifications:withBlock:];
-[CABrightnessControl maximumReferenceLuminance];
-[CABrightnessControl displayType];
-[CABrightnessControl unregisterSyncNotificationBlocks];
-[CABrightnessControl uuid];
-[CABrightnessControl displayId];
-[CABrightnessControl setMaximumReferenceLuminance:];
```
