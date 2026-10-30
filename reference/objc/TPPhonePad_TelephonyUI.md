# `TPPhonePad`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI`](../userland/System__Library__PrivateFrameworks__TelephonyUI.framework__TelephonyUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `TPDialerKeypadProtocol`
- 15 instance variables, 4 properties, 41 instance methods, 3 class methods

## Instance variables

```
q _downKey;
q _highlightKey;
@"<TPDialerKeypadDelegate>" _delegate;
B _playsSounds;
d _topHeight;
d _midHeight;
d _bottomHeight;
d _leftWidth;
d _midWidth;
d _rightWidth;
^{__CFSet=} _inflightSounds;
^{__CFDictionary=} _keyToButtonMap;
I _incompleteSounds;
b1 _delegateSoundCallbacks;
b1 _soundsActivated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TPPhonePad _delayedDeactivate];
+[TPPhonePad launchFieldTestIfNeeded:];
+[TPPhonePad shouldStringAutoDial:givenLastChar:];
```

## Instance methods

```
-[TPPhonePad cancelTouchTracking];
-[TPPhonePad dealloc];
-[TPPhonePad drawRect:];
-[TPPhonePad hitTest:withEvent:];
-[TPPhonePad setDelegate:];
-[TPPhonePad setHighlighted:];
-[TPPhonePad removeFromSuperview];
-[TPPhonePad initWithFrame:];
-[TPPhonePad movedFromWindow:];
-[TPPhonePad movedToWindow:];
-[TPPhonePad pointMostlyInside:withEvent:];
-[TPPhonePad _buttonForKeyAtIndex:];
-[TPPhonePad _rectForKey:];
-[TPPhonePad _highlightedImage];
-[TPPhonePad _stopAllSoundsForcingCallbacks:];
-[TPPhonePad setPlaysSounds:];
-[TPPhonePad _yFudge];
-[TPPhonePad _activateSounds:];
-[TPPhonePad _appResumed];
-[TPPhonePad _appSuspended];
-[TPPhonePad _handleKey:forUIEvent:];
-[TPPhonePad _handleKeyPressAndHoldForDownKey:];
-[TPPhonePad _handleKeyPressAndHoldForHighlightedKey:];
-[TPPhonePad _handleKeyPressAndHoldForKey:];
-[TPPhonePad _imageByCroppingImage:toRect:];
-[TPPhonePad _keyForPoint:];
-[TPPhonePad _keypadImage];
-[TPPhonePad _keypadOrigin];
-[TPPhonePad _notifySoundCompletionIfNecessary:];
-[TPPhonePad _playSoundForKey:];
-[TPPhonePad _pressedImage];
-[TPPhonePad _stopSoundForKey:];
-[TPPhonePad _updateRect:withScale:];
-[TPPhonePad highlightKeyAtIndex:];
-[TPPhonePad indexForHighlightedKey];
-[TPPhonePad performTapActionCancelForHighlightedKey];
-[TPPhonePad performTapActionDownForHighlightedKey];
-[TPPhonePad performTapActionEndForHighlightedKey];
-[TPPhonePad reloadButtonImages];
-[TPPhonePad setButton:forKeyAtIndex:];
-[TPPhonePad setNeedsDisplayForKey:];
```
