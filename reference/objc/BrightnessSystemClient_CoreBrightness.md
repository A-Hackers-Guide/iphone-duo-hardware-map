# `BrightnessSystemClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 1 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSObject<BSCIProtocol>" bsci;
@"NSObject<OS_os_log>" _logHandle;
B _isRunning;
@? _displayNotificationBlock;
@? _keyboardNotificationBlock;
@? _propertyNotificationBlock;
@"NSHashTable" _observers;
@"NSMutableSet" _observedKeys;
Q _observersCount;
@"NSString" _clientID;
```

## Properties

```
@property (T@"NSString",R,N,V_clientID) clientID;
```

## Instance methods

```
-[BrightnessSystemClient copyPropertyForKey:];
-[BrightnessSystemClient setProperty:forKey:];
-[BrightnessSystemClient clientID];
-[BrightnessSystemClient registerNotificationBlock:];
-[BrightnessSystemClient init];
-[BrightnessSystemClient dealloc];
-[BrightnessSystemClient activateWithError:];
-[BrightnessSystemClient initWithClientID:];
-[BrightnessSystemClient registerNotificationBlock:forProperties:];
-[BrightnessSystemClient registerObserver:];
-[BrightnessSystemClient cancel];
-[BrightnessSystemClient unregisterObserver:];
-[BrightnessSystemClient unregisterNotificationForKey:];
-[BrightnessSystemClient setProperty:withKey:keyboardID:];
-[BrightnessSystemClient setProperty:withKey:andDisplay:];
-[BrightnessSystemClient copyPropertyForKey:andDisplay:];
-[BrightnessSystemClient copyPropertyForKey:keyboardID:];
-[BrightnessSystemClient copyPropertyForKey:withHandle:error:];
-[BrightnessSystemClient deliverNotificationToObservers:andValue:handle:];
-[BrightnessSystemClient initWithClientID:andBackend:];
-[BrightnessSystemClient isAlsSupported];
-[BrightnessSystemClient observerSlug:];
-[BrightnessSystemClient refreshKeys];
-[BrightnessSystemClient registerDisplayNotificationCallbackBlock:];
-[BrightnessSystemClient registerKeyboardNotificationCallbackBlock:];
-[BrightnessSystemClient registerNotificationForKey:];
-[BrightnessSystemClient registerNotificationForKey:andDisplay:];
-[BrightnessSystemClient registerNotificationForKeys:];
-[BrightnessSystemClient registerNotificationForKeys:andDisplay:];
-[BrightnessSystemClient registerNotificationForKeys:keyboardID:];
-[BrightnessSystemClient setProperty:forKey:withHandle:error:];
-[BrightnessSystemClient setSyncProperty:forKey:withHandle:error:];
-[BrightnessSystemClient unregisterDisplayNotificationBlock];
-[BrightnessSystemClient unregisterKeyboardNotificationBlock];
-[BrightnessSystemClient unregisterNotificationForKey:andDisplay:];
-[BrightnessSystemClient unregisterNotificationForKeys:];
-[BrightnessSystemClient unregisterNotificationForKeys:andDisplay:];
-[BrightnessSystemClient unregisterNotificationForKeys:keyboardID:];
-[BrightnessSystemClient unregisterPropertyNotificationBlock];
```
