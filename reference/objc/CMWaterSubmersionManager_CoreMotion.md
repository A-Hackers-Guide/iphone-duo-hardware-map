# `CMWaterSubmersionManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 10 instance methods, 3 class methods

## Instance variables

```
^v _locationConnection;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"<CMWaterSubmersionManagerDelegate>" _delegate;
@"NSMeasurement" _maximumDepth;
```

## Properties

```
@property (T@"<CMWaterSubmersionManagerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSMeasurement",R,N,V_maximumDepth) maximumDepth;
```

## Class methods

```
+[CMWaterSubmersionManager authorizationStatus];
+[CMWaterSubmersionManager waterSubmersionAvailable];
+[CMWaterSubmersionManager isAuthorizedAndEntitled];
```

## Instance methods

```
-[CMWaterSubmersionManager _connect];
-[CMWaterSubmersionManager _setDelegate:];
-[CMWaterSubmersionManager _disconnect];
-[CMWaterSubmersionManager init];
-[CMWaterSubmersionManager dealloc];
-[CMWaterSubmersionManager setDelegate:];
-[CMWaterSubmersionManager _handleMessage:];
-[CMWaterSubmersionManager delegate];
-[CMWaterSubmersionManager maximumDepth];
-[CMWaterSubmersionManager notifySubmersionStateProcessingCompleted];
```
