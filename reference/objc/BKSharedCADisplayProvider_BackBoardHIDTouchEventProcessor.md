# `BKSharedCADisplayProvider`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKCADisplayProvider`
- 4 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_monitors;
@"NSMutableSet" _lock_observedDisplays;
B _isObserving;
```

## Properties

```
@property (T@"NSArray",R,C,N) displays;
@property (T@"CADisplay",R,N) mainDisplay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSharedCADisplayProvider sharedInstance];
```

## Instance methods

```
-[BKSharedCADisplayProvider observeValueForKeyPath:ofObject:change:context:];
-[BKSharedCADisplayProvider init];
-[BKSharedCADisplayProvider addMonitor:];
-[BKSharedCADisplayProvider invalidate];
-[BKSharedCADisplayProvider displays];
-[BKSharedCADisplayProvider removeMonitor:];
-[BKSharedCADisplayProvider mainDisplay];
-[BKSharedCADisplayProvider _lock_addObserversToDisplay:];
-[BKSharedCADisplayProvider _lock_removeObserversFromDisplay:];
-[BKSharedCADisplayProvider _lock_updateObservingState];
-[BKSharedCADisplayProvider _postImmutableDisplayToObservers:context:];
```
