# `ULAttitudeSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 1 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"<ULAttitudeDelegate>",R,W,N) delegate;
```

## Class methods

```
+[ULAttitudeSource isAvailable];
```

## Instance methods

```
-[ULAttitudeSource stopUpdates];
-[ULAttitudeSource delegate];
-[ULAttitudeSource startUpdates];
-[ULAttitudeSource initWithQueue:delegate:updateInterval:bufferDurationSeconds:];
```
