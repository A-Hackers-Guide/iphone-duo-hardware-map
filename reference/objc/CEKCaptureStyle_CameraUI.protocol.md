# `CEKCaptureStyle` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisNeutral) neutral;
@property (TB,R,N,GisCustomizable) customizable;
@property (TB,R,N,GisCustomized) customized;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) presetDisplayName;
@property (T@"NSDictionary",R,N) dictionaryRepresentation;
@property (T@"NSDictionary",R,N) analyticsDictionaryForCapture;
@property (T@"NSDictionary",R,N) analyticsDictionaryForPreferences;
```

## Instance methods

```
-[CEKCaptureStyle analyticsDictionaryForPreferences];
-[CEKCaptureStyle displayName];
-[CEKCaptureStyle presetDisplayName];
-[CEKCaptureStyle isCustomized];
-[CEKCaptureStyle isNeutral];
-[CEKCaptureStyle analyticsDictionaryForCapture];
-[CEKCaptureStyle isCustomizable];
-[CEKCaptureStyle dictionaryRepresentation];
```
