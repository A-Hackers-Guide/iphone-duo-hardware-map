# `PKLiveStrokesParticlesAnimation`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _strokes;
d _startTime;
d _duration;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _destinationFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (Td,R,N,V_startTime) startTime;
@property (Td,R,N,V_duration) duration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_destinationFrame) destinationFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
```

## Instance methods

```
-[PKLiveStrokesParticlesAnimation startTime];
-[PKLiveStrokesParticlesAnimation duration];
-[PKLiveStrokesParticlesAnimation bounds];
-[PKLiveStrokesParticlesAnimation strokes];
-[PKLiveStrokesParticlesAnimation destinationFrame];
-[PKLiveStrokesParticlesAnimation _calculateBounds];
-[PKLiveStrokesParticlesAnimation initWithStrokes:startTime:duration:destinationFrame:];
-[PKLiveStrokesParticlesAnimation isDoneAtTime:];
```
