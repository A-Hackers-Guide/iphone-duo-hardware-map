# `TUCallScreenShareAttributes`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUScreenShareAttributes`
- 12 instance variables, 16 properties, 34 instance methods, 9 class methods

## Instance variables

```
B _windowed;
q _deviceFamily;
q _deviceHomeButtonType;
q _style;
@"NSNumber" _displayScale;
@"NSValue" _systemRootLayerTransform;
@"NSNumber" _scaleFactor;
@"NSNumber" _cornerRadius;
@"NSNumber" _frameRate;
@"NSNumber" _displayID;
@"NSValue" _originalResolution;
@"NSUUID" _windowUUID;
```

## Properties

```
@property (Tq,N,V_deviceFamily) deviceFamily;
@property (Tq,N,V_deviceHomeButtonType) deviceHomeButtonType;
@property (Tq,N,V_style) style;
@property (T@"NSNumber",&,N,V_displayScale) displayScale;
@property (T@"NSValue",&,N,V_systemRootLayerTransform) systemRootLayerTransform;
@property (T@"NSNumber",&,N,V_scaleFactor) scaleFactor;
@property (T@"NSNumber",&,N,V_cornerRadius) cornerRadius;
@property (T@"NSNumber",&,N,V_frameRate) frameRate;
@property (T@"NSNumber",&,N,V_displayID) displayID;
@property (T@"NSValue",&,N,V_originalResolution) originalResolution;
@property (TB,N,GisWindowed,V_windowed) windowed;
@property (T@"NSUUID",&,N,V_windowUUID) windowUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallScreenShareAttributes defaultAttributes];
+[TUCallScreenShareAttributes supportsSecureCoding];
+[TUCallScreenShareAttributes defaultCornerRadius];
+[TUCallScreenShareAttributes defaultSystemRootLayerTransform];
+[TUCallScreenShareAttributes defaultDisplayScale];
+[TUCallScreenShareAttributes currentDeviceFamily];
+[TUCallScreenShareAttributes currentDeviceHomeButtonType];
+[TUCallScreenShareAttributes originalResolutionWithContentScale:contentRect:displayScale:];
+[TUCallScreenShareAttributes defaultScaleFactor];
```

## Instance methods

```
-[TUCallScreenShareAttributes setDisplayID:];
-[TUCallScreenShareAttributes initWithAttributes:];
-[TUCallScreenShareAttributes deviceFamily];
-[TUCallScreenShareAttributes setDisplayScale:];
-[TUCallScreenShareAttributes setScaleFactor:];
-[TUCallScreenShareAttributes displayScale];
-[TUCallScreenShareAttributes displayID];
-[TUCallScreenShareAttributes style];
-[TUCallScreenShareAttributes setCornerRadius:];
-[TUCallScreenShareAttributes setStyle:];
-[TUCallScreenShareAttributes scaleFactor];
-[TUCallScreenShareAttributes cornerRadius];
-[TUCallScreenShareAttributes encodeWithCoder:];
-[TUCallScreenShareAttributes hash];
-[TUCallScreenShareAttributes description];
-[TUCallScreenShareAttributes initWithCoder:];
-[TUCallScreenShareAttributes copyWithZone:];
-[TUCallScreenShareAttributes isEqual:];
-[TUCallScreenShareAttributes setFrameRate:];
-[TUCallScreenShareAttributes frameRate];
-[TUCallScreenShareAttributes setWindowUUID:];
-[TUCallScreenShareAttributes windowUUID];
-[TUCallScreenShareAttributes originalResolution];
-[TUCallScreenShareAttributes setOriginalResolution:];
-[TUCallScreenShareAttributes isEqualToScreenShareAttributes:];
-[TUCallScreenShareAttributes deviceHomeButtonType];
-[TUCallScreenShareAttributes isSignificantChangeFromAttributes:];
-[TUCallScreenShareAttributes isWindowed];
-[TUCallScreenShareAttributes setDeviceFamily:];
-[TUCallScreenShareAttributes setDeviceHomeButtonType:];
-[TUCallScreenShareAttributes setResolutionAttributesWithContentScale:contentRect:displayScale:];
-[TUCallScreenShareAttributes setSystemRootLayerTransform:];
-[TUCallScreenShareAttributes setWindowed:];
-[TUCallScreenShareAttributes systemRootLayerTransform];
```
