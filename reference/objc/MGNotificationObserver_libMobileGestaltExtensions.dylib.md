# `MGNotificationObserver`

- Image: [`/usr/lib/libMobileGestaltExtensions.dylib`](../userland/usr__lib__libMobileGestaltExtensions.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `MCProfileConnectionObserver`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _blocks;
i _type;
@"NSString" _argument;
(?="_darwinTokens"@"NSMutableArray""_scPrefs"^{__SCPreferences}"_mcConnection"@"MCProfileConnection""_mainDisplay"@"CADisplay""_ctCenter"^{__CTServerConnection}"_scdynaStore"^{__SCDynamicStore}) _registration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MGNotificationObserver observeValueForKeyPath:ofObject:change:context:];
-[MGNotificationObserver _cancelRegistration];
-[MGNotificationObserver profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[MGNotificationObserver initWithType:argument:];
-[MGNotificationObserver dealloc];
-[MGNotificationObserver _addBlock:];
-[MGNotificationObserver profileConnectionDidReceiveRestrictionChangedNotification:userInfo:];
-[MGNotificationObserver startDynaStoreMonitoringWithArgument:];
-[MGNotificationObserver invokeBlocks];
-[MGNotificationObserver copyWithZone:];
-[MGNotificationObserver _removeBlock:];
```
