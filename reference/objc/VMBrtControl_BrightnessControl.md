# `VMBrtControl`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BCBrtControl`
- 4 instance variables, 0 properties, 16 instance methods, 2 class methods

## Instance variables

```
I _paravirtDisplayService;
^{IONotificationPort=} _terminationPort;
^{?=@?} _terminationCallback;
I _terminationIterator;
```

## Class methods

```
+[VMBrtControl copyAvailableControls];
+[VMBrtControl newMonitorWithHandler:error:];
```

## Instance methods

```
-[VMBrtControl ID];
-[VMBrtControl dealloc];
-[VMBrtControl registryID];
-[VMBrtControl initWithService:];
-[VMBrtControl minNits];
-[VMBrtControl maxNits];
-[VMBrtControl convertArrayValuesUintToFloat:];
-[VMBrtControl convertUintToFloat:];
-[VMBrtControl copyModuleIdentifier];
-[VMBrtControl invalidateForService:];
-[VMBrtControl parseAurora:];
-[VMBrtControl parseCapabilities:];
-[VMBrtControl parseGCP:];
-[VMBrtControl registerForTerminationNotifications];
-[VMBrtControl setDisplayService:];
-[VMBrtControl setNits:error:];
```
