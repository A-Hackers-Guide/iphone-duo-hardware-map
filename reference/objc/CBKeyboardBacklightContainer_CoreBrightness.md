# `CBKeyboardBacklightContainer`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBContainer`
- Protocols: `CBContainerProtocol`, `CBHIDServiceProtocol`, `CBStatusInfoProtocol`
- 6 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"KeyboardBacklight" _keyboardBacklight;
B _userActive;
@"NSMutableDictionary" _properties;
@"NSObject<CBDisplayModeProvider>" _displayModeProvider;
@"HIDDevice" _device;
```

## Properties

```
@property (T@"NSObject<CBDisplayModeProvider>",&,N,V_displayModeProvider) displayModeProvider;
@property (T@"HIDDevice",R,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBKeyboardBacklightContainer copyPropertyForKey:];
-[CBKeyboardBacklightContainer sendNotificationForKey:andValue:];
-[CBKeyboardBacklightContainer setProperty:forKey:];
-[CBKeyboardBacklightContainer handleEvent:];
-[CBKeyboardBacklightContainer addHIDServiceClient:];
-[CBKeyboardBacklightContainer copyIdentifiers];
-[CBKeyboardBacklightContainer initWithDevice:];
-[CBKeyboardBacklightContainer removeHIDServiceClient:];
-[CBKeyboardBacklightContainer copyPropertyInternalForKey:];
-[CBKeyboardBacklightContainer observeValueForKeyPath:ofObject:change:context:];
-[CBKeyboardBacklightContainer device];
-[CBKeyboardBacklightContainer stop];
-[CBKeyboardBacklightContainer dealloc];
-[CBKeyboardBacklightContainer start];
-[CBKeyboardBacklightContainer setPropertyInternal:forKey:];
-[CBKeyboardBacklightContainer setDisplayModeProvider:];
-[CBKeyboardBacklightContainer displayModeProvider];
-[CBKeyboardBacklightContainer keyboardBacklightInitialization];
-[CBKeyboardBacklightContainer keyboardUsesNitUnits:];
-[CBKeyboardBacklightContainer newKeyboardBacklightWithQueue:device:];
```
