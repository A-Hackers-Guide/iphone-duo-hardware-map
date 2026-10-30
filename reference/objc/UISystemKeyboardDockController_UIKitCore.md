# `UISystemKeyboardDockController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIKeyboardDockViewDelegate`
- 15 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _dictationHasUsedServerManualEndpointing;
B _dictationUsingServerManualEndpointing;
B _isSuppressingDockItemTouch;
@"UIKeyboardDockItem" _globeDockItem;
@"UIKeyboardDockItem" _dictationDockItem;
@"UIKeyboardDockItem" _dictationRunningDockItem;
@"UIKeyboardDockItem" _keyboardDockItem;
@"UIButton" _stopDictationButton;
@"NSDate" _dictationItemButtonTouchDownTime;
{CGPoint="x"d"y"d} _dictationItemButtonTouchDownLocationInView;
@"NSDate" _globeItemButtonTouchDownTime;
{CGPoint="x"d"y"d} _globeItemButtonTouchDownLocationInView;
@"NSBundle" _priorityGlyphBundle;
@"NSNumber" _lastLoggedDockMicState;
@"UIKeyboardDockView" _dockView;
```

## Properties

```
@property (T@"UIKeyboardDockView",&,N,V_dockView) dockView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISystemKeyboardDockController dockView];
-[UISystemKeyboardDockController updateRightButtonItemWithCustomAction:];
-[UISystemKeyboardDockController dealloc];
-[UISystemKeyboardDockController customDockItemWasTapped:withEvent:];
-[UISystemKeyboardDockController viewDidLoad];
-[UISystemKeyboardDockController keyboardItemButtonWasTapped:withEvent:];
-[UISystemKeyboardDockController setKeyboardDockItem];
-[UISystemKeyboardDockController _canShowWhileLocked];
-[UISystemKeyboardDockController loadView];
-[UISystemKeyboardDockController keyboardDockView:didPressDockItem:withEvent:];
-[UISystemKeyboardDockController configuredGlyphWithName:];
-[UISystemKeyboardDockController traitCollectionDidChange:];
-[UISystemKeyboardDockController updateDockItemsVisibility];
-[UISystemKeyboardDockController imageConfig];
-[UISystemKeyboardDockController updateDockItemsVisibilityWithCustomDictationAction:];
-[UISystemKeyboardDockController setDockView:];
-[UISystemKeyboardDockController globeItemButtonWasPressed:withEvent:];
-[UISystemKeyboardDockController _dictationDidBeginNotification:];
-[UISystemKeyboardDockController dictationItemButtonWasPressed:withEvent:isRunningButton:];
```
