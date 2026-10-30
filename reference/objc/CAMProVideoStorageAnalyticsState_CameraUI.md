# `CAMProVideoStorageAnalyticsState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _hasRecordedState;
B _created;
q _initialCapacityBytes;
q _remainingCapacityBytes;
```

## Properties

```
@property (TB,R,N,V_hasRecordedState) hasRecordedState;
@property (TB,R,N,V_created) created;
@property (Tq,R,N,V_initialCapacityBytes) initialCapacityBytes;
@property (Tq,R,N,V_remainingCapacityBytes) remainingCapacityBytes;
```

## Class methods

```
+[CAMProVideoStorageAnalyticsState sharedInstance];
```

## Instance methods

```
-[CAMProVideoStorageAnalyticsState created];
-[CAMProVideoStorageAnalyticsState hasRecordedState];
-[CAMProVideoStorageAnalyticsState initialCapacityBytes];
-[CAMProVideoStorageAnalyticsState remainingCapacityBytes];
-[CAMProVideoStorageAnalyticsState updateWithCreated:initialCapacityBytes:remainingCapacityBytes:];
```
