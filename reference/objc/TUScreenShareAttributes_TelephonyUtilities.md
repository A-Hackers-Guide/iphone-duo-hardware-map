# `TUScreenShareAttributes`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUScreenShareAttributes`
- 12 instance variables, 16 properties, 33 instance methods, 8 class methods

## Instance variables

```
B _windowed;
q _deviceFamily;
q _deviceHomeButtonType;
@"NSNumber" _displayID;
@"NSNumber" _displayScale;
@"NSNumber" _frameRate;
@"NSValue" _originalResolution;
@"NSNumber" _scaleFactor;
@"NSNumber" _cornerRadius;
q _style;
@"NSUUID" _windowUUID;
@"NSValue" _systemRootLayerTransform;
```

## Properties

```
@property (Tq,N,V_deviceFamily) deviceFamily;
@property (Tq,N,V_deviceHomeButtonType) deviceHomeButtonType;
@property (Tq,N,V_style) style;
@property (T@"NSNumber",&,N,V_displayScale) displayScale;
@property (T@"NSNumber",&,N,V_scaleFactor) scaleFactor;
@property (T@"NSNumber",&,N,V_cornerRadius) cornerRadius;
@property (T@"NSValue",&,N,V_systemRootLayerTransform) systemRootLayerTransform;
@property (T@"NSValue",&,N,V_originalResolution) originalResolution;
@property (T@"NSNumber",&,N,V_frameRate) frameRate;
@property (T@"NSNumber",&,N,V_displayID) displayID;
@property (TB,N,GisWindowed,V_windowed) windowed;
@property (T@"NSUUID",&,N,V_windowUUID) windowUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUScreenShareAttributes defaultAttributes];
+[TUScreenShareAttributes supportsSecureCoding];
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
-[TUScreenShareAttributes encodeWithCoder:];
-[TUScreenShareAttributes hash];
-[TUScreenShareAttributes description];
-[TUScreenShareAttributes initWithCoder:];
-[TUScreenShareAttributes copyWithZone:];
-[TUScreenShareAttributes isEqual:];
-[TUScreenShareAttributes setFrameRate:];
-[TUScreenShareAttributes frameRate];
-[TUScreenShareAttributes setWindowUUID:];
-[TUScreenShareAttributes windowUUID];
-[TUScreenShareAttributes originalResolution];
-[TUScreenShareAttributes setOriginalResolution:];
-[TUScreenShareAttributes isEqualToScreenShareAttributes:];
-[TUScreenShareAttributes deviceHomeButtonType];
-[TUScreenShareAttributes isSignificantChangeFromAttributes:];
-[TUScreenShareAttributes isWindowed];
-[TUScreenShareAttributes setDeviceFamily:];
-[TUScreenShareAttributes setDeviceHomeButtonType:];
-[TUScreenShareAttributes setSystemRootLayerTransform:];
-[TUScreenShareAttributes setWindowed:];
-[TUScreenShareAttributes systemRootLayerTransform];
```
