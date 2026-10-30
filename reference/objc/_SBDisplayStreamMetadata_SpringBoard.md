# `_SBDisplayStreamMetadata`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 12 instance variables, 16 properties, 26 instance methods, 1 class methods

## Instance variables

```
I _displayID;
@"NSString" _nativeOrientation;
@"NSString" _currentOrientation;
d _scale;
d _nativeScale;
q _maximumFramesPerSecond;
d _timestamp;
d _targetTimestamp;
d _duration;
q _preferredFramesPerSecond;
d _currentFrameTime;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (TI,N,V_displayID) displayID;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_bounds) bounds;
@property (T@"NSString",C,N,V_nativeOrientation) nativeOrientation;
@property (T@"NSString",C,N,V_currentOrientation) currentOrientation;
@property (Td,N,V_scale) scale;
@property (Td,N,V_nativeScale) nativeScale;
@property (Tq,N,V_maximumFramesPerSecond) maximumFramesPerSecond;
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_targetTimestamp) targetTimestamp;
@property (Td,N,V_duration) duration;
@property (Tq,N,V_preferredFramesPerSecond) preferredFramesPerSecond;
@property (Td,N,V_currentFrameTime) currentFrameTime;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBDisplayStreamMetadata initialize];
```

## Instance methods

```
-[_SBDisplayStreamMetadata currentOrientation];
-[_SBDisplayStreamMetadata targetTimestamp];
-[_SBDisplayStreamMetadata setDisplayID:];
-[_SBDisplayStreamMetadata setTimestamp:];
-[_SBDisplayStreamMetadata nativeOrientation];
-[_SBDisplayStreamMetadata setTargetTimestamp:];
-[_SBDisplayStreamMetadata timestamp];
-[_SBDisplayStreamMetadata setScale:];
-[_SBDisplayStreamMetadata setPreferredFramesPerSecond:];
-[_SBDisplayStreamMetadata displayID];
-[_SBDisplayStreamMetadata setBounds:];
-[_SBDisplayStreamMetadata duration];
-[_SBDisplayStreamMetadata scale];
-[_SBDisplayStreamMetadata maximumFramesPerSecond];
-[_SBDisplayStreamMetadata preferredFramesPerSecond];
-[_SBDisplayStreamMetadata bounds];
-[_SBDisplayStreamMetadata setDuration:];
-[_SBDisplayStreamMetadata nativeScale];
-[_SBDisplayStreamMetadata membersForCoder];
-[_SBDisplayStreamMetadata setCurrentOrientation:];
-[_SBDisplayStreamMetadata setMaximumFramesPerSecond:];
-[_SBDisplayStreamMetadata currentFrameTime];
-[_SBDisplayStreamMetadata setCurrentFrameTime:];
-[_SBDisplayStreamMetadata setNativeScale:];
-[_SBDisplayStreamMetadata initWithDisplay:screen:displayLink:];
-[_SBDisplayStreamMetadata setNativeOrientation:];
```
