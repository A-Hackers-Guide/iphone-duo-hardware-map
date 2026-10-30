# `KeyboardBrightnessClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"BrightnessSystemClient" bsc;
@"NSObject<OS_os_log>" _logHandle;
```

## Instance methods

```
-[KeyboardBrightnessClient init];
-[KeyboardBrightnessClient dealloc];
-[KeyboardBrightnessClient isBacklightSaturatedOnKeyboard:];
-[KeyboardBrightnessClient brightnessForKeyboard:];
-[KeyboardBrightnessClient isAmbientFeatureAvailableOnKeyboard:];
-[KeyboardBrightnessClient setBrightness:fadeSpeed:commit:forKeyboard:];
-[KeyboardBrightnessClient suspendIdleDimming:forKeyboard:];
-[KeyboardBrightnessClient backlightLevelForKeyboard:];
-[KeyboardBrightnessClient copyKeyboardBacklightIDs];
-[KeyboardBrightnessClient enableAutoBrightness:forKeyboard:];
-[KeyboardBrightnessClient idleDimTimeForKeyboard:];
-[KeyboardBrightnessClient isAutoBrightnessEnabledForKeyboard:];
-[KeyboardBrightnessClient isBacklightDimmedOnKeyboard:];
-[KeyboardBrightnessClient isBacklightSuppressedOnKeyboard:];
-[KeyboardBrightnessClient isIdleDimmingSuspendedOnKeyboard:];
-[KeyboardBrightnessClient isKeyboardBuiltIn:];
-[KeyboardBrightnessClient registerNotificationForKeys:keyboardID:block:];
-[KeyboardBrightnessClient setBrightness:forKeyboard:];
-[KeyboardBrightnessClient setIdleDimTime:forKeyboard:];
-[KeyboardBrightnessClient unregisterKeyboardNotificationBlock];
```
