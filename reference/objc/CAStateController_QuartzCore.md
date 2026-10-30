# `CAStateController`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 18 instance methods, 0 class methods

## Instance variables

```
^{_CAStateControllerData=@^{__CFDictionary}@@} _data;
```

## Properties

```
@property (T@"CALayer",R) layer;
@property (T@"NSObject<CAStateControllerDelegate>",W) delegate;
```

## Instance methods

```
-[CAStateController layer];
-[CAStateController stateOfLayer:];
-[CAStateController setState:ofLayer:];
-[CAStateController removeAllStateChanges];
-[CAStateController dealloc];
-[CAStateController cancelTimers];
-[CAStateController _addAnimation:forKey:target:undo:];
-[CAStateController restoreStateChanges:];
-[CAStateController initWithLayer:];
-[CAStateController setInitialStatesOfLayer:];
-[CAStateController _applyTransition:layer:undo:speed:];
-[CAStateController _nextStateTimer:];
-[CAStateController setDelegate:];
-[CAStateController delegate];
-[CAStateController _applyTransitionElement:layer:undo:speed:];
-[CAStateController _removeTransition:layer:];
-[CAStateController setInitialStatesOfLayer:transitionSpeed:];
-[CAStateController setState:ofLayer:transitionSpeed:];
```
