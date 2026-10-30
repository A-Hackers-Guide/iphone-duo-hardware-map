# `ULAltitudeSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 5 instance methods, 2 class methods

## Properties

```
@property (T@"<ULAltitudeDelegate>",R,W,N) delegate;
```

## Class methods

```
+[ULAltitudeSource isAvailable];
+[ULAltitudeSource new];
```

## Instance methods

```
-[ULAltitudeSource init];
-[ULAltitudeSource stopBackgroundUpdates];
-[ULAltitudeSource delegate];
-[ULAltitudeSource startBackgroundUpdates];
-[ULAltitudeSource initWithDelegateQueue:delegate:];
```
