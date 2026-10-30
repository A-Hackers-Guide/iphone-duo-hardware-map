# `CMOnBodyStatusManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 9 instance methods, 2 class methods

## Instance variables

```
^v fLocationdConnection;
B fSubscribedToOnBodyStatusDetection;
@"NSObject<OS_dispatch_queue>" fOnBodyStatusQueue;
@? fOnBodyStatusHandler;
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
```

## Class methods

```
+[CMOnBodyStatusManager isOnBodyStatusDetectionAvailable];
+[CMOnBodyStatusManager sharedOnBodyStatusManager];
```

## Instance methods

```
-[CMOnBodyStatusManager connect];
-[CMOnBodyStatusManager init];
-[CMOnBodyStatusManager dealloc];
-[CMOnBodyStatusManager disconnect];
-[CMOnBodyStatusManager setPropertiesWithDictionary:];
-[CMOnBodyStatusManager startOnBodyStatusDetectionPrivateToQueue:withParameters:handler:];
-[CMOnBodyStatusManager startOnBodyStatusDetectionToQueue:withParameters:handler:];
-[CMOnBodyStatusManager stopOnBodyStatusDetection];
-[CMOnBodyStatusManager stopOnBodyStatusDetectionPrivate];
```
