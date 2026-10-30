# `BCAppleBacklightBrtControl`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BCBrtControl`
- 16 instance variables, 1 properties, 14 instance methods, 2 class methods

## Instance variables

```
I _backlightService;
I _dispService;
d _minUser;
d _maxUser;
d _minMilliAmps;
d _maxMilliAmps;
d _maxNitsEDR;
B _isDFR;
B _isDCP;
B _override;
B _energySaving;
Q _thermalMitigation;
^{?=@?} _terminationCallback;
^{IONotificationPort=} _terminationNotifPort;
I _terminationIterator;
@"<CBPrimitiveConfigurationProvider>" provider;
```

## Properties

```
@property (TQ,R) registryID;
```

## Class methods

```
+[BCAppleBacklightBrtControl copyAvailableControls];
+[BCAppleBacklightBrtControl newMonitorWithHandler:error:];
```

## Instance methods

```
-[BCAppleBacklightBrtControl ID];
-[BCAppleBacklightBrtControl init];
-[BCAppleBacklightBrtControl dealloc];
-[BCAppleBacklightBrtControl copyProperty:error:];
-[BCAppleBacklightBrtControl description];
-[BCAppleBacklightBrtControl registryID];
-[BCAppleBacklightBrtControl initWithService:];
-[BCAppleBacklightBrtControl copyModuleIdentifier];
-[BCAppleBacklightBrtControl getNitsWithError:];
-[BCAppleBacklightBrtControl parseAABCapCurve:];
-[BCAppleBacklightBrtControl parseColorCapabilities];
-[BCAppleBacklightBrtControl setDisplayService:];
-[BCAppleBacklightBrtControl setNits:error:];
-[BCAppleBacklightBrtControl setProperty:value:error:];
```
