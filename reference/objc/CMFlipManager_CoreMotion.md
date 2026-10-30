# `CMFlipManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 14 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Class methods

```
+[CMFlipManager isAvailable];
```

## Instance methods

```
-[CMFlipManager connect];
-[CMFlipManager dealloc];
-[CMFlipManager stopUpdates];
-[CMFlipManager deallocPrivate];
-[CMFlipManager initWithName:];
-[CMFlipManager feedFlipEvent:reason:timestamp:continuousTimestamp:];
-[CMFlipManager onDistributedNotification:];
-[CMFlipManager onFlipStateData:];
-[CMFlipManager sendEventToClientPrivate];
-[CMFlipManager sendServiceRequestPrivate];
-[CMFlipManager simulateFlipState:reason:];
-[CMFlipManager startUpdatesPrivateToQueue:withHandler:];
-[CMFlipManager startUpdatesToQueue:withHandler:];
-[CMFlipManager stopUpdatesPrivate];
```
