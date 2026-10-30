# `BWStillImageTimeMachine`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _timeMachineMutex;
^^{opaqueCMSampleBuffer} _frames;
B _suspended;
i _capacity;
```

## Properties

```
@property (Ti,R,N,V_capacity) capacity;
```

## Class methods

```
+[BWStillImageTimeMachine initialize];
+[BWStillImageTimeMachine afComplete:];
```

## Instance methods

```
-[BWStillImageTimeMachine capacity];
-[BWStillImageTimeMachine dealloc];
-[BWStillImageTimeMachine initWithCapacity:];
-[BWStillImageTimeMachine drain];
-[BWStillImageTimeMachine resume];
-[BWStillImageTimeMachine suspendAndDrain];
-[BWStillImageTimeMachine copyBestFrame];
-[BWStillImageTimeMachine insertFrame:];
```
