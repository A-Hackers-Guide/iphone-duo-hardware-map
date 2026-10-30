# `AVSmartStyleSettingsState`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bundleID;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSString" _systemStyleKey;
@"NSString" _systemStyleTimestampKey;
@"NSString" _systemStyleEnabledKey;
@"AVCaptureSmartStyle" _systemStyle;
B _systemStyleEnabled;
```

## Class methods

```
+[AVSmartStyleSettingsState _smartStyleSettingsQueue];
+[AVSmartStyleSettingsState smartStyleSettingsStateForBundleID:];
```

## Instance methods

```
-[AVSmartStyleSettingsState dealloc];
-[AVSmartStyleSettingsState systemStyle];
-[AVSmartStyleSettingsState setSystemStyle:];
-[AVSmartStyleSettingsState _proprietaryDefaultChanged:keyPath:];
-[AVSmartStyleSettingsState initForBundleID:];
-[AVSmartStyleSettingsState installProprietaryDefaultListeners];
-[AVSmartStyleSettingsState setSystemStyleEnabled:];
-[AVSmartStyleSettingsState systemStyleEnabled];
```
