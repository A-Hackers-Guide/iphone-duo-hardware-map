# `CMSensorRecorderInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fInternalQueue;
^v fLocationdConnection;
```

## Instance methods

```
-[CMSensorRecorderInternal init];
-[CMSensorRecorderInternal dealloc];
-[CMSensorRecorderInternal teardown];
-[CMSensorRecorderInternal _newMetaUsingMessage:withIdentifier:forType:];
-[CMSensorRecorderInternal newDataByID:metaID:forType:];
-[CMSensorRecorderInternal newMetaByID:forType:];
-[CMSensorRecorderInternal newMetaFrom:to:forType:];
-[CMSensorRecorderInternal newMetaSinceID:forType:];
-[CMSensorRecorderInternal setSensorSampleRate:forType:];
-[CMSensorRecorderInternal writeSensorDataToFile:from:to:forType:];
```
