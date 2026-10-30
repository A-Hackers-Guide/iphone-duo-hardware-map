# `_SBRecordingIndicatorStreamState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 3 instance variables, 7 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _indicators;
@"NSArray" _boundingBoxes;
q _orientation;
```

## Properties

```
@property (T@"NSArray",C,N,V_indicators) indicators;
@property (T@"NSArray",C,N,V_boundingBoxes) boundingBoxes;
@property (Tq,N,V_orientation) orientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_SBRecordingIndicatorStreamState initialize];
```

## Instance methods

```
-[_SBRecordingIndicatorStreamState setOrientation:];
-[_SBRecordingIndicatorStreamState indicators];
-[_SBRecordingIndicatorStreamState boundingBoxes];
-[_SBRecordingIndicatorStreamState orientation];
-[_SBRecordingIndicatorStreamState membersForCoder];
-[_SBRecordingIndicatorStreamState setBoundingBoxes:];
-[_SBRecordingIndicatorStreamState initWithIndicators:boundingBoxes:orientation:];
-[_SBRecordingIndicatorStreamState setIndicators:];
```
