# `SBPlatformController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _defaultIconState;
@"NSOrderedSet" _defaultIconStateDisplayIdentifiers;
@"NSString" _localizedDeviceName;
B _isRoundCornerPhone;
B _isRoundCornerPad;
B _internalInstall;
B _carrierInstall;
B _supportsHWButtonBezelEffects;
B _isButterflyCapable;
q _medusaCapabilities;
```

## Class methods

```
+[SBPlatformController sharedInstance];
```

## Instance methods

```
-[SBPlatformController isInternalInstall];
-[SBPlatformController uniqueDeviceIdentifier];
-[SBPlatformController isCarrierInstall];
-[SBPlatformController hardwareModel];
-[SBPlatformController deviceClass];
-[SBPlatformController init];
-[SBPlatformController isHomeGestureEnabled];
-[SBPlatformController productType];
-[SBPlatformController defaultIconState];
-[SBPlatformController supportsMultiwindow];
-[SBPlatformController systemBuildVersion];
-[SBPlatformController deviceSupportsHingeInteractions];
-[SBPlatformController isMedusaCapable];
-[SBPlatformController _loadDefaultIconInfo];
-[SBPlatformController defaultIconStateDisplayIdentifiers];
-[SBPlatformController deviceSupportsHWButtonBezelEffects];
-[SBPlatformController isButterflyCapable];
-[SBPlatformController isRoundCornerPad];
-[SBPlatformController isRoundCornerPhone];
-[SBPlatformController isiPadMini];
-[SBPlatformController localizedPlatformName];
-[SBPlatformController medusaCapabilities];
```
