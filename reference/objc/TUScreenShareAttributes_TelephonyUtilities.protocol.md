# `TUScreenShareAttributes` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSSecureCoding`, `NSCopying`
- 0 instance variables, 18 properties, 26 instance methods, 7 class methods

## Properties

```
@property (Tq,N) deviceFamily;
@property (Tq,N) deviceHomeButtonType;
@property (Tq,N) style;
@property (T@"NSNumber",&,N) displayScale;
@property (T@"NSNumber",&,N) scaleFactor;
@property (T@"NSNumber",&,N) cornerRadius;
@property (T@"NSValue",&,N) systemRootLayerTransform;
@property (T@"NSValue",&,N) originalResolution;
@property (T@"NSNumber",&,N) frameRate;
@property (T@"NSNumber",&,N) displayID;
@property (TB,N,GisWindowed) windowed;
@property (T@"NSUUID",&,N) windowUUID;
@property (class, Tq,R,N) currentDeviceFamily;
@property (class, Tq,R,N) currentDeviceHomeButtonType;
@property (class, T@"NSNumber",R,C,N) defaultDisplayScale;
@property (class, T@"NSNumber",R,C,N) defaultScaleFactor;
@property (class, T@"NSNumber",R,C,N) defaultCornerRadius;
@property (class, T@"NSValue",R,C,N) defaultSystemRootLayerTransform;
```

## Class methods

```
+[TUScreenShareAttributes defaultAttributes];
+[TUScreenShareAttributes defaultCornerRadius];
+[TUScreenShareAttributes defaultSystemRootLayerTransform];
+[TUScreenShareAttributes defaultDisplayScale];
+[TUScreenShareAttributes currentDeviceFamily];
+[TUScreenShareAttributes currentDeviceHomeButtonType];
+[TUScreenShareAttributes defaultScaleFactor];
```

## Instance methods

```
-[TUScreenShareAttributes setDisplayID:];
-[TUScreenShareAttributes initWithAttributes:];
-[TUScreenShareAttributes deviceFamily];
-[TUScreenShareAttributes setDisplayScale:];
-[TUScreenShareAttributes setScaleFactor:];
-[TUScreenShareAttributes displayScale];
-[TUScreenShareAttributes displayID];
-[TUScreenShareAttributes style];
-[TUScreenShareAttributes setCornerRadius:];
-[TUScreenShareAttributes setStyle:];
-[TUScreenShareAttributes scaleFactor];
-[TUScreenShareAttributes cornerRadius];
-[TUScreenShareAttributes setFrameRate:];
-[TUScreenShareAttributes frameRate];
-[TUScreenShareAttributes setWindowUUID:];
-[TUScreenShareAttributes windowUUID];
-[TUScreenShareAttributes originalResolution];
-[TUScreenShareAttributes setOriginalResolution:];
-[TUScreenShareAttributes deviceHomeButtonType];
-[TUScreenShareAttributes isSignificantChangeFromAttributes:];
-[TUScreenShareAttributes isWindowed];
-[TUScreenShareAttributes setDeviceFamily:];
-[TUScreenShareAttributes setDeviceHomeButtonType:];
-[TUScreenShareAttributes setSystemRootLayerTransform:];
-[TUScreenShareAttributes setWindowed:];
-[TUScreenShareAttributes systemRootLayerTransform];
```
