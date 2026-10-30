# `DCCircularProgressView`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
d _progress;
@"NSProgress" _observedProgress;
@"CAShapeLayer" _circleLayer;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_circleLayer) circleLayer;
@property (Td,N,V_progress) progress;
@property (T@"NSProgress",&,N,V_observedProgress) observedProgress;
```

## Instance methods

```
-[DCCircularProgressView observeValueForKeyPath:ofObject:change:context:];
-[DCCircularProgressView setProgress:];
-[DCCircularProgressView dealloc];
-[DCCircularProgressView progress];
-[DCCircularProgressView awakeFromNib];
-[DCCircularProgressView observedProgress];
-[DCCircularProgressView setObservedProgress:];
-[DCCircularProgressView circleLayer];
-[DCCircularProgressView setCircleLayer:];
-[DCCircularProgressView newPathForProgress:];
```
