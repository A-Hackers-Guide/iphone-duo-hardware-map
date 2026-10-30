# `CBDisplayModuleHIDiOS`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBDisplayModule`
- Protocols: `CBDisplayModeProtocol`, `CBContainerModuleProtocol`
- 20 instance variables, 7 properties, 29 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDDevice=} _hidDisplayDevice;
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSUUID" _containerID;
^{__IOHIDElement=} _brightnessElement;
^{__IOHIDElement=} _durationElement;
@"NSArray" _elements;
f _minNits;
f _maxNits;
f _currentNits;
f _nitsScaler;
f _minLinearBrightness;
@"NSObject<OS_dispatch_queue>" _brightnessUpdateQueue;
Q _brightnessUpdateCounter;
f _brightnessUpdateTarget;
Q _displayVID;
Q _displayPID;
q _displayMode;
Q _VID;
Q _PID;
```

## Properties

```
@property (TQ,R,V_VID) VID;
@property (TQ,R,V_PID) PID;
@property (Tq,V_displayMode) displayMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBDisplayModuleHIDiOS copyPropertyForKey:];
-[CBDisplayModuleHIDiOS handleDisplayModeUpdate:withDuration:callback:];
-[CBDisplayModuleHIDiOS setProperty:forKey:];
-[CBDisplayModuleHIDiOS setNits:];
-[CBDisplayModuleHIDiOS copyIdentifiers];
-[CBDisplayModuleHIDiOS copyPropertyInternalForKey:];
-[CBDisplayModuleHIDiOS setDisplayMode:];
-[CBDisplayModuleHIDiOS stop];
-[CBDisplayModuleHIDiOS dealloc];
-[CBDisplayModuleHIDiOS displayMode];
-[CBDisplayModuleHIDiOS setSlider:];
-[CBDisplayModuleHIDiOS start];
-[CBDisplayModuleHIDiOS sendNotificationForKey:withValue:];
-[CBDisplayModuleHIDiOS handleNotificationForKey:withProperty:];
-[CBDisplayModuleHIDiOS copyPropertyForKey:withParameter:];
-[CBDisplayModuleHIDiOS PID];
-[CBDisplayModuleHIDiOS VID];
-[CBDisplayModuleHIDiOS handleDisplayProductIDProperty:];
-[CBDisplayModuleHIDiOS getLinearBrightness];
-[CBDisplayModuleHIDiOS getNits:];
-[CBDisplayModuleHIDiOS getNitsForUserBrightness:];
-[CBDisplayModuleHIDiOS getUserBrightnessForNits:];
-[CBDisplayModuleHIDiOS handleDisplayBrightnessProperty:];
-[CBDisplayModuleHIDiOS handleDisplayLinearBrightnessProperty:];
-[CBDisplayModuleHIDiOS handleDisplayVendorIDProperty:];
-[CBDisplayModuleHIDiOS initWithDevice:andQueue:];
-[CBDisplayModuleHIDiOS newDisplayBrightnessData];
-[CBDisplayModuleHIDiOS setLinearBrightness:];
-[CBDisplayModuleHIDiOS setNits:withPeriod:];
```
