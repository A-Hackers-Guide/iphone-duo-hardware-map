# `CMDeviceStateManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 13 instance methods, 6 class methods

## Instance variables

```
@ _internal;
```

## Class methods

```
+[CMDeviceStateManager isAvailable];
+[CMDeviceStateManager sharedManager];
+[CMDeviceStateManager computeDeviceStateEventForPropertyA:angle:propertyC:timestamp:continuousTimestamp:];
+[CMDeviceStateManager computeDeviceStateEventForPropertyA:propertyA0:propertyA1:angle:propertyC:timestamp:continuousTimestamp:];
+[CMDeviceStateManager computeDeviceStatePropertiesForPropertyA:propertyBFloat:propertyCBool:outPropertyB:outPropertyC:];
+[CMDeviceStateManager propertyAForDeviceState:configType:];
```

## Instance methods

```
-[CMDeviceStateManager init];
-[CMDeviceStateManager dealloc];
-[CMDeviceStateManager stopUpdates];
-[CMDeviceStateManager deallocPrivate];
-[CMDeviceStateManager onNotification:];
-[CMDeviceStateManager initWithName:];
-[CMDeviceStateManager currentDeviceState];
-[CMDeviceStateManager onDeviceStateData:];
-[CMDeviceStateManager simulateDeviceStateEventForPropertyA:propertyA0:propertyA1:propertyB:propertyC:propertyD:delaySecs:];
-[CMDeviceStateManager startUpdatesPrivateToQueue:withHandler:];
-[CMDeviceStateManager startUpdatesToQueue:withHandler:];
-[CMDeviceStateManager startUpdatesWithProgressToQueue:withHandler:];
-[CMDeviceStateManager stopUpdatesPrivate];
```
