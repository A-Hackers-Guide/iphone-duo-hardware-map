# `SBPressSequenceValidator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBPressSequenceSettings" _settings;
```

## Properties

```
@property (T@"SBPressSequenceSettings",R,N,V_settings) settings;
```

## Instance methods

```
-[SBPressSequenceValidator init];
-[SBPressSequenceValidator settings];
-[SBPressSequenceValidator initWithSettings:];
-[SBPressSequenceValidator _modeForDesiredIndex:isDownEvent:];
-[SBPressSequenceValidator _pressDownBoundsForDesiredIndex:sequence:];
-[SBPressSequenceValidator _pressUpBoundsForDesiredIndex:sequence:];
-[SBPressSequenceValidator pressEventIsValidInSequence:endingDownEvent:duration:];
-[SBPressSequenceValidator timeUntilNextPressEventIsInValidInSequence:lastPressEventInSequenceIsDown:];
```
