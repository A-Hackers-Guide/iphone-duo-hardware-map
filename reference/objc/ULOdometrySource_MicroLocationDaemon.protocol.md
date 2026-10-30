# `ULOdometrySource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 7 instance methods, 3 class methods

## Properties

```
@property (T@"<ULOdometryDelegate>",R,W,N) delegate;
@property (Tq,R,N) odometrySourceType;
```

## Class methods

```
+[ULOdometrySource new];
+[ULOdometrySource isBackgroundAvailable];
+[ULOdometrySource isNeuralPDRAvailable];
```

## Instance methods

```
-[ULOdometrySource init];
-[ULOdometrySource requestNPDRUpdate];
-[ULOdometrySource stopBackgroundUpdates];
-[ULOdometrySource delegate];
-[ULOdometrySource startBackgroundUpdates];
-[ULOdometrySource odometrySourceType];
-[ULOdometrySource initWithDelegateQueue:delegate:];
```
