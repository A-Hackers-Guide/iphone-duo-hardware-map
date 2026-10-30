# `PKFadeOutStrokeAnimation`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UIColor" _startColor;
@"PKStroke" _stroke;
d _startTime;
d _duration;
```

## Properties

```
@property (T@"PKStroke",R,N,V_stroke) stroke;
@property (Td,R,N,V_startTime) startTime;
@property (Td,R,N,V_duration) duration;
```

## Instance methods

```
-[PKFadeOutStrokeAnimation startTime];
-[PKFadeOutStrokeAnimation duration];
-[PKFadeOutStrokeAnimation stroke];
-[PKFadeOutStrokeAnimation initWithStroke:startTime:duration:];
-[PKFadeOutStrokeAnimation isDoneAtTime:];
-[PKFadeOutStrokeAnimation newStrokeAtTime:];
```
